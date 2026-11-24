# 🍵 Matcha Avı — Gabar Dağları Efsanesi

Dokunmatik tahtalar için tasarlanmış, Streamlit içinde çalışan 12 bölümlük hikayeli arcade oyunu (Gabar Dağları + Nevada).
Kurt matchaları toplar, prensesi kurtarır, absürt rakiplerden kaçar.

## Kontroller
- **Dokunmatik / fare:** ekrana bas ve sürükle (sanal joystick), sağ alttaki 🍵 düğmesi ile matcha içip enerji kazan (toplanan matchalar stok olur).
- Klavye: WASD veya ok tuşları ile hareket, **E** (veya boşluk) ile matcha içip enerji kazanma, P = duraklat.

## Yerelde çalıştırma
```
pip install -r requirements.txt
streamlit run app.py
```

## Yayınlama (Streamlit Community Cloud)
1. Bu klasörü GitHub'a yükle (`app.py`, `game.html`, `requirements.txt`, `.streamlit/`).
2. share.streamlit.io → New app → depo ve `app.py` seç → Deploy.

Not: Tüm karakterler kurgusal parodidir.

## Çevrimiçi co-op (oda kodu)
Menü → "ÇEVRİMİÇİ CO-OP". Biri "ODA KUR" der ve ekrandaki 4 haneli kodu söyler, öteki "ODAYA GİR" ile kodu yazar.
Oyunu oda kurucunun tarayıcısı çalıştırır, öteki oyuncu tuşlarını gönderir. Eşleştirme için ücretsiz PeerJS bulut sunucusu kullanılır,
bu yüzden `peerjs.min.js` dosyası `app.py` ile aynı klasörde durmalıdır. Okul ağı WebRTC bağlantısını engelliyorsa bağlantı kurulamayabilir.
