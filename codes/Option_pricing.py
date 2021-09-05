
import math
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

from scipy.integrate import quad

def dN(x):

 return math.exp(-0.5 * x ** 2) / math.sqrt(2 * math.pi)
def N(d):

 return quad(lambda x: dN(x), -20, d, limit=50)[0]
def d1f(St, K, T, r, sigma):

 d1 = (math.log(St / K) + (r + 0.5 * sigma ** 2)
 * (T)) / (sigma * math.sqrt(T))
 return d1

def BSM_call_value(St, K, T, r, sigma):

 d1 = d1f(St, K, T, r, sigma)
 d2 = d1 - sigma * math.sqrt(T)
 call_value = St * N(d1) - math.exp(-r * (T)) * K * N(d2)
 return call_value
 

def mc(S0, K, T, r, sigma, I):

 z = np.random.standard_normal(I) # pseudorandom numbers
 ST = S0 * np.exp((r - 0.5 * sigma ** 2) * T + sigma * np.sqrt(T) * z)
 
 hT = np.maximum(ST - K, 0) # payoffs at maturity
 C0 = np.exp(-r * T) * np.sum(hT) / I # Monte Carlo estimator

 return C0

def plot_option(St,K,T,r,sigma):

 plt.figure(figsize=(10, 8.3))
 points = 100


# C(K) plot
 plt.subplot(221)
 klist = np.linspace(80, 120, points)
 vlist = [BSM_call_value(St, K, T, r, sigma) for K in klist]
 plt.plot(klist, vlist)
 plt.grid()
 plt.xlabel('strike $K$')
 plt.ylabel('present value')
 # C(T) plot
 plt.subplot(222)
 tlist = np.linspace(0.0001, 1, points)
 vlist = [BSM_call_value(St, K, T, r, sigma) for T in tlist]
 plt.plot(tlist, vlist)
 plt.grid(True)
 plt.xlabel('maturity $T$')
 # C(r) plot
 plt.subplot(223)
 rlist = np.linspace(0, 0.1, points)
 vlist = [BSM_call_value(St, K, T, r, sigma) for r in rlist]
 plt.plot(tlist, vlist)
 plt.grid(True)
 plt.xlabel('short rate $r$')
 plt.ylabel('present value')
 plt.axis('tight')
# C(sigma) plot
 plt.subplot(224)
 slist = np.linspace(0.01, 0.5, points)
 vlist = [BSM_call_value(St, K, T, r, sigma) for sigma in slist]
 plt.plot(slist, vlist)
 plt.grid(True)
 plt.xlabel('volatility $\sigma$')
 plt.tight_layout()

 return plt.show()
 

