import random

def game_logic(user_choice,comp_choice):
    if(user_choice == comp_choice):
        return "It's a TIE."
    elif((user_choice == 'rock' and comp_choice =='scissor') or
         (user_choice == 'scissor' and comp_choice =='paper')or
         (user_choice == 'paper' and comp_choice =='rock')):
        return "You WIN!"
    else:
        return "You LOOSE!"

def game():
    
    u_score=0
    c_score=0
    while(True):
        print("\n***ROCK-PAPER-SCISSORS***")
        print('1. ROCK')
        print('2. PAPER')
        print('3. SCISSOR')
        print('4. QUIT')
        try:
            user_input = int(input('Select the option of your choice(1/2/3/4):'))
            if user_input not in [1,2,3,4]:
                print("Invaild Choice.Enter 1 for ROCK, 2 for PAPER, 3 for SCISSOR or 4 for QUIT.")
                continue
        except ValueError:
            print("Invalid input.Please, enter valid input choice.")
            continue

        if user_input == 4 :
            if (u_score > c_score):
                print("\nCongratulations!! you WON the game.")
            elif(u_score < c_score):
                print("\nYou LOST the game.Better Luck Next Time.")
            else:
                print("\nIt's a TIE. Play Again.")
            print("Thanks for Playing!!\n")
            break
        
        opt=['rock','paper','scissor']
        user_choice=opt[user_input-1]
        comp_choice=random.choice(opt)
        print(f"\nYour Choice : {user_choice}")
        print(f"Computer's Choice : {comp_choice}")
        
        score = (game_logic(user_choice,comp_choice))
        print(score)
        
        if 'WIN' in score:
            u_score+=1
        elif 'LOOSE' in score:
            c_score+=1
        print(f'Scores :\n YOU: {u_score}   COMPUTER: {c_score}')
        

game()
            
        
