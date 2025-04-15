import matplotlib.pyplot as plt
import numpy as np
import random

# Define IFS transformations inspired by both Koch + Dragon
# Format: (scale, rotation_deg, dx, dy)
transforms = [
    # Koch-style angles (60° triangle forms)
    (1/3, 0,     0,    0),
    (1/3, 60,   1/3,   0),
    (1/3, -60,  0.5, np.sqrt(3)/6),
    (1/3, 0,    2/3,   0),

    # Dragon-style turns (90° folds)
    (1/np.sqrt(2), 45,   0,     0),
    (1/np.sqrt(2), -45,  0.5,   0),
]

# Apply transformation to a point
def apply_transform(x, y, scale, angle, dx, dy):
    angle_rad = np.radians(angle)
    x_new = scale * (x * np.cos(angle_rad) - y * np.sin(angle_rad)) + dx
    y_new = scale * (x * np.sin(angle_rad) + y * np.cos(angle_rad)) + dy
    return x_new, y_new

# Chaos game to generate IFS fractal points
def generate_ifs(transforms, n_points=500000, discard=50):
    x, y = 0.0, 0.0
    points = []

    for i in range(n_points + discard):
        t = random.choice(transforms)
        x, y = apply_transform(x, y, *t)
        if i >= discard:
            points.append((x, y))
    return zip(*points)

# Generate points
x, y = generate_ifs(transforms, n_points=500000)

# Plot
plt.figure(figsize=(8, 8))
plt.scatter(x, y, s=0.1, color='black', alpha=0.8)
plt.axis('equal')
plt.axis('off')
plt.tight_layout()
plt.savefig("dragon_koch_hybrid.png", bbox_inches='tight', pad_inches=0, dpi=600)
