import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from random import randrange
from math import exp, log, sqrt


LEARNING_RATE = 0.027
global m
global thetas

df = pd.read_csv("ex1data1.csv", header=None, names=["x", "y"]) # Giving the data headers with names x and y
train_x, train_y = [np.array([df["x"]]), np.array([df["y"]])] # Assigning the columns to np.arrays
train_x, train_y = np.transpose(train_x), np.transpose(train_y) # changing from a 1x97 to a 97x1 for consistency
ax = plt.subplot(2, 1, 1)
ax.scatter(train_x, train_y)
train_x = np.append(np.ones(shape=(train_x.shape)), train_x, axis=1)

m = train_x.shape[0] #Initialize m
thetas = np.zeros(shape=(train_x.shape[1], 1)) # Initialize thetas as zero


#plt.show()

print(train_x.shape, train_y.shape, thetas.shape)

def prediction(X, theta_v):
    #This assumes that both theta and x are vectors

    return np.matmul(X, theta_v)

def cost_function(theta_v, X, y):
    H = prediction(X, theta_v)
    S = sum((H - y)**2)
    J = S/(2*m)
    #print(S, J)
    return J


def grad_desc(theta_v, X, y, iters=1):

    J_hist = np.zeros(shape=(iters, 1))
    #This isnt right but im close
    for i in range(iters):
        theta_v -= LEARNING_RATE*1/(2*m) * np.transpose(np.matmul(np.transpose(prediction(X, theta_v)-y), X))
        thetas = theta_v
        J_hist[i][0] = cost_function(thetas, X, y)
    return J_hist



J_hist = grad_desc(thetas, train_x, train_y, iters=4000)

ax.plot(train_x, prediction(train_x, thetas))

ax2 = plt.subplot(2, 1, 2)
print(J_hist.shape)
ax2.plot( [i for i in range(len(J_hist))], J_hist[:,0])
plt.show()