import random
import time

# ---- Attack on Titan Themed Battle Game ----

scouts = {
    "Mikasa": {"hp": 120, "power": 25},
    "Eren": {"hp": 100, "power": 30},
    "Levi": {"hp": 110, "power": 35},
    "Armin": {"hp": 80, "power": 15},
}

def print_slow(text):
    print(text)
    time.sleep(0.6)

def choose_scout():
    print_slow("Choose your Scout:")
    for i, name in enumerate(scouts, 1):
        print(f"{i}. {name} (HP:{scouts[name]['hp']} POWER:{scouts[name]['power']})")
    choice = int(input("Enter number: "))
    return list(scouts.keys())[choice - 1]

def battle():
    print_slow("=== SHIGANSHINA DISTRICT - TITAN BREACH ===")
    scout_name = choose_scout()
    scout = scouts[scout_name].copy()
    titan_hp = 150
    titan_power = 20

    print_slow(f"\n{scout_name} has entered the battlefield!")
    print_slow("A Titan approaches... ODM Gear activated!\n")

    turn = 1
    while scout["hp"] > 0 and titan_hp > 0:
        print_slow(f"--- Turn {turn} ---")
        action = input("Choose action: (1) Slash Nape  (2) Dodge & Reposition\n> ")

        if action == "1":
            dmg = scout["power"] + random.randint(-5, 10)
            titan_hp -= dmg
            print_slow(f"{scout_name} slashes the nape for {dmg} damage!")
        else:
            dmg = 0
            print_slow(f"{scout_name} dodges using ODM gear, avoiding damage!")

        if titan_hp <= 0:
            print_slow("\nThe Titan's body evaporates into steam... VICTORY!")
            break

        titan_dmg = titan_power + random.randint(-5, 5)
        if action != "2":
            scout["hp"] -= titan_dmg
            print_slow(f"Titan swings back! {scout_name} takes {titan_dmg} damage.")

        print_slow(f"{scout_name} HP: {max(scout['hp'],0)} | Titan HP: {max(titan_hp,0)}\n")
        turn += 1

    if scout["hp"] <= 0:
        print_slow(f"\n{scout_name} has fallen... 'Tribute to Eren!' The fight continues another day.")

if __name__ == "__main__":
    battle()

