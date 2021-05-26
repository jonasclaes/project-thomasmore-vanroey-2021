import io
import os
import logging


class General:
    @staticmethod
    def is_raspberrypi():
        logging.debug('System is running on: ' + str(os.name))
        if os.name != "posix":
            return False

        try:
            with io.open('/proc/cpuinfo', 'r') as cpuinfo:
                found = False
                for line in cpuinfo:
                    if line.startswith('Hardware'):
                        found = True
                        label, value = line.strip().split(':', 1)
                        value = value.strip()

                        logging.debug("System chip is a: " + value)

                        if value not in (
                            'BCM2708',
                            'BCM2709',
                            'BCM2835',
                            'BCM2836',
                            'BCM2837',
                            'BCM2711'
                        ):
                            return False
                        else:
                            return True
        except IOError:
            raise ValueError('Unable to open `/proc/cpuinfo`.')
