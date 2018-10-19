import random
STR_SIZE = 5
def rand_string():
    STR = ""
    for i in range(0, STR_SIZE):
        STR += random.choice("abcdefghijklmnopqrstuvwxyz" + "abcdefghijklmnopqrstuvwxyz".upper())
    return STR
test_file = open("test.txt", "w")
NODE_COUNT = 10
CONNECTION_COUNT = 10
nodes = []
for i in range(0, NODE_COUNT):
    nodes.append(rand_string())
    print(nodes[-1])

layers = []

count = len(nodes)
layer = 0
while 0 < len(nodes):
    num = random.randint(1, min(len(nodes), int(count / 2)))
    layers.append([])
    for i in range(0, num):
        node = random.choice(nodes)
        nodes.remove(node)
        layers[layer].append(node)
    layer += 1

while count > 0:
    startLayer = random.randint(0, len(layers) - 2)
    endLayer = random.randint(startLayer + 1, len(layers) - 1)

    test_file.write(random.choice(layers[startLayer]) + " " + random.choice(layers[endLayer]) + "\n")

    count -= 1