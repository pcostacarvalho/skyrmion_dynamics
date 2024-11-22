
for i in $(seq 1 9); do echo "   $i   -0.00000000    0.00000003    0.51241448    2.83583351" >> self_aux; done
for i in $(seq 10 19); do echo "  $i   -0.00000000    0.00000003    0.51241448    2.83583351" >> self_aux; done
for i in $(seq 20 38); do echo "  $i   -0.00000000    0.00000003    0.12336022    2.83583351" >> self_aux; done
for i in $(seq 39 57); do echo "  $i   -0.00000000    0.00000003    0.09795952    2.83583351" >> self_aux; done
for i in $(seq 58 76); do echo "  $i   -0.00000000    0.00000003   -0.00035712    2.83583351" >> self_aux; done
for i in $(seq 77 95); do echo "  $i   -0.00000000    0.00000003   -0.03670596    2.83583351" >> self_aux; done


for i in $(seq 1 9) 
	do
 	echo   " ATOM     Q0NEUTER      Q2NEUTER" >> self_aux
   	echo   "   $i    0.00000000    0.00000000" >> self_aux
   	echo   "   $i    0.00000000    0.00000000" >> self_aux
	echo   "   $i    0.00000000    0.00000000" >> self_aux
	echo   "   $i    0.00000000    0.00000000" >> self_aux
 	echo   "   $i    0.00000000    0.00000000" >> self_aux
	echo   "   $i    0.00000000    0.00000000" >> self_aux
	done

for i in $(seq 10 19)  
        do
        echo   " ATOM     Q0NEUTER      Q2NEUTER" >> self_aux
        echo   "  $i    0.00000000    0.00000000" >> self_aux
        echo   "  $i    0.00000000    0.00000000" >> self_aux
        echo   "  $i    0.00000000    0.00000000" >> self_aux
        echo   "  $i    0.00000000    0.00000000" >> self_aux
        echo   "  $i    0.00000000    0.00000000" >> self_aux
        echo   "  $i    0.00000000    0.00000000" >> self_aux
        done

for i in $(seq 20 38)
        do
	echo   " ATOM     Q0NEUTER	Q2NEUTER" >> self_aux
        echo   "  $i    0.50000000    0.00000000" >> self_aux
        echo   "  $i    0.50000000    0.00000000" >> self_aux
        echo   "  $i    4.00000000    0.00000000" >> self_aux
        echo   "  $i    0.50000000    0.00000000" >> self_aux
        echo   "  $i    0.50000000    0.00000000" >> self_aux
        echo   "  $i    4.00000000    0.00000000" >> self_aux
        done

for i in $(seq 39 57)
        do
	echo   " ATOM     Q0NEUTER	Q2NEUTER" >> self_aux
        echo   "  $i    0.35000000    0.00000000" >> self_aux
        echo   "  $i    0.35000000    0.00000000" >> self_aux
        echo   "  $i    4.30000000    0.00000000" >> self_aux
        echo   "  $i    0.35000000    0.00000000" >> self_aux
        echo   "  $i    0.35000000    0.00000000" >> self_aux
        echo   "  $i    2.30000000    0.00000000" >> self_aux
        done

for i in $(seq 58 76)
        do
	echo   " ATOM     Q0NEUTER	Q2NEUTER" >> self_aux
        echo   "  $i    0.50000000    0.00000000" >> self_aux
        echo   "  $i    0.50000000    0.00000000" >> self_aux
        echo   "  $i    3.50000000    0.00000000" >> self_aux
        echo   "  $i    0.50000000    0.00000000" >> self_aux
        echo   "  $i    0.50000000    0.00000000" >> self_aux
        echo   "  $i    3.50000000    0.00000000" >> self_aux
        done

for i in $(seq 77 95)
        do
	echo   " ATOM     Q0NEUTER	Q2NEUTER" >> self_aux
        echo   "  $i    0.50000000    0.00000000" >> self_aux
        echo   "  $i    0.50000000    0.00000000" >> self_aux
        echo   "  $i    3.50000000    0.00000000" >> self_aux
        echo   "  $i    0.50000000    0.00000000" >> self_aux
        echo   "  $i    0.50000000    0.00000000" >> self_aux
        echo   "  $i    3.50000000    0.00000000" >> self_aux
        done

