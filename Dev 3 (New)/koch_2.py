import matplotlib.pyplot as plt
import numpy as np

def koch_snowflake(order, scale=10):
    def koch_curve(p1, p2, order):
        if order == 0:
            return [p1, p2]
        else:
            p1 = np.array(p1)
            p2 = np.array(p2)
            delta = (p2 - p1) / 3
            pA = p1
            pB = p1 + delta
            pD = p1 + 2 * delta

            angle = np.pi / 3
            rotation = np.array([[np.cos(angle), -np.sin(angle)],
                                 [np.sin(angle),  np.cos(angle)]])
            pC = pB + rotation @ delta

            return (koch_curve(pA, pB, order - 1) +
                    koch_curve(pB, pC, order - 1)[1:] +
                    koch_curve(pC, pD, order - 1)[1:] +
                    koch_curve(pD, p2, order - 1)[1:])

    height = np.sqrt(3) / 2 * scale
    A = [0, 0]
    B = [scale / 2, height]
    C = [scale, 0]

    points = []
    points += koch_curve(A, B, order)[:-1]
    points += koch_curve(B, C, order)[:-1]
    points += koch_curve(C, A, order)

    return np.array(points)

line_col = ((240/255), (224/255), (191/255))
fill_col = ((240/255), (224/255), (191/255))

def draw_recursive_snowflakes(order=3, scale=10, depth=3, scale_factor=0.9, center=None, linewidth=4, fill_color=None):
    # Generate the current snowflake
    points = koch_snowflake(order=order, scale=scale)

    # Find the centroid (center) of the current snowflake
    current_center = np.mean(points, axis=0)

    # If this is the first (largest) snowflake, store its center
    if center is None:
        center = current_center

    # Calculate the translation vector to align to the original center
    translation = center - current_center

    # Apply the translation
    points_translated = points + translation

    # Fill the current snowflake if fill_color is provided
    if fill_color is not None:
        plt.fill(points_translated[:, 0], points_translated[:, 1], color=fill_color, linewidth=0)

    # Plot the current snowflake
    plt.plot(points_translated[:, 0], points_translated[:, 1], color=line_col, linewidth=linewidth)

    # Recursive call for next smaller snowflake with reduced linewidth
    if depth > 1:
        draw_recursive_snowflakes(order, scale * scale_factor, depth - 1, scale_factor, center=center, linewidth=linewidth * 0.8, fill_color=fill_color)

# Save/show the plot
plt.figure(figsize=(6, 6))
# draw_recursive_snowflakes(order=3, scale=10, depth=100, scale_factor=0.99) Fade
draw_recursive_snowflakes(order=2, scale=10, depth=1, scale_factor=0.75, fill_color=(fill_col))
plt.axis('equal')
plt.axis('off')

plt.savefig("Dev 3 (New)/snowflake_6.png", dpi=300, bbox_inches='tight', transparent=True)
plt.show()
