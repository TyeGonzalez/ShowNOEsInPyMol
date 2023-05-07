import pymol
from pymol import cmd


def draw_noe_lines(noe_data_file='unambig.tbl'):
    with open(noe_data_file, 'r') as noe_file:
        noe_data = noe_file.readlines()

    for line in noe_data:
        if line.startswith("assign"):
            print(line)
            tokens = line.split()
            atom1 = " ".join(tokens[1:6])
            atom2 = " ".join(tokens[6:11])
            # replace "#" character with * to avoid pymol error
            atom1 = atom1.replace("#", "*")
            atom2 = atom2.replace("#", "*")
            print(tokens[1:11])
            print(atom1)
            print(atom2)
            cmd.distance(
                f"{tokens[2]}{tokens[5]}-{tokens[7]}{tokens[10]}", atom1, atom2, mode=0)


cmd.extend("draw_noe_lines", draw_noe_lines)
