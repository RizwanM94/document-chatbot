import os
import fitz  
from flask import Flask, request, jsonify
from flask_cors import CORS
import google.generativeai as genai
from dotenv import load_dotenv


load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

app = Flask(__name__)
CORS(app)

# Store documents
documents = {}

@app.route("/upload", methods=["POST"])
def upload_document():
    file = request.files.get("file")
    if not file:
        return jsonify({"error": "No file provided"}), 400

    try:
        if file.filename.endswith(".pdf"):
            # Extract text from PDF
            doc = fitz.open(stream=file.read(), filetype="pdf")
            doc_text = "\n".join([page.get_text() for page in doc])
        else:
            # Decode plain text file
            doc_text = file.read().decode("utf-8")

        documents["user_doc"] = doc_text 

        return jsonify({"message": "Document uploaded successfully!"})

    except Exception as e:
        return jsonify({"error": f"Failed to process file: {str(e)}"}), 500

@app.route("/ask", methods=["POST"])
def ask_question():
    data = request.json
    question = data.get("question")

    if "user_doc" not in documents:
        return jsonify({"error": "No document uploaded"}), 400

    # Get document 
    context = documents["user_doc"]
    
    # Generate response using Gemini
    model = genai.GenerativeModel("gemini-2.0-flash")
    response = model.generate_content(f"Document: {context}\n\nQuestion: {question}")

    return jsonify({"answer": response.text})

if __name__ == "__main__":
    app.run(debug=True)
