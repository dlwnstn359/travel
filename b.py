import streamlit as st
import folium
from streamlit_folium import folium_static
import pandas as pd


import streamlit as st
import pandas as pd
import os

# CSV 파일 경로 설정
CSV_FILE = "messages.csv"

# CSV 파일이 없으면 생성
if not os.path.exists(CSV_FILE):
    df = pd.DataFrame(columns=["보낸 사람", "메시지"])
    df.to_csv(CSV_FILE, index=False)

# 데이터 불러오기
def load_messages():
    return pd.read_csv(CSV_FILE)

# 데이터 저장하기
def save_message(sender, message):
    df = load_messages()
    new_entry = pd.DataFrame({"보낸 사람": [sender], "메시지": [message]})
    df = pd.concat([df, new_entry], ignore_index=True)
    df.to_csv(CSV_FILE, index=False)

# Streamlit UI
st.title("📢 학부모 및 학생 게시판")

# 선생님이 메시지를 입력하는 부분
st.subheader("✏️ 선생님 메시지 작성")
message = st.text_area("게시판에 남길 메시지를 입력하세요")
if st.button("게시하기"):
    if message:
        save_message("선생님", message)
        st.success("✅ 메시지가 게시되었습니다!")
        st.experimental_rerun()  # 새로고침하여 메시지 업데이트
    else:
        st.warning("⚠️ 메시지를 입력하세요.")

# 모든 사용자가 볼 수 있는 게시판
st.subheader("📜 전체 게시판")
df = load_messages()
if not df.empty:
    st.table(df)  # 게시글을 표 형태로 출력
else:
    st.info("아직 게시된 메시지가 없습니다.")

