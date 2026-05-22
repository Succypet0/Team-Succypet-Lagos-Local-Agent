import streamlit as st
import requests

st.set_page_config(page_title="Lagos Local Agent", layout="centered")
st.title("🇳🇬 Lagos Local: User Modeling & Recommendation Agent")

tab1, tab2 = st.tabs(["Task A: Review Simulator", "Task B: Smart Recommender"])

with tab1:
    st.subheader("Simulate a Local Review")
    
    persona_a = st.text_area("User Persona", placeholder="e.g., A 22-year-old student on a tight budget")
    product = st.text_input("Product Details", placeholder="e.g., A new fast-food burger joint in Yaba")
    
    if st.button("Generate Review"):
        with st.spinner("Agent is reasoning..."):
            payload = {"persona": persona_a, "product_details": product}
            
            response = requests.post("http://n8n:5678/webhook/test-a-simulate", json=payload)
            
            if response.status_code == 200:
                data = response.json()
                st.metric(label="Predicted Rating", value=f"{data.get('rating')} ⭐")
                st.info(data.get('review_text'))
            else:
                st.error("Backend orchestration failed.")

with tab2:
    st.subheader("Get a Contextual Recommendation")
    
    persona_b = st.text_area("User Persona / Context", placeholder="e.g., A tech bro who just moved to Lagos and doesn't know where to eat")
    
    if st.button("Get Recommendation"):
        with st.spinner("Analyzing constraints and ranking items..."):
            payload = {"persona": persona_b}
            
            response = requests.post("http://n8n:5678/webhook/task-b-review", json=payload)
            
            if response.status_code == 200:
                data = response.json()
                st.success(f"**Recommended:** {data.get('selected_item')}")
                st.write(f"**Agent Reasoning:** {data.get('reasoning')}")
            else:
                st.error("Backend orchestration failed.")