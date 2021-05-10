import math


#edge structure
class Edge:
    def __init__(self,endPoint1,endPoint2, cost):
                self.endPoint1=endPoint1
                self.endPoint2=endPoint2
                self.cost=cost


#function to search valid edges for the lowest cost edge that connects a new node
def enterNextNode(edgeList, optEdgeList, unconnectedNodes, connectedNodes, totalCost, altCounter):
    altCounter

    #if no nodes are connected yet, connect node 1
    if not connectedNodes:
        connectedNodes.append(1)
        unconnectedNodes.remove(1)

    #finds lowest costing edge to an unconnected node and connects it
    if unconnectedNodes:
        posEdgeList = []
        for i in edgeList:
            if ((i.endPoint1 in connectedNodes and i.endPoint2 in unconnectedNodes) or (i.endPoint1 in unconnectedNodes and i.endPoint2 in connectedNodes)):
                posEdgeList.append(i)
        posEdgeList.sort(key=lambda x: x.cost)

        optEdgeList.append(posEdgeList[0])
        totalCost += (posEdgeList[0].cost)
        if posEdgeList[0].endPoint1 in unconnectedNodes:
           connectedNodes.append(posEdgeList[0].endPoint1)
           unconnectedNodes.remove(posEdgeList[0].endPoint1)
        elif posEdgeList[0].endPoint2 in unconnectedNodes:
           connectedNodes.append(posEdgeList[0].endPoint2)
           unconnectedNodes.remove(posEdgeList[0].endPoint2)

        #if there are multiple lowest cost edges ie. alternative optimal solutions
        if posEdgeList[0].cost == posEdgeList[1].cost:
            if posEdgeList[1].cost == posEdgeList[2].cost:
                altCounter = 2
                print("Has 2 alternative optimal solutions: edges from "+str(posEdgeList[1].endPoint1)+" to "+str(posEdgeList[1].endPoint2)+" and from "+str(posEdgeList[2].endPoint1)+" to "+str(posEdgeList[2].endPoint2))
            else:
                altCounter = 1
                print("Has 1 alternative optimal solution: edge from "+str(posEdgeList[1].endPoint1)+" to "+str(posEdgeList[1].endPoint2))

        return edgeList, optEdgeList, unconnectedNodes, connectedNodes, totalCost, altCounter;

def main():
    #list of all edges
    edgeList = []
    #list of edges in optimal solution
    optEdgeList = []
    #list of nodes that have not yet been connected
    unconnectedNodes = []
    #list of nodes already connected
    connectedNodes = []
    #total cost of tree
    totalCost = 0
    #number of alternative optimal solutions
    altCounter = 0

    #user input - is this solving problem 1 or 2
    problemNum = int(input("Enter the number of the problem to be solved: "))
    if problemNum == 1:
        edgeList = [Edge(1, 2, 1), Edge(1, 3, 5), Edge(1, 4, 7), Edge(1, 5, 9), Edge(2, 3, 6), Edge(2, 4, 4), Edge(2, 5, 3), Edge(3, 4, 5), Edge(3, 6, 10), Edge(4, 5, 8), Edge(4, 6, 3)]
        unconnectedNodes = [1, 2, 3, 4, 5, 6]

    elif problemNum == 2:
        edgeList = [Edge(1, 2, 1), Edge(1, 3, 2), Edge(1, 4, 3), Edge(2, 5, 18), Edge(3, 5, 5), Edge(3, 6, 10), Edge(3, 8, 25), Edge(4, 6, 4), Edge(5, 7, 7), Edge(5, 8, 22), Edge(6, 8, 8), Edge(6, 9, 6), Edge(7, 10, 10), Edge(8, 10, 10), Edge(9, 10, 10)]
        unconnectedNodes = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    #iterates the function to connect all the nodes and prints progress after every iteration
    for i in range(len(unconnectedNodes)-1):
        edgeList, optEdgeList, unconnectedNodes, connectedNodes, totalCost, altCounter = enterNextNode(edgeList, optEdgeList, unconnectedNodes, connectedNodes, totalCost, altCounter)
        #print statements
        print("Connected nodes: "+str(connectedNodes))
        print("Unconnected nodes: "+str(unconnectedNodes))
        if optEdgeList:
            print("Connecting edges: ")
            for i in optEdgeList:
                print("node "+str(i.endPoint1)+" to node "+str(i.endPoint2))

        print("Total cost = "+str(totalCost)) 

    print("Alternate optimal solutions: "+str(altCounter))

main()