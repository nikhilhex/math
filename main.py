import sys
import random
from colorama import Fore, Back, Style

want = input(Fore.GREEN + "ready for some math? (y/n) \n")

if want == "y" or want == "yes" or want == "Y" or want == "Yes" or want == "yEs" or want == "yeS" or want == "YES":
  print(Fore.RED + "Okay!")
  mode = input(Fore.CYAN +
               "Select a mode (a/s/m/d/da/dm/ds/dd/fa/fs/fm/fd/ehm/msh) \n")
  if mode == "a":
    print(Fore.LIGHTBLUE_EX + "To exit, type exit \n")
    questions = input(
      f"{Fore.MAGENTA}How many questions would you like to do? \n")
    if questions == 0:
      exit()
    correct = 0
    incorrect = 0
    for x in range(int(questions)):

      num1 = random.randint(1, (x + 1))
      num2 = random.randint(1, (x + 1))
      ans = input(
        f"{Fore.MAGENTA}Whats {str(num1)} + {str(num2)}? {Fore.CYAN}\n")
      if ans == "exit":
        exit()
      if ans == "":
        print(f"{Fore.RED}Don't be shy! We're moving on. And that's wrong")
        ans = "1304050"

      if int(ans) == num1 + num2:
        print(f"{Fore.GREEN}Correct")
        correct = correct + 1
      else:
        print(f"{Fore.RED}INCORRECT")
        incorrect = incorrect + 1
      print(
        f"{Fore.LIGHTYELLOW_EX}Total: {x} {Fore.WHITE}| {Fore.GREEN}Correct: {correct} {Fore.WHITE}| {Fore.RED}Incorrect:{incorrect}"
      )
    print("Great work! Restart this app to do another mode!")
    exit()
  elif mode == "s":
    print(Fore.LIGHTBLUE_EX + "To exit, type exit \n")
    negative = input("Negative numbers? (y/n) \n")
    if negative == "y":
      positive = input("Positive numbers also? (y/n) \n")

    questions = input(
      f"{Fore.MAGENTA}How many questions would you like to do? \n")

    if questions == 0:
      exit()

    correct = 0
    incorrect = 0

    for x in range(int(questions)):
      if negative == "y" and positive == "y":
        num1 = random.randint(x * -1, x + 1)
        num2 = random.randint(x * -1, x + 1)
      elif negative == "y" and positive == "n":
        num1 = random.randint(x * -1, x * -1)
        num2 = random.randint(-x * -1, x * -1)
      elif negative == "n":
        num1 = random.randint(x + 1, x + 1)
        num1 = random.randint(x + 1, x + 1)

else:
  print("oh...")
  quit()
