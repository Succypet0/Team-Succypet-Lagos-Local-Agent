# 🇳🇬 Lagos Local Agent | DSN X BCT Hackathon 3.0

The "Lagos Local" Agent is an advanced, multi-agentic orchestration system designed for hyper-contextual user modeling and intelligent restaurant recommendation within the Nigerian consumer landscape.

## 🚀 Quick Start
1. Ensure [Docker](https://www.docker.com/) and `docker-compose` are installed on your machine.
2. Clone this repository to your local machine.
3. Boot up the unified multi-container stack by running the following command in the root directory:
   ```bash
   docker-compose up -d

⚙️ Configuration (One-Time Setup)
Once the containers are running, you must configure the orchestration engine:

Access n8n: Navigate to http://localhost:5678 in your browser.

Import Workflow:

Go to the Workflows tab in the sidebar.

Select Import from File.

Select the dsn_hackathon_workflow.json file located in the /workflow folder of this repository.

Configure Credentials:

Open your n8n credentials manager.

Add your OpenAI API Token to enable the LLM agents.

Data Table Integration:

Open the Data Table nodes within the workflow.

Task A: Configure the node to read the review dataset from /data/Lagos_Local_Agent_Balanced_Reviews.csv.

Task B: Configure the node to read the restaurant dataset from /data/Lagos_Local_Agent_Restaurants.csv.

Publish/Activate: Click Save and then toggle the workflow to Active to register the Webhook endpoints.

🧪 Testing the Agent
Once configured, head to the frontend interface:

Streamlit UI: http://localhost:8501

🏗 Modular Architecture
Orchestration Layer: Built with n8n to execute conditional routing, agent logic, and data payload compilation.

Frontend Layer: Built with Streamlit to provide an interactive interface for human evaluators and judges.

Task A (Behavioral Simulator Agent): Utilizes few-shot prompting grounded in actual text responses to mirror local pacing, slang, and cultural tone.

Task B (Contextual Recommender Agent): Processes real-world data stores dynamically to match user personas against local constraints (budget, location, and vibe).

📊 Grounding Data Pipeline
The intelligence of our agents is grounded in heavily curated datasets located in the /data folder:

Task A Data: Lagos_Local_Agent_Balanced_Reviews.csv (1-5 star behavioral grounding).

Task B Data: Lagos_Local_Agent_Restaurants.csv (Verified restaurant database).

📝 Core Submission Endpoints
Task A (Review Simulator): /webhook/task-a-simulate

Task B (Smart Recommender): /webhook/task-b-recommend