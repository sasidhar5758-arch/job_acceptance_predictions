import pandas as pd

df = pd.read_csv("data/raw/job_acceptance.csv")

print(df.shape)

df.drop_duplicates(inplace=True)

num_cols = df.select_dtypes(include=['int64','float64']).columns
cat_cols = df.select_dtypes(include=['object']).columns

for col in num_cols:
    df[col] = df[col].fillna(df[col].median())

for col in cat_cols:
    df[col] = df[col].fillna(df[col].mode()[0])

df.to_csv(
    "data/processed/cleaned_job_acceptance.csv",
    index=False
)

print("Cleaning Completed")
df = pd.read_csv("data/raw/job_acceptance.csv")
import pandas as pd

df = pd.read_csv("data/raw/Job_Acceptance_Dataset.csv")

print(df.head())
import pandas as pd

df = pd.read_csv("data/raw/HR_Job_Placement_Dataset.csv")

print(df.shape)
print(df.columns)
print(df.head())
import pandas as pd

df = pd.read_csv("data/raw/HR_Job_Placement_Dataset.csv")

print("Shape:", df.shape)
print("\nColumns:")
print(df.columns.tolist())

print("\nFirst 5 Rows:")
print(df.head())