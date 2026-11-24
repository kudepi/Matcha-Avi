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
Oyunu oda kurucunun tarayıcısı çalıştırır, öteki oyuncu tuşlarını gönderir. Cihaz/marka fark etmez (Mac, Windows, telefon, tablet).
Bağlantı önce WebRTC (PeerJS, `peerjs.min.js` `app.py` ile aynı klasörde olmalı) ile denenir; ~3 sn içinde kurulamazsa
otomatik olarak yedek hatta (halka açık MQTT sunucuları üzerinden WebSocket) geçilir. Yedek hat biraz daha gecikmeli olabilir ve
halka açık olduğu için oda kodunu sadece arkadaşınla paylaş. Okul ağı her iki yolu da engelliyorsa bağlantı kurulamaz.

## Yenilikler
- Büyük harita (1600×1000) + kamera takibi + mini harita
- Yeni rakipler: Dolmuş Şoförü (kırmızı şeritte hasar), Kargo Kuryesi (patlayan paketler), Hırsız Kedi (matcha çalar, yakalarsan geri verir), Poşet Teyze (giden-gelen poşet)
- Matcha enerjisi zamanla azalır (yaklaşık 6 sn); ne kadar enerji varsa o kadar hız ve mıknatıs
https://matcha-avi.streamlit.app/
