def f(t, y):
    """Function f(t, y) = t - y^2"""
    return t - y**2

def euler():
    """Euler Method"""
    a = 0
    b = 2.0
    n = 10
    h = (b - a) / n  # Step size
    t = 0.0
    y = 1.0  # Initial condition y(0) = 1

    for _ in range(n):
        yt = f(t, y)  # Compute f(t, y)
        y = y + h * yt
        t = t + h

    print(y)

def runge_kutta():
    """Runge-Kutta Method (RK4)"""
    a = 0
    b = 2.0
    n = 10
    h = (b - a) / n  # Step size
    t = 0.0
    y = 1.0  # Initial condition y(0) = 1

    for _ in range(n):
        k1 = h * f(t, y)
        k2 = h * f(t + h / 2, y + k1 / 2)
        k3 = h * f(t + h / 2, y + k2 / 2)
        k4 = h * f(t + h, y + k3)

        y = y + (1.0 / 6.0) * (k1 + 2 * k2 + 2 * k3 + k4)
        t = t + h  # Move to the next time step

    print(y)

def main():
    """Run both methods"""
    euler()
    runge_kutta()

if __name__ == "__main__":
    main()
