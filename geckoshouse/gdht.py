from time import sleep

import dht
from machine import Pin


def d_one():  # ( Sensor DHT hot side)
    sensor = dht.DHT22(Pin(4, Pin.IN, Pin.PULL_UP))
    sensor.measure()
    temp = sensor.temperature()  # eg. 30.6 (°C)
    humid = sensor.humidity()  # eg. 25.3 (% RH)
    area = "hot"
    return area, temp, humid


def d_two():  # ( Sensor DHT cold side)
    sensor = dht.DHT22(Pin(4, Pin.IN, Pin.PULL_UP))
    sensor.measure()
    temp = sensor.temperature()  # eg. 30.6 (°C)
    humid = sensor.humidity()  # eg. 25.3 (% RH)
    area = "cold"
    return area, temp, humid


def d_main():
    while True:
        d_one()
        d_two()
        sleep(2)


if __name__ == '__main__':
    d_main()
