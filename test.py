def print_hello(amount):
    for _ in range(amount):
        print("Hello World!")

if __name__ == "__main__":
    num = int(input("Enter a number: "))
    print_hello(num)
