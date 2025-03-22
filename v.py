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
    "시간": ["08:40", "10:00~11:00", "11:00~14:30", "14:30~16:00", "16:00~17:00","17:00~17:30"],
    "장소": ["출발", "경희대 탐방", "광장 시장", "국립중앙박물관", "석식",""],
    "설명": [
        "",
        "가이드 예약",
        "중식(개별 부담)",
        "",
        "애슐리(한강공원 지점)",
        "서울"
    ]
})
st.dataframe(schedule, hide_index=True)

