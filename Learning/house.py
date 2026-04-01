name = input("What's your name? ").capitalize()

match name:
    case "Harry" | "Hermione" | "Ron":
        print("Gryffindor")
    case "Hermione":
        print("Gryffindor")
    case "Ron":
        print("Gryffindor")
    case "Draco":
        print("Slytherin")
    case _:
        print("who?")