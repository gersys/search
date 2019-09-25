graph = {
'Arad': [('Zerind',75), ('Timisoara', 118), ('Sibiu', 140) ],
'Sibiu': [('Fagaras', 99), ('RV', 80), ('Oradea',151), ('Arad', 140)],
'RV':[('Sibiu',80), ('Pitesti',97), ('Craiova', 146)]
}

class Node:
    def __init__(self,s, p, c, d):
        self.state = s
        self.parent = p
        self.cost = c
        self.depth = d
        #self.action = a

    def __str__(self):
        return 'S: ' + self.state + ', depth = ' + str(self.depth) + ', cost = ' + str(self.cost)

    
    def solution(self):
        sol = self.state
        if self.depth == 0 :
            return sol
        else:
            return sol + '<==' + self.parent.solution()


class Stack:
    def __init__(self, node):
        self.items = [node]

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

class Queue:
    def __init__(self, node):
        self.items = [node]

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

class Problem:
    def __init__(self, a, b, m):
        self.init = a
        self.goal = b
        self.model = m
    
    def goal_test(self, state):    
        if self.goal == state:
            return True
        else:
            return False
    
    def sucFN(self, state):
        children = self.model.get(state, False)
        return children
  
    def __str__(self):
        return 'problem: goal: ' + self.goal
      

prob = Problem('Arad', 'Craiova', graph)
print(prob)
