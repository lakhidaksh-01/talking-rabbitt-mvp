import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Talking Rabbitt 🐰")
st.subheader("Conversational AI for Business Data")

uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)

    st.write("### Data Preview")
    st.dataframe(df)

    question = st.text_input("Ask a question about your data")

    if question:

        if "highest" in question.lower():

            column = df.columns[1]
            result = df.loc[df[column].idxmax()]

            st.write(f"📊 {result[0]} has the highest {column}")

        elif "lowest" in question.lower():

            column = df.columns[1]
            result = df.loc[df[column].idxmin()]

            st.write(f"📉 {result[0]} has the lowest {column}")

        st.write("### Visualization")
        st.bar_chart(df.set_index(df.columns[0]))