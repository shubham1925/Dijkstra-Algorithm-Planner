import math
import cv2 as cv
from shapely.geometry import Point
from shapely.geometry.polygon import Polygon
import sys

xmax = 300
ymax = 200

start_x = int(input("Enter x coordinate of start position: "))
start_y = int(input("Enter y coordinate of start position: "))
goal_x = int(input("Enter x coordinate of goal position: "))
goal_y = int(input("Enter y coordinate of goal position: "))

#radius and clearance 0 for point robot
radius = int(input("Enter radius of the robot: "))
clearance = int(input("Enter clearance of the robot: "))


def obstacle(x,y):
    flag = 0    
    point = Point(x,y)
    rectangle = Polygon([(35, 76), (100, 39),(95, 30), (30, 68)])
    complex_polygon = Polygon([(25, 185), (75, 185),(100, 150), (75, 120), (50,150), (20,120)])
    kite = Polygon([(225, 40), (250, 25),(225, 10), (200, 25)])
    #circle
    if(((x - (225))**2 + (y - (150))**2 - (25+radius+clearance)**2) <= 0) :
        print("obs - circ")
        flag = 1
    #ellipse
    if (((x - (150))/(40+radius+clearance))**2 + ((y - (100))/(20+radius+clearance))**2 - 1) <= 0:
        print("obs-ellip")
        flag = 1
    #check if point is inside polygon
    if rectangle.contains(point) == True or point.distance(rectangle) <= radius+clearance:
        print("obs - rect")
        flag = 1
    if complex_polygon.contains(point) == True or point.distance(complex_polygon) <= radius+clearance:
        print("obs - poly")
        flag = 1
    if kite.contains(point) == True or point.distance(kite) <= radius+clearance:
        print("obs - kite")
        flag = 1
    return flag

#check = obstacle(20,100)
#init = [50,170]


def obstacle_space_rectangel(point):
    # four points in a square
    flag_check = 0
    pt1 = [35,76]
    pt2 = [100,39]
    pt3 = [95,30]
    pt4 = [30,68]

    x = point[0]
    y = point[1]

    line_1 = ((y-76)*65) + ((x-35)*37)
    line_2 = ((y-39)*5) - ((x-100)*9)
    line_3 = ((y-30)*65) + ((x-95)*38)
    line_4 = ((y-68)*5) - ((x-30)*8)
    
    
    if line_1 < 0 and line_2 > 0 and line_3 > 0 and line_4 < 0:
        return True
    else:
        return False

def obstacle_space_kite(point):
    # four points in a square
    x = point[0]
    y = point[1]

    line_1 = ((y-25)*25) + ((x-200)*15)
    line_2 = ((y-10)*25) - ((x-225)*15)
    line_3 = ((y-25)*25) + ((x-250)*15)
    line_4 = ((y-40)*25) - ((x-225)*15)
    
    print("line1",line_1)
    print("line2",line_2)
    print("line3",line_3)
    print("line4",line_4)
    
    if line_1 > 0 and line_2 > 0 and line_3 < 0 and line_4 < 0:
        return True
    else:
        return False

def obstacle_space_circle(point):
    radius = 25
    radius_x = 225
    radius_y = 150

    x = point[0]
    y = point[1]

    d = sqrt(((x-radius_x)**2) + ((y-radius_y)**2))

    if d < radius:
        return True
    else:
        return False

def obstacle_space_ellipse(point):
    semi_major_axis = 40
    center_x = 150
    center_y = 100

    x = point[0]
    y = point[1]

    d = ((x-center_x)**2)/(semi_major_axis**2) + ((y-center_y)**2)/(semi_major_axis**2)

    if d <= 1:
        return True
    else:
        return False

def obstacle_space_polygon(point):
    pt1 = [25,185]
    pt1 = [20,120]
    pt1 = [50,150]
    pt1 = [75,120]
    pt1 = [100,150]
    pt1 = [175,185]

    x = point[0]
    y = point[1]
    flag_1 = 0
    flag_2 = 0
    
    quad_1_1 = ((y-150)*25) + ((x-50)*30)
    quad_1_2 = ((y-120)*25) - ((x-75)*30)
    quad_1_3 = ((y-150)*25) - ((x-100)*35)
    quad_1_4 = ((y-150)*25) - ((x-50)*35)
    
    quad_2_1 = ((y-185)*5) - ((x-25)*65)
    quad_2_2 = ((y-120)*30) - ((x-20)*30)
    quad_2_3 = ((y-150)*25) - ((x-50)*35)
    quad_2_4 = ((y-185)*(-50))
    
    if quad_1_1 > 0 and quad_1_2 > 0 and quad_1_3 > 0 and quad_1_4 <= 0:
        flag_1 = 1
    else:
        flag_1 = 0

    if quad_2_1 < 0 and quad_2_2 > 0 and quad_2_3 >= 0 and quad_2_4 > 0:
        flag_2 = 1
    else:
        flag_2 = 0

    if flag_1 == 1 or flag_2 == 1:
        return True
    else:
        return False

def draw_obstacle(x,y):
    flag = 0    
    point = Point(x,y)
    rectangle = Polygon([(35, 76), (100, 39),(95, 30), (30, 68)])
    complex_polygon = Polygon([(25, 185), (75, 185),(100, 150), (75, 120), (50,150), (20,120)])
    kite = Polygon([(225, 40), (250, 25),(225, 10), (200, 25)])
    #circle
    if(((x - (225))**2 + (y - (150))**2 - (25)**2) <= 0) :
        print("obs - circ")
        flag = 1
    #ellipse
    if (((x - (150))/(40))**2 + ((y - (100))/(20))**2 - 1) <= 0:
        print("obs-ellip")
        flag = 1
    #check if point is inside polygon
    if rectangle.contains(point) == True:
        print("obs - rect")
        flag = 1
    if complex_polygon.contains(point) == True:
        print("obs - poly")
        flag = 1
    if kite.contains(point) == True:
        print("obs - kite")
        flag = 1
    return flag

def generate_obstacle_map():
    obstacle_list = []
    for x in range(0,xmax+1):
        for y in range(0,ymax+1):
            if draw_obstacle(x,y):
                obstacle_list.append([x,y])
    return obstacle_list

def CheckStart(x,y):
    if obstacle(x,y) or x not in range(0,xmax+1) or y not in range(0,ymax+1):
        print("Start position invalid")
        return False
    else:
        return True


def CheckGoal(x,y):
    if obstacle(x,y) or x not in range(0,xmax+1) or y not in range(0,ymax+1):
        print("Goal position invalid")
        return False
    else:
        return True


if CheckStart(start_x,start_y) == False or CheckGoal(goal_x, goal_y) == False:
    sys.exit()
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

def MoveUp(prev_node):
    
    current=prev_node[:]
    x,y = current[0], current[1] + 1
    cost=1+cumulative_cost
    IsMoveWorthy(x,y,cost,prev_node)
    print(cumulative_cost)
    
def MoveRight(prev_node):
    current=prev_node[:]
    x,y=current[0]+1, current[1]
    cost=1+cumulative_cost
    IsMoveWorthy(x,y,cost,prev_node)
    print(cumulative_cost)


def MoveDown(prev_node):
    current=prev_node[:]
    x,y = current[0], current[1] - 1
    cost=1+cumulative_cost
    IsMoveWorthy(x,y,cost,prev_node)
    print(cumulative_cost)

def MoveLeft(prev_node):
    current=prev_node[:]
    x,y = current[0]-1, current[1]
    cost=1+cumulative_cost    
    IsMoveWorthy(x,y,cost,prev_node)
    print(cost)


def MoveUpRight(prev_node):
    current=prev_node[:]
    x,y = current[0] + 1, current[1] + 1
    cost=math.sqrt(2)+cumulative_cost
    IsMoveWorthy(x,y,cost,prev_node)
    print(cumulative_cost)

def MoveDownRight(prev_node):
    current=prev_node[:]
    x,y = current[0] + 1, current[1] - 1
    cost=math.sqrt(2)+cumulative_cost
    IsMoveWorthy(x,y,cost,prev_node)
    print(cumulative_cost)
    
def MoveDownLeft(prev_node):
    current=prev_node[:]
    x,y = current[0]-1, current[1]-1
    cost=math.sqrt(2)+cumulative_cost
    IsMoveWorthy(x,y,cost,prev_node)
    print(cumulative_cost)

def MoveUpLeft(prev_node):
    current=prev_node[:]
    x,y = current[0]-1, current[1]+1
    cost=math.sqrt(2)+cumulative_cost
    IsMoveWorthy(x,y,cost,prev_node)
    print(cumulative_cost)

def iteration(node):
    MoveUp(node)
    MoveRight(node)
    MoveDown(node)
    MoveLeft(node)
    MoveUpRight(node)
    MoveDownRight(node)
    MoveDownLeft(node)
    MoveUpLeft(node)

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
            else:
                allnodes.append(current)
                cost_list.append(cost)
                parent.append(prev_node)
        else:
            pass
    #return current,cost

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
            
#backtrack
while goal != [start_x, start_y]:
    if goal in visited_nodes:
        goal_index=visited_nodes.index(goal)
        goal=temp[goal_index]
        solution.append(goal)
