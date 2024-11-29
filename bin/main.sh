#!/bin/bash


######## CHANGE HERE #########
path_to_files="/Users/pamaccarvalho/Documents/GitHub/skyrmion_dynamics/bin"

final_path="$PWD/d_asd_files"

FLAG=0 #1layer 

#FLAG=1 #3layer

#############################

rm -rf ${final_path}

mkdir -p ${final_path}

if [ $FLAG -ne 0 ] && [ $FLAG -ne 1 ]; then
	echo -e "The FLAG must be 1 or 0.\n"
	exit 1
fi

size_z=$(grep size_z inputs/lattice_inputs | awk '{print $2}')

if [ $FLAG -eq 0 ] && [ ${size_z} -ne 1 ]; then
	echo -e "Please, set the FLAG accordingly to size_z in lattice inputs. \n"
	exit 1
elif [ $FLAG -eq 1 ] && [ ${size_z} -ne 3 ]; then
	echo -e "Please, set the FLAG accordingly to size_z in lattice inputs. \n"
	exit 1
fi

cp ${path_to_files}/make_jij_imp_files.sh .
cp ${path_to_files}/make_posfile.sh .
cp ${path_to_files}/make_other_files.sh .

gsed -i "s|#PATH_BIN#|\"${path_to_files}\"|g" make_jij_imp_files.sh
gsed -i "s|#PATH_output#|\"${final_path}\"|g" make_jij_imp_files.sh

gsed -i "s|#PATH_BIN#|\"${path_to_files}\"|g" make_posfile.sh
gsed -i "s|#PATH_output#|\"${final_path}\"|g" make_posfile.sh

gsed -i "s|#PATH_BIN#|\"${path_to_files}\"|g" make_other_files.sh
gsed -i "s|#PATH_output#|\"${final_path}\"|g" make_other_files.sh

echo -e "Running block 1: generating files with interactions (jfile and dm) \n"

./make_jij_imp_files.sh ${FLAG}

if [[ $? -eq 1 ]]; then
  echo -e "Failed!\n"
  exit 1
else
  echo -e "Finished successfully\n"
fi

echo -e "Running block 2: generating file with atomic positions (posfile) \n"

./make_posfile.sh ${FLAG}

if [[ $? -eq 1 ]]; then
  echo -e "Failed!\n"
  exit 1
else
  echo -e "Finished successfully\n"
fi

echo -e "Running block 3: generating remaining files (momfile and kfile) \n"

./make_other_files.sh ${FLAG}

if [[ $? -eq 1 ]]; then
  echo -e "Failed!\n"
  exit 1
else
  echo -e "Finished successfully\n"
fi


rm make_jij_imp_files.sh make_posfile.sh make_other_files.sh

