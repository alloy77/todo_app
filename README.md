# ✅ Todo App — FastAPI + Streamlit + SQLite

This project is a full-stack Todo application built as part of the **Keploy Session 2 Assignment**. It features:

- 🚀 FastAPI backend with custom REST APIs
- 🖥️ Streamlit frontend for interacting with todos
- 💾 SQLite database using SQLAlchemy ORM
- 🐳 Docker support for easy deployment and testing

---

## 📌 Features

- Add, update, delete todos
- Mark todos as complete/incomplete
- Real-time UI using Streamlit
- SQLite for persistent storage
- REST API powered by FastAPI
- Dockerized for easy portability

---

## 🧑‍💻 How to Run (Without Docker)

### 1. 📦 Install dependencies

Create a virtual environment (optional but recommended):

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 2. ▶️ Run the FastAPI server
```bash
uvicorn app.main:app --reload
```

### 3. 🖥️ Run the Streamlit UI
```bash
streamlit run ui.py
```
UI available at: http://localhost:8501

## 🐳 How to Run with Docker

### 1. 🔨 Build the Docker image
```bash
docker build -t todo-app .
```

### 2. ▶️ Run the container
```bash
docker run -p 8000:8000 -p 8501:8501 todo-app
```
- FastAPI API: http://localhost:8000/docs
- Streamlit UI: http://localhost:8501

  # Thank You!
