# app.py
import streamlit as st
from streamlit_folium import st_folium
import folium

st.set_page_config(page_title="서울 여행 추천 지도", layout="wide")

# ------------------ 제목 & 설명 ------------------
st.title("🇰🇷 외국인이 사랑하는 서울 관광지 Top 10")
st.markdown(
    """
    서울을 처음 방문하는 사람들에게 추천하는 대표 관광 명소 💗  
    지도에서 마커를 클릭하면 간단한 설명과 가장 가까운 전철역 정보를 볼 수 있어요!
    """,
    unsafe_allow_html=True,
)

# ------------------ 관광지 데이터 ------------------
places = [
    {
        "name": "경복궁",
        "coords": (37.579617, 126.977041),
        "desc": "조선의 대표 궁궐로, 한복을 입고 사진 찍기 좋은 명소예요 👑",
        "subway": "🚇 3호선 경복궁역",
    },
    {
        "name": "창덕궁",
        "coords": (37.582600, 126.991000),
        "desc": "유네스코 세계문화유산으로 지정된 고궁이에요. 후원(비원)이 특히 유명해요 🍃",
        "subway": "🚇 3호선 안국역",
    },
    {
        "name": "북촌한옥마을",
        "coords": (37.582542, 126.983047),
        "desc": "전통 한옥이 모여 있는 아름다운 골목길로, 한복 체험도 가능해요 🏠",
        "subway": "🚇 3호선 안국역",
    },
    {
        "name": "인사동",
        "coords": (37.576540, 126.985120),
        "desc": "전통 찻집과 공예품 상점이 모여 있는 한국적인 거리 🎎",
        "subway": "🚇 3호선 안국역",
    },
    {
        "name": "명동",
        "coords": (37.560988, 126.985385),
        "desc": "쇼핑과 길거리 음식으로 유명한 활기찬 거리 🛍️",
        "subway": "🚇 4호선 명동역",
    },
    {
        "name": "N서울타워 (남산타워)",
        "coords": (37.551169, 126.988227),
        "desc": "서울의 전경을 한눈에 볼 수 있는 전망 명소 🌃",
        "subway": "🚇 4호선 명동역",
    },
    {
        "name": "동대문디자인플라자 (DDP)",
        "coords": (37.566295, 127.009356),
        "desc": "디자인, 전시, 야시장 등 현대적인 서울의 상징 ✨",
        "subway": "🚇 2·4·5호선 동대문역사문화공원역",
    },
    {
        "name": "홍대",
        "coords": (37.556264, 126.923965),
        "desc": "젊음의 거리! 버스킹과 예술적인 분위기가 가득해요 🎸",
        "subway": "🚇 2호선 홍대입구역",
    },
    {
        "name": "광장시장",
        "coords": (37.570375, 126.999186),
        "desc": "빈대떡, 마약김밥 등 한국 전통 먹거리의 천국 🍢",
        "subway": "🚇 1호선 종로5가역",
    },
    {
        "name": "코엑스·스타필드 도서관",
        "coords": (37.512050, 127.058647),
        "desc": "대형 쇼핑몰과 인스타 감성 도서관이 함께 있는 명소 📚",
        "subway": "🚇 2호선 삼성역",
    },
]

# ------------------ 지도 생성 ------------------
center = [37.5665, 126.9780]
m = folium.Map(location=center, zoom_start=12, tiles="OpenStreetMap")

# 핑크색 마커 표시
for p in places:
    popup_html = f"""
    <b>{p['name']}</b><br>
    {p['desc']}<br>
    {p['subway']}
    """
    folium.Marker(
        location=p["coords"],
        popup=popup_html,
        tooltip=p["name"],
        icon=folium.Icon(color="pink", icon="info-sign"),
    ).add_to(m)

# 지도 표시 (크기 70%)
st_folium(m, width=630, height=420)

# ------------------ 관광지 요약 ------------------
st.markdown("### 📍 관광지 요약")
for i, p in enumerate(places, start=1):
    st.write(f"{i}. **{p['name']}** — {p['desc']} ({p['subway']})")

# ------------------ 일정 추천 기능 ------------------
st.markdown("---")
st.markdown("## 🗓️ 나만의 서울 여행 일정 만들기")

day = st.selectbox("여행 일수를 선택하세요 👇", ["1일차", "2일차", "3일차"])

# 일정 추천 로직
if day == "1일차":
    st.success("✨ 1일차 추천 일정")
    st.write("1️⃣ 경복궁 → 2️⃣ 북촌한옥마을 → 3️⃣ 인사동 → 4️⃣ 명동 → 5️⃣ N서울타워")
elif day == "2일차":
    st.success("✨ 2일차 추천 일정")
    st.write("1️⃣ 동대문디자인플라자(DDP) → 2️⃣ 광장시장 → 3️⃣ 명동 → 4️⃣ 코엑스 → 5️⃣ N서울타워")
else:
    st.success("✨ 3일차 추천 일정")
    st.write("1️⃣ 경복궁 → 2️⃣ 창덕궁 → 3️⃣ 북촌한옥마을 → 4️⃣ 인사동 → 5️⃣ 홍대")

st.markdown("---")
st.caption("🗺️ 데이터 출처: TripAdvisor, VisitSeoul, Lonely Planet / 앱 목적: 관광 정보 제공용")
