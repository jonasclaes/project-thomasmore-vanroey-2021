import logging
import board
import busio
import adafruit_mpr121


class Hardware:
    _bus_i2c = None
    _mpr121 = None

    def __init__(self, mpr121_address=adafruit_mpr121.MPR121_I2CADDR_DEFAULT):
        logging.debug("Initializing hardware...")

        # Setup the I2C bus.
        self._bus_i2c = busio.I2C(board.SCL, board.SDA)
        logging.debug("Initialized I2C.")

        # Setup the MPR121 library for use.
        self._mpr121 = adafruit_mpr121.MPR121(self._bus_i2c, mpr121_address)
        logging.debug("Initialized Adafruit MPR121.")
        logging.info("Initialized hardware.")

    def get_capacitive_input(self, input_number: int):
        return self._mpr121[input_number]
