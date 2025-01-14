# import streamlit as st

# import os
# import time
# import getpass

# from dotenv import load_dotenv
# from llm import get_ai_response


    

# st.set_page_config(page_title="부동산 챗봇", page_icon = '집')

# st.title("부동산 챗봇")
# st.caption("부동산 법에 근거하여 어떠한 내용이든 대답해 드립니다.")

# load_dotenv(dotenv_path = './api_key.env')

# if 'message_list' not in st.session_state:
#     st.session_state.message_list = []

# for message in st.session_state.message_list:
#     with st.chat_message(message["role"]):
#         st.write(message["content"])



# if user_question := st.chat_input(placeholder = "부동산과 관련된 궁금한 내용들을 말씀해주세요"):
#     with st.chat_message("user"):
#         st.write(user_question)
#     st.session_state.message_list.append({"role" : "user", "content": user_question})

#     with st.spinner("답변을 생성하는 중입니다"):
#         ai_response = get_ai_response(user_question)
    
#         with st.chat_message("ai"):
#           ai_message = st.write_stream(ai_response)
#           st.session_state.message_list.append({"role" : "ai", "content": ai_message})


import streamlit as st
import os
import time
from llm import get_ai_response

st.set_page_config(page_title="부동산 챗봇", page_icon='집')

st.title("부동산 챗봇")
st.caption("부동산 법에 근거하여 어떠한 내용이든 대답해 드립니다.")

# 'dotenv' 제거 후 secrets 사용
openai_api_key = st.secrets["OPENAI_API_KEY"]
pinecone_api_key = st.secrets["PINECONE_API_KEY"]

if 'message_list' not in st.session_state:
    st.session_state.message_list = []

for message in st.session_state.message_list:
    with st.chat_message(message["role"]):
        st.write(message["content"])

if user_question := st.chat_input(placeholder="부동산과 관련된 궁금한 내용들을 말씀해주세요"):
    with st.chat_message("user"):
        st.write(user_question)
    st.session_state.message_list.append({"role": "user", "content": user_question})

    with st.spinner("답변을 생성하는 중입니다"):
        ai_response = get_ai_response(user_question)
    
        with st.chat_message("ai"):
            ai_message = st.write_stream(ai_response)
            st.session_state.message_list.append({"role": "ai", "content": ai_message})

