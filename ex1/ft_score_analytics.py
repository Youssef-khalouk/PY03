
import sys

if __name__ == "__main__":
    array = []

    try:
        print("=== Player Score Analytics ===")
        if len(sys.argv) <= 1:
            print("No scores provided. Usage: python3 ", end='')
            print("ft_score_analytics.py <score1> <score2> ...")
        else:
            for i in range(1, len(sys.argv)):
                array.append(int(sys.argv[i]))

            print("Scores processed: ", array)
            print("Total players: ", len(array))
            print("Total score: ", sum(array))
            print("Average score: ", sum(array) / len(array))
            print("High score: ", max(array))
            print("Low score: ", min(array))
            print(f"Score range: {max(array) - min(array)}\n")

    except ValueError as e:
        print("Error: ", e, file=sys.stderr)
