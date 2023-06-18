def generiraj_parni_neparni(parametar):
    for broj in range(parametar):
        if broj % 2 == 0:
            yield broj, 'paran'
        else:
            yield broj, 'neparan'
for broj, parnost in generiraj_parni_neparni(10):
    print(f"Broj {broj} je {parnost}.")
