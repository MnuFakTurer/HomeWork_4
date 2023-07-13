
# task 1

try:

    name_line = input("Enter string: ")

    letter = 0
    digit = 0

    for char in name_line:
        if (char >= 'a' and char <= 'z') or (char >= 'A' and char <= 'Z'):
            letter += 1
        if char >= '0' and char <= '9':
            digit += 1

    print(f"Quantity of letter: {letter}")
    print(f"Quantity of numbers: {digit}")

except Exception as e:
    print(f"Incorrect action{e}")
finally:
    print("End program\n")
