def print_hello(amount):
    for _ in range(amount):
        print("Hello World!")

def print_bye():
    print("Good Bye...")

if __name__ == "__main__":
    num = int(input("Enter a number: "))
    print_hello(num)
    print_bye()