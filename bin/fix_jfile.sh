rm -f jij.#NAME.correct

#sed  's/\./,/g' dij.out| awk '{printf("%8s%8s  %12.6f%12.6f%12.6f  %12.6f%12.6f%12.6f %12.6f\n", $1, $2, $3/3.89, $4/3.89, $5/3.89, $6, $7, $8, $9/3.89)}' > dij.aux

awk '{printf ("%1s %1s%12s%12s%12s\n", $1, $2, $3, $4, $5)}' jij.#NAME > aux

gsed -i -E 's/(0\.577).{3}/\1300/' aux

gsed -i -E 's/(1\.154).{3}/\1600/' aux

gsed -i -E 's/(1\.731).{3}/\1900/' aux

gsed -i -E 's/(0\.204).{3}/\1100/' aux

gsed -i -E 's/(0\.408).{3}/\1200/' aux

gsed -i -E 's/(0\.816).{3}/\1400/' aux

gsed -i -E 's/(1\.02).{4}/\10500/' aux

gsed -i -E 's/(1\.428).{3}/\1700/' aux

gsed -i -E 's/(1\.632).{3}/\1800/' aux

gsed -i -E 's/(2\.04).{4}/\11000/' aux

gsed -i -E 's/(2\.24).{4}/\15100/' aux

gsed -i -E 's/(2\.653).{3}/\1300/' aux

gsed -i -E 's/(2\.857).{3}/\1400/' aux

gsed -i -E 's/(0\.353).{3}/\1500/' aux

gsed -i -E 's/(0\.707).{3}/\1000/' aux

gsed -i -E 's/(\.414).{3}/\1000/' aux

gsed -i -E 's/(\.060).{3}/\1500/' aux

gsed -i -E 's/(1\.76).{4}/\17500/' aux

gsed -i -E 's/(1\.83).{4}/\16900/' aux

gsed -i -E 's/(2\.47).{4}/\14500/' aux

gsed -i -E 's/(2\.12).{4}/\11000/' aux

gsed -i -E 's/(0\.612).{3}/\1300/' aux

gsed -i -E 's/(1\.22).{4}/\14600/' aux

gsed -i -E 's/(2\.44).{4}/\19200/' aux

gsed -i -E 's/(2\.82).{4}/\18000/' aux

gsed -i -E 's/(3\.06).{4}/\11500/' aux

gsed -i -E 's/(3\.18).{4}/\11500/' aux

gsed -i -E 's/(3\.53).{4}/\15000/' aux

gsed -i -E 's/(3\.67).{4}/\13800/' aux

gsed -i -E 's/(3\.88).{4}/\18500/' aux

gsed -i -E 's/(4\.24).{4}/\12000/' aux

gsed -i -E 's/(4\.28).{4}/\16100/' aux

gsed -i -E 's/(4\.59).{4}/\15500/' aux

gsed -i -E 's/(4\.898).{3}/\1400/' aux

gsed -i -E 's/(4\.949).{3}/\1000/' aux

gsed -i -E 's/(5\.3).{5}/\102500/' aux

gsed -i -E 's/(5\.51).{4}/\10700/' aux

gsed -i -E 's/(5\.656).{3}/\1000/' aux

gsed -i -E 's/(6\.0).{5}/\109500/' aux

gsed -i -E 's/(6\.123).{3}/\1000/' aux

gsed -i -E 's/(6\.363).{3}/\1000/' aux

gsed -i -E 's/(6\.73).{4}/\15300/' aux

gsed -i -E 's/(6\.71).{4}/\16500/' aux

gsed -i -E 's/(0\.0000).{2}/\100/' aux

gsed 's/\./,/g' jij.#NAME | awk '{printf("%12s%12s\n", $6, $7)}' > aux.2
gsed -i 's/\,/./g' aux.2

paste aux aux.2 > jij.#NAME.correct
rm aux aux.2
