#!/usr/bin/env python3

from datetime import datetime, time



def main():
    print("The Timer program")
    print()

    # start timer
    input("Press Enter to start...")
    start_time = datetime.now()
    x = start_time.strftime('%H:%M:%S.%f')
    print("Start time:", x)
    print()

    
    # stop timer
    input("Press Enter to stop...")    
    stop_time = datetime.now()
    y = stop_time.strftime('%H:%M:%S.%f')
    print("Stop time: ", y)
    print()

    # calculate elapsed time
    elapsed_time = stop_time - start_time
    days = elapsed_time.days
    minutes = elapsed_time.seconds // 60
    seconds = elapsed_time.seconds % 60
    microseconds = elapsed_time.microseconds
    hours = minutes // 60
    minutes = minutes % 60

    # create time object
    time_object = time(hours, minutes, seconds, microseconds)

    # display results
    print("ELAPSED TIME")
    if time_object.minute > 0:
        print("Hours/Minutes: ", time_object.hour,time_object.minute)
        print("Seconds: ", time_object.second, time_object.microsecond)
    elif time_object.minute <= 0:
        print("Seconds: ", time_object.second, ".", time_object.microsecond, sep="")
if __name__ == "__main__":
    main()

    
