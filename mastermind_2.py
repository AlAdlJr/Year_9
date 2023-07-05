# Master Mind - Ismail AlAdl

import random

def generate_code():
  #Generates a random list of four numbers
  code = []
  for _ in range(4):
    code.append(random.randint(1, 4))
  return code

def get_guess():
  #Gets a guess from the user
  guess = []
  for _ in range (4):
    guess_input = input("Enter a number from 1 to 4: ")
    guess.append(int(guess_input))
  return guess

def evaluate_guess(code,guess):
  #Comparing the guess to the list
  correct_colour = 0
  correct_positions = 0
  for i in range (4):
    if code[i] == guess[i]:
      correct_positions += 1
    elif guess[i] in code:
      correct_colour += 1
  return correct_colour , correct_positions

#Operation
code = generate_code()
lines = 5

for i in range (5):
  guess = get_guess()
  correct_position, correct_colour = evaluate_guess(code , guess)
  print("Correct position:", correct_position)
  print("Correct colour:", correct_colour)
  if correct_position == 4:
    print("You have won!")
    break
  else:
   print("You have lost!")
   lines -= 1
   print("Tries left" , str(lines))

  if lines == 0:
    print("The secret code is:", code)
