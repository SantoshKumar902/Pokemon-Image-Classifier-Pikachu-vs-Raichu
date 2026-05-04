# ⚡ Pokemon Image Classifier: Pikachu vs Raichu

A Convolutional Neural Network (CNN) that classifies Pokemon images as **Pikachu**, **Raichu**, or **Unknown**. Built with TensorFlow/Keras and deployed live on Hugging Face Spaces.

🚀 **[Try the Live Demo](https://huggingface.co/spaces/SantoshKumar21/Pokemon_Image_Classifier)**

---

## 🆕 What's New in v2
- Added **3rd class (Other/Unknown)** — non-Pokemon images are now detected
- Upgraded from binary classification to **multi-class classification**
- Improved model robustness with out-of-distribution detection
- Deployed live with interactive **Gradio UI**

---

## 🛠️ Tech Stack
- Python
- TensorFlow / Keras
- NumPy, Pillow
- Gradio (deployment)
- Hugging Face Spaces

---

## 🧾 Dataset
- **Pikachu:** ~25 training images, ~5 test images
- **Raichu:** ~25 training images, ~5 test images
- **Other:** 55 training images, 15 test images (Cat, Elephant, Horse)
  - Other class sourced from [Animals-10 Dataset](https://www.kaggle.com/datasets/alessiocorrado99/animals10)

---

## 📂 Project Structure
```
├── Pokemon_Prediction_Project.ipynb  — Training notebook
├── pokemon_model.h5                  — Trained CNN model
├── app.py                            — Gradio app for deployment
└── requirements.txt                  — Dependencies
```

---

## 🚀 Model Pipeline
1. Preprocess images (resize to 64x64, normalize)
2. Build CNN — 2 Conv layers + MaxPooling + Dense layers
3. Train with `categorical_crossentropy` (3 classes)
4. Evaluate on test set
5. Deploy with Gradio on Hugging Face Spaces

---

## 🧠 Model Architecture
```
Input (64x64x3)
→ Conv2D (32 filters) + MaxPooling
→ Conv2D (32 filters) + MaxPooling
→ Flatten
→ Dense (128, ReLU)
→ Dense (3, Softmax)   ← Pikachu / Raichu / Other
```

---

## 📊 Results
| Class | Prediction |
|-------|-----------|
| Pikachu image | ⚡ Pikachu! |
| Raichu image | ⚡ Raichu! |
| Random/Unknown image | ⚠️ Unknown Image |

> **Note:** Model works best with cartoon-style Pokemon images. Unknown detection may vary for highly ambiguous inputs.

---

## ▶️ Run Locally
```bash
pip install -r requirements.txt
python app.py
```

---

## 📩 Connect with Me
- 📧 Email: santoshkumar729629@gmail.com
- 💼 LinkedIn: [linkedin.com/in/santosh-kumar-sk](https://www.linkedin.com/in/santosh-kumar-sk)
- 🐙 GitHub: [github.com/SantoshKumar902](https://github.com/SantoshKumar902)
