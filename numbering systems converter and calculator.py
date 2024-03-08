# Name: Mohamed Ahmed Mohamed Abd El_Wahab   Id: 20231134
# Name: Mohamed Ahmed Mohamed Hamed          Id: 20231131
# Name: Mostafa Mahmoud Fathy Hamdan         Id: 20231244
def hexa_decimal():
 sum = 0
 num = list(inserted_number)
 for i in range(len(num)): #converting the letters to its value
        if num[i] == "A":
            num[i] = 10
        elif num[i] == "B":
            num[i] = 11
        elif num[i] == "C":
            num[i] = 12
        elif num[i] == "D":
            num[i] = 13
        elif num[i] == "E":
            num[i] = 14
        elif num[i] == "F":
            num[i] = 15
        else:
            continue
 num = num[::-1] #reversing the list
 for i in range(len(num)): #converting to decimal and getting the sum
     sum = sum + int(num[i]) * 16 ** i
 print(sum)
def decimal_hexa():
    result = int(inserted_number)
    hexa_list = list() #creating an empty list to add the converted values
    while result > 0:
        reminder = result % 16
        hexa_list.append(reminder)
        result = int(result / 16)
    for i in range(len(hexa_list)): #converting values to letters
        if hexa_list[i] == 10:
            hexa_list[i] = "A"
        elif hexa_list[i] == 11:
            hexa_list[i] = "B"
        elif hexa_list[i] == 12:
            hexa_list[i] = "C"
        elif hexa_list[i] == 13:
            hexa_list[i] = "D"
        elif hexa_list[i] == 14:
            hexa_list[i] = "E"
        elif hexa_list[i] == 15:
            hexa_list[i] = "F"
    hexa_list = hexa_list[::-1] #reversing the list
    hexa_result = str() #an empty string variable
    for i in range(len(hexa_list)): #concatinating the converted values to the empty string
        hexa_result = str(hexa_result) + str(hexa_list[i])
    print(hexa_result)
def decimal_binary():
    binary_result = str() #an empty string variable
    binary_list = list()#creating an empty list to add the converted values
    result = int(inserted_number)
    while result > 0:
        decimal = result % 2
        binary_list.append(str(decimal))
        result = int(result / 2)
    for i in range(len(binary_list)): #concatinating the converted values to the empty string
      binary_result += binary_list[i]
    binary_result = binary_result[::-1] #reversing the list
    print(binary_result)
def binary_decimal():
    binary = str(inserted_number) #casting the inserted number
    decimal_result = 0
    binary = binary[::-1] #reversing the string
    for i in range(len(binary)): #converting binary to decimal and getting the sum
        decimal_result += int(binary[i]) * 2 ** i
    print(decimal_result)
def octal_decimal(): #the same as the previous function
        octal = str(inserted_number)
        decimal__result = 0
        octal = octal[::-1]
        for i in range(len(octal)):
            decimal__result += int(octal[i]) * 8 ** i
        print(decimal__result)
def decimal_octal(): #the same as decimal_binary
    octal_result = str()
    octal_list = list()
    result = int(inserted_number)
    while result > 0:
        decimal = result % 8
        octal_list.append(str(decimal))
        result = int(result / 8)
    for i in range(len(octal_list)):
        octal_result += octal_list[i]
    octal_result = octal_result[::-1]
    print(octal_result)
def hexa_bin():
    #hexa to dec
    sum = 0
    num2 = list(inserted_number)
    for i in range(len(num2)):
        if num2[i] == "A":
            num2[i] = 10
        elif num2[i] == "B":
            num2[i] = 11
        elif num2[i] == "C":
            num2[i] = 12
        elif num2[i] == "D":
            num2[i] = 13
        elif num2[i] == "E":
            num2[i] = 14
        elif num2[i] == "F":
            num2[i] = 15
        else:
                continue
    num2 = num2[::-1]
    for i in range(len(num2)):
        sum = sum + int(num2[i]) * 16 ** i
    #dec to bin
    binary_result = str()
    binary_list = list()
    result = int(sum)
    while result > 0:
        decimal = result % 2
        binary_list.append(str(decimal))
        result = int(result / 2)
    for i in range(len(binary_list)):
        binary_result += binary_list[i]
    binary_result = binary_result[::-1]
    print(binary_result)
def bin_hexa():
    #bin to dec
    binary = str(inserted_number)
    decimal_result = 0
    binary = binary[::-1]
    for i in range(len(binary)):
        decimal_result += int(binary[i]) * 2 ** i
    #dec to hexa
    result = int(decimal_result)
    hexa_list = list()
    while result > 0:
        reminder = result % 16
        hexa_list.append(reminder)
        result = int(result / 16)
    for i in range(len(hexa_list)):
        if hexa_list[i] == 10:
            hexa_list[i] = "A"
        elif hexa_list[i] == 11:
            hexa_list[i] = "B"
        elif hexa_list[i] == 12:
            hexa_list[i] = "C"
        elif hexa_list[i] == 13:
            hexa_list[i] = "D"
        elif hexa_list[i] == 14:
            hexa_list[i] = "E"
        elif hexa_list[i] == 15:
            hexa_list[i] = "F"
    hexa_list = hexa_list[::-1]
    hexa_result = str()
    for i in range(len(hexa_list)):
        hexa_result = str(hexa_result) + str(hexa_list[i])
    print(hexa_result)
def bin_oct():
    #bin to dec
    binary = str(inserted_number)
    decimal_result = 0
    binary = binary[::-1]
    for i in range(len(binary)):
        decimal_result += int(binary[i]) * 2 ** i
    #dec to oct
    octal_result = str()
    octal_list = list()
    result = int(decimal_result)
    while result > 0:
        decimal = result % 8
        octal_list.append(str(decimal))
        result = int(result / 8)
    for i in range(len(octal_list)):
        octal_result += octal_list[i]
        octal_result = octal_result[::-1]
    print(octal_result)
def oct_bin():
    #oct to dec
    octal = str(inserted_number)
    decimal_result = 0
    octal = octal[::-1]
    for i in range(len(octal)):
        decimal_result += int(octal[i]) * 8 ** i
    #dec to bin
    binary_result = str()
    binary_list = list()
    result = int(decimal_result)
    while result > 0:
        decimal = result % 2
        binary_list.append(str(decimal))
        result = int(result / 2)
    for i in range(len(binary_list)):
        binary_result += binary_list[i]
    binary_result = binary_result[::-1]
    print(binary_result)
def oct_hexa():
    #oct to dec
    octal = str(inserted_number)
    decimal_result = 0
    octal = octal[::-1]
    for i in range(len(octal)):
        decimal_result += int(octal[i]) * 8 ** i
    #dec to hexa
    result = int(decimal_result)
    hexa_list = list()
    while result > 0:
        reminder = result % 16
        hexa_list.append(reminder)
        result = int(result / 16)
    for i in range(len(hexa_list)):
        if hexa_list[i] == 10:
            hexa_list[i] = "A"
        elif hexa_list[i] == 11:
            hexa_list[i] = "B"
        elif hexa_list[i] == 12:
            hexa_list[i] = "C"
        elif hexa_list[i] == 13:
            hexa_list[i] = "D"
        elif hexa_list[i] == 14:
            hexa_list[i] = "E"
        elif hexa_list[i] == 15:
            hexa_list[i] = "F"
    hexa_list = hexa_list[::-1]
    hexa_result = str()
    for i in range(len(hexa_list)):
        hexa_result = str(hexa_result) + str(hexa_list[i])
    print(hexa_result)
def hexa_oct():
    #hexa to dec
    sum = 0
    temp = list(inserted_number)
    for i in range(len(temp)):
        if temp[i] == "A":
            temp[i] = 10
        elif temp[i] == "B":
            temp[i] = 11
        elif temp[i] == "C":
            temp[i] = 12
        elif temp[i] == "D":
            temp[i] = 13
        elif temp[i] == "E":
            temp[i] = 14
        elif temp[i] == "F":
            temp[i] = 15
        else:
            continue
    temp = temp[::-1]
    for i in range(len(temp)):
        sum = sum + int(temp[i]) * 16 ** i
    #dec to oct
    octal_result = str()
    octal_list = list()
    result = int(sum)
    while result > 0:
        decimal = result % 8
        octal_list.append(str(decimal))
        result = (result // 8)
    for i in range(len(octal_list)):
        octal_result += octal_list[i]
    octal_result = octal_result[::-1]
    print(octal_result)
while True: #repeating the menus

    print("** numbering system convertor **")
    print()
    print("A) insert a new number")
    print("B) Exit program")
    choice = input()
    # checking the input
    if choice == "A":
        inserted_number = input("Please insert a number: ")
        print("** please select the base you want to convert from **")
        print("A) Decimal ")
        print("B) Binary ")
        print("C) Octal ")
        print("D) Hexadecimal ")
        choice2 = input()
        # repeating menu 1 if the choice 2 does not equal any of the available choices
        while choice2 != "A" and choice2 != "B" and choice2 != "C" and choice2 != "D":
            print("please  select a valid choice")
            choice2 = input()
            # breaking the loop if the inserted choice is one of the available choices
            if choice2 == "A" or choice2 == "B" or choice2 == "C" or choice2 == "D":
                break
            else:
                continue
        print("** please select the base you want to convert to **")
        print("A) Decimal ")
        print("B) Binary ")
        print("C) Octal ")
        print("D) Hexadecimal ")
        choice3 = input()
        # repeating menu 2 if the choice 3 does not equal any of the available choices
        while choice3 != "A" and choice3 != "B" and choice3 != "C" and choice3 != "D":
            print("please  select a valid choice")
            choice3 = input()
            # breaking the loop if the inserted choice is one of the available choices
            if choice3 == "A" or choice3 == "B" or choice3 == "C" or choice3 == "D":
                break
            else:
                continue
        # implementing the right function
        if choice2 == "D" and choice3 == "A":
         hexa_decimal()
        elif choice2 == "A" and choice3 == "D":
         decimal_hexa()
        elif choice2 == "A" and choice3 == "B":
         decimal_binary()
        elif choice2 == "B" and choice3 == "A":
         binary_decimal()
        elif choice2 == "C" and choice3 == "A":
         octal_decimal()
        elif choice2 == "A" and choice3 == "C":
         decimal_octal()
        elif choice2 == "D" and choice3 == "B":
         hexa_bin()
        elif choice2 == "B" and choice3 == "D":
         bin_hexa()
        elif choice2 == "B" and choice3 == "C":
         bin_oct()
        elif choice2 == "C" and choice3 == "B":
         oct_bin()
        elif choice2 == "C" and choice3 == "D":
         oct_hexa()
        elif choice2 == "D" and choice3 == "C":
         hexa_oct()
        else:
            print(inserted_number)
    # ending the program if the choice of the main menu equal "B"
    elif choice == "B":
        print("Thanks for using the program")
        break
    # checking if the inserted choice does not equal "A" or "B"
    else:
        # the loop will be implemented if the inserted choice does not equal "A" or "B"
        while choice != "A" and choice != "B":
            print("please select a valid choice")
            # checking the input
            choice = input()
            if choice == "A":
                inserted_number = int(input("Please insert a number: "))
                print("** please select the base you want to convert from **")
                print("A) Decimal ")
                print("B) Binary ")
                print("C) Octal ")
                print("D) Hexadecimal ")
                choice2 = input()
                # repeating menu 1 if the choice 2 does not equal any of the available choices
                while choice2 != "A" and choice2 != "B" and choice2 != "C" and choice2 != "D":
                    print("please  select a valid choice")
                    choice2 = input()
                    # breaking the loop if the inserted choice is one of the available choices
                    if choice2 == "A" or choice2 == "B" or choice2 == "C" or choice2 == "D":
                        break
                    else:
                        continue
                print("** please select the base you want to convert to **")
                print("A) Decimal ")
                print("B) Binary ")
                print("C) Octal ")
                print("D) Hexadecimal ")
                choice3 = input()
                # repeating menu 2 if the choice 3 does not equal any of the available choices
                while choice3 != "A" and choice3 != "B" and choice3 != "C" and choice3 != "D":
                    print("please  select a valid choice")
                    choice3 = input()
                    # breaking the loop if the inserted choice is one of the available choices
                    if choice3 == "A" or choice3 == "B" or choice3 == "C" or choice3 == "D":
                        break
                    else:
                        continue
                # implementing the right function
                if choice2 == "D" and choice3 == "A":
                    hexa_decimal()
                elif choice2 == "A" and choice3 == "D":
                    decimal_hexa()
                elif choice2 == "A" and choice3 == "B":
                    decimal_binary()
                elif choice2 == "B" and choice3 == "A":
                    binary_decimal()
                elif choice2 == "C" and choice3 == "A":
                    octal_decimal()
                elif choice2 == "A" and choice3 == "C":
                    decimal_octal()
                elif choice2 == "D" and choice3 == "B":
                    hexa_bin()
                elif choice2 == "B" and choice3 == "D":
                    bin_hexa()
                elif choice2 == "B" and choice3 == "C":
                    bin_oct()
                elif choice2 == "C" and choice3 == "B":
                    oct_bin()
                elif choice2 == "C" and choice3 == "D":
                    oct_hexa()
                elif choice2 == "D" and choice3 == "C":
                    hexa_oct()
                else:
                    print(inserted_number)
            # ending the program if the choice of the main menu equal "B"
            elif choice == "B":
                print("Thanks for using the program")
                exit() # we used exit() to end the program because if we used break it will affect the nested loop but,
                # the main loop will be repeated
            else:
                continue
