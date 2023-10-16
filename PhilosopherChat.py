#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import openai
import streamlit as st
from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage, SystemMessage

# 공통 API 키
api_key = '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'

# 사용 가능한 철학자와 대화 프롬프트 목록
philosophers = {
    "소크라테스": "소크라테스가 말하듯이 대답해주세요",
    "니체": "니체가 말하듯이 대답해주세요",
    "칸트": "칸트가 말하듯이 대답해주세요"
}

len_select = {"짧은 답변 📑":100, "긴 답변 📜":300}

#서비스 제목
st.title('🧔📚 철학자와 대화하기')

# 사용자 선택에 따라 프롬프트 설정
selected_philosopher = st.radio("👨‍🏫 철학자 선택:", list(philosophers.keys()))
selected_prompt = philosophers[selected_philosopher]

# 답변 길이 설정 버튼
# 답변 길이에 따라 max_tokens 설정
selected_len = st.radio("🗣️ 답변 길이:", list(len_select.keys()))
max_tokens = len_select[selected_len]

# ChatOpenAI 챗봇 모델 생성
chat = ChatOpenAI(
    temperature=0.7,
    model_name="gpt-3.5-turbo",
    openai_api_key=api_key
)


def send_click(chat, prompt):
    messages = [
        SystemMessage(content='I want you to act as a philosophy teacher.'),
        HumanMessage(content=prompt)
    ]
    response = chat(messages).content
    return response

def main():
    # 사용자 입력을 받는 텍스트 입력 위젯 생성
    user_input = st.text_input("철학자와 대화를 시작해보세요: ", key='prompt')
    
    # 선택한 철학자 버튼을 누를 때만 대화 시작
    if st.button("선택한 철학자와 대화 시작"):
        response = send_click(chat, selected_prompt + " " + user_input+'를'+str(max_tokens)+'자로 말해주세요.')
        st.subheader(f"{selected_philosopher}: ")
        st.success(response, icon='🧔')

if __name__ == '__main__':
    main()


# In[ ]:




