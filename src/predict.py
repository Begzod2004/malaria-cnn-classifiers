import cv2
import numpy as np
from tensorflow.keras.models import load_model

model = load_model("models/malaria_cnn_model.h5")

def predict_image(image_path):
    img = cv2.imread(image_path)
    img = cv2.resize(img, (128, 128))
    img = img / 255.0
    img = np.expand_dims(img, axis=0)
    prediction = model.predict(img)[0][0]
    return "🦠 Parasitized" if prediction > 0.5 else "✅ Uninfected"
