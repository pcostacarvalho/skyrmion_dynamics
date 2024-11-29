#!/bin/bash

path_to_files=#PATH_BIN#
final_path=#PATH_output#

mkdir -p a_interactions

cd a_interactions

cp ../inputs/jij.imp ../inputs/dij.imp ../inputs/jij.sup ../inputs/dij.sup ../inputs/dij.sup.3l ../inputs/jij.sup.3l .

cp ${path_to_files}/commands-dm ${path_to_files}/commands-jfile ${path_to_files}/commands-new ${path_to_files}/fix_dm.sh ${path_to_files}/fix_jfile.sh ${path_to_files}/rotate_clust.py .


./commands-new


files_to_check=(
  "jfile_clus_1layer"
  "dm_clus_1layer"
  "jij.sup.rot.correct"
  "dij.sup.rot.correct"
  "jfile_clus_3layer"
  "dm_clus_3layer"
  "jij.sup.3l.rot.correct"
  "dij.sup.3l.rot.correct"
)

for file in "${files_to_check[@]}"; do
  if [[ ! -f "$file" ]]; then
    echo "Error: File '$file' does not exist. Exiting script."
    exit 1
  fi
done

if [ $1 -eq 0 ]; then
	cp jfile_clus_1layer ${final_path}/jfile_clus
	cp dm_clus_1layer ${final_path}/dm_clus
	cp jij.sup.rot.correct ${final_path}/jfile_host
	cp dij.sup.rot.correct ${final_path}/dm_host
else
	cp jfile_clus_3layer ${final_path}/jfile_clus
        cp dm_clus_3layer ${final_path}/dm_clus
	awk -v s=2 '{printf "%3s%3s%12.6f%12.6f%12.6f%12.6f%12.6f\n", $1-s, $2-s, $3, $4, $5, $6, $7}' jij.sup.3l.rot.correct > ${final_path}/jfile_host
	awk -v s=2 '{printf "%3s%3s%12.6f%12.6f%12.6f%12.6f%12.6f%12.6f%12.6f\n", $1-s, $2-s, $3, $4, $5, $6, $7, $8, $9}' dij.sup.3l.rot.correct > ${final_path}/dm_host
fi

rm commands-dm commands-jfile commands-new fix_dm.sh fix_jfile.sh rotate_clust.py

cd ../

