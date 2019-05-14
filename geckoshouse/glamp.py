from machine import Pin


def state_lamp():
    lpd_uv = Pin(5, Pin.OUT, Pin.PULL_UP)  # (D1) UV light
    lpd_uva = Pin(5, Pin.OUT, Pin.PULL_UP)  # (D1) UVA-B light
    led_rgb = Pin(5, Pin.OUT, Pin.PULL_UP)  # (D1) RGB LED overnight
    lpd_day = Pin(5, Pin.OUT, Pin.PULL_UP)  # (D1) day heat lamp
    lpd_night = Pin(5, Pin.OUT, Pin.PULL_UP)  # (D1) night heat lamp

    uv = lpd_uv.value()
    uva = lpd_uva.value()
    rgb = led_rgb.value()
    day = lpd_day.value()
    night = lpd_night.value()
    return uv, uva, rgb, day, night
