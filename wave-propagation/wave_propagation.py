#Imports
import pyglet
import numpy as np

#Parameters
GRID_WIDTH = 150
GRID_HEIGHT = 150
CELL_SIZE = 5
SCREEN_WIDTH = CELL_SIZE*GRID_WIDTH
SCREEN_HEIGHT = CELL_SIZE*GRID_HEIGHT

#Physics parameters
C_SQUARED = 25
FREQUENCY = (1/20)
AMPLITUDE = 1
DT = 0.001

#Initial conditions
grid_pos = np.zeros((GRID_WIDTH, GRID_HEIGHT), dtype=np.float32)
grid_vel = np.zeros((GRID_WIDTH, GRID_HEIGHT), dtype=np.float32)
time = 0

win = pyglet.window.Window(SCREEN_WIDTH, SCREEN_HEIGHT, caption = "Standing waves")

#Value to color
def value_to_colour(displacement, amplitude):
    if amplitude == 0:
        return(0,0,0)
    brightness = min(1.0, abs(displacement) / amplitude)
    val = int(255 * brightness)
    return (val, val, val)
    
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
    time += dt
    grid_pos[GRID_WIDTH//2][GRID_HEIGHT//2] = AMPLITUDE*np.sin(time*FREQUENCY*2*np.pi)
    old_pos = grid_pos.copy()
    
    laplacian = (old_pos[2:, 1:-1] + old_pos[:-2, 1:-1] +
                 old_pos[1:-1, 2:] + old_pos[1:-1, :-2] -
                 4 * old_pos[1:-1, 1:-1])
    grid_vel[1:-1, 1:-1] += (C_SQUARED * laplacian) * dt
    grid_vel[1:-1, 1:-1] *= 0.995
    grid_pos[1:-1, 1:-1] += grid_vel[1:-1, 1:-1] * dt

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
