import os
import pandas as pd

# Paths
csv_path = "C:\\Users\\satya\\OneDrive\\Desktop\\keerthana\\DL_APSAC\\combined_labels.csv"
image_folder = "C:\\Users\\satya\\OneDrive\\Desktop\\keerthana\\DL_APSAC\\ds\\DATASET"

df = pd.read_csv(csv_path)

df['image'] = df['image'].astype(str).str.lower().str.strip()

existing_images = {f.lower() for f in os.listdir(image_folder)}

df_filtered = df[df['image'].isin(existing_images)]

output_csv = csv_path.replace(".csv", "_filtered.csv")
df_filtered.to_csv(output_csv, index=False)

print(f"Done. Rows reduced from {len(df)} to {len(df_filtered)}.")
print(f"Cleaned CSV saved at: {output_csv}")

