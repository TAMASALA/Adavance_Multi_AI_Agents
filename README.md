# 🚀 Multi-AI Agent Assistant

This project is a **Multi-Agent AI System** built using FastAPI and CrewAI.  
It supports multiple intelligent agents like:

- 🧠 Information Retrieval (Web + Writer)
- 💻 Code Generation
- ✈️ Flight Suggestions
- 🎨 Image Generation (Diffusion Models)

---

## 🔥 Features

- Multi-Agent Architecture using CrewAI
- Intent Detection System
- LLM-powered reasoning (Groq API)
- Stable Diffusion Image Generation (local)
- Context-based responses using documents
- FastAPI Web Interface
- Lightweight CPU-compatible setup

---

## 🧠 How It Works

### 1. User Input
User enters a query in the web UI.

Example:
Find flights from Hyderabad to Goa


---

### 2. Intent Detection

The system detects user intent using `router.py`:

- `code` → Coding Agent
- `flight` → Flight Agent
- `image` → Image Agent
- `info` → Web + Writer Agents

---

### 3. Agent Execution (CrewAI)

Based on intent:

- Crew is created with specific agents + tasks
- Each agent has:
  - Role
  - Goal
  - Tools (Serper API for search)
  - LLM (Groq)

---

### 4. Knowledge Injection (RAG-style)

Each agent gets context from:
/documents/*.txt


Example:
- coding rules
- flight examples
- writing style

---

### 5. Image Generation Flow

- LLM enhances user prompt
- Diffusion model generates image locally

User Prompt → LLM Enhancement → Stable Diffusion → Image Output


---

### 6. Output

- Text → shown in UI
- Image → saved in `/static` and displayed

---

## 🏗️ Project Structure

├── app.py
├── agents.py
├── tasks.py
├── router.py
├── image_agent.py
├── documents/
│ ├── web_agent_docs.txt
│ ├── writer_agent_docs.txt
│ ├── coder_agent_docs.txt
│ ├── flight_agent_docs.txt
│ └── image_agent_docs.txt
├── templates/
│ └── index.html
├── static/
│ └── style.css


---

## ⚙️ Installation

### 1. Create Environment
python -m venv venv
venv\Scripts\activate


### 2. Install Dependencies
pip install -r requirements.txt


---

## 🔑 Environment Variables

Create `.env` file:

GROQ_API_KEY=your_groq_api_key
SERPER_API_KEY=your_serper_api_key


---

## ▶️ Run Application

uvicorn app:app --reload


Open in browser:
http://127.0.0.1:8000


---

## 🧪 Sample Queries

- "Write Python code for Fibonacci"
- "Find flights from Delhi to Mumbai"
- "Generate image of futuristic city"
- "What is Artificial Intelligence?"

---

## ⚡ Tech Stack

- FastAPI
- CrewAI
- Groq LLM
- Serper API (Search)
- Stable Diffusion (Diffusers)
- Jinja2 Templates

---

## 🐳 Docker (Optional)

Build:
docker build -t multi-ai-agent .


Run:
docker run -p 8000:8000 multi-ai-agent


---

## 🚀 Future Improvements

- Add GPU acceleration
- Add multi-image generation
- Add chat history
- Add voice input
- Deploy on cloud (AWS / GCP)

---

## 👨‍💻 Author

Built with ❤️ using AI Agents