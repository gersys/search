# [the number of missionaries, cannibals at left of river , and the location of boat (left 1, right 0)]

frontiers=[]
explored=[]
sol=[]

def derive_succ(input_node):
    state_list = input_node.state
    succ_list=[]
    l_m=state_list[0]
    l_c=state_list[1]
    r_m=3-state_list[0]
    r_c=3-state_list[1]
    boat=state_list[2]
    if (l_m<l_c and l_m!=0) or (r_m<r_c and r_m!=0):
        return make_Qnode(input_node,succ_list)


    if state_list[2]==1:
        for i in range(2):
            if l_m-(i+1)>=0:
                succ_list.append([l_m-(i+1),l_c,0])
        for i in range(2):
            if l_c - (i + 1)>=0:
                succ_list.append([l_m, l_c - (i + 1), 0])
        if l_m-1 >=0 and l_c-1 >=0:
            succ_list.append([l_m-1, l_c -  1, 0])

    elif state_list[2]==0:
        for i in range(2):
            if r_m - (i + 1) >= 0:
                succ_list.append([l_m + (i + 1), l_c, 1])
        for i in range(2):
            if r_c - (i + 1) >= 0:
                succ_list.append([l_m, l_c + (i + 1), 1])
        if r_m - 1 >= 0 and r_c - 1 >=0:
            succ_list.append([l_m + 1, l_c + 1, 1])

    return make_Qnode(input_node,succ_list)




def make_Qnode(parent_node,suc_list):
    Q=[]
    for i in suc_list:
        suc_node=Node(i,parent_node,parent_node.cost+1,parent_node.depth+1)
        if suc_node.state in explored:
            print("jump")
            continue
        else:
            Q.append(suc_node)
    return Q

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


#
prob=Problem([3,3,1],[0,0,0])
# succ=derive_succ([0,2,1])
# print(succ)


def BFS(prob):
    print("BFS search start")
    initial_node = Node(prob.init,None,0,0)

    print(initial_node.state)
    frontiers=derive_succ(initial_node)
    explored.append(initial_node.state)
    j = 0
    while(len(frontiers)!=0):

        f0=frontiers.pop(0)
        if f0.state==[0,0,0]:
            print("Congratulations! it's a goal : {}".format(f0.state))
            sol.append(f0)

        explored.append(f0.state)
        frontiers=frontiers+derive_succ(f0)

        print("explored:")
        for i in explored:
            print(i)
        print("frontiers:")
        for i in frontiers:
            print(i)

        print("--------------------------------")
        j=j+1
        # if j==40:
        #     print("Done")
        #     exit(1)
    print("solution list")
    for i in sol:
        print(i)
    print("--------------------------------")

    sol_path(sol)

def sol_path(sol_list):
    for sol in sol_list:
        while(sol.parent!=None):
            print(sol)
            sol=sol.parent
        print(sol)

        print("done")




BFS(prob)





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
