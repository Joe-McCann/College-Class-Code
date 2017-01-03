try:
    word = input("Number: ")
    num = int(word)
    print(num)
except ValueError:
    print("Exception Thrown: Enter digits")

print("we survived")
