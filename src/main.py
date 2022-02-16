import random, string, click

@click.command()
@click.option("-c", default=16, 
              show_default=True, type=int, 
              help="Number of character in password")
def main(c):
  print("hi")
