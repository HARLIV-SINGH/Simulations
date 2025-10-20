# Ring formation Simulation

This project simulates ring formation involving a large number of small bodies forming a ring around a large central body. Each of the small bodies are attracted to the central body by a gravitational force and the inter-gravitational forces between them are ignored. The final product is a beautiful ring system, much like Saturn.

## Features

* Uses leapfrog over euler integration, making the simulation more stable.
* Adjustable masses, positions, number of particles, strength of gravity.

## Files

* `Ring_simulation.py` – Python script.

## How to Run

1. Install dependencies (if not already installed):

   ```bash
   pip install numpy pyglet
   ```
2. Run the script:

   ```bash
   python Ring_simulation.py
   ```

## Example Output

<img width="531" height="523" alt="5" src="https://github.com/user-attachments/assets/bade9e7b-4de8-476d-ab2a-ed923f33d1e2" />

NOTE: You may have to run this code for 15+ minutes to achieve a similar output.

---

**Next steps:** Scale this to a 3D version.

