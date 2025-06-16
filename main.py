from src.utils import load_data, plot_metrics, save_report
from tensorflow.keras import layers, models
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix
import numpy as np
import os

# ✅ TO‘G‘RI YO‘L: Dataset papkasi — cell_images/
data = load_data("cell_images")

# Preprocessing
X, y = zip(*data)
X = np.array(X) / 255.0  # Normalize
y = np.array(y)

# Train/test ajratish
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, stratify=y, random_state=42)

# CNN model
model = models.Sequential([
    layers.Conv2D(32, (3,3), activation='relu', input_shape=(128, 128, 3)),
    layers.MaxPooling2D(2,2),
    layers.Conv2D(64, (3,3), activation='relu'),
    layers.MaxPooling2D(2,2),
    layers.Conv2D(128, (3,3), activation='relu'),
    layers.MaxPooling2D(2,2),
    layers.Flatten(),
    layers.Dense(128, activation='relu'),
    layers.Dense(1, activation='sigmoid')  # Binary classification
])

model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# O‘qitish
history = model.fit(X_train, y_train, epochs=10, validation_data=(X_test, y_test), batch_size=32)

# Modelni saqlash
if not os.path.exists("models"):
    os.makedirs("models")
model.save("models/malaria_cnn_model.h5")

# Baholash
y_pred = (model.predict(X_test) > 0.5).astype("int32")
report = classification_report(y_test, y_pred)
matrix = confusion_matrix(y_test, y_pred)

# Report yozish
if not os.path.exists("results"):
    os.makedirs("results")
save_report(report, matrix, "results/report.txt")

# Grafik chizish
plot_metrics(history, "results")
