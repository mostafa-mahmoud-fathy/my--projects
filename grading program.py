#defining a function checks that the input can be a positive number
def is_number_and_positive(input_str):
    try:
        if 0 <= float(input_str) <= 100:
             return True
    except ValueError:
        return False
# printing a greeting message
print("Welcome to the grading program")
print("Please, enter your mark to determine your grade")
# an infinite loop that takes the input and if the function returns true the loop will be broken
# and if the function returns false the loop will continue
while True:
    mark = input()
    if is_number_and_positive(mark):
        break
    else:
        print(f"{mark} is an invalid input,\nPlease enter your mark again .")
        continue
# determining the grade and printing it
if 100 >= int(float(mark)) >= 90:
    print("Your grade is A+")
elif 90 > int(float(mark)) >= 85:
    print("Your grade is A")
elif 85 > int(float(mark)) >= 80:
    print("Your grade is B+")
elif 80 > int(float(mark)) >= 75:
    print("Your grade is B")
elif 75 > int(float(mark)) >= 70:
    print("Your grade is C+")
elif 70 > int(float(mark)) >= 65:
    print("Your grade is C")
elif 65 > int(float(mark)) >= 60:
    print("Your grade is D+")
elif 60 > int(float(mark)) >= 50:
    print("Your grade is D")
elif 50 > int(float(mark)):
    print("Your grade is F")