import streamlit as st
import folium
from streamlit_folium import folium_static
import pandas as pd
import networkx as nx

# 페이지 설정
st.set_page_config(page_title="수학여행 코스 안내", page_icon="🌍", layout="wide")

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

# 여행 코스 추천
st.subheader("🎯 맞춤 여행 코스 추천")
data = {
    "코스명": ["경복궁 역사 탐방", "한강 자전거 투어", "남산 야경 투어", "에버랜드 놀이공원"],
    "유형": ["역사", "액티비티", "야경", "테마파크"]
}
df = pd.DataFrame(data)
selected_category = st.selectbox("유형 선택", df["유형"].unique())
filtered_df = df[df["유형"] == selected_category]
st.table(filtered_df)

# 최적 경로 탐색
st.subheader("🚀 최적 경로 찾기")
G = nx.Graph()
edges = [("경복궁", "N서울타워", 3), ("N서울타워", "롯데월드", 8), ("경복궁", "롯데월드", 12)]
G.add_weighted_edges_from(edges)
start = st.selectbox("출발지 선택", locations.keys())
end = st.selectbox("목적지 선택", locations.keys())
if st.button("최적 경로 계산"):
    path = nx.shortest_path(G, source=start, target=end, weight="weight")
    st.success(f"최적 경로: {' → '.join(path)}")
