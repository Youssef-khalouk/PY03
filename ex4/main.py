# ft_inventory_system.py

print("=== Player Inventory System ===")

# Inventory structure:
# player -> item -> details
inventories = dict()

inventories.update({
    "Alice": {
        "sword": {
            "category": "weapon",
            "rarity": "rare",
            "quantity": 1,
            "value": 500
        },
        "potion": {
            "category": "consumable",
            "rarity": "common",
            "quantity": 5,
            "value": 50
        },
        "shield": {
            "category": "armor",
            "rarity": "uncommon",
            "quantity": 1,
            "value": 200
        }
    },
    "Bob": {
        "magic_ring": {
            "category": "accessory",
            "rarity": "rare",
            "quantity": 1,
            "value": 300
        }
    }
})

# ----- Inventory Display -----
print("=== Alice's Inventory ===")

total_value = 0
total_items = 0
categories = dict()

alice_inventory = inventories.get("Alice")

for item, data in alice_inventory.items():
    qty = data.get("quantity")
    value = data.get("value")
    item_total = qty * value

    total_value = total_value + item_total
    total_items = total_items + qty

    category = data.get("category")
    if categories.get(category) is None:
        categories.update({category: qty})
    else:
        categories.update({category: categories.get(category) + qty})

    print(
        item,
        "(" + data.get("category") + ", " + data.get("rarity") + "):",
        str(qty) + "x @",
        value,
        "gold each =",
        item_total,
        "gold"
    )

print("Inventory value:", total_value, "gold")
print("Item count:", total_items, "items")

print("Categories:", end=" ")
for cat, count in categories.items():
    print(cat + "(" + str(count) + ")", end=", ")
print()

# ----- Transaction -----
print("=== Transaction: Alice gives Bob 2 potions ===")

alice_potions = inventories.get("Alice").get("potion")
bob_inventory = inventories.get("Bob")

if alice_potions.get("quantity") >= 2:
    alice_potions.update({"quantity": alice_potions.get("quantity") - 2})

    if bob_inventory.get("potion") is None:
        bob_inventory.update({
            "potion": {
                "category": "consumable",
                "rarity": "common",
                "quantity": 2,
                "value": 50
            }
        })
    else:
        bob_inventory.get("potion").update({
            "quantity": bob_inventory.get("potion").get("quantity") + 2
        })

    print("Transaction successful!")
else:
    print("Transaction failed!")

# ----- Updated Inventories -----
print("=== Updated Inventories ===")
print("Alice potions:", inventories.get("Alice").get("potion").get("quantity"))
print("Bob potions:", inventories.get("Bob").get("potion").get("quantity"))

# ----- Inventory Analytics -----
print("=== Inventory Analytics ===")

most_value = 0
most_items = 0
richest_player = ""
largest_inventory = ""

rare_items = dict()

for player, inv in inventories.items():
    player_value = 0
    player_items = 0

    for item, data in inv.items():
        qty = data.get("quantity")
        val = data.get("value")
        player_value = player_value + (qty * val)
        player_items = player_items + qty

        if data.get("rarity") == "rare":
            rare_items.update({item: True})

    if player_value > most_value:
        most_value = player_value
        richest_player = player

    if player_items > most_items:
        most_items = player_items
        largest_inventory = player

print("Most valuable player:", richest_player, "(" + str(most_value) + " gold)")
print("Most items:", largest_inventory, "(" + str(most_items) + " items)")

print("Rarest items:", end=" ")
for item in rare_items.keys():
    print(item, end=", ")
print()

print()
print("Why are dictionaries essential for game data?")
print("They allow instant access to items by name and flexible data organization.")
print("How do nested dictionaries model complex relationships?")
print("They represent real-world hierarchies like players owning items with attributes.")
