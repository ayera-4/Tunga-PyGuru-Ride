def print_number(): #Number 1
    print(5)
    print(100)

#for i in range(2):
#    print_number()


def checkMarks(marks): #Number 2
    if marks >= 70:
        return print("Pass")
    else:
        return print("Fail")

#input_mark = int(input("Enter your marks: "))
#checkMarks(input_mark)


def my_function(num_A, num_B): #Number 3
    if num_A == num_B:
        return print(True)
    else:
        return print(False)

#num1 = int(input("Enter first integer: "))
#num2 = int(input("Enter second integer: "))
#my_function(num1, num2)


def full_name(first_name, last_name):
    print(f"{first_name} {last_name}")

#first = input("Enter your first name: ")
#last = input("Enter your last name: ")
#full_name(first, last)