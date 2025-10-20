#Imports
import pyglet
import numpy as np
import colorsys

#Parameters
GRID_WIDTH = 150
GRID_HEIGHT = 150
CELL_SIZE = 5
SCREEN_WIDTH = CELL_SIZE*GRID_WIDTH
SCREEN_HEIGHT = CELL_SIZE*GRID_HEIGHT

#Physics parameters
C_SQUARED = 15   # Wave speed
AMPLITUDE = 2    # Amplitude
FREQUENCY = 0.1  # Frequency
DT = 0.1 # Timestep

#Initial conditions
grid_pos = np.zeros((GRID_WIDTH, GRID_HEIGHT), dtype=np.float32)
grid_vel = np.zeros((GRID_WIDTH, GRID_HEIGHT), dtype=np.float32)
time = 0

win = pyglet.window.Window(SCREEN_WIDTH, SCREEN_HEIGHT, caption = "Wave Propagation")

#Value to color - Red is positive and blue is negative
def value_to_colour(displacement, amplitude):
    if amplitude == 0:
        return (0, 0, 0)
    brightness = min(1.0, abs(displacement) / amplitude)
    brightness = max(0.0, brightness)
    color_value = int(brightness * 255)
    
    if displacement > 0:
        return (0, 0, color_value)
    else:
        return (color_value, 0, 0)
    
#Creating the grid
batch = pyglet.graphics.Batch()
sprites = []
for i in range(GRID_WIDTH):
    column = []
    for j in range(GRID_HEIGHT):
        column.append(pyglet.shapes.Rectangle(i*CELL_SIZE, j*CELL_SIZE, CELL_SIZE, CELL_SIZE, color=(0,0,0), batch=batch))
    sprites.append(column)

#Updating
def update(dt):
    global grid_pos, grid_vel, time
    time += DT

    grid_pos[GRID_WIDTH//2, GRID_HEIGHT//2] = AMPLITUDE * np.sin(time * FREQUENCY * 2 * np.pi)
    
    # Copy the current positions
    old_pos = grid_pos.copy()
    
    # Calculate the Laplacian
    laplacian = (old_pos[2:, 1:-1] + old_pos[:-2, 1:-1] +
                 old_pos[1:-1, 2:] + old_pos[1:-1, :-2] -
                 4 * old_pos[1:-1, 1:-1])
                 
    # Update velocities
    grid_vel[1:-1, 1:-1] += (C_SQUARED * laplacian) * dt
    # Update positions
    grid_pos[1:-1, 1:-1] += grid_vel[1:-1, 1:-1] * dt

    # Update the color of each cell
    for i in range(GRID_WIDTH):
        for j in range(GRID_HEIGHT):
            displacement = grid_pos[i][j]
            sprites[i][j].color = value_to_colour(displacement, AMPLITUDE)
            
@win.event
def on_draw():
    win.clear()
    batch.draw()

if __name__ == "__main__":
    pyglet.clock.schedule(update)
    pyglet.app.run()