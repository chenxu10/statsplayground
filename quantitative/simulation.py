"""
Simulate 100 data points,when use linear regression to
do OLS, slope=2, r-square=0.8
"""

import numpy as np
import math

from sklearn.linear_model import LinearRegression

def generate_rnorm_x(mu=0,sigma=1,n=100):
    x = np.random.normal(mu,sigma,n)
    return x

if __name__ == "__main__":
    # sx = 1
    # sy = sx * 2/math.sqrt(0.8)
    # se = math.sqrt(sy**2-2**2)


    # x = np.array([generate_rnorm_x(n=100)])
    # y = 2 * x + generate_rnorm_x(n=100) * se
    
    # reg = LinearRegression().fit(x,y)
    # print(reg.score(x,y))
    # print(reg.coef_)

    print("every thing is working")