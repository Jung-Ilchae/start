
import streamlit as st
from langchain_google_genai import GoogleGenerativeAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
import os

# 페이지 제목 설정
st.title("6하원칙 작문 생성기")

# API 키 입력 섹션
api_key = st.text_input("Google API 키를 입력하세요", type="password")

if api_key:
    os.environ["GOOGLE_API_KEY"] = api_key
    
    # 6하원칙 입력 필드
    who = st.text_input("누가 (Who)")
    what = st.text_input("무엇을 (What)")
    when = st.text_input("언제 (When)")
    where = st.text_input("어디서 (Where)")
    why = st.text_input("왜 (Why)")
    how = st.text_input("어떻게 (How)")

    # 생성 버튼
    if st.button("작문 생성"):
        if who and what and when and where and why and how:
            try:
                # Gemini 모델 초기화
                llm = GoogleGenerativeAI(model="gemini-1.0-pro")
                
                # 프롬프트 템플릿 설정
                template = """
                다음의 6하원칙을 바탕으로 자연스러운 글을 작성해주세요:
                
                누가: {who}
                무엇을: {what}
                언제: {when}
                어디서: {where}
                왜: {why}
                어떻게: {how}
                
                위 정보를 바탕으로 300자 내외의 자연스러운 글을 작성해주세요.
                """
                
                prompt = PromptTemplate(
                    input_variables=["who", "what", "when", "where", "why", "how"],
                    template=template
                )
                
                # LLMChain 생성 및 실행
                chain = LLMChain(llm=llm, prompt=prompt)
                result = chain.run({
                    "who": who,
                    "what": what,
                    "when": when,
                    "where": where,
                    "why": why,
                    "how": how
                })
                
                # 결과 출력
                st.subheader("생성된 작문:")
                st.write(result)
                
            except Exception as e:
                st.error(f"오류가 발생했습니다: {str(e)}")
        else:
            st.warning("모든 항목을 입력해주세요.")
else:
    st.warning("API 키를 입력해주세요.")