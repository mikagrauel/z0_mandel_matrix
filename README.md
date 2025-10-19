# Z0-Mandel-Matrix

This repository contains two implementations for exploring the **Z0-Mandel-Matrix**, a generalization of the Mandelbrot set where the iteration

\[
z_{n+1} = z_n^2 + c
\]

starts from different initial values \(z_0 \neq 0\). This allows investigation of structural variations and the emergence of stability “islands” in the Mandelbrot family.

## Implementations

1. **Python (`mandelbrot_raster.py`)**  
   - Generates a grid of full Mandelbrot variants for varying \(z_0\).  
   - Produces a static image showing the structural diversity.

2. **JavaScript (`z0_mandel_matrix.html`)**  
   - Interactive web tool computing a similarity measure relative to the classical set \(M_0\).  
   - Binary visualization: black = similar, white = dissimilar.  
   - Adjustable grid resolution and similarity threshold.  
   - Allows fast exploration of stability regions and export of images.

## Usage

- **Python:** `python mandelbrot_raster.py`  
- **JavaScript:** open `z0_mandel_matrix.html` in a web browser.

## References

- Mandelbrot, B. B. (1982). *The Fractal Geometry of Nature*. W. H. Freeman.  
- Peitgen, H.-O., Jürgens, H., & Saupe, D. (1986). *Chaos and Fractals*. Springer.  
- Devaney, R. L. (1990). *Chaos, Fractals, and Dynamics: Computer Experiments in Mathematics*. Addison-Wesley.


