# model.py

import numpy as np
import random

def predict(image):
    """
    Simulate AI predictions
    Returns: {
        'heatmap': np.array,
        'predictions': list of {condition, confidence},
        'urgency': str
    }
    """
    # Simulate heatmap
    heatmap = np.random.rand(224, 224)

    # Simulate predictions
    conditions = [
        "Pneumonia", "Pleural Effusion", "Cardiomegaly",
        "Pneumothorax", "Mass", "Normal"
    ]
    num_predictions = random.randint(1, 3)
    predictions = [
        {"condition": cond, "confidence": round(random.uniform(0.5, 0.98), 2)}
        for cond in random.sample(conditions, num_predictions)
    ]

    # Simulate urgency
    urgent_conditions = ["Pneumothorax", "Cardiomegaly"]
    urgency = "High" if any(p["condition"] in urgent_conditions for p in predictions) else "Routine"

    return {
        'heatmap': heatmap,
        'predictions': predictions,
        'urgency': urgency
    }