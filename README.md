


# Crystallographic Symmetry Analysis and Crystal Packing of SARS Coronavirus Main Protease (PDB ID: 2BX3)

**Assignment for the Course:** Biophysics  
 

---

## Abstract

This project presents a systematic crystallographic symmetry analysis of the SARS Coronavirus Main Protease (UniProt ID: P43212; PDB ID: 2BX3). Explicit crystallographic symmetry operators obtained from the Protein Data Bank were applied directly to atomic coordinates using matrix-based transformations implemented in Python. The resulting symmetry-related molecules were visualized using PyMOL to examine crystal packing within the tetragonal unit cell. The study emphasizes the distinction between crystallographic symmetry and biological assembly and demonstrates the role of space group symmetry in defining protein organization within a crystal lattice.

---

## Objectives

The objectives of this assignment were to:

- Select a protein crystal structure exhibiting higher-order crystallographic symmetry.
- Identify crystallographic symmetry operators from PDB metadata.
- Apply symmetry operations to atomic coordinates using rotation matrices and translation vectors.
- Generate symmetry-related molecules corresponding to the crystal space group.
- Visualize and analyze crystal packing using molecular visualization tools.

---

## Software and Resources

- **Python** (VS Code / Spyder) – implementation of symmetry transformations  
- **PyMOL** – molecular visualization and lattice inspection  
- **RCSB Protein Data Bank (PDB)** – structural and crystallographic data  

---

## Structure Selection and Rationale

The crystal structure of the SARS Coronavirus Main Protease (PDB ID: 2BX3) was selected due to the following characteristics:

- Crystallization in the higher-order space group **P 43 21 2**
- Availability of multiple crystallographic symmetry operators suitable for explicit analysis
- High-resolution X-ray diffraction data (2.00 Å), ensuring reliable atomic coordinates
- Complete crystallographic metadata provided in the PDB file under **REMARK 290**

---

## Crystallographic Parameters

Based on information obtained from the PDB file and the RCSB database:

- **Space group:** P 43 21 2  
- **Crystal system:** Tetragonal  
- **Unit cell dimensions:**  
  - a = 69.675 Å  
  - b = 69.675 Å  
  - c = 100.197 Å  
  - α = β = γ = 90°

---

## Theoretical Background

Crystallographic symmetry operations are mathematically expressed as:

r′ = Rr + t


where:

- **r = (x, y, z)** represents the original atomic coordinates  
- **R** is a 3 × 3 rotation matrix  
- **t** is a translation vector  
- **r′** denotes the transformed coordinates  

Each symmetry operator defined in **REMARK 290** of the PDB file corresponds to a unique combination of **R** and **t**, defining the spatial relationship between symmetry-related molecules in the crystal lattice.

---

## Methodology

### 1. Data Acquisition
The legacy PDB file of the SARS Coronavirus Main Protease (2BX3) was obtained from the RCSB Protein Data Bank.

### 2. Identification of Symmetry Operators
Crystallographic symmetry operators were extracted from **REMARK 290** in the PDB file.  
**REMARK 350**, which describes BIOMT transformations for biological assemblies, was examined but excluded from the analysis, as it does not represent crystallographic symmetry.

### 3. Initial Structural Inspection
The asymmetric unit was visualized and oriented in PyMOL to establish a reference for subsequent symmetry expansion.

### 4. Application of Symmetry Operations
Python code was developed to apply the rotation matrices and translation vectors to the atomic coordinates. Execution of the script generated a new PDB file (`2BX3_lattice.pdb`) containing all symmetry-related molecules.

**Validation of Transformation:**

- Number of atoms in asymmetric unit: 2413  
- Number of symmetry operators: 8  
- Total atoms after transformation: 19304  

This confirms the successful application of all crystallographic symmetry operations.

### 5. Visualization of Crystal Packing
The transformed structure was loaded into PyMOL, and standard visualization commands were used to isolate, color, and orient each symmetry-related molecule. A PyMOL session file was saved for reproducibility and reference.

---

## Reproducibility and Usage

### Requirements
- Python 3.x
- Standard Python libraries (no external dependencies)
- PyMOL (for visualization)

### Running the Symmetry Transformation

1. Place `2BX3.pdb` and `2BX3_transformation.py` in the same directory.
2. Execute the script:
python 2BX3_transformation.py

3. The script generates:
- `2BX3_lattice.pdb` containing all symmetry-related molecules.

### Visualization
Open the generated PDB file in PyMOL and apply the visualization commands described in the Methodology section to reproduce the crystal packing.

---

## Results and Analysis

Application of the crystallographic symmetry operators generated a complete representation of the crystal lattice consistent with the space group **P 43 21 2**.

### Key Observations

- Eight symmetry-related copies of the asymmetric unit were generated, matching the expected number of crystallographic operators.
- Symmetry mates are related through rotations, screw-axis operations, and translational components characteristic of the space group.
- Intermolecular contacts observed within the lattice arise from crystallographic symmetry rather than biological oligomerization.
- Visualization confirmed regular packing along the crystallographic c-axis within the tetragonal unit cell.

---

## Limitations

- Only crystallographic symmetry operators explicitly listed in **REMARK 290** were considered.
- Thermal motion, solvent effects, and crystal disorder were not analyzed.
- The study focuses on geometric symmetry and does not evaluate energetic stability or intermolecular interaction strength.

---

## Skills Demonstrated

- Interpretation of crystallographic metadata from PDB files
- Application of matrix-based symmetry transformations
- Scientific Python programming for structural biology
- Molecular visualization and lattice analysis using PyMOL
- Clear distinction between crystallographic symmetry and biological assembly

---

## Data Source

The structural data used in this project were obtained from the RCSB Protein Data Bank:

- SARS Coronavirus Main Protease (PDB ID: 2BX3)

---

## Repository Contents

- `2BX3.pdb` – Original PDB file (asymmetric unit)  
- `2BX3_lattice.pdb` – Symmetry-expanded crystal lattice  
- `Final_transformed_structures.cif` – Final structures after visualization refinement  
- `2BX3_transformation.py` – Python script for symmetry transformations  
- `pymol_session_2BX3.pse` – PyMOL session file  
- `figures/` – Initial and final visualization images  
- `README.md` – Project documentation  

---

## References

- RCSB Protein Data Bank. https://www.rcsb.org  
- PyMOL Molecular Graphics System  
- International Tables for Crystallography
