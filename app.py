import streamlit as st
import plotly.express as px
from analysis import *

st.set_page_config(page_title="IPL Player Dashboard", layout="wide")

st.title("🏏 IPL Player Performance Dashboard")

player_name = st.text_input("Enter Player Name (Example: V Kohli)")

if player_name:

    # ==========================================================
    #                       BATTING SECTION
    # ==========================================================

    stats = get_player_stats(player_name)

    if stats:
        total_matches, total_runs, average, strike_rate = stats

        st.subheader("📊 Batting Statistics")

        col1, col2, col3, col4 = st.columns(4)
        col1.metric("Matches Played", total_matches)
        col2.metric("Total Runs", total_runs)
        col3.metric("Batting Average", f"{average:.2f}")
        col4.metric("Strike Rate", f"{strike_rate:.2f}")

        st.subheader("📈 Runs Per Match")

        runs_data = runs_per_match(player_name)

        if runs_data is not None:
            fig = px.line(
                runs_data,
                x="Match_No",
                y="batsman_run",
                markers=True,
                hover_data=["ID"]
            )
            st.plotly_chart(fig, use_container_width=True)

        st.subheader("🔥 Batting Form Analysis")

        last5 = get_last_5_matches(player_name)
        if last5 is not None:
            st.dataframe(last5, use_container_width=True)

        form = get_form_analysis(player_name)
        if form:
            avg_last5, best_last5, rating = form
            st.write(f"Average (Last 5): **{avg_last5:.2f}**")
            st.write(f"Best Score (Last 5): **{best_last5}**")
            st.write(f"Form Rating: **{rating}**")

    # ==========================================================
    #                       BOWLING SECTION
    # ==========================================================

    bowling = get_bowling_stats(player_name)

    if bowling:
        matches, wickets, runs_conceded, economy = bowling

        st.subheader("🎯 Bowling Statistics")

        col1, col2, col3, col4 = st.columns(4)
        col1.metric("Matches Played", matches)
        col2.metric("Total Wickets", wickets)
        col3.metric("Runs Conceded", runs_conceded)
        col4.metric("Economy Rate", f"{economy:.2f}")

        st.subheader("📊 Wickets Per Match")

        wickets_data = wickets_per_match(player_name)
        if wickets_data is not None:
            fig2 = px.bar(
                wickets_data,
                x="Match_No",
                y="wickets",
                hover_data=["ID"]
            )
            st.plotly_chart(fig2, use_container_width=True)

        st.subheader("🔥 Bowling Form Analysis")

        last5_bowl = get_last_5_bowling_matches(player_name)
        if last5_bowl is not None:
            st.dataframe(last5_bowl, use_container_width=True)

        bowling_form = get_bowling_form(player_name)
        if bowling_form:
            avg_wkts, best_spell, rating = bowling_form
            st.write(f"Average Wickets (Last 5): **{avg_wkts:.2f}**")
            st.write(f"Best Spell (Last 5): **{best_spell} wickets**")
            st.write(f"Bowling Form Rating: **{rating}**")

    if not stats and not bowling:
        st.error("Player not found.")