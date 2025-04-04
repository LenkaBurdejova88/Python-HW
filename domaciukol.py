import json

slovnik = dict()

with open("alice.txt", mode="r", encoding="utf-8") as file:
    for radek in file:
        radek = radek.lower()
        radek = radek.strip().replace(" ", "")

        for znak in radek:
            if znak in slovnik:
                slovnik[znak] += 1
            else:
                slovnik[znak] = 1


serazeny_slovnik = dict()
for klic in sorted(slovnik):
    serazeny_slovnik[klic] = slovnik[klic]

with open("hw_01_output_Burdejova.json", "w", encoding="utf-8") as vystup:
    json.dump(serazeny_slovnik, vystup, indent=4, ensure_ascii=False)