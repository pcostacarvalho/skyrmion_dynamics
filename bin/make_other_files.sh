#!/bin/bash

path_to_files=#PATH_BIN#
final_path=#PATH_output#

mkdir -p c_other_files

cd c_other_files

cp ${path_to_files}/create_inpsd.py .
cp ../inputs/lattice_inputs .

python create_inpsd.py

cp ${path_to_files}/create_momfile.py .

if [ $1 == 0 ]; then
        python create_momfile.py ../inputs/moments.host.1l momfile_host
        python create_momfile.py ../inputs/moments.imp.1l momfile_clus
else
        python create_momfile.py ../inputs/moments.host.3l momfile_host
        python create_momfile.py ../inputs/moments.imp.3l momfile_clus
fi

files_to_check=(
  "momfile_clus"
  "momfile_host"
  "inpsd.dat" 
)
 
for file in "${files_to_check[@]}"; do
  if [[ ! -f "$file" ]]; then
    echo "Error: File '$file' does not exist. Exiting script."
    exit 1
  fi
done


cp  ${path_to_files}/create_kfile.py .

python create_kfile.py "$1"

files_to_check=(
  "kfile_clus"                  
  "kfile_host"
)

for file in "${files_to_check[@]}"; do
  if [[ ! -f "$file" ]]; then
    echo "Error: File '$file' does not exist. Exiting script."
    exit 1
  fi
done

rm create_momfile.py create_kfile.py create_inpsd.py lattice_inputs 

cp kfile_clus kfile_host momfile_host momfile_clus inpsd.dat ${final_path}/
cd ../
