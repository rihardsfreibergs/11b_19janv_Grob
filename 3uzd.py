# 3. Uzdevums: Izveidot Python programmu, kas nolasītu un izdrukātu trešās teksta faila rindas saturu. (3 punkti)

def lasit_un_drukat(faila_nosaukums):
    try:
        with open(faila_nosaukums, 'r') as fails:
            rindas = fails.readlines()
            if len(rindas) >= 3:
                tresa_rinda = rindas[2]
                print("Trešās rindas saturs:")
                print(tresa_rinda)
            else:
                print("Kļūda: Fails nav pietiekami garš, vai arī tam nav trešā rinda.")
    except FileNotFoundError:
        print(f"Kļūda: fails ar nosaukumu '{faila_nosaukums}' nav atrasts.")
    except Exception as e:
        print(f"Kļūda: {e}")


lasit_un_drukat('3uzdteksts.txt')
