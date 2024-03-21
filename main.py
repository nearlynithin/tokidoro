import click


@click.command()
@click.option("--name", prompt="Enter your name", help="The name of the user")
def hello(name):
    click.echo(f"Hello {name}!")

DURATION={
    "n": "Normal",
    "p": "Pro",
    "c":"Custom"
}

@click.command
@click.argument("duration",type=click.Choice(DURATION.keys()), default="n")
@click.option("-a","--auto",prompt="Do you need the timer to loop?", help="Infiinite pomodoro cycles")
def pomo(duration, autostart, cycle):
    pass
if __name__ == "__main__":
    hello()
