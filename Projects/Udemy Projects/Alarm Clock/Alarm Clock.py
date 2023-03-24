from datetime import datetime
from pygame import mixer


def valid_alarm_time():
    while True:
        alarm = input("Set alarm in format HH:MM:SS AM/PM:\t")
        if alarm[:8].isalpha():
            print("FORMAT ERROR - Time must be entere as numbers e.g. 12:30:00 PM")
        elif len(alarm) != 11:
            print("FORMAT ERROR - Time must be entered as HH:MM:SS AM/PM e.g. 12:30:00 PM")
        else:
            # Hour <= 12
            if int(alarm[:2]) > 12:
                print("FORMAT ERROR - Hours cannot be greater than 12")
            # Minute <= 59
            elif int(alarm[3:5]) > 59:
                print("FORMAT ERROR - Minutes cannot be greater than 59")
            # Seconds <= 59
            elif int(alarm[6:8]) > 59:
                print("FORMAT ERROR - Seconds cannot be greater than 59")
            else:
                print(f"Thank you. Alarm set for {alarm}")
                return alarm


def set_alarm():
    mixer.init()
    mixer.music.load("/Projects/Udemy Projects/Alarm Clock/Sunny Rasta - ALARM 1.wav")
    alarm = valid_alarm_time()
    alarm_hour = alarm[:2]
    alarm_min = alarm[3:5]
    alarm_sec = alarm[6:8]
    alarm_period = alarm[9:].upper()

    while True:
        now = datetime.now()
        current_hour = now.strftime("%I")
        current_min = now.strftime("%M")
        current_sec = now.strftime("%S")
        current_period = now.strftime("%p")

        if alarm_period == current_period:
            if alarm_hour == current_hour:
                if alarm_min == current_min:
                    if alarm_sec == current_sec:
                        break

    print("Alarm")
    mixer.music.play()
    stop = input("Enter x to stop alarm:\t")
    while True:
        if stop.lower() == "x":
            mixer.music.stop()
            break


set_alarm()




