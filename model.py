# model.py

import numpy as np
import random

def predict(image):
    """
    Simulates AI predictions.
    Returns: {
        'heatmap': np.array,
        'predictions': list of {condition, confidence},
        'urgency': str
    }
    """

    # Simulate heatmap (AI focus areas)
    heatmap = np.random.rand(224, 224)
    heatmap -= heatmap.min()
    heatmap /= heatmap.max()
    heatmap = (heatmap * 255).astype(np.uint8)  # Convert to grayscale image format

    # Simulate abnormality predictions
    conditions = [
        "Pneumothorax", "Pleural Effusion", "Cardiomegaly",
        "Mass", "Atelectasis", "Normal"
    ]
    num_predictions = random.randint(1, 3)
    predictions = [
        {"condition": cond, "confidence": round(random.uniform(0.5, 0.98), 2)}
        for cond in random.sample(conditions, num_predictions)
    ]

    # Determine urgency
    urgent_conditions = ["Pneumothorax", "Cardiomegaly"]
    high_priority = any(p["condition"] in urgent_conditions for p in predictions)
    medium_conditions = ["Pleural Effusion", "Mass"]

    if high_priority:
        urgency = "High"
    elif any(p["condition"] in medium_conditions for p in predictions):
        urgency = "Medium"
    else:
        urgency = "Routine"

    return {
        'heatmap': heatmap,
        'predictions': predictions,
        'urgency': urgency
    }
