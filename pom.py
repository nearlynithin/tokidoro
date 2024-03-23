#!/usr/bin/env python3
import click
import time
from datetime import datetime
from playsound import playsound
from rich import print
import json


@click.group()
def cli():
    pass

now = datetime.now()
formatted_time=now.strftime("%I:%M %p")
def play_sound():
    for i in range(3):
        playsound("/home/nithin/college/play/py/pomo/sounds/notification.mp3")

def load_config():
    try:
        with open("config.json","r") as f:
            return json.load(f)
    except FileNotFoundError:
        return None

def save_config(config):
    with open("config.json","w") as f:
        json.dump(config,f)

def timer(duration):
    while duration > 0:
        m, s = divmod(duration, 60)
        timer_str = "{:02d}:{:02d}".format(int(m), int(s))
        print(timer_str,end='\r')
        time.sleep(1)
        duration -= 1
    play_sound()

@click.command()
@click.option('-d',prompt='Enter the duration of the pomodoro ',type=float)
@click.option('-s',prompt='Enter the duration of short break',type=float)
@click.option('-l',prompt='Enter the duration of the long break',type=float)
@click.option('-c',prompt='Enter the number of cycles',type=float)
def configure(d,s,l,c):
    config = load_config() or {"d":25,"s":5,"l":15,"c":4}
    if d:
        config["d"]=d
    if s:
        config["s"]=s
    if l:
        config["l"]=l
    if c:
        config["c"]=c
    save_config(config)
    print("Configuration saved successfully")



@cli.command()
@click.option('-d', '--duration',default=None, help='Duration of pomodoro in minutes', type=float)
@click.option('-s', '--short',default=None, help='Duration of short break in minutes', type=float)
@click.option('-l', '--long',default=None, help='Duration of long break in minutes', type=float)
@click.option('-c', '--cycles',default=None, help='Number of pomodoro cycles')
def start(duration, short, long, cycles):
    config=load_config() or {"d":25, "s":5,"l":15,"c":4}
    if duration is None:
        duration=int(config["d"])
    if short is None:
        short=int(config["s"])
    if long is None:
        long=int(config["l"])
    if cycles is None:
        cycles=int(config["c"])
    for cycle in range(1, int(cycles) + 1):
        print(f"[#ff85ed]Pomodoro Cycle:[/#ff85ed] {cycle}/{cycles}")
        timer(duration * 60)
        if cycle < int(cycles):
            print("[#0ff0fc]Short Break![/#0ff0fc]")
            timer(short * 60)
            print("-"*120,end='')
            print(f"Ended at {formatted_time}")
        else:
            print("[blue]Long Break !![/blue]")
            timer(long * 60)


cli.add_command(start)
cli.add_command(configure)
if __name__ == "__main__":
    cli()
