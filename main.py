#!/usr/bin/env python3
import click
import time
import threading
from playsound import playsound

def play_sound():
    while True:
        playsound("/home/nithin/college/play/py/pomo/sounds/notification.mp3")

def timer(c):
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
    

@click.command()
@click.option('-d','--duration',default=25,help='Duration of pomodoro',type=int)
@click.option('-n','name',prompt="Enter the user name",default="user",required=0)
#@click.option("-a","--auto",prompt="Do you need the timer to loop?", help="Infiinite pomodoro cycles")
def pomo(duration,name):
    duration=int(duration*60)
    timer(duration)
    click.echo(name)
        
        
if __name__ == "__main__":
    pomo()
