import argparse
import numpy as np
import matplotlib.pyplot as plt

print("We need to reference the python script that is called BrakingCode.py, followed by the desired values of velocity (In km/h), mass (In kg) and coefficient of friction in that particular order")
print("Example, it should look like this: BrakingCode.py 80 1000 0.2 ")


def brake_distance(velocity, mass, friction):
    # Gravity
    g = 9.81

    # Braking force
    braking_f = friction * mass * g * (1 + mass * g / (friction * mass * g))

    # Deceleration
    deceleration = braking_f / mass

    # Braking time formula
    braking_t = velocity / abs(deceleration)

    # Braking distance formula
    braking_d = velocity * braking_t + 0.5 * deceleration * braking_t**2

    return braking_d, braking_t


def plot_graph(velocity, time, deceleration):
    t = np.linspace(0, time, 100)
    s = velocity * t + 0.5 * deceleration * t**2

    plt.plot(t, s, label='Braking Distance')
    plt.xlabel('Time (seconds)')
    plt.ylabel('Distance (m)')
    plt.show()


def main():
    parser = argparse.ArgumentParser(description="Program for calculating and graphing the braking distance")
    parser.add_argument("velocity", type=float)
    parser.add_argument("mass", type=float)
    parser.add_argument("friction", type=float)

    args = parser.parse_args()

    distance, time = brake_distance(args.velocity, args.mass, args.friction)

    print(f"The braking distance will be {distance:.2f} meters.")
    print(f"The braking time will be {time:.2f} seconds.")

    plot_graph(args.velocity, time, time)  # Assuming 9.8 m/s^2 for acceleration due to gravity


if __name__ == "__main__":
    main()