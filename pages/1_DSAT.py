import streamlit as st
import pandas as pd
import utils

def calculate_weighted_score_and_table(a1_score, a1_total, 
                                       a2_score, a2_total, 
                                       minor_score, minor_total, 
                                       major_score, major_total):
    # Define weights
    weights = {
        "Assignment 1": 0.15,
        "Assignment 2": 0.15,
        "Minor Exam": 0.25,
        "Major Exam": 0.45
    }
    # Calculate component percentages and weighted contributions
    data = []
    total = 0
    for name, score, total_marks, weight in zip(
        ["Assignment 1", "Assignment 2", "Minor Exam", "Major Exam"],
        [a1_score, a2_score, minor_score, major_score],
        [a1_total, a2_total, minor_total, major_total],
        [weights["Assignment 1"], weights["Assignment 2"], weights["Minor Exam"], weights["Major Exam"]]
    ):
        perc = (score / total_marks) * 100 if total_marks > 0 else 0
        weighted = perc * weight
        total += weighted
        data.append({
            "Component": name,
            "Score": f"{score:.2f}/{total_marks:.2f}",
            "Percentage": f"{perc:.2f}%",
            "Weight": f"{int(weight*100)}%",
            "Weighted Contribution": f"{weighted:.2f}"
        })
    return total, pd.DataFrame(data)


# --- Streamlit interface ---
st.title('T1 DSAT Weighted Score Calculator')

st.subheader('Evaluation Breakdown')
eval_data = {
    "Component": ["Assignment 1", "Assignment 2", "Minor Exam", "Major Exam", "Total"],
    "Weightage": ["15%", "15%", "25%", "45%", "100%"]
}
eval_df = pd.DataFrame(eval_data)
st.table(eval_df)

# User input
st.subheader('Enter Your Scores')

a1_total = st.number_input('Assignment 1 total marks', min_value=1.0, step=1.0, value=25.0)
a1_score = st.number_input('Assignment 1 score', min_value=0.0, max_value=a1_total, step=0.1, value=0.0, key='a1_score_input')

a2_total = st.number_input('Assignment 2 total marks', min_value=1.0, step=1.0, value=8.0)
a2_score = st.number_input('Assignment 2 score', min_value=0.0, max_value=a2_total, step=0.1, value=0.0, key='a2_score_input')

minor_total = st.number_input('Minor exam total marks', min_value=1.0, step=1.0, value=30.0)
minor_score = st.number_input('Minor exam score', min_value=0.0, max_value=minor_total, step=0.1, value=0.0, key='minor_score_input')

major_total = st.number_input('Major exam total marks', min_value=1.0, step=1.0, value=39.0)
major_score = st.number_input('Major exam score', min_value=0.0, max_value=major_total, step=0.1, value=0.0, key='major_score_input')

if st.button('Calculate Weighted Score'):
    total_score, summary_df = calculate_weighted_score_and_table(
        a1_score, a1_total,
        a2_score, a2_total,
        minor_score, minor_total,
        major_score, major_total
    )
    st.success(f'Your weighted total score is: {total_score:.2f}')
    st.subheader('Summary Table')
    st.table(summary_df)
    st.markdown(f"**Final Weighted Score:** {total_score:.2f}")
    message = utils.get_encouraging_message(total_score)
    st.info(message)
    st.markdown(f"### Quote of the Day:\n> {utils.get_random_motivational_quote()}")
