import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# Streamlit Page Setup

st.set_page_config(page_title="Agriculture Dashboard", layout="wide")
st.title("🌾 India Agriculture Production Dashboard (50 Years)")

# Load CSV File

uploaded_file = st.sidebar.file_uploader("Upload the ICRISAT CSV file", type=["csv"])

if uploaded_file is None:
    st.warning(r"C:\Users\BaBuReDdI\Desktop\Data Science\Project\ICRISAT-District Level Data - ICRISAT-District Level Data.csv")
    st.stop()

df = pd.read_csv(uploaded_file)
df['Year'] = df['Year'].astype(int)

st.sidebar.success("File Loaded Successfully!")

# Show columns for debugging 
# st.write(df.columns.tolist())
# TAB SETUP

tab1, tab2, tab3, tab4 = st.tabs([
    "📊 Crop Production Overview",
    "📈 50-Year Trends",
    "🗺 State & District Insights",
    "⚡ Yield & Correlation"
])


# TAB 1 — CROP PRODUCTION OVERVIEW

with tab1:
    st.header("📊 Crop Production Overview")

    # Top 7 Rice
    st.subheader("Top 7 Rice Producing States")
    rice_state = df.groupby("State Name")['RICE PRODUCTION (1000 tons)'].sum().nlargest(7).reset_index()
    fig1 = px.bar(rice_state, x='State Name', y='RICE PRODUCTION (1000 tons)', color='State Name')
    st.plotly_chart(fig1, use_container_width=True)

    # Top 5 Wheat
    st.subheader("Top 5 Wheat Producing States")
    wheat_state = df.groupby("State Name")['WHEAT PRODUCTION (1000 tons)'].sum().nlargest(5).reset_index()
    col1, col2 = st.columns(2)

    fig2 = px.bar(wheat_state, x='State Name', y='WHEAT PRODUCTION (1000 tons)', color='State Name')
    col1.plotly_chart(fig2, use_container_width=True)

    fig2_pie = px.pie(wheat_state, names='State Name', values='WHEAT PRODUCTION (1000 tons)')
    col2.plotly_chart(fig2_pie, use_container_width=True)

    # Oilseeds
    st.subheader("Top 5 Oilseed Producing States")
    oil = df.groupby("State Name")['OILSEEDS PRODUCTION (1000 tons)'].sum().nlargest(5).reset_index()
    fig3 = px.bar(oil, x='State Name', y='OILSEEDS PRODUCTION (1000 tons)', color='State Name')
    st.plotly_chart(fig3, use_container_width=True)

    # Sunflower
    st.subheader("Top 7 Sunflower Producing States")
    sun = df.groupby("State Name")['SUNFLOWER PRODUCTION (1000 tons)'].sum().nlargest(7).reset_index()
    fig4 = px.bar(sun, x='State Name', y='SUNFLOWER PRODUCTION (1000 tons)', color='State Name')
    st.plotly_chart(fig4, use_container_width=True)


# TAB 2 — 50-YEAR TRENDS

with tab2:
    st.header("📈 50-Year Trend Analysis")

    # Sugarcane Trend
    st.subheader("Sugarcane Production in India (50 Years)")
    sugar = df.groupby("Year")['SUGARCANE PRODUCTION (1000 tons)'].sum().reset_index()
    fig5 = px.line(sugar, x="Year", y="SUGARCANE PRODUCTION (1000 tons)")
    st.plotly_chart(fig5, use_container_width=True)

    # Rice vs Wheat Trend
    st.subheader("Rice vs Wheat Production (50 Years)")
    rice_yearly = df.groupby("Year")['RICE PRODUCTION (1000 tons)'].sum().reset_index()
    wheat_yearly = df.groupby("Year")['WHEAT PRODUCTION (1000 tons)'].sum().reset_index()

    fig6 = go.Figure()
    fig6.add_trace(go.Scatter(x=rice_yearly['Year'], y=rice_yearly['RICE PRODUCTION (1000 tons)'], name="Rice"))
    fig6.add_trace(go.Scatter(x=wheat_yearly['Year'], y=wheat_yearly['WHEAT PRODUCTION (1000 tons)'], name="Wheat"))
    st.plotly_chart(fig6, use_container_width=True)

    # Millet (Maize)
    st.subheader("Millet (Maize) Production – 50 Years")
    millet = df.groupby("Year")['MAIZE PRODUCTION (1000 tons)'].sum().reset_index()
    fig9 = px.line(millet, x="Year", y="MAIZE PRODUCTION (1000 tons)")
    st.plotly_chart(fig9, use_container_width=True)


# TAB 3 — STATE & DISTRICT INSIGHTS

with tab3:
    st.header("🗺 State & District Insights")

    # West Bengal Rice
    st.subheader("West Bengal – Top 10 Rice Producing Districts")
    wb = df[df["State Name"] == "West Bengal"].groupby("Dist Name")['RICE PRODUCTION (1000 tons)'].sum().nlargest(10).reset_index()
    fig7 = px.bar(wb, x='Dist Name', y='RICE PRODUCTION (1000 tons)', color='Dist Name')
    st.plotly_chart(fig7, use_container_width=True)

    # Uttar Pradesh Wheat
    st.subheader("Uttar Pradesh – Top 10 Wheat Production Years")
    up = df[df["State Name"] == "Uttar Pradesh"].groupby("Year")['WHEAT PRODUCTION (1000 tons)'].sum().nlargest(10).reset_index()
    fig8 = px.bar(up, x='Year', y='WHEAT PRODUCTION (1000 tons)', color='Year')
    st.plotly_chart(fig8, use_container_width=True)

    # Groundnut
    st.subheader("Top 7 Groundnut Producing States")
    ground = df.groupby("State Name")['GROUNDNUT PRODUCTION (1000 tons)'].sum().nlargest(7).reset_index()
    fig11 = px.bar(ground, x='State Name', y='GROUNDNUT PRODUCTION (1000 tons)', color='State Name')
    st.plotly_chart(fig11, use_container_width=True)

    # Oilseeds Major States (Mean)
    st.subheader("Oilseed Production in Major States (Average)")
    oil_major = df.groupby("State Name")['OILSEEDS PRODUCTION (1000 tons)'].mean().nlargest(10).reset_index()
    fig13 = px.bar(oil_major, x='State Name', y='OILSEEDS PRODUCTION (1000 tons)', color='State Name')
    st.plotly_chart(fig13, use_container_width=True)


# TAB 4 — YIELD & CORRELATION

with tab4:
    st.header("⚡ Yield & Correlation Analysis")

    # Scatter: Area vs Production (Rice)
    st.subheader("Rice Area vs Production Relationship")
    fig14 = px.scatter(
        df,
        x='RICE AREA (1000 ha)',
        y='RICE PRODUCTION (1000 tons)',
        trendline='ols'
    )
    st.plotly_chart(fig14, use_container_width=True)

    # Yield Comparison
    st.subheader("Rice vs Wheat Yield Comparison (Across States)")
    yield_compare = df.groupby("State Name")[[
        'RICE YIELD (Kg per ha)', 'WHEAT YIELD (Kg per ha)'
    ]].mean().reset_index()

    fig15 = px.bar(
        yield_compare,
        x='State Name',
        y=['RICE YIELD (Kg per ha)', 'WHEAT YIELD (Kg per ha)'],
        barmode='group'
    )
    st.plotly_chart(fig15, use_container_width=True)
