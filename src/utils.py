import os
import cv2
import matplotlib.pyplot as plt
from sklearn.metrics import ConfusionMatrixDisplay

def load_data(data_dir):
    categories = ['Parasitized', 'Uninfected']
    data = []
    for category in categories:
        path = os.path.join(data_dir, category)
        label = 1 if category == "Parasitized" else 0
        for img_name in os.listdir(path):
            img_path = os.path.join(path, img_name)
            try:
                img = cv2.imread(img_path)
                img = cv2.resize(img, (128, 128))
                data.append((img, label))
            except:
                continue
    return data

def plot_metrics(history, save_dir):
    plt.figure(figsize=(12, 5))

    plt.subplot(1, 2, 1)
    plt.plot(history.history['accuracy'], label="Train Acc")
    plt.plot(history.history['val_accuracy'], label="Val Acc")
    plt.title("Accuracy")
    plt.legend()

    plt.subplot(1, 2, 2)
    plt.plot(history.history['loss'], label="Train Loss")
    plt.plot(history.history['val_loss'], label="Val Loss")
    plt.title("Loss")
    plt.legend()

    plt.tight_layout()
    plt.savefig(os.path.join(save_dir, "metrics.png"))

def save_report(report, matrix, file_path):
    with open(file_path, "w") as f:
        f.write("Classification Report:\n")
        f.write(report)
        f.write("\nConfusion Matrix:\n")
        f.write(str(matrix))
