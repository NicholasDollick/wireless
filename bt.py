import bluetooth as bt

def run_continuous_scan(running):
    count = 0
    while running:
        print('cycle\n')
        nearby_devices = bt.discover_devices(Lookup_names=True)
        for addr, name in nearby_devices:
            print("adr: ", addr)
            print("name: ", name)
        count+=1
        if count >= 10:
            return