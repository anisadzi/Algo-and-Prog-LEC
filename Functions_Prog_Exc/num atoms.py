def num_atoms(gr, at = 196.97) :
    mole = gr / at
    atoms = mole * (6.022*(10**23))

    print(atoms)
    return atoms

num_atoms(10)
num_atoms(10, 12.001)
num_atoms(10,1.008)