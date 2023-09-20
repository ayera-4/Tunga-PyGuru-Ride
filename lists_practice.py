def print_list_items(item_list): #Number 1
    for item in item_list:
        print(item)

#fruits = ["apple", "kiwi", "grapes", "mango"]
#print_list_items(fruits)


def add_to_list_end(odd_list): #Number 2
    try:
        number = int(input("Enter another odd number: "))
        if number % 2 == 1:
            odd_list.append(number)
            print(odd_list)
        else:
            print("Input is not an odd number")
    except ValueError:
        print("Input is not an odd number")
        return 0

#odd_numbers = [1,3,5]
#print(f"Current odd number list: {odd_numbers}")
#add_to_list_end(odd_numbers)


def calculate_product(item_list): #Number 3
    product = 1
    for item in item_list:
        product *= item
    return print(product)

#my_list = [2,5,3,4,1]
#calculate_product(my_list)


def check_first_and_last(literal): #Number 4
    char_list = list(literal)
    if char_list[0] == char_list[-1]:
        return print("Equal")
    else:
        return print("Not Equal")

#check = "banana"
#check_first_and_last(check)


def print_odd_numbers(num_list): #Number 5
    for num in num_list:
        if num % 2 == 1:
            print(num)

#numbers = [1,2,3,4,5,6,7,8]
#print_odd_numbers(numbers)


def reverse_list(num_list): #Number 6
    return print(num_list[::-1])
#my_list = [1,2,3,4]
#reverse_list(my_list)


def create_new_list(char_list): #Number 7
    return print(char_list[1:-1])

#my_list = ['p','y','t','h','o','n']
#create_new_list(my_list)


def sum_even_and_odd(num_list): #Number 8
    odd_sum = 0
    even_sum = 0
    for num in num_list:
       if num % 2 == 0:
           even_sum += num
       else:
           odd_sum += num
    return (odd_sum, even_sum)

#test_list = [51,75,69,36,75,44,82,36]
#print(sum_even_and_odd(test_list))


def square_numbers(num_list): #Number 9
    square_list = []
    for num in num_list:
        square_list.append(num**2)
    square_list.sort()
    return square_list

#test_list = [-7,-2,0,4,5,7]
#print(square_numbers(test_list))


def check_sequence(num_list): #Number 10
    benchmark_list = num_list.copy()
    num_list.sort()
    if num_list == benchmark_list:
        return True
    else:
        return False
#test_list = [1,2,3,4,5]
#print(check_sequence(test_list))


def print_char_occurrence(literal, in_char): #Number 11
    count = 0
    for char in literal:
        if char == in_char:
            count += 1
    return count

#string1 = input("Enter a string for check: ")
#character1 = input("Enter a character to be checked: ")
#print(print_char_occurrence(string1, character1))


def replace_yt(literal): #Number 12
    language = "Python"
    language = language.replace("yt", literal)
    return language
#ch = input("Enter a string: ")
#print(replace_yt(ch))


def concatenate_strings(literal1, literal2): #Number 13
    result = literal1 + literal2
    return result
#string1 = input("Enter first string")
#string2 = input("Enter second string")
#print(concatenate_strings(string1, string2))