import sys, netifaces

if len(sys.argv) > 1 and sys.argv[1] == 'default':
    # get default gateway
    ip, iface = netifaces.gateways()['default'][netifaces.AF_INET]
    # get first addr from the default iface
    addrs = netifaces.ifaddresses(iface)[netifaces.AF_INET][0]['addr']
    print(addrs)
else:
    for ip,iface,default in netifaces.gateways()[netifaces.AF_INET]:
        print(netifaces.ifaddresses(iface)[netifaces.AF_INET][0]['addr'])