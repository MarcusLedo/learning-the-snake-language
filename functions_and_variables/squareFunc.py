def main():
    x = int(input("Enter x: "))
    print("x squared is ", square(x))


def square(num):
    return pow(num, 2)

main();