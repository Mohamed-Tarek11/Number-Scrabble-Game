#CS112_A1_T2_2_20230341
"""
Number scrabble is played with the list of numbers between 1 and 9. Each player takes
turns picking a number from the list. Once a number has been picked, it cannot be picked
again. If a player has picked three numbers that add up to 15, that player wins the game.
However, if all the numbers are used and no player gets exactly 15, the game is a draw.
"""
#Mohamed Tarek Fawzey Abd-El fattah
#ID:20230341



from itertools import combinations
# Built in function that find all combinations of the player list elements in form of tupels

#Function that checks the numbers of the players and detrmine if there is a player wins
def checking_winner(player_numbers): 
    for combine_numbers in combinations(player_numbers,3):
        if sum(combine_numbers) == 15:   #statment that checks if there is three numbers in -->
                                         # the list of the player sum of them equals 15
            return True  
            # If there are three numbers whose sum is 15, return True value         
    return False  # If there is no such combination is found satisfy the condition then return False value

#Function that runs the game 
def the_game():
    available_numbers =[1,2,3,4,5,6,7,8,9]        
    player1_numbers= []
    player2_numbers= []

    #for loop to detrmine wich turn of the two players
    for turn in range(1,10):
        print("available numbers",available_numbers)
        if turn%2 == 1:                              #if turn is odd then player 1 has to play else player 2 play 
            current_player = "player 1"
            player_numbers = player1_numbers
        else:
            current_player = "player 2"
            player_numbers = player2_numbers
        try:
            select_number= int(input(f"{current_player} pick a number: "))
            if select_number not in available_numbers :
                raise ValueError("Number already taken or not in the range of numbers of the game")  
        except ValueError as i : # if the player have been choosen a number that is wrong let him/her choose again print error message and make him choose again
            print(i)
            turn = turn - 1
            continue
        player_numbers.append(select_number)      #Adding the numers that have been choosen ny the players 
        available_numbers.remove(select_number)   #removing the elements that have been choosen by the players

        #statment that calls checking_winner function and checks the winer 
        if checking_winner(player_numbers):       
            print(f"{current_player}, wins")    #declaring the winner 
            break
    else:
            print("Draw")


#game name 
print("********Welcome to NUMBER SCRABLLE GAME********\n ")

#Game describtion
print("Description of the game:\nNumber scrabble is played with the list of numbers between 1 and 9. Each player takesturns picking a number from the list.")
print("Once a number has been picked, it cannot be pickedagain.\nIf a player has picked three numbers that add up to 15, that player wins the game.\nHowever, if all the numbers are used and no player gets exactly 15, the game is a draw.\n ")
#calling the game function
the_game()
