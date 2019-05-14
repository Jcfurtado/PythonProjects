from time import sleep

from umqtt.simple import MQTTClient

from .gdht import d_one, d_two
from .glamp import state_lamp


def data_pub(server="192.168.0.102"):
    c = MQTTClient("umqtt_client", server)
    c.connect()
    # hot side
    temp1, humid1 = d_one()
    # cold side
    temp2, humid2 = d_two()
    # Measurements
    all_measurements = [temp1, humid1, temp2, humid2]
    while True:
        for measurement in all_measurements:
            c.publish(b"tempone", "Temp: {}°C\nHumid: {}%\n".format(*all_measurements).encode("utf-8"))
            c.publish(b"tempone", "Light: {}".format(list(state_lamp())).encode("utf-8"))
            sleep(2)
        c.disconnect()
