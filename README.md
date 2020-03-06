## **ENPM661: Planning for Autonomous Robots**

## **Project 2: Implementation of Dijkstra algorithm for a Point and Rigid Robot**

## **Team Members:**

  * Shubham Sonawane (UID:  )
  * Revati Naik (UID: 116723015)

## **Problem Statement:**
Find the most optimal path from initial node to goal node using Dijkstra's Algorithm.



This project is divided into three sub-questions:

1. Checking the fesability of the given start node and goal node (if they lie in the obstacle space)

2. Implementing Dijkstra's Algorithm to find path between start node and goal node on a given map for point robot and rigid roobt

3. Output an animation of optimal path from start node to goal node on the graph. 

## **Approach:**

The input points (start node and goal node) are forst checked if they lie in the obstacle space. 

If not, then the program proceeds to find the optimal path from start node to goal node using Dijkstra's algorithm. 

This is implemented for both the point robot (no dimension) and the rigid robot (dimension and clearance to be considered). 

The program then backtracks the optimal path and outputs it in the form of animnation using `pygame` package. 

## **Dependencies:**

1. shapely : Install shapely pacakge from python3 using the following command on the terminal  `pip install shapely`

2. pygame : Install pygame pacakge from python3 using the following command on the terminal  `pip install pygame`


3. numpy : Install numpy pacakge from python3 using the following command on the terminal  `pip install numpy`




## **Running the code:**

There are two .py files

1. pointrobot.py
2. rigidrobot.py

Run the code on the commandline using the follwoing command `python3 pointrobot.py` and `rigidrobot.py`

The user will be prompted to give the coordinates of the start node and the goal node. 

`Enter x coordinate of start position: x_start`

`Enter y coordinate of start position: y_start`

`Enter x coordinate of goal position: x_goal`

`Enter y coordinate of goal position: y_goal`


