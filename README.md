# 🎯 GapHunter

**GapHunter**, dijital varlığı olmayan işletmeleri tespit etmek için tasarlanmış profesyonel bir otomasyon aracıdır. Google Maps API'sini (Serper.dev aracılığıyla) kullanarak, belirli sektörlerdeki ve konumlardaki yerel işletmeleri keşfeder, web sitesi olmayanları filtreler ve yerel etkilerine (yorum sayısı) göre sıralar.

Bu araç; girişimciler, dijital ajanslar ve yerel işletmeler için "dijital boşluğu" kapatmak isteyen serbest çalışanlar (freelancer) için geliştirilmiştir.

---

## 🚀 Özellikler

- **Otomatik Keşif**: Herhangi bir sektör ve konumda yüzlerce işletmeyi tarayın.
- **Akıllı Filtreleme**: Web sitesi listelenmemiş olan işletmeleri otomatik olarak tespit eder.
- **Potansiyel Müşteri Skorlama**: Yüksek etkili hedeflere öncelik vermenize yardımcı olmak için potansiyel müşterileri yorum sayılarına göre sıralar.
- **Excel Uyumlu Dışa Aktarma**: Sonuçları Microsoft Excel için yapılandırılmış CSV dosyalarına kaydeder.
- **Teknik Borçsuz**: Loglama, tip ipuçları (type hints) ve sağlam hata yönetimi ile modüler mimari.

---

## 🛠️ Kurulum

### 1. Repoyu Klonlayın

```bash
git clone https://github.com/Ali-bot-prog/GapHunter.git
cd GapHunter
```

### 2. Bağımlılıkları Yükleyin

```bash
pip install -r requirements.txt
```

### 3. Yapılandırma

Kök dizinde bir `.env` dosyası oluşturun ve Serper.dev API anahtarınızı ekleyin:

```env
MAPS_API_KEY=your_serper_api_key_here
```

*Ücretsiz API anahtarınızı [serper.dev](https://serper.dev) adresinden alabilirsiniz.*

---

## 📖 Kullanım

Otomasyonu tek bir komutla çalıştırın:

```bash
python main.py
```

### Özelleştirme

Hedef sektörü ve konumu `main.py` dosyasından değiştirebilirsiniz:

```python
SECTOR = "restoran"
LOCATION = "Ünye"
TARGET_COUNT = 50
```

---

## 📂 Proje Yapısı

- `main.py`: Otomasyonun giriş noktası.
- `scraper.py`: Serper/Google Maps API ile etkileşim kuran çekirdek mantık.
- `processor.py`: Veri filtreleme, sıralama ve dışa aktarma mantığı.
- `reports/`: (Otomatik oluşturulur) CSV sonuçlarının kaydedildiği dizin.
- `.gitignore`: `.env` gibi hassas dosyaların GitHub'a yüklenmemesini sağlar.

---

## 🤝 Katkıda Bulunma

GapHunter geliştirilmeye açık bir projedir! Her türlü katkıya (Pull Request) ve yeni fikre açığız. Özellikle şu alanlarda yardıma ihtiyacımız var:

- 🤖 **AI Enhancements**: İşletme büyüklüğünü daha hassas ölçen yeni algoritmalar.
- 📧 **Automation**: Filtrelenen işletmelere özel teklif sunan otomatik mail modülleri.
- 🌐 **Dashboard**: Verilerin izlenebileceği basit bir web arayüzü.

### Nasıl Katkı Sağlarsınız?

1. Repoyu fork'layın.
2. Yeni bir özellik için branch oluşturun (`git checkout -b feature/AmazingFeature`).
3. Değişikliklerinizi commit edin (`git commit -m 'Add: AmazingFeature'`).
4. Branch'inizi push edin (`git push origin feature/AmazingFeature`).
5. Bir Pull Request açın.

---

## 🛡️ Lisans ve Telif Hakkı

Bu proje açık kaynaklıdır. Ancak, uygulama ve mantık yüksek performanslı potansiyel müşteri oluşturma için optimize edilmiştir.

**© 2026 OmNexus. Tüm Hakları Saklıdır.**
