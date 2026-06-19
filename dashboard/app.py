import streamlit as st
import os

st.write("Current Working Directory:")
st.write(os.getcwd())

st.write("Files in current directory:")
st.write(os.listdir("."))
import pandas as pd

df = pd.read_csv("data/raw/job_acceptance.csv")
import pandas as pd
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
csv_path = os.path.join(BASE_DIR, "data", "raw", "job_acceptance.csv")

df = pd.read_csv(csv_path)