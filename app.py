import streamlit as st
import pandas as pd
import pickle

# Load the trained model
pipe = pickle.load(open("pipe.pkl", "rb"))

# Define IPL teams and host cities
teams = [
    "Chennai Super Kings",
    "Delhi Capitals",
    "Gujarat Titans",
    "Kolkata Knight Riders",
    "Lucknow Super Giants",
    "Mumbai Indians",
    "Punjab Kings",
    "Rajasthan Royals",
    "Royal Challengers Bangalore",
    "Sunrisers Hyderabad",
]

city = [
    "Bangalore", "Delhi", "Mumbai", "Kolkata", "Hyderabad", "Chennai",
    "Jaipur", "Cape Town", "Port Elizabeth", "Durban", "Centurion",
    "East London", "Johannesburg", "Kimberley", "Bloemfontein",
    "Ahmedabad", "Cuttack", "Nagpur", "Visakhapatnam", "Pune",
    "Raipur", "Ranchi", "Abu Dhabi", "Bengaluru", "Dubai",
    "Sharjah", "Navi Mumbai", "Chandigarh", "Lucknow", "Guwahati",
    "Dharamsala", "Mohali"
]

# App Title with Style
st.markdown(
    "<h1 style='text-align: center; color: #FF4B4B;'>🏏 IPL Win Probability Predictor</h1>",
    unsafe_allow_html=True,
)

# Layout for team selection
with st.container():
    st.subheader("🔍 Select Match Details")
    col1, col2 = st.columns(2)

    with col1:
        batting_team = st.selectbox("🏏 Select the Batting Team", sorted(teams))
    with col2:
        bowling_team = st.selectbox("🎯 Select the Bowling Team", sorted(teams))

    selected_city = st.selectbox("📍 Select the Host City", sorted(city))
    target = st.number_input("🎯 Enter the Target Score", min_value=1)

# Layout for match situation
with st.container():
    st.subheader("📊 Enter Current Match Situation")
    col3, col4, col5 = st.columns(3)

    with col3:
        score = st.number_input("🏏 Current Score", min_value=0, max_value=target)
    with col4:
        overs = st.number_input("⏳ Overs Completed", min_value=0.0, max_value=20.0, step=0.1)
    with col5:
        wickets = st.number_input("❌ Wickets Lost", min_value=0, max_value=10)

# Predict button
if st.button("🔮 Predict Probability"):
    if overs == 0:  # Avoid division by zero
        st.warning("Overs cannot be zero! Please enter a valid number of overs.")
    else:
        runs_left = target - score
        balls_left = 120 - (overs * 6)
        wickets_left = 10 - wickets
        crr = score / overs
        rrr = (runs_left * 6) / balls_left if balls_left > 0 else 0

        # Create input dataframe
        input_df = pd.DataFrame(
            {
                "batting_team": [batting_team],
                "bowling_team": [bowling_team],
                "city": [selected_city],
                "runs_left": [runs_left],
                "balls_left": [balls_left],
                "wickets_left": [wickets_left],
                "total_runs_x": [target],
                "crr": [crr],
                "rrr": [rrr],
            }
        )

        # Get prediction
        result = pipe.predict_proba(input_df)
        loss = result[0][0]
        win = result[0][1]

        # Display prediction
        st.markdown("---")
        st.markdown("<h2 style='text-align: center;'>📈 Win Probability</h2>", unsafe_allow_html=True)

        col6, col7 = st.columns(2)

        with col6:
            st.markdown(f"<h3 style='color: green;'>{batting_team} 🏆</h3>", unsafe_allow_html=True)
            st.metric("Win Probability", f"{round(win * 100)}%", delta=round(win * 100))
            st.progress(win)

        with col7:
            st.markdown(f"<h3 style='color: red;'>{bowling_team} 🎯</h3>", unsafe_allow_html=True)
            st.metric("Win Probability", f"{round(loss * 100)}%", delta=-round(loss * 100))
            st.progress(loss)


