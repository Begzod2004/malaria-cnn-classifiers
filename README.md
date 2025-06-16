# 🦠 Malaria Cell Classification with CNN

Bu loyiha Convolutional Neural Network (CNN) yordamida hujayra tasvirlarida **malaria paraziti bor-yo‘qligini** aniqlashga qaratilgan. Loyihada sizga quyidagi imkoniyatlar taqdim etiladi:

- Tasvirlarni yuklab, avtomatik tozalash va tayyorlash
- CNN modeli yaratish va o‘qitish
- Modelni test qilish va aniqlik (accuracy) baholash
- Natijalarni vizual ko‘rish
- Parazitlangan va sog‘lom hujayralar o‘rtasidagi farqlarni ajratish

---

## 📂 Loyiha Tuzilmasi

```bash
malaria-cnn-classifier/
├── cell_images/              # Dataset (Parasitized va Uninfected)
├── malaria_cnn.ipynb         # Asosiy kod va model
├── models/
│   └── malaria_model.h5      # Trained model (CNN)
├── utils/
│   └── load_data.py          # Datasetni yuklovchi va tayyorlovchi skript
├── images/
│   ├── example_parasitized.png
│   ├── example_uninfected.png
│   └── result_accuracy.png   # Model accuracy grafik natijasi
└── README.md                 # Loyiha hujjati

🦠 Parazitlangan (Parasitized)
![image](https://github.com/user-attachments/assets/d06fa09b-c1f6-450f-9a3d-bbf3c2137761)



✅ Sog‘lom (Uninfected)
![image](https://github.com/user-attachments/assets/6e1c75c4-7561-4131-b864-a0fc2ce3f6a5)


oxirgi natija:

![image](https://github.com/user-attachments/assets/3e59f1f2-8c61-4f9c-b2ea-39bc3b40228b)


Classification Report:
              precision    recall  f1-score   support

           0       0.94      0.95      0.95      2756
           1       0.95      0.94      0.95      2756

    accuracy                           0.95      5512
   macro avg       0.95      0.95      0.95      5512
weighted avg       0.95      0.95      0.95      5512

Confusion Matrix:
[[2627  129]
 [ 168 2588]]
