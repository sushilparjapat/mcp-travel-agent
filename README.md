# 🌍 MCP Travel Assistant Chatbot

An interactive **Streamlit-based AI Travel Assistant** powered by **LangChain**, **OpenAI**, and multiple **MCP (Modular Component Protocol) servers**.  
It allows the chatbot to coordinate with specialized back-end agents for **flight search, hotel booking, weather info, finance insights**, and more — all via a single unified chat interface.

---

## 🚀 Features

- 🧠 **Multi-Agent Orchestration:** Communicates with multiple MCP servers (Flight, Hotel, Weather, etc.)  
- 🤖 **LLM-Powered Chat:** Uses OpenAI models (e.g., `gpt-5-nano`) for reasoning and response generation  
- ⚙️ **Asynchronous Processing:** Handles multiple server calls efficiently using `asyncio`  
- 💬 **Streamlit Chat UI:** User-friendly conversational interface  
- 🔐 **Environment-Based Configuration:** Keys and paths are securely managed via `.env`  

---

## 📁 Project Structure

mcp-travel-agent/ 
│ 
├── backend/ 
│   └── servers/ 
│       ├── flight_server/ 
│       │   └── flight_server.py 
│       ├── hotel_server/ 
│       │   └── hotel_server.py 
│       ├── event_server/ 
│       │   └── event_server.py 
│       ├── geocoder_server/ 
│       │   └── geocoder_server.py 
│       ├── weather_server/ 
│       │   └── weather_server.py 
│       └── finance_server/ 
│           └── finance_server.py 
<br>
├── frontend/ 
│   ├── app.py           # Streamlit app 
│   ├── config.py       # MCP server configuration      
│   └── .env            # Environment variables (excluded from Git) 
│ 
├── .gitignore          # Ignored files like .env, __pycache__, etc. 
├── README.md           # Project documentation    
└── LICENSE             # MIT License 


---

## ⚙️ Installation

### 1. Clone the repository

git clone https://github.com/sushilparjapat/mcp-travel-agent.git
cd mcp-travel-agent/frontend

### 2 Create and activate a virtual environment for each server(backend) and frontend 
uv sync

### 3 Create a .env file inside your frontend folder:
OPENAI_API_KEY=your_openai_api_key_here
<br>
SERPAPI_KEY=your_serpapi_key_here

### 4 how to run 
streamlit run app.py
