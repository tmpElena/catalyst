import click
import os

from flowform.run import runCommand

@click.group()
def main():
    pass


@main.command(name='run')
@click.option('--file', default='demo.yaml', help='the script file you want to run')
def run(file):
    currentFileDir = os.path.abspath(file)
    runCommand(currentFileDir)


if __name__ == "__main__":
    main()
