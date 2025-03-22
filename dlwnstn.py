import streamlit as st
import folium
from streamlit_folium import folium_static
import pandas as pd


# 페이지 설정
st.set_page_config(page_title="수학여행", page_icon="🌍", layout="wide")

# 스타일 적용
st.markdown(
    """
    <style>
        body {
            background-color: #f8f9fa;
        }
        .title {
            font-size: 36px;
            text-align: center;
            color: #4CAF50;
        }
        .sidebar .sidebar-content {
            background-color: #e3f2fd;
        }
        .stButton>button {
            background-color: #4CAF50;
            color: white;
            width: 100%;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

# 제목
st.markdown("<p class='title'>📍 수학여행 코스 안내</p>", unsafe_allow_html=True)

# 지도 생성
st.subheader("🌎 여행 코스 지도")
m = folium.Map(location=[37.5665, 126.9780], zoom_start=10)

# 예제 장소 데이터
locations = {
    "경복궁": [37.5796, 126.9770],
    "N서울타워": [37.5512, 126.9882],
    "롯데월드": [37.5112, 127.0980]
}

for name, coords in locations.items():
    folium.Marker(coords, tooltip=name, popup=name).add_to(m)

# 지도 표시
folium_static(m)

st.subheader("📅 주요 일정")
schedule = pd.DataFrame({
"시간": ["08:00", "10:00", "12:30", "15:00", "18:00"],
"장소": ["학교 출발", "박물관 탐방", "점심 식사", "유적지 방문", "숙소 도착"],
"설명": [
    "학교에서 버스를 타고 출발",
    "역사적인 박물관에서 투어 진행",
    "맛집에서 점심 식사",
    "유명한 유적지를 탐방",
    "숙소에서 휴식 및 자유 시간"
        ]
    })
    st.dataframe(schedule, hide_index=True)



