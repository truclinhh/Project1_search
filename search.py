# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import re
from turtle import st
import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """
    "*** YOUR CODE HERE ***"
    from util import Stack

    # because dfs visits the deepest nodes, I use a stack of states to manage 
    # which state will be visited next after current state. 
    state_to_visit = Stack()
    # I use a list to store all the states that are visited.
    visited_state = []
    # I use a stack to store the actions from start state to current state.
    actions_to_current = Stack()
    # I use a list to store the action path from start state to goal state.
    # The actions from start to goal is the list of directions that pacman had visited util reach goal orderly.
    actions = []

    state = problem.getStartState()

    while not problem.isGoalState(state):
        if state not in visited_state:
            visited_state.append(state)
            for next_state, action, cost in problem.getSuccessors(state):
                temp_action = actions + [action]
                actions_to_current.push(temp_action)
                state_to_visit.push(next_state)
        state = state_to_visit.pop()
        actions = actions_to_current.pop()

    return actions
    util.raiseNotDefined()

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    
    from util import Queue
    # because bfs visits the nearest nodes, I use a queue of states to manage 
    # which state will be visited next after current state. 
    state_to_visit = Queue()
    # I use a list to store all the states that are visited.
    visited_state = []
    # I use a list to store the actions from start state to goal state.
    # The actions from start to goal is the list of directions that pacman had visited util reach goal orderly.
    actions = []
    # I use a queue to store the actions from start state to current state.
    actions_to_current = Queue()
    state = problem.getStartState()

    while not problem.isGoalState(state):
        if state not in visited_state:
            visited_state.append(state)
            for next_state, action, cost in problem.getSuccessors(state):
                temp_action = actions + [action]
                actions_to_current.push(temp_action)
                state_to_visit.push(next_state)
        state = state_to_visit.pop()
        actions = actions_to_current.pop()

    return actions

    util.raiseNotDefined()

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"

    from util import PriorityQueue
    # because ucs visits the nodes which has least cost first, I use a priority queue of states to manage 
    # which state will be visited next after current state, the priority attribute is cost of action. 
    state_to_visit = PriorityQueue()
    # I use a list to store all the states that are visited.
    visited_state = []
    # I use a list to store the actions from start state to goal state.
    # The actions from start to goal is the list of nodes that pacman had visited till reach goal orderly.
    actions = []
    # I use a stack to store the actions from start state to current state.
    actions_to_current = PriorityQueue()
    state = problem.getStartState()
    while not problem.isGoalState(state):
        if state not in visited_state:
            visited_state.append(state)
            for next_state, action, cost in problem.getSuccessors(state):
                temp_action = actions + [action]
                cost_of_state = problem.getCostOfActions(temp_action)
                actions_to_current.push(temp_action, cost_of_state)
                state_to_visit.push(next_state, cost_of_state)
        state = state_to_visit.pop()
        actions = actions_to_current.pop()

    return actions
    util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    from util import PriorityQueue
    # because a* visits the node which has least cost + heuristic first, I use a priority queue 
    # of states to manage which state will be visited next after current state 
    # the priority attribute is sum of cost of action and heuristic function. 
    state_to_visit = PriorityQueue()
    # I use a list to store all the states that are visited.
    visited_state = []
    # I use a list to store the actions from start state to goal state.
    # The actions from start to goal is the list of nodes that pacman had visited till reach goal orderly.
    actions = []
    # I use a stack to store the actions from start state to current state.
    actions_to_current = PriorityQueue()
    state = problem.getStartState()

    while not problem.isGoalState(state):
        if state not in visited_state:
            visited_state.append(state)
            for next_state, action, cost in problem.getSuccessors(state):
                temp_action = actions + [action]
                cost_of_state = problem.getCostOfActions(temp_action)
                actions_to_current.push(temp_action, cost_of_state + heuristic(next_state, problem))
                state_to_visit.push(next_state, cost_of_state + heuristic(next_state, problem))
        state = state_to_visit.pop()
        actions = actions_to_current.pop()

    return actions
    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
