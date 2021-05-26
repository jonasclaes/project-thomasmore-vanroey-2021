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

    logging.info("Initializing WebSocket...")
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
    logging.info("WebSocket connected.")

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

    logging.info("Software started.")

    if hardware is not None:
        hardware._mpr121[1].threshold = 6

    while True:
        for i in range(0, 12):
            if hardware is not None:
                if hardware.get_capacitive_input(i):
                    print("Change to window " + str(i))
                    sio.emit("change window", {'window': i})
                time.sleep(0.1)
            else:
                print("Change to window " + str(i))
                sio.emit("change window", {'window': i})
                time.sleep(1)


if __name__ == '__main__':
    run_app()
