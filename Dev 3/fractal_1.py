import numpy as np
import matplotlib.pyplot as plt
import random

# Function to generate the Julia set
def julia_set(c, size=800, max_iter=256):
    x = np.linspace(-1.5, 1.5, size)
    y = np.linspace(-1.5, 1.5, size)
    X, Y = np.meshgrid(x, y)
    Z = X + 1j * Y
    img = np.zeros(Z.shape, dtype=int)
    
    for i in range(size):
        for j in range(size):
            z = Z[i, j]
            iteration = 0
            while abs(z) <= 2 and iteration < max_iter:
                z = z**2 + c
                iteration += 1
            img[i, j] = iteration
    return img

# L-system functions
def apply_lsystem(axiom, rules, iterations):
    result = axiom
    for _ in range(iterations):
        result = ''.join([rules.get(c, c) for c in result])
    return result

def lsystem_to_points(lsystem_str, angle_step=25, length=5):
    x, y = 0, 0
    angle = 0
    points = [(x, y)]
    stack = []

    for symbol in lsystem_str:
        if symbol == 'F':  # Move forward and plot
            x += length * np.cos(np.radians(angle))
            y += length * np.sin(np.radians(angle))
            points.append((x, y))
        elif symbol == '+':  # Turn right
            angle += angle_step
        elif symbol == '-':  # Turn left
            angle -= angle_step
        elif symbol == '[':  # Save state
            stack.append((x, y, angle))
        elif symbol == ']':  # Restore state
            x, y, angle = stack.pop()

    return points

# L-system rules to generate branching fractals
def generate_lsystem():
    axiom = "F"
    rules = {
        'F': 'F+F-F-F+F',  # classic fractal branching rule
        '+': '+',  # turn right
        '-': '-',  # turn left
        '[': '[',  # save state
        ']': ']'   # restore state
    }
    return axiom, rules

# Parameters
c = complex(random.uniform(-1, 1), random.uniform(-1, 1))  # Randomized Julia set constant
iterations = 8  # Number of L-system iterations (increased for complexity)
lsystem_axiom, lsystem_rules = generate_lsystem()

# Generate the Julia set
img = julia_set(c)

# Apply L-system to generate fractal pattern
lsystem_string = apply_lsystem(lsystem_axiom, lsystem_rules, iterations)
lsystem_points = lsystem_to_points(lsystem_string)

# Plotting the Julia set with L-system fractal
plt.figure(figsize=(10, 10))

# Plot Julia Set as background
plt.imshow(img, cmap='inferno', extent=[-1.5, 1.5, -1.5, 1.5])

# Plot the L-system fractal on top of the Julia set
lsystem_x, lsystem_y = zip(*lsystem_points)
plt.plot(lsystem_x, lsystem_y, color='cyan', linewidth=1.5)

# Remove axes and labels for clean visualization
plt.axis('off')
plt.tight_layout()
plt.show()

