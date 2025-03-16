# ✋ Hand Gesture Recognition using OpenCV & SVM  

This project is a **Machine Learning-based Hand Gesture Recognition System** that detects and classifies hand gestures in real-time using **OpenCV & Support Vector Machine (SVM)**.

## 📌 Features  
- 🚀 **Real-time Gesture Recognition** using a webcam 🎥  
- 🎯 **Uses OpenCV** for image preprocessing 🎦  
- 🤖 **Machine Learning (SVM) for classification**  
- 🔥 **Expandable** for gesture-based control (IoT, Media, Automation)  

---

## 🛠️ Installation & Running the Project  

### 🔹 Clone the Repository  
```sh
git clone https://github.com/your-username/gesture-recognition.git
cd gesture-recognition
```

### 🔹 Install Dependencies  
```sh
pip install opencv-python numpy scikit-learn joblib tqdm
```

### 🔹 Train the Model  
```sh
python train.py
```
- This will train the model and save it as `gesture_svm_model.pkl`.

### 🔹 Run Gesture Recognition  
```sh
python gesture_recognition.py
```
- The webcam will open & recognize hand gestures.  
- Press **'q'** to exit.

---

## 📂 Project Structure  

| Folder/File                | Description |
|----------------------------|-------------|
| `dataset/`                 | Gesture dataset (LeapGestRecog - Not included) |
| `models/`                  | Contains trained models |
| ├── `gesture_svm_model.pkl` | SVM model for gesture classification |
| ├── `label_encoder.pkl`     | Encodes gesture labels |
| `scripts/`                 | Contains Python scripts |
| ├── `train.py`              | Trains the SVM model |
| ├── `gesture_recognition.py` | Real-time gesture detection |
| ├── `data_preprocessing.py` | Checks & prepares dataset |
| ├── `check.py`              | Verifies dataset structure |
| ├── `count.py`              | Counts images per gesture |
| ├── `visualize.py`          | Displays sample images |
| `README.md`                | Project Documentation |

---

## 📊 Model Performance  
| Metric        | Score |
|--------------|-------|
| **Accuracy**  | 98%  |
| **Training Time** | 1 min |
| **Model Used** | SVM |

📌 **Want better accuracy?** Try switching to **CNN (Deep Learning).** 🎯  

---

## 🎮 Future Enhancements  
| Feature | Description |
|---------|------------|
| ✅ Gesture-based media control | Play/Pause, Volume Up/Down |
| ✅ IoT integration | Turn lights on/off with gestures |
| ✅ Mouse control | Move & click using hand gestures |

---

## 🐜 License  
This project is open-source and available under the **MIT License**.  

---

### Made with ❤️ by [Srijoy Mitra](https://github.com/srijoymitra) 🚀  

