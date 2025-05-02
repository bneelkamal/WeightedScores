# pages/3_Machine_Learning.py
import streamlit as st
import pandas as pd
import utils # Your shared utility functions

# --- Page Configuration and Title ---
st.title("Machine Learning - Weighted Score Calculator")

# --- Evaluation Breakdown Display (Modified) ---
st.subheader("Evaluation Breakdown - Machine Learning")
# Display the final components and their weights, showing assignments separately
eval_data = {
    "Component": [
        "Assignment 1",         # Changed
        "Assignment 2",         # Changed
        "Quizzes (Combined)",
        "Major Examination",
        "Total"
    ],
    "Weightage": ["12.5%", "12.5%", "25%", "50%", "100%"] # Changed weights
}
st.table(pd.DataFrame(eval_data))

# --- Maximum Marks Information ---
# Display the fixed maximum marks for each individual input component (remains the same)
st.write("### Maximum Marks for Each Input Component")
st.write("- Assignment 1: 50")
st.write("- Assignment 2: 100")
st.write("- Quiz 1: 20")
st.write("- Quiz 2: 20")
st.write("- Quiz 3: 20")
st.write("- Major Examination: 100")

# --- Score Input Fields ---
# (Remain the same)
st.subheader("Enter Your Scores")
a1_score = st.number_input("Assignment 1 Score", min_value=0.0, max_value=50.0, value=0.0, step=0.1, key="ml_a1")
a2_score = st.number_input("Assignment 2 Score", min_value=0.0, max_value=100.0, value=0.0, step=0.1, key="ml_a2")

q1_score = st.number_input("Quiz 1 Score", min_value=0.0, max_value=20.0, value=0.0, step=0.1, key="ml_q1")
q2_score = st.number_input("Quiz 2 Score", min_value=0.0, max_value=20.0, value=0.0, step=0.1, key="ml_q2")
q3_score = st.number_input("Quiz 3 Score", min_value=0.0, max_value=20.0, value=0.0, step=0.1, key="ml_q3")

major_score = st.number_input("Major Examination Score", min_value=0.0, max_value=100.0, value=0.0, step=0.1, key="ml_major")

# --- Calculation Function (Modified) ---
def calculate_ml_score_and_table(a1_score, a2_score, q1_score, q2_score, q3_score, major_score):
    """
    Calculates the weighted score for Machine Learning based on fixed max marks
    and specified weights, treating assignments individually.
    """
    # Define weights (modified for individual assignments)
    weight_a1 = 0.125         # 12.5%
    weight_a2 = 0.125         # 12.5%
    weight_quizzes = 0.25     # 25%
    weight_major = 0.50       # 50%

    # Define fixed maximum marks
    max_a1 = 50.0
    max_a2 = 100.0
    max_q1 = 20.0
    max_q2 = 20.0
    max_q3 = 20.0
    max_major = 100.0

    # --- Assignment Calculations (Individual) ---
    a1_perc = (a1_score / max_a1) * 100 if max_a1 > 0 else 0
    a2_perc = (a2_score / max_a2) * 100 if max_a2 > 0 else 0
    weighted_a1 = a1_perc * weight_a1
    weighted_a2 = a2_perc * weight_a2

    # --- Quiz Calculation (Combined) ---
    combined_quiz_score = q1_score + q2_score + q3_score
    combined_quiz_max = max_q1 + max_q2 + max_q3 # 60
    quiz_perc = (combined_quiz_score / combined_quiz_max) * 100 if combined_quiz_max > 0 else 0
    weighted_quizzes = quiz_perc * weight_quizzes

    # --- Major Exam Calculation ---
    major_perc = (major_score / max_major) * 100 if max_major > 0 else 0
    weighted_major = major_perc * weight_major

    # Calculate final total score by summing individual weighted contributions
    total_weighted_score = weighted_a1 + weighted_a2 + weighted_quizzes + weighted_major

    # Prepare data for the summary table (modified for individual assignments)
    summary_data = [
        {
            "Component": "Assignment 1", # Changed
            "Score": f"{a1_score:.2f}/{max_a1:.0f}", # Changed
            "Percentage": f"{a1_perc:.2f}%", # Changed
            "Weight": f"{weight_a1*100:.1f}%", # Changed (using .1f for 12.5%)
            "Weighted Contribution": f"{weighted_a1:.2f}" # Changed
        },
        {
            "Component": "Assignment 2", # Changed
            "Score": f"{a2_score:.2f}/{max_a2:.0f}", # Changed
            "Percentage": f"{a2_perc:.2f}%", # Changed
            "Weight": f"{weight_a2*100:.1f}%", # Changed
            "Weighted Contribution": f"{weighted_a2:.2f}" # Changed
        },
        {
            "Component": "Quizzes (Combined)",
            "Score": f"{combined_quiz_score:.2f}/{combined_quiz_max:.0f}",
            "Percentage": f"{quiz_perc:.2f}%",
            "Weight": f"{int(weight_quizzes*100)}%",
            "Weighted Contribution": f"{weighted_quizzes:.2f}"
        },
        {
            "Component": "Major Examination",
            "Score": f"{major_score:.2f}/{max_major:.0f}",
            "Percentage": f"{major_perc:.2f}%",
            "Weight": f"{int(weight_major*100)}%",
            "Weighted Contribution": f"{weighted_major:.2f}"
        }
    ]
    return total_weighted_score, pd.DataFrame(summary_data)

# --- Calculation Button and Results Display ---
# (Remains the same)
if st.button("Calculate Weighted Score - Machine Learning"):
    total_score, summary_df = calculate_ml_score_and_table(
        a1_score, a2_score,
        q1_score, q2_score, q3_score,
        major_score
    )

    st.success(f"Your weighted total score for Machine Learning is: {total_score:.2f}")
    st.subheader("Summary Table")
    st.table(summary_df)
    st.markdown(f"**Final Weighted Score:** {total_score:.2f}")

    message = utils.get_encouraging_message(total_score)
    st.info(message)
    st.markdown(f"### Quote of the Day:\n> {utils.get_random_motivational_quote()}")
