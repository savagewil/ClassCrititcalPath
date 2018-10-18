from graph import graph

def main():
    g = graph()
    g.readGraph("test.txt")
    g.printAdjList()
    g.writeToFile("test1.txt")

if __name__ == "__main__":
    main()
