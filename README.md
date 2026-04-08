# 🚀 NeuroFlow Lite – Multi-Agent AI Productivity System

## 🧠 Overview
NeuroFlow Lite is a multi-agent AI system designed to automate task management, scheduling, and information handling by coordinating multiple intelligent agents and tools.

## 🎯 Problem Statement
Managing tasks, schedules, and information across multiple tools is:
- Time-consuming
- Unorganized
- Inefficient

## 💡 Solution
NeuroFlow Lite uses a multi-agent architecture where:
- A primary coordinator agent orchestrates the workflow
- Multiple sub-agents handle specific tasks
- Tools simulate real-world integrations

## 🏗️ Architecture

User Input  
↓  
Coordinator Agent  
↓  
Task Agent → Generates tasks  
Schedule Agent → Creates schedule  
↓  
Tools Layer (Storage)  
↓  
Structured Output  

## ⚙️ Features
- Multi-agent coordination  
- Task generation  
- Automated scheduling  
- Structured data storage  
- API-based workflow execution  
- Cloud deployment (Google Cloud Run)  

## 🧰 Tech Stack
- Python  
- FastAPI  
- Docker  
- Google Cloud Run  

## 🔄 Workflow
1. User sends input (e.g., "I have exams, plan my schedule")
2. Coordinator agent processes request
3. Task agent generates tasks
4. Schedule agent organizes tasks
5. Tools store structured data
6. System returns final output

## 📡 API Endpoints

### GET /
Check system status

Response:
{
  "message": "NeuroFlow API running"
}

### POST /query

Example Input:
{
  "user_input": "I have exams, plan my schedule"
}

Example Output:
{
  "tasks": ["Study ML", "Revise DBMS"],
  "schedule": {
    "Monday": "Study ML - 2 hours",
    "Tuesday": "Revise DBMS - 2 hours"
  },
  "status": "stored successfully"
}
## ☁️ Live Deployment
https://neuroflow-753770087433.asia-south1.run.app

Try:
https://neuroflow-753770087433.asia-south1.run.app/docs

## 🎥 Demo
(Add your video link here)

## 🚀 Future Improvements
- Real MCP integration
- Google Calendar API integration
- Notes & Email automation
- Persistent database (AlloyDB / Firestore)
- LLM-powered intelligent agents

## 🏆 Hackathon Goal Alignment
- Multi-agent system
- Coordinator + sub-agents
- Tool integration
- Structured data handling
- API-based deployment

## 👩‍💻 Author
Pravallika Vetapalem  
B.Tech CSE (Data Science)  
Passionate about AI & ML  

## 🌟 Acknowledgment
Built as part of Gen AI Hackathon APAC Edition 2026

⭐ If you like this project, give it a star!
