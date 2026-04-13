from flask import Flask, render_template, request
import docx
import PyPDF2
import re

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

app = Flask(__name__)


# -------------------------------
# TEXT EXTRACTION
# -------------------------------
def extract_text(file):
    text = ""

    if file.filename.endswith(".pdf"):
        reader = PyPDF2.PdfReader(file)
        for page in reader.pages:
            text += page.extract_text() or ""

    elif file.filename.endswith(".docx"):
        doc = docx.Document(file)
        for para in doc.paragraphs:
            text += para.text + "\n"

    return text.lower()


def clean_text(text):
    return re.sub(r'[^a-zA-Z0-9\s]', '', text)


# -------------------------------
# SKILLS
# -------------------------------
def extract_skills(jd_text):
    skills = [
        "python", "java", "sql", "mysql", "postgresql",
        "api", "flask", "django", "aws", "docker"
    ]
    return [s for s in skills if s in jd_text]


# -------------------------------
# TF-IDF SCORE
# -------------------------------
def tfidf_score(resume, jd):
    vectorizer = TfidfVectorizer()
    vectors = vectorizer.fit_transform([resume, jd])
    score = cosine_similarity(vectors[0:1], vectors[1:2])[0][0]
    return score * 100


# -------------------------------
# WEIGHTED SCORE
# -------------------------------
def weighted_score(resume, jd_skills):
    weights = {
        "python": 3,
        "java": 3,
        "postgresql": 3,
        "mysql": 2,
        "sql": 2,
        "api": 2,
        "flask": 2,
        "django": 2,
        "aws": 2,
        "docker": 1
    }

    total = 0
    matched = 0
    breakdown = []
    missing = []
    rationale = []

    for skill in jd_skills:
        w = weights.get(skill, 1)
        total += w

        if skill in resume:
            matched += w
            status = "Met"
            rationale.append(f"{skill} found in resume.")
        else:
            status = "Not Met"
            missing.append(skill)
            rationale.append(f"{skill} missing from resume.")

        breakdown.append({"skill": skill, "status": status})

    score = (matched / total) * 100 if total else 0

    return score, breakdown, missing, rationale


# -------------------------------
# HYBRID SCORE
# -------------------------------
def hybrid_score(resume, jd):
    jd_skills = extract_skills(jd)

    w_score, breakdown, missing, rationale = weighted_score(resume, jd_skills)
    t_score = tfidf_score(resume, jd)

    final = round((0.6 * t_score) + (0.4 * w_score), 2)

    return final, breakdown, missing, rationale, jd_skills


# -------------------------------
# SUGGESTIONS
# -------------------------------
def generate_suggestions(missing, score):
    suggestions = []

    for skill in missing:
        suggestions.append(f"Add hands-on experience with {skill}.")
        suggestions.append(f"Include project using {skill}.")

    if score < 60:
        suggestions.append("Add measurable achievements.")
        suggestions.append("Use strong action verbs.")

    return list(set(suggestions))


# -------------------------------
# BULLET GENERATOR
# -------------------------------
def generate_bullets(jd_skills):
    bullets = []

    for skill in jd_skills[:3]:
        bullets.append(
            f"Developed solutions using {skill}, improving performance and scalability."
        )

    if "api" in jd_skills:
        bullets.append("Built REST APIs for efficient data communication.")

    if "aws" in jd_skills:
        bullets.append("Deployed applications on AWS cloud infrastructure.")

    return bullets


# -------------------------------
# ROUTES
# -------------------------------
@app.route('/')
def index():
    return render_template('index.html')


@app.route('/analyze', methods=['POST'])
def analyze():
    if 'resume' not in request.files or 'jd' not in request.files:
        return "Missing file upload", 400

    resume_file = request.files['resume']
    jd_file = request.files['jd']

    if resume_file.filename == '' or jd_file.filename == '':
        return "No selected file", 400

    # Extract text
    resume_text = clean_text(extract_text(resume_file))
    jd_text = clean_text(extract_text(jd_file))

    # Run AI
    score, breakdown, missing, rationale, jd_skills = hybrid_score(resume_text, jd_text)

    suggestions = generate_suggestions(missing, score)
    bullets = generate_bullets(jd_skills)

    return render_template(
        'result.html',
        score=score,
        breakdown=breakdown,
        missing_skills=missing,
        suggestions=suggestions,
        rationale=rationale,
        bullets=bullets
    )


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8000)