import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px

st.set_page_config(page_title="지하철 승하차 분석", layout="wide")

st.title("🚇 서울 지하철 승·하차 분석 (2025년 10월)")

# 데이터 불러오기 (CSV는 루트 폴더에 위치)
@st.cache_data
def load_data():
    return pd.read_csv("bongsuuun.csv", encoding="cp949")

df = load_data()

# 날짜 선택 (2025년 10월)
df['사용일자'] = df['사용일자'].astype(str)
unique_dates = sorted(df['사용일자'].unique())
unique_dates = [d for d in unique_dates if d.startswith("202510")]

selected_date = st.selectbox("📅 날짜 선택", unique_dates)

# 호선 선택
lines = sorted(df["노선명"].unique())
selected_line = st.selectbox("🚉 호선 선택", lines)

# 선택 필터 적용
filtered = df[(df["사용일자"] == selected_date) & (df["노선명"] == selected_line)].copy()

# 승하차 합계 계산
filtered["승하차합계"] = filtered["승차총승객수"] + filtered["하차총승객수"]

# 가장 큰 순서대로 정렬
filtered = filtered.sort_values("승하차합계", ascending=False)

# Plotly용 색상 생성
top_station = filtered.iloc[0]["역명"]

# 파란색 → 밝은 파란색 그라데이션
blue_colors = px.colors.sequential.Blues[::-1]  # 진한 → 옅은 순서로 변환

# 1등 빨간색 + 나머지 그라데이션 매핑
colors = ["red"] + blue_colors[: len(filtered) - 1]

# 그래프 생성
fig = go.Figure()

fig.add_trace(go.Bar(
    x=filtered["역명"],
    y=filtered["승하차합계"],
    marker=dict(color=colors),
    text=filtered["승하차합계"],
    textposition='outside'
))

fig.update_layout(
    title=f"📊 {selected_date} / {selected_line} 승·하차 합계 TOP 역",
    xaxis_title="역명",
    yaxis_title="승·하차 합계",
    template="plotly_white",
    height=600
)

st.plotly_chart(fig, use_container_width=True)

st.write("### 데이터 미리보기")
st.dataframe(filtered)
