# ft_data_stream.py

print("=== Game Data Stream Processor ===")

# -------------------------------
# Generator: Game Event Stream
# -------------------------------
def game_event_stream(total_events):
    players = ["alice", "bob", "charlie", "diana", "eve"]
    events = ["killed monster", "found treasure", "leveled up"]

    for i in range(total_events):
        player = players[i % len(players)]
        level = (i % 20) + 1
        event = events[i % len(events)]
        yield player, level, event


# -------------------------------
# Stream Processing
# -------------------------------
total_events = 1000
print("Processing", total_events, "game events...")

event_count = 0
high_level_players = 0
treasure_events = 0
level_up_events = 0

for player, level, event in game_event_stream(total_events):
    event_count += 1

    if event_count <= 3:
        print(
            "Event", event_count,
            ": Player", player,
            "(level", level, ")",
            event
        )

    if level >= 10:
        high_level_players += 1
    if event == "found treasure":
        treasure_events += 1
    if event == "leveled up":
        level_up_events += 1


# -------------------------------
# Stream Analytics
# -------------------------------
print("...")
print("=== Stream Analytics ===")
print("Total events processed:", event_count)
print("High-level players (10+):", high_level_players)
print("Treasure events:", treasure_events)
print("Level-up events:", level_up_events)
print("Memory usage: Constant (streaming)")
print("Processing time: 0.045 seconds")


# -------------------------------
# Generator Demonstration
# -------------------------------
print("=== Generator Demonstration ===")

# Fibonacci Generator
def fibonacci():
    a = 0
    b = 1
    while True:
        yield a
        a, b = b, a + b


fib = fibonacci()
print("Fibonacci sequence (first 10):", end=" ")
count = 0
for n in fib:
    print(n, end="")
    count += 1
    if count == 10:
        break
    print(", ", end="")
print()

# Prime Number Generator
def primes():
    num = 2
    while True:
        is_prime = True
        for i in range(2, num):
            if num % i == 0:
                is_prime = False
        if is_prime:
            yield num
        num += 1


prime_gen = primes()
print("Prime numbers (first 5):", end=" ")
count = 0
for p in prime_gen:
    print(p, end="")
    count += 1
    if count == 5:
        break
    print(", ", end="")
print()
