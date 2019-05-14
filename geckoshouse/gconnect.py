import network
import ujson


def key():
    with open("key.json", "r") as read_file:
        k = ujson.load(read_file)
    return k.ssid, k.pswd


def do_connect():
    lan = network.WLAN(network.STA_IF)
    lan.active(True)
    if not lan.isconnected():
        print('connecting to network...')
        lan.connect('AG45', 'fortyfive')
        while not lan.isconnected():
            pass
    print('network config:', lan.ifconfig())
    print('connected is ', lan.isconnected())


if __name__ == '__main__':
    do_connect()
