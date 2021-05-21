# Project - Main file
import logging
from modules.example import ExampleModule


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

    # Do stuff here.
    example_module = ExampleModule()     # Initialize a new instance of example modules

    logging.info("Software started.")


if __name__ == '__main__':
    run_app()
