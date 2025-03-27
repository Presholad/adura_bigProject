import pickle
import os

# Dummy model (replace with your trained model)
model = {"message": "This is a test model"}

# Ensure the artifacts directory exists
os.makedirs("C:/Users/gbemi/book recommender system/artifacts", exist_ok=True)

# Save the model
model_path = "C:/Users/gbemi/book recommender system/artifacts/model.pkl"
with open(model_path, "wb") as f:
    pickle.dump(model, f)

print("✅ model.pkl saved successfully at:", model_path)
