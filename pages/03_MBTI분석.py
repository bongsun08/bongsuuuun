import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np

st.set_page_config(page_title="🌍 MBTI 국가별 비율 시각화", layout="centered")

st.title("🌍 국가별 MBTI 유형 비율 시각화")
st.markdown("""
MBTI 16유형이 전 세계 국가별로 어떤 비율을 보이는지 확인해보세요!  
선택한 국가의 **각 MBTI 유형 비율**이 막대그래프로 표시됩니다.
""")

# --- 파일 업로드 ---
uploaded_file = st.file_uploader("📂 MBTI 국가별 데이터 파일 업로드 (countriesMBTI_16types.csv)", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)

    # 국가 목록
    countries = df["Country"].unique()
    selected_country = st.selectbox("🌎 국가를 선택하세요", countries)

    # 선택한 국가의 데이터
    country_data = df[df["Country"] == selected_country].iloc[0, 1:]  # Country 열 제외
    mbti_types = country_data.index.tolist()
    mbti_values = country_data.values

    # 데이터프레임으로 정리
    plot_df = pd.DataFrame({
        "MBTI 유형": mbti_types,
        "비율": mbti_values
    }).sort_values(by="비율", ascending=False)

    # 색상 처리 (1등=빨강, 나머지=파란색 그라데이션)
    top_color = 'red'
    n = len(plot_df)
    gradient_colors = px.colors.sequential.Blues[::-1]  # 파란색 계열 그라데이션
    color_scale = [gradient_colors[int(i * (len(gradient_colors)-1) / (n-1))] for i in range(n)]
    colors = [top_color] + color_scale[1:]

    # Plotly 막대 그래프
    fig = px.bar(
        plot_df,
        x="MBTI 유형",
        y="비율",
        text="비율",
        color=plot_df["MBTI 유형"],
        color_discrete_sequence=colors,
    )

    fig.update_traces(texttemplate="%{text:.2%}", textposition="outside")
    fig.update_layout(
        title=f"🇨🇴 {selected_country}의 MBTI 유형 비율",
        xaxis_title="MBTI 유형",
        yaxis_title="비율 (비중)",
        showlegend=False,
        plot_bgcolor="white",
        yaxis=dict(tickformat=".0%"),
    )

    st.plotly_chart(fig, use_container_width=True)

else:
    st.info("CSV 파일을 업로드하면 시각화를 시작할 수 있습니다. 😊")
