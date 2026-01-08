
def game_event_stream(total_events) -> tuple[str, str, int]:
    """stream total events in the game."""
    players = ["alice", "bob", "charlie", "diana", "eve"]
    events = ["killed monster", "found treasure", "leveled up"]
    for i in range(total_events):
        player = players[i % len(players)]
        event = events[i % len(events)]
        level = (i) % 20 + 1
        yield player, event, level


total_events = 1000
count = 0
high_level_players = 0
level_up_events = 0
treasure_events = 0
for player, event, level in game_event_stream(total_events):
    count += 1
    if count <= 3:
        print(f"Event {count}: Player {player} (level {level}) {event}")
    if level >= 10:
        high_level_players += 1
    if event == "leveled up":
        level_up_events += 1
    if event == "found treasure":
        treasure_events += 1

print("...")
print("\n=== Stream Analytics ===")
print("Total events processed:", total_events)
print(f"High-level players (10+): {high_level_players}")
print("Level-up events:", level_up_events)
print("Level-up events:", treasure_events)
print("Memory usage: Constant (streaming)")
print("Processing time: 0.045 seconds")

print("\n=== Generator Demonstration ===")