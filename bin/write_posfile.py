# %%
# adapted from write-inputs-cluster (Ivan)
import numpy as np
import sys

# %%


def decimal_digits(va, vb, vc):
    maxn = 0

    for i in range(len(va)):
        if int(str(va[i])[::-1].find('.')) >= maxn:
            maxn = int(str(va[i])[::-1].find('.'))
        if int(str(vb[i])[::-1].find('.')) >= maxn:
            maxn = int(str(vb[i])[::-1].find('.'))
        if int(str(vc[i])[::-1].find('.')) >= maxn:

            maxn = int(str(vc[i])[::-1].find('.'))

    return maxn


# %%
def construct_lattice(va, vb, vc, size_x, size_y, size_z, maxn):

    positions = []

    for k in range(size_z):
        for i in range(size_x):
            for j in range(size_y):
                p = (np.multiply(va, i)+np.multiply(vb, j)+np.multiply(vc, k))
                positions.append(p.tolist())

    return np.round(positions, decimals=maxn).tolist()


# %%
def get_center_position(size_x, size_y, size_z, fx, fy, fz):

    mean_x = round(size_x*fx)
    mean_y = round(size_y*fy)
    mean_z = round(size_z*fz)

    center = size_x*size_y*mean_z + size_y*mean_x + mean_y + 1

    return center

# %%


def write_posfile_clus(data_imp, center, positions, NAME, maxn):

    print('Writing posfile_clus \n', end='')

    # index in list of cluster atoms
    index_interactions = list(np.where(data_imp[:, 0] == 1)[0])
    data_imp_positions = data_imp[index_interactions, 2:5]

    posclus = open('posfile_clus_'+NAME, 'w')

    # index in lattice of cluster atoms with center, ordered as firstly defined
    all_sites_imp = []

    all_sites_imp.append(center)
    print('%3s%3s' % (1, 1) +
          '{0:12.6f} {1:12.6f} {2:12.6f}'.format(*positions[center-1]), file=posclus)

    for i in range(len(data_imp_positions)):
        # from center, finding position in lattice of cluster atoms
        pos_now = np.add(positions[center-1], data_imp_positions[i])
        pos_now = np.round(pos_now, decimals=maxn)
        print('%3s%3s' % (i+2, i+2) +
              '{0:12.6f} {1:12.6f} {2:12.6f}'.format(*pos_now), file=posclus)

        # finding index in lattice from position
        ind = int(positions.index(list(pos_now)))+1
        all_sites_imp.append(ind)

    posclus.close()

    print('[ok!]')
    return all_sites_imp


# %%
def write_xyz(all_sites_imp, positions, NAME, maxn):

    # write a *.xyz file with 'Fe' format as the impurities and 'Nb' as the pristine
    #   index order of atoms cluster respect lattice index order
    print('writing file .xyz \n', end='')

    system_file = open('system_'+NAME+'.xyz', 'w')

    print(str(len(positions)) + '\n', file=system_file)

    count = 1
    for i in range(len(positions)):
        pos_now = positions[i]
        pos_now = np.round(pos_now, decimals=maxn)
        if i+1 in all_sites_imp:
            print(
                "Nb " + '{0:12.6f} {1:12.6f} {2:12.6f}'.format(*pos_now), file=system_file)
            count += 1
        else:
            print(
                "Fe" + '{0:12.6f} {1:12.6f} {2:12.6f}'.format(*pos_now), file=system_file)

    system_file.close()
    print('[ok!]')


# %%
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


# %%
data_imp = np.loadtxt('jfile_clus')
variables = read_variables_from_file('lattice_inputs')

### Definitions ####
size_x = variables['size_x']
size_y = variables['size_y']
size_z = variables['size_z']
va = variables['va']
vb = variables['vb']
vc = variables['vc']
fx = variables['fx']
fy = variables['fy']
fz = variables['fz']

NAME = str(size_x)+'x'+str(size_y)+'x'+str(size_z)

maxn = decimal_digits(va, vb, vc)

positions = construct_lattice(va, vb, vc, size_x, size_y, size_z, maxn)

center = get_center_position(size_x, size_y, size_z, fx, fy, fz)

# %%
all_sites_imp = write_posfile_clus(data_imp, center, positions, NAME, maxn)

write_xyz(all_sites_imp, positions, NAME, maxn)

# %%


def write_data_to_file(filename, flag):
    # Define the data to write

    if flag == 0:
        data = [
            (1, 1, 0.000000000, 0.000000000, 0.00000000),
        ]
    else:
        data = [
            (1, 1, 0.000000000, 0.000000000, 0.00000000),
            (2, 2, 0.353500000, 0.204100000, 0.57730000),
            (3, 3, 0.707000000, 0.408200000, 1.15460000),
        ]

    # Open the file and write the data
    with open(filename, 'w') as file:
        for row in data:
            file.write(
                f"{row[0]:2}  {row[1]:2}   {row[2]:12.9f}  {row[3]:12.9f}   {row[4]:12.8f}\n")


# Example usage
output_filename = "posfile_host"
write_data_to_file(output_filename, flag=int(sys.argv[1]))
# print(f"Data has been written to {output_filename}.")
