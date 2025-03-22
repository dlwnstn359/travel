import streamlit as st
import folium
from streamlit_folium import folium_static
st.title("2코스")

st.subheader("🌎 여행 코스 지도")

# 지도 생성
m = folium.Map(location=[37.4756, 126.6186], zoom_start=11)

# 예제 장소 데이터 (수정된 장소)
locations = {
    "인천차이나 타운": [37.4756, 126.6186],
    "센트럴파크": [37.3945, 126.6306],
    
}

# 마커 추가
for name, coords in locations.items():
    folium.Marker(coords, tooltip=name, popup=name).add_to(m)



# 지도 표시
folium_static(m)

✅ 여행 일정 요약
st.subheader("📅 주요 일정")
schedule = pd.DataFrame({
    "시간": ["08:40", "10:00~11:00", "11:00~14:30", "14:30~16:00", "16:00~17:00","17:00~17:30"],
    "장소": ["출발", "송도센트럴파크", "인천 차이나타운&개항장", "식당", "석식","한강 유람선 탑승장으로 이동"],
    "설명": [
        "",
        "그룹별 탐방",
        "중식(개별 부담)",
        "",
        "애슐리(종각지점)",
        "서울"
    ]
})
st.dataframe(schedule, hide_index=True)
