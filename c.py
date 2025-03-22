import streamlit as st
import pandas as pd
import folium
from streamlit_folium import folium_static
st.title("3코스")
m = folium.Map(location=[37.4581, 126.9522], zoom_start=11)
locations = {
    "서울대학교": [37.4581, 126.9522],
    "남대문 시장": [37.5588,  126.9781],
    "국립 중앙 박물관": [37.5235,  126.9803],

}


#마커 추가
for name, coords in locations.items():
    folium.Marker(coords, tooltip=name, popup=name).add_to(m)

#지도 표시
folium_static(m)

#✅ 여행 일정 요약
st.subheader("📅 주요 일정")
schedule = pd.DataFrame({
    "시간": ["08:40", "9:30 ~ 11:00", "11:00 ~ 13:00", "13:00 ~ 16:00", "16:30 ~ 17:30"],
    "장소": ["출발", "서울대 탐방", "남대문 시장", "국립중앙박물관", "석식"],
    "설명": [
        "",
        "본교 졸업생이 가이드",
        "중식(자유식 개별 부담) / 그룹별 탐방",
        "그룹별 탐방",
        "애슐리(한강공원 지점)"
    ]
})
st.dataframe(schedule, hide_index=True)
