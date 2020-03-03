import math
import cv2 as cv
from shapely.geometry import Point
from shapely.geometry.polygon import Polygon

xmax = 300
ymax = 200

start_x = int(input("Enter x coordinate of start position: "))
start_y = int(input("Enter y coordinate of start position: "))
goal_x = int(input("Enter x coordinate of goal position: "))
goal_y = int(input("Enter y coordinate of goal position: "))

radius = int(input("Enter radius of the robot: "))
clearance = int(input("Enter clearance of the robot: "))


def obstacle(x,y):
    flag = 0
    
    point = Point(x,y)
    #define polygons by their vertices
#    rectangle = Polygon([(35-radius-clearance, 76+radius+clearance), (100+radius+clearance, 39+radius+clearance), 
#                         (95+radius+clearance, 30-radius-clearance), (30-radius-clearance, 68-radius-clearance)])
#    complex_polygon = Polygon([(25, 185), (75, 185), (100, 150), (75, 120), (50, 150), (20, 120)])
#    kite = Polygon([(225, 40+radius+clearance), (250+radius+clearance, 25), (225, 10-radius-clearance), (200-radius-clearance, 25)])
    #print(point.distance(complex_polygon))
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
    
def draw_obstacle(x,y):
    flag = 0
    
    point = Point(x,y)
    #define polygons by their vertices
#    rectangle = Polygon([(35-radius-clearance, 76+radius+clearance), (100+radius+clearance, 39+radius+clearance), 
#                         (95+radius+clearance, 30-radius-clearance), (30-radius-clearance, 68-radius-clearance)])
#    complex_polygon = Polygon([(25, 185), (75, 185), (100, 150), (75, 120), (50, 150), (20, 120)])
#    kite = Polygon([(225, 40+radius+clearance), (250+radius+clearance, 25), (225, 10-radius-clearance), (200-radius-clearance, 25)])
    #print(point.distance(complex_polygon))
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
    if obstacle(x,y) or x  not in range(0,xmax+1) or (y not in range(0,ymax+1)):
        print("Start point inside obstacle space or not in workspace space or not a good entry for resolution")
        exit()
    else:
        pass

#start(init)

def CheckGoal(x,y):
    if obstacle(x,y) or x not in range(0,xmax+1) or y not in range(0,ymax+1):
        print("Goal point inside obstacle space or not in workspace space or not a good entry for resolution")
        exit()
    else:
        pass
#end(init)
CheckStart(start_x,start_y)
CheckGoal(goal_x, goal_y)


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
#    x=current[0]
#    y=current[1]+1
    x,y = current[0], current[1] + 1
    cost=1+cumulative_cost
    current,cost=IsMoveWorthy(x,y,cost,prev_node,current)
    print(cumulative_cost)
    
def MoveRight(prev_node):
    current=prev_node[:]
    x,y=current[0]+1, current[1]
    cost=1+cumulative_cost
    current,cost=IsMoveWorthy(x,y,cost,prev_node,current)
    print(cumulative_cost)
#    return current

def MoveDown(prev_node):
    current=prev_node[:]
#    x=current[0]
#    y=current[1]-1
    x,y = current[0], current[1] - 1
    cost=1+cumulative_cost
    current,cost=IsMoveWorthy(x,y,cost,prev_node,current)
    print(cumulative_cost)

def MoveLeft(prev_node):
    current=prev_node[:]
#    x=current[0]-1
#    y=current[1]
    x,y = current[0]-1, current[1]
    cost=1+cumulative_cost    
    current,cost=IsMoveWorthy(x,y,cost,prev_node,current)
    print(cost)
#    return current

def MoveUpRight(prev_node):
    current=prev_node[:]
#    x=current[0]+1
#    y=current[1]+1
    x,y = current[0] + 1, current[1] + 1
    cost=math.sqrt(2)+cumulative_cost
    current,cost=IsMoveWorthy(x,y,cost,prev_node,current)
    print(cumulative_cost)

def MoveDownRight(prev_node):
    current=prev_node[:]
#    x=current[0]+1
#    y=current[1]-1
    x,y = current[0] + 1, current[1] - 1
    cost=math.sqrt(2)+cumulative_cost
    current,cost=IsMoveWorthy(x,y,cost,prev_node,current)
    print(cumulative_cost)
    
def MoveDownLeft(prev_node):
    current=prev_node[:]
#    x=current[0]-1
#    y=current[1]-1
    x,y = current[0]-1, current[1]-1
    cost=math.sqrt(2)+cumulative_cost
    current,cost=IsMoveWorthy(x,y,cost,prev_node,current)
    print(cumulative_cost)

def MoveUpLeft(prev_node):
    current=prev_node[:]
#    x=current[0]-1
#    y=current[1]+1
    x,y = current[0]-1, current[1]+1
    cost=math.sqrt(2)+cumulative_cost
    current,cost=IsMoveWorthy(x,y,cost,prev_node,current)
    print(cumulative_cost)
#    return current

def iteration(node):
    MoveUp(node)
    MoveRight(node)
    MoveDown(node)
    MoveLeft(node)
    MoveUpRight(node)
    MoveDownRight(node)
    MoveDownLeft(node)
    MoveUpLeft(node)

def IsMoveWorthy(x,y,cost,prev_node,current):
    c=obstacle(x,y)
    if x in range(0,xmax+1) and y in range(0,ymax+1)and c==0:
        current[0]=x
        current[1]=y
        #cost=cost
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
    return current,cost

while goal not in visited_nodes:
        iteration(allnodes[new_index])
        visited_nodes.append(allnodes[new_index])
        temp.append(parent[new_index])
        allnodes.pop(new_index)
        cost_list.pop(new_index)
        parent.pop(new_index)
        
        if len(cost_list) != 0:#cost_list != []:
            cumulative_cost=min(cost_list)
            new_index=cost_list.index(min(cost_list))
            

while goal != [start_x, start_y]:#True:
    if goal in visited_nodes:
        goal_index=visited_nodes.index(goal)
        goal=temp[goal_index]
        solution.append(goal)
