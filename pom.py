#!/usr/bin/env python3
import click
import time
from datetime import datetime
import threading
from playsound import playsound
from rich import print

@click.group()
def cli():
    pass

now = datetime.now()
formatted_time=now.strftime("%I:%M %p")
def play_sound():
    playsound("/home/nithin/college/play/py/pomo/sounds/notification.mp3")

def timer(duration):
    while duration > 0:
        m, s = divmod(duration, 60)
        timer_str = "{:02d}:{:02d}".format(int(m), int(s))
        print(timer_str,end='\r')
        #click.echo("Time Remaining: " + timer_str, nl=False)
        time.sleep(1)
        duration -= 1
    play_sound()

@cli.command()
@click.option('-d', '--duration', default=25.0, help='Duration of pomodoro in minutes', type=float)
@click.option('-s', '--short', default=5.0, help='Duration of short break in minutes', type=float)
@click.option('-l', '--long', default=15.0, help='Duration of long break in minutes', type=float)
@click.option('-c', '--cycles', default=4, help='Number of pomodoro cycles')
def start(duration, short, long, cycles):
    for cycle in range(1, cycles + 1):
        print(f"[#ff85ed]Pomodoro Cycle:[/#ff85ed] {cycle}/{cycles}")
        timer(duration * 60)
        if cycle < cycles:
            print("[#0ff0fc]Short Break![/#0ff0fc]")
            timer(short * 60)
            print(f"Ended at {formatted_time}")
        else:
            print("[blue]Long Break !![/blue]")
            timer(long * 60)

if __name__ == "__main__":
    cli()
