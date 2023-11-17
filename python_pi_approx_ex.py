import random

def estimate_pi_monte_carlo(n):
    num_inside_circle = 0
    for i in range(n):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)
        if x**2 + y**2 <= 1:
            num_inside_circle += 1
    return 4 * num_inside_circle / n
approx_pi = estimate_pi_monte_carlo(1000000)
print(approx_pi)
