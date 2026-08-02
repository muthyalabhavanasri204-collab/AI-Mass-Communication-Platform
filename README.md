# 🚀 AI-Based Multilingual Mass Communication Platform

An AI-powered Mass Communication Platform built using **FastAPI**, **PostgreSQL**, and **Google Gemini AI**. This platform helps organizations create, manage, and deliver multilingual communication campaigns while efficiently managing audiences.

---

## 📌 Features

### 🔐 Authentication
- User Registration
- User Login
- JWT Authentication
- Secure Password Hashing

### 👥 Audience Management
- Add Audience
- Update Audience
- Delete Audience
- View Audience
- Audience Segmentation
- Demographics Management
- Geographic Information
- Language Preferences

### 📢 Campaign Management
- Create Campaign
- Update Campaign
- Delete Campaign
- Campaign Status Management
- Campaign Lifecycle Tracking

### 📝 Template Management
- Create Templates
- Edit Templates
- Delete Templates
- Reusable Communication Templates

### 📊 Dashboard
- Total Audience Count
- Total Campaign Count
- Total Templates
- Campaign Statistics

### 📜 Campaign History
- Track Campaign Activities
- View Campaign History

### 🌍 AI Translation
Powered by **Google Gemini AI**

Supported Languages:
- English
- Telugu
- Hindi
- Tamil
- Kannada
- Malayalam

---

## 🛠️ Tech Stack

### Backend
- FastAPI
- Python
- SQLAlchemy
- PostgreSQL
- JWT Authentication

### AI
- Google Gemini API

### Database
- PostgreSQL

### API Testing
- Swagger UI
- Postman

### Version Control
- Git
- GitHub

---

## 📂 Project Structure

```text
backend/
│
├── app/
│   ├── auth/
│   ├── models/
│   ├── routes/
│   ├── schemas/
│   ├── services/
│   ├── database.py
│   ├── config.py
│   └── main.py
│
├── .env
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/muthyalabhavanasri204-collab/AI-Mass-Communication-Platform.git
```

### Navigate

```bash
cd AI-Mass-Communication-Platform/backend
```

### Create Virtual Environment

```bash
python -m venv .venv
```

### Activate

Windows

```bash
.venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Configure Environment Variables

Create a `.env` file:

```env
DATABASE_URL=your_database_url
SECRET_KEY=your_secret_key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
GEMINI_API_KEY=your_gemini_api_key
```

### Run Server

```bash
python -m uvicorn app.main:app --reload
```

---

## 📖 API Documentation

After starting the server:

Swagger UI

```
http://127.0.0.1:8000/docs
```

---

## 📸 Current Modules

- ✅ Authentication
- ✅ Role Based Access
- ✅ Audience Management
- ✅ Audience Segmentation
- ✅ Campaign Management
- ✅ Template Library
- ✅ Campaign History
- ✅ Dashboard APIs
- ✅ AI Translation (Gemini)

---

## 🚀 Future Enhancements

- AI Scam Detection
- AI Campaign Generation
- Email Integration
- WhatsApp Integration
- SMS Integration
- Sentiment Analysis
- Campaign Analytics
- React Dashboard

---

## 👩‍💻 Developer

**Muthyala Bhavana Sri**

GitHub:
https://github.com/muthyalabhavanasri204-collab

---

## 📄 License

This project is developed for learning, internship, and hackathon purposes.