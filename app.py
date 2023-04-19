print('Welcome to the Guessing Game! Please input your range.')

while True:
    begin = int(input('From: '))
    end = int(input('To: '))
    yorno = input(f"So you want to guess a number between {begin} and {end}? Write 'yes' or 'no': ")
    if yorno.upper() == "YES":
        import random
        thenumb = random.randint(begin, end)
        #print(thenumb)
        i = int(input("Guess a number: "))
        break
    else:
        print ("Let's try this again. Give me a range.")

count = 1
while i != thenumb:
    if i < thenumb:
        count = count+1
        #print(count)
        i = int(input("Higher! Guess a new number: "))
    elif i > thenumb:
        count = count+1
        #print(count)
        i = int(input("Lower! Guess a new number: "))
print(f"Congrats! You got it right! It took you {count} tries")
