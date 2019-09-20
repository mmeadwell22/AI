import sys
import time

if __name__ == "__main__":

    extend = " "
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
            elif sys.argv[x].__contains__("-e"):
                extend = "true"
    else:
        print("please enter command line arguments")
        exit()

    startTime = time.time()
    file = open(filename, "r")
    start = 1

    vertices = int(file.readline())
    global graph
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
                    return [(edges, numOfVertices, path + [next])]
                else:
                    stack.append((next, path + [next]))
                   
                    edges += 1
                numOfVertices += 1

    def dfs_paths_ext(graph, start, goal):
        global edges, numOfVertices
        extSet = set()
        stack = [(start, [start])]
        while stack:
            (vertex, path) = stack.pop()
            list = graph[vertex] - set(path) - extSet
            i = 0
            for next in graph[vertex] - set(path):
                i +=1
                if next == goal:
                    return [(edges, numOfVertices, path + [next])]
                else:
                    if(i == len(list)):
                        extSet.add(vertex)
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
                    
                    return [(edges, numOfVertices, path +[next])]
                else:
                    queue.append((next, path + [next]))
                    edges += 1

    def bfs_paths_ext(graph, start, goal):
        global edges, numOfVertices
        extSet = set()
        queue = [(start, [start])]
        while queue:
            (vertex, path) = queue.pop(0)
            numOfVertices += 1
            list = graph[vertex] - set(path) - extSet
            j = 0
            for next in list:
                j+=1
                if next == goal:
                    return [(edges, numOfVertices, path + [next])]
                else:
                    if j == len(list):
                        extSet.add(vertex)
                    queue.append((next, path + [next]))
                    edges += 1
    
    if search.__contains__("bfs"):
        if extend == "true":
            searchComp = bfs_paths_ext(graph, start, dest) 
        else:
            searchComp = bfs_paths(graph, start, dest)
    else:
        if extend == "true":
            searchComp = dfs_paths_ext(graph, start, dest)
        else:
            searchComp = dfs_paths(graph, start, dest)
        
    listResult = list(searchComp[0])
    print("Path:", end=" ")
    print(" -- ".join(list(map(str,listResult[2]))))  
    print("edges: %d" % listResult[0])
    print("vertices: %d" % listResult[1])
    print("%.3f ms" % ((time.time() - startTime) * 1000))
