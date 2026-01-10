
players = [
    {
        "name": "alice",
        "score": 2300,
        "active": True,
        "region": "north",
        "achievements": 5
    },
    {
        "name": "bob",
        "score": 1800,
        "active": True,
        "region": "east",
        "achievements": 3
    },
    {
        "name": "charlie",
        "score": 2150,
        "active": True,
        "region": "central",
        "achievements": 7
    },
    {
        "name": "diana",
        "score": 2050,
        "active": False,
        "region": "north",
        "achievements": 4
    },
    {
        "name": "franklen",
        "score": 700,
        "active": False,
        "region": "north",
        "achievements": 4
    },
    {
        "name": "hassan",
        "score": 10,
        "active": False,
        "region": "east",
        "achievements": 1
    },
]

achievement_log = [
    "first_kill",
    "level_10",
    "boss_slayer",
    "first_kill",
    "level_10",
]


high_scorers = [p["name"] for p in players if p["score"] > 2000]
scorers_doubled = [p.get("score") * 2 for p in players]
active_players = [p.get("name") for p in players if p.get("active") is True]

print("=== Game Analytics Dashboard ===")

print("\n=== List Comprehension Examples ===")
print("High scorers (>2000):", high_scorers)
print("Score doubled:", scorers_doubled)
print("Active -layers:", active_players)


players_score = {p["name"]: p["score"] for p in players}
score_categories = {
    "hight": len([p for p in players if p["score"] >= 2200]),
    "medium": len(
        [p for p in players if p["score"] >= 1800 and p["score"] < 2200]
        ),
    "low": len([p for p in players if p["score"] < 1800]),
}
achievement_counts = {p.get("name"): p.get("achievements") for p in players}

print("\n=== Dict Comprehension Examples ===")
print("Players score:", players_score)
print("Score categories:", score_categories)
print("Achievements counts:", achievement_counts)

unique_players = {p["name"] for p in players}
unique_achievements = {a for a in achievement_log}
active_region = {p["region"] for p in players}

print("\n=== Set Comprehension Examples ===")
print("Unique players:", unique_players)
print("Uniqte achievements:", unique_achievements)
print("Active region:", active_region)

print("\n=== Combined Analysis ===")

total_players = len(players)
total_unique_achievements = len({a for a in achievement_log})
avrege_score = sum(p["score"] for p in players) / len(players)
t_per = max(players, key=lambda p: p["score"])
l_per = min(players, key=lambda p: p["score"])

print("Total players:", total_players)
print("Total unique achievements:", total_unique_achievements)
print(f"Avrege score:{avrege_score:.1f}:")
print(f"Top performer: {t_per["name"]} ({t_per["score"]} points, ", end='')
print(f"{t_per["achievements"]} achievements)")
print(f"Low performer: {l_per["name"]} ({l_per["score"]} points, ", end='')
print(f"{l_per["achievements"]} achievements)")
