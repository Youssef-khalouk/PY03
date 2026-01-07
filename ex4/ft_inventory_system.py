
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
