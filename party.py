#!/usr/bin/python
from datetime import datetime
from random import randint, uniform

from bootstrap import *


def get_random_color_value():
    """
    Return a floating point value between 0 and 255, rounded to the
    nearest tenth place.
    :return: floating point value between 0 and 255.
    """
    return round(uniform(0, 255), 1)


def step_thru_colors():
    # setup colors to loop through for fade
    colors = [
        (get_random_color_value(), get_random_color_value(), get_random_color_value()),
        (get_random_color_value(), get_random_color_value(), get_random_color_value()),
        (get_random_color_value(), get_random_color_value(), get_random_color_value()),
        (get_random_color_value(), get_random_color_value(), get_random_color_value()),
    ]

    step = 0.01
    for c in range(4):
        r, g, b = colors[c]
        level = 0.01
        direction = step
        while level >= 0.0:
            led.fill(Color(r, g, b, level))
            led.update()
            if level >= 0.99:
                direction = -step
            level += direction

    led.all_off()


def do_the_wave():
    # sin wave animations
    anim = Wave(led, Color(randint(0, 255), randint(0, 255), randint(0, 255)), randint(1, 5))
    for i in range(led.lastIndex):
        anim.step()
        led.update()

    led.all_off()


def make_a_rainbow():
    # rolling rainbow
    anim = Rainbow(led)
    for i in range(384):
        anim.step()
        led.update()

    led.fillOff()


def even_rainbow():
    # evenly distributed rainbow
    anim = RainbowCycle(led)
    for i in range(768):
        anim.step()
        led.update()

    led.fillOff()


def color_chase():
    colors = [
        Color(randint(100, 255), 0, 0),
        Color(0, randint(100, 255), 0),
        Color(0, 0, randint(100, 255)),
        Color(randint(200, 255), randint(200, 255), randint(200, 255)),
    ]

    for c in range(4):
        anim = ColorChase(led, colors[c])

        for i in range(num):
            anim.step()
            led.update()

    led.fillOff()


def color_wipe():
    colors = [
        Color(randint(100, 255), 0, 0),
        Color(0, randint(100, 255), 0),
        Color(0, 0, randint(100, 255)),
        Color(randint(200, 255), randint(200, 255), randint(200, 255)),
    ]

    for c in range(4):
        anim = ColorWipe(led, colors[c])

        for i in range(num):
            anim.step()
            led.update()
        # sleep(0.03)

    led.fillOff()


def larson_rainbow():
    anim = LarsonRainbow(led, 2, 0.5)
    for i in range(led.lastIndex * 4):
        anim.step()
        led.update()

    led.all_off()


def larson_scanner():
    # scanner: single color and changing color
    anim = LarsonScanner(led, Color(randint(150, 255), 0, 0))
    for i in range(led.lastIndex * 4):
        anim.step()
        led.update()
    # sleep(0.03)

    led.fillOff()


def random_anim():
    anims = {
        0: step_thru_colors,
        1: do_the_wave,
        2: make_a_rainbow,
        3: even_rainbow,
        4: color_chase,
        5: color_wipe,
        6: larson_rainbow,
        7: larson_scanner,
    }
    return anims[randint(0, len(anims))]


def main():
    # Lower the brightness at night
    if datetime.now().hour > 21:
        led.setMasterBrightness(0.5)

    anim = random_anim()
    anim()


main()
