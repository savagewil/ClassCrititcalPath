from graph import graph

def main():
    g = graph()
    g.readGraph("test.txt")
    g.printAdjList()

if __name__ == "__main__":
    main()
