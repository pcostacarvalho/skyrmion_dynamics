awk -v s=19 '{printf "%3s 1 %12.6f%12.6f%12.6f%12.6f\n", $2-s, $5, 0, 0, 1}' moments > momfile_clus 
