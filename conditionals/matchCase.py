name = input("What is your name?\n");

match name:
    case "Harry" | "Hermione" | "Ron":
        print("Gryffindor");
    case "Draco":
        print("Slytherin");
    case _:
        print("Who?")