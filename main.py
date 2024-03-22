#!/usr/bin/env python3
import click
import time
from playsound import playsound

@click.group()
def cli():
    pass

def play_sound():
    for i in range(4):
        playsound("/home/nithin/college/play/py/pomo/sounds/notification.mp3")

def timer(c):
    while c > 0:
        m, s = divmod(c, 60)
        timer_str = "{:02d}:{:02d}".format(int(m), int(s))
        print(timer_str, end="\r")
        time.sleep(1)
        c -= 1
    click.echo('Time UP!')
    play_sound()

@click.command()
@click.option('-d', '--duration',default=25,help='Duration of pomodoro in minutes', type=float)
@click.option('-s','--short',default=5,help='Duraton of short break',type=float)
@click.option('-l','--long',default=15,help='Duraton of short break',type=float)
@click.option('-c','--cycle',default=4,help='Cycles of pomodoro',type=float)
def start(duration,short,long,cycle):
    pomo=1
    while(cycle>1):
            if duration:
                duration_seconds = int(duration * 60)
                print('Pomodoro %d\n'%pomo,end="\r")
                pomo+=1
                timer(duration_seconds)
            if short:
                duration_seconds = int(short * 60)
                print('Short Break!\n',end="\r")
                timer(duration_seconds)
            cycle-=1
    if duration:
        print('Pomodoro %d\n'%pomo,end="\r")
        duration_seconds = int(duration * 60)
        timer(duration_seconds)
    if long:
      print("Long break!")
      duration_seconds = int(short * 60)
      timer(duration_seconds)
                

cli.add_command(start)
if __name__ == "__main__":
    cli()
