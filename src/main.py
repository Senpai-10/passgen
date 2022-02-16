import click

@click.command()
@click.option("-c", default=16, help="Number of character in password")
def main(c):
  print(c)