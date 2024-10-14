#rotate jij and dij files; correct them for UppASD

#pristine surface
NAME='sup'
gsed "s/#NAME/${NAME}/g" rotate_clust.py > rotate_temp.py
python3 rotate_temp.py

gsed "s/#NAME/${NAME}.rot/g" fix_jfile.sh > fix_jfile_temp.sh
chmod +x fix_jfile_temp.sh
./fix_jfile_temp.sh

gsed "s/#NAME/${NAME}.rot/g" fix_dm.sh > fix_dm_temp.sh  
chmod +x fix_dm_temp.sh
./fix_dm_temp.sh

rm rotate_temp.py fix_jfile_temp.sh fix_dm_temp.sh


