Group 13 Matthew Meadwell, Sean McLennan

1.) Project Description
    Our task was to implement a depth first search and a breadth first search for any given graph. On top on being able to do the standard depth first and breadth first we also had to implement an extended list option which saved nodes as they were visited. This implementation would cause the two different algorithms to perform better using the extended list option compared to the standard search.

2.) Group Member Contribution
    Matthew Meadwell: 50%
    Sean McLennan: 50%

3.) We used python for this project. Compiling instructions are below.
    -first make sure both the python file and the txt file containing the graph are in the same directory
    -Once both are in the same directory open a terminal in that directory and type "python3 search.py -dest 10 -bfs -e graph.txt"
    -The parameters in the command line arguments can be changed according to the project specifications.
    -If the following instruction is input correctly you should see the output of the program.

4.) Below are some same test runs
    
    python3 search.py -dest 40 -bfs node_50.txt

    Path: 1 -- 8 -- 21 -- 28 -- 40
    edges: 77
    vertices: 27
    1.279 ms
    ------------------------------------------------
    python3 search.py -dest 40 -bfs node_50.txt

    Path: 1 -- 8 -- 21 -- 28 -- 40
    edges: 77
    vertices: 27
    1.765 ms
    ------------------------------------------------
    python3 search.py -dest 40 -dfs node_50.txt

    Path: 1 -- 24 -- 47 -- 23 -- 7 -- 30 -- 9 -- 38 -- 17 -- 21 -- 28 -- 40
    edges: 34
    vertices: 34
    1.430 ms
    ------------------------------------------------
    python3 search.py -dest 40 -dfs -e node_50.txt

    Path: 1 -- 24 -- 47 -- 23 -- 7 -- 30 -- 9 -- 38 -- 17 -- 21 -- 28 -- 40
    edges: 34
    vertices: 34
    1.311 ms

5.) Existing Bugs
    The only bug we were running into is when the extended list option is ran using windows it ALWAYS produces a execution time that is smaller compared to not using the extended list option. On linux this does not seems to be the case the execution time for the extended option fluctuates a lot more and sometimes the extended option will be slower than the standard search, but there was no consistancy to this error so finding the fix was very difficult.

    Based on the tests that we ran the extended list option should be working as intended according to the project specifications.  