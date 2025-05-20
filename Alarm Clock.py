import time
import datetime
import os
def alarm_clock():
    alarm_time = input("Set the alarm (HH:MM, 24-hour format): ")
    print(f'The alarm set for {alarm_time}.waiting....')
    while True:
        current_time = datetime.datetime.now().strftime("%H:%M")
        if current_time == alarm_time:
            print("\n⏰⏰⏰ WAKE UP! It's", current_time)
            try:
                for i in range(5):
                    print('/a')
                    time.sleep(1)
            except:
                print("Beep not suppoted in this system")
            break
        time.sleep(1)
alarm_clock()
