import streamlit as st
import folium
from streamlit_folium import folium_static
import pandas as pd
import sqlite3





# 데이터베이스 연결 함수
def save_message(sender, message):
    conn = sqlite3.connect('messages.db')  # 데이터베이스 연결
    c = conn.cursor()
    
    # 새로운 메시지 저장
    c.execute("INSERT INTO messages (sender, message) VALUES (?, ?)", (sender, message))
    
    conn.commit()  # 변경 사항 저장
    conn.close()  # 연결 종료

# 게시글 조회 함수
def load_messages():
    conn = sqlite3.connect('messages.db')  # 데이터베이스 연결
    c = conn.cursor()
    
    # 모든 메시지 가져오기
    c.execute("SELECT * FROM messages")
    messages = c.fetchall()  # 결과를 모두 가져오기
    
    conn.close()  # 연결 종료
    return messages

# 데이터베이스 초기화 (테이블이 없으면 생성)
def initialize_db():
    conn = sqlite3.connect('messages.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS messages (
            sender TEXT,
            message TEXT
        )
    ''')
    conn.commit()
    conn.close()

# Streamlit UI 설정
st.title("📢 학부모 및 학생 게시판")

# 데이터베이스 초기화
initialize_db()

# 선생님 메시지 작성
st.subheader("✏️ 선생님 메시지 작성")
message = st.text_area("게시판에 남길 메시지를 입력하세요")

# 메시지 게시 버튼
if st.button("게시하기"):
    if message:
        save_message("선생님", message)  # 데이터베이스에 저장
        st.success("✅ 메시지가 게시되었습니다!")
    else:
        st.warning("⚠️ 메시지를 입력하세요.")

# 게시판 읽기
st.subheader("📜 전체 게시판")
messages = load_messages()

# 게시글을 표 형태로 출력
if messages:
    for sender, msg in messages:
        st.write(f"**{sender}:** {msg}")
else:
    st.info("아직 게시된 메시지가 없습니다.")

