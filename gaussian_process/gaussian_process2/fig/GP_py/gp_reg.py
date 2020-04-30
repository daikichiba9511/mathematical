import numpy as np


#TODO 色々なカーネルを同じ形式で使えるようにする, 　定義だけしてカーネルの計算はあとでできるようにしたい。

class GaussianProcess(object):
    def __init__(self):
        self.__kernel = None
        self.mu = None
        self.var = None
        self.a = None
        self.b = None

    def __size_check(self,x, y, z):
        if len(x) == len(y) and len(x) == len(z):
            pass
        else:
            raise ValueError("data size is not same!")

    def naive_gpr(self, xtrain, ytrain, xtest, kernel):
        self.__size_check(xtrain, ytrain, xtest)

        N = len(ytrain)
        M = len(xtest)
        K = [0.]*N
        for i in range(N):
            for j in range(N):
                K[i, j] = self.__kernel(x=xtrain[i], x_prime=xtrain[j])
        K_inv = np.linalg.pinv(k)
        yy = K_inv * ytrain
        k = [0.]*N
        mu = [0.]*M
        var = [0.]*M
        for m in range(M):
            for n in range(N):
                k[n] = self.__kernel(xtrain[n], xtest[n])
            s = kernel(xtest[m], xtest[m])
            mu[m] = k * yy
            var[m] = s - k * K_inv * k.T
        self.mu = mu
        self.var = var
        return self

    def RBFkernel(self, x=None, x_prime=None, a=1, b=1):
        self.a = a
        self.b = b
        self.kernel =  self.a * np.exp( - (x - x_prime)**2 / self.b )

    def LinearKernel(
        self, x : np.ndarray =None, x_prime : np.ndarray = None
        ):
        self.kernel = x.T * x_prime

    def ExpKernel(
        self, x : np.ndarray = None, x_prime : np.ndarray = None, b=1
                ):

        self.b = b
        self.kernel = np.exp( - np.abs(x - x_prime) / self.b)

    def PeriodicKernel(
        self, x : np.ndarray = None, x_prime : np.ndarray = None, a=1, b=1
        ):
        self.a = a
        self.b = b
        self.kernel = np.exp(a * np.cos( np.abs(x - x_prime) / b))



def test_gpr():
    xtrain = np.random.rand(100)
    xtest  = np.random.rand(100)
    ytrain  = np.random.rand(100)

    gp = GaussianProcess()
    gp.LinearKernel()
    model = gpr.naive_gpr(xtrain, ytrain, xtest)



if __name__ == "__main__":
    test_gpr()