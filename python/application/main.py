# Project - Main file
import asyncio
import logging
import time

from modules.general import General
import socketio


def run_app():
    # Log format according to ISO8601.
    # Example: 2021-05-21T21:37:13+0200
    #          ^    ^  ^  ^  ^  ^  ^
    #          |    |  |  |  |  |  |
    #          |    |  |  |  |  |  ---- Timezone offset from UTC
    #          |    |  |  |  |  ------- Seconds starting from 0
    #          |    |  |  |  ---------- Minutes starting from 0
    #          |    |  |  ------------- Hours starting from 0
    #          |    |  ---------------- Days starting from 1
    #          |    ------------------- Month starting from 1
    #          ------------------------ Year
    logging.basicConfig(filename='application.log', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s', datefmt='%Y-%m-%dT%H:%M:%S%z')

    logging.info("Starting software...")

    hardware = None
    # Check if the system is a Raspberry Pi.
    if General.is_raspberrypi():
        logging.debug("System is a Raspberry Pi.")

        # Only import it here.
        # If you import it earlier, it will fail because the Adafruit libraries.
        from modules.hardware import Hardware
        hardware = Hardware()
    else:
        logging.debug("System is a PC.")

    logging.info("Software started.")

    sio = socketio.Client(
        reconnection=True,
        reconnection_attempts=float('Inf'),
        reconnection_delay=1,
        reconnection_delay_max=1,
        randomization_factor=0,
        logger=False,
        engineio_logger=False
    )

    sio.connect(url="http://localhost:8080")

    @sio.event
    def message(data):
        # print("I received a message!")
        pass

    @sio.event
    def connect():
        print("I'm connected!")

    @sio.event
    def connect_error(data):
        print("The connection failed!")

    @sio.event
    def disconnect():
        print("I'm disconnected!")

    while True:
        sio.emit("change window", {'window': 0})
        time.sleep(1)
        # print("Working...")
        sio.emit("change window", {'window': 1})
        time.sleep(1)
        # print("Working...")


if __name__ == '__main__':
    run_app()
