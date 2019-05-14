import ujson


def w_dht(area, temp, humid):
    dht_json = {
        "dht":
            {
                "area": area,
                "temperature": temp,
                "humidity": humid
            },

    }
    with open("gdht.json", "w") as write_file:
        ujson.dump(dht_json, write_file)


def r_dht():
    with open("gdht.json", "r") as read_file:
        measurement = ujson.load(read_file)
    return measurement


def w_lamp(uv, uva, rgb, day, night):
    lamp_json = {
        "lamps": {
            "uv": uv,
            "uva": uva,
            "led": rgb,
            "h_day": day,
            "h_night": night
        }
    }
    with open("glamp.json", "w") as write_file:
        ujson.dump(lamp_json, write_file)


def r_lamp():
    with open("glamp.json", "r") as read_file:
        lamps = ujson.load(read_file)
    return lamps
