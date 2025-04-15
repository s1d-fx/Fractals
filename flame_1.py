import matplotlib.pyplot as plt
import random
import math

# Number of points
n = 100000

# Storage
x_vals = []
y_vals = []

# Start at origin
x, y = 0.0, 0.0

# Flame-style transformations (edited for stability)
def transform_1(x, y):
    r = math.sqrt(x**2 + y**2) + 1e-6
    theta = math.atan2(y, x)
    new_x = math.sin(theta * r) / r
    new_y = math.cos(theta * r) / r
    return 0.7 * new_x, 0.7 * new_y

def transform_2(x, y):
    new_x = math.sin(x) + 0.5 * math.sin(y)
    new_y = math.cos(y) - 0.5 * math.cos(x)
    return 0.5 * new_x, 0.5 * new_y

def transform_3(x, y):
    angle = math.radians(45)
    scale = 0.85
    new_x = scale * (math.cos(angle) * x - math.sin(angle) * y) + 0.2
    new_y = scale * (math.sin(angle) * x + math.cos(angle) * y)
    return new_x, new_y

# Generate points
for _ in range(n):
    r = random.random()
    if r < 0.4:
        x, y = transform_1(x, y)
    elif r < 0.7:
        x, y = transform_2(x, y)
    else:
        x, y = transform_3(x, y)

    x_vals.append(x)
    y_vals.append(y)

# Plot with color, better point size, and black background
plt.figure(figsize=(6, 6), facecolor='black')
plt.scatter(x_vals, y_vals, s=0.05, c='orangered', alpha=0.7, edgecolors='none')
plt.axis('off')
plt.tight_layout()
plt.show()
