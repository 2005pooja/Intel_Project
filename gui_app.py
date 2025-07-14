import tkinter as tk
from tkinter import filedialog, messagebox
import numpy as np
import joblib
import matplotlib.pyplot as plt
from feature_extraction import extract_features

# Load the pre-trained model
model = joblib.load('models/fault_model.pkl')

def analyze_signal(signal):
    if signal.size == 0:  # Check if the signal is empty
        messagebox.showerror("Error", "The signal data is empty or invalid!")
        return None
    
    features = extract_features(signal)
    X = np.array([list(features.values())])
    prediction = model.predict(X)[0]
    return prediction

def load_and_predict():
    file_path = filedialog.askopenfilename()
    if file_path:
        try:
            # Use np.genfromtxt to load the data correctly
            signal = np.genfromtxt(file_path, delimiter=',')
            
            if signal.size == 0:  # Ensure there's data in the signal
                messagebox.showerror("Error", "The signal data is empty or invalid!")
                return
                
            pred = analyze_signal(signal)
            if pred is not None:
                result_label.config(text=f"Detected Fault: {pred}")
                plt.plot(signal)
                plt.title("Vibration Signal")
                plt.xlabel("Time")
                plt.ylabel("Amplitude")
                plt.show()

        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")

# Create GUI window
app = tk.Tk()
app.title("Bearing Fault Detection")
app.geometry("400x200")

# Load signal button
load_btn = tk.Button(app, text="Load Vibration Signal", command=load_and_predict)
load_btn.pack(pady=20)

# Result display label
result_label = tk.Label(app, text="Detected Fault: ")
result_label.pack(pady=10)

app.mainloop()
