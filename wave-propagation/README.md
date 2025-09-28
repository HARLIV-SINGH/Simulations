# Wave Propagation Simulation

This project simulates **wave propagation** on a 2D grid. The central pixel oscillates sinusoidally, and the motion of each surrounding cell is determined by the **wave equation**.

Wave propagation is naturally a **3D phenomenon**. Here, the simulation maps it onto a 2D plane by representing displacement along the *z-axis* (in and out of the screen) as pixel brightness. A **grayscale colour theme** is used to accentuate the evolving wave patterns.

---

## Methodology

* **Displacement to brightness**: Brightness is scaled between 0 and 1 according to the displacement of each cell.
* **Laplacian**: The curvature of each cell is computed relative to its neighbours. This is the core of the simulation. Instead of iterating cell-by-cell, **NumPy vectorization** is used to calculate the Laplacian efficiently.
* **Equations of motion**: Acceleration is proportional to the Laplacian. Velocity and position are updated using **Euler integration** over a timestep `dt`.
* **Boundary conditions**: Edges reflect waves, producing **interference patterns** when incoming and reflected waves overlap.

---

## Observations

* Some frequencies (e.g. **1/20**) create stable patterns resembling **standing waves**, which persist for a relatively long time.
* Other frequencies (e.g. **1/60** or **1/30**) generate complex, psychedelic interference patterns as waves overlap chaotically.
* On further research, these patterns are related to **Chladni figures**, which are resonance patterns formed in vibrating systems.

---

## Files

* `wave_propagation.py` – Standalone simulation script.

---

## Requirements

Install the dependencies:

```bash
pip install numpy matplotlib
```

---

## How to Run

Run the script:

```bash
python wave_propagation.py
```

---

## Example Output

Example of expected resonance:

<img width="300" height="300" alt="image" src="https://github.com/user-attachments/assets/3fb7a537-14b3-4dbe-aea5-72f295c3ff7a" />

Example of chaotic resonance:

<img width="300" height="300" alt="image" src="https://github.com/user-attachments/assets/0dae30a4-51ab-4447-98e1-412014240beb" />


---
