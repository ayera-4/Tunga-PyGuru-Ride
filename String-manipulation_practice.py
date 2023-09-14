
def num_special(literal): #Number 1
    count = 0
    for char in literal:
        if not char.isalnum() and not char.isspace():
            count += 1
    return count
#Test Output
#input_sent = "hello! good morning *."
#print(num_special(input_sent))

def string_rep(n): #Number 2
    out_list = []
    for num in range(1, n+1):
        if num % 3 == 0:
            out_list.append("Fizz")
        elif num % 5 == 0:
            out_list.append("Buzz")
        else:
            out_list.append(str(num))
    return out_list
#Test Output
#number = 9
#print(string_rep(number))

def first_index_of_no_repeat(literal): # Number 3
    for char in literal:
        if literal.count(char) == 1:
            return literal.find(char)
#Test Output
#input_sent = "python.program.py"
#print(first_index_of_no_repeat(input_sent))

def get_bill_share(bill, persons): # Number 4
    tax = 0.08875 * bill
    total_bill = bill + tax
    try:
        bill_share = total_bill / persons
        return bill_share
    except ZeroDivisionError:
        print("No persons accountable")
        return 0
#Test Output
#bill = int(input("Enter total bill: "))
#persons = int(input("Enter number of people: "))
#print(f"Individual contribution is {get_bill_share(bill, persons)}")

def check_if_palindrome(literal): # Number 5
#remove space and special character
    test_input = ""
    for char in literal:
        if char.isalnum():
            test_input += char.lower()
    if test_input == test_input[::-1]:
        return print("String is Palindrome")
    else:
        return print("Try another string")
#Test Output
#input_sent = "A man, a plan, a canal: Panama"
#check_if_palindrome(input_sent)

def is_harshad_number(number): # Number 6
    digit_sum = 0
    for digit in str(number):
        digit_sum += int(digit)
    if number % digit_sum == 0:
        print("It is a Harshad Number")
    else:
        print("It is not a Harshad Number")
#Test Output
#number = 15
#is_harshad_number(number)

def is_armstrong_number(number): # Number 7
    digit_sum = 0
    for digit in str(number):
        digit_sum += (int(digit)**3)
    if number == digit_sum:
        print("It is a Armstrong Number")
    else:
        print("It is not a Armstrong Number")
#Test Output
#number = 371
#is_armstrong_number(number)

def word_occurrence(literal): # Number 8
    word_list = [x.lower() for x in literal.split()]
    out_dict = {}
    for word in word_list:
        out_dict.update({word:word_list.count(word)})
    return out_dict
#Test output
#input_sent = "Captain America is Captain of America"
#print(word_occurrence(input_sent))

def get_required_and_extra_fuel(distance): # Number 9
    min_fuel = 100
    required_fuel = distance * 10
    if required_fuel > min_fuel:
        extra_fuel = required_fuel - min_fuel
    else:
        extra_fuel = 0
    return (required_fuel, extra_fuel)
#Test Output
#test_distance = 0
#print(get_required_and_extra_fuel(test_distance))

def sums_even_and_odd(num_list): # Number 10
    even_sum = 0
    odd_sum = 0
    for num in num_list:
        if num % 2 == 0:
            even_sum += num
        else:
            odd_sum += num
    return (odd_sum, even_sum)
#Test Output
#test_list = [51, 75, 69, 36, 75, 44, 82, 36]
#print(sums_even_and_odd(test_list))

def char_occurrence(literal): # Number 11
    char_list = []
    for char in literal.lower():
        if char.isalnum() and literal.count(char) > 1 and char not in char_list:
            char_list.append(char)
    return len(char_list)

#Test Output
#test_literal = "Nick Fury Hired Iron Man"
#print(char_occurrence(test_literal))

def is_abundant_number(number): # Number 12
    digit_sum = 0
    for num in range(2, number):
        if number % num == 0:
            digit_sum += num
    if digit_sum > number:
        print("It is an Abundant Number")
    else:
        print("It is not an Abundant Number")
#Test Output
#number = 14
#is_abundant_number(number)

def is_sum_of_digits_equal(int1, int2): # Number 13
    int1_sum = 0
    int2_sum = 0
    for digit in str(int1):
        int1_sum += int(digit)
    for digit in str(int2):
        int2_sum += int(digit)
    if int1_sum == int2_sum:
        return True
    else:
        return False
#Test Output
#first_int = 243
#second_int = 900
#print(is_sum_of_digits_equal(first_int, second_int))

def repeat_vowels(literal, num): # Number 14
    vowels = ['a','e','i','o','u']
    new_literal = []
    for char in literal:
        if char in vowels:
            new_literal.append(char*num)
        else:
            new_literal.append(char)
    return str("{}"*len(new_literal)).format(*new_literal)
#Test Output
#test_string = "banana"
##print(repeat_vowels(test_string, test_number))

def count_digits_in_string(literal): # Number 15
    digit_count = 0
    for char in literal:
        if char.isdigit():
            digit_count += 1
    return digit_count
#Test Output
#test_string = "Boys was released in 2019"
#print(count_digits_in_string(test_string))

def convert_camel_2_snake(literal): # Number 16
    if literal[0].islower() and "_" not in literal:
        new_literal = ""
        for char in literal:
            if char.isupper():
                new_literal += f"_{char.lower()}"
            else:
                new_literal += char
        return new_literal
    else:
        return "Not camelCase"
#Test Output
#test_string = "helloworld"
#print(convert_camel_2_snake(test_string))

def is_lapindrome_number(num): # Number 17
    literal = str(num)
    mid = len(literal)//2
    first_seg = literal[:mid]
    if len(literal) % 2 == 0:
        second_seg = literal[mid:][::-1]
    else:
        second_seg = literal[mid+1:][::-1]

    if first_seg == second_seg:
        return "It is Lapindrome Number"
    else:
        return "It is not Lapindrome Number"
#Test Output
#test_number = 1234321
#print(is_lapindrome_number(test_number))

def calculate_BMI(weight, height): # Number 18
    _BMI = round(weight/(height**2), 1)
    if _BMI >= 30.0:
        return "Obese"
    elif _BMI >= 25.0:
        return "Overweight"
    elif _BMI >= 18.5:
        return "Normal Weight"
    else:
        return "Underweight"
#Test Output
#test_weight = 65
#test_height = 1.67
#print(calculate_BMI(test_weight, test_height))


def reverse_odd_long_words(literal): # Number 19
    word_list = literal.split()
    new_literal = ""
    for word in word_list:
        if len(word) % 2 == 1:
            word_list[word_list.index(word)] = word[::-1]
    return " ".join(word_list)
#Test Output
#test_literal = "Learn to code from Programiz"
#print(reverse_odd_long_words(test_literal))

def ascending_squares(num_list): # Number 20
    square_list = [num**2 for num in num_list]
    square_list.sort()
    return square_list
#Test Output
#test_num_list = [-7,-2,0,4,5]
#print(ascending_squares(test_num_list))

def words_start_char(literal, char): # Number 21
    word_list = literal.split()
    out_list = []
    for word in word_list:
        if char in word:
            out_list.append(word)
    return out_list
#Test Output
#test_literal = "Doe went to Dubai"
#test_char = 'd'
#print(words_start_char(test_literal, test_char))

def most_vowel_at_end(literal): # Number 22
    word_list = literal.split()
    vowels = ['a','e','i','o','u']
    last_char = []
    max_count = 0
    max_char = ""
    for word in word_list:
        if word[-1] in vowels:
            last_char.append(word[-1])
    for char in last_char:
        if last_char.count(char) > max_count:
            max_count = last_char.count(char)
            max_char = char
    return max_char
#Test Output
#test_literal = "I owe you two hundred twenty two dollars"
#print(most_vowel_at_end(test_literal))

def build_readable_string(literal): # Number 23
    temp_literal = literal.strip().lower() + "."
    new_literal = temp_literal[0].upper() + temp_literal[1:]
    return new_literal
#Test Output
#test_literal = "  hEllo worlD iN Python  "
#print(build_readable_string(test_literal))

def check_sequence(num_list): # Number 24
    init_list = num_list.copy()
    num_list.sort()
    if num_list == init_list:
        return True
    else:
        return False
    return num_list
    #print(init_list)
    #print(num_list)
#Test Output
#number_list = [1,2,3,4,5]
#print(check_sequence(number_list))