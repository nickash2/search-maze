#!/usr/bin/env python3
from fringe import Fringe, GreedyFringe, AStarFringe, UCSFringe
from state import State


def solve_maze(maze, fr):
    # get the start room, create state with start room and None as parent and put it in fringe
    room = maze.get_room(*maze.get_start())
    state = State(room, None)

    fr.push(state)
    visited = set()    # set consisting of only the visited rooms

    while not fr.is_empty():

        # get item from fringe and get the room from that state
        state = fr.pop()
        room = state.get_room()

        if room.is_goal():
            # if room is the goal, print that with the statistics and the path and return
            print("solved")
            fr.print_stats()
            state.print_path()
            state.print_actions()
            print()  # print newline
            maze.print_maze_with_path(state)
            return True

        if room not in visited:
            # if room was not visited before, add it to the set
            visited.add(room)
            for d in room.get_connections():    # for move in [N,S,E,W]
                # loop through every possible move
                # Get new room after move and cost to get there
                new_room, cost = room.make_move(d, state.get_cost())
                if new_room not in visited:
                    # create the new state and push to the stack if the new room has not been visited before
                    # Create new state with new room and old room
                    new_state = State(new_room, state, cost)
                    # push the new state
                    fr.push(new_state)

    # fringe is empty and goal is not found, so maze is not solved
    print("not solved")
    fr.print_stats()        # print the statistics of the fringe
    return False


def solveIDS(maze, fr):
    room = maze.get_room(*maze.get_start())
    state = State(room, None, depth=0)
    fr.push(state)
    visited = set()
    depth_limit = 0
    
    while True:
        if not fr.is_empty():
            if(DFS(state, visited, fr, depth_limit, maze)):
            # goal found
                return True
            depth_limit += 1
    
    
def DFS(state, visited, fr, depth_limit, maze):
    
    # get item from fringe and get the room from that state
    state = fr.pop()
    room = state.get_room()

    if room.is_goal(): 
        print("solved")
        fr.print_stats()
        state.print_path()
        state.print_actions()
        print()
        maze.print_maze_with_path(state)
        return True
    
    if state.get_depth() > depth_limit:
        print("depth limit reached")
        return False

    if room not in visited:
        # if room was not visited before, add it to the set
        visited.add(room)
        for d in room.get_connections():    # for move in [N,S,E,W]
            # loop through every possible move
            # Get new room after move and cost to get there
            new_room, cost = room.make_move(d, state.get_cost())
            if new_room not in visited:
                # create the new state and push to the stack if the new room has not been visited before
                # Create new state with new room and old room
                new_state = State(new_room, state, cost, depth = state.get_depth() + 1)
                # push the new state
                fr.push(new_state)

    # goal is not found, so maze is not solved
    return False
    
    
def solve_maze_general(maze, algorithm):
    """
    Finds a path in a given maze with the given algorithm
    :param maze: The maze to solve
    :param algorithm: The desired algorithm to use
    :return: True if solution is found, False otherwise
    """
    # select the right fringe for each algorithm
    if algorithm == "BFS":
        fr = Fringe("FIFO")
    elif algorithm == "DFS":
        fr = Fringe("STACK")
    elif algorithm == "UCS":
        fr = UCSFringe("PRIORITY")
    elif algorithm == "ASTAR":
        fr = AStarFringe("PRIORITY")
    elif algorithm == "GREEDY":
        fr = GreedyFringe("PRIORITY")
    elif algorithm == "IDS":
        fr = Fringe("STACK")
        if (solveIDS(maze, fr)):
            return True
        return False
    else:
        print("Algorithm not found/implemented, exit")
        return
    
    if (solve_maze(maze,fr)):
        return True
    return False






