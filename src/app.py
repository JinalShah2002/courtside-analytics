"""

@author: Jinal Shah

This file is the main web UI

"""
import streamlit as st
from agent import Agent
from guardrails import Guardrails

st.title('Courtside Analytics 🏀')
st.subheader('Unveiling NBA insights through AI.')

openai_api_key = st.sidebar.text_input('OpenAI API Key', type='password')

def generate_response(input_text):
    guardrails = Guardrails(api_key=openai_api_key)
    if guardrails.nbaQuestion(input_text):
        agent = Agent(api_key=openai_api_key,logging=True)
        st.info(agent.get_answer(input_text)['output'])
    else:
        st.error('Please enter a question related to the NBA!')

with st.form('my_form'):
    text = st.text_area('Enter text:', 'How does Anthony Edwards impact the Timberwolves points per game?')
    submitted = st.form_submit_button('Submit')
    if not openai_api_key.startswith('sk-'):
        st.warning('Please enter your OpenAI API key!', icon='⚠')
    if submitted and openai_api_key.startswith('sk-'):
        generate_response(text)