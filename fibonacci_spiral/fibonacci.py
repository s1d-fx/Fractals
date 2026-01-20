import numpy as np
from matplotlib import pyplot as plt
import matplotlib.patches as patches

def fibonacci(length: int) -> list[int]:
    """Generate Fibonacci sequence.

    :param length: The length of the Fibonacci sequence.
    :return: The Fibonacci sequence of length.
    """
    if length <= 0:
        return []
    if length == 1:
        return [1]
    sequence = [1, 1]
    while len(sequence) < length:
        sequence.append(sequence[-1] + sequence[-2])
    return sequence

def plot_fibonacci_squares_and_spiral(n: int) -> None:
    """Plot Fibonacci squares and spiral up to the nth Fibonacci number."""
    fib = fibonacci(n)
    
    # Initialize plot
    fig, ax = plt.subplots(figsize=(10, 10))
    ax.set_aspect("equal")
    ax.axis("off")

    # Start position and orientation
    x, y = 0, 0
    direction = 0  # 0=right, 1=up, 2=left, 3=down

    for i in range(n):
        side = fib[i]
        # Draw square
        square = patches.Rectangle((x, y), side, side, fill=False, edgecolor="gray", linewidth=1, alpha=0.6)
        ax.add_patch(square)

        # Update position for next square
        if direction == 0:
            x += side
        elif direction == 1:
            y += side
            x -= fib[i-1] if i >= 1 else 0
        elif direction == 2:
            x -= side
            y -= fib[i-1] if i >= 1 else 0
        elif direction == 3:
            y -= side

        direction = (direction + 1) % 4

    # Plot spiral
    angles = np.linspace(0, direction * np.pi / 2 + np.pi * 2, 1000)
    a = 1  # scaling factor
    r = a * np.exp(angles * 0.30635)  # approximate growth rate for Fibonacci spiral

    x_spiral = r * np.cos(angles)
    y_spiral = r * np.sin(angles)

    ax.plot(x_spiral, y_spiral, color="black", linewidth=2)

    # Save and show
    plt.savefig("fibonacci_spiral.png", dpi=300, bbox_inches="tight")
    plt.show()

plot_fibonacci_squares_and_spiral(10)
