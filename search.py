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

def graphSearch(problem, container, Stack_or_Queue):
    """
    Search algorithm of graph. BFS and DFS are similar, 
    but BFS uses Queue to manage which state will be visited next
    while DFS uses Stack.
    
    container parameter is used to specify the container the algorithm uses: Queue or Stack.
    """
    from util import Stack, Queue

    current_state = problem.getStartState()

    visited_state = []
    action_to_goal = []
    
    if (Stack_or_Queue == 'stack'):
        action_to_current = Stack()
    else:
        action_to_current = Queue()

    while not problem.isGoalState(current_state):
        if current_state not in visited_state:
            visited_state.append(current_state)
            for next_state, action, cost in problem.getSuccessors(current_state):
                container.push(next_state)
                temp_action = action_to_goal + [action]
                action_to_current.push(temp_action)

        current_state = container.pop()
        action_to_goal = action_to_current.pop()
    
    return action_to_goal
    util.raiseNotDefined()

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
    
    stack_state = Stack()
    return graphSearch(problem, stack_state, 'stack')
        
    util.raiseNotDefined()

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    from util import Queue
    
    queue_state = Queue()
    return graphSearch(problem, queue_state, 'queue')

    util.raiseNotDefined()

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    from util import PriorityQueue
    priority_queue = PriorityQueue()
    priority_queue.push((problem.getStartState(), [], 0), 0)
    visited = []
    while not priority_queue.isEmpty():
        state, actions, cost = priority_queue.pop()
        if problem.isGoalState(state):
            return actions
        if state not in visited:
            visited.append(state)
            for next_state, action, next_cost in problem.getSuccessors(state):
                if next_state not in visited:
                    priority_queue.push((next_state, actions + [action], cost + next_cost), cost + next_cost)

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
    priority_queue = PriorityQueue()
    priority_queue.push((problem.getStartState(), [], 0), 0)
    visited = []
    while not priority_queue.isEmpty():
        state, actions, cost = priority_queue.pop()
        if problem.isGoalState(state):
            return actions
        if state not in visited:
            visited.append(state)
            for next_state, action, next_cost in problem.getSuccessors(state):
                if next_state not in visited:
                    priority_queue.push((next_state, actions + [action], cost + next_cost), 
                        cost + next_cost + heuristic(next_state, problem))

    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
