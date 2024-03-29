import time

def greedy_forward_checking_assignment(cost_matrix):
    """
    Implements a greedy algorithm with forward checking for assignment problems.
    
    Parameters:
    - cost_matrix: 2D matrix representing the cost of assigning tasks to workers.

    Returns:
    - assignment: List representing the assignment of tasks to workers.
    """

    num_tasks = len(cost_matrix)
    # Initializing assignedAgentsForForwardChecking with 0
    assignedAgentsForForwardChecking = [0] * num_tasks
    
    # Initializing assignments with -1
    assignment = [-1] * num_tasks

    for task in range(num_tasks):
        min_cost = float('inf') # infinity value
        assigned_worker = -1

        for worker in range(num_tasks):
            #     ckeck if the worker is already assigned     and    the cost is less
            if assignedAgentsForForwardChecking[worker] == 0  and cost_matrix[task][worker] < min_cost:
                min_cost = cost_matrix[task][worker]
                assigned_worker = worker

        assignment[task] = assigned_worker
        assignedAgentsForForwardChecking[assigned_worker] = 1  # to indicate that the worker is assigend for the next iterations

    return assignment

def print_matrix(matrix):
    for row in matrix:
        print(row)

def print_assignment_description(assignment):
    for task, worker in enumerate(assignment):
        print(f"Task {task + 1} is assigned to Worker {worker + 1}")

# Get the matrix size from the user
n = int(input("Enter the size of the matrix (n): "))

# Generate a dummy cost matrix (replace this with the actual generation logic)
cost_matrix = [[i + j for j in range(n)] for i in range(n)]

# Print the original matrix
print("Original Cost Matrix:")
print_matrix(cost_matrix)

# Measure the computational time
start_time = time.time()

# Call the function
result_assignment = greedy_forward_checking_assignment(cost_matrix)

# Print the result and computational time
print("\nTask assignment:")
print_assignment_description(result_assignment)
print("\nComputational time:", time.time() - start_time, "seconds")
