# 📄 Document Chatbot using Google Gemini 2.0 API

This is a simple Flask-based chatbot that allows users to upload a document and ask questions about its content using Google Gemini 2.0 API.

## 🚀 Features

- Upload a document (text file)
- Store document content in memory
- Ask questions about the uploaded document
- Get responses using Google Gemini 2.0 API
- Basic Flask API with CORS enabled

## 🛠️ Technologies Used

- Python 3.10
- Flask
- Flask-CORS
- Google Generative AI (Gemini 2.0 API)

## 📂 Project Structure

```
📦 document-chatbot
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── .gitignore             # Git ignore file
├── .env                   # Environment variables (API key)
├── README.md              # Project documentation
```

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/document-chatbot.git
cd document-chatbot
```

### 2️⃣ Create a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Set Up Environment Variables

Create a `.env` file and add your Gemini API Key:

```env
GEMINI_API_KEY=your_api_key_here
```

### 5️⃣ Run the Application

```bash
python app.py
```

## 📤 API Endpoints

### **1. Upload Document**

**Endpoint:** `POST /upload`

- Upload a text file
- Stores document content in memory

```bash
curl -X POST -F "file=@example.txt" http://127.0.0.1:5000/upload
```

### **2. Ask a Question**

**Endpoint:** `POST /ask`

- Takes a question as input
- Returns an AI-generated response based on the uploaded document

```bash
curl -X POST http://127.0.0.1:5000/ask \
     -H "Content-Type: application/json" \
     -d '{"question": "What is the document about?"}'
```

## 🛠️ Future Improvements

- Store documents in a database
- Support PDF file uploads and text extraction
- Enhance UI for document uploading and chat

## 📜 License

This project is open-source and available under the MIT License.

---

### 🌟 Show Some Support!

If you find this project useful, don't forget to give it a ⭐ on GitHub!

