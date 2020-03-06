## **ENPM661: Planning for Autonomous Robots**

## **Project 2: Implementation of Dijkstra algorithm for a Point and Rigid Robot**

## **Team Members:**

  * Shubham Sonawane (UID: 116808996 )
  * Revati Naik (UID: 116723015)

## **Problem Statement:**
Find the optimal path from initial node to goal node using Dijkstra's Algorithm.



This project is divided into three sub-questions:

1. Checking the feasibility of the given start node and goal node (if they lie in the obstacle space)

2. Implementing Dijkstra's Algorithm to find path between start node and goal node on a given map for point robot and rigid robot

3. Output an animation of optimal path from start node to goal node on the graph. 

## **Approach:**

The input points (start node and goal node) are first checked if they lie in the obstacle space. 

If not, then the program proceeds to find the optimal path from start node to goal node using Dijkstra's algorithm. 

This is implemented for both the point robot (no dimension) and the rigid robot (dimension and clearance to be considered). 

The program then backtracks the optimal path and outputs it in the form of animnation using `pygame` package. 

## **Dependencies:**

1. shapely : Install shapely pacakge from python3 using the following command on the terminal  `pip install shapely`

2. pygame : Install pygame pacakge from python3 using the following command on the terminal  `pip install pygame`

3. numpy : Install numpy pacakge from python3 using the following command on the terminal  `pip install numpy`

4. math: Install math package from python3 using the following command on the terminal `pip install math`

5. sys

6. time

## **Running the code:**

The code contains two .py files

1. Dijkstra_point.py

2. Dijkstra_rigid.py


**For Point Robot**: 

Run the code on the command line using the following command `python3 Dijkstra_point.py`


The user will be prompted for:

1. Coordinates of the start node and the goal node 


`Enter x coordinate of start position: x_start`

`Enter y coordinate of start position: y_start`

`Enter x coordinate of goal position: x_goal`

`Enter y coordinate of goal position: y_goal`



**For Rigid Robot**

Run the code on the command line using the following command `python3 Dijkstra_rigid.py`

The user will be prompted for:

1. Coordinates of the start node and the goal node 

2. Radius of the robot

3. Clearance of the robot

`Enter x coordinate of start position: x_start`

`Enter y coordinate of start position: y_start`

`Enter x coordinate of goal position: x_goal`

`Enter y coordinate of goal position: y_goal`

`Enter radius of the robot: `

`Enter clearance of the robot:`

## **Running the test case:**

`Enter x coordinate of start position: 5`

`Enter y coordinate of start position: 5`

`Enter x coordinate of goal position: 295`

`Enter y coordinate of goal position: 195`


The time taken by the point robot to go from (5,5) to (295,195) is approximately 7 minutes 40 seconds
Tested on IDE: Spyder Python version 3.7.4
