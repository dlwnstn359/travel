import streamlit as st
import folium
from streamlit_folium import folium_static
import pandas as pd
import sqlite3







# 데이터베이스 연결
conn = sqlite3.connect("messages.db")
cursor = conn.cursor()

# 메시지 테이블에서 모든 데이터 삭제
cursor.execute("DELETE FROM messages")

# 변경사항 저장 후 연결 종료
conn.commit()
conn.close()

print("메시지가 삭제되었습니다.")

