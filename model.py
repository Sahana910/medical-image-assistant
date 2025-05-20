import numpy as np
import random

def predict(image):
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
    urgency = "High" if any(p["condition"] in urgent_conditions for p in predictions) else \
              "Medium" if any(p["condition"] in ["Pleural Effusion", "Mass"] for p in predictions) else "Routine"

    return {
        'heatmap': np.random.rand(224, 224),
        'predictions': predictions,
        'urgency': urgency
    }
