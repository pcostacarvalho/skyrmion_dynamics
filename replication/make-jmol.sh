awk '{printf "Fe %12.6f%12.6f%12.6f\n", $2, $3, $4}' coord.PdFeIr11.out > jmol

NREC=38 

for i in $(seq 1 $NREC)
do
	N=$(tail -n $NREC clus_info.PdFeIr11.out | sed -n ${i}p | awk '{print $2}')
	gsed -i "${N}s/Fe/Nb/" jmol
done
