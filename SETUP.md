# AutoMind Quick Setup Guide

## ⚠️ Windows Users: Before Starting

If you encounter `error: Microsoft Visual C++ 14.0 or greater is required`, follow one of these solutions:

### Solution 1: Use Docker (Easiest for Windows) ⭐ RECOMMENDED

```bash
docker-compose up --build
```

This avoids Windows build tools entirely. Backend runs at `http://localhost:8000`, frontend at `http://localhost:5173`.

---

### Solution 2: Install Visual C++ Build Tools

1. Download: https://visualstudio.microsoft.com/visual-cpp-build-tools/
2. Install "Desktop development with C++"
3. Restart terminal and retry:

```bash
cd backend
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python main.py
```

---

### Solution 3: Use Pre-built ChromaDB Wheel (Windows Only)

If you want to avoid installing Build Tools, update `requirements.txt` to use a pre-compiled version:

```bash
cd backend
python -m venv venv
venv\Scripts\activate
# Use this command instead of pip install -r requirements.txt
pip install fastapi uvicorn langchain langchain-core langchain-groq pydantic pydantic-settings python-dotenv chromadb
python main.py
```

---

## 1-Minute Backend Start (After Installing Build Tools)

```bash
cd backend
python -m venv venv
venv\Scripts\activate  # Windows
# OR: source venv/bin/activate  # macOS/Linux

pip install -r requirements.txt
cp .env.example .env
# Edit .env and add GROQ_API_KEY
python main.py
```

Backend runs at: `http://localhost:8000`

## 1-Minute Frontend Start (New Terminal)

```bash
cd frontend
npm install
npm run dev
```

Frontend runs at: `http://localhost:5173`

## Full-Stack Docker (No Installation Required)

This is the **easiest way** to get started on Windows:

```bash
# Make sure you're in the project root
cd automind-intelligence-platform

# Copy environment file
cp backend/.env.example backend/.env
# Edit backend/.env and add GROQ_API_KEY

# Start everything
docker-compose up --build
```

Both services will be ready:
- Backend: `http://localhost:8000`
- Frontend: `http://localhost:5173`
- API Docs: `http://localhost:8000/docs`

## API Testing

```bash
curl -X POST http://localhost:8000/api/generate-report \
  -H "Content-Type: application/json" \
  -d '{"prompt":"Design a futuristic electric SUV for the Indian market."}'
```

Visit `http://localhost:8000/docs` for interactive API docs.
