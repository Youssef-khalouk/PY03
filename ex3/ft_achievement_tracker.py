

if __name__ == "__main__":

    list1 = ['first_kill', 'level_10', 'treasure_hunter', 'speed_demon']
    list2 = ['first_kill', 'level_10', 'boss_slayer', 'collector']
    list3 = [
        'level_10', 'treasure_hunter', 'boss_slayer',
        'speed_demon', 'perfectionist'
        ]
    alice = set(list1)
    boob = set(list2)
    charlie = set(list3)

    print("=== Achievement Tracker System ===\n")
    print("Player alice achievements: ", alice)
    print("Player boob achievements: ", boob)
    print("Player charlie achievements: ", charlie)

    print("\n=== Achievement Analytics ===")
    unipue = alice.union(boob, charlie)
    print("All unique achievements: ", unipue)
    print("Total unipue achievements: ", len(unipue))

    common = alice.intersection(boob, charlie)
    print("common to all players: ", common)

    rare = (
        alice.union(boob, charlie)
        .difference(
            alice.intersection(boob)
            .union(alice.intersection(charlie))
            .union(boob.intersection(charlie))
        ))

    print("Rare achivements (1 player): ", rare)
