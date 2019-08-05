class Graph:
    def __init__(self):        
        self.vertices = {}
        
    def addVertex(self, vertex):
        if vertex not in self.vertices:  
            lengthOfVertices = len(self.vertices) #length of before adding new vertex
            self.vertices[vertex] = [0 for i in range(lengthOfVertices + 1)]
            # Iterating over keys 
            for v in self.vertices: 
                if v != vertex:
                    self.vertices[v].append(0)
                                
    def addEdge(self, start, end, weight=1):
        if start not in self.vertices:
            self.addVertex(start)
        if end not in self.vertices:
            self.addVertex(end)                
        endIndex = list(self.vertices.keys()).index(end)
        self.vertices[start][endIndex] = weight
            
          
    def dummyGraph(self):
        self.addVertex('A')
        self.addVertex('B')
        self.addVertex('C')
        self.addVertex('D')
        self.addVertex('E')
        self.addVertex('F')        
        
        self.addEdge('A','B')
        self.addEdge('B','A')        
        self.addEdge('A','C')
        self.addEdge('C','D')        
        self.addEdge('D','E')
        self.addEdge('E','F')        