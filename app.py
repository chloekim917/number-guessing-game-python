print('Welcome to the Guessing Game! Please input your range.')
begin = int(input('From: '))
end = int(input('To: '))
yorno = input(f"So you want to guess a number between {begin} and {end}? Write 'yes' or 'no': ")
if yorno.upper() == "YES":
    import random
    thenumb = random.randint(begin, end)
    print (thenumb)

    """
    print("Guess a number: ")
    i = input("Alright then, guess a number: ")
    if i < thenumb:
        input("Higher! Guess a new number: ")
    elif i > thenumb:
        input ("Lower! Guess a new number: ")
    
    """

     