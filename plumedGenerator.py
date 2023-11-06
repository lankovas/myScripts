import numpy as np

"""
This module generates plumed.dat file from topology (*.top file)
It is possible to choose sigma, height of the hill and pace.
One can also decide whether the hills would be added to phi, psi or both.
"""
"""
try:
    print(f"Plese provide the value of sigma:")
    sigma = float(input())
    print("height of the hill:")
    height = float(input())
    print("pace:")
    pace = float(input())
except ValueError as tex:
    print(f"{tex.__class__.__name__}, {tex}")
except Exception as ex:
    print(f"Unexpected error: {ex}")
"""
dihedral_atoms = []
dihedrals_list = []

try:
    #topology_file_name = input("now the name of topology file (without .top)") + ".top"
    topology_file_name = "5awl.top"

    appending_atoms = False
    appending_dihedrals = False
    residue_count = 0

    with open(topology_file_name, "r", encoding="utf-8") as file:
        for line in file:
            if line == "\n":
                appending_atoms = False
                appending_dihedrals = False
            if line == "[ atoms ]\n":
                appending_atoms = True
            if appending_atoms == True:
                if "atom" in line:
                    continue
                if "residue" in line:
                    residue_count += 1
                    continue
                line = line.strip()  # Remove leading/trailing whitespace
                if line:  # Check if the line is not empty
                    values = line.split()  # Split and convert to integers
                    if values[4] == "N" or values[4] == "C" or values[4] == "CA":
                        dihedral_atoms.append([int(values[0]), int(values[2]), values[4]])
            """
            if line == "[ dihedrals ]\n":
                appending_dihedrals = True
            if appending_dihedrals:
                if "dihedrals" in line or ";" in line:
                    continue
                line = line.strip()  # Remove leading/trailing whitespace
                if line:  # Check if the line is not empty
                    values = [int(value) for value in line.split()]  # Split and convert to integers
                    dihedrals_list.append(values[:-1])
            """
        print(dihedral_atoms)
        #print(residue_count)
except FileNotFoundError as fex:
    print(f"You topology cannot be found: {fex}")
except Exception as ex:
    print(f"Unexpected error: {ex}")

phis = []
psis = []

for index, atom in enumerate(dihedral_atoms):

    if atom[2] == "C":
        if not atom[1] == residue_count:
            psis.append(atom[0])
        if index == 0 or index == 1:
            continue
        else:
            if atom[1] == 1 or atom[1] == residue_count:
                phis.append(atom[0])
            else:
                phis.append(atom[0])
                phis.append(atom[0])
    if atom[2] == "N":
        if atom[1] == 1 or atom[1] == residue_count:
            psis.append(atom[0])
        else:
            psis.append(atom[0])
            psis.append(atom[0])
        if index == 0 or index == 1:
            continue
        else:
            phis.append(atom[0])
    if atom[2] == "CA":
        if not atom[1] == residue_count:
            psis.append(atom[0])
        if index == 0 or index == 1:
            continue
        else:
            phis.append(atom[0])


phis = [phis[i:i+4] for i in range (0,len(phis), 4)]
psis = [psis[i:i+4] for i in range (0,len(psis), 4)]
#split_lists = [original_list[i:i+chunk_size] for i in range(0, len(original_list), chunk_size)]
print(phis)
print(psis)