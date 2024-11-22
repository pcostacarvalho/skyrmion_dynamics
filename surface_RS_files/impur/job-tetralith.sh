#!/bin/bash
#SBATCH -o control.out
#SBATCH -J impur
#SBATCH -N 1
#SBATCH -t 00:20:00
#SBATCH -A snic2022-1-36

export OMP_NUM_THREADS=4
mpprun -np 8 ./rsnew-ultimo-damping.x > job.out
