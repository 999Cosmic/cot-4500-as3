def euler_method(f, t0, y0, t_final, num_steps):
    h = (t_final - t0) / num_steps

    t = t0
    y = y0
    iterations = [(t, y)]

    for _ in range(num_steps):
        slope = f(t, y)
        y = y + h * slope
        t = t + h
        iterations.append((t, y))

    return iterations, y

def runge_kutta(f, t0, y0, t_final, num_steps):
    h = (t_final - t0) / num_steps

    t = t0
    y = y0
    iterations = [(t, y)]

    for _ in range(num_steps):
        k1 = f(t, y)
        k2 = f(t + h / 2, y + h * k1 / 2)
        k3 = f(t + h / 2, y + h * k2 / 2)
        k4 = f(t + h, y + h * k3)

        y = y + (h / 6) * (k1 + 2 * k2 + 2 * k3 + k4)
        t = t + h
        iterations.append((t, y))

    return iterations, y

def f(t, y):
    return t - y**2