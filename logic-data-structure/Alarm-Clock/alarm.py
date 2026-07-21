from datetime import datetime
import time


class Alarm:

    def __init__(self, alarm_time):
        self.alarm_time = alarm_time

    def start(self):

        print(f"\nAlarm set for {self.alarm_time}")

        while True:

            current_time = datetime.now().strftime("%H:%M:%S")

            print(f"\rCurrent Time: {current_time}", end="")

            if current_time == self.alarm_time:
                print("\n\n⏰ Wake Up! Alarm Ringing!")
                break

            time.sleep(1)