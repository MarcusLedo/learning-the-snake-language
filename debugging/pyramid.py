def main():
    height = int(input("Height: "))
    drawing_pyramid(height)




def drawing_pyramid(height):
    for i in range(height):
        print('#' * (i + 1), end = "\n")


main()

