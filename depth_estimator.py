import numpy as np

def calculate_distance(depth_map, scaling_factor=100):
    """
    Calculate distances from the depth map.

    Parameters:
    depth_map (numpy.ndarray): The input depth map as a NumPy array.
    scaling_factor (float): The factor to convert normalized depth values to real-world distances. Default is 100.

    Returns:
    numpy.ndarray: An array representing distances in centimeters.
    """
    # Ensure the input is a NumPy array
    if not isinstance(depth_map, np.ndarray):
        raise ValueError("Depth map must be a numpy array.")

    # Normalize depth map values to [0, 1] range
    depth_map_normalized = depth_map / 255.0
    
    # Inverse the normalized values to simulate distance (closer objects = higher values)
    distances = (1 - depth_map_normalized) * scaling_factor
    
    return distances