from time import sleep

from .gled import clear, cock_shut, cockcrow, overnight


def morning():
    cockcrow()
    print("\n Cockcrow!! ON!")
    sleep(300)
    clear()
    print("\n Cockcrow!!! OFF!")


def evening():
    from time import sleep
    cock_shut()
    print("\n Cockshut, ON!")
    sleep(300)
    clear()
    print("\n Cockshut, OFF!")


def light_ctrl():
    if KEY == 'cockcrow':  # wawr LED
        morning()
    elif KEY == 'day':  # day lights
        day_ctrl()
    elif KEY == 'cockshut':  # cockshut LED
        cock_shut()
    elif KEY == 'overnight':  # night lights
        night_ctrl()
    else:
        print('error... esp_light_controller')

'''
def day_ctrl():  # control day lamps
    if lpd_hot_day == 'cold_day':  # day heat lamp
        lpd_day.on()
        return print("\n Heat lamp, ON!")
    elif lpd_hot_day == 'hot_day':
        lpd_day.off()
        return print("\n Heat lamp, OFF!")
    elif uv_on == 'rooster':  # UV light
        lpd_uv.on()
        return print("\n UV, ON!")
    elif uv_off == 'rooster':
        lpd_uv.off()
        return print("\n UV, OFF!")
    elif uva_on == 'rooster':  # UVA-B light
        lpd_uva.on()
        return print("\n UVA-B, ON!")
    elif uva_off == 'rooster':
        lpd_uva.off()
        return print("\n UVA-B, OFF!")
    else:
        print('error... esp_day_controller')


def night_ctrl():  # control overnight lights
    if hot_night == 'cold_night':  # heat lamp night
        lpd_night.on()
        return print("\n Overnight heat lamp, ON!")
    elif hot_night == 'hot_night':
        lpd_night.off()
        print("\n Overnight heat lamp, OFF!")
        overnight()  # overnight LED
        print("\n Overnight LED light, ON!")
    else:
        clear()
        print("\n Overnight LED light, OFF!")
'''
