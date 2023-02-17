class Hamiltonian:

    #constr. to set starting point to 0
    def __init__(self, start):
        self.start = start
        # empty list to store the cycle
        self.c = []
        # set the cycle bool to False until found
        self.ifhamil = False
        # to acknowledge the path hamilton
        self.path = False

    # function to set the starting point/vertex
    def find(self):
        # add starting vertex to the list
        self.c.append(self.start)
        # starting the search
        self.search(self.start)


    def search(self, vertex):
        # condition if the vertex is not equal to the start vertex and all nodes have been visited, so it's a path
        if vertex != self.start and len(self.c) == N :
            if self.path != True:
                self.ifhamil = True
                # output it's a path
                print("It's a Hamilton Path")
                self.path = True


            # since every circuit has a path, condition if the vertex is the start vertex and all nodes have been visited
            # incluing the start vertex, so it's a circuit
        if vertex == self.start and len(self.c) == N+1 :
            self.ifhamil = True

            # output it's a circuit
            print("It's a Hamilton Circuit")

            exit(0)


        # iterate through all graph vertices
        for i in range(N):
            if graph[vertex][i] == 1 and visited[i] == 0:
                # variable to change the staring point every iteration til reaches no. of vertices
                ch = i
                # add 1 for the visited vertex in the list visited
                visited[ch] = 1
                # add the visited vertex in the list of the cycle
                self.c.append(ch)
                # call the function again (recursion)
                self.search(ch)

                # Backtracking to set the last visited vertex to 0 if not found to be linked
                # and delete it from the cycle list
                visited[ch] = 0
                self.c.pop()



if __name__ == '__main__':
    # N = eval(input("Number of vertices: "))
    # print("Enter the 2D graph in order.i.e (1 for connected & 0 for not)")
    # graph = []
    # for i in range (N):
    #     a = []
    #     for j in range (N):
    #         a.append(int(input()))
    #     graph.append(a)

    graph    =   [[0, 1, 0, 0, 0],
                  [1, 0, 1, 0, 0],
                  [0, 1, 0, 1, 0],
                  [0, 0, 1, 0, 1],
                  [0, 0, 0, 1, 0]]
    # number of vertices in the graph
    N=5

    # list to set 0 for every vertix until it's visited
    visited = [0 for x in range(N)]

    # if Circuit
    h = Hamiltonian(0)
    h.find()

    # if not Circuit
    if not h.ifhamil:
            print("Not a Hamiltonian Graph!")
