# MPI

setup: openmpi-bin openmpi-doc libopenmpi-dev

nbp -> https://www.nas.nasa.gov/software/npb.html

achar as chamadas coletivas:

    MPI_Allgather
    Gathers data from all members of a group and sends the data to all members of the group.

    MPI_Allgatherv
    Gathers a variable amount of data from each member of a group and sends the data to all members of the group.

    MPI_Allreduce
    Combines values from all processes and distributes the result back to all processes.

    MPI_Alltoall
    Gathers data from and scatters data to all members of a group.

    MPI_Alltoallv
    Gathers data from and scatters data to all members of a group.

    MPI_Alltoallw
    Gathers data from and scatters data to all members of a group.

    MPI_Barrier
    Initiates barrier synchronization across all members of a group.

    MPI_Bcast
    Broadcasts data from one member of a group to all members of the group.

    MPI_Gather
    Gathers data from all members of a group to one member.

    MPI_Gatherv
    Gathers variable data from all members of a group to one member.

    MPI_Iallgather
    Gathers data from all members of a group and sends the data to all members of the group in a non-blocking way.

    MPI_Iallreduce
    Combines values from all processes and distributes the result back to all processes in a non-blocking way.

    MPI_Ibarrier
    Performs a barrier synchronization across all members of a group in a non-blocking way.

    MPI_Ibcast
    Broadcasts a message from the process with rank "root" to all other processes of the communicator in a non-blocking way.

    MPI_Igather
    Gathers data from all members of a group to one member in a non-blocking way.

    MPI_Igatherv
    Gathers variable data from all members of a group to one member in a non-blocking way.

    MPI_Ireduce
    Performs a global reduce operation (for example sum, maximum, or logical and) across all members of a group in a non-blocking way.

    MPI_Iscatter
    Scatters data from one member across all members of a group in a non-blocking way. This function performs the inverse of the operation that is performed by the MPI_Igatherfunction.

    MPI_Iscatterv
    MPI_Reduce
    Performs a global reduce operation across all members of a group.

    MPI_Scatter
    Scatters data from one member across all members of a group.

    MPI_Scatterv
    Scatters data from one member across all members of a group.

    MPI_Exscan
    Computes the exclusive scan (partial reductions) of data on a collection of processes.

    MPI_Op_create
    Creates a user-defined combination function handle.

    MPI_Op_free
    Frees a user-defined combination function handle.

    MPI_Reduce_local
    Applies a reduction operator to local arguments.

    MPI_Reduce_scatter
    Combines values and scatters the results.

    MPI_Scan
    Computes the scan (partial reductions) of data on a collection of processes.

    MPI_User_function
    MPI_User_function is a placeholder for the application-defined function name.
