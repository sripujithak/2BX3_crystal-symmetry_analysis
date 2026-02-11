import numpy as np

# ================================
# INPUT / OUTPUT FILES
# ================================
pdb_file = "2BX3.pdb"
output_pdb = "2BX3_lattice.pdb"

atoms = []        # full ATOM lines
coordinates = []  # x, y, z coordinates

# ================================
# READ PDB FILE
# ================================
with open(pdb_file, "r") as f:
    for line in f:
        if line.startswith("ATOM"):
            atoms.append(line)
            x = float(line[30:38])
            y = float(line[38:46])
            z = float(line[46:54])
            coordinates.append([x, y, z])

coordinates = np.array(coordinates)

print("Atoms read:", len(coordinates))
print("First atom coordinate:", coordinates[0])

# ================================
# CRYSTALLOGRAPHIC SYMMETRY OPERATORS
# From REMARK 290 (Space group P 43 21 2)
# ================================
sym_ops = [

    # Operator 1:  X, Y, Z
    (np.array([[ 1,  0,  0],
               [ 0,  1,  0],
               [ 0,  0,  1]]),
     np.array([0.00000, 0.00000, 0.00000])),

    # Operator 2:  -X, -Y, Z+1/2
    (np.array([[-1,  0,  0],
               [ 0, -1,  0],
               [ 0,  0,  1]]),
     np.array([0.00000, 0.00000, 50.09850])),

    # Operator 3:  -Y+1/2, X+1/2, Z+3/4
    (np.array([[ 0, -1,  0],
               [ 1,  0,  0],
               [ 0,  0,  1]]),
     np.array([34.83750, 34.83750, 75.14775])),

    # Operator 4:  Y+1/2, -X+1/2, Z+1/4
    (np.array([[ 0,  1,  0],
               [-1,  0,  0],
               [ 0,  0,  1]]),
     np.array([34.83750, 34.83750, 25.04925])),

    # Operator 5:  -X+1/2, Y+1/2, -Z+3/4
    (np.array([[-1,  0,  0],
               [ 0,  1,  0],
               [ 0,  0, -1]]),
     np.array([34.83750, 34.83750, 75.14775])),

    # Operator 6:  X+1/2, -Y+1/2, -Z+1/4
    (np.array([[ 1,  0,  0],
               [ 0, -1,  0],
               [ 0,  0, -1]]),
     np.array([34.83750, 34.83750, 25.04925])),

    # Operator 7:  Y, X, -Z
    (np.array([[ 0,  1,  0],
               [ 1,  0,  0],
               [ 0,  0, -1]]),
     np.array([0.00000, 0.00000, 0.00000])),

    # Operator 8:  -Y, -X, -Z+1/2
    (np.array([[ 0, -1,  0],
               [-1,  0,  0],
               [ 0,  0, -1]]),
     np.array([0.00000, 0.00000, 50.09850]))
]

# ================================
# WRITE MULTI-MODEL LATTICE PDB
# ================================
with open(output_pdb, "w") as out:
    model_id = 1

    for R, t in sym_ops:
        transformed = coordinates @ R.T + t

        out.write(f"MODEL     {model_id}\n")

        for i, line in enumerate(atoms):
            x, y, z = transformed[i]
            new_line = (
                line[:30]
                + f"{x:8.3f}{y:8.3f}{z:8.3f}"
                + line[54:]
            )
            out.write(new_line)

        out.write("ENDMDL\n")
        model_id += 1

print("Lattice PDB written to:", output_pdb)
print("Total atoms:", len(coordinates) * len(sym_ops))
