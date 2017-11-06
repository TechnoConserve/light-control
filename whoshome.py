#!/usr/bin/python3

import bluetooth
import time
import datetime

import party

start = datetime.time(7, 00)
end = datetime.time(21, 30)
partytime = False

while True:
    now = datetime.datetime.now().time()
    print("The time is: " + str(now))

    if start <= now <= end or partytime:
        print("Checking if my master is within range...")
        try:
            result = bluetooth.lookup_name('24:4B:81:1F:33:E4', timeout=5)
            print("Result: ", result)

            if result is not None or partytime:
                print ("...he's here...Muahahahahaha")
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
