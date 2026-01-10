
list1 = ['first_kill', 'level_10', 'treasure_hunter', 'speed_demon']
list2 = ['first_kill', 'level_10', 'boss_slayer', 'collector']
list3 = [
    'level_10', 'treasure_hunter', 'boss_slayer',
    'speed_demon', 'perfectionist'
    ]
alice = set(list1)
bob = set(list2)
charlie = set(list3)

print("=== Achievement Tracker System ===\n")
print("Player alice achievements: ", alice)
print("Player bob achievements: ", bob)
print("Player charlie achievements: ", charlie)

print("\n=== Achievement Analytics ===")
unipue = alice.union(bob, charlie)
print("All unique achievements: ", unipue)
print("Total unipue achievements: ", len(unipue))

common = alice.intersection(bob, charlie)
print("\ncommon to all players: ", common)

rare = (
    alice.union(bob, charlie)
    .difference(
        alice.intersection(bob)
        .union(alice.intersection(charlie))
        .union(bob.intersection(charlie))
    ))
print("Rare achivements (1 player): ", rare)

avb = alice.intersection(bob)
print("\nAlice vs Bob common: ", avb)

alice_unique = alice.difference(bob)
print("Alice unique: ", alice_unique)

bob_unique = bob.difference(alice)
print("Bob unique: ", bob_unique)
