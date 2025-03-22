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

# ✅ 날짜 선택 (Day 1, Day 2, Day 3)
selected_day = st.selectbox("🔎 날짜를 선택하세요", ["1일차", "2일차", "3일차"])

# ✅ 각 날짜별 일정 데이터
schedules = {
    "1일차": pd.DataFrame({
        "시간": ["06:30", "10:00", "12:30", "15:00", "18:00"],
        "장소": ["학교 출발", "박물관 탐방", "점심 식사", "유적지 방문", "숙소 도착"],
        "설명": [
            "학교에서 버스를 타고 출발",
            "역사적인 박물관에서 투어 진행",
            "맛집에서 점심 식사",
            "유명한 유적지를 탐방",
            "숙소에서 휴식 및 자유 시간"
        ]
    }),

    "2일차": pd.DataFrame({
        "시간": ["07:00", "09:30", "12:00", "14:30", "17:30"],
        "장소": ["아침 식사", "자연 체험 학습", "전통 시장 방문", "테마파크 탐방", "숙소 귀환"],
        "설명": [
            "숙소에서 아침 식사",
            "자연 속에서 체험 학습 진행",
            "전통 시장에서 문화 체험 및 점심",
            "놀이공원에서 자유 시간",
            "숙소에서 휴식 및 저녁 식사"
        ]
    }),

    "3일차": pd.DataFrame({
        "시간": ["07:30", "10:00", "12:00", "14:00", "16:30"],
        "장소": ["아침 식사", "기념품 쇼핑", "점심 식사", "공원 산책", "학교 복귀"],
        "설명": [
            "숙소에서 조식 후 체크아웃",
            "기념품 가게 방문 및 쇼핑",
            "현지 맛집에서 점심 식사",
            "공원에서 자유 산책 및 사진 촬영",
            "버스를 타고 학교로 출발"
        ]
    }),
}

# ✅ 선택한 날짜의 일정 표시
st.subheader(f"📅 {selected_day} 일정")
st.dataframe(schedules[selected_day], hide_index=True)


