import pandas as pd
csv_path = "https://ibm.box.com/shared/static/keo2qz0bvh4iu6gf5qjq4vdrkt67bvvb.csv"
df = pd.read_csv(csv_path)
x = df.head()
x
