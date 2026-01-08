
print("=== Player Inventory System ===")
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
print("\n=== Alice's Inventory ===")
alice_inventoryies = inventories.get("Alice")
total_items = 0
total_inv_value = 0
categorys_string = ""

for item, data in alice_inventoryies.items():
    category = data.get("category")
    rarity = data.get("rarity")
    quantity = data.get("quantity")
    value = data.get("value")
    total_items += quantity
    total_inv_value += quantity * value
    categorys_string += f" {item}({quantity}),"
    print(
        item,
        "(" + category + ", " + rarity + "):",
        str(quantity) + "x @",
        value,
        "gold each =",
        quantity * value,
        "gold"
    )
categorys_string = categorys_string[:-1]
print("Inventory value:", total_inv_value, "gold")
print("Item count:", total_items, "items")
print(f"Categories:{categorys_string}")

print("\n=== Transaction: Alice gives Bob 2 potions ===")

inv_alice = inventories.get("Alice").get("potion")
inv_bob = inventories.get("Bob")
if inv_alice.get("quantity") >= 2:
    inv_alice.update({"quantity": inv_alice.get("quantity") - 2})
    if inv_bob.get("potion") is None:
        inv_bob.update({
            "potion": {
                "category": "consumable",
                "rarity": "common",
                "quantity": 0,
                "value": 50
                }
        })

    inv_bob.get("potion").update({"quantity": 2})
    print("Transaction successful!\n")
else:
    print("Transaction failed!")

print("Alice potions:", inv_alice.get("quantity"))
print("Bob potions:", inv_bob.get("potion").get("quantity"))

print("\n=== Inventory Analytics ===")

richest_player = ""
value = 0
most_items_player = ""
items = 0
rarest_items = ""

for player, data in inventories.items():
    player_value = 0
    items_value = 0
    for item, values in data.items():
        player_value += values["quantity"] * values["value"]
        items_value += values["quantity"]
        if values["rarity"] == "rare":
            rarest_items += f" {item},"
    if player_value > value:
        value = player_value
        richest_player = player
    if items_value > items:
        items = items_value
        most_items_player = player

print("Most valuable player:", richest_player, f"({value} gold)")
print("Most items:", most_items_player, f"({items} items)")
rarest_items = rarest_items[:-1]
print(f"Rarest items:{rarest_items}")
