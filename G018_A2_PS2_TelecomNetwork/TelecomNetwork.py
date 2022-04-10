# 
# Program to find the minimum spanning tree using Kruskals algorithm
# 

# File connection for input and output
inputFile = open('inputPS2.txt', 'r')
outputFile = open('outputPS2.txt', 'w')

#Initialising the arrays 
#Containing vertices and edges of the graph
vertices = []
edges = []

#Class defining edges for the graph
class Edge:
    def __init__(self, source, dest, weight):
        self.source = source
        self.dest = dest 
        self.weight = weight

#Function to find parent of the vertex of the graph
def findParent(vertices, vertex, parent):
    if parent[vertices.index(vertex)] == vertex:
        return vertex
    return findParent(vertices, parent[vertices.index(vertex)], parent)

#Function finding MST using Kruskals algorithm
def kruskals(vertices, edges , num_Of_Vertices, num_Of_Edges):
    edges = sorted(edges, key=lambda item: item.weight)

    output = []
    parent = []

    #print("Edges :", edges)

    for i in range(num_Of_Vertices):
        parent.append(vertices[i])
    
    #print("Parent :" ,parent)

    count = 0
    i = 0

    while count != num_Of_Vertices-1:
        currentEdge = edges[i]
        
        #check if currentEdge is in MST ot not
        sourceParent = findParent(vertices, currentEdge.source, parent)
        destParent = findParent(vertices, currentEdge.dest, parent)

        if sourceParent != destParent:
            output.append(currentEdge)
            count += 1
            parent[vertices.index(sourceParent)] = destParent

        i += 1
    
    #printing the edges to outFile
    mini_cost = 0
    num = 0
    outputFile.write("The offices can be connected as\n\n")
    for i in range(num_Of_Vertices - 1):
        num += 1
        #print(output[i].source, " ",  output[i].dest , " ", output[i].weight)
        mini_cost += output[i].weight
        string = "(" + output[i].source+ "," + output[i].dest + ")"
        if num != num_Of_Vertices - 1:
            string = string + ", "
        outputFile.write(string)
    #print("mini_cost :", mini_cost)
    outputFile.write("\n\nThe minimum cost of connecting the offices is ")
    outputFile.write(str(mini_cost))
    outputFile.close()


#main() function
def main():
    #vertices from inputFile
    for i in inputFile.readlines():
        l = i.split('/')
        u = l[0].strip()
        v = l[1].strip()
        if u not in vertices:
            vertices.append(u)
        if v not in vertices:
            vertices.append(v)
    num_Of_Vertices = len(vertices)

    #print("Vertices :",vertices)
    
    #edges from inputFile
    inputFile.seek(0)   #resetting the cursor of the file
    for i in inputFile.readlines():
        i = i.split('/')
        u = i[0].strip()
        v = i[1].strip()
        w = int(i[2].strip())
        e = Edge(u, v, w)
        #print("edge created")
        edges.append(e)
    num_Of_Edges = len(edges)

    #Find MST
    kruskals(vertices, edges, num_Of_Vertices, num_Of_Edges)


if __name__ == "__main__":
    main()

