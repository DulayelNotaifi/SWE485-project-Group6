import random
import math
import time

# Function to generate a random initial solution
def generateInitialSolution(n):
    """
    Generates a random initial solution.

    Parameters:
    - n (int): Number of workers.

    Returns:
    - solution (list): A 1D list representing a random permutation of workers, which represents initial task assignments.
    """
    # Generates a random permutation of workers representing initial task assignments
    solution = list(range(n))
    random.shuffle(solution)
    return solution

# Function to calculate the total cost of a given solution
def calculateCost(solution, c):
    """
    Calculates the total cost of a given solution.

    Parameters:
    - solution (list): A 1D list representing the task assignment to workers.
    - c (list): A 2D matrix representing the cost of assigning each task to each worker.

    Returns:
    - cost (int): Total cost of the solution.
    """
    cost = 0
    # Calculates the total cost by summing the costs of task assignments for each worker
    for task, worker in enumerate(solution):
        cost += c[task][worker]
    return cost

# Function to generate a neighboring solution by swapping tasks between two workers
def swapTasks(solution, n):
    """
    Creates a neighboring solution by swapping the assignments of two randomly chosen workers.

    Parameters:
    - solution (list): Current task assignment to workers.
    - n (int): Number of workers.

    Returns:
    - new_solution (list): A neighboring solution obtained by swapping tasks between two workers.
    """
    # Creates a neighboring solution by swapping the assignments of two randomly chosen workers
    new_solution = solution.copy()
    worker1, worker2 = random.sample(range(n), 2)
    # Swapping tasks between the two workers
    new_solution[worker1], new_solution[worker2] = new_solution[worker2], new_solution[worker1]
    return new_solution

# Simulated Annealing algorithm implementation
def simulatedAnnealing(c, initial_temp, cooling_rate, min_temp, max_iter, nReheat):
    """
    Implementation of the Simulated Annealing algorithm to solve the task assignment problem.

    Parameters:
    - c (list): A 2D matrix representing the cost of assigning each task to each worker. Each element c[i][j] represents the cost of assigning task i to worker j.
    - initial_temp (float): Initial temperature.
    - cooling_rate (float): Rate at which the temperature is reduced.
    - min_temp (float): Minimum temperature threshold.
    - max_iter (int): Maximum number of iterations.
    - nReheat (int): Number of times to reheat.

    Returns:
   - best_solution (list): The best solution found by the algorithm. 
   - best_cost (float): The corresponding cost of the best solution. 
    """
    n = len(c) # n workers with n tasks (n*n)
    current_solution = generateInitialSolution(n) # Generate initial random solution
    current_cost = calculateCost(current_solution, c) # Calculate cost of initial solution
    temp = initial_temp # Set initial temperature

    best_solution = current_solution # Initialize best solution
    best_cost = current_cost # Initialize best cost

    reheats = 0
    while reheats < nReheat:
        iteration = 0
        while temp > min_temp and iteration < max_iter:
            new_solution = swapTasks(current_solution, n)
            new_cost = calculateCost(new_solution, c)
            # Accept the new solution if it improves the cost or with a probability based on the temperature
            if new_cost < current_cost or random.random() < math.exp((current_cost - new_cost) / temp):
                current_solution, current_cost = new_solution, new_cost
               # Update the best solution if the current solution is better
                if current_cost < best_cost:
                    best_solution, best_cost = current_solution, current_cost
            temp *= cooling_rate # Cooling down the temperature
            iteration += 1
        
        temp = initial_temp # Reheat by resetting the temperature
        reheats += 1

    return best_solution, best_cost

# Function to print the final task assignment result
def printAssignmentResult(best_solution, c):
    """
    Prints the final task assignment result.

    Parameters:
    - best_solution (list): Best task assignment to workers.
    - c (list): Cost matrix representing the cost of assigning each task to each worker.
    """
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

# Cost matrix representing the cost of assigning each task to each worker
c = [
    [40, 10, 12],  # Costs of assigning task 1 to workers 1, 2, and 3 respectively
    [25, 30, 7],   # Costs of assigning each worker to task 2
    [22, 6, 40]    # Costs of assigning each worker to task 3
]

# Start the computational time
start_time = time.time()

# Run the Simulated Annealing algorithm
best_solution, best_cost = simulatedAnnealing(c, initial_temp, cooling_rate, min_temp, max_iter, nReheat)

# Print the result and computational time
printAssignmentResult(best_solution, c)
print("Computational time:", time.time() - start_time, "seconds")
