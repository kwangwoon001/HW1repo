def print_hello(amount):
    for i in range(amount):
        print("Line {}: Hello World!".format(i+1))

def print_bye():
    print("Good Bye...")

if __name__ == "__main__":
    num = int(input("Enter a number: "))
    print_hello(num)
    print_bye()