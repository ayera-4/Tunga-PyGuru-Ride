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


def full_name(first_name, last_name): #Number 4
    print(f"{first_name} {last_name}")

#first = input("Enter your first name: ")
#last = input("Enter your last name: ")
#full_name(first, last)


#def check_prime(num): #Number 5


def calculate_pow(arg1): #Number 6
    return print(arg1**3)

#input_num = int(input("Enter an integer: "))
#calculate_pow(input_num)


def display_info(name, location): #Number 7
    print(name)
    print(location)
#country = input("Enter country of location: ")
#display_info(name="Magnus",location=country)


def find_sum(n): #Number 8
    total = 0
    for i in range(1, n+1):
        total += i
    return print(total)

#number = int(input("Enter an integer: "))
#find_sum(number)


def compute_area(radius, pi): #Number 9
    area = pi * (radius ** 2)
    return print(area)

#circle_rad = float(input("Enter radius of the circle: "))
#circle_pi = 3.14
#compute_area(circle_rad, circle_pi)


