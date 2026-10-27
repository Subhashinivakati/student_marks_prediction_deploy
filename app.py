import pickle
import streamlit as st
import numpy as np
# Set up the web page
st.title("🎓 Student marks Predictor")
st.write("Enter the number of hours studied.")

# Load the saved ML model
with open("studentmarks_model.pkl", "rb") as file:
    model = pickle.load(file)

# Take input from the user
hours = st.number_input(
    "Study hours",
    min_value=0.0,
    max_value=24.0,
    value=4.0,
    step=0.5
)
# Predict when the button is click
if st.button("Predicted Marks", use_container_width=True):
    input_data = np.array([[hours]])
    predicted_marks = model.predict(input_data)[0]
    st.success("Prediction Completed!")
    st.metric( label="Expected Student Marks", value=f"{predicted_marks:.2f} / 100" )
    st.write(f"📚 Hours Studied: {hours}")
    st.write( f"📝 Predicted Marks: {predicted_marks:.2f}" ) 
    # Display performance message
if predicted_marks >= 80: 
    st.info("Excellent performance! 🌟")
elif predicted_marks >= 60: 
    st.info("Good performance! 👍")
elif predicted_marks >= 40: 
    st.info("Average performance. Keep practicing! 📖") 
else: st.warning("More study and practice may be helpful.")
st.divider()




