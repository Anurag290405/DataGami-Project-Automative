# AutoMind Intelligence Platform

AutoMind is a unified AI platform combining agentic and generative capabilities for automotive research report generation and concept intelligence.

## Features

- **Multi-Agent Orchestration**: Prompt enhancement, research, writing, and memory storage
- **FastAPI Backend**: RESTful API with Pydantic validation
- **React + Vite Frontend**: Interactive UI for report generation and browsing
- **Groq LLM Integration**: Fast inference using llama-3.3-70b-versatile
- **ChromaDB Vector Memory**: Semantic search and embedding storage
- **Docker Support**: Containerized local and production deployments
- **GitHub Actions CI/CD**: Automated build and deployment pipeline

## Quick Start (Local Development)

### Prerequisites

- Python 3.11+
- Node.js 20+
- Docker (optional, for containerized setup)
- Groq API Key (get from https://console.groq.com)

### Step 1: Clone and Setup Environment

```bash
git clone <repo>
cd automind-intelligence-platform

cp backend/.env.example backend/.env
# Edit backend/.env and add your GROQ_API_KEY
```

### Step 2: Backend Setup

```bash
cd backend
python -m venv venv

# Windows:
venv\Scripts\activate

# macOS/Linux:
source venv/bin/activate

pip install -r requirements.txt
python main.py
```

Backend will run on: `http://localhost:8000`  
API docs available at: `http://localhost:8000/docs`

### Step 3: Frontend Setup (New Terminal)

```bash
cd frontend
npm install
npm run dev
```

Frontend will run on: `http://localhost:5173`

### Step 4: Test the Platform

1. Open `http://localhost:5173` in your browser.
2. Enter a prompt (e.g., "Design a futuristic electric SUV for the Indian market.").
3. Click "Generate Report".
4. Wait for the agent pipeline to complete and see the results.

## Project Structure

```
automind-intelligence-platform/
  backend/               # FastAPI server
    main.py             # Entry point
    config.py           # Configuration
    requirements.txt    # Dependencies
    routers/            # API routes
    agents/             # Agent implementations
    services/           # Services (Groq, ChromaDB, Reports)
    models/             # Pydantic schemas
    utils/              # Utilities (logging, etc.)
    database/           # ChromaDB storage
  
  frontend/             # React + Vite
    src/
      App.jsx          # Main app component
      main.jsx         # React entry point
    package.json
    vite.config.js
  
  infra/               # Infrastructure
    docker/            # Dockerfiles
    github-actions/    # CI/CD workflows
  
  docs/                # Documentation
  
  docker-compose.yml   # Full stack local run
```

## API Endpoints

### Generate Report
- **POST** `/api/generate-report`
- Creates a full automotive report using the agent pipeline.
- Body: `{ "prompt": "..." }`
- Returns: Full report with research, narrative, and memory IDs.

### Enhance Prompt
- **POST** `/api/enhance-prompt`
- Improves user prompt with automotive terminology.
- Body: `{ "prompt": "..." }`
- Returns: `{ "enhanced_prompt": "..." }`

### Store Memory
- **POST** `/api/store-memory`
- Embeds and stores content in ChromaDB.
- Body: `{ "report_id": "...", "content": "...", "metadata": {...} }`
- Returns: `{ "status": "stored", "memory_id": "..." }`

### List Reports
- **GET** `/api/reports`
- Fetches all generated reports.
- Returns: List of report metadata.

### Health Check
- **GET** `/api/health`
- Returns: `{ "status": "ok", "service": "AutoMind Intelligence Platform" }`

## Docker Compose (Full Stack)

```bash
docker-compose up --build
```

This will start:
- Backend on port `8000`
- Frontend on port `5173`

## Architecture

### Agent Pipeline
1. **Prompt Enhancer**: Refines user prompt with automotive expertise.
2. **Research Agent**: Generates technical insights and automotive data.
3. **Writer Agent**: Produces professional structured report.
4. **Memory Agent**: Stores embeddings in ChromaDB for semantic search.
5. **Response Agent**: Composes final API response.

### Data Flow
```
User Prompt → API Gateway → Orchestrator → Agents → LLM (Groq)
↓
ChromaDB (vector memory) + Report Store
↓
Frontend Result Display
```

## Environment Configuration

Set in `backend/.env`:

- `GROQ_API_KEY`: Your Groq API key
- `GROQ_MODEL`: LLM model (default: llama-3.3-70b-versatile)
- `APP_NAME`: App display name
- `API_PREFIX`: API base path (default: /api)
- `CHROMA_PERSIST_DIR`: Vector DB storage location
- `CORS_ORIGINS`: Comma-separated allowed origins

## CI/CD Pipeline

GitHub Actions workflow (`.github/workflows/ci-cd.yml`):
1. Lint backend code
2. Install and build frontend
3. Run tests (extensible)
4. Optional: Build and push Docker images
5. Optional: Deploy to production

## Production Considerations

- [ ] Add input validation and sanitization
- [ ] Implement request rate limiting
- [ ] Add authentication (JWT/OAuth2)
- [ ] Use PostgreSQL for report metadata (vs. JSON file)
- [ ] Deploy backend and frontend to cloud (AWS/GCP/Azure)
- [ ] Set up observability (logging, metrics, tracing)
- [ ] Add integration tests
- [ ] Configure secrets management

## Troubleshooting

### Backend fails to start
- Ensure Python 3.11+ is installed.
- Check `GROQ_API_KEY` is set in `backend/.env`.

### Frontend can't connect to backend
- Ensure backend is running on port 8000.
- Check `vite.config.js` proxy configuration.

### ChromaDB connection issues
- Ensure `database/chroma` directory exists.
- Check file permissions on the database directory.

## Next Steps

1. Integrate additional LLM providers (OpenAI, Anthropic, etc.).
2. Add streaming response support (SSE/WebSocket).
3. Implement user authentication and authorization.
4. Add support for image generation concepts.
5. Enhance UI with advanced report browsing and filtering.
6. Add evaluation framework for agent quality.

## License

MIT
