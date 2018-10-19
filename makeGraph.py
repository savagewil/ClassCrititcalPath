import GraphNode
FILE_NAME = "test.txt"
FILE = open(FILE_NAME, 'r')
names = []
nodes = []
for line in FILE:
    line = line.split(" ")
    line[1] = line[1].strip()
    line[0] = line[0].strip()
    if line[0] not in names:
        names.append(line[0])
        nodes.append(GraphNode.GraphNode(line[0], 1))
    if line[1] not in names:
        names.append(line[1])
        nodes.append(GraphNode.GraphNode(line[1], 1))

    nodestart = nodes[names.index(line[0])]
    nodeend = nodes[names.index(line[1])]

    nodeend.addConnectionFrom(nodestart)
    nodestart.addConnectionTo(nodeend)
# print("-------------")
# for node in nodes:
#     print(node)
# print("-------------")
startNode = GraphNode.GraphNode("start", 0)
endNode = GraphNode.GraphNode("end", 0)
startNode.earlyStart = 0
nodes.append(startNode)
nodes.append(endNode)

startNodes = []
endsNodes = []
finishedNodesForward = []
finishedNodesBack = []
workingNodesForward = list(nodes)
workingNodesBack = list(nodes)


for node in nodes:
    if not node.connectionsFrom and startNode is not node:
        startNode.addConnectionTo(node)
        node.addConnectionFrom(startNode)
    if not node.connectionsTO and endNode is not node:
        endNode.addConnectionFrom(node)
        node.addConnectionTo(endNode)

startNodes.append(startNode)
endsNodes.append(endNode)

# for node in workingNodesForward:
#     print(node)

if not (startNodes and endsNodes):
    print("No Start or No end, No can do")
else:
    while len(finishedNodesForward) != len(nodes):
        startNode = None

        for node in workingNodesForward:
            if node.earlyStart is not None:
                if startNode is None:
                    startNode = node
                else:
                    if startNode.earlyStart > node.earlyStart:
                        startNode = node
        # print(startNode)
        # for node in workingNodesForward:
        #     print("\t" + str(node))
        finishedNodesForward.append(startNode)
        workingNodesForward.remove(startNode)

        for i in range(0, len(startNode.connectionsTO)):
            if startNode.connectionsTO[i].earlyStart is not None:
                startNode.connectionsTO[i].earlyStart = min(startNode.connectionsTO[i].earlyStart,
                                                               startNode.weight +
                                                               startNode.earlyStart)
            else:
                startNode.connectionsTO[i].earlyStart = startNode.weight + startNode.earlyStart

    # for node in nodes:
    #     print(node)

    for node in endsNodes:
        node.lateFinish = node.earlyStart + node.weight

        # print(node)

    while len(finishedNodesBack) != len(nodes):
        endNode = None

        for node in workingNodesBack:
            if node.lateFinish is not None:
                if endNode is None:
                    endNode = node
                else:
                    if endNode.lateFinish < node.lateFinish:
                        endNode = node

        finishedNodesBack.append(endNode)

        workingNodesBack.remove(endNode)

        for i in range(0, len(endNode.connectionsFrom)):
            if endNode.connectionsFrom[i].lateFinish is not None:
                endNode.connectionsFrom[i].lateFinish = max(endNode.connectionsFrom[i].lateFinish,
                                                            endNode.lateFinish - endNode.weight )
            else:
                endNode.connectionsFrom[i].lateFinish = endNode.lateFinish - endNode.weight

# for node in nodes:
#     for n in node.connectionsFrom:
#         print(n)
#     print("\t" + str(node))
#     for n in node.connectionsTO:
#         print("\t\t" + str(n))

node = endsNodes[0]

# print("--------------------")
# for n in node.connectionsFrom:
#     print(n)
print("--------------------")
while node != startNodes[0]:
    MAX = None
    for n in node.connectionsFrom:
        # print(n.lateFinish - n.earlyStart)
        # print(n.weight)
        if n.lateFinish - n.earlyStart == n.weight:
            MAX = n
    print(MAX)
    node = MAX