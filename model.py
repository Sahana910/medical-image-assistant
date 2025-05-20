import numpy as np
import matplotlib.pyplot as plt

def predict(image):
    # Simulate AI predictions
    heatmap = np.random.rand(224, 224)  # Replace with real heatmap logic
    heatmap -= heatmap.min()
    heatmap /= heatmap.max()
    heatmap = (heatmap * 255).astype(np.uint8)

    return {
        'heatmap': heatmap,
        'predictions': [
            {'condition': 'Pneumothorax', 'confidence': 0.56},
            {'condition': 'Pleural Effusion', 'confidence': 0.42}
        ],
        'urgency': 'High'
    }
