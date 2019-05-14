from machine import Pin
from neopixel import NeoPixel

# --- rgb led --- #
# the number 12 is number of led
rgb_led = NeoPixel(Pin(5), 12)  # (D1) overnight RGB LED
lpd_uv = Pin(5, Pin.OUT, Pin.PULL_UP)  # (D1) UV light
lpd_uva = Pin(5, Pin.OUT, Pin.PULL_UP)  # (D1) UVA-B light
lpd_day = Pin(5, Pin.OUT, Pin.PULL_UP)  # (D1) day heat lamp
lpd_night = Pin(5, Pin.OUT, Pin.PULL_UP)  # (D1) night heat lamp


def clear():
    for i in range(12):
        rgb_led[i] = (0, 0, 0)
        rgb_led.write()


def cockcrow():
    sunrise = 64, 35, 0
    for i in range(4 * 12):
        for j in range(12):
            rgb_led[j] = sunrise
        rgb_led.write()


def cock_shut():
    sunset = 128, 88, 0
    for i in range(4 * 12):
        for j in range(12):
            rgb_led[j] = sunset
        rgb_led.write()


def overnight():
    night = 15, 0, 45
    for i in range(4 * 12):
        for j in range(12):
            rgb_led[j] = night
        rgb_led.write()
