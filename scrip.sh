# Function to search for MPI in a file
# -F to get from file
# -H to get origin file
# -i to ignore case sensitive
# -r to do recursion in directories
search_mpi() {
  grep -FHir "MPI_" "$1" > list_of_mpi
}


# Start searching recursively
search_mpi "$1"
