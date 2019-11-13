import json
import argparse
import random
import datetime
random.seed(datetime.datetime.now())

parser = argparse.ArgumentParser(description='Generate random topology.')
parser.add_argument('-n', default=16, help='number of nodes (default: 16)')
parser.add_argument('-p', default=0.5, help='the probability for each pair of node to be connected (default: 0.3)')
parser.add_argument('-o', default='topo.json', help='out put file')
regions = [0, 1, 2, 3, 4, 5]
args = parser.parse_args()
args.n = int(args.n)
args.p = float(args.p)
topo = {"nodes":[]}
for i in range(args.n):
    node = {"id": i, "region": random.sample(regions, 1)[0], "isMiner": True, "hashRate": random.random(), "neighbor":[]}
    topo["nodes"].append(node)

for i in range(0, args.n):
    if(i > 0 and len(topo["nodes"][i]["neighbor"]) == 0):
        # to make sure there is a path between any two nodes, we force a node to be connected to a randomly selected former node
        forcedNeighbor = random.sample(range(0, i), 1)[0]
        topo["nodes"][i]["neighbor"].append({"id": forcedNeighbor})
        topo["nodes"][forcedNeighbor]["neighbor"].append({"id": i})
    for j in range(i+1, args.n):
        if random.random() < args.p:
            topo["nodes"][i]["neighbor"].append({"id": j})
            topo["nodes"][j]["neighbor"].append({"id": i})

for i in range(0, args.n):
    print('# neighbor for node {}: {}'.format(i, len(topo["nodes"][i]["neighbor"])))


with open(args.o, "w") as write_file:
    json.dump(topo, write_file, sort_keys=True, indent=4)
