import asyncio
from asyncio.streams import StreamReaderProtocol
import sys
from bleak import BleakScanner, BleakClient
from time import perf_counter

start_time = None
# Battery SoC
char_uuid = '00002a19-0000-1000-8000-00805f9b34fb'

async def main():
    global start_time
    global recorded_data

    print('Searching for devices...')
    devices = await BleakScanner.discover()
    print('Please select a devcice:')
    for idx, d in enumerate(devices):
        print(f'  {(idx+1):02d}. {d}')

    selection = None
    while selection is None:
        select = input('Enter the device number: ')
        try:
            selection = int(select) - 1
            if selection >= len(devices):
                print('Selection out of range! Please try again')
                selection = None
        except:
            print('Could not parse input! Please try again')

    device = devices[selection]
    print(device)
    print(device.metadata)
    print(device.details)

    # test: BluetoothLEAdvertisementReceivedEventArgs = None
    # device.pair()

    print(f'Connecting to "{ device.name or device.address }"...')
    async with BleakClient(device.address, timeout=30) as client:

        print('Connected! Getting services...')
        services = await client.get_services()
        for service in services:
            print(f'  { service }')
            for characteristic in service.characteristics:
                print(f'    { characteristic }')

        data_read = await client.read_gatt_char(char_uuid)
        # print(data_read)
        data_int = int.from_bytes(data_read, byteorder='big')
        print("Battery: ",data_int)

asyncio.run(main())
