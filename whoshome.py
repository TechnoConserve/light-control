#!/usr/bin/python3

import bluetooth
import datetime
import json
import signal
import time

import party

start = datetime.time(7, 00)
end = datetime.time(21, 30)


class GracefulKiller:
    kill_now = False

    def __init__(self):
        signal.signal(signal.SIGINT, self.exit_gracefully)
        signal.signal(signal.SIGTERM, self.exit_gracefully)

    def exit_gracefully(self, signum, frame):
        self.kill_now = True


def get_party_time():
    with open('party.json') as f:
        data = json.load(f)
        party_value = data['party']
    return party_value


if __name__ == '__main__':
    killer = GracefulKiller()
    while True:
        now = datetime.datetime.now().time()
        print("The time is: " + str(now))
        partytime = get_party_time()

        if start <= now <= end or partytime:
            if killer.kill_now:
                break
            print("Checking if my master is within range...")
            try:
                result = bluetooth.lookup_name('24:4B:81:1F:33:E4', timeout=5)
                print("Result: ", result)

                if result is not None or partytime:
                    print("...he's here...Muahahahahaha")
                    party.start_party()
                else:
                    print("No one home. A pity.")
                    party.stop_party()
                    time.sleep(10)

            except bluetooth.btcommon.BluetoothError as error:
                print("Could not connect: {}. Retrying in 30 seconds.".format(error))
                time.sleep(30)

        else:
            party.stop_party()
            time.sleep(10)

    party.stop_party()
    print("Script killed gracefully.")
