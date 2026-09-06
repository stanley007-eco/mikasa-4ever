import random
import time
import sys
import os

# ---- Attack on Titan Themed Battle Game (Animated Edition) ----

# ANSI colors (works in VS Code terminal / most modern terminals)
class C:
    RED = "\033[91m"2
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    CYAN = "\033[96m"
    BOLD = "\033[1m"
    END = "\033[0m"

scouts = {
    "Mikasa": {"hp": 120, "power": 25},
    "Eren": {"hp": 100, "power": 30},
    "Levi": {"hp": 110, "power": 35},
    "Armin": {"hp": 80, "power": 15},
}

def type_effect(text, delay=0.02, color=C.END):
    for ch in text:
        sys.stdout.write(color + ch + C.END)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def hp_bar(current, max_hp, color):
    current = max(current, 0)
    filled = int((current / max_hp) * 20)
    bar = "█" * filled + "░" * (20 - filled)
    return f"{color}[{bar}] {current}/{max_hp}{C.END}"

def loading_animation(text, cycles=3):
    for _ in range(cycles):
        for frame in ["|", "/", "-", "\\"]:
            sys.stdout.write(f"\r{text} {frame}")
            sys.stdout.flush()
            time.sleep(0.1)
    print()

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

# Frame-by-frame ASCII animation: Titan walking in from the distance
TITAN_WALK_FRAMES = [
r"""
                                          ,;;;;;;;;;;;,
                                         ;;;;;;;;;;;;;;;
                                        ;;;;   TITAN  ;;;
                                         '  |      |  '
                                            |      |
""",
r"""
                             ,;;;;;;;;;;;,
                            ;;;;;;;;;;;;;;;
                           ;;;;   TITAN  ;;;
                            '  |      |  '
                               |      |
""",
r"""
             ,;;;;;;;;;;;,
            ;;;;;;;;;;;;;;;
           ;;;;   TITAN  ;;;
            '  |      |  '
               |      |
""",
r"""
   ,;;;;;;;;;;;,
  ;;;;;;;;;;;;;;;
 ;;;;   TITAN  ;;;
  '  |      |  '
     |      |
""",
]

# Frame-by-frame ASCII animation: ODM gear slash attack
SLASH_FRAMES = [
r"""
        \
         \
          \    <-- ODM Gear approaching
""",
r"""
          \
       ----X----
          /
""",
r"""
       -=======-
      SLASH!!
       -=======-
""",
r"""
       *  *  *
     *   +   *
       *  *  *
""",
]

def play_frames(frames, delay=0.25, color=C.RED):
    for frame in frames:
        clear_screen()
        print(color + frame + C.END)
        time.sleep(delay)
    clear_screen()

def choose_scout():
    type_effect("Choose your Scout:", 0.02, C.CYAN)
    for i, name in enumerate(scouts, 1):
        print(f"  {C.YELLOW}{i}.{C.END} {name} (HP:{scouts[name]['hp']} POWER:{scouts[name]['power']})")
    choice = int(input(f"{C.BOLD}Enter number: {C.END}"))
    return list(scouts.keys())[choice - 1]

def battle():
    os.system("")  # enables ANSI colors on Windows terminals
    type_effect("=== SHIGANSHINA DISTRICT - TITAN BREACH ===", 0.03, C.RED)
    scout_name = choose_scout()
    scout = scouts[scout_name].copy()
    max_scout_hp = scout["hp"]
    titan_hp = 150
    max_titan_hp = titan_hp
    titan_power = 20

    print()
    loading_animation("Deploying ODM Gear", 3)
    type_effect(f"{scout_name} has entered the battlefield!", 0.02, C.GREEN)
    type_effect("A Titan emerges from the mist...", 0.03, C.RED)
    play_frames(TITAN_WALK_FRAMES, delay=0.3, color=C.RED)
    print()

    turn = 1
    while scout["hp"] > 0 and titan_hp > 0:
        print(f"{C.BOLD}--- Turn {turn} ---{C.END}")
        action = input("Choose action: (1) Slash Nape  (2) Dodge & Reposition\n> ")

        if action == "1":
            play_frames(SLASH_FRAMES, delay=0.2, color=C.YELLOW)
            dmg = scout["power"] + random.randint(-5, 10)
            titan_hp -= dmg
            type_effect(f"{scout_name} slashes the nape for {dmg} damage!", 0.02, C.YELLOW)
        else:
            loading_animation("Dodging", 2)
            dmg = 0
            type_effect(f"{scout_name} dodges using ODM gear, avoiding damage!", 0.02, C.CYAN)

        if titan_hp <= 0:
            print()
            type_effect("The Titan's body evaporates into steam...", 0.03, C.RED)
            type_effect("VICTORY!", 0.05, C.GREEN)
            break

        titan_dmg = titan_power + random.randint(-5, 5)
        if action != "2":
            scout["hp"] -= titan_dmg
            type_effect(f"Titan swings back! {scout_name} takes {titan_dmg} damage.", 0.02, C.RED)

        print(f"{scout_name}: {hp_bar(scout['hp'], max_scout_hp, C.GREEN)}")
        print(f"Titan:   {hp_bar(titan_hp, max_titan_hp, C.RED)}")
        print()
        turn += 1

    if scout["hp"] <= 0:
        print()
        type_effect(f"{scout_name} has fallen...", 0.03, C.RED)
        type_effect("The fight continues another day.", 0.03, C.YELLOW)

if __name__ == "__main__":
    battle()
