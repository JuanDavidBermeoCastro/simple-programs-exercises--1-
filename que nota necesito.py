certamenFirst = float(input("Enter contest grade 1: "))
certamenSecond = float(input("Enter contest note 2: "))
gradeLaboratory = float(input("ENTER nota laboratorio: "))
NF_requerida = 60
NC_requerida = (NF_requerida - gradeLaboratory * 0.3) / 0.7
C3_necesaria = NC_requerida * 3 - certamenFirst - certamenSecond
print(f"NEED nota {C3_necesaria:.2f} in the contest3")
