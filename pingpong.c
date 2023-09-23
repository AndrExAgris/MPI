#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <mpi.h>

#define MB 1024*1024

int main(int argc, char* argv[]){
    int rank, size, rounds, i, j;
    float sum_send, sum_rtt;
    int bytes[] = {1, 5, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 200};
    char *data = NULL;
    double start, end_send, rtt;
    MPI_Status status;
    int configs = sizeof(bytes)/sizeof(int);

    MPI_Init(&argc, &argv);
    MPI_Comm_rank(MPI_COMM_WORLD, &rank);
    MPI_Comm_size(MPI_COMM_WORLD, &size);

    if (size != 2) {
        printf("Informe 2 processos\n");
        MPI_Abort(MPI_COMM_WORLD, 1);
    }

    if (argc != 2) {
        printf("Informe o # de rodadas\n");
        MPI_Abort(MPI_COMM_WORLD, 1);
    }

    rounds = atoi(argv[1]);
    
    data = (char *) malloc(sizeof(char) * bytes[configs - 1] * MB);
    
    if (!rank) {
        srand(time(NULL));
         for (i = 0; i < bytes[configs - 1]; i++) {
            data[i] = rand();
        }
    }
        
    for (i = 0; i < configs; i++){
        for (j = 0; j < rounds; j++){
            sum_send = 0;
            sum_rtt = 0;
            if (!rank) {
                start = MPI_Wtime();
                MPI_Send(data, bytes[i] * MB, MPI_CHAR, 1, 0, MPI_COMM_WORLD);
                end_send = MPI_Wtime();
                MPI_Recv(data, bytes[i] * MB, MPI_CHAR, 1, 0, MPI_COMM_WORLD, &status);
                rtt = MPI_Wtime();
//                printf("%d MB %d %.6lf %.6lf\n", bytes[i], j, end_send - start, rtt - start);
                sum_send+=(end_send - start);
                sum_rtt+=(rtt - start);
            } else {
                MPI_Recv(data, bytes[i] * MB, MPI_CHAR, 0, 0, MPI_COMM_WORLD, &status);
                MPI_Send(data, bytes[i] * MB, MPI_CHAR, 0, 0, MPI_COMM_WORLD);
            }
        }
	if (!rank) {
            printf("    [%d MB] avg_send %.6lf avg_rtt %.6lf\n", bytes[i], sum_send/(double)rounds, sum_rtt/(double)rounds);
    	}
    }
    MPI_Finalize();
    return 0;
}
