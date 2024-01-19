# 1. Uzdevums: Izveidot Python programmu, kas nolasītu un izdrukātu visu teksta faila saturu (txt formātā). (3 punkti)

def LasaUnDruka(faila_nosaukums):
    try:
        with open(faila_nosaukums, 'r') as fails:
            saturs = fails.read()
            print("Faila saturs:")
            print(saturs)
    except FileNotFoundError:
        print(f"Kļūda: fails ar nosaukumu '{faila_nosaukums}' nav atrasts.")
    except Exception as e:
        print(f"Kļūda: {e}")

LasaUnDruka('dokuments.txt')
