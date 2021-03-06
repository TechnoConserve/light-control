#!/usr/bin/python3
import json
from random import randint

from bibliopixel.layout import Strip
from bibliopixel.animation import OffAnim
from bibliopixel.drivers.SPI.LPD8806 import LPD8806
from BiblioPixelAnimations.strip.Alternates import Alternates
from BiblioPixelAnimations.strip.ColorChase import ColorChase
from BiblioPixelAnimations.strip.ColorFade import ColorFade


def init():
    # create driver for a 162 pixels
    driver = LPD8806(num=162)
    led = Strip(driver)
    return led


def get_anim(led):
    color1, color2 = get_colors()
    choice = randint(0, 2)
    if choice == 0:
        anim = Alternates(led, max_led=162, color1=color1, color2=color2)
    if choice == 1:
        anim = ColorChase(led, color=color1)
    if choice == 2:
        anim = ColorFade(led, colors=[color1, color2])
    return anim


def get_colors():
    with open('custom_colors') as f:
        data = json.load(f)
        color1 = data["color1"]
        color2 = data["color2"]
    return color1, color2


def start_party():
    led = init()
    anim = get_anim(led)
    anim.run(seconds=30)


def stop_party():
    led = init()
    anim = OffAnim(led)
    anim.run(seconds=5)


if __name__ == '__main__':
    try:
        while True:
            start_party()
    except KeyboardInterrupt:
        stop_party()
