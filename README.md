# skyrmion_dynamics repository
This folder contains the necessary files to create UppASD input files for impurity cluster from RS-LMTO-ASA calculations.

To use this, copy the main.sh file into the a new folder and change the CHANGE HERE section with the correct path to the bin
folder. The final_path may be change in to the any folder name.

Create a folder named 'inputs'. Inside this folder, the necessary information from the RS-LMTO-ASA output should be 
contained in the following files:

-dij.imp: DM interactions from the impurity cluster (for the case with 3 layers)
-jij.imp: J interactions from the impurity cluster (for the case with 3 layers) 
-dij.sup: DM interactions from the pristine surface (for the case with 1 layer)
-jij.sup: J interactions from the pristine surface (for the case with 1 layer)
-dij.sup.3l: DM interactions from the pristine surface (for the case with 3 layers) 
-jij.sup.3l: J interactions from the pristine surface (for the case with 3 layers)

*NOTE that the interactions from the empty spheres layer has been excluded and the NBULK value here is 8. Alterations must
be made to run this code for other pristine surfaces. 

-moments.host.1l: magnetic moments for the atoms in the pristine surface (for the case with 1 layer)
-moments.host.3l: magnetic moments for the atoms in the pristine surface (for the case with 3 layers)
-moments.imp.1l: magnetic moments for the atoms in the impurity cluster (for the case with 1 layer)
-moments.imp.3l: magnetic moments for the atoms in the impurity cluster (for the case with 3 layers)

*NOTE the structure of these files are:

number_of_atom magnetic_moment

-lattice_inputs: file with lattice information such as name of the simulation (simid), size (size_x, size_y, size_z), 
primitive vectors (va, vb, vc) and relative position of the impurity cluster in the lattice (fx, fy, fz).

Check the test_automated folder for an example. 
 
