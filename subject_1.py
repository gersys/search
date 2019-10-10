# [the number of missionaries, cannibals at left of river , and the location of boat (left 1, right 0)]

frontiers=[]
explored=[]
sol=[]


class AStar:
    def __init__(self,prob):
        self.prob=prob
        self.expand=0

    def solution(self):
        print("A* search start")
        initial_node = A_star_Node(self.prob.init, None, 0, self.prob.init[0], 0)

        frontiers = self.derive_succ(initial_node)
        explored.append(initial_node.state)


        while (len(frontiers) != 0):
            f_cost = []
            for i in frontiers:
                f_cost.append(i.f_cost)
            argmax=-max((x, -i) for i, x in enumerate(f_cost))[1]

            f0 = frontiers.pop(argmax)

            if f0.state == [0, 0, 0]:
                print("Congratulations! it's a goal : {}".format(f0.state))
                sol.append(f0)
                break

            explored.append(f0.state)
            frontiers = frontiers + self.derive_succ(f0)

            print("explored:")
            for i in explored:
                print(i)
            print("frontiers:")
            for i in frontiers:
                print(i)

            print("--------------------------------")

        print("solution list")
        for i in sol:
            print(i)
        print("--------------------------------")

        self.sol_path(sol)
        return self.expand

    def derive_succ(self,input_node):
        state_list = input_node.state
        succ_list = []
        l_m = state_list[0]
        l_c = state_list[1]
        r_m = 3 - state_list[0]
        r_c = 3 - state_list[1]
        boat = state_list[2]
        if (l_m < l_c and l_m != 0) or (r_m < r_c and r_m != 0):
            return self.make_Qnode(input_node, succ_list)

        if state_list[2] == 1:
            for i in range(2):
                if l_m - (i + 1) >= 0:
                    succ_list.append([l_m - (i + 1), l_c, 0])
                    self.expand = self.expand + 1
            for i in range(2):
                if l_c - (i + 1) >= 0:
                    succ_list.append([l_m, l_c - (i + 1), 0])
                    self.expand = self.expand + 1
            if l_m - 1 >= 0 and l_c - 1 >= 0:
                succ_list.append([l_m - 1, l_c - 1, 0])
                self.expand = self.expand + 1

        elif state_list[2] == 0:
            for i in range(2):
                if r_m - (i + 1) >= 0:
                    succ_list.append([l_m + (i + 1), l_c, 1])
                    self.expand = self.expand + 1
            for i in range(2):
                if r_c - (i + 1) >= 0:
                    succ_list.append([l_m, l_c + (i + 1), 1])
                    self.expand = self.expand + 1
            if r_m - 1 >= 0 and r_c - 1 >= 0:
                succ_list.append([l_m + 1, l_c + 1, 1])
                self.expand = self.expand + 1

        return self.make_Qnode(input_node, succ_list)

    def make_Qnode(self, parent_node, suc_list):
        Q = []
        for i in suc_list:
            suc_node = A_star_Node(i, parent_node, parent_node.g_cost + 1,i[0], parent_node.depth + 1)
            if suc_node.state in explored:
                print("jump")
                continue
            else:
                Q.append(suc_node) #replace if there are same state in frontier
        return Q

    def sol_path(self,sol_list):
        for sol in sol_list:
            while (sol.parent != None):
                print(sol)
                sol = sol.parent
            print(sol)

            print("done")


class Problem:
    def __init__(self, a, b):
        self.init = a
        self.goal = b
        #self.model = m

    def goal_test(self, state):
        if self.goal == state:
            return True
        else:
            return False

    def sucFN(self, state):
        childrens = derive_succ(state)
        return childrens

    def __str__(self):
        return 'goal: ' + self.goal

class A_star_Node:
    def __init__(self,s,p,g,h,d):
        self.state = s
        self.parent = p
        self.g_cost = g
        self.h_cost=h
        self.f_cost=g+h
        self.depth = d
        # self.action = a

    def __str__(self):
        try:
            return 'S: ' + str(self.state) +', P: ' + str(self.parent.state) + ', depth = ' + str(self.depth) + ', f_cost : ' +str(self.f_cost) +'='+ str(self.g_cost)+'+'+str(self.h_cost)
        except AttributeError:
            return 'S: ' + str(self.state) + ', P: ' + "None" + ', depth = ' + str(self.depth) + ', f_cost : ' +str(self.f_cost) +'='+ str(self.g_cost)+'+'+str(self.h_cost)


    def solution(self):
        sol = self.state
        if self.depth == 0:
            return sol
        else:
            return sol + '<==' + self.parent.solution()

prob=Problem([3,3,1],[0,0,0])


astar=AStar(prob)
expand=astar.solution()
print("Node generated:{}".format(expand))


class Node:
    def __init__(self,s,p,c,d):
        self.state = s
        self.parent = p
        self.cost = c
        self.depth = d
        # self.action = a

    def __str__(self):
        try:
            return 'S: ' + str(self.state) +', P: ' + str(self.parent.state) + ', depth = ' + str(self.depth) + ', cost = ' + str(self.cost)
        except AttributeError:
            return 'S: ' + str(self.state) + ', P: ' + "None" + ', depth = ' + str(self.depth) + ', cost = ' + str(self.cost)


    def solution(self):
        sol = self.state
        if self.depth == 0:
            return sol
        else:
            return sol + '<==' + self.parent.solution()

class BFS:
    def __init__(self,prob):
        self.prob=prob
        self.expand = 0

    def make_Qnode(self,parent_node, suc_list):
        Q = []
        for i in suc_list:
            suc_node = Node(i, parent_node, parent_node.cost + 1, parent_node.depth + 1)
            if suc_node.state in explored:
                print("jump")
                continue
            else:
                Q.append(suc_node)
        return Q

    def derive_succ(self,input_node):
        state_list = input_node.state
        succ_list = []
        l_m = state_list[0]
        l_c = state_list[1]
        r_m = 3 - state_list[0]
        r_c = 3 - state_list[1]
        boat = state_list[2]
        if (l_m < l_c and l_m != 0) or (r_m < r_c and r_m != 0):
            return self.make_Qnode(input_node, succ_list)

        if state_list[2] == 1:
            for i in range(2):
                if l_m - (i + 1) >= 0:
                    succ_list.append([l_m - (i + 1), l_c, 0])
                    self.expand=self.expand+1
            for i in range(2):
                if l_c - (i + 1) >= 0:
                    succ_list.append([l_m, l_c - (i + 1), 0])
                    self.expand = self.expand + 1
            if l_m - 1 >= 0 and l_c - 1 >= 0:
                succ_list.append([l_m - 1, l_c - 1, 0])
                self.expand = self.expand + 1

        elif state_list[2] == 0:
            for i in range(2):
                if r_m - (i + 1) >= 0:
                    succ_list.append([l_m + (i + 1), l_c, 1])
                    self.expand = self.expand + 1
            for i in range(2):
                if r_c - (i + 1) >= 0:
                    succ_list.append([l_m, l_c + (i + 1), 1])
                    self.expand = self.expand + 1
            if r_m - 1 >= 0 and r_c - 1 >= 0:
                succ_list.append([l_m + 1, l_c + 1, 1])
                self.expand = self.expand + 1

        return self.make_Qnode(input_node, succ_list)

    def sol_path(self,sol_list):
        for sol in sol_list:
            while (sol.parent != None):
                print(sol)
                sol = sol.parent
            print(sol)

            print("done")

    def solution(self):
        print("BFS search start")
        initial_node = Node(self.prob.init, None, 0, 0)

        frontiers = self.derive_succ(initial_node)
        explored.append(initial_node.state)

        while (len(frontiers) != 0):

            f0 = frontiers.pop(0)
            if f0.state == [0, 0, 0]:
                print("Congratulations! it's a goal : {}".format(f0.state))
                sol.append(f0)
                break


            explored.append(f0.state)
            frontiers = frontiers + self.derive_succ(f0)

            print("explored:")
            for i in explored:
                print(i)
            print("frontiers:")
            for i in frontiers:
                print(i)

            print("--------------------------------")

        print("solution list")
        for i in sol:
            print(i)
        print("--------------------------------")

        self.sol_path(sol)
        return self.expand





#bfs=BFS(prob)
#expand=bfs.solution()
#print("Node generated:{}".format(expand))





# graph={
#     "[3,3,1]" : ["[3,2,0]","[3,1,0]","[2,3,0]","[1,3,0]","[2,2,0]"],
#     "[3,2,0]" : ["[3,3,1]"],
#     "[3,1,0]" : ["[3,3,1]","[3,2,1]"],
#     "[2,3,0]" : -1, #Game Over
#     "[1,3,0]" : -1,
#     "[2,2,0]" : ["[3,2,1]","[2,3,1]","[3,3,1]"],
#     "[3,2,1]" : ["[3,0,0]","[3,1,0]","[2,2,0]","[1,2,0]","[2,1,0]"],
#     "[2,3,1]" : -1,
#     "[3,0,0]" : ["[3,2,1]","[3,1,1]"],
#     "[1,2,0]" : -1,
#     "[2,1,0]" : -1,
#     "[3,1,1]" : ["[3,0,0]","[2,1,0]","[1,1,0]","[2,0,0]"],
#     "[1,1,0]" : ["[3,1,1]","[2,1,1]","[1,2,1]","[1,3,1]","[2,2,1]"],
#     "[2,1,1]" : -1,
#     "[1,2,1]" : -1,
#     "[1,3,1]" : -1,
#     "[2,2,1]" : ["[1,1,0]","[1,2,0]","[2,1,0]","[2,0,0]","[0,2,0]"],
#     "[2,0,0]" : -1,
#     "[0,2,0]" : ["[2,2,1]","[1,2,1]","[0,3,1]","[1,3,1]"],
#     "[0,3,1]" : ["[0,2,0]","[0,1,0]"],
#     "[0,1,0]" : ["[0,3,1]","[1,2,1]","[2,1,1]","[1,1,1]","[0,2,1]"],
#     "[1,1,1]" : ["[0,1,0]","[1,0,0]","[0,0,0]"],
#     "[1,0,0]" : -1,
#     "[0,0,0]" : 0, # goal
#     "[0,2,1]" : ["[0,1,0]","[0,0,0]"]
# }
