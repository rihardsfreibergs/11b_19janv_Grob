# 4. Uzdevums: Izveidot Python programmu, kur lietotājs ievada gan faila nosaukumu, 
# gan faila formātu (paplašinājumu), un atkarībā no faila paplašinājuma tiek nolasīts faila saturs.
# Nolasītā informācija ir jāizdrukā terminālī. Ievērot iespejamās kļūdas! (8 punkti)

def lasit_un_drukat_failu(nosaukums, paplasinajums):
    try:
        faila_nosaukums = f"{nosaukums}.{paplasinajums}"
        with open(faila_nosaukums, 'r') as fails:
            saturs = fails.read()
            print(f"Faila saturs ({paplasinajums}):")
            print(saturs)
    except FileNotFoundError:
        print(f"Kļūda: fails ar nosaukumu '{faila_nosaukums}' nav atrasts.")
    except Exception as e:
        print(f"Kļūda: {e}")

if __name__ == "__main__":
    nosaukums = input("Ievadiet faila nosaukumu (bez faila paplašinājuma): ")
    paplasinajums = input("Ievadiet faila paplašinājumu (piemēram, 'txt'): ")

    lasit_un_drukat_failu(nosaukums, paplasinajums)
    
