import pandas as pd

df = pd.read_csv(
    "data/processed/cleaned_job_acceptance.csv"
)

if "Years_Experience" in df.columns:

    df["Experience_Category"] = pd.cut(
        df["Years_Experience"],
        bins=[0,2,5,100],
        labels=["Fresher","Junior","Senior"]
    )

df.to_csv(
    "data/processed/final_dataset.csv",
    index=False
)

print("Feature Engineering Done")