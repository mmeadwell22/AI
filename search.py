import sys
import time
from datetime import datetime

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

    startTime = time.time()
    if len(sys.argv) > 1:
        for x in range(0, len(sys.argv)):
            sys.argv[x] = sys.argv[x].lower()
            if sys.argv[x].__contains__(".txt"):
                filename = sys.argv[x]
            elif sys.argv[x].__contains__("dest"):
                dest = int(sys.argv[x + 1])
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
    # filename = "graph.txt"
    # dest = 10
    # search = "dfs"


    file = open(filename, "r")
    start = 1

    vertices = int(file.readline())
    #for old way leave just in case
    #graph = Graph(vertices)
    graph = {}
    edges = 0
    numOfVertices = 0

    for line in file:
        info = line.replace("\n", "").strip().split(" ")
        source = int(info[0])
        info.pop(0)
        for vert in range(0, len(info)):
            info[vert] = int(info[vert])
        for vert in info:
            if vert != source:
                #for old way leave just in case
                #graph.AddEdge(source, int(vert))
                graph[source] = set(info)

    file.close()

    def dfs_paths(graph, start, goal):
        global edges, numOfVertices
        stack = [(start, [start])]
        while stack:
            (vertex, path) = stack.pop()
            temp = set(path)
            for next in graph[vertex] - set(path):
                if next == goal:
                    yield path + [next]
                else:
                    stack.append((next, path + [next]))
                    edges += 1
                numOfVertices += 1

    def bfs_paths(graph, start, goal):
        global edges, numOfVertices
        queue = [(start, [start])]
        while queue:
            (vertex, path) = queue.pop(0)
            numOfVertices += 1
            for next in graph[vertex] - set(path):
                if next == goal:
                    yield path + [next]
                else:
                    queue.append((next, path + [next]))
                    edges += 1



    def shortestPathbfs(graph, start, dest):
        try:
            return next(bfs_paths(graph, start, dest))
        except StopIteration:
            return None
    
    def shortestPathdfs(graph, start, dest):
        try:
            return (next(dfs_paths(graph, start, dest)))
        except StopIteration:
            return None


    if search.__contains__("bfs"):
        print(shortestPathbfs(graph, start, dest))
    else:
        print(shortestPathdfs(graph, start, dest))  
    
    print("edges %d" % edges)
    print("vertices %d" % vertices)
    

    print("%.3f ms" % ((time.time() - startTime) * 1000))