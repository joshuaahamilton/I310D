def calculate_volume_of_sphere(radius):
    if radius < 0:
        raise ValueError("Radius cannot be negative.")
    pi = 3.14
    volume = (4 / 3) * pi * (radius ** 3)
    return volume

if __name__ == "__main__":
    radii = [30, 40]
    for r in radii:
        volume = calculate_volume_of_sphere(r)
        print(f"The volume of a sphere with radius {r} is {volume:.2f} cubic units.")
