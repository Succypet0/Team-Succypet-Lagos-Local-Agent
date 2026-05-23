
---

```markdown
# 🇳🇬 Lagos Local Agent | DSN X BCT Hackathon 3.0

The "Lagos Local" Agent is an advanced, multi-agentic orchestration system designed for hyper-contextual user modeling and intelligent restaurant recommendation within the Nigerian consumer landscape.

## Features
* **Behavioral Simulator (Task A):** Generates highly realistic, localized product reviews utilizing authentic Nigerian context, tone, and slang (e.g., "Sapa", mainland traffic).
* **Contextual Recommender (Task B):** Processes dynamic real-world data to match user personas against local constraints (budget, location, and vibe).
* **Multi-Agentic Orchestration:** Built on conditional routing and agent logic that acts dynamically based on persona constraints.
* **Containerized Environment:** Fully reproducible Docker infrastructure ensuring a flawless "Quick Start" deployment.
* **Interactive UI:** A clean, progressive frontend built with Streamlit to showcase agent reasoning in real-time.

## Tech Stack
* **Orchestration Engine:** n8n 
* **Frontend UI:** Streamlit (Python 3.9)
* **AI/LLM Core:** OpenAI API
* **Containerization:** Docker & Docker Compose
* **Data Grounding:** Curated Local CSV Data Stores

---

## Quick Start

### Prerequisites
* [Docker](https://www.docker.com/) and `docker-compose` installed.
* An active OpenAI API Key.

### Installations
Clone the repository to your local machine:
```bash
git clone https://github.com/Succypet0/Team-Succypet-Lagos-Local-Agent.git
cd Team-Succypet-Lagos-Local-Agent

```

Spin up the containerized environment:

```bash
docker-compose up -d --build

```

### Environment Setup (n8n Configuration)

Once the containers are running, you must configure the orchestration engine:

1. Navigate to `http://localhost:5678` in your browser to access n8n.
2. Go to the **Workflows** tab and select **Import from File**.
3. Import `dsn_hackathon_workflow.json` located in the `/workflow` folder.
4. Add your **OpenAI API Token** in the n8n credentials manager.

### Data Table Integration

Ensure the agent can read the local datasets:

1. Open the **Data Table** nodes inside the imported n8n workflow.
2. **Task A:** Set the read path to `/data/Reviews.csv`.
3. **Task B:** Set the read path to `/data/Restaurants.csv`.
4. Click **Save** and toggle the workflow to **Active** to register the webhooks.

### Development & Testing

To interact with the agent, visit the Streamlit Frontend:

* **URL:** `http://localhost:8501`

---

## Repository Structure

```text
/Lagos-Local-Agent
├── /data
│   ├── Reviews.csv  # 1-5 star behavioral grounding
│   └── Restaurants.csv       # Verified restaurant database
├── /workflow
│   └── dsn_hackathon_workflow.json             # Exported n8n orchestration logic
├── app.py                                      # Streamlit frontend application
├── Dockerfile                                  # Python environment configuration
├── docker-compose.yml                          # Multi-container network setup
└── README.md                                   # Project documentation

```

---

## Architecture Overview

* **Frontend (Streamlit):** Captures user personas and product details, sending requests to the orchestration layer and displaying the agent's progressive reasoning.
* **Backend (n8n):** Serves as the brain. It receives webhook payloads, queries the local Data Tables (RAG approach) to ground the prompt, communicates with the OpenAI API, and enforces strict JSON formatting via a dedicated "Think Tool."

---

## Example API Endpoints

The n8n container exposes two core webhook endpoints utilized by the frontend:

### Task A (Review Simulator)

* **Endpoint:** `POST http://n8n:5678/webhook/task-a-simulate`
* **Description:** Generates a localized review based on user persona.

**Example Request:**

```json
{
  "persona": "A 22-year-old student on a tight budget",
  "product_details": "A new fast-food burger joint in Yaba"
}

```

**Example Response:**

```json
{
  "rating": 4,
  "review_text": "Mad o! The food is always on par, though the meat options need more spices for an African tongue. Definitely coming back with my guys once mainland traffic reduces."
}

```

### Task B (Smart Recommender)

* **Endpoint:** `POST http://n8n:5678/webhook/task-b-recommend`
* **Description:** Recommends a local spot based on persona constraints.

---

## Environment Variables

The application relies on secure credential management directly within the n8n UI, keeping API keys out of the codebase.

* `OPENAI_API_KEY`: Configured natively in n8n credentials.

---

## Continuous Integration & Deployment

This application is fully containerized for local evaluation. To deploy or test across different environments, `docker-compose` orchestrates the internal bridge network (`agent-network`), ensuring seamless API communication between Streamlit and n8n without CORS or localhost routing issues.

---

## Versioning & Changelog

* **v1.0.0:** Initial hackathon submission. Implemented multi-agent architecture, Dockerized deployment, and local Data Store integrations.

---

## Developer Checklist (Judge Evaluation)

To ensure a smooth evaluation process, please verify:

* [x] Docker containers are running securely (`docker ps`).
* [x] `dsn_hackathon_workflow.json` is imported and set to **Active**.
* [x] OpenAI API keys are saved in n8n.
* [x] Data Table nodes point correctly to the `/data/...` directory.

---

## Code of Conduct

Focus on collaboration, build hyper-local solutions, and respect the data.

## License

There is no license

```

```