import random
import math

def generateInitialSolution(n):
    # Generates a random initial solution: each task is assigned to one and only one agent
    solution = list(range(n))
    random.shuffle(solution)
    return solution

def calculateCost(solution, c):
    cost = 0
    for task, agent in enumerate(solution):
        cost += c[agent][task]
    return cost

def swapTasks(solution, n):
    # Creates a neighboring solution by swapping the assignments of two randomly chosen agents
    new_solution = solution.copy()
    agent1, agent2 = random.sample(range(n), 2)
    # Swapping tasks between the two agents
    new_solution[agent1], new_solution[agent2] = new_solution[agent2], new_solution[agent1]
    return new_solution

def simulatedAnnealing(c, n, initial_temp, cooling_rate, min_temp, max_iter):
    current_solution = generateInitialSolution(n)
    current_cost = calculateCost(current_solution, c)
    temp = initial_temp

    best_solution = current_solution
    best_cost = current_cost

    while temp > min_temp:
        for _ in range(max_iter):
            new_solution = swapTasks(current_solution, n)
            new_cost = calculateCost(new_solution, c)

            if new_cost < current_cost or random.random() < math.exp((current_cost - new_cost) / temp):
                current_solution, current_cost = new_solution, new_cost
                
                if current_cost < best_cost:
                    best_solution, best_cost = current_solution, current_cost

        temp *= cooling_rate

    return best_solution, best_cost

#FOLLOWING CODE WILL BE CHANGED LATER TO BE TAKEN BY USER 

# Parameters for the SA algorithm
initial_temp = 1000
cooling_rate = 0.95
min_temp = 1
max_iter = 10000

# Example cost matrix for assigning tasks to agents
# Assume c[i][j] is the cost of assigning task j to agent i
c = [
    [4, 5, 6],  # Costs for agent 1
    [2, 4, 6],  # Costs for agent 2
    [3, 5, 7]   # Costs for agent 3
]

# n agents with n tasks (n*n)
n = len(c)

best_solution, best_cost = simulatedAnnealing(c, n, initial_temp, cooling_rate, min_temp, max_iter)

print("Best solution:", best_solution)
print("Best cost:", best_cost)
