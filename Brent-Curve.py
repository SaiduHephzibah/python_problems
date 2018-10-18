from scipy import optimize
def f(x):
    return -np.exp(-(x - 0.7)**2)
result = optimize.minimize_scalar(f)
result.success # check if solver was successful
x_min = result.x
x_min 
x_min - 0.7 
