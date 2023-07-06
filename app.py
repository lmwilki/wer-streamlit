import streamlit as st
import werpy
import pandas as pd
import datetime

st.title("Word Error Rate (WER) Calculator")

input_mode = st.selectbox("Select input mode", ["Single", "Bulk (2 Text Files)", "Bulk (1 CSV)"])

global input_text, ground_truth

input_text = None
ground_truth = None



if input_mode == "Single":

    input_text = st.text_area("Enter your text here", "The quick brown fox jumps of the lazy dog")
    ground_truth = st.text_area("Enter the ground truth", "The quick brown fox jumps over the lazy dog")

elif input_mode == "Bulk (2 Text Files)":
    input_col, ground_truth_col = st.columns(2)

    with input_col:
        input_file = st.file_uploader("Upload the input text file", type=["txt"])
        if input_file is not None:
            input_text = input_file.readlines()
            input_text = [line.decode("utf-8").strip() for line in input_text]
    
    with ground_truth_col:
        ground_truth_file = st.file_uploader("Upload the ground truth text file", type=["txt"])
        if ground_truth_file is not None:
            ground_truth = ground_truth_file.readlines()
            ground_truth = [line.decode("utf-8").strip() for line in ground_truth]

elif input_mode == "Bulk (1 CSV)":
    csv_file = st.file_uploader("Upload the CSV file", type=["csv"])

    if csv_file is not None:
        df = pd.read_csv(csv_file)
        columns = df.columns
        # Check there is more than one column
        if len(columns) < 2:
            st.error("Please upload a CSV file with more than one column")
            st.stop()
        input_col, ground_truth_col = st.columns(2)

        with input_col:
            input_text_column = st.selectbox("Select the input column", columns)
            input_text = df[input_text_column].tolist()
        
        with ground_truth_col:
            ground_truth_column = st.selectbox("Select the ground truth column", columns)
            ground_truth = df[ground_truth_column].tolist()
        

run_wer = st.button("Calculate WER")

if run_wer:
    if input_text is None or ground_truth is None:
        st.error("Please enter the input text and ground truth")
        st.stop()

    st.write(input_text)
    st.write(ground_truth)

    normalised_input = werpy.normalize(input_text)
    normalised_ground_truth = werpy.normalize(ground_truth)

    summary = werpy.summary(normalised_input, normalised_ground_truth)

    calculation_time = datetime.datetime.now(tz=datetime.timezone.utc).strftime("%Y-%m-%dT%H-%M-%SZ")

    st.write(summary)

    # Download the summary

    st.divider()
    st.subheader("Download the Summary")

    include_input_ground_truth = st.checkbox("Include the input and ground truth in the summary", value=True)

    if include_input_ground_truth:
        if len(summary) == 1:
            summary["input"] = [input_text]
            summary["ground_truth"] = [ground_truth]
        else:
            summary["input"] = input_text
            summary["ground_truth"] = ground_truth

    csv_col, json_col = st.columns(2)

    with csv_col:
        csv = summary.to_csv(index=False)

        download_button = st.download_button(
            label="Download the Summary CSV",
            data=csv,
            file_name=f"summary_{calculation_time}.csv",
            mime="text/csv"
        )

    with json_col:
        json = summary.to_json(orient="records")

        download_button = st.download_button(
            label="Download the Summary JSON",
            data=json,
            file_name=f"summary_{calculation_time}.json",
            mime="application/json"
        )