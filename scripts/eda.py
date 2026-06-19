import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv(
    "data/processed/cleaned_job_acceptance.csv"
)

print(df.describe())

sns.heatmap(df.select_dtypes(include='number').corr(),
            annot=True)

plt.show()