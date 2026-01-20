# Fractals

A collection of Python scripts for generating and visualizing various fractal patterns, including classic fractals like the Dragon Curve, Koch Snowflake, Mandelbrot Set, and artistic variations using different rendering techniques.

## Overview

This repository explores the mathematical beauty of fractals through Python implementations. Each script generates unique fractal patterns using different algorithms and visualization methods, from L-systems to iterated function systems (IFS) and complex number iterations.

## Fractals Included

### Classic Fractals

- **Dragon Curve** (`dragon_curve/dragon.py`, `dragon_curve/dragon_koch_hybrid.py`)
  - Implementation using L-system rules
  - Generates the classic Heighway dragon curve
  - Includes hybrid variations combining dragon and Koch patterns
  - High-resolution output with transparent backgrounds

- **Koch Snowflake** (`koch_snowflake/koch_*.py`)
  - Recursive subdivision algorithm
  - Multiple variations and iterations
  - Configurable order and scale parameters
  - Mathematical precision using numpy arrays

- **Mandelbrot Set** (`mandelbrot/mandelbrot_*.py`)
  - Complex number iteration visualizations
  - Multiple rendering approaches (PIL, matplotlib)
  - Viewport control for zooming into specific regions
  - Various color schemes and reflections

### Nature-Inspired Fractals

- **Fractal Trees** (`fractal_trees/Tree_turtle.py`, `fractal_trees/tree.py`)
  - Recursive branching algorithms
  - Both turtle graphics and matplotlib implementations
  - Configurable parameters: branch angle, recursion depth, scale factor
  - Realistic tree-like structures

- **Fibonacci Spiral** (`fibonacci_spiral/fibonacci.py`)
  - Golden ratio visualization
  - Combines Fibonacci squares with logarithmic spiral
  - Demonstrates the relationship between Fibonacci sequence and nature

### Artistic & Experimental

- **Flame Fractals** (`flame_fractals/flame_1.py`)
  - Iterated function system (IFS) approach
  - Multiple non-linear transformations
  - Stochastic point generation (100,000+ points)
  - Beautiful organic patterns with custom color schemes

- **Triangulation Art** (`clint_fulkerson_meshes/triangulation.py`)
  - Delaunay triangulation with point clustering
  - Random colored regions with transparency
  - Edge masking for aesthetic control
  - High-DPI output suitable for printing

## Requirements

The project uses the following Python libraries:

- **numpy** - Numerical computations and array operations
- **matplotlib** - 2D plotting and visualization
- **PIL (Pillow)** - Image processing (for some Mandelbrot variations)
- **turtle** - Graphics library (for tree fractals)

## Customization

Most scripts include parameters that can be modified for different results:

### Dragon Curve
```python
iterations = 14  # Higher values = more detail (but exponentially larger)
step = 1         # Step size for drawing
dpi = 600        # Resolution for output image
```

### Koch Snowflake
```python
order = 3        # Recursion depth (0-6 recommended)
scale = 10       # Size of the base triangle
```

### Fractal Tree
```python
size = 70        # Initial branch length
levels = 7       # Recursion depth
angle = 30       # Branch angle in degrees
```

### Flame Fractal
```python
n = 100000       # Number of points to generate
# Modify transform functions for different patterns
```

## Technical Details

### L-Systems
Dragon and some Koch implementations use Lindenmayer systems (L-systems), which generate fractals through string rewriting rules:
- Start with an axiom (initial string)
- Apply production rules iteratively
- Interpret the final string as drawing commands

### Iterated Function Systems
Flame fractals use IFS, where multiple affine transformations are applied stochastically to generate points that converge to the fractal attractor.

### Recursive Algorithms
Tree fractals and some Koch implementations use direct recursive subdivision, where each branch/segment spawns smaller copies of itself.

## Credits

- Triangulation art inspired by Clint Fulkerson's geometric work
- Classic fractal algorithms based on mathematical literature

## Gallery

Example outputs can be found in each subdirectory:
- `dragon_curve/dragon_1.png`, `dragon_curve/dragon_2.png` - Dragon curve visualizations
- `dragon_curve/dragon_koch_hybrid.png` - Hybrid dragon-Koch pattern
- `fractal_trees/*.png` - Various fractal tree renderings
- `koch_snowflake/snowflake_*.png` - Koch snowflake variations
- `clint_fulkerson_meshes/*.png` - Triangulation mesh art

Run the scripts to generate your own unique variations!
