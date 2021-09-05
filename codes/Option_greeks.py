import math
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

import mpl_toolkits.mplot3d.axes3d as p3
from Option_pricing import d1f, N, dN

# Functions for Greeks

def BSM_delta(St, K, T, r, sigma):


 d1 = d1f(St, K, T, r, sigma)
 delta = N(d1)
 return delta
def BSM_gamma(St, K, T, r, sigma):

 d1 = d1f(St, K, T, r, sigma)
 gamma = dN(d1) / (St * sigma * math.sqrt(T))
 return gamma

def BSM_theta(St, K, T, r, sigma):
 d1 = d1f(St, K, T, r, sigma)
 d2 = d1 - sigma * math.sqrt(T)
 theta = -(St * dN(d1) * sigma / (2 * math.sqrt(T))
 + r * K * math.exp(-r * (T)) * N(d2))
 return theta

def BSM_vega(St, K, T, r, sigma):
    
 d1 = d1f(St, K,  T, r, sigma)
 vega = St * dN(d1) * math.sqrt(T)
 return vega


# Plotting the Greeks

def plot_greeks(St, K, T, r, sigma):
 
 points=100

# Delta plot
 plt.subplot(221)
 klist = np.linspace(80, 120, points)
 vlist = [BSM_delta(S, K, T, r, sigma) for S in klist]
 plt.plot(klist, vlist)
 plt.grid()
 plt.xlabel('St  ')
 plt.ylabel('Delta')
 # Gamma plot
 plt.subplot(222)
 tlist = np.linspace(80, 120, points)
 vlist = [BSM_gamma(S, K, T, r, sigma) for S in tlist]
 plt.plot(tlist, vlist)
 plt.grid(True)
 plt.xlabel('St')
 plt.ylabel('Gamma')
 # Theta plot
 plt.subplot(223)
 rlist = np.linspace(1, 20, points)
 vlist = [BSM_theta(St, K, T1, r, sigma) for T1 in rlist]
 plt.plot(tlist, vlist)
 plt.grid(True)
 plt.xlabel('maturity $T$')
 plt.ylabel('Theta')
 plt.axis('tight')
# Vega plot
 plt.subplot(224)
 slist = np.linspace(0.01, 0.5, points)
 vlist = [BSM_vega(St, K, T, r, sigma1) for sigma1 in slist]
 plt.plot(slist, vlist)
 plt.grid(True)
 plt.xlabel('volatility $\sigma$')
 plt.ylabel('Vega')
 plt.tight_layout()

 return plt.show()


