# File: CS112_A1_T2_3_20231244
""""Purpose: The game starts with a certain number of coins where each player removes a square number of coins and who
             removes the last coin wins"""
# Auther: Mostafa Mahmoud Fathy
# ID: 20231244
#displaying a greeting message
print("*************************************\n* Welcome to subtract a square game *\n*************************************\n")
print("- The game starts with a random number of coins\n- the player who removes the last coin wins")
print("- Each player can remove a square number of coins except zero\n")
while True:
 input("Press enter to continue: \n")
#creating a random number of coins
 import random
 coins = random.randint(10, 1000)
 #checking that the random number is not a square number
 for n in range(1, 31):
    if n == coins/n:
          coins = random.randint(10, 1000)
 print("the number of coins = ", coins)
 while coins > 0:
    player1 = int(input("player 1,enter the number of coins you want to remove: "))
    # checking if the inserted number is positive or not
    while player1 <= 0:
        player1 = int(input("choose a positive number"))
    #checking if the inserted number is less than the number of coins
    while player1 > coins:
       player1 = int(input("choose a smaller number "))
       # checking if the inserted number is positive or not
       while player1 <= 0:
           player1 = int(input("choose a positive number"))
    # checking if the inserted number is a square number or not
    while True:
     while player1 <= 0:
      player1 = int(input("choose a positive number"))
     if int(player1**0.5) != float(player1**0.5):
         player1 = int(input("choose a square number"))
         # checking if the inserted number is less than the number of coins
         while player1 > coins:
           player1 = int(input("choose a smaller number "))
           # checking if the inserted number is positive or not
           while player1 <= 0:
               player1 = int(input("choose a positive number"))
     else:
         break
    coins = coins - player1
    print("the number of coins = ", coins)
    if coins == 0:
        print("player1 is the winner")
        break

    player2 = int(input("player 2,enter the number of coins you want to remove: "))
    # checking if the inserted number is positive or not
    while player2 <= 0:
        player2 = int(input("choose a positive number"))
    # checking if the inserted number is less than the number of coins
    while player2 > coins:
        player2 = int(input("choose a smaller number "))
        # checking if the inserted number is positive or not
        while player2 <= 0:
            player2 = int(input("choose a positive number"))
    # checking if the inserted number is a square number or not
    while True:
       # checking if the inserted number is positive or not
       while player2 <= 0:
            player2 = int(input("choose a positive number"))
       if int(player2 ** 0.5) != float(player2 ** 0.5):
            player2 = int(input("choose a square number"))
        # checking if the inserted number is less than the number of coins
            while player2 > coins:
              player2 = int(input("choose a smaller number "))
              # checking if the inserted number is positive or not
              while player2 <= 0:
                    player2 = int(input("choose a positive number"))
       else:
         break
    coins = coins - player2
    print("the number of coins = ", coins)
    if coins == 0:
        print("player2 is the winner")
        break
