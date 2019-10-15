# [the number of missionaries, cannibals at left of river , and the location of boat (left 1, right 0)]


explored=[]
sol=[]


class AStar: #Astar 클래스 정의
    def __init__(self,prob):
        self.prob=prob
        self.numberGeneratedNodes=0 #생성된 노드 개수 저장

    def solution(self):
        frontiers = []
        print("A* search start")
        initial_node = A_star_Node(self.prob.init, None, 0, self.prob.init[0], 0) #처음 시작 노드 생성 ,휴리스틱 왼쪽에 있는 선교사 수 self.prob.init[0]

        frontiers = self.derive_succ(initial_node,frontiers) #시작 노드로 부터 탐색할 노드들 생성
        explored.append(initial_node.state) #시작 노드를 탐색한 곳으로 분류


        while (len(frontiers) != 0):  #탐색할 곳 중 f_cost가 가장 작은곳을 먼저 탐색
            f_cost = []
            for i in frontiers:
                f_cost.append(i.f_cost)
            argmin=-min((x, -i) for i, x in enumerate(f_cost))[1]

            f0 = frontiers.pop(argmin)

            if f0.state == [0, 0, 0]:
                print("Congratulations! it's a goal : {}".format(f0.state))
                sol.append(f0)
                return f0

            explored.append(f0.state)
            frontiers = frontiers + self.derive_succ(f0,frontiers)

            # for i in frontiers:
            #     frontier.append(i.state)

            # 잘생성되는지 확인하는 용도의 코드
            # print("explored:")
            # for i in explored:
            #     print(i)
            # print("frontiers:")
            # for i in frontiers:
            #     print(i)
            #
            # print("--------------------------------")

    def derive_succ(self,input_node,frontiers): #현재 상태에서 탐색할 노드들 생성하는 함수
        state_list = input_node.state
        succ_list = []
        l_m = state_list[0] # 왼쪽 선교사수
        l_c = state_list[1] # 왼쪽 식인종수
        r_m = 3 - state_list[0] # 오른쪽 선교사수
        r_c = 3 - state_list[1] # 오른쪽 식인종 수
        boat = state_list[2]
        if (l_m < l_c and l_m != 0) or (r_m < r_c and r_m != 0): #Game over 조건으로 추가로 탐색할 구간을 생성하지 않는다.
            return self.make_Qnode(input_node, succ_list,frontiers)  #리스트로 생성 후 node로 변경한다.

        if state_list[2] == 1: # 배가 왼쪽에 있는 경우에 탐색할 노드 생성
            for i in range(2):
                if l_m - (i + 1) >= 0:
                    succ_list.append([l_m - (i + 1), l_c, 0])
                    self.numberGeneratedNodes = self.numberGeneratedNodes + 1
            for i in range(2):
                if l_c - (i + 1) >= 0:
                    succ_list.append([l_m, l_c - (i + 1), 0])
                    self.numberGeneratedNodes = self.numberGeneratedNodes + 1
            if l_m - 1 >= 0 and l_c - 1 >= 0:
                succ_list.append([l_m - 1, l_c - 1, 0])
                self.numberGeneratedNodes = self.numberGeneratedNodes + 1

        elif state_list[2] == 0: # 배가 오른쪽에 있는 경우에 탐색할 노드 생성
            for i in range(2):
                if r_m - (i + 1) >= 0:
                    succ_list.append([l_m + (i + 1), l_c, 1])
                    self.numberGeneratedNodes = self.numberGeneratedNodes + 1
            for i in range(2):
                if r_c - (i + 1) >= 0:
                    succ_list.append([l_m, l_c + (i + 1), 1])
                    self.numberGeneratedNodes = self.numberGeneratedNodes + 1
            if r_m - 1 >= 0 and r_c - 1 >= 0:
                succ_list.append([l_m + 1, l_c + 1, 1])
                self.numberGeneratedNodes = self.numberGeneratedNodes + 1

        return self.make_Qnode(input_node, succ_list,frontiers) #생성된 리스트를 노드로 변경하여 리턴한다.

    def make_Qnode(self, parent_node, suc_list,frontiers): #리스트로 되어있는 상태를 노드로 변경하는 함수
        Q = []
        for i in suc_list:
            suc_node = A_star_Node(i, parent_node, parent_node.g_cost + 1,i[0], parent_node.depth + 1) #휴리스틱 왼쪽에 있는 선교사 수 i[0]
            frontier=[]
            for i in frontiers:
                frontier.append(i.state)
            if suc_node.state in explored: #탐색한 곳 탐색제외
                continue
            elif suc_node.state in frontier: #탐색할 곳에 이미 그 state가 있는 경우 f score를 비교하여 작은걸로 변경해줌
                for i in frontiers:
                    if i.state==suc_node.state:
                        if i.f_cost> suc_node.f_cost:
                            frontiers.pop(i)
                            frontiers.append(suc_node)
                continue
            else:
                Q.append(suc_node)
        return Q

class Problem:
    def __init__(self, a, b):
        self.init = a
        self.goal = b

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

    def __str__(self):
        try:
            return 'S: ' + str(self.state) +', P: ' + str(self.parent.state) + ', depth = ' + str(self.depth) + ', f_cost : ' +str(self.f_cost) +'='+ str(self.g_cost)+'+'+str(self.h_cost)
        except AttributeError:
            return 'S: ' + str(self.state) + ', P: ' + "None" + ', depth = ' + str(self.depth) + ', f_cost : ' +str(self.f_cost) +'='+ str(self.g_cost)+'+'+str(self.h_cost)


    def solution(self):
        p_node = self
        while (p_node != None):
            print(str(p_node.state) + " ("+str(p_node.f_cost)+"="+str(p_node.g_cost)+"+"+str(p_node.h_cost)+")")
            p_node=p_node.parent

        return "solution path return done"

#----------------------------------------------------------------------------------------------------------------------------------------------


prob=Problem([3,3,1],[0,0,0])
astar=AStar(prob)
goalNode=astar.solution()
print("Node generated:{}".format(astar.numberGeneratedNodes))
print(goalNode.solution())






