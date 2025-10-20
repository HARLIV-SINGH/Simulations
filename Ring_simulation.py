import pyglet
import numpy as np

#Parameters
n = 10000 #Number of particles
G = 5.0 #Gravitational constant
M = 5000.0 #Central Max
dt = 0.001 #Timestep
f = 1 #Eccentricity

#Window
WINDOW_WIDTH, WINDOW_HEIGHT = 800, 800
win = pyglet.window.Window(WINDOW_WIDTH, WINDOW_HEIGHT, caption="Ring Simulation")

#Particles' array
pos = np.zeros((n, 2), dtype=np.float64)
vel = np.zeros((n, 2), dtype=np.float64)
acc = np.zeros((n, 2), dtype=np.float64)

#Initializing a cluster of particles
cluster_radius = 30
pos = np.random.normal(100, cluster_radius, size=(n, 2)).astype(np.float64)

#Orbital speeds of the particles
r = np.linalg.norm(pos, axis=1)
speed = np.sqrt(G * M / r)

#Tangential velocities
vel[:,0] = -f*speed * pos[:,1] / r
vel[:,1] = f*speed * pos[:,0] / r

#Pyglet batch
batch = pyglet.graphics.Batch()
particles = [pyglet.shapes.Circle(pos[i,0]+WINDOW_WIDTH//2,
                                  pos[i,1]+WINDOW_HEIGHT//2,
                                  radius=1, color=(255,255,255), batch=batch)
             for i in range(n)]

# Central mass
central = pyglet.shapes.Circle(WINDOW_WIDTH//2, WINDOW_HEIGHT//2, radius=20, color=(255,255,255), batch=batch)

#Update
def compute_acc(pos):
    dist2 = np.sum(pos**2, axis=1) + 1e-8
    dist = np.sqrt(dist2)
    acc = -G*M*pos / (dist2[:, None] * dist[:, None])
    return acc

vel_half = vel - 0.5*acc*dt

def update(dt):
    global pos, vel, acc, vel_half
    pos += vel_half*dt
    acc_new = compute_acc(pos)
    vel_half += acc_new*dt
    acc = acc_new
    for i in range(n):
        particles[i].x = pos[i,0] + WINDOW_WIDTH//2
        particles[i].y = pos[i,1] + WINDOW_HEIGHT//2


@win.event
def on_draw():
    win.clear()
    batch.draw()

acc = compute_acc(pos)
pyglet.clock.schedule_interval(update, dt)
pyglet.app.run()
