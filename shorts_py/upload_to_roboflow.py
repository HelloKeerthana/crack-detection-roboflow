from roboflow import Roboflow

# Paste your actual API key below
rf = Roboflow(api_key="xxxxxxxxxxxxxxxxxxx")

# Replace with your workspace and project
project = rf.workspace("kira-hs9v0").project("crackdetection02")

# Upload folder path (update this)
dataset_path = "C:\\Users\\satya\\OneDrive\\Desktop\\keerthana\\DL_APSAC\\ds\\tiled_dataset"

# Upload to Roboflow
project.upload(dataset_path)

