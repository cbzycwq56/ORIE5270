from scipy.optimize import minimize, rosen_der
import numpy as np
def rosen(x):
    """
    this function output the rosenbrock function
    :param x: It is the input of the rosenbrock function. It is a three dimentional vector
    :return: it returns the rosenbrock funtion
    """
    return 100*(x[1]**2-2*x[1]*x[0]**2+x[0]**4)+1-2*x[0]+x[0]**2+(100*(x[2]-x[1]**2)**2+(1-x[1])**2)
def gradient(x):
    """
    This function output the gradient of the rosenbrock function
    :param x: It is the input of the rosenbrock function. It is a three dimentional vector
    :return: it returns the gradient of the rosenbrock function
    """
    return np.array([400*x[0]**3-400*x[1]*x[0]+2*x[0]-2,
            400*x[1]**3-400*x[2]*x[1]-200*x[0]**2+202*x[1]-2
            ,-200*x[1]**2+200*x[2],])
if __name__ == "__main__":
    for i in range(100):
        start=[2,2,2]
        for j in range(3):
            start[j]=np.random.uniform(-10,10)
            res=minimize(rosen,start,method='BFGS',jac=gradient)
        print("The optimal solution is:"+str(res.x))
        print("The optimal function value is: "+ str(res.fun))
