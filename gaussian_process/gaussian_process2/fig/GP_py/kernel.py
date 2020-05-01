import numpy as np
import matplotlib.pyplot as plt

plt.style.use("ggplot")

class RBFkernel(object):
    def __init__(self, a, b):
        self._a = a
        self._b = b
    def __call__(self,x, x_prime):
        return self._a * np.exp( - (x - x_prime)**2 / self._b )

class LinearKernel(object):
    def __init__(self):
        pass
    def __call__(self,x : np.ndarray, x_prime : np.ndarray):
        return x.T * x_prime

class ExpKernel(object):
    def __init__(self, b):
        self._b = b
    def __call__(self, x : np.ndarray, x_prime : np.ndarray, b):
        return np.exp( - np.abs(x - x_prime) / self._b)

class PeriodicKernel(object):
    def __init__(self,a, b):
        self._a = a
        self._b = b

    def __call__(self,x : np.ndarray, x_prime : np.ndarray):
        return np.exp(self._a * np.cos( np.abs(x - x_prime) / self._b))


if __name__ == "__main__":
   pass