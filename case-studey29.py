import pandas as pd

df = pd.read_csv(r"C:\Users\ELCOT\Desktop\Data-Science\Q29_telecom_network.csv")

df = df.drop_duplicates()

df["signal_strength_dbm"] = df["signal_strength_dbm"].fillna(
    df["signal_strength_dbm"].mean()
)

df = df[df["call_duration_min"] >= 0]

df["dropped_call"] = pd.to_numeric(df["dropped_call"], errors="coerce").fillna(0).astype(int)

rate = df.groupby("location")["dropped_call"].mean() * 100
print("Dropped Call Rate:")
print(rate)

df["signal_quality"] = pd.cut(
    df["signal_strength_dbm"],
    bins=[-100, -80, -60, 0],
    labels=["Poor", "Average", "Good"]
)

df["call_reliability"] = 1 - df["dropped_call"]


print("\nFirst 5 rows:")
print(df.head())
