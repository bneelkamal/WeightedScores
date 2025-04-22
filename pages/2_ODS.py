import streamlit as st
import pandas as pd
import utils

st.set_page_config(page_title="ODS - Weighted Score Calculator", layout="centered")
st.title("T1 ODS - Weighted Score Calculator")


st.subheader("Evaluation Breakdown - ODS")
eval_data = {
"Component": ["Major Examination", "Best Quiz (Fractal 1)", "Assignment (Fractal 1)", "Quiz & Assignment (Fractal 2)", "Total"],
"Weightage": ["50%", "15%", "10%", "25%", "100%"]
}
st.table(pd.DataFrame(eval_data))

st.write("### Maximum Marks for Each Component")
st.write("- Major Examination: 70")
st.write("- Assignment (Fractal 1): 10")
st.write("- Assignment (Fractal 2): 9")
st.write("- Quiz 1 (Fractal 1): 15")
st.write("- Quiz 2 (Fractal 1): 15")
st.write("- Quiz 1 (Fractal 2): 10")
st.write("- Quiz 2 (Fractal 2): 12")

st.subheader("Enter Your Scores")
major_score = st.number_input("Major Examination Score", min_value=0.0, max_value=70.0, value=0.0, step=0.1)
quiz1_f1 = st.number_input("Quiz 1 (Fractal 1) Score", min_value=0.0, max_value=15.0, value=0.0, step=0.1, key="quiz1_f1")
quiz2_f1 = st.number_input("Quiz 2 (Fractal 1) Score", min_value=0.0, max_value=15.0, value=0.0, step=0.1, key="quiz2_f1")
assignment_f1_score = st.number_input("Assignment (Fractal 1) Score", min_value=0.0, max_value=10.0, value=0.0, step=0.1, key="assignment_f1")

quiz1_f2 = st.number_input("Quiz 1 (Fractal 2) Score", min_value=0.0, max_value=10.0, value=0.0, step=0.1, key="quiz1_f2")
quiz2_f2 = st.number_input("Quiz 2 (Fractal 2) Score", min_value=0.0, max_value=12.0, value=0.0, step=0.1, key="quiz2_f2")
assignment_f2_score = st.number_input("Assignment (Fractal 2) Score", min_value=0.0, max_value=9.0, value=0.0, step=0.1, key="assignment_f2")

def calculate_weighted_score_and_table(major_score, quiz1_f1, quiz2_f1, assignment_f1_score, quiz1_f2, quiz2_f2, assignment_f2_score):
    weight_major = 0.50
    weight_quiz_f1 = 0.15
    weight_assignment_f1 = 0.10
    weight_quiz_assign_f2 = 0.25


    major_perc = (major_score / 70) * 100 if 70 > 0 else 0

    quiz1_f1_perc = (quiz1_f1 / 15) * 100 if 15 > 0 else 0
    quiz2_f1_perc = (quiz2_f1 / 15) * 100 if 15 > 0 else 0
    if quiz1_f1_perc >= quiz2_f1_perc:
        best_quiz_f1_perc = quiz1_f1_perc
        best_quiz_f1_score = quiz1_f1
        best_quiz_f1_max = 15
    else:
        best_quiz_f1_perc = quiz2_f1_perc
        best_quiz_f1_score = quiz2_f1
        best_quiz_f1_max = 15

    assignment_f1_perc = (assignment_f1_score / 10) * 100 if 10 > 0 else 0

    quiz1_f2_perc = (quiz1_f2 / 10) * 100 if 10 > 0 else 0
    quiz2_f2_perc = (quiz2_f2 / 12) * 100 if 12 > 0 else 0
    if quiz1_f2_perc >= quiz2_f2_perc:
        best_quiz_f2_perc = quiz1_f2_perc
        best_quiz_f2_score = quiz1_f2
        best_quiz_f2_max = 10
    else:
        best_quiz_f2_perc = quiz2_f2_perc
        best_quiz_f2_score = quiz2_f2
        best_quiz_f2_max = 12

    assignment_f2_perc = (assignment_f2_score / 9) * 100 if 9 > 0 else 0

    weighted_major = major_perc * weight_major
    weighted_quiz_f1 = best_quiz_f1_perc * weight_quiz_f1
    weighted_assignment_f1 = assignment_f1_perc * weight_assignment_f1
    avg_fractal2_perc = (best_quiz_f2_perc + assignment_f2_perc) / 2
    weighted_quiz_assign_f2 = avg_fractal2_perc * weight_quiz_assign_f2

    total_weighted = weighted_major + weighted_quiz_f1 + weighted_assignment_f1 + weighted_quiz_assign_f2

    data = [
        {
            "Component": "Major Examination",
            "Score": f"{major_score:.2f}/70",
            "Percentage": f"{major_perc:.2f}%",
            "Weight": "50%",
            "Weighted Contribution": f"{weighted_major:.2f}"
        },
        {
            "Component": "Best Quiz (Fractal 1)",
            "Score": f"{best_quiz_f1_score:.2f}/{best_quiz_f1_max}",
            "Percentage": f"{best_quiz_f1_perc:.2f}%",
            "Weight": "15%",
            "Weighted Contribution": f"{weighted_quiz_f1:.2f}"
        },
        {
            "Component": "Assignment (Fractal 1)",
            "Score": f"{assignment_f1_score:.2f}/10",
            "Percentage": f"{assignment_f1_perc:.2f}%",
            "Weight": "10%",
            "Weighted Contribution": f"{weighted_assignment_f1:.2f}"
        },
        {
            "Component": "Quiz & Assignment (Fractal 2)",
            "Score": f"Quiz: {best_quiz_f2_score:.2f}/{best_quiz_f2_max} + Assignment: {assignment_f2_score:.2f}/9",
            "Percentage": f"{avg_fractal2_perc:.2f}%",
            "Weight": "25%",
            "Weighted Contribution": f"{weighted_quiz_assign_f2:.2f}"
        }
    ]
    return total_weighted, pd.DataFrame(data)


if st.button("Calculate Weighted Score - New Subject"):
    total_score, summary_df = calculate_weighted_score_and_table(
    major_score,
    quiz1_f1, quiz2_f1, assignment_f1_score,
    quiz1_f2, quiz2_f2, assignment_f2_score )
    st.success(f"Your weighted total score is: {total_score:.2f}")
    st.subheader("Summary Table")
    st.table(summary_df)
    st.markdown(f"Final Weighted Score: {total_score:.2f}")
    message = utils.get_encouraging_message(total_score)
    st.info(message)
    st.markdown(f"### Quote of the Day:\n> {utils.get_random_motivational_quote()}")
