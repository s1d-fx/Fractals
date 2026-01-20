import matplotlib.pyplot as plt
import numpy as np

# Generate the classic dragon curve using L-system rules
def dragon_lsystem(iterations):
    axiom = "FX"
    rules = {
        "X": "X+YF+",
        "Y": "-FX-Y"
    }
    result = axiom
    for _ in range(iterations):
        new_result = ""
        for char in result:
            new_result += rules.get(char, char)
        result = new_result
    return result

# Convert instruction string into coordinates
def draw_lsystem(seq, step=1):
    x, y = 0.0, 0.0
    angle = 0
    points = [(x, y)]

    for cmd in seq:
        if cmd == "F":
            x += step * np.cos(np.radians(angle))
            y += step * np.sin(np.radians(angle))
            points.append((x, y))
        elif cmd == "+":
            angle -= 90
        elif cmd == "-":
            angle += 90
    return zip(*points)

# Generate the curve
iterations = 14
sequence = dragon_lsystem(iterations)
x, y = draw_lsystem(sequence, step=1)

# Plot with transparent background
fig = plt.figure(figsize=(8, 8), dpi=600)
ax = fig.add_subplot(111)

col = ((255/255), (255/255), (255/255))

ax.plot(x, y, color=col, linewidth=2)
ax.axis('equal')
ax.axis('off')

# Set transparent background
fig.patch.set_alpha(0)
ax.patch.set_alpha(0)

# Save as PNG with transparency
plt.savefig("dragon_2.png", transparent=True, bbox_inches='tight', pad_inches=0)

