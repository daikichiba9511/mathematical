import numpy as np
import matplotlib.pyplot as plt

import kernel

from pathlib import Path

np.random.seed(123)
plt.style.use("ggplot")

ITER_NUMS = 5
DATA_NUMS = 100

def gaussian_plot():
    data1 = np.random.rand(DATA_NUMS)
    data2 = np.random.rand(DATA_NUMS)
    x = np.linspace(-5, 5, DATA_NUMS)
    fig, ax = plt.subplots(figsize=(8, 6))
    
    for _ in range(ITER_NUMS):
        a = np.random.randn(1)
        b = np.random.randn(1)
        rbf = kernel.RBFkernel(data1, data2, a, b)
        ax.plot(x, rbf, label="a={a}, b={b}".format(a=a, b=b))

    fig.legend()
    plt.show()
    fig.savefig(Path.cwd()/"gaussian_process"/"gaussian_process2"/"fig"/"figure"/"gaussian_kernel_py.png")
    plt.close()

def linear_plot():
    fig, ax = plt.subplots(figsize=(8, 6))
    x = np.linspace(-5, 5, DATA_NUMS)
    for _ in range(ITER_NUMS):
        data1 = np.random.rand(DATA_NUMS)
        data2 = np.random.rand(DATA_NUMS)
        lk = kernel.LinearKernel(data1, data2)
        ax.plot(x, lk)
    plt.show()
    fig.savefig(Path.cwd()/"gaussian_process"/"gaussian_process2"/"fig"/"figure"/"linear_kernel_py.png")
    plt.close()

def exponential_plot():
    data1 = np.random.rand(DATA_NUMS)
    data2 = np.random.rand(DATA_NUMS)
    x = np.linspace(-5, 5, DATA_NUMS)
    fig, ax = plt.subplots(figsize=(8, 6))

    for _ in range(ITER_NUMS):
        b = np.random.randn(1)
        rbf = kernel.ExpKernel(data1, data2,  b)
        ax.plot(x, rbf, label="b={b}".format(b=b))
    
    fig.legend()
    plt.show()
    fig.savefig(Path.cwd()/"gaussian_process"/"gaussian_process2"/"fig"/"figure"/"EXP_kernel_py.png")
    plt.close()

def periodic_plot():
    data1 = np.random.rand(DATA_NUMS)
    data2 = np.random.rand(DATA_NUMS)
    x = np.linspace(-5, 5, DATA_NUMS)
    fig, ax = plt.subplots(figsize=(8, 6))
    
    for _ in range(ITER_NUMS):
        a = np.random.randn(1)
        b = np.random.randn(1)
        rbf = kernel.PeriodicKernel(data1, data2, a, b)
        ax.plot(x, rbf, label="a={a}, b={b}".format(a=a, b=b))

    fig.legend()
    plt.show()
    fig.savefig(Path.cwd()/"gaussian_process"/"gaussian_process2"/"fig"/"figure"/"periodic_kernel_py.png")
    plt.close()


if __name__ == "__main__":
    # gaussian_plot()
    # linear_plot()
    # exponential_plot()
    periodic_plot()