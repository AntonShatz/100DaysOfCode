import math

# Ceil floor the num
# def ceil_num(x):
#     y = math.ceil(x)
#     z = math.floor(x)
#     print(f'you had {x} now you have {y} and {z}')
#
#
# ceil_num(10.3)
#
# def check_if_prime(n): # Prime checker
#     is_prime = True
#     for i in range(2, n):
#         if n % i == 0:
#             is_prime = False
#     if is_prime:
#         print("Yes its a prime")
#     else:
#         print("No its not")
#
#
# n = int(input())
# check_if_prime(n)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def caesar(text, shift, direction):
    end_text = ""
    if direction == "dyc":
        shift *= -1
    for char in text.lower():
        if char in alphabet:
            position = alphabet.index(char)
            new_position = position + shift
            end_text += alphabet[new_position]
        else:
            end_text+= char
    print(f"The {direction} text is {end_text}")

should_continue = True
while should_continue:
    direction = input("Type dyc to dycrypt or type enc to encrypt\n")
    text = input("Type the text  \n").lower()
    shift = int(input("How much u wanna shift ? \n"))
    shift = shift%25
    print(shift)
    caesar(text=text,shift=shift,direction=direction)
    result = input("Type 'yes' to continue or 'No' to stop\n")
    if result == 'no':
        should_continue=False
