import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import joblib
from feature_extraction import extract_features
import os

# Create the models folder if it doesn't exist
if not os.path.exists('models'):
    os.makedirs('models')

# Load dataset
print("Loading data...")
df = pd.read_csv('data/vibration_data.csv')
features = []
labels = []

# Extract features from the dataset
for i, row in df.iterrows():
    # Convert the signal to a string to use np.fromstring
    signal_str = str(row['signal'])
    
    # Convert the string to a numpy array
    signal = np.fromstring(signal_str, sep=',')
    
    feature_dict = extract_features(signal)
    features.append(list(feature_dict.values()))
    labels.append(row['label'])

# Check if features and labels were populated
print(f"Features length: {len(features)}, Labels length: {len(labels)}")

X = pd.DataFrame(features)
y = labels

# Train the model
print("Training model...")
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
clf = RandomForestClassifier(n_estimators=100)
clf.fit(X_train, y_train)

# Save the model to the models directory
print("Saving the model...")
joblib.dump(clf, 'models/fault_model.pkl')

print("Model training complete and saved to models/fault_model.pkl")
