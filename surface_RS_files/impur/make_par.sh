#cria os arquivos uppar, dwpar e jinfo a partir de uppar.surf, dwpar.surf, jinfo.surf

#para uppar/dwpar

nuppar="uppar.ll22"
ndwpar="dwpar.ll22"
name="ll22"

a=$((5))                    
b=$((8))

for i in $(seq 1 5)
do

	if [ $i == 1 ]
	then
		sed "$a,$b!d" $nuppar > uppar.es.$name
		sed "$a,$b!d" $ndwpar > dwpar.es.$name
	fi

	if [ $i == 2 ]
        then
                sed "$a,$b!d" $nuppar > uppar.pd.$name
                sed "$a,$b!d" $ndwpar > dwpar.pd.$name
        fi

	if [ $i == 3 ]
        then
                sed "$a,$b!d" $nuppar > uppar.fe.$name
                sed "$a,$b!d" $ndwpar > dwpar.fe.$name
        fi

	if [ $i == 4 ]
        then
                sed "$a,$b!d" $nuppar > uppar.ir.$name
                sed "$a,$b!d" $ndwpar > dwpar.ir.$name
        fi

	if [ $i == 5 ]
        then
                sed "$a,$b!d" $nuppar > uppar.ir2.$name
                sed "$a,$b!d" $ndwpar > dwpar.ir2.$name
        fi

	a=$(($b+1))               
	b=$(($a+3))

done

more uppar.$name > uppar
more dwpar.$name > dwpar

for i in $(seq 1 19); do more uppar.es.$name >> uppar; done
for i in $(seq 20 38); do more uppar.pd.$name >> uppar; done
for i in $(seq 39 57); do more uppar.fe.$name >> uppar; done
for i in $(seq 58 76); do more uppar.ir.$name >> uppar; done
for i in $(seq 77 95); do more uppar.ir2.$name >> uppar; done


for i in $(seq 1 19); do more dwpar.es.$name >> dwpar; done
for i in $(seq 20 38); do more dwpar.pd.$name >> dwpar; done
for i in $(seq 39 57); do more dwpar.fe.$name >> dwpar; done
for i in $(seq 58 76); do more dwpar.ir.$name >> dwpar; done
for i in $(seq 77 95); do more dwpar.ir2.$name >> dwpar; done


