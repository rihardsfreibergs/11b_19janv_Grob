# 2. Uzdevums: Izveidot Python programmu, kas nolasītu un izdrukātu tikai otrās kolonnas datus no CSV faila. (3 punkti)

import csv

def lasit_otro_kolonnu(csv_fails):
    try:
        with open(csv_fails, 'r', newline='') as fails:
            lasitajs = csv.reader(fails)
            
            next(lasitajs)
            
            print("Otrās kolonnas dati:")
            for rinda in lasitajs:
                if len(rinda) >= 2:
                    otra_kolonna_dati = rinda[1]
                    print(otra_kolonna_dati)
    except FileNotFoundError:
        print(f"Kļūda: fails ar nosaukumu '{csv_fails}' nav atrasts.")
    except Exception as e:
        print(f"Kļūda: {e}")


lasit_otro_kolonnu('fails.csv')
