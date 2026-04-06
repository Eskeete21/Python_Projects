def main():
    number = get_number()
    meow(number)


def meow(n):
    for _ in range(n):
        print("meow")


def get_number():
    while True:
        num = int(input("Enter a number: "))
        if num > 0:
            return num


main()