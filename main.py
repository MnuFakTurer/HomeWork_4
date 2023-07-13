
# task 1

try:

    name_line = input("Enter string: ")

    letter = 0
    digit = 0

    for symbol in name_line:
        if (symbol >= 'a' and symbol <= 'z') or (symbol >= 'A' and symbol <= 'Z'):
            letter += 1
        if symbol >= '0' and symbol <= '9':
            digit += 1

    print(f"Quantity of letter: {letter}")
    print(f"Quantity of numbers: {digit}")

except Exception as e:
    print(f"Incorrect action{e}")
finally:
    print("End program\n")

# task 2

try:

    name_string = input("Enter text: ")
    name_symbol = input("Enter symbol: ")

    i = 0

    for letter in name_string:
            if letter == name_symbol:
                i += 1



    print(f"Requested symbol: {name_symbol}\nQuantity of letter: {i}")

except Exception as e:
    print(f"Incorrect action{e}")
finally:
    print("End program\n")

