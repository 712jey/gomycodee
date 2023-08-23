import random
x=random.randint(1,100)
print(x)
n=int(input("guess it :"))
while True:
  if x==n:
    print("Congratulations! You guessed the number correctly!")
    break
  elif x<n:
    n=int(input("Your guess is too high. Guess again."))
  else:
    n=int(input("Your guess is too low. Guess again."))
