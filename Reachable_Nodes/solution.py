
def reachableNodes(adj_list, start_node):
    reachableNodes = []
    toVisit = []
    reachableNodes.append(start_node)
    toVisit.append(start_node)
    
    while not toVisit == []:
        targetNode = toVisit.pop(0)
        for node in adj_list[targetNode]:
            if not node in reachableNodes:
                reachableNodes.append(node)
                toVisit.append(node)

    return set(sorted(reachableNodes))


if __name__ == "__main__":
    adjList = [[1, 3], [2], [0], [4], [3], []]
    print(reachableNodes(adjList, 2))