# chatbot_basic

# Installation modules:


pip install streamlit transformers torch



# selection Model


Model Selection: The most important change is on line 5. I've switched the MODEL_NAME from "microsoft/DialoGPT-medium" to "google/gemma-2b-it". The "it" in the name stands for "instruction-tuned," which means it has been specifically trained to follow instructions and answer questions, making it much more suitable for your use case.

Input Formatting: The gemma model requires the entire chat history to be passed to it as a single, specially formatted tensor. I've updated the logic inside the if prompt := st.chat_input(...) block to build a full conversation history list and then use st.session_state.tokenizer.apply_chat_template() to format it correctly for the model. This is the new standard for modern conversational models and makes the chatbot more robust.

Generation Parameters: I've also slightly adjusted the generate parameters (max_length, top_k, top_p, temperature) to values that are commonly used and work well with the gemma model.
🧠 Ollama-Powered Python Agent with Streamlit

This project is a locally hosted AI agent built using 
, , and 

. It interprets natural language commands, generates Python code, and executes it live — all without needing an API key or internet access.
🚀 Features

    ✅ Local LLM (Mistral via Ollama)

    🧪 Python code execution using LangChain’s PythonREPLTool

    🧠 Agent reasoning with Thought → Action → Observation

    📚 Injected knowledge base for Indian state capitals

    🖥️ Streamlit UI with live agent feedback

    🔐 Fully offline — no external APIs required

📦 Requirements


pip install streamlit langchain langchain_experimental langchain_community


To pull the ollama model

curl -fsSL https://ollama.ai/install.sh | sh
ollama pull mistral


chatbot_basic/
├── agent_app.py         # Main Streamlit app
├── README.md            # Project documentation

Usuage

streamlit run agent_app.py



Streamlit learning 


Streamlit –usage 

Allows us to create data applications

1. Deploy a machine learning model

2. Deploy a dashboard

3. Share a data science project


Streamlit detects the changes and displays them on the browser → Make changes to your file 


With caching we can avoid running expensive code

→ @st.cache_data

1. Serializable objects
    -- Functions
    -- API calls
    -- Data frames

→ @st.cache_resource

	Unserializable objects
	-- ML Models
	-- Database Connections
Features of streamlit

1. Display text
2. Display plots
3. Interactivity (radio Buttons, check boxes, forms,sliders etc..)
4. Multi-page apps
5. Stateful apps
6. Data base connections



Default port for running the streamlit -- 8501



Basic headers usage

Title of the web app 

→ st.title(“first app”)

headers

→ st.header(“Basic hello world app”)

still requires any sub headers we can use the subheader

→ st.subheader(“Basic application for the hello world app”)


Let say if we want to have the more subheaders then we can go for the markdown option


→ st.markdown()


Caption :

→ st.caption()


→ Code implementation we can use  the st.code (“”’ import pandas as pd pd.read_csv
(my_csv_file)“””)


Text option 

→ st.text()


Latex :

let say if we want to add any kind of equation we can use the Latex method


→ st.latex()