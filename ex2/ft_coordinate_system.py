
import math


def get_distance(point1, point2):
    """return the distance between point1 and point2."""
    return math.sqrt(
        (point1[0] - point2[0])**2 +
        (point1[1] - point2[1])**2 +
        (point1[2] - point2[2])**2
        )


if __name__ == "__main__":
    player_position = (10, 20, 5)
    zero_position = (0, 0, 0)

    print("=== Game Coordinate System ===\n")
    print("Position created: ", player_position)
    print(f"Distance between {zero_position} and {player_position}: ", end='')
    print(f"{get_distance(zero_position, player_position):.2f}")

    string_position = "3,4,0"
    array = string_position.split(",")
    player_position = tuple(int(x) for x in array)

    print(f"\nParsing coordinate: \"{string_position}\"")
    print("Parsed position: ", player_position)
    print(f"Distance between {zero_position} and {player_position}: ", end='')
    print(f"{get_distance(zero_position, player_position):.1f}")

    string_position = "abc,def,ghi"
    array = string_position.split(",")
    print(f"\nParsing coordinate: \"{string_position}\"")
    try:
        p_position = tuple(int(x) for x in array)
        print("Parsed position: ", p_position)
        print(f"Distance between {zero_position} and {p_position}: ", end='')
        print(f"{get_distance(zero_position, p_position):.2f}")

    except ValueError as e:
        print(f"Error parsing coordinates: {e}")
        print(f"Error details - Type: {type(e).__name__}, args: {e.args}")

    print("\nUnpacking demonstration:")
    x, y, z = player_position
    print(f"Playe at, x={x}, y={y}, z={z}")
    print("Coordinates: X={}, Y={}, Z={}".format(*player_position))
