
import streamlit as st
from langchain_experimental.agents.agent_toolkits import create_python_agent
from langchain_experimental.tools.python.tool import PythonREPLTool
from langchain.llms import Ollama
from langchain_community.callbacks.streamlit import StreamlitCallbackHandler

# 🧠 Load local model via Ollama
llm = Ollama(model="mistral")

# 🛠️ Create Python agent
agent_executor = create_python_agent(
    llm=llm,
    tool=PythonREPLTool(),
    verbose=True,
    handle_parsing_errors=True
    
  # Optional but helpful
)

# 🎨 Streamlit UI
st.set_page_config(page_title="Local Python Agent", layout="centered")
st.title("🧠 Local Python Agent (No API Key)")

st.markdown("Enter a natural language command below. For example:")
st.markdown("- `Create a file named hello.txt and write 'Hi GOPAVARAPU'`")
st.markdown("- `Load the Iris dataset and split it for classification`")

user_input = st.text_area("🗣️ Your command:", height=100)

if st.button("Run Agent"):
    if user_input.strip():
        with st.spinner("🤖 Thinking..."):
            try:
                # 🧠 Create callback handler to stream thoughts/actions
                st_callback = StreamlitCallbackHandler(st.container())

                # 🧠 Run agent with callback
                result = agent_executor.invoke(
                    {"input": user_input},
                    {"callbacks": [st_callback]}
                )

                st.success("✅ Agent Response:")
                st.code(result["output"])
            except Exception as e:
                st.error(f"❌ Error: {str(e)}")
    else:
        st.warning("Please enter a command.")

