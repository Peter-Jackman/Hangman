import pdb
from Gallows import drawing 

def two_player():
    past_guesses=set()
    running=1 

    #main loop
    while running==1:
        #set variables
        dashes=[]
        not_solved=1
        set.clear(past_guesses)
        failed_guesses=0
        separator=' '
        success=0
        word=input("Player 1 input a word: ") 

        #hide word from player 2
        for i in range(0,50):
            print(' ')

        #makes list of dashes
        for i in word:
            dashes.append('_') 

        while not_solved==1:
            print(separator.join(dashes))
            guess_input=1
            
            while guess_input==1:  
                guess=input("Player 2 make a guess: ")

                #tests for double letters guessed
                for i in range(0, len(guess)):
                    if i>=1:
                        guess_input=1
                        print('Only guess one letter')

                    else:
                        guess_input=0

            #tests if the guess is correct
            if guess in word:
                #tests if the guess has been made before
                if guess in past_guesses:
                    print("You've already guessed that, try again")
                    continue

                elif guess=='':
                    print('Please enter a letter')
                else:
                    #loops through dashes to test for multiples
                    for i in range (0,len(word)):
                        if guess==word[i]:
                            dashes[i]=guess
                            success+=1
                    print(guess +" is in the word!")                  

            else:
                if guess in past_guesses:
                    print("You've already guessed that, try again")
                    continue

                #tests if guess was incorrect
                else:
                    print(guess+" is not in the word")
                    failed_guesses+=1
                    print(f"{7-failed_guesses} guesses remaining")
                    drawing(failed_guesses)

            #adds guess to set
            past_guesses.add(guess)

            #tests if word is guessed     
            if success>=len(dashes):
                print('You guessed the word!')
                print(f"The word was {word}")
                x=player_input('yes','no','Would you like to play again? yes/no?')
                
                if x==1:
                    not_solved=0
                    
                else:
                    not_solved=0
                    running=0
                   
            #tests if 7 guesses have been made   
            if failed_guesses==7:
                print('You lost!')
                print(f"The word was {word}")
                x=player_input('yes','no','Would you like to play again? yes/no?')             

                if x==1:
                    not_solved=0

                else:
                    not_solved=0
                    running=0
 
def player_input(correct_input, incorrect_input, question):
    y=1

    while y==1:
        output=input(question)
        if output==correct_input:
            x=1
            y=0

        elif output==incorrect_input:
            x=0
            y=0

        else:
            print('Please input '+str(correct_input)+'/'+str(incorrect_input))
    return x

two_player()
