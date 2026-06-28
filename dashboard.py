import streamlit as st
import sqlite3
import pandas as pd

st.set_page_config(
    page_title="Smart Focus Tracker",
    page_icon="🎯",
    layout="wide"
)

st.title("🎯 Smart Focus, Stress & Productivity Tracker")
st.markdown("---")

conn = sqlite3.connect("tracker.db")
df = pd.read_sql_query("SELECT * FROM sessions", conn)

if not df.empty:

    latest = df.iloc[-1]

    focus_time = latest["focus_time"]
    face_distractions = latest["distraction_count"]
    screen_distractions = latest["screen_distraction_count"]

    score = focus_time - (face_distractions * 5) - (screen_distractions * 5)

    if score < 0:
        score = 0

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("⏱ Focus Time", focus_time)
    col2.metric("🚨 Face Distractions", face_distractions)
    col3.metric("💻 Screen Distractions", screen_distractions)
    col4.metric("🎯 Productivity Score", score)

    st.markdown("---")

    st.subheader("📊 Focus Time Analysis")
    st.bar_chart(df["focus_time"])

    st.subheader("📉 Distraction Analysis")
    st.line_chart(df["distraction_count"])

    st.subheader("📋 Session History")
    st.dataframe(df, use_container_width=True)

else:
    st.warning("No session data available.")

conn.close()