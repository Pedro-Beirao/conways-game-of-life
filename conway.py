import numpy as np
import matplotlib as mlib 
import matplotlib.pyplot as plt 
import matplotlib.animation as animation

N = 50
ON = 1
OFF = 0

grid = np.random.choice([ON,OFF], N*N, p=[0.2, 0.8]).reshape(N, N)

def update(data):
    global grid
    for gx in range(N):
        for gy in range(N):
            neighbors=0
            if(gx-1>=0 and gy+1<N and grid[gx-1,gy+1]==ON):
                neighbors+=1
            if(gy+1<N and grid[gx,gy+1]==ON):
                neighbors+=1
            if(gx+1<N and gy+1<N and grid[gx+1,gy+1]==ON):
                neighbors+=1
            if(gx-1>=0 and grid[gx-1,gy]==ON ):
                neighbors+=1
            if(gx+1<N and grid[gx+1,gy]==ON):
                neighbors+=1
            if(gx-1>=0 and gy-1>=0 and grid[gx-1,gy-1]==ON):
                neighbors+=1
            if(gy-1>=0 and grid[gx,gy-1]==ON):
                neighbors+=1
            if(gx+1<N and gy-1>=0 and grid[gx+1,gy-1]==ON):
                neighbors+=1
            
            if(grid[gx,gy]==ON):
                if(neighbors<2 or neighbors>3):
                    grid[gx,gy]=OFF
            else:
                if(neighbors==3):
                    grid[gx,gy]=ON
    mat.set_data(grid)
    return [mat]

fig, ax = plt.subplots()
mat = ax.matshow(grid, cmap=plt.cm.colors.ListedColormap(np.random.rand ( 256,3)))
ani = animation.FuncAnimation(fig, update, interval=100, save_count=50)
plt.axis('off')
plt.show()