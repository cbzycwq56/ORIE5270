from scipy.optimize import minimize, rosen_der
import numpy as np
def rosen(x):
    return 100*(x[1]**2-2*x[1]*x[0]**2+x[0]**4)+1-2*x[0]+x[0]**2+(100*(x[2]-x[1]**2)**2+(1-x[1])**2)

for i in range(100):
    start=[2,2,2]
    for j in range(3):
        start[j]=np.random.uniform(-10,10)
    print(minimize(rosen,start,method='BFGS',jac=rosen_der).x)
