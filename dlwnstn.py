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

# 🌟 제목 & 소개
st.title("🎒 수학여행 안내")
st.markdown("""  
수학여행 일정을 확인하고, 여행 코스와 정보를 볼 수 있습니다.  
사이드바에서 원하는 메뉴를 선택하세요! 🚀
""")

# 지도 생성
m = folium.Map(location=[37.5105, 127.0980], zoom_start=15)

# 예제 장소 데이터 (수정된 장소)
locations = {
    "롯데월드 아쿠아리움": [37.5115, 127.0980],
    "롯데월드 어드벤처": [37.5112, 127.0980],
    "국도호텔": [37.5100, 127.0965]
}

# 마커 추가
for name, coords in locations.items():
    folium.Marker(coords, tooltip=name, popup=name).add_to(m)

# 지도 표시
folium_static(m)

# ✅ 날짜 선택 (Day 1, Day 2, Day 3)
selected_day = st.selectbox("🔎 날짜를 선택하세요", ["1일차", "2일차", "3일차"])

# ✅ 각 날짜별 일정 데이터
schedules = {
    "1일차": pd.DataFrame({
        "시간": ["06:30", "07:00~", "11:00~12:00", "13:00~15:00", "15:00~21:00","21:30~","22:00~"],
        "일정": ["집합", "출발", "중식", "롯데월드 아쿠아리움", "롯데월드 어드벤처","숙소 체크인 및 휴식","취침"],
        "설명": [
            "",
            "휴게소 2번이용",
            "휴게소",
            "",
            "석식(밀쿠폰)",
            "서울",
            "",
        ]
    }),

    "2일차": pd.DataFrame({
        "시간": ["06:30", "07:00~08:20", "08:50~17:30", "17:30~18:30", "18:30~20:30","21:00~22:00","22:00~"],
        "일정": ["기상", "조식 및 출발", "선택행 체험", "학급별 단체사진", "한강 뮤직 크루즈","숙소 도착 후 휴식","취침"],
        "설명": [
            "",
            "조식",
            "중식(개별부담),석식(애슐리)",
            "배 타기 전 음식소화 시간",
            "19시 운항시작",
            "간식(치킨 3인 1개)",
            "",
        ]
    }),

    "3일차": pd.DataFrame({
        "시간": ["06:30", "07:00~09:20", "10:00~11:30", "11:30~13:00", "13:00~18:00"],
        "일정": ["기상", "조식 및 출발", "대학로 연극 관람", "중식", "부산행"],
        "설명": [
            "",
            "조식 및 카드키 반환",
            "옥탑방고양이(틴틴홀)",
            "중식(성균관번벤션홀)",
            "휴게소2번",
        ]
    }),
}

# ✅ 선택한 날짜의 일정 표시
st.subheader(f"📅 {selected_day} 일정")
st.dataframe(schedules[selected_day], hide_index=True)

# 🌟 추가 정보
st.markdown("""
---
📌 **이준수,강지원 만듬.**    
✅ **안전한 여행 되세요! 🚀**
""")

