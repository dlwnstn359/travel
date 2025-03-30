import streamlit as st
import folium
from streamlit_folium import folium_static
import pandas as pd
st.title("4코스")
st.subheader("🌎 여행 코스 지도")
m = folium.Map(location=[37.5972, 127.0520], zoom_start=11)
locations = {
    "경희대학교": [37.5972, 127.0520],
    "광장시장": [37.5701, 126.9997],

}

#마커 추가
for name, coords in locations.items():
    folium.Marker(coords, tooltip=name, popup=name).add_to(m)

#지도 표시
folium_static(m)

#✅ 여행 일정 요약
st.subheader("📅 주요 일정")
schedule = pd.DataFrame({
    "시간": ["08:40", "09:30~11:00", "11:00~13:00", "13:00~16:00", "16:30~17:30"],
    "장소": ["출발", "경희대 탐방", "광장 시장", "국립중앙박물관", "석식"],
    "설명": [
        "",
        "경희대 캠퍼스 투어 예약",
        "중식(개별 부담)",
        "그룹별 탐방",
        "애슐리(한강공원 지점)",
    ]
})
st.dataframe(schedule, hide_index=True)


st.subheader("경희대")
st.image("경희대.jpg")
st.write("🎒경희대학교는 예쁘기로 인기있는 캠퍼스 건축물과 학생들에게 다양한 교육을 재공해주는 교육기관입니다.")
st.subheader("광장 시장")
st.image("광장시장.png")
st.write("🎒광장시장은 대한민국 최초의 전통 거래시장으로 음식과 전통 먹거리 문화로 유명하여 다채로운 한식이 존재하는 시장입니다.")
st.subheader("국립중앙박물관")
st.image("국립중앙박물관.png")
st.write("🎒국립 중앙 박물관은 한국에 존재하는 가장 큰 국립 박물관으로 다양한 유물과 예술품을 전시해두었으며 관광객들에게 다양한 역사적 지식을 전해주는 공간입니다.")




restaurants = pd.DataFrame({
    "맛집 이름": ["박가네 빈대떡", "형제육회 본점", "원조누드치즈김밥"],
    "주요 메뉴": ["박가네삼합, 마약김밥, 모듬전", "육회, 육회비빔밥", "치즈참치김밥, 세트김밥"],
    "링크":[ 
        "[박가네 빈대떡](https://naver.me/FDnCdFbP)",
        "[형제육회 본점](https://naver.me/GeUR3WGZ)",
        "[원조누드치즈김밥](https://naver.me/xDJucSNM)",
    ]
})

st.title("📍 광장시장 맛집 추천")


st.table(restaurants)
