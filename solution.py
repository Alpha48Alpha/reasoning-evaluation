def calculate_total_distance(segments):
    """Calculate total distance for a list of (speed, time) segments."""
    return sum(speed * time for speed, time in segments)


if __name__ == "__main__":
    segments = [(60, 2), (30, 1)]
    total_distance = calculate_total_distance(segments)
    print(f"Total distance: {total_distance} miles")
