import streamlit as st
import folium
from streamlit_folium import folium_static
st.title("1코스")

st.subheader("🌎 여행 코스 지도")

# 지도 생성
m = folium.Map(location=[37.5105, 127.0980], zoom_start=15)

# 예제 장소 데이터 (수정된 장소)
locations = {
    "인천차이나 타운": [37.4756, 126.6186],
    "인천항갑문홍보관": [37.4666, 126.6031],
    
}

# 마커 추가
for name, coords in locations.items():
    folium.Marker(coords, tooltip=name, popup=name).add_to(m)

# 지도 표시
folium_static(m)
