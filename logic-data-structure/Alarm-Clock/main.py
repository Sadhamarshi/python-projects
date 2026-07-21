from alarm import Alarm


print("===== ALARM CLOCK =====")

alarm_time = input("Enter Alarm Time (HH:MM:SS): ")

alarm = Alarm(alarm_time)

alarm.start()