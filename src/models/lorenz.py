'''
  File: lorenz.py
 
  Author: Thomas Kost
  
  Date: 08 August 2021
  
  @breif function for lorenz chaotic system, and plotting script
 '''
import numpy as np
import matplotlib.pyplot as plt
def lorenz(x :np.array, beta: np.array)->np.array:
    '''
    x: position state vector of lorenz system

    beta: vector of lorenz parameters

    return: derivative of state vector

    '''

    dx = np.array([ beta[0]*(x[1]-x[0]),
                    x[0]*(beta[1]-x[2])-x[1],
                    x[0]*x[1]-beta[2]*x[2]])
    return dx

def step_lorenz(x:np.array, beta:np.array, dt:float)->np.array:
    next_x = x + lorenz(x,beta)*dt
    return next_x

if __name__ == "__main__":
    dt = 0.001
    t = np.arange(0,50,dt)
    x = np.zeros((3,len(t)))
    x_0 = np.array((0,1,20))
    b = np.array((10,28,8/3.0))
    
    for i in range(len(t)):
      if(i == 0):
        x[:,i] = x_0
      else:
        x[:,i] = step_lorenz(x[:,i-1],b,dt)

    ax = plt.figure().add_subplot(projection='3d')
    ax.plot(x[0,:], x[1,:], x[2,:], lw=0.5)
    ax.set_xlabel("X Axis")
    ax.set_ylabel("Y Axis")
    ax.set_zlabel("Z Axis")
    ax.set_title("Lorenz Attractor")
    plt.show()
