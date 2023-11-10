# Define the input file name and the vector to search for matches
input_file = 'list_of_mpi'
collective_calls = ['MPI_Allgather', 'MPI_Allgatherv', 'MPI_Allreduce', 'MPI_Alltoall', 'MPI_Alltoallv', 'MPI_Alltoallw', 'MPI_Barrier', 'MPI_Bcast', 'MPI_Gather', 'MPI_Gatherv',    'MPI_Iallgather', 'MPI_Iallreduce', 'MPI_Ibarrier', 'MPI_Ibcast', 'MPI_Igather', 'MPI_Igatherv', 'MPI_Ireduce', 'MPI_Iscatter', 'MPI_Iscatterv', 'MPI_Reduce', 'MPI_Scatter', 'MPI_Scatterv', 'MPI_Exscan', 'MPI_Op_create', 'MPI_Op_free', 'MPI_Reduce_local', 'MPI_Reduce_scatter', 'MPI_Scan', 'MPI_User_function']
benchmarks = ['BT', 'CG', 'DT', 'EP', 'FT', 'IS', 'LU', 'MG', 'SP']

# Initialize a vector to store the counts
count_vector = [0] * len(collective_calls)

# Initialize a dictionary to store counts for each combination of benchmarks and collective_calls
count_matrix = {}

# Function to compare lines and update the count vector
def update_count_vector(line):
    for i, element in enumerate(collective_calls):
        if element.lower() in line.lower():
            count_vector[i] += 1

# Function to update the count matrix
def update_count_matrix(line):
    if line.strip():  # Check if the line is not empty
        for benchmark in benchmarks:
            if benchmark not in count_matrix:
                count_matrix[benchmark] = [0] * len(collective_calls)

            if benchmark.lower() in line.lower():
                for i, element in enumerate(collective_calls):
                    if element.lower() in line.lower():
                        count_matrix[benchmark][i] += 1



# Read the input file line by line and update the count vector
with open(input_file, 'r') as file:
    for line in file:
        update_count_vector(line)


# Read the input file line by line and update the count matrix
with open(input_file, 'r') as file:
    for line in file:
        update_count_matrix(line)




# Print the count vector
print("Count Vector:")

for i in range(len(collective_calls)):
    print(collective_calls[i]+ ":", count_vector[i])


# Print the count matrix
print("    ", end="")
for call in collective_calls:
    print(f"{call:<10}", end="")
print()

for benchmark in benchmarks:
    print(f"{benchmark:<5}", end="")
    for count in count_matrix[benchmark]:
        print(f"{count:<10}", end="")
    print()