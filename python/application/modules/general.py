import io
import os


class General:
    @staticmethod
    def is_raspberrypi():
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

                        if value not in (
                            'BCM2708',
                            'BCM2709',
                            'BCM2835',
                            'BCM2836'
                        ):
                            return False
        except IOError:
            raise ValueError('Unable to open `/proc/cpuinfo`.')
