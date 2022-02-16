import os, random, string, click

@click.command()
@click.option("-f", "--file", type=str, help="write passwords to file")
@click.option("-no", "--no-output", type=bool, is_flag=True, help="no output")
@click.option("-l", "--length", default=16, show_default=True, type=int, help="length of password")
@click.option("-c", "--count", default=1, show_default=True, type=int, help="number of generated passwords")
@click.option("-nl", "--no-lower", type=bool, help="no lower case character", is_flag=True)
@click.option("-nu", "--no-upper", type=bool, help="no upper case character", is_flag=True)
@click.option("-nn", "--no-num", type=bool, help="no numbers", is_flag=True)
@click.option("-ns", "--no-symbols", type=bool, help="no symbols", is_flag=True)
def main(file, no_output, count, length, no_lower, no_upper, no_num, no_symbols):
  lower = string.ascii_lowercase
  upper = string.ascii_uppercase
  num = string.digits
  symbols = string.punctuation
  
  chars = ""
  
  if no_lower == False: chars += lower
  if no_upper == False: chars += upper
  if no_num == False: chars += num
  if no_symbols == False: chars += symbols
  
  if len(chars) == 0: chars += lower
  
  if int(count) > 1:
    if file: f = open(file, "a")
    for i in range(count):
      password = "".join(random.sample(chars, length))
      if no_output == False: click.echo(password)
      
      if file: f.write(password + "\n")
    if file: f.close()
      
  elif int(count) == 1:
    password = "".join(random.sample(chars, length))
    if no_output == False: click.echo(password)
    if file:
      with open(file, "a") as f:
        f.write(password + "\n")
        f.close()
