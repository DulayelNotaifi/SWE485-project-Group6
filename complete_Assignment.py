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
    for task, worker in enumerate(solution):
        cost += c[task][worker]
    return cost

def swapTasks(solution, n):
    # Creates a neighboring solution by swapping the assignments of two randomly chosen workers
    new_solution = solution.copy()
    worker1, worker2 = random.sample(range(n), 2)
    # Swapping tasks between the two workers
    new_solution[worker1], new_solution[worker2] = new_solution[worker2], new_solution[worker1]
    return new_solution

def simulatedAnnealing(c, initial_temp, cooling_rate, min_temp, max_iter, nReheat):
    n = len(c) # n workers with n tasks (n*n)
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
        

    
    return best_solution, best_cost


def printAssignmentResult(best_solution, c):
    print("\nTask assignment:")
    for task, worker in enumerate(best_solution):
        print(f"Task {task+1} is assigned to Worker {worker+1} (Cost: {c[task][worker]})")
    print("Total cost:", calculateCost(best_solution, c))


# Parameters for the SA algorithm
initial_temp = 1000
cooling_rate = 0.95
min_temp = 1
max_iter = 10000
nReheat = 5  # Number of times to reheat


# Assume c[i][j] is the cost of assigning task i to worker (agent) j
c = [
    [40, 10, 12],  # Costs of assigning task 1 to workers 1, 2, and 3 respectively
    [25, 30, 7],   # Costs of assigning each worker to task 2
    [22, 6, 40]    # Costs of assigning each worker to task 3
]


# Start the computational time
start_time = time.time()

best_solution, best_cost = simulatedAnnealing(c, initial_temp, cooling_rate, min_temp, max_iter, nReheat)


# Print the result and computational time
printAssignmentResult(best_solution, c)
print("Computational time:", time.time() - start_time, "seconds")

