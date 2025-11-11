# app.py
import streamlit as st
from streamlit_folium import st_folium
import folium

st.set_page_config(page_title="Seoul Top10 (외국인 추천) — Folium Map", layout="wide")

st.title("🇰🇷 Seoul Top 10 관광지 (외국인 선호) — 지도 표시")
st.markdown(
    "아래 지도는 외국인들이 좋아하는 서울의 주요 관광지 Top 10을 Folium으로 표시한 것입니다. "
    "마커를 클릭하면 간단한 설명을 볼 수 있어요. (출처: TripAdvisor, VisitSeoul, Lonely Planet)"
)

# Top10 장소와 좌표(대략 위치)
places = [
    {
        "name": "Gyeongbokgung Palace (경복궁)",
        "coords": (37.579617, 126.977041),
        "desc": "조선의 대표 궁궐 — 한복 체험 추천 👑"
    },
    {
        "name": "Changdeokgung Palace (창덕궁)",
        "coords": (37.582600, 126.991000),
        "desc": "후원(비원)으로 유명한 고궁 🍃"
    },
    {
        "name": "Bukchon Hanok Village (북촌한옥마을)",
        "coords": (37.582542, 126.983047),
        "desc": "전통 한옥 사이 골목 산책 🏠"
    },
    {
        "name": "Insadong (인사동)",
        "coords": (37.576540, 126.985120),
        "desc": "전통 공예·차·기념품 거리 🎎"
    },
    {
        "name": "Myeongdong (명동)",
        "coords": (37.560988, 126.985385),
        "desc": "쇼핑·뷰티 천국 🛍️"
    },
    {
        "name": "N Seoul Tower (N서울타워, 남산)",
        "coords": (37.551169, 126.988227),
        "desc": "서울 전망과 야경 스팟 🌃"
    },
    {
        "name": "Dongdaemun Design Plaza (동대문DDP)",
        "coords": (37.566295, 127.009356),
        "desc": "미래적 건축과 밤시장 ✨"
    },
    {
        "name": "Hongdae (홍대)",
        "coords": (37.556264, 126.923965),
        "desc": "젊음의 거리·라이브 공연 🎸"
    },
    {
        "name": "Gwangjang Market (광장시장)",
        "coords": (37.570375, 126.999186),
        "desc": "한국 전통 먹거리의 천국 🍢"
    },
    {
        "name": "COEX Mall / Starfield Library (코엑스 / 스타필드)",
        "coords": (37.512050, 127.058647),
        "desc": "대형 쇼핑몰·포토 스팟 📚"
    },
]

# 초기 지도 중심 (서울 중심)
m = folium.Map(location=[37.5665, 126.9780], zoom_start=12, tiles="OpenStreetMap")

# 마커 추가
for p in places:
    folium.Marker(
        location=p["coords"],
        popup=f"<b>{p['name']}</b><br>{p['desc']}",
        tooltip=p["name"],
        icon=folium.Icon(color="blue", icon="info-sign"),
    ).add_to(m)

# 추가: CircleMarker로 시각 강조 (선택)
for p in places:
    folium.CircleMarker(
        location=p["coords"],
        radius=6,
        fill=True,
        fill_opacity=0.7
    ).add_to(m)

# Folium을 Streamlit에 표시
st.subheader("지도 (클릭해서 팝업 확인)")
map_data = st_folium(m, width=900, height=600)

# 사이드바: 장소 목록과 복사 가능한 코드 보기
st.sidebar.header("장소 목록 (Top 10)")
for i, p in enumerate(places, start=1):
    st.sidebar.write(f"{i}. {p['name']} — {p['desc']}")

st.sidebar.markdown("---")
st.sidebar.subheader("앱 소스코드 복사")
st.sidebar.markdown("아래 버튼으로 코드 블록을 복사하세요 (마우스로 드래그 후 복사 가능).")
with open(__file__, "r", encoding="utf-8") as f:
    code_text = f.read()
st.sidebar.code(code_text, language="python")

st.markdown("---")
st.caption("데이터 출처: TripAdvisor, VisitSeoul, Lonely Planet 등. (앱 목적: 정보 제공)")
