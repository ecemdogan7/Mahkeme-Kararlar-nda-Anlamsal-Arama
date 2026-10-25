# Mahkeme_kararlarinda_anlamsal_arama
Türkçe mahkeme kararlarında anlamsal arama | Semantic search over Turkish court decisions (legal tech)

Bu proje, Türkçe mahkeme kararları üzerinde anlamsal arama yapan basit bir legal tech prototipidir. Kullanıcı sorusunu günlük dille yazar; sistem, soruyla anlamca en çok örtüşen kararları benzerlik puanıyla birlikte listeler.

Klasik kelime aramasından farkı: Soruda geçen kelimeler kararda birebir geçmese bile ilgili kararı bulabilir. Örneğin "kiracı kirayı ödemedi" diye sorulduğunda, "kira bedelinin ödenmemesi" ifadesini içeren karar da eşleşir.

Nasıl çalışır?
kararlar/ klasöründeki .txt karar metinleri okunur.
Her karar, çok dilli bir embedding modeliyle (paraphrase-multilingual-MiniLM-L12-v2) anlamını temsil eden bir vektöre çevrilir.
Kullanıcının sorusu da aynı modelle vektöre çevrilir.
Soru vektörü ile her karar vektörü arasındaki kosinüs benzerliği hesaplanır.
En yüksek puanlı 3 karar, dosya adı ve benzerlik puanıyla gösterilir.
Kullanılan teknolojiler
Python 3.11
sentence-transformers
Kurulum
bash
python3 -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt
Kullanım

Karar metinlerini .txt dosyaları olarak kararlar/ klasörüne koyun, ardından:

bash
python main.py

İlk çalıştırmada model (~470 MB) indirilir. Program her sorudan sonra yeni soru bekler; çıkmak için q yazın.

Örnek çıktı
Sorunuz (çıkmak için q): kira sözleşmesinde depozito
karar1.txt  (benzerlik: 0.48)
karar.txt  (benzerlik: 0.44)
karar2.txt  (benzerlik: 0.39)
