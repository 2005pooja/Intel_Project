# Bearing Fault Detection in High-Speed Textile Spinning Frames

## Project Structure
- `data/` — synthetic dataset (`bearing_vibration_data.csv`)  
- `models/` — trained model (`model.pkl`)  
- `app/` — Streamlit app (`app.py`) and training script (`train_model.py`)  
- `requirements.txt` — Python dependencies

## Setup Instructions
- Install dependencies:  
  ```bash
  pip install -r requirements.txt

- Train the model:  
  ```bash
  cd app
  python train_model.py
This saves model.pkl in the models/ folder.

- Run the Streamlit app:
  ```bash
  streamlit run app/app.py

## Features
- Predict bearing condition level from vibration sensor data
- Support for manual input or CSV upload
- Feature importance visualization
- Prediction probability display
- Advice on bearing replacement or maintenance

## Notes
- Dataset is synthetic and for demonstration purposes only.
- Project can be extended with:
  - Real sensor data
  - Additional physical features (temperature, load, etc.)
  - Advanced ML models (LSTM, XGBoost, CNNs)
