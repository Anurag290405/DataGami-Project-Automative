# Windows Installation Troubleshooting

## Problem: `error: Microsoft Visual C++ 14.0 or greater is required`

This occurs when installing ChromaDB on Windows because it contains C++ native extensions that need compilation.

---

## ✅ Solution 1: Use Docker (RECOMMENDED for Windows)

Docker eliminates all Windows-specific build issues. Install Docker Desktop and run:

```bash
cd automind-intelligence-platform

# Copy environment
cp backend/.env.example backend/.env
# Edit backend/.env and add GROQ_API_KEY

# Start full stack
docker-compose up --build
```

**Result:**
- Backend: `http://localhost:8000`
- Frontend: `http://localhost:5173`
- API Docs: `http://localhost:8000/docs`

---

## ✅ Solution 2: Install Microsoft Visual C++ Build Tools

This enables Windows to compile C++ packages like ChromaDB.

### Steps:
1. Download: https://visualstudio.microsoft.com/visual-cpp-build-tools/
2. Run the installer
3. Select "Desktop development with C++"
4. Install (~4GB)
5. Restart your terminal/PowerShell
6. Retry installation:

```bash
cd backend
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env
# Edit .env and add GROQ_API_KEY
python main.py
```

---

## ✅ Solution 3: Minimal Install (Skip ChromaDB Build)

If you only want quick testing without the full C++ toolchain:

```bash
cd backend
python -m venv venv
venv\Scripts\activate

# Install everything except what needs compilation
pip install fastapi==0.115.0
pip install uvicorn[standard]==0.30.6
pip install langchain==0.3.7
pip install langchain-core==0.3.19
pip install langchain-groq==0.2.1
pip install pydantic==2.9.2
pip install pydantic-settings==2.6.1
pip install python-dotenv==1.0.1

# Then try chromadb separately
pip install chromadb --no-build-isolation
```

---

## 📊 Comparison

| Method | Effort | Time | Dependencies | Notes |
|--------|--------|------|--------------|-------|
| Docker | Low | 5 min | Docker Desktop | **Recommended** |
| Build Tools | Medium | 10 min | Visual C++ | Full capability |
| Minimal | Low | 5 min | Python only | May have ChromaDB issues |

---

## ✅ Verify Installation

Once installed (any method), test:

```bash
curl -X GET http://localhost:8000/api/health
# Should return: {"status":"ok","service":"AutoMind Intelligence Platform"}
```

Or visit: `http://localhost:8000/docs`

---

## Still Having Issues?

### Check Python Version
```bash
python --version
# Should be 3.11+
```

### Check pip version
```bash
python -m pip install --upgrade pip
```

### Clear pip cache
```bash
pip cache purge
pip install -r requirements.txt --no-cache-dir
```

### Force reinstall chromadb without build
```bash
pip install chromadb --only-binary :all:
```

---

## Next Steps

1. **Choose a method** (Docker recommended for Windows)
2. **Configure `.env`** with your Groq API key
3. **Run the setup** from SETUP.md
4. **Test at** `http://localhost:8000/docs`

Good luck! 🚀
