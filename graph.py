class graph:
    
    def __init__(self):
        self.adjList = dict()

    def readGraph(self, fileName):
        for line in open(fileName):
            print(line)
            nodes = line.split()
            if nodes[0] in self.adjList:
                if nodes[1] not in self.adjList[nodes[0]]:
                    self.adjList[nodes[0]].append(nodes[1])
            else:
                self.adjList[nodes[0]] = [nodes[1]]

    def printAdjList(self):
        for key in self.adjList:
            print(key + ", " +  str(self.adjList[key]))
