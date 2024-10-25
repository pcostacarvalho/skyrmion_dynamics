#size=$(wc -l moment.PdFeIr11.out | awk '{print $1}')
rm moment.reduced

tail -n +8 moment.PdFeIr11.out > aux


for i in $(seq 0 10 1500)
do
        ini=$(($i*$size + 1))
        fin=$(($ini+$size-1))
        gsed -n "$ini,$fin p" aux >> moment.reduced
done

rm aux

mv moment.PdFeIr11.out moment.PdFeIr11.full
mv moment.reduced moment.PdFeIr11.out

