# %%
import numpy as np
import pyglet

rng = np.random.default_rng()

screen_height = 1080
screen_width = 1920
origin = np.array([screen_width/2, (screen_height/2)])
radius = 5
m = 1
G = 600
scale = 25

positions = np.array([
    [0.0, -300.0],      
    [150.0, -300.0],    
    [0.0, -100.0]
])
velocities = np.array([
    [0.0, -1.0],      
    [-1.0, 1.0],    
    [0.0, 1.0]
])

win = pyglet.window.Window(screen_width, screen_height, caption="SIMULATION")

bodies = [
    pyglet.shapes.Circle(origin[0] + positions[0][0], origin[1] + positions[0][1], radius, color=(255, 0, 0)),
    pyglet.shapes.Circle(origin[0] + positions[1][0], origin[1] + positions[1][1], radius, color=(0, 255, 0)),
    pyglet.shapes.Circle(origin[0] + positions[2][0], origin[1] + positions[2][1], radius, color=(0, 0, 255))
]

@win.event
def on_draw():
    win.clear()
    for body in bodies:
        body.draw()

dt = 0.00000001
def update(dt):
    global positions, velocities
    acc = np.zeros_like(positions)
    
    for i in range(len(positions)):
        for j in range(len(positions)):
            if i != j:
                r = positions[i] - positions[j]
                mag = np.linalg.norm(r)
                acc[i] += -G * r / (mag**3)
    
    velocities += acc * dt * scale
    positions += velocities * dt * scale
    
    for i, body in enumerate(bodies):
        body.x = origin[0] + positions[i,0]
        body.y = origin[1] + positions[i,1]
    
if __name__ == "__main__":
    pyglet.clock.schedule_interval(update, dt)
    pyglet.app.run()


