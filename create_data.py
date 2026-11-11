import pandas as pd

data = {
    "customer_id": [101, 102, 103, 104, 105],
    "age": [25, 40, 35, 50, 28],
    "monthly_charges": [50, 80, 65, 100, 55],
    "tenure": [2, 24, 12, 36, 5],
    "churn": [1, 0, 0, 0, 1]
}

df = pd.DataFrame(data)

df.to_csv("data/customer_data.csv", index=False)

print(df)
print("Dataset created successfully!")