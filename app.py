print('Welcome to the Guessing Game! Please input your range.')
begin = int(input('From: '))
end = int(input('To: '))
yorno = input(f"So you want to guess a number between {begin} and {end}? Write 'yes' or 'no': ")
if yorno.upper() == "YES":
    import random
    thenumb = random.randint(begin, end)
    print(thenumb)
    i = int(input("Guess a number: "))

while i != thenumb:
    count = 0
    if i < thenumb:
        count+1
        i = int(input("Higher! Guess a new number: "))
    elif i > thenumb:
        count+1
        i = int(input("Lower! Guess a new number: "))
        
print(f"Congrats! You got it right! It took you {count} tries")
