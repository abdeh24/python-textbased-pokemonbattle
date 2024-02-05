import random


class createAv:
  def __init__(self, name, gender, pkmn):
    self.name = name
    self.gender = gender
    self.pkmn = pkmn

def start():
  name = input("Hello! What's your name?: ")
  gender = input("Your gender?: ")
  pkmnStr = ["0.Bulbasaur", "1.Charmander", "2.Squirtle"]
  print("Great! Now which one will be your first Pokèmon?")
  done = False
  print(*pkmnStr, sep="\n")
  
def main():
  start()
  
main()
  