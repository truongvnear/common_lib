#!/usr/bin/env python

import serial.tools.list_ports

def find_com_ports():
    ports = serial.tools.list_ports.comports()
    com_ports = []
    for port in ports:
        com_ports.append(port)
        
    return com_ports

# Gọi hàm để tìm các cổng COM
com_ports = find_com_ports()

# In danh sách các cổng COM đã tìm thấy
if com_ports:
    print("PID", "DESCRIPTION", sep="\t")
    print("--------------------------------------")
    for port in com_ports:
        
        print(port.pid, port.description, sep="\t")
else:
    print("Không tìm thấy cổng COM nào.")
