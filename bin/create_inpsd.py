import sys


def read_variables_from_file(filename):
    variables = {}

    with open(filename, 'r') as file:
        for line in file:
            # Strip leading/trailing whitespaces
            line = line.strip()

            # Skip empty lines
            if not line:
                continue

            # Split by first space to separate key and value
            key, value = line.split(maxsplit=1)

            # Process value
            if value.startswith("[") and value.endswith("]"):
                # Convert to list of floats
                value = [float(x) for x in value.strip("[]").split(",")]
            elif "/" in value:
                # Handle fractions
                numerator, denominator = map(int, value.split("/"))
                value = numerator / denominator
            elif value.isdigit():
                # Convert to integers
                value = int(value)
            elif value.replace(".", "", 1).isdigit() and value.count('.') < 2:
                # Handle float values
                value = float(value)
            else:
                # If it's a string, leave it as is
                value = value.strip()

            # Assign to dictionary
            variables[key] = value

    return variables


def write_config_to_file(filename, simid, size_x, size_y, size_z, va, vb, vc):

    va_str = "     ".join([f"{x:0.6f}" for x in va])
    vb_str = "     ".join([f"{x:0.6f}" for x in vb])
    vc_str = "     ".join([f"{x:0.6f}" for x in vc])
    content = f"""simid {simid}
ncell    {size_x}       {size_y}        {size_z}                System size
BC       P       P         0                 Boundary conditions (0=vacuum,P=periodic)

cell    {va_str}
        {vb_str}
        {vc_str}

Sym       0                                     Symmetry of lattice (0 for no, 1 for cubic, 2 for 2d cubic, 3 for hexagonal)

ncell_clus   1       1         1 

cell_clus    0.000000     0.000000     0.000000
             0.000000     0.000000     0.000000
             0.000000     0.000000     1.000000

maptype 1
Mensemble 1
do_prnstruct 1
do_cluster Y

posfile  ./posfile_host
posfile_clus ./posfile_clus
exchange ./jfile_host
exchange_clus ./jfile_clus 
momfile  ./momfile_host
momfile_clus ./momfile_clus
dm ./dm_host
dm_clus ./dm_clus
anisotropy ./kfile_host
anisotropy_clus ./kfile_clus

Initmag   4                                     (1=random, 2=cone, 3=spec., 4=file)
restartfile ./start.bubble

ip_mode N                                         Initial phase parameters
ip_mcanneal 8
        20000  350
        20000   50
        20000   30
        20000   10
        20000    1
        20000    0.01
        20000    0.001
        20000    0.0001
ip_hfield 0.0 0.0 0

mode      S                                     S=SD, M=MC           
Temp      1e-6         K                     Measurement phase parameters
damping   0.5                               Damping parameter
nstep   50000                                 Number of time-steps
timestep  1.000e-15        s                    The time step-size for the SDE-solver
hfield 0.0 0.0 3.0

do_proj_avrg Y

plotenergy   1
do_cumu Y
cumu_step 50
cumu_buff 10
do_avrg Y
do_tottraj Y                                    Measure moments
tottraj_step       100
tottraj_buff       10                           time step, buffer size
avrg_step 100
avrg_buff 10
skyno T
alat 3.84e-10

!do_skyno_cmass Y
!stt A
!jvec  1.00000000 0.0000000000 0.0000000000
!adibeta 0.05"""

    # Open the file and write the content to it
    with open(filename, 'w') as f:
        f.write(content)

    print(f"Configuration written to {filename}")


variables = read_variables_from_file('lattice_inputs')

### Definitions ####
simid = variables['simid']
size_x = variables['size_x']
size_y = variables['size_y']
size_z = variables['size_z']
va = variables['va']
vb = variables['vb']
vc = variables['vc']

filename = 'inpsd.dat'  # The first argument is the filename

write_config_to_file(filename, simid, size_x, size_y, size_z, va, vb, vc)
