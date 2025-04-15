import matplotlib.pyplot as plt
import numpy as np
import random


tree_colour = (0/255, 90/255, 45/255)  # tree colour

def draw_tree(x, y, length, angle, branch_angle, shrink_factor, depth, thickness, decay_prob):
    if depth == 0 or random.random() < decay_prob:
        return

    # end point of branches
    x_end = x + length * np.cos(np.radians(angle))
    y_end = y + length * np.sin(np.radians(angle))

    # plot tree trunk
    plt.plot([x, x_end], [y, y_end], color=tree_colour, lw=thickness)

    # branches
    new_length = length * shrink_factor 
    new_thickness = max(thickness * 0.7, 0.5)

    draw_tree(x_end, y_end, new_length, angle - branch_angle, branch_angle, shrink_factor, depth - 1, new_thickness, decay_prob)
    draw_tree(x_end, y_end, new_length, angle + branch_angle, branch_angle, shrink_factor, depth - 1, new_thickness, decay_prob)


# parameters
init_x = 0 
init_y = -150
branch_length = 100
rotation = 90  # orientation
branch_angle = 20 # angle
branch_shrink = 0.7  
depth = 8  # recursion
trunk_thickness = 16
background_colour = (180/255, 220/255, 255/255)  # bg colour
decay_probability = 0.08

fig, ax = plt.subplots(figsize=(8, 8), facecolor=background_colour)
ax.set_facecolor(background_colour)
plt.axis('off')

plt.xlim(-170, 170)
plt.ylim(-170, 170)

draw_tree(init_x, init_y, branch_length, rotation, branch_angle, branch_shrink, depth, trunk_thickness, decay_probability)

# save as png
filename = "fractal_tree.png"
plt.savefig(filename, dpi=600, bbox_inches='tight', facecolor=background_colour)  

print(f"Image saved as '{filename}'")

plt.show()