
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


# task 3

try:

    name_text = input("Enter text: ")
    text_search = input("Enter text search: ")
    text_replace = input("Enter text replace: ")

    result_text = name_text.replace(text_search, text_replace)

    print(f"Result: {result_text}")

except Exception as e:
    print(f"Incorrect action{e}")
finally:
    print("End program\n")