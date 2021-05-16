import random
from typing import List
Vector = List[float]

from linear_algebra import distance, add, scalar_multiply
from linear_algebra import vector_mean
inputs = [(x,10*x) for x in range(-50, 50)]
# Këtu shenojme vlerat per x dhe y si:
# inputs = [(x,x) for x in range(-50, 50)]
# inputs = [(x,10*x) for x in range(-50, 50)]
# inputs = [(x,x*x) for x in range(-50, 50)]
# inputs = [(x,x/10) for x in range(-50, 50)]
def linear_gradient(x: float, y: float, theta: Vector) -> Vector:
    slope, intercept = theta
    predicted = slope * x + intercept # The prediction of the model.
    error = (predicted - y) # error is (predicted - actual).
    squared_error = error ** 2 # We'll minimize squared error
    grad = [2 * error * x, 2 * error] # using its gradient.
    return grad
def gradient_step(v: Vector, gradient: Vector, step_size: float) -> Vector:
    """Moves `step_size` in the `gradient` direction from `v`"""
    assert len(v) == len(gradient)
    step = scalar_multiply(step_size, gradient)
    return add(v, step)
def sum_of_squares_gradient(v: Vector) -> Vector:
    return [2 * v_i for v_i in v]
# pick a random starting point
learning_rate = 0.001
theta = [random.uniform(-1, 1), random.uniform(-1, 1)]
for epoch in range(5000):
# Compute the mean of the gradients
    grad = vector_mean([linear_gradient(x, y, theta) for x, y in inputs])
# Take a step in that direction
    theta = gradient_step(theta, grad, -learning_rate)
print(epoch, theta)
slope, intercept = theta
# assert 19.9 < slope < 20.1, "slope should be about 20"
# assert 4.9 < intercept < 5.1, "intercept should be about 5"
