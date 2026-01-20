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

# Define IFS functions (Iterated Function System)
def func_1(x, y):
    # Sinusoidal variation
    return math.sin(x), math.sin(y)

def func_2(x, y):
    # Linear contraction + rotation
    r = 0.5
    theta = math.radians(30)
    nx = r * (x * math.cos(theta) - y * math.sin(theta))
    ny = r * (x * math.sin(theta) + y * math.cos(theta))
    return nx, ny

def func_3(x, y):
    # Another affine transform
    return 0.5 * x + 0.5, 0.5 * y + 0.5

# Generate points
for i in range(n + 20):
    r = random.random()
    if r < 0.33:
        x, y = func_1(x, y)
    elif r < 0.66:
        x, y = func_2(x, y)
    else:
        x, y = func_3(x, y)

    # Discard first 20 points (burn-in) to reach the attractor
    if i >= 20:
        x_vals.append(x)
        y_vals.append(y)

# Plot
plt.figure(figsize=(8, 8), facecolor='black')
# Use a colormap or single bright color. 'hot' colormap looks like fire.
plt.scatter(x_vals, y_vals, s=0.2, c=range(len(x_vals)), cmap='magma', alpha=0.5, edgecolors='none')
plt.axis('off')
plt.tight_layout()
plt.savefig("flame_fractal.png", dpi=300, bbox_inches="tight", facecolor='black')
# plt.show() # Commented out to avoid blocking if run in automation, but user can uncomment
