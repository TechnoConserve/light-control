from time import sleep

from bibliopixel.layout import Strip
from bibliopixel.animation import BaseStripAnim, OffAnim
from bibliopixel.drivers.SPI import SPI
from bibliopixel.drivers.driver_base import ChannelOrder
from bibliopixel import colors


class StripTest(BaseStripAnim):
    def __init__(self, led, start=0, end=-1):
        # The base class MUST be initialized by calling super like this
        super(StripTest, self).__init__(led, start, end)
        # Create a color array to use in the animation
        self._colors = [colors.Red, colors.Orange, colors.Yellow, colors.Green, colors.Blue, colors.Indigo]

    def step(self, amt=1):
        # Fill the strip, with each sucessive color
        for i in range(self._led.numLEDs):
            self._led.set(i, self._colors[(self._step + i) % len(self._colors)])
        # Increment the internal step by the given amount
        self._step += amt
        sleep(0.1)


def init():
    # create driver for a 162 pixels
    driver = SPI(type='LPD8806', num=162, c_order=ChannelOrder.GRB, use_py_spi=True, dev='/dev/spidev0.0', SPISpeed=16)
    #driver = DriverLPD8806(162, c_order=ChannelOrder.GRB, use_py_spi=True, dev='/dev/spidev0.0', SPISpeed=16)
    led = Strip(driver)
    return led


def start_party():
    led = init()
    anim = StripTest(led)
    anim.run(fps=8, seconds=60)


def stop_party():
    led = init()
    anim = OffAnim(led)
    anim.run()


if __name__ == '__main__':
    start_party()
