class graphVertex(object):
    """
    represents a vertex
    """
    def __init__(self, value):
        """
        initialising class attributes
        """
        self.value = value
        self.attached = []
        self.distance = -1

    def getValue(self):
        return self.value

    def getAttachedVertices(self):
        return self.attached

    def getDistance(self):
        return self.distance

    def setDistance(self, distance):
        self.distance = distance

    def attachVertex(self, vertex, edgeLength):
        """
        appends a tupple with first element
        as the vertex instance and the second
        as the edge length
        """
        self.attached.append((vertex,edgeLength))

def makeVertices(numVertices):
    """
    returns a list of vertices
    """
    vertices = []
    for i in range(numVertices):
        vertices.append(graphVertex(i + 1))
    return vertices

def makeEdges(numEdges, vertices):
    """
    joins vertices with edges
    with respective weights
    """
    for edge in range(numEdges):
        s = raw_input('Enter the two vertices and edge length between them: ')
        v1, v2, edgeLength = s.split(' ')
        v1, v2, edgeLength = vertices[int(v1) - 1], vertices[int(v2) - 1], int(edgeLength)
        v1.attachVertex(v2, edgeLength)
        v2.attachVertex(v1, edgeLength)

def setDistances(root):
    """
    sets distances of all nodes from the given root vertex
    """
    queue = [root]
    while True:
        if queue == []:
            return
        here = queue.pop(0)
        
        attached = here.getAttachedVertices()
        distance = here.getDistance()

        for vertex in attached:
            if vertex[0].getDistance() < 0 or vertex[0].getDistance() > distance + vertex[1]:
                vertex[0].setDistance(distance + vertex[1])
                queue.append(vertex[0])

def printDistances(vertices, start):
    """
    prints distances set in the graphVertex
    instances
    """
    for vertex in vertices:
        if vertex.getValue() != start:
        	print (str(start) + ' to ' + str(vertex.getValue()) + ' distance: ' + str(vertex.getDistance()))
    print ''

def main():
    T = 1
    for t in range(T):
        s = raw_input('Enter number of vertices and number of edges respectively: ')
        numVertices, numEdges = s.split(' ')
        numVertices, numEdges = int(numVertices), int(numEdges)
        vertices = makeVertices(numVertices)
        makeEdges(numEdges, vertices)
        start = int(input('Which vertex would you like to start from? '))
        root = vertices[start - 1]
        root.setDistance(0)
        setDistances(root)
        printDistances(vertices, start)
        
main()
