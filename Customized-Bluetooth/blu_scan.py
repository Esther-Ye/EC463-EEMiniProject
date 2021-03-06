#!/usr/bin/env python3
"""
Example of scanning Bluetooth Low Energy (BLE) devices.
Requires a Linux computer due to gattlib underlying BLE scanning requiring Glib.
"""

# 09/15/2021 added date-time
from datetime import datetime

#testing git

import argparse
from bluetooth.ble import DiscoveryService

p = argparse.ArgumentParser(description="BLE scanner")
p.add_argument(
    "timeout",
    help="number of seconds to scan for BLE devices",
    nargs="?",
    type=int,
    default=5,
)
P = p.parse_args()

timeout = P.timeout

for x in range(5):
    print(f"Scanning BLE devices for {timeout} seconds")
    svc = DiscoveryService()
    ble_devs = svc.discover(timeout)

# 09/15/21 formatting print output
    for u, n in ble_devs.items():
        print(u, n, datetime.now().strftime("%Y-%m-%dT%H:%M:%S"))


