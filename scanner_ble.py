#!/usr/bin/env python

import asyncio
from asyncio.streams import StreamReaderProtocol
import sys
from bleak import BleakScanner, BleakClient, exc
from time import perf_counter

start_time = None
NAME_KEY = "FRENZ"
# Battery SoC
char_uuid   = '00002a19-0000-1000-8000-00805f9b34fb'
log_uuid    = '45420102-0000-ffff-ff45-415241424c45'

async def main():
    global start_time
    global recorded_data

    print('Searching for devices...')
    devices = await BleakScanner.discover()
    print('Please select a devcice or enter "q" key to exit:')
    for idx, d in enumerate(devices):
        # print(f'  {(idx+1):02d}. {d}')
        if (NAME_KEY in d.name):
            print(f'  {(idx+1):02d}. {d}')
        # else:
        #     print(f'  {(idx+1):02d}. (No name)')

    selection = None
    while selection is None:
        select = input('Enter the device number: ')
        if 'q' in select :
            return
        try:
            selection = int(select) - 1
            if selection >= len(devices):
                print('Selection out of range! Please try again')
                selection = None
        except:
            print('Could not parse input! Please try again')

    device = devices[selection]
    # print(device)
    # print(device.metadata)
    # print(device.details)

    # test: BluetoothLEAdvertisementReceivedEventArgs = None
    # device.pair()

    print(f'Connecting to "{ device.name or device.address }"...')
    async with BleakClient(device.address, timeout=30) as client:

        print('Connected! Getting services...')
        services = await client.get_services()
        # for service in services:
        #     print(f'  { service }')
        #     for characteristic in service.characteristics:
        #         print(f'    { characteristic }')

        data_read = await client.read_gatt_char(char_uuid)
        # print(data_read)
        data_int = int.from_bytes(data_read, byteorder='big')
        print(f"Battery capacity: {data_int} %")

        try:
            log_read = await client.read_gatt_char(log_uuid)
            log_int = int.from_bytes(log_read, byteorder='big')
            print(f"Log data: {log_int}")
            print(type(log_read))
        except exc.BleakError as e:
            print(f"Error reading characteristic: {e}")
        # log_int = int.from_bytes(log_read, byteorder='big')
        # print(f"Log data: {log_int} ")


asyncio.run(main())
