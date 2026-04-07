# Customer Support Automation System 


## 🚀 Overview

The **Customer Support Automation System** is a multi-agent AI-powered solution built with CrewAI that automates customer support inquiries. It uses specialized AI agents working together to provide comprehensive, accurate, and friendly customer support responses.

### Key Features
- 🤖 **Multi-agent architecture** with specialized roles
- ✅ **Quality assurance** with automatic review process
- 🛠️ **Extensible tool system** for web scraping and research
- 💾 **Memory support** for contextual conversations
- 🐳 **Docker-ready** for easy deployment
- 📊 **Monitoring & health checks**
- 🔧 **REST API** for easy integration

## 🏗️ Architecture

### System Components

```
┌─────────────────┐    ┌──────────────────┐    ┌─────────────────┐
│   Client App    │ ──▶│   FastAPI API    │ ──▶│   Support Crew  │
└─────────────────┘    └──────────────────┘    └─────────────────┘
                              │                         │
                              ▼                         ▼
                    ┌──────────────────┐    ┌─────────────────┐
                    │   Configuration  │    │   Agent Pool    │
                    └──────────────────┘    └─────────────────┘
                              │                         │
                              ▼                         ▼
                    ┌──────────────────┐    ┌─────────────────┐
                    │   Tools Registry │    │   Task Queue    │
                    └──────────────────┘    └─────────────────┘
```

### Agent Workflow

```mermaid
graph LR
    A[Customer Inquiry] --> B[Support Agent]
    B --> C[Draft Response]
    C --> D[QA Agent]
    D --> E[Quality Review]
    E --> F[Final Response]
    F --> G[Customer]
```

## 🚀 Quick Start

### Prerequisites

- Python 3.9+
- OpenAI API key
- (Optional) Serper API key for web search

### Installation

#### Option 1: Using Docker (Recommended)

```bash
# Clone the repository
git clone <repository-url>
cd customer-support-automation

# Copy environment file
cp .env.example .env

# Edit .env with your API keys
nano .env

# Start with Docker Compose
docker-compose up -d
```

#### Option 2: Local Installation

```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Set environment variables
export OPENAI_API_KEY="your-api-key"
export OPENAI_MODEL_NAME="gpt-3.5-turbo"

# Run the application
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
```

### Verify Installation

```bash
# Check health endpoint
curl http://localhost:8000/health

# Expected response:
{"status":"healthy","service":"customer-support-automation"}
```

## 📚 API Reference

### Base URL
```
http://localhost:8000
```

### Endpoints

#### 🩺 Health Check
```http
GET /health
```

**Response:**
```json
{
  "status": "healthy",
  "service": "customer-support-automation"
}
```

#### 💬 Process Support Inquiry
```http
POST /support/inquiry
```

**Request Body:**
```json
{
  "customer": "DeepLearningAI",
  "person": "Andrew Ng",
  "inquiry": "How do I add memory to my crew?",
  "metadata": {
    "priority": "high",
    "category": "technical"
  }
}
```

**Response:**
```json
{
  "success": true,
  "response": "Detailed support response here...",
  "processing_time": 12.45,
  "error": null
}
```

**Error Response:**
```json
{
  "success": false,
  "response": null,
  "processing_time": null,
  "error": "Error processing inquiry: API key invalid"
}
```

## ⚙️ Configuration

### Environment Variables

Create a `.env` file in the root directory:

```env
# Required: OpenAI Configuration
OPENAI_API_KEY=sk-your-openai-api-key-here
OPENAI_MODEL_NAME=gpt-3.5-turbo

# Optional: Web Search (Serper API)
SERPER_API_KEY=your-serper-api-key

# Application Settings
VERBOSE=false
MEMORY=true
ENABLE_WEB_SEARCH=false
ENABLE_WEB_SCRAPE=true

# Server Configuration
HOST=0.0.0.0
PORT=8000
LOG_LEVEL=INFO
```

### Configuration Options

| Variable | Default | Description |
|----------|---------|-------------|
| `OPENAI_API_KEY` | Required | Your OpenAI API key |
| `OPENAI_MODEL_NAME` | `gpt-3.5-turbo` | OpenAI model to use |
| `VERBOSE` | `false` | Enable verbose logging for CrewAI |
| `MEMORY` | `true` | Enable conversation memory |
| `ENABLE_WEB_SEARCH` | `false` | Enable web search capabilities |
| `ENABLE_WEB_SCRAPE` | `true` | Enable web scraping tools |

## 🤖 Agents & Tasks

### Support Agent
- **Role**: Senior Support Representative
- **Goal**: Provide friendly and comprehensive support
- **Tools**: Web scraping, documentation lookup
- **Delegation**: Not allowed

### Quality Assurance Agent
- **Role**: Support Quality Assurance Specialist
- **Goal**: Ensure response quality and completeness
- **Tools**: Review and validation
- **Delegation**: Can delegate back to Support Agent

### Task Flow

1. **Inquiry Resolution Task**
   - Handled by Support Agent
   - Uses available tools to research and draft response
   - Ensures completeness and accuracy

2. **Quality Assurance Task**
   - Handled by QA Agent
   - Reviews Support Agent's response
   - Ensures tone, completeness, and accuracy
   - Provides final approved response

## 🐳 Deployment

### Docker Deployment

```bash
# Build and start
docker-compose up -d

# View logs
docker-compose logs -f

# Scale services
docker-compose up -d --scale customer-support=3
```

### Kubernetes Deployment

```yaml
# kubernetes/deployment.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: customer-support-automation
spec:
  replicas: 3
  selector:
    matchLabels:
      app: customer-support
  template:
    metadata:
      labels:
        app: customer-support
    spec:
      containers:
      - name: customer-support
        image: your-registry/customer-support:latest
        ports:
        - containerPort: 8000
        env:
        - name: OPENAI_API_KEY
          valueFrom:
            secretKeyRef:
              name: api-secrets
              key: openai-api-key
        livenessProbe:
          httpGet:
            path: /health
            port: 8000
          initialDelaySeconds: 30
          periodSeconds: 10
```

### Cloud Deployment (AWS ECS)

```bash
# Build and push image
docker build -t your-ecr-repo/customer-support .
docker push your-ecr-repo/customer-support

# Deploy to ECS
aws ecs update-service --cluster your-cluster --service customer-support --force-new-deployment
```

## 📊 Monitoring & Logging

### Health Monitoring

The application includes built-in health checks:

```bash
# Manual health check
curl http://localhost:8000/health

# With detailed info
curl http://localhost:8000/health?detailed=true
```

### Logging

Logs are structured and include:

- Request/response timing
- Agent activities
- Error details
- Performance metrics

**Sample Log Output:**
```json
{
  "timestamp": "2024-01-15T10:30:00Z",
  "level": "INFO",
  "service": "customer-support",
  "message": "Processing inquiry from DeepLearningAI",
  "processing_time": 12.45,
  "customer": "DeepLearningAI"
}
```

### Metrics (Optional)

Enable Prometheus metrics:

```python
# Add to main.py
from prometheus_fastapi_instrumentator import Instrumentator

Instrumentator().instrument(app).expose(app)
```

## 🔧 Troubleshooting

### Common Issues

#### 1. API Key Issues
**Symptoms**: `401 Unauthorized` errors
**Solution**:
```bash
# Verify API key is set
echo $OPENAI_API_KEY

# Test OpenAI API directly
curl https://api.openai.com/v1/models \
  -H "Authorization: Bearer $OPENAI_API_KEY"
```

#### 2. Memory Issues
**Symptoms**: Slow performance with large conversations
**Solution**:
```env
# Reduce context window or disable memory
MEMORY=false
OPENAI_MODEL_NAME=gpt-3.5-turbo-16k
```

#### 3. Tool Execution Failures
**Symptoms**: Web scraping/timeout errors
**Solution**:
```env
# Disable problematic tools
ENABLE_WEB_SCRAPE=false
ENABLE_WEB_SEARCH=false
```

### Debug Mode

Enable debug logging for troubleshooting:

```bash
export LOG_LEVEL=DEBUG
export VERBOSE=true

# Restart application
docker-compose restart
```

## 💡 Examples

### Basic Usage

```python
import requests
import json

def submit_support_request(customer, person, inquiry):
    url = "http://localhost:8000/support/inquiry"
    payload = {
        "customer": customer,
        "person": person,
        "inquiry": inquiry
    }
    
    response = requests.post(url, json=payload)
    return response.json()

# Example usage
result = submit_support_request(
    customer="DeepLearningAI",
    person="Andrew Ng",
    inquiry="How do I create a crew with multiple agents?"
)

print(f"Success: {result['success']}")
print(f"Response: {result['response']}")
print(f"Processing Time: {result['processing_time']}s")
```

### Advanced Usage with Metadata

```python
def submit_priority_request(customer, inquiry, priority="normal"):
    payload = {
        "customer": customer,
        "person": "Technical Team",
        "inquiry": inquiry,
        "metadata": {
            "priority": priority,
            "category": "technical",
            "source": "api",
            "tags": ["crewai", "setup"]
        }
    }
    
    response = requests.post(SUPPORT_URL, json=payload)
    return response.json()
```

### Integration with Webhook

```python
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/webhook/support', methods=['POST'])
def handle_support_webhook():
    data = request.json
    
    # Process through support automation
    result = submit_support_request(
        customer=data['company'],
        person=data['requester']['name'],
        inquiry=data['message']
    )
    
    # Return formatted response
    return jsonify({
        "response": result['response'],
        "automated": True,
        "processing_time": result['processing_time']
    })
```

## 🎯 Use Cases

### 1. Technical Support
- Software documentation queries
- API usage questions
- Troubleshooting guidance

### 2. Product Support
- Feature explanations
- Best practices
- Integration guidance

### 3. Developer Support
- Code examples
- Architecture advice
- Implementation guidance

## 🔮 Extending the System

### Adding New Tools

```python
# src/tools/custom_tools.py
from crewai_tools import BaseTool
from typing import Any, Dict

class CustomKnowledgeBaseTool(BaseTool):
    name: str = "Knowledge Base Lookup"
    description: str = "Search internal knowledge base for solutions"
    
    def _run(self, query: str) -> str:
        # Implement your knowledge base search
        return "Relevant knowledge base article..."
```

### Creating New Agents

```python
# src/agents/specialized_agent.py
from crewai import Agent

class TechnicalSupportAgent:
    def create_agent(self):
        return Agent(
            role="Technical Support Specialist",
            goal="Provide deep technical guidance and troubleshooting",
            backstory="Expert in technical architecture and problem resolution...",
            tools=[technical_tools],
            allow_delegation=True
        )
```


