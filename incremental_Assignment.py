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
    # Initializing assignedTasksForForwardChecking with 0
    assignedTasksForForwardChecking = [0] * num_tasks
    
    # Initializing assignments with -1
    assignment = [-1] * num_tasks

    # Dummy solution (replace this with the actual implementation)
    num_tasks = len(cost_matrix)
    #assignment = [i % len(cost_matrix[0]) for i in range(num_tasks)]
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
    for task, worker in enumerate(assignment):
        print(f"Task {task + 1} is assigned to Worker {worker + 1}")

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
