#This adventure game gives you a choice to risk it all, Will you survive? You won't know until you try.
#tell the user, "welcome to my first game"
'''ask what is your name? what is your age
are you old enough to play?(has to be over 18) if old enough print You are old enough to play!
If not old enough then, "Sorry, to play you have to be 18+" If older than 14 say "You can play with supervison" '''
#ask  "do you want to play?" (think of the caps when they enter in their answer)
#If they want to play tell them "You are starting out with # health"
'''after say "Let's play!" otherwise, "sad to see you go :((" 
Start game after 'let's play' say "First choice... Left or Right (left/right)?" if they answered right say "Nice, you follow
the path and reach a lake... Do you swim across or go around (across/around)?"?
'''
user = print("Welcome to my first game.")
name = input(print("What is your name? "))
age = int(input(print("What is your age? ")))

age = 18
health = 7

if age >= 18:
    print("You are old enough to play!")
    
    want_to_play = input(print("Do you want to play (yes/no)? ")).lower()
    if want_to_play == ("yes"):
        print("You are starting out with ", health, " health" )
        print("Let's play!")

        left_or_right = input(print("First choice... Left or Right (left/right)? ")).lower()
        if left_or_right == ("left"):
            input(print("Nice, you follow the path anf reach a lake... Do you swim across or go around (across/around)? ")).lower()
        else:
            print("OOoOpPpp... down you GOOoOo, you fell down and lost..")
     
    else:
        print("Sad to see you go 😓")

elif age >= 14:
        print("You can play this with supervision")

else: 
    print("Sorry, to play you have to be 18+")