import pandas as pd
from sqlalchemy import create_engine

df = pd.read_csv(
    "data/processed/final_dataset.csv"
)

engine = create_engine(
    "mysql+pymysql://root:12345@localhost:3306/job_acceptance"
)

df.to_sql(
    "candidate_data",
    engine,
    if_exists="replace",
    index=False
)

print("Data Loaded")