class Car:
    def __init__(self, max_speed: int, unit: str):
        self.max_speed = max_speed
        self.unit = unit

    def __str__(self):
        return f"Car with the maximum speed of {self.max_speed} {self.unit}"


class Boat:
    def __init__(self, max_speed: int):
        self.max_speed = max_speed

    def __str__(self):
        return f"Boat with the maximum speed of {self.max_speed} knots"


if __name__ == "__main__":
    import sys
    data = sys.stdin.read().strip().split()
    q = int(data[0])
    idx = 1
    for _ in range(q):
        typ = data[idx]; idx += 1
        if typ == "car":
            speed = int(data[idx]); unit = data[idx + 1]; idx += 2
            vehicle = Car(speed, unit)
        elif typ == "boat":
            speed = int(data[idx]); idx += 1
            vehicle = Boat(speed)
        else:
            raise ValueError(f"Unknown vehicle type: {typ}")
        print(vehicle)
