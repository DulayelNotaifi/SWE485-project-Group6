import random
import math
import time

# Function to generate a random initial solution
def generateInitialSolution(n):
    """
    Generates a random initial solution for the task assignment problem.

    Parameters:
    - n (int): The number of workers, also indicating the number of tasks.

    Returns:
    - solution (list): A randomized list of worker indices, representing initial task assignments.
    """
    # Create a list of worker indices and shuffle it to represent a random task assignment
    solution = list(range(n))
    random.shuffle(solution)
    return solution

# Function to calculate the total cost of a given solution
def calculateCost(solution, c):
    """
    Calculates the total cost of a solution based on the given cost matrix.

    Parameters:
    - solution (list): A list of task assignments where each index represents a task, and its value represents the assigned worker.
    - c (list): A cost matrix where c[task][worker] represents the cost of assigning task to worker.

    Returns:
    - cost (int): The total cost of the solution based on the given assignments.
    """
    # Aggregate the cost of each task assignment from the solution
    cost = 0
    # Calculates the total cost by summing the costs of task assignments for each worker
    for task, worker in enumerate(solution):
        cost += c[task][worker]
    return cost

# Function to generate a neighboring solution by swapping tasks between two workers
def swapTasks(solution, n):
    """
    Generates a neighboring solution by swapping tasks between two randomly chosen workers.

    Parameters:
    - solution (list): The current task assignments.
    - n (int): Number of workers (and tasks).

    Returns:
    - new_solution (list): A slightly altered version of the input solution.
    """
    # Copy the current solution and swap tasks of two randomly selected workers
    new_solution = solution.copy()
    # Swapping tasks between the two workers
    worker1, worker2 = random.sample(range(n), 2)
    new_solution[worker1], new_solution[worker2] = new_solution[worker2], new_solution[worker1]
    return new_solution

# Simulated Annealing algorithm implementation
def simulatedAnnealing(c, initial_temp, cooling_rate, min_temp, max_iter, nReheat):
    """
    Applies the Simulated Annealing algorithm to find a near-optimal solution for the task assignment problem.

    Parameters:
    - c (list): Cost matrix.
    - initial_temp (float): The starting temperature for annealing.
    - cooling_rate (float): The rate at which the temperature decreases.
    - min_temp (float): The minimum temperature to terminate the algorithm.
    - max_iter (int): Maximum iterations per temperature level.
    - nReheat (int): Number of reheating phases to avoid local minima.

    Returns:
    - best_solution (list): The best solution found.
    - best_cost (float): The cost of the best solution.
    """
    # Initialization
    n = len(c)
    current_solution = generateInitialSolution(n)
    current_cost = calculateCost(current_solution, c)
    temp = initial_temp

    best_solution = current_solution
    best_cost = current_cost

    # Simulated annealing process with reheating
    reheats = 0
    while reheats < nReheat:
        iteration = 0
        while temp > min_temp and iteration < max_iter:
            new_solution = swapTasks(current_solution, n)
            new_cost = calculateCost(new_solution, c)

            # Decide whether to accept the new solution
            if new_cost < current_cost or random.random() < math.exp((current_cost - new_cost) / temp):
                current_solution, current_cost = new_solution, new_cost
                # Update the best solution if the current solution is better
                if current_cost < best_cost:
                    best_solution, best_cost = current_solution, current_cost
            temp *= cooling_rate  # Cool down
            iteration += 1
        
        temp = initial_temp  # Reheat
        reheats += 1

    return best_solution, best_cost

# Function to print the final task assignment result
def printAssignmentResult(best_solution, c):
    """
    Prints the final task assignments and the total cost of the solution.

    Parameters:
    - best_solution (list): The best task assignment found by the algorithm.
    - c (list): The cost matrix for the problem.
    """
    print("\nTask assignment:")
    for task, worker in enumerate(best_solution):
        print(f"Task {task+1} is assigned to Worker {worker+1} (Cost: {c[task][worker]})")
    print("Total cost:", calculateCost(best_solution, c))

# Algorithm parameters
initial_temp = 1000
cooling_rate = 0.95
min_temp = 1
max_iter = 10000
nReheat = 5  # Number of reheating phases

# Cost matrix for the task assignment problem
c = [
    [40, 10, 12],  # Costs for task 1
    [25, 30, 7],   # Costs for task 2
    [22, 6, 40]    # Costs for task 3
]

# Start timing the algorithm
start_time = time.time()

# Run the Simulated Annealing algorithm
best_solution, best_cost = simulatedAnnealing(c, initial_temp, cooling_rate, min_temp, max_iter, nReheat)

# Print the results and the computational time
printAssignmentResult(best_solution, c)
print("Computational time:", time.time() - start_time, "seconds")



