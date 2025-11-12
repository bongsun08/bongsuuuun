import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np

st.set_page_config(page_title="🌍 MBTI 국가/유형별 시각화", layout="centered")

st.title("🌍 MBTI 국가 및 유형별 시각화")
st.markdown("""
MBTI 16유형의 전 세계 분포를 한눈에 볼 수 있는 대시보드입니다.  
**탭을 전환**해 국가별 혹은 유형별 데이터를 확인해보세요.
""")

# --- 파일 업로드 ---
uploaded_file = st.file_uploader("📂 MBTI 국가별 데이터 파일 업로드 (countriesMBTI_16types.csv)", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)

    # Tabs
    tab1, tab2 = st.tabs(["🌎 국가별 보기", "💡 MBTI 유형별 보기"])

    # ==========================
    # 1️⃣ 국가별 보기
    # ==========================
    with tab1:
        countries = df["Country"].unique()
        selected_country = st.selectbox("🌍 국가를 선택하세요", countries)

        # 선택한 국가의 데이터
        country_data = df[df["Country"] == selected_country].iloc[0, 1:]
        mbti_types = country_data.index.tolist()
        mbti_values = country_data.values

        # 데이터프레임 구성
        plot_df = pd.DataFrame({
            "MBTI 유형": mbti_types,
            "비율": mbti_values
        }).sort_values(by="비율", ascending=False)

        # 색상 처리 (1등 빨강, 나머지는 파란색 그라데이션 반대: 진한 → 밝은)
        n = len(plot_df)
        gradient_colors = px.colors.sequential.Blues[::-1]  # 진한 파랑 → 밝은 파랑
        color_scale = [gradient_colors[int(i * (len(gradient_colors)-1) / (n-1))] for i in range(n)]
        colors = ["red" if i == 0 else color_scale[i] for i in range(n)]

        fig1 = px.bar(
            plot_df,
            x="MBTI 유형",
            y="비율",
            text="비율",
            color=plot_df["MBTI 유형"],
            color_discrete_sequence=colors,
        )

        fig1.update_traces(texttemplate="%{text:.2%}", textposition="outside")
        fig1.update_layout(
            title=f"🇨🇴 {selected_country}의 MBTI 유형 비율",
            xaxis_title="MBTI 유형",
            yaxis_title="비율 (비중)",
            showlegend=False,
            plot_bgcolor="white",
            yaxis=dict(tickformat=".0%"),
        )

        st.plotly_chart(fig1, use_container_width=True)

    # ==========================
    # 2️⃣ MBTI 유형별 보기
    # ==========================
    with tab2:
        mbti_columns = [col for col in df.columns if col != "Country"]
        selected_type = st.selectbox("💡 MBTI 유형을 선택하세요", mbti_columns)

        # 선택한 유형의 상위 10개국
        top_countries = df[["Country", selected_type]].sort_values(by=selected_type, ascending=False)

        # South Korea 포함 여부 확인
        if "South Korea" not in top_countries["Country"].head(10).values:
            top10 = pd.concat([
                top_countries.head(10),
                top_countries[top_countries["Country"] == "South Korea"]
            ])
        else:
            top10 = top_countries.head(10)

        # 색상 처리 (한국은 빨강, 나머지는 파란색 그라데이션 반대)
        n2 = len(top10)
        gradient_colors2 = px.colors.sequential.Blues[::-1]  # 진한 → 밝은
        color_scale2 = [gradient_colors2[int(i * (len(gradient_colors2)-1) / (n2-1))] for i in range(n2)]
        colors2 = [
            "red" if c == "South Korea" else color_scale2[i]
            for i, c in enumerate(top10["Country"])
        ]

        fig2 = px.bar(
            top10,
            x="Country",
            y=selected_type,
            text=selected_type,
            color="Country",
            color_discrete_sequence=colors2
        )

        fig2.update_traces(texttemplate="%{text:.2%}", textposition="outside")
        fig2.update_layout(
            title=f"💡 {selected_type} 유형 비율이 높은 상위 10개국 (+ South Korea 포함)",
            xaxis_title="국가",
            yaxis_title=f"{selected_type} 비율",
            showlegend=False,
            plot_bgcolor="white",
            yaxis=dict(tickformat=".0%"),
        )

        st.plotly_chart(fig2, use_container_width=True)

else:
    st.info("CSV 파일을 업로드하면 시각화를 시작할 수 있습니다. 😊")
