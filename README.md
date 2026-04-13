# 🤖 AI Resume Matcher

An AI-powered web application that analyzes and matches resumes with job descriptions using Natural Language Processing (NLP) and Machine Learning.

---

## 🚀 Features

* 📄 Upload Resume (PDF)
* 📝 Paste Job Description
* 🧠 NLP-based text processing
* 📊 Similarity score calculation
* ⚡ Fast and simple Flask-based UI

---

## 🛠️ Tech Stack

* **Backend:** Flask (Python)
* **Machine Learning:** Scikit-learn
* **Data Processing:** Pandas, NumPy
* **NLP:** TF-IDF Vectorization
* **Frontend:** HTML, Bootstrap
* **File Handling:** PyPDF2

---

## 📂 Project Structure

```
resume-matcher-ai/
│
├── app.py
├── requirements.txt
├── model/
│   └── model.pkl (if applicable)
├── templates/
│   └── index.html
├── static/
│
└── README.md
```

---

## ⚙️ Installation & Setup

### 1. Clone the repository

```
git clone https://github.com/your-username/resume-matcher-ai.git
cd resume-matcher-ai
```

### 2. Create virtual environment

```
python -m venv testenv
```

### 3. Activate environment

**Windows:**

```
testenv\Scripts\activate
```

**Mac/Linux:**

```
source testenv/bin/activate
```

### 4. Install dependencies

```
pip install -r requirements.txt
```

### 5. Run the application

```
python app.py
```

---

## 🌐 Usage

1. Upload a resume (PDF format)
2. Enter or paste the job description
3. Click on **Analyze**
4. View the matching score and insights

---

## 🧠 How It Works

* Extracts text from resume PDF
* Cleans and preprocesses text
* Converts text into numerical vectors using **TF-IDF**
* Computes similarity between resume and job description
* Outputs a matching score

---

## 📈 Future Improvements

* Use advanced models (BERT / Transformers)
* Add skill extraction
* Improve UI/UX
* Support multiple resumes comparison
* Deploy on AWS

---

## 🤝 Acknowledgment

This project was developed with the help of AI tools like ChatGPT to accelerate development, debugging, and implementation.

---

## 📬 Contact

For any queries or suggestions, feel free to connect.

---
