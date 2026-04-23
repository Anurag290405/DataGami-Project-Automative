## 📂 AutoMind Project Navigation

### 🚀 Get Started Here
1. **[SETUP.md](SETUP.md)** ← Start here for quick 1-minute setup
2. **[README.md](README.md)** ← Full documentation and troubleshooting
3. **[IMPLEMENTATION_SUMMARY.md](IMPLEMENTATION_SUMMARY.md)** ← What was built and next steps

### 📚 Documentation
- **[ARCHITECTURE.txt](ARCHITECTURE.txt)** - Visual component map
- **[docs/architecture.md](docs/architecture.md)** - Detailed architecture (expandable)
- **[docs/api-spec.md](docs/api-spec.md)** - API specification (expandable)

### 🔧 Backend (Python FastAPI)

#### Entry Points
- **[backend/main.py](backend/main.py)** - FastAPI app setup and routing
- **[backend/config.py](backend/config.py)** - Configuration and settings

#### Agent Pipeline (The 5-Agent System)
- **[backend/agents/orchestrator.py](backend/agents/orchestrator.py)** - Main pipeline controller
- **[backend/agents/prompt_enhancer_agent.py](backend/agents/prompt_enhancer_agent.py)** - Refines user input
- **[backend/agents/research_agent.py](backend/agents/research_agent.py)** - Technical analysis
- **[backend/agents/writer_agent.py](backend/agents/writer_agent.py)** - Professional reports
- **[backend/agents/memory_agent.py](backend/agents/memory_agent.py)** - ChromaDB storage
- **[backend/agents/response_agent.py](backend/agents/response_agent.py)** - Output composition

#### API Routes
- **[backend/routers/health.py](backend/routers/health.py)** - `/api/health`
- **[backend/routers/reports.py](backend/routers/reports.py)** - `/api/generate-report`, `/api/reports`
- **[backend/routers/prompts.py](backend/routers/prompts.py)** - `/api/enhance-prompt`
- **[backend/routers/memory.py](backend/routers/memory.py)** - `/api/store-memory`

#### Services
- **[backend/services/groq_service.py](backend/services/groq_service.py)** - Groq LLM integration
- **[backend/services/chroma_service.py](backend/services/chroma_service.py)** - ChromaDB vector DB
- **[backend/services/report_service.py](backend/services/report_service.py)** - Report metadata (JSON store)

#### Data Models
- **[backend/models/request_models.py](backend/models/request_models.py)** - Input schemas
- **[backend/models/response_models.py](backend/models/response_models.py)** - Output schemas

#### Config
- **[backend/.env.example](backend/.env.example)** - Environment template (copy to .env)
- **[backend/requirements.txt](backend/requirements.txt)** - Python dependencies

### 🎨 Frontend (React + Vite)
- **[frontend/src/App.jsx](frontend/src/App.jsx)** - Main React component
- **[frontend/src/main.jsx](frontend/src/main.jsx)** - React entry point
- **[frontend/index.html](frontend/index.html)** - HTML shell
- **[frontend/package.json](frontend/package.json)** - npm dependencies and scripts
- **[frontend/vite.config.js](frontend/vite.config.js)** - Vite config + proxy to backend

### 🐳 Infrastructure
- **[infra/docker/backend.Dockerfile](infra/docker/backend.Dockerfile)** - Python image
- **[infra/docker/frontend.Dockerfile](infra/docker/frontend.Dockerfile)** - Node image
- **[infra/github-actions/ci-cd.yml](infra/github-actions/ci-cd.yml)** - CI/CD workflow
- **[docker-compose.yml](docker-compose.yml)** - Full-stack local development

---

## 🎯 Quick Reference

### Development Commands
```bash
# Backend
cd backend
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python main.py

# Frontend (new terminal)
cd frontend
npm install
npm run dev

# Full-stack Docker
docker-compose up --build
```

### API Endpoints
| Endpoint | Method | Purpose |
|----------|--------|---------|
| `/api/health` | GET | Service status |
| `/api/generate-report` | POST | Full agent pipeline |
| `/api/enhance-prompt` | POST | Prompt refinement |
| `/api/store-memory` | POST | Vector storage |
| `/api/reports` | GET | Report history |

### Key Files to Edit
- **Add LLM provider**: [backend/services/groq_service.py](backend/services/groq_service.py)
- **Customize agents**: [backend/agents/](backend/agents/)
- **Modify UI**: [frontend/src/App.jsx](frontend/src/App.jsx)
- **Add routes**: [backend/routers/](backend/routers/)

---

## 📋 Architecture at a Glance

```
User Input (React Frontend)
         ↓
   FastAPI Gateway
         ↓
   Agent Orchestrator
    ↙  ↓  ↓  ↓  ↘
   5 Specialized Agents
         ↓
   Groq LLM API
         ↓
   ChromaDB Vector Store
         ↓
   Report Metadata Store
         ↓
   React Frontend Display
```

---

## 🔗 Original Projects (Untouched)

Your original projects are still in the root directory:
- `Agentic-Ai/` - Original multi-agent system (Streamlit)
- `GEN-AI/` - Original multimodal generation (GenAI concepts)
- `Devops/` - Original Laravel deployment template
- `Integration.md` - Your original integration proposal

**AutoMind** is the unified production version combining their strengths.

---

## ✅ Status

The AutoMind platform is **production-ready** to:
- Generate automotive reports using multi-agent orchestration
- Store semantic memory in ChromaDB
- Serve a React web interface
- Run in Docker containers
- Deploy with GitHub Actions CI/CD

Happy building! 🚀
