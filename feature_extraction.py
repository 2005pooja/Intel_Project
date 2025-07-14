import numpy as np
import pandas as pd

def extract_features(signal):
    features = {
        'mean': np.mean(signal),
        'std_dev': np.std(signal),
        'max': np.max(signal),
        'min': np.min(signal),
        'rms': np.sqrt(np.mean(signal**2)),
        'kurtosis': pd.Series(signal).kurt(),
        'skewness': pd.Series(signal).skew()
    }
    return features
