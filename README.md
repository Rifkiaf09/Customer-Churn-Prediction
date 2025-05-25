# Telco Customer Churn Prediction

Proyek sederhana ini mempunyai tujuan untuk memprediksi apakah pelanggan akan berhenti berlangganan dari layanan telekomunikasi berdasarkan data historis pelanggan. Model ini dapat digunakan untuk membantu tim retensi untuk mengambil tindakan sebelum pelanggan benar-benar berhenti berlangganan.

## 📦 Dataset

Dataset yang digunakan yaitu **Telco Customer Churn** yang bersumber dari dataset Kaggle:  
https://www.kaggle.com/blastchar/telco-customer-churn

- Jumlah entri: 7043 pelanggan
- Target: `Churn` (Yes/No)
- Fitur mencakup: demografi, layanan yang digunakan, kontrak, pembayaran, dll.

## ⚙️ Metodologi

1. Data Preprocessing:
   - Handle missing values
   - Encoding fitur kategorikal
   - SMOTE untuk balancing data

2. Modeling:
   - Menggunakan **XGBoost Classifier**
   - Hyperparameter tuning via `RandomizedSearchCV`

3. Evaluasi:
   - Akurasi: **83.4%**
   - F1-score: **83%**
   - ROC AUC Score: **83.4%**

## 📊 Hasil Evaluasi

| Metrik     | Nilai   |
|------------|---------|
| Accuracy   | 0.834   |
| F1-Score   | 0.83    |
| ROC AUC    | 0.834   |

### Confusion Matrix
![Confusion Matrix](images/confusion_matrix.png)

## 🔍 Insight Bisnis

- **84% pelanggan churn berhasil diprediksi** → Dapat untuk membantu tim marketing agar bisa melakukan retensi lebih awal.
- Fitur penting yang berkontribusi terhadap churn:
  - Lama kontrak (contract)
  - Jenis pembayaran
  - Layanan seperti tech support dan online security
- **Pelanggan dengan kontrak bulanan & pembayaran elektronik lebih cenderung churn.**

## 🚀 Tools & Library
- Python, Pandas, Scikit-learn, XGBoost, imbalanced-learn
- Matplotlib, Seaborn
- Streamlit (untuk deployment)

## 💻 Streamlit Deployment

Kami menyediakan antarmuka sederhana untuk memprediksi churn pelanggan berbasis input manual.  
Run dengan:

```bash
streamlit run app.py
```

---
