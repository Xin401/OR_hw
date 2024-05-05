from gurobipy import *

def solve():
    model = Model("Scheduling")
    x = model.addVars(2, vtype=GRB.CONTINUOUS, name='x')
    model.setObjective((x[0]-3)**2 + (x[1]-2)**2, GRB.MINIMIZE)
    model.addConstr(x[0] + 2*x[1] >= 10)
    model.optimize()
    print('Obj:', model.objVal)
    for i in range(2):
        print('x[', i, '] = ', x[i].x)
        


if __name__ == '__main__':
    solve()