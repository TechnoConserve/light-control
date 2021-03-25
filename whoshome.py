#!/usr/bin/python3

import bluetooth
import datetime
import signal
import subprocess
import time

start = datetime.time(7, 00)
end = datetime.time(22, 30)


class GracefulKiller:
    kill_now = False

    def __init__(self):
        signal.signal(signal.SIGINT, self.exit_gracefully)
        signal.signal(signal.SIGTERM, self.exit_gracefully)

    def exit_gracefully(self, signum, frame):
        self.kill_now = True


if __name__ == '__main__':
    killer = GracefulKiller()
    while True:
        now = datetime.datetime.now().time()
        print("The time is: " + str(now))

        if start <= now <= end:
            if killer.kill_now:
                break
            print("Checking if my master is within range...")
            try:
                result = bluetooth.lookup_name('58:cb:52:05:42:be', timeout=5)
                print("Result: ", result)

                if result is not None:
                    print("...he's here...Muahahahahaha")
                    subprocess.run(['/home/pi/light-control/party.py'], cwd='/home/pi/RPi-LPD8806')
                else:
                    print("No one home. A pity.")
                    time.sleep(10)

            except bluetooth.btcommon.BluetoothError as error:
                print("Could not connect: {}. Retrying in 30 seconds.".format(error))
                time.sleep(30)

        else:
            time.sleep(10)

    print("Script killed gracefully.")
