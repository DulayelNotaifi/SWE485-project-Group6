import time
import random

def do_assignment(cost_matrix):
    """
    Implements the algorithm for assignment problems.

    Parameters:
    - cost_matrix: 2D matrix representing the cost of assigning tasks to workers.

    Returns:
    - assignment: List representing the assignment of tasks to workers.
    """
    num_tasks = len(cost_matrix)
    # Initialize assignedAgentsForForwardChecking with 0 to track the assignment status of workers. 1 indicates assigned, 0 indicates unassigned.
    assignedAgentsForForwardChecking = [0] * num_tasks  
    # Ex: if worker 1 is assigned then assignedAgentsForForwardChecking[0] will be 1
    
    # Initialize assignments with -1, indicating that no worker is initially assigned to each task. 
    # The index represents each task, and the value will be updated to the index of the worker assigned to that task.
    assignment = [-1] * num_tasks 
    # Ex: if task 1 is assigned to worker 2 then assignment[0] will be 2 

    for task in range(num_tasks):
        min_cost = float('inf') # initially infinity value
        assigned_worker = -1 # Initially, set to -1 to indicate that no worker has been assigned to the current task.

        for worker in range(num_tasks):
           # Check if the worker is not already assigned (0) and if the cost for this worker and task is the lowest seen so far.
            if assignedAgentsForForwardChecking[worker] == 0  and cost_matrix[task][worker] < min_cost:
                min_cost = cost_matrix[task][worker] # Update min_cost with the lowest cost found for assigning this task.
                assigned_worker = worker  # Update assigned_worker to the current worker who offers the lowest cost for this task.

        assignment[task] = assigned_worker # Assign the task to the worker with the lowest cost for this task.
        assignedAgentsForForwardChecking[assigned_worker] = 1  # Mark the worker as assigned.

    return assignment

def generate_random_cost_matrix(n):
    """
    Generates a random cost matrix for testing.

    Parameters:
    - n: Size of the matrix.

    Returns:
    - cost_matrix: 2D matrix with random costs.
    """
    return [[random.randint(1, 10) for _ in range(n)] for _ in range(n)]

def print_matrix(matrix):
    for row in matrix:
        print(row)

def print_assignment_description(assignment):
    total_cost = 0
    for task, worker in enumerate(assignment):
        cost = cost_matrix[task][worker]  # Get the cost of assigning this task to this worker
        total_cost += cost  # Add the cost to the total cost
        print(f"Task {task + 1} is assigned to Worker {worker + 1} (Cost: {cost})")
    print("Total cost:", total_cost)

# Ask the user for the matrix size and the number of instances
n = int(input("Enter the size of the matrix (n): "))
num_instances = int(input("Enter the number of instances to test: "))

for instance in range(num_instances):
    print(f"\nInstance {instance + 1}:")

    # Choose whether to use a user-entered matrix or a randomly generated one
    use_user_matrix = input("Do you want to enter your own cost matrix? (y/n): ").lower() == 'y'

    if use_user_matrix:
        # Allow the user to input their own cost matrix
        cost_matrix = [[int(input(f"Enter cost for task {i + 1} and worker {j + 1}: ")) for j in range(n)] for i in range(n)]
        print("User-Entered Cost Matrix:")
        print_matrix(cost_matrix)
    else:
        # Generate a random cost matrix
        cost_matrix = generate_random_cost_matrix(n)
        print("Randomly Generated Cost Matrix:")
        print_matrix(cost_matrix)

    # Measure the computational time
    start_time = time.time()

    # Call the function
    result_assignment = do_assignment(cost_matrix)

    # Print the result and computational time
    print("\nTask assignment:")
    print_assignment_description(result_assignment)
    print("Computational time:", time.time() - start_time, "seconds")
