## Importing Dependencies
import os
from apikey import apikey

import streamlit as st
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain, SequentialChain
from langchain.memory import ConversationBufferMemory
from langchain.utilities import WikipediaAPIWrapper
os.environ['OPENAI_API_KEY'] = apikey

## Streamlit App
st.set_page_config(page_title='YouTube Title and Script Generator', page_icon="🦜")
st.title("🦜🔗 YouTube Title and Script Generator")
prompt = st.text_input("Enter Your Prompt Here:")

## Title template
title_template = PromptTemplate(
    input_variables = ['topic'],
    template = 'write me a youtube video title about {topic}'
    
)

## Script template
script_template = PromptTemplate(
    input_variables = ['title','wikipedia_research'],
    template = 'write me a youtube video script based on this title TITLE: {title} while leveraging the following research: {wikipedia_research}'  
)

## Memory to store conversation history
title_memory = ConversationBufferMemory(input_key='topic',memory_key='chat_history')
script_memory = ConversationBufferMemory(input_key='title',memory_key='chat_history')

## LLMS
llm = OpenAI(temperature=0.9)
title_chain = LLMChain(llm=llm, prompt = title_template, verbose=True, output_key='title',memory=title_memory)
script_chain = LLMChain(llm=llm, prompt = script_template, verbose=True, output_key='script',memory=script_memory)
# ## Using SequentialChain to run both chains in sequence
# sequential_chain = SequentialChain(chains=[title_chain, script_chain],input_variables=['topic'],
#                                    output_variables=['title','script'],verbose=True)

wiki = WikipediaAPIWrapper()
## Generating Text if Prompt is Provided
if prompt:
    # response = sequential_chain({'topic':prompt})
    title = title_chain.run(prompt)
    wiki_research = wiki.run(prompt)
    script = script_chain.run(title=title,wikipedia_research=wiki_research)
    st.write(title)
    st.write(script)
    with st.expander('Title History'):
        st.info(title.buffer)
    with st.expander('Script History'):
        st.info(script.buffer)
    with st.expander('Wikipedia Research History'):
        st.info(wiki_research)