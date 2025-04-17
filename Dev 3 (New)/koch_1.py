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

# Set the outline color here
col = ((50/255), (50/255), (50/255))

# Generate the snowflake
points = koch_snowflake(order=3, scale=10)

# Plot the snowflake
plt.figure(figsize=(6, 6))
plt.plot(points[:, 0], points[:, 1], color=col, linewidth=2)
plt.axis('equal')
plt.axis('off')
plt.savefig("stage_1.png", dpi=300, bbox_inches='tight', transparent=True)
plt.show()