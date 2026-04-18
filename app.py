from flask import Flask, request, jsonify
import pdfplumber

app = Flask(__name__)

# Home route
@app.route("/", methods=["GET"])
def home():
    return "API is running!"

# Resume upload route
@app.route("/upload", methods=["POST"])
def upload_resume():
    file = request.files["file"]

    text = ""
    with pdfplumber.open(file) as pdf:
        for page in pdf.pages:
            text += page.extract_text()

    result = {
        "ats_score": 72,
        "missing_skills": ["Docker", "AWS", "CI/CD"],
        "suggestion": "Add DevOps tools and project details"
    }

    return jsonify(result)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
