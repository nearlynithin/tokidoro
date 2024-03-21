import time
import sys
from playsound import playsound
import threading


def play_sound():
    while True:
        playsound("/home/nithin/college/play/py/pomo/sounds/notification.mp3")


def pomo(c):
    sound_thread = threading.Thread(target=play_sound)
    sound_thread.daemon = True

    while c > 0:
        m, s = divmod(c, 60)
        timer = "{:02d}:{:02d}".format(int(m), int(s))
        print(timer, end="\r")
        time.sleep(1)
        c = c - 1
    sound_thread.start()
    key = input("Enter any key : ")


if __name__ == "__main__":
    args = sys.argv[1:]
    if args:
        function_name = args[0]
        if function_name == pomo.__name__:
            if len(args) >= 2:
                try:
                    c = float(args[1])
                    c = int(c * 60)  # Convert minutes to seconds
                    pomo(c)
                except ValueError:
                    print("Invalid argument. Please provide a numeric value for time.")
            else:
                print("Usage: python script.py pomo <minutes>")
        else:
            print("Function not found.")
    else:
        print("Usage: python script.py <function_name>")
