import random
import math
import time

def generateInitialSolution(n):
    # Generates a random initial solution: each task is assigned to one and only one agent
    solution = list(range(n))
    random.shuffle(solution)
    return solution

def calculateCost(solution, c):
    cost = 0
    for task, agent in enumerate(solution):
        cost += c[task][agent]
    return cost

def swapTasks(solution, n):
    # Creates a neighboring solution by swapping the assignments of two randomly chosen agents
    new_solution = solution.copy()
    agent1, agent2 = random.sample(range(n), 2)
    # Swapping tasks between the two agents
    new_solution[agent1], new_solution[agent2] = new_solution[agent2], new_solution[agent1]
    return new_solution

def simulatedAnnealing(c, n, initial_temp, cooling_rate, min_temp, max_iter, nReheat):
    start_time = time.time()  # Start time
    
    current_solution = generateInitialSolution(n)
    current_cost = calculateCost(current_solution, c)
    temp = initial_temp

    best_solution = current_solution
    best_cost = current_cost

    reheats = 0
    while reheats < nReheat:
        iteration = 0
        while temp > min_temp and iteration < max_iter:
            new_solution = swapTasks(current_solution, n)
            new_cost = calculateCost(new_solution, c)

            if new_cost < current_cost or random.random() < math.exp((current_cost - new_cost) / temp):
                current_solution, current_cost = new_solution, new_cost
                
                if current_cost < best_cost:
                    best_solution, best_cost = current_solution, current_cost

            temp *= cooling_rate
            iteration += 1
        
        temp = initial_temp  # Reheat by resetting the temperature
        reheats += 1
        
    end_time = time.time()  # End time
    
    return best_solution, best_cost, end_time - start_time

# Parameters for the SA algorithm
initial_temp = 1000
cooling_rate = 0.95
min_temp = 1
max_iter = 10000
nReheat = 5  # Number of times to reheat

# COULD BE REPLACED LATER
# Example cost matrix for assigning tasks to agents
# Assume c[i][j] is the cost of assigning task i to agent j
c = [
    [40, 10, 12],  # Costs of assigning task 1 to agents 1, 2, and 3 respectively
    [25, 30, 7],   # Costs of assigning each agent to task 2
    [22, 6, 40]    # Costs of assigning each agent to task 3
]



n = len(c)  # n agents with n tasks (n*n)

best_solution, best_cost, computation_time = simulatedAnnealing(c, n, initial_temp, cooling_rate, min_temp, max_iter, nReheat)

print("Best solution:", best_solution)
print("Best cost:", best_cost)
print("Computation time (seconds):", computation_time)

''' 
Best solution output example:
[1, 2, 0]
Task 0 (the first task) is assigned to Agent 1 (second agent), at a cost of c[0][1] which is 10.
Task 1 (the second task) is assigned to Agent 2 (third agent), at a cost of c[1][2] which is 7.
Task 2 (the third task) is assigned to Agent 0 (first agent), at a cost of c[2][0] which is 22.

'''