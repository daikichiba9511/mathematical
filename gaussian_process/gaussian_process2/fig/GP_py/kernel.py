import numpy as np
import matplotlib.pyplot as plt

plt.style.use("ggplot")

def RBFkernel(x, x_prime, a, b):
    return a * np.exp( - (x - x_prime)**2 / b )

def LinearKernel(x : np.ndarray, x_prime : np.ndarray):
    return x.T * x_prime

def ExpKernel(x : np.ndarray, x_prime : np.ndarray, b):
    return np.exp( - np.abs(x - x_prime) / b)

def PeriodicKernel(x : np.ndarray, x_prime : np.ndarray, a, b):
    return np.exp(a * np.cos( np.abs(x - x_prime) / b))


if __name__ == "__main__":
   pass