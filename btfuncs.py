import bluetooth as bt
# from bluetooth.bluez import discover_devices


def get_scan_data(cycles=4):
    discovered = []
    for count in range(cycles):
        print('Scan'+str(count)+'\n')
        nearby_devices = bt.discover_devices(lookup_names=True)
        for addr, name in nearby_devices:
            if addr not in dict(discovered):
                discovered.append((addr, name))
                # print("adr: ", addr)
                # print("name: ", name)
    print("Scans finsished.")
    return discovered


def run_scan():
    print("Single scan...")
    nearby_devices = bt.discover_devices(lookup_names=True)
    discovered = []
    for addr, name in nearby_devices:
        discovered.append((addr, name))
        # print("adr: ", addr)
        # print("name: ", name)
    print("Scan finished.")
    return discovered
