# app.py
import streamlit as st
from streamlit_folium import st_folium
import folium
from folium import features

st.set_page_config(page_title="Seoul Top10 (외국인 추천)", layout="wide")

st.title("🇰🇷 외국인이 사랑하는 서울 관광지 Top 10")
st.markdown(
    "아래 지도는 외국인들이 가장 많이 찾는 서울의 관광지 Top 10입니다. "
    "마커를 클릭하면 간단한 설명을 볼 수 있어요 💖"
)

# Top10 장소 데이터
places = [
    {"name": "경복궁 (Gyeongbokgung Palace)", "coords": (37.579617, 126.977041), "desc": "조선의 대표 궁궐 👑"},
    {"name": "창덕궁 (Changdeokgung Palace)", "coords": (37.582600, 126.991000), "desc": "비원으로 유명한 고궁 🍃"},
    {"name": "북촌한옥마을 (Bukchon Hanok Village)", "coords": (37.582542, 126.983047), "desc": "전통 한옥 골목길 🏠"},
    {"name": "인사동 (Insadong)", "coords": (37.576540, 126.985120), "desc": "전통 공예·차 카페 거리 🎎"},
    {"name": "명동 (Myeongdong)", "coords": (37.560988, 126.985385), "desc": "쇼핑·뷰티 천국 🛍️"},
    {"name": "N서울타워 (N Seoul Tower)", "coords": (37.551169, 126.988227), "desc": "서울 전망 명소 🌃"},
    {"name": "동대문디자인플라자 (DDP)", "coords": (37.566295, 127.009356), "desc": "야시장·전시·디자인 ✨"},
    {"name": "홍대 (Hongdae)", "coords": (37.556264, 126.923965), "desc": "젊음의 거리·공연 🎸"},
    {"name": "광장시장 (Gwangjang Market)", "coords": (37.570375, 126.999186), "desc": "전통 먹거리 시장 🍢"},
    {"name": "코엑스·스타필드 (COEX Mall)", "coords": (37.512050, 127.058647), "desc": "대형 쇼핑·도서관 📚"},
]

# 서울 중심 좌표
center = [37.5665, 126.9780]

# 지도 생성 (색상 없는 베이스)
m = folium.Map(location=center, zoom_start=12, tiles=None)

# 마커 추가 (핑크색)
for p in places:
    folium.Marker(
        location=p["coords"],
        popup=f"<b>{p['name']}</b><br>{p['desc']}",
        tooltip=p["name"],
        icon=folium.Icon(color="pink", icon="info-sign"),
    ).add_to(m)

# 지도 표시 (크기 70%로 축소)
st_folium(m, width=630, height=420)

# 관광지 요약 표 표시
st.markdown("### 📍 관광지 간단 요약")
for i, p in enumerate(places, start=1):
    st.write(f"{i}. **{p['name']}** — {p['desc']}")

st.caption("출처: TripAdvisor, VisitSeoul, Lonely Planet 등. (앱 목적: 정보 제공)")
