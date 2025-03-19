import matplotlib.pyplot as plt
import numpy as np


tree_colour = (0/255, 90/255, 45/255)


def draw_tree(x, y, length, angle, branch_angle, shrink_factor, depth):
    if depth == 0:
        return

    # end point of branch
    x_end = x + length * np.cos(np.radians(angle))
    y_end = y + length * np.sin(np.radians(angle))

    # plot trunk
    plt.plot([x, x_end], [y, y_end], color=tree_colour, lw=2)

    # drawing branches
    new_length = length * shrink_factor
    draw_tree(x_end, y_end, new_length, angle - branch_angle, branch_angle, shrink_factor, depth - 1)
    draw_tree(x_end, y_end, new_length, angle + branch_angle, branch_angle, shrink_factor, depth - 1)

plt.figure(figsize=(8, 8))
plt.axis('off') 

# parameters
init_x = 0 
init_y = -200 
branch_length = 100
rotation = 90  # Rotation
branch_angle = 20  # Angle
branch_shrink = 0.7  
depth = 8  # Recursion


draw_tree(init_x, init_y, branch_length, rotation, branch_angle, branch_shrink, depth)
plt.show()



