import numpy as np

import kernel

#TODO 一応は計算は回るようになったので正しくできてるか確認する。

class GaussianProcess(object):
    def __init__(self, kernel):
        self.__kernel = kernel
        self.mu = None
        self.var = None

    def __size_check(self,x, y, z):
        if len(x) == len(y) and len(x) == len(z):
            pass
        else:
            raise ValueError("data size is not same!")

    def naive_gpr(self, xtrain, ytrain, xtest):
        self.__size_check(xtrain, ytrain, xtest)

        N = len(ytrain)
        M = len(xtest)
        K = [[0.]*N for _ in range(N)]
        for i in range(N):
            for j in range(N):
                K[i][j] = self.__kernel(x=xtrain[i], x_prime=xtrain[j])
        K_inv = np.linalg.pinv(K)
        yy = K_inv * ytrain
        k = [0.]*N
        mu = [0.]*M
        var = [0.]*M
        for m in range(M):
            for n in range(N):
                k[n] = self.__kernel(xtrain[n], xtest[n])
            s = self.__kernel(xtest[m], xtest[m])
            mu[m] = k * yy
            var[m] = s - np.array(k) * K_inv * np.array(k).T
        self.mu = np.array(mu)
        self.var = np.array(var)
        return self


def test_gpr():
    xtrain = np.random.rand(100)
    xtest  = np.random.rand(100)
    ytrain  = np.random.rand(100)
    k = kernel.LinearKernel()
    gpr = GaussianProcess(kernel=k)
    model = gpr.naive_gpr(xtrain, ytrain, xtest)
    print("variance : ", model.var.shape)
    print("mean : ", model.mu.shape)


if __name__ == "__main__":
    test_gpr()