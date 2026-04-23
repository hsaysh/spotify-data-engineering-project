from pymongo import MongoClient
import pandas as pd

# MongoDB connect
client = MongoClient("mongodb://localhost:27017/")
db = client["spotifyDB"]
collection = db["tracks"]

# Data fetch
data = list(collection.find())

# Convert to DataFrame
df = pd.DataFrame(data)

# _id column remove
df.drop("_id", axis=1, inplace=True)

print(df.head())
# Missing values handle
df.fillna(0, inplace=True)

# Remove duplicates
df.drop_duplicates(inplace=True)

# New column (popularity level example)
if "popularity" in df.columns:
    df["popularity_level"] = df["popularity"].apply(
        lambda x: "High" if x > 80 else ("Medium" if x > 50 else "Low")
    )

# Save to CSV
df.to_csv("cleaned_spotify_data.csv", index=False)

print("Cleaned data saved successfully!")