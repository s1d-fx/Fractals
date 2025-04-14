import numpy as np
import matplotlib.pyplot as plt
from matplotlib.tri import Triangulation
import matplotlib.collections as mcoll
from matplotlib.colors import to_rgba

# --- Create a base grid of evenly spaced points across the whole area ---
cols, rows = 30, 30
x = np.linspace(0, 1, cols)
y = np.linspace(0, 1, rows)
xx, yy = np.meshgrid(x, y)
base_points = np.column_stack([xx.ravel(), yy.ravel()])

# --- Create a dense cluster of points near a random center location ---
cx, cy = np.random.uniform(0.3, 0.7, 2)
cluster_size = 40
jitter = 0.005
cluster_x = np.linspace(cx - 0.07, cx + 0.07, cluster_size)
cluster_y = np.linspace(cy - 0.07, cy + 0.07, cluster_size)
cluster_xx, cluster_yy = np.meshgrid(cluster_x, cluster_y)
cluster = np.column_stack([
    cluster_xx.ravel() + np.random.uniform(-jitter, jitter, cluster_xx.size),
    cluster_yy.ravel() + np.random.uniform(-jitter, jitter, cluster_yy.size)
])

cluster = cluster[(cluster[:, 0] >= 0) & (cluster[:, 0] <= 1) &
                  (cluster[:, 1] >= 0) & (cluster[:, 1] <= 1)]

# --- Combine points and triangulate ---
all_points = np.vstack([base_points, cluster])
x, y = all_points[:, 0], all_points[:, 1]
triang = Triangulation(x, y)

# --- Zoom settings ---
zoom_x = 0.1
zoom_y = 0.1
x_min, x_max = cx - zoom_x, cx + zoom_x
y_min, y_max = cy - zoom_y, cy + zoom_y

# --- Mask triangles that are outside zoom or have long edges ---
max_edge_length = 0.02

mask = []
for tri in triang.triangles:
    x_tri = x[tri]
    y_tri = y[tri]
    outside = np.any((x_tri < x_min) | (x_tri > x_max) |
                     (y_tri < y_min) | (y_tri > y_max))
    pts = np.column_stack((x_tri, y_tri))
    edge_lengths = [
        np.linalg.norm(pts[0] - pts[1]),
        np.linalg.norm(pts[1] - pts[2]),
        np.linalg.norm(pts[2] - pts[0])
    ]
    too_long = any(edge > max_edge_length for edge in edge_lengths)
    mask.append(outside or too_long)

triang.set_mask(mask)

# --- Create random colored transparent triangle patches ---
num_regions = 5
region_size = 200
colors = [
    to_rgba('cyan', 0.2),
    to_rgba('magenta', 0.2),
    to_rgba('lime', 0.2),
    to_rgba('orange', 0.2),
    to_rgba('deeppink', 0.2),
]

valid_tris = triang.triangles[~np.array(triang.mask)]
np.random.shuffle(valid_tris)
colored_regions = [
    valid_tris[i * region_size: (i + 1) * region_size]
    for i in range(min(num_regions, len(valid_tris) // region_size))
]

patches = []
for region_tris, color in zip(colored_regions, colors):
    triangles = [
        [(x[i], y[i]) for i in tri]
        for tri in region_tris
    ]
    coll = mcoll.PolyCollection(triangles, facecolors=[color], edgecolors='none')
    patches.append(coll)

# --- Plot it all ---
fig, ax = plt.subplots(figsize=(6, 6), facecolor='black', dpi=125)
ax.set_aspect('equal')
ax.axis('off')
ax.set_facecolor('black')

# Draw transparent color patches
for coll in patches:
    ax.add_collection(coll)

# Draw white wireframe on top
ax.triplot(triang, color='white', linewidth=0.3)

# Zoom view
ax.set_xlim(x_min, x_max)
ax.set_ylim(y_min, y_max)

# Save and show
plt.savefig('weighted_mesh.png', dpi=300, bbox_inches='tight', pad_inches=0, facecolor='black')
plt.show()
