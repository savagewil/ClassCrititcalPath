from graph import graph

def shell():
    while command.to_lower() != "q":
        command = input("> ")
        if command == "critical path":

        print(command)

def main():
    g = graph()
    g.readGraph("test.txt")
    shell()

if __name__ == "__main__":
    main()
