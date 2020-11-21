

##print('Hello')

##x = input('What is your name?')
##
##y = int(input('How old are you?'))
##
##print(f"Let us get this straight. You are {y} years old and not getting any younger.")
##
##print()

 
##
##a= input ('How is your day so far?').lower()
##
##if a[0] == 's':
##    print('I think it will be getting better')
##else:
##    print ('That is better than what I thought')
##
##print()
##
##b = input('Did you take a bath? Y/N').lower()
##print()
##
##if b == 'y':
##    print('Are you sure because you still stink?')
##else:
##    print('That makes sense, I could smell you from the office today. BAO!')
##
##print()
##
##print('All jokes aside')
##
##print()
##
##z = input('Wanna play a guessing game against me? Y/N').lower()
##
##while z == 'y':
##    print('Are you ready patas?')
##    print()
##    break
##if z == 'n':
##    print('Please la. I am lonely here')
##    print()
##    z = input('Pretty please. Do you wanna play a game against me? Y/N').lower()
##    print()
##    if z == 'n':
##        print ('Please la. I know you have nothing to do with your life.')
##        z = input('Last time I am going to ask. Do you wanna play a game against me? Y/N').lower()
##        if y == 'n':
##            print('Goodbye. You are not my friend. ')
##            print()


         
import random



while True:
    number = random.randint(1,20)
    count = 0 
    
    try:
        guess = int(input("I have a number in mind. Please guess if you dare: "))
        while guess != number:
            count += 1
            if guess > number:
                print('Please guess a smaller number you pea brain.')
                guess = int(input("Use what the good lord gave you. Please enter a guess: "))
            else:
                print ('Please guess a larger number you airhead.')
                guess = int(input("Try harder if you can. Please enter a guess: "))
        else:
            print('Finally! Your IQ is the same as a peanut.')
            print(f'Also, it took you {count} guesses. Not smart at all.')
           
    except ValueError:
        print("Ooops, please enter a number. Not the brightest bulb I see.")

    q = input('Do you want to play again if your brain can take it. Y/N').lower()

    if q[0] == 'n':
        print('You weak. I strong. Chao')
        break



##while True:
##    number = random.randint(1,20)
##    count = []
##    print(number)
##    try:
##        guess = int(input("I have a number in mind. Please guess if you dare: "))
##        while guess != number:
##            count.append(guess)
##            if guess > number:
##                print('Please guess a smaller number you pea brain.')
##                guess = int(input("Use what the good lord gave you. Please enter a guess: "))
##            else:
##                print ('Please guess a larger number you airhead.')
##                guess = int(input("Try harder if you can. Please enter a guess: "))
##        else:
##            print('Finally! Your IQ is the same as a peanut.')
##
##    for i,j in enumerate(count): #some mistake here
##        print (f'Also, it took you {i+1} guesses. Not smart at all.')
##           
##    except ValueError:
##        print("Ooops, please enter a number. Not the brightest bulb I see.")
##
##    q = input('Do you want to play again if your brain can take it. Y/N').lower()
##
##    if q[0] == 'n':
##        print('You weak. I strong. Chao')
##        break
##    

