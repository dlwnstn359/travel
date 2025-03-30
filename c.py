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

st.subheader("서울대학교")
st.image("서울대.jpg")
st.write("🎒서울대학교는 국내 최고로 불리는 명문대로 우수한 연구 역량과 교육 시스템과 역사, 전통을 자랑하는 교육기관입니다")
st.subheader("남대문 시장")
st.image("남대문시장.png")
st.write("🎒남대문 시장은 600년 이상 상업활동이 이어진 전통시장으로 다양한 상품과 음식점등이 혼합된 공간으로 도시의 발전과 변화를 상징하는 중요한 장소이기도 합니다.")

st.title("📍 남대문 시장 맛집 추천")


restaurants = pd.DataFrame({
    "맛집 이름": ["효담칼국수 닭한마리 명동본점", "가메골손왕만두 남대문본점"],
    "주요 메뉴": ["닭한마리 칼국수, 감자전, 효담 만두", "고기왕만두, 김치왕만두"],
    "링크":[ 
        "[효담 칼국수 닭한마리 명동본점](https://naver.me/GCvqNkCW)",
        "[가메골손왕만두 남대문본점](https://naver.me/x8tNnx6Y)",
    ]
})



st.table(restaurants)
st.subheader("효담칼국수 닭한마리 명동본점(닭반마리 칼국수)")
st.image("칼국수.jpg")
st.subheader("가메골손왕만두 남대문본점(고기왕만두)")
st.image("만두.jpg")
