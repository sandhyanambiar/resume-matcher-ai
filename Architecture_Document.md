# 🏗️ AI Resume Matcher – Architecture Document

---

## 1. 📌 System Architecture Overview

The system is a web-based application that analyzes resumes against job descriptions and provides a similarity score along with optional AI-generated feedback.

### 🔧 Components:

* **Frontend (UI):** HTML + Bootstrap
* **Backend API:** Flask (Python)
* **ML Engine:** TF-IDF + Cosine Similarity
* **Optional AI Layer:** LLaMA (via Ollama)
* **Containerization:** Docker
* **Deployment Target:** AWS (EC2 / ECS / Elastic Beanstalk)

---

## 2. 🧩 Architecture Diagram (Logical)

```
User (Browser)
      ↓
Frontend (HTML Form)
      ↓
Flask Backend (app.py)
      ↓
-----------------------------
| Resume Processing         |
| - PDF Text Extraction     |
| - Text Cleaning           |
-----------------------------
      ↓
-----------------------------
| ML Engine                 |
| - TF-IDF Vectorization    |
| - Cosine Similarity       |
-----------------------------
      ↓
(Optional)
-----------------------------
| LLM Layer (LLaMA via API) |
| - Feedback Generation     |
-----------------------------
      ↓
Response (Score + Feedback)
      ↓
Frontend Display
```

---

## 3. ⚙️ Technology Choices & Rationale

### 🐍 Backend: Python + Flask

* Lightweight and fast for prototyping
* Easy integration with ML libraries

---

### 🧠 ML Approach: TF-IDF + Cosine Similarity

* Fast and efficient
* Works well for keyword-based matching
* No heavy compute required → suitable for container deployment

---

### 🤖 LLM: LLaMA (via Ollama)

* Used for generating **explainable insights**
* Provides:

  * Strengths
  * Missing skills
  * Suggestions

**Why optional?**

* Large model size (2–4 GB)
* Not suitable for lightweight AWS deployment
* Designed as an enhancement layer

---

### 🐳 Containerization: Docker

* Ensures consistent environment
* Packages code + dependencies
* Makes deployment portable

---

### ☁️ Deployment: Amazon Web Services

Planned services:

* **EC2** → simple VM-based deployment
* **Elastic Beanstalk** → easy app deployment
* **ECS** → container orchestration (future scaling)

---

## 4. 🔄 Data Flow

### Step-by-step flow:

1. User uploads resume (PDF) and enters job description
2. Frontend sends request to Flask backend
3. Backend:

   * Extracts text from PDF
   * Cleans and preprocesses text
4. ML Engine:

   * Converts text to vectors using TF-IDF
   * Calculates similarity score
5. (Optional) LLM Layer:

   * Sends text to LLaMA API
   * Receives structured feedback
6. Backend returns:

   * Match score
   * AI feedback
7. Frontend displays results to user

---

## 5. 🧠 Key Design Decisions & Trade-offs

### ✅ Decision 1: Use TF-IDF instead of deep learning

**Why:**

* Fast
* Lightweight
* No GPU needed

**Trade-off:**

* Less semantic understanding compared to transformers

---

### ✅ Decision 2: Keep LLaMA as optional module

**Why:**

* Avoid heavy deployment
* Maintain AWS compatibility

**Trade-off:**

* Requires separate setup for full AI experience

---

### ✅ Decision 3: Docker-based deployment

**Why:**

* Ensures consistency across environments
* Simplifies AWS deployment

**Trade-off:**

* Slight learning curve

---

### ✅ Decision 4: Simple Flask architecture

**Why:**

* Faster development
* Easy debugging

**Trade-off:**

* Not ideal for large-scale systems

---

## 6. 🚀 Future Enhancements

* Replace TF-IDF with transformer-based embeddings
* Deploy LLM via API (OpenAI / hosted model)
* Add skill extraction and ranking
* Multi-resume comparison
* ATS-style scoring system

---

## 7. 🏁 Conclusion

This system is designed with a balance between:

* **Performance (TF-IDF)**
* **Scalability (Docker + AWS)**
* **Intelligence (Optional LLaMA integration)**

The architecture ensures:

* Lightweight deployment
* Extensibility for advanced AI features
* Real-world applicability

---
