import cv2
import numpy as np

# Load your depth map
depth_map = cv2.imread("depth_image.png", cv2.IMREAD_GRAYSCALE)

# Define your max visible distance (e.g., 20 meters)
MAX_DISTANCE_METERS = 20.0

# Convert grayscale [0,255] to normalized [0.0, 1.0]
normalized = depth_map.astype(np.float32) / 255.0

# Estimate real-world distance per pixel
distance_map = normalized * MAX_DISTANCE_METERS

# Example: distance at pixel (x, y)
x, y = 300, 250
print(f"Estimated distance at ({x}, {y}): {distance_map[y, x]:.2f} meters")
