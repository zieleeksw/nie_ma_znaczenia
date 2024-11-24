def print_names(names: list[str]):
    if len(names) != 5:
        print("You need to pass 5 names")
        return []

    print(names)


names = ["Patricio", "Juliet", "Jacob", "Tomas", "Roberto"]

print_names(names)


names = ["Patricio", "Juliet", "Jacob", "Tomas", "Roberto", "Marco"]

print_names(names)
