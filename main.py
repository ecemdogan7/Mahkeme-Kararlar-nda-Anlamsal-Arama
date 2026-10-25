from pathlib import Path
from sentence_transformers import SentenceTransformer, util

dosyalar = sorted(Path("kararlar").glob("*.txt"))
kararlar = [d.read_text(encoding="utf-8") for d in dosyalar]

model = SentenceTransformer("paraphrase-multilingual-MiniLM-L12-v2")
karar_vektorleri = model.encode(kararlar)

while True:
    soru = input("\nSorunuz (çıkmak için q): ")
    if soru == "q":
        break
    skorlar = util.cos_sim(model.encode(soru), karar_vektorleri)[0]
    for i in skorlar.argsort(descending=True)[:3]:
        print(f"{dosyalar[i].name}  (benzerlik: {skorlar[i]:.2f})")