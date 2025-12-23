# Engagement Level Prediction Project 🎮

Bu proje, oyuncuların çevrimiçi oyunlardaki davranış verilerini kullanarak **Engagement Level (Bağlılık Seviyesi)** tahmini yapmayı amaçlayan bir makine öğrenmesi uygulamasıdır.

## 📌 Proje Özeti
- **Veri Seti:** 40,034 oyuncunun davranış verileri (Yaş, Oyun Süresi, Satın Alma vb.)
- **Kaynak:** [Predict Online Gaming Behavior Dataset](https://www.kaggle.com/datasets/rabieelkharoua/predict-online-gaming-behavior-dataset?resource=download)
- **Hedef:** Oyuncunun bağlılığını `Low`, `Medium` veya `High` olarak sınıflandırmak.
- **Model:** Random Forest Classifier
- **Başarı Oranı:** %91 Doğruluk (Accuracy)

## 📂 Dosya Yapısı
- `train_model.py`: Veri işleme, model eğitimi ve raporlama yapan ana kod.
- `inspect_data.py`: Veri setini analiz etmek için kullanılan yardımcı kod.
- `generate_pdf.py`: Analiz sonuçlarını PDF raporuna dönüştüren kod.
- `online_gaming_behavior_dataset.csv`: Kullanılan veri seti.
- `Engagement_Analysis_Report.pdf`: Sonuçların yer aldığı detaylı PDF raporu.

## 🚀 Kurulum ve Çalıştırma

### Gereksinimler
Kodları çalıştırmak için Python yüklü olmalıdır. Gerekli kütüphaneleri yüklemek için:

```bash
pip install pandas scikit-learn matplotlib seaborn fpdf
```

### Modeli Eğitme ve Sonuç Alma
Analizi başlatmak ve sonuçları üretmek için terminalde şu komutu çalıştırın:

```bash
python train_model.py
```
Bu işlem sonucunda `model_performance_report.txt` ve grafik dosyaları oluşacaktır.

### PDF Raporu Oluşturma
Sonuçları tek bir dosyada toplamak için:

```bash
python generate_pdf.py
```

## 📊 Sonuçlar
Modelimiz aşağıdaki özellikleri kullanarak tahmin yapmaktadır:
1. **SessionsPerWeek**: Haftalık oturum sayısı (En etkili özellik)
2. **Age**: Oyuncu yaşı
3. **PlayTimeHours**: Toplam oyun süresi
4. **PlayerLevel**: Oyuncu seviyesi
5. **AvgSessionDurationMinutes**: Ortalama oturum süresi

**Detaylı analiz için `Engagement_Analysis_Report.pdf` dosyasına göz atabilirsiniz.**

---
*Bu proje İstanbul Ticaret Üniversitesi-BIL460 Veri Tabanı dersinin projesi kapsamında hazırlanmıştır.*
