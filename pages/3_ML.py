# pages/3_Machine_Learning.py
import streamlit as st
import pandas as pd
import utils # Your shared utility functions

# --- Page Configuration and Title ---
# Consider setting page_config only once in your main app file if needed globally
# st.set_page_config(page_title="ML - Weighted Score Calculator", layout="centered")
st.title("Machine Learning - Weighted Score Calculator")

# --- Evaluation Breakdown Display ---
st.subheader("Evaluation Breakdown - Machine Learning")
# Display the final components and their weights
eval_data = {
    "Component": [
        "Assignments (Combined)",
        "Quizzes (Combined)",
        "Major Examination",
        "Total"
    ],
    "Weightage": ["25%", "25%", "50%", "100%"]
}
st.table(pd.DataFrame(eval_data))

# --- Maximum Marks Information ---
# Display the fixed maximum marks for each individual input component
st.write("### Maximum Marks for Each Input Component")
st.write("- Assignment 1: 50")
st.write("- Assignment 2: 100")
st.write("- Quiz 1: 20")
st.write("- Quiz 2: 20")
st.write("- Quiz 3: 20")
st.write("- Major Examination: 100")

# --- Score Input Fields ---
st.subheader("Enter Your Scores")
# Use unique keys for each input widget
a1_score = st.number_input("Assignment 1 Score", min_value=0.0, max_value=50.0, value=0.0, step=0.1, key="ml_a1")
a2_score = st.number_input("Assignment 2 Score", min_value=0.0, max_value=100.0, value=0.0, step=0.1, key="ml_a2")

q1_score = st.number_input("Quiz 1 Score", min_value=0.0, max_value=20.0, value=0.0, step=0.1, key="ml_q1")
q2_score = st.number_input("Quiz 2 Score", min_value=0.0, max_value=20.0, value=0.0, step=0.1, key="ml_q2")
q3_score = st.number_input("Quiz 3 Score", min_value=0.0, max_value=20.0, value=0.0, step=0.1, key="ml_q3")

major_score = st.number_input("Major Examination Score", min_value=0.0, max_value=100.0, value=0.0, step=0.1, key="ml_major")

# --- Calculation Function ---
def calculate_ml_score_and_table(a1_score, a2_score, q1_score, q2_score, q3_score, major_score):
    """
    Calculates the weighted score for Machine Learning based on fixed max marks
    and specified weights, combining assignments and quizzes.
    """
    # Define weights
    weight_assignments = 0.25 # 25%
    weight_quizzes = 0.25     # 25%
    weight_major = 0.50       # 50%

    # Define fixed maximum marks
    max_a1 = 50.0
    max_a2 = 100.0
    max_q1 = 20.0
    max_q2 = 20.0
    max_q3 = 20.0
    max_major = 100.0

    # Calculate combined scores and max marks
    combined_assignment_score = a1_score + a2_score
    combined_assignment_max = max_a1 + max_a2 # 150

    combined_quiz_score = q1_score + q2_score + q3_score
    combined_quiz_max = max_q1 + max_q2 + max_q3 # 60

    # Calculate percentage for each combined component
    assignment_perc = (combined_assignment_score / combined_assignment_max) * 100 if combined_assignment_max > 0 else 0
    quiz_perc = (combined_quiz_score / combined_quiz_max) * 100 if combined_quiz_max > 0 else 0
    major_perc = (major_score / max_major) * 100 if max_major > 0 else 0

    # Calculate weighted contributions
    weighted_assignments = assignment_perc * weight_assignments
    weighted_quizzes = quiz_perc * weight_quizzes
    weighted_major = major_perc * weight_major

    # Calculate final total score
    total_weighted_score = weighted_assignments + weighted_quizzes + weighted_major

    # Prepare data for the summary table
    summary_data = [
        {
            "Component": "Assignments (Combined)",
            "Score": f"{combined_assignment_score:.2f}/{combined_assignment_max:.0f}",
            "Percentage": f"{assignment_perc:.2f}%",
            "Weight": f"{int(weight_assignments*100)}%",
            "Weighted Contribution": f"{weighted_assignments:.2f}"
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
if st.button("Calculate Weighted Score - Machine Learning"):
    # Call the calculation function with the user inputs
    total_score, summary_df = calculate_ml_score_and_table(
        a1_score, a2_score,
        q1_score, q2_score, q3_score,
        major_score
    )

    # Display the results
    st.success(f"Your weighted total score for Machine Learning is: {total_score:.2f}")
    st.subheader("Summary Table")
    st.table(summary_df) # Display the detailed breakdown
    st.markdown(f"**Final Weighted Score:** {total_score:.2f}") # Repeat final score

    # Display messages using the utils module
    message = utils.get_encouraging_message(total_score) # Score-based message
    st.info(message)
    st.markdown(f"### Quote of the Day:\n> {utils.get_random_motivational_quote()}") # Random quote