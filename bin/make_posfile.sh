#!/bin/bash

path_to_files=#PATH_BIN#
final_path=#PATH_output#

mkdir -p b_posfile

cd b_posfile

cp ${path_to_files}/write_posfile.py .
cp ${final_path}/jfile_clus . 
cp ../inputs/lattice_inputs .

python3 write_posfile.py "$1"

sx=$(grep size_x lattice_inputs| awk '{print $2}')
sy=$(grep size_y lattice_inputs| awk '{print $2}')
sz=$(grep size_z lattice_inputs| awk '{print $2}')

files_to_check=(
  "posfile_clus_${sx}x${sy}x${sz}"
  "posfile_host"
)

for file in "${files_to_check[@]}"; do
  if [[ ! -f "$file" ]]; then
    echo "Error: File '$file' does not exist. Exiting script."
    exit 1
  fi
done

cp posfile_clus_${sx}x${sy}x${sz} ${final_path}/posfile_clus
cp posfile_host ${final_path}/

rm write_posfile.py 

cd ../
