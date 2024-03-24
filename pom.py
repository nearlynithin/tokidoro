#!/usr/bin/env python3
import click
from rich import print
from rich.console import Console
from rich.layout import Layout
from rich.table import Table
from rich.panel import Panel
import time
from datetime import datetime
from pydub import AudioSegment
from pydub.playback import play
import json
import shutil

@click.group()
def cli():
    pass

now = datetime.now()
terminal_width=int(shutil.get_terminal_size().columns)
formatted_time=now.strftime("%I:%M %p")

audio_path="/home/nithin/college/play/py/pomo/sounds/notification.mp3"
def play_sound():
    for i in range(3):
        sound = AudioSegment.from_file(audio_path)
        play(sound)
    

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
    while True:
        for cycle in range(1, int(cycles) + 1):
            print("─"*int((terminal_width/2)-9),end='')
            print(f"[#ff85ed]Pomodoro Cycle:[/#ff85ed] {cycle}/{cycles}",end='')
            print("─"*int((terminal_width/2)-9))
            timer(duration * 60)
            if cycle < int(cycles):
                print("[#0ff0fc]Short Break![/#0ff0fc]")
                timer(short * 60)
                print("-"*(terminal_width-17),end='')
                print(f"Ended at {formatted_time}")
            else:
                print("[blue]Long Break !![/blue]")
                timer(long * 60)
        new=input("do you want to start over? : (y/n) ")
        if new=="n":
            break
        
@click.command()
def showconfig():
    config=load_config()
    console=Console()
    config_string = "\n".join([
    f"Pomodoro duration       : {config['d']}",
    f"Short break duration    : {config['s']}",
    f"Long break duration     : {config['l']}",
    f"Number of cycles        : {config['c']}"
 ])
    console.print("[bold white]Configuration:[/bold white]")
    console.print("┌" + "─" * (terminal_width-2) + "┐", style="blue")  
    for line in config_string.split('\n'):
        console.print(f"│ {line:<{terminal_width-4}} │", style="blue")
    console.print("└" + "─" * (terminal_width-2) + "┘", style="blue")
    
    
cli.add_command(start)
cli.add_command(configure)
cli.add_command(showconfig)
if __name__ == "__main__":
    cli()
