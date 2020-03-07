import math
import sys
import pygame
from pygame.locals import QUIT, MOUSEBUTTONUP
import numpy as np
import time

xmax = 300
ymax = 200

start_x = int(input("Enter x coordinate of start position: "))
start_y = int(input("Enter y coordinate of start position: "))
goal_x = int(input("Enter x coordinate of goal position: "))
goal_y = int(input("Enter y coordinate of goal position: "))

"""Calculates the manhattan distance between two points

Args:
    x1,y1,x2,y2: coordinates of the 2 points
    
Returns:
    Manhattan distance
"""
def manhattan_heuristics(x1,y1,x2,y2):
    return abs(x1-x2) + abs(y1-y2)

"""Calculates the euclidean distance between two points

Args:
    x1,y1,x2,y2: coordinates of the 2 points
    
Returns:
    Euclidean distance
"""
def euclidean_heuristics(x1,y1,x2,y2):
    return math.sqrt((x1-x2)**2 + (y1-y2)**2)

"""Checks for obstacles at any particular point

Args:
    x,y: coordinates of the point to be checked
    
Returns:
    Flag indicating presence or absence of obstacles
"""
def obstacle(x,y):
    flag = 0
    flag_1 = 0
    flag_2 = 0
    
    #kite
    kite_line_1 = ((y-25)*25) + ((x-200)*15)
    kite_line_2 = ((y-10)*25) - ((x-225)*15)
    kite_line_3 = ((y-25)*25) + ((x-250)*15)
    kite_line_4 = ((y-40)*25) - ((x-225)*15)
    
    #rectangle
    rect_line_1 = ((y-76)*65) + ((x-35)*37)
    rect_line_2 = ((y-39)*5) - ((x-100)*9)
    rect_line_3 = ((y-30)*65) + ((x-95)*38)
    rect_line_4 = ((y-68)*5) - ((x-30)*8)
    
    #complex polygon
    quad_1_1 = 5*y+6*x-1050
    quad_1_2 = 5*y-6*x-150
    quad_1_3 = 5*y+7*x-1450
    quad_1_4 = 5*y-7*x-400
    
    quad_2_1 = ((y-185)*5) - ((x-25)*65)
    quad_2_2 = ((y-120)*30) - ((x-20)*30)
    quad_2_3 = ((y-150)*25) - ((x-50)*35)
    quad_2_4 = ((y-185)*(-50))   
    
    #check kite
    if kite_line_1 > 0 and kite_line_2 > 0 and kite_line_3 < 0 and kite_line_4 < 0:
        flag = 1
    
    #check rectangle
    if rect_line_1 < 0 and rect_line_2 > 0 and rect_line_3 > 0 and rect_line_4 < 0:
        flag = 1
    
    #check polygon
    if quad_1_1>0 and quad_1_2>0 and quad_1_3<0 and quad_1_4<0:
        flag_1 = 1
    else:
        flag_1 = 0

    if quad_2_1 < 0 and quad_2_2 > 0 and quad_2_3 > 0 and quad_2_4 > 0:
        flag_2 = 1
    else:
        flag_2 = 0

    if flag_1 == 1 or flag_2 == 1:
        flag = 1
        
    #circle
    if(((x - (225))**2 + (y - (150))**2 - (25)**2) <= 0) :
        flag = 1
        
    #ellipse
    if (((x - (150))/(40))**2 + ((y - (100))/(20))**2 - 1) <= 0:
        flag = 1    
    return flag  

"""Generate obstacle map

Args:
   None
    
Returns:
    List containing obstacles
"""
def generate_obstacle_map():
    obstacle_list = []
    for x in range(0,xmax+1):
        for y in range(0,ymax+1):
            if obstacle(x,y):
                obstacle_list.append([x,y])
    return obstacle_list

"""Check start position

Args:
   x,y:start point
    
Returns:
    False if invalid start point
"""
def CheckStart(x,y):
    if obstacle(x,y) or x not in range(0,xmax+1) or y not in range(0,ymax+1):
        print("Start position invalid")
        return False
    else:
        return True

"""Check goal position

Args:
   x,y:goal point
    
Returns:
    False if invalid goal point
"""
def CheckGoal(x,y):
    if obstacle(x,y) or x not in range(0,xmax+1) or y not in range(0,ymax+1):
        print("Goal position invalid")
        return False
    else:
        return True

if CheckStart(start_x,start_y) == False or CheckGoal(goal_x, goal_y) == False:
    print(sys.exit())
else:pass

start = [start_x,start_y]
goal=[goal_x,goal_y]

allnodes=[]
parent=[]
cost_list=[]
temp=[]
visited_nodes=[]
solution=[]

allnodes.append(start)
parent.append(start)
solution.append(goal)

cost=999999
cost_list.append(cost)
new_index=0
cumulative_cost=0

animation_flag = 0

tic = time.time()

"""Move robot

Args:
   prev_node:previous node
    
Returns:
    None
"""
def MoveUp(prev_node):    
    current=prev_node[:]
    x,y = current[0], current[1] + 1
    h = euclidean_heuristics(current[0], current[1], x, y)
#    h = manhattan_heuristics(current[0], current[1], x, y)
    cost=h+cumulative_cost
    IsMoveWorthy(x,y,cost,prev_node)
    
def MoveRight(prev_node):
    current=prev_node[:]
    x,y=current[0]+1, current[1]
    h = euclidean_heuristics(current[0], current[1], x, y)
#    h = manhattan_heuristics(current[0], current[1], x, y)
    cost=h+cumulative_cost
    IsMoveWorthy(x,y,cost,prev_node)

def MoveDown(prev_node):
    current=prev_node[:]
    x,y = current[0], current[1] - 1
    h = euclidean_heuristics(current[0], current[1], x, y)
#    h = manhattan_heuristics(current[0], current[1], x, y)
    cost=h+cumulative_cost
    IsMoveWorthy(x,y,cost,prev_node)

def MoveLeft(prev_node):
    current=prev_node[:]
    x,y = current[0]-1, current[1]
    h = euclidean_heuristics(current[0], current[1], x, y)
#    h = manhattan_heuristics(current[0], current[1], x, y)
    cost=h+cumulative_cost    
    IsMoveWorthy(x,y,cost,prev_node)

def MoveUpRight(prev_node):
    current=prev_node[:]
    x,y = current[0] + 1, current[1] + 1
    h = euclidean_heuristics(current[0], current[1], x, y)
#    h = manhattan_heuristics(current[0], current[1], x, y)
    cost=h+cumulative_cost
    IsMoveWorthy(x,y,cost,prev_node)

def MoveDownRight(prev_node):
    current=prev_node[:]
    x,y = current[0] + 1, current[1] - 1
    h = euclidean_heuristics(current[0], current[1], x, y)
#    h = manhattan_heuristics(current[0], current[1], x, y)
    cost=h+cumulative_cost
    IsMoveWorthy(x,y,cost,prev_node)
    
def MoveDownLeft(prev_node):
    current=prev_node[:]
    x,y = current[0]-1, current[1]-1
    h = euclidean_heuristics(current[0], current[1], x, y)
#    h = manhattan_heuristics(current[0], current[1], x, y)
    cost=h+cumulative_cost
    IsMoveWorthy(x,y,cost,prev_node)

def MoveUpLeft(prev_node):
    current=prev_node[:]
    x,y = current[0]-1, current[1]+1
    h = euclidean_heuristics(current[0], current[1], x, y)
#    h = manhattan_heuristics(current[0], current[1], x, y)
    cost=h+cumulative_cost
    IsMoveWorthy(x,y,cost,prev_node)

"""Move oover action space

Args:
   node:node from where the expansion is to be done
    
Returns:
    None
"""
def iteration(node):
    MoveUp(node)
    MoveRight(node)
    MoveDown(node)
    MoveLeft(node)
    MoveUpRight(node)
    MoveDownRight(node)
    MoveDownLeft(node)
    MoveUpLeft(node)
    
"""Check if the move is worthy i.e less cost

Args:
   x,y, cost, prev_node
    
Returns:
    None
"""
def IsMoveWorthy(x,y,cost,prev_node):
    flag = obstacle(x,y)
    current = []
    current.append(x)
    current.append(y)
    if x in range(0,xmax+1) and y in range(0,ymax+1) and flag == 0:
        if current not in visited_nodes:
            if current in allnodes:
                #extract node index
                check=allnodes.index(current)
                #extract cost corresponding to the node
                prev_cost=cost_list[check]
                if prev_cost <= cost:
                    pass
                else:
                    #remove previous node, and append new/currentnode
                    allnodes.pop(check)
                    cost_list.pop(check)
                    parent.pop(check)
                    allnodes.append(current)
                    cost_list.append(cost)
                    parent.append(prev_node)
#                    print(str(current)+str(cost))
            else:
                allnodes.append(current)
                cost_list.append(cost)
                parent.append(prev_node)
        else:
            pass
    #return current,cost
print("Solving...")

while goal not in visited_nodes:
    #iterate possible moves
    iteration(allnodes[new_index])
    #add to visited nodes
    visited_nodes.append(allnodes[new_index])
    temp.append(parent[new_index])
    #remove the low cost node after being appended
    cost_list.pop(new_index)
    allnodes.pop(new_index)    
    parent.pop(new_index)    
    if len(cost_list) != 0:
        cumulative_cost=min(cost_list)
        new_index=cost_list.index(min(cost_list))
            
while goal != [start_x, start_y]:
    if goal in visited_nodes:
        goal_index=visited_nodes.index(goal)
        goal=temp[goal_index]
        solution.append(goal)
        
toc = time.time()

print("Time to solve: "+str((toc-tic)/60))
print("Length of path to reach goal: "+str(len(solution)))
print("Number of nodes explored: "+str(len(visited_nodes)))

obstacle_map = generate_obstacle_map()


#animation
OBS_C = [219, 114, 15]
EXP_C = [36, 237, 130]
PATH_C = [230, 90, 104]
WHITE = [255, 255, 255]
START_C = [255, 0, 0]
GOAL_C = [0,0,255]
#preparing data for pygame
scale_factor = 3
obstacle_map = np.array(obstacle_map)
visited_nodes = np.array(visited_nodes)
solution = np.array(solution)
pygame.init()
size = (xmax*scale_factor, ymax*scale_factor)
win = pygame.display.set_mode((xmax*scale_factor, ymax*scale_factor))
win.fill(WHITE)
pygame.display.set_caption("Dijsktra algorithm - point robot")
while True:
    win.fill(WHITE)
    pygame.event.get()
    for event in pygame.event.get():
        if event.type == MOUSEBUTTONUP:
            None
    for obs in obstacle_map:
        pygame.draw.rect(win, OBS_C, [obs[0]*scale_factor, (ymax-obs[1])*scale_factor,3,3])
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == MOUSEBUTTONUP:
                None
        
    pygame.draw.rect(win, START_C, [start_x*scale_factor, (ymax-start_y)*scale_factor,3,3])
    pygame.draw.rect(win, GOAL_C, [goal_x*scale_factor, (ymax-goal_y)*scale_factor,3,3])
    pygame.display.flip()

    for vis in visited_nodes:
        pygame.draw.rect(win, EXP_C, [vis[0]*scale_factor, (ymax-vis[1])*scale_factor,3,3])
        pygame.time.wait(1)
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == MOUSEBUTTONUP:
                None
        
    for sol in solution:
        pygame.draw.rect(win, PATH_C, [sol[0]*scale_factor, (ymax-sol[1])*scale_factor,3,3])
        pygame.time.wait(1)
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == MOUSEBUTTONUP:
                None        
    animation_flag = 1
    while animation_flag == 1:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()