import sys
import fileinput

#this class might not be needed at the moment leaving them in here just in case

# class Node:
#     def __init__(self, value):
#         self.value = value
#         self.next = None
#         self.visited = False
    
#     def CheckValue(self):
#         print(self.value)
    
#     def CheckNext(self):
#         print(self.next)


#this class we may not need but I am leaving it in here just in case.

# class Graph:
#     def __init__(self, vertices):
#         self.vertices = vertices
#         self.list = [None] * (int(self.vertices) + 1)

#     def AddEdge(self, source, dest):
#         source = int(source)
#         dest = int(dest)

#         node = Node(dest)
#         node.next = self.list[source]
#         self.list[source] = node

#         node = Node(source)
#         node.next = self.list[dest]
#         self.list[dest] = node



if __name__ == "__main__":

    if len(sys.argv) > 1:
        for x in range(0, len(sys.argv)):
            sys.argv[x] = sys.argv[x].lower()
            if sys.argv[x].__contains__(".txt"):
                filename = sys.argv[x]
            elif sys.argv[x].__contains__("dest"):
                dest = sys.argv[x + 1]
            elif sys.argv[x].__contains__("dfs"):
                search = sys.argv[x]
            elif sys.argv[x].__contains__("bfs"):
                search = sys.argv[x]
            elif sys.argv[x].__contains__("test"):
                filename = "graph.txt"
                search = "dfs"
                dest = 6
    else:
        print("please enter command line arguments")
        exit()

    file = open(filename, "r")

    vertices = int(file.readline())
    #for old way leave just in case
    #graph = Graph(vertices)
    graph = {}

    for line in file:
        info = line.replace("\n", "").strip().split(" ")
        source = int(info[0])
        info.pop(0)
        for vert in info:
            if int(vert) != source:
                #for old way leave just in case
                #graph.AddEdge(source, int(vert))
                graph[source] = set(info)


    for line in graph:
        print(line, graph[line])
        
    file.close()