#!/bin/bash
#SBATCH -o control.out
#SBATCH -J pdi
#SBATCH -N 1
#SBATCH --ntasks-per-node=32
#SBATCH -t 7:30:00
#SBATCH -A snic2021-1-36

./rsnew-ultimo-damping.x > job.out
