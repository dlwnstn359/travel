import streamlit as st
import folium
from streamlit_folium import folium_static
import pandas as pd
if st.button('The Easter Egg'):
    st.title("1코스")
    st.subheader("📅 주요 일정")
    schedule = pd.DataFrame({
    "시간": ["08:40", "10:00~11:00", "11:00~14:30", "14:30~16:00", "16:00~17:00","17:00~17:30"],
    "장소": ["출발", "인천항갑문홍보관", "인천 차이나타운&개항장", "식당", "석식","한강 유람선 탑승장으로 이동"],
    "설명": [
        "",
        "가이드 예약",
        "중식(개별 부담)",
        "",
        "애슐리(종각지점)",
        "서울"
    ]
    })
    st.dataframe(schedule, hide_index=True)
    st.subheader("📅 주요 일정")
    schedule = pd.DataFrame({
    "시간": ["08:40", "10:00~11:00", "11:00~14:30", "14:30~16:00", "16:00~17:00","17:00~17:30"],
    "장소": ["출발", "인천항갑문홍보관", "인천 차이나타운&개항장", "식당", "석식","한강 유람선 탑승장으로 이동"],
    "설명": [
        "",
        "가이드 예약",
        "중식(개별 부담)",
        "",
        "애슐리(종각지점)",
        "서울"
    ]
    })
    st.dataframe(schedule, hide_index=True)
    st.subheader("🌎 여행 코스 지도")
    m = folium.Map(location=[37.4756, 126.6186], zoom_start=11)
    locations = {
    "인천차이나 타운": [37.4756, 126.6186],
    "인천항갑문홍보관": [37.4666, 126.6031],
    }
    # 마커 추가
    for name, coords in locations.items():
    folium.Marker(coords, tooltip=name, popup=name).add_to(m)
    # 지도 표시
    folium_static(m)
    if st.button('장소 및 맛집 안내'):
    st.subheader("인천 갑문 홍보관")
    st.image("갑문홍보관.png")
    st.write("🎒인천항 갑문 홍보관은 인천항의 갑문 시스템과 항만 운영의 중요성을 알리기 위한 전시공간으로 갑문의 역할 작동원리 역사등을 다양한방법으로 설명하는 장소이다.")
    st.subheader("차이나 타운")
    st.image("차이나타운.png")
    st.write("🎒인천 차이나타운은 한국애서 가장 오래된 차이나타운으로 전통적인 중국 건축물과 다채로운 음식문화등을 즐길 수 있는 관광지이다.")








