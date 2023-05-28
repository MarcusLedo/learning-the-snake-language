def main():
    x = int(input("What is x: "))
    print(f"{x} ^ 2 = {square(x)}")



def square(x):
    return x * x


if __name__ == "__main__":
    main()