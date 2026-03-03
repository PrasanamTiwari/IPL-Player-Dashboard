import pandas as pd

# ==========================================================
#                       LOAD DATASET
# ==========================================================

data = pd.read_csv("data/IPL_Ball_by_Ball_2008_2022.csv")


# ==========================================================
#                       BATTING SECTION
# ==========================================================

def get_player_stats(player_name):
    """
    Returns:
    total_matches, total_runs, batting_average, strike_rate
    """

    player_data = data[data['batter'] == player_name]

    if player_data.empty:
        return None

    total_runs = player_data['batsman_run'].sum()
    total_balls = player_data.shape[0]
    total_matches = player_data['ID'].nunique()

    batting_average = total_runs / total_matches if total_matches > 0 else 0
    strike_rate = (total_runs / total_balls) * 100 if total_balls > 0 else 0

    return total_matches, total_runs, batting_average, strike_rate


def runs_per_match(player_name):
    """
    Returns runs scored in each match
    """

    player_data = data[data['batter'] == player_name]

    if player_data.empty:
        return None

    runs_match = (
        player_data
        .groupby('ID')['batsman_run']
        .sum()
        .reset_index()
        .sort_values('ID')
    )

    runs_match['Match_No'] = range(1, len(runs_match) + 1)

    return runs_match


# ==========================================================
#                    BATTING FORM ANALYSIS
# ==========================================================

def get_last_5_matches(player_name):

    runs_match = runs_per_match(player_name)

    if runs_match is None:
        return None

    last5 = runs_match.tail(5)

    return last5[['ID', 'batsman_run']].rename(
        columns={'ID': 'Match ID', 'batsman_run': 'Runs Scored'}
    )


def get_form_analysis(player_name):

    last5 = get_last_5_matches(player_name)

    if last5 is None or last5.empty:
        return None

    avg_last5 = last5['Runs Scored'].mean()
    best_last5 = last5['Runs Scored'].max()

    if avg_last5 >= 50:
        rating = "🔥 Excellent Form"
    elif avg_last5 >= 30:
        rating = "⚖️ Good Form"
    elif avg_last5 >= 20:
        rating = "📉 Average Form"
    else:
        rating = "❄️ Poor Form"

    return avg_last5, best_last5, rating


# ==========================================================
#                       BOWLING SECTION
# ==========================================================

def get_bowling_stats(player_name):
    """
    Returns:
    total_matches, total_wickets, runs_conceded, economy
    """

    player_data = data[data['bowler'] == player_name]

    if player_data.empty:
        return None

    valid_dismissals = [
        "bowled",
        "caught",
        "lbw",
        "stumped",
        "caught and bowled"
    ]

    wickets_data = player_data[player_data['kind'].isin(valid_dismissals)]

    total_wickets = wickets_data.shape[0]
    total_runs_conceded = player_data['total_run'].sum()
    total_balls = player_data.shape[0]
    total_matches = player_data['ID'].nunique()

    economy = (total_runs_conceded / total_balls) * 6 if total_balls > 0 else 0

    return total_matches, total_wickets, total_runs_conceded, economy


# ==========================================================
#               WICKETS PER MATCH (0 INCLUDED)
# ==========================================================

def wickets_per_match(player_name):

    player_data = data[data['bowler'] == player_name]

    if player_data.empty:
        return None

    # All matches bowled
    all_matches = (
        player_data
        .groupby('ID')
        .size()
        .reset_index(name='balls')
        .sort_values('ID')
    )

    valid_dismissals = [
        "bowled",
        "caught",
        "lbw",
        "stumped",
        "caught and bowled"
    ]

    wickets_data = player_data[player_data['kind'].isin(valid_dismissals)]

    wickets_match = (
        wickets_data
        .groupby('ID')
        .size()
        .reset_index(name='wickets')
    )

    final_df = pd.merge(
        all_matches[['ID']],
        wickets_match,
        on='ID',
        how='left'
    )

    final_df['wickets'] = final_df['wickets'].fillna(0)

    final_df = final_df.sort_values('ID')
    final_df['Match_No'] = range(1, len(final_df) + 1)

    return final_df


# ==========================================================
#                    BOWLING FORM ANALYSIS
# ==========================================================

def get_last_5_bowling_matches(player_name):

    wickets_data = wickets_per_match(player_name)

    if wickets_data is None:
        return None

    last5 = wickets_data.tail(5)

    return last5[['ID', 'wickets']].rename(
        columns={'ID': 'Match ID', 'wickets': 'Wickets Taken'}
    )


def get_bowling_form(player_name):

    last5 = get_last_5_bowling_matches(player_name)

    if last5 is None or last5.empty:
        return None

    avg_wickets = last5['Wickets Taken'].mean()
    best_spell = last5['Wickets Taken'].max()

    # Realistic IPL thresholds
    if avg_wickets >= 2:
        rating = "🔥 Excellent Bowling Form"
    elif avg_wickets >= 1:
        rating = "⚖️ Good Bowling Form"
    elif avg_wickets >= 0.5:
        rating = "📉 Average Bowling Form"
    else:
        rating = "❄️ Poor Bowling Form"

    return avg_wickets, best_spell, rating