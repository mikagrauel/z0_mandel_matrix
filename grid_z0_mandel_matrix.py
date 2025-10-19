"""
Z0-Mandel-Matrix Visualization (z₀ ≠ 0)

This script generates a visualization of the Z0-Mandel-Matrix, illustrating how
the Mandelbrot set changes when the iteration

    zₙ₊₁ = zₙ² + c

starts from different initial values z₀ ≠ 0. Each panel corresponds to a Mandelbrot
variant for a specific z₀ on a regular grid over the complex plane.

Author: Mika Grauel
"""

import numpy as np
import matplotlib.pyplot as plt
from tqdm import tqdm

# =========================================
# Configuration
# =========================================
GRID_N = 1000               # Number of panels along each axis in the Z0-Mandel-Matrix
PANEL_SIZE = 5              # Resolution (pixels) of each Mandelbrot variant
MAX_ITER = 5                # Maximum iterations for escape test
ESCAPE_RADIUS = 2.0         # Escape radius threshold for divergence
Z0_RADIUS = 3               # Range of z₀ values sampled: [-Z0_RADIUS, Z0_RADIUS] for both real and imag parts
CMAP = 'turbo'              # Colormap suitable for visualizing iteration counts
OUTPUT_FILE = "z0_mandel_matrix.png"

# =========================================
# Domain for c-values (identical for all panels)
# =========================================
RE_MIN, RE_MAX = -2.0, 1.0
IM_MIN, IM_MAX = -1.5, 1.5
re = np.linspace(RE_MIN, RE_MAX, PANEL_SIZE)
im = np.linspace(IM_MIN, IM_MAX, PANEL_SIZE)
c_grid = re[np.newaxis, :] + 1j * im[:, np.newaxis]

# =========================================
# Generate z₀ values across the Z0-Mandel-Matrix
# =========================================
z0_real = np.linspace(-Z0_RADIUS, Z0_RADIUS, GRID_N)
z0_imag = np.linspace(-Z0_RADIUS, Z0_RADIUS, GRID_N)
z0_values = [x + 1j*y for y in z0_imag for x in z0_real]

# =========================================
# Compute a Mandelbrot variant for a given z₀
# =========================================
def mandelbrot_variant(z0, max_iter=MAX_ITER):
    """
    Compute a Mandelbrot variant starting from a specific initial value z₀.

    Parameters
    ----------
    z0 : complex
        The initial value for the iteration
    max_iter : int
        Maximum number of iterations for the escape-time algorithm

    Returns
    -------
    img : np.ndarray
        2D array representing the number of iterations until escape for each c
    """
    z = np.full_like(c_grid, z0, dtype=np.complex128)
    img = np.zeros_like(z, dtype=np.float32)
    mask = np.ones(z.shape, dtype=bool)

    for i in range(max_iter):
        z[mask] = z[mask]**2 + c_grid[mask]
        escaped = np.abs(z) > ESCAPE_RADIUS
        img[mask & escaped] = i
        mask &= ~escaped
        if not mask.any():
            break

    img[mask] = max_iter
    return img

# =========================================
# Prepare full Z0-Mandel-Matrix image
# =========================================
canvas_size = GRID_N * PANEL_SIZE
canvas = np.zeros((canvas_size, canvas_size), dtype=np.float32)

print(f"Generating Z0-Mandel-Matrix with {GRID_N}×{GRID_N} panels...")
for idx, z0 in enumerate(tqdm(z0_values, desc="Processing z0 variants")):
    row = idx // GRID_N
    col = idx % GRID_N
    mandel_img = mandelbrot_variant(z0)
    canvas[
        row * PANEL_SIZE:(row + 1) * PANEL_SIZE,
        col * PANEL_SIZE:(col + 1) * PANEL_SIZE
    ] = mandel_img

# =========================================
# Display and save the Z0-Mandel-Matrix
# =========================================
plt.figure(figsize=(10, 10))
plt.imshow(canvas, cmap=CMAP, origin='lower')
plt.axis('off')
plt.title("Z0-Mandel-Matrix: Mandelbrot Variants for z₀ ≠ 0", fontsize=14)
plt.tight_layout()
plt.savefig(OUTPUT_FILE, dpi=300, bbox_inches='tight')
plt.show()

print(f"Z0-Mandel-Matrix image saved as: {OUTPUT_FILE}")
