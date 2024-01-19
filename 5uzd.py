# 5. Uzdevums: Izveidot Python programmu, kas ļauj lietotājam ievadīt savu vārdu terminālī.
# Ievadīto vārdu pēc tam ierakstīt teksta failā (piemēram, "lietotajs.txt").
# Programmai jābūt spējīgai apstrādāt kļūdas, piemēram, faila nepieejamību vai rakstīšanas problēmas.
# Pēc ierakstīšanas izvadīt paziņojumu par veiksmīgu darbību vai kļūdu gadījumā attiecīgu kļūdas ziņojumu. (8 punkti)

def vardsfaila(vards):
    faila_nosaukums = "lietotajs.txt"
    
    try:
        with open(faila_nosaukums, 'a') as fails:
            fails.write(vards + "\n")
        print(f"Vārds '{vards}' tika ierakstīts failā '{faila_nosaukums}'.")
    except FileNotFoundError:
        print(f"Kļūda: fails '{faila_nosaukums}' nav atrasts.")
    except Exception as e:
        print(f"Kļūda: {e}")

if __name__ == "__main__":
    vards = input("Ievadiet savu vārdu: ")

    vardsfaila(vards)
