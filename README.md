# Bearing Fault Detection in High-Speed Textile Spinning Frames

## Project Structure
- `data/` — synthetic dataset (`Signal1.csv`)  
- `models/` — trained model (`fault_model.pkl`)  
- `src/` — Streamlit app (`gui_app.py`) and training script (`model_training.py`)  
- `requirements.txt` — Python dependencies

## Setup Instructions
- Install dependencies:  
  ```bash
  pip install -r requirements.txt

- Train the model:  
  ```bash
  cd gui_app
  python model_training.py
This saves fault_model.pkl in the models/ folder.

- Run the Streamlit app:
  ```bash
  streamlit run src/gui_app.py

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
