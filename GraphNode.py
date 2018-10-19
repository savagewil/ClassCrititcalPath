class GraphNode:
    def __init__(self, name, weight):
        self.earlyStart = None
        self.earlyFinish = None
        self.lateStart = None
        self.lateFinish = None
        self.weight = weight
        self.connectionsTO = []
        self.connectionsFrom = []
        self.name = name.strip()

    def addConnectionTo(self, node):
        if (node not in self.connectionsTO):
            self.connectionsTO.append(node)

    def addConnectionFrom(self, node):
        if (node not in self.connectionsFrom):
            self.connectionsFrom.append(node)

    def __str__(self):
        return self.name + " " + str(self.earlyStart) + " " + str(self.lateFinish) + " " + str(self.weight)
