import sys
import csv
import random

admin_username = "Admin"
admin_password = "main123"

class Character:
    def __init__(self, name, health):
        self._name = name
        self._health = health

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def health(self):
        return int(self._health)

    @health.setter
    def health(self, health):
        self._health = health

    def __str__(self):
        return f"Name: {self._name}, Health: {self._health}"

class Hero(Character):
    def __init__(self, name, health, attack1, attack2, special):
        super().__init__(name, health)
        self._attack1 = attack1
        self._attack2 = attack2
        self._special = special

    @property
    def attack1(self):
        return int(self._attack1)

    @attack1.setter
    def attack1(self, attack1):
        self._attack1 = attack1

    @property
    def attack2(self):
        return int(self._attack2)

    @attack2.setter
    def attack2(self, attack2):
        self._attack2 = attack2

    @property
    def special(self):
        return int(self._special)

    @special.setter
    def special(self, special):
        self._special = special

    def __str__(self):
        return f"{super().__str__()}, Attack1: {self._attack1}, Attack2: {self._attack2}, Special: {self.special}"

class Enemy(Character):
    def __init__(self, name, health, attack1, attack2):
        super().__init__(name, health)
        self._attack1 = attack1
        self._attack2 = attack2

    @property
    def attack1(self):
        return int(self._attack1)

    @attack1.setter
    def attack1(self, attack1):
        self._attack1 = attack1

    @property
    def attack2(self):
        return int(self._attack2)

    @attack2.setter
    def attack2(self, attack2):
        self._attack2 = attack2

    def __str__(self):
        return f"{super().__str__()}, Attack1: {self._attack1}, Attack2: {self._attack2}"

def main():
    while True:
        input_option = main_menu()
        if input_option == "1":
            validation = login()

            match validation:
                case "Success":
                    admin_page()
                case "Failed":
                    print("Login Failed!\n")
                    continue
        elif input_option == "2":
            play_page()
        elif input_option == "3":
            sys.exit("Program Closed")
        elif input_option == "Invalid":
            print("Invalid Option\n")
            continue


def main_menu():
    print("~~~~~~~~~~~~~ Crown Master ~~~~~~~~~~~~~\n")
    input_option = input("Choose your option:\n1. Log in (for admins)\n2. Play\n3. Exit\n\nYour Option (Choose the number or the name of the option): ").strip().lower()

    match input_option:
        case "1"|"log in":
            return "1"
        case "2"|"play":
            return "2"
        case "3"|"exit":
            return "3"
        case _:
            return "Invalid"


def login():
    username = input("Username: ")
    password = input("Password: ")

    return check_login(username, password)

# To help in testing
def check_login(username, password):
    if username != admin_username or password != admin_password:
        return "Failed"

    return "Success"


def admin_page():
    while True:
        heroes = read_csv("heroes.csv")
        enemies = read_csv("enemies.csv")

        print(f"\n\nWelcome {admin_username}\n")
        admin_input = input("Choose your option:\n1. Display Heroes\n2. Add a Hero\n3. Remove a Hero\n4. Display Enemies\n5. Add an Enemy\n6. Remove an Enemy\n7. Log out\n\nYour Option (Choose the number of the option): ").strip().lower()

        match admin_input:
            case "1":
                display_heroes(heroes)
            case "2":
                add_hero(heroes)
            case "3":
                remove_hero(heroes)
            case "4":
                display_enemies(enemies)
            case "5":
                add_enemy(enemies)
            case "6":
                remove_enemy(enemies)
            case "7":
                return
            case _:
                print("Invalid Input\n")
                continue

def add_hero(heroes):
    display_heroes(heroes)

    new_hero = {}

    for key in heroes[0].keys():
        value = input(f"Enter the value for {key}: ")
        new_hero[key] = value

    try:
        _ = int(new_hero["health"])
    except ValueError:
        print("Invalid Input")
        return
    else:
        try:
            _ = int(new_hero["attack1"])
        except ValueError:
            print("Invalid Input")
            return
        else:
            try:
                _ = int(new_hero["attack2"])
            except ValueError:
                print("Invalid Input")
                return
            else:
                try:
                    _ = int(new_hero["special"])
                except ValueError:
                    print("Invalid Input")
                    return
                else:
                    new_hero_name = new_hero["name"]
                    existing_heroes = [hero["name"] for hero in heroes]

                    if new_hero_name in existing_heroes:
                        print(f"{new_hero_name} already exists")
                        return
                    else:
                        heroes.append(new_hero)
                        write_csv("heroes.csv", heroes, heroes[0].keys())
                        return

def remove_hero(heroes):
    display_heroes(heroes)

    hero_name = input("Enter the name of the hero you want to delete: ")
    for hero in heroes:
        if hero["name"] == hero_name:
            heroes.remove(hero)
            write_csv("heroes.csv", heroes, heroes[0].keys())
            return

    print("Hero not found")
    return

def add_enemy(enemies):
    display_enemies(enemies)

    new_enemy = {}

    for key in enemies[0].keys():
        value = input(f"Enter the value for {key}: ")
        new_enemy[key] = value

    try:
        _ = int(new_enemy["health"])
    except ValueError:
        print("Invalid Input")
        return
    else:
        try:
            _ = int(new_enemy["attack1"])
        except ValueError:
            print("Invalid Input")
            return
        else:
            try:
                _ = int(new_enemy["attack2"])
            except ValueError:
                print("Invalid Input")
                return
            else:
                new_enemy_name = new_enemy["name"]
                existing_enemies = [enemy["name"] for enemy in enemies]

                if new_enemy_name in existing_enemies:
                    print(f"{new_enemy_name} already exists")
                    return
                else:
                    enemies.append(new_enemy)
                    write_csv("enemies.csv", enemies, enemies[0].keys())
                    return

def remove_enemy(enemies):
    display_enemies(enemies)

    enemy_name = input("Enter the name of the enemy you want to delete: ")
    for enemy in enemies:
        if enemy["name"] == enemy_name:
            enemies.remove(enemy)
            write_csv("enemies.csv", enemies, enemies[0].keys())
            return

    print("Enemy not found")
    return

def play_page():
    heroes = read_csv("heroes.csv")
    if len(heroes) < 2:
        print("Not enough heroes to play")
        return

    enemies = read_csv("enemies.csv")
    if len(enemies) == 0:
        print("Not enough enemies to play")
        return

    # Choosing from the csv files
    chosen_heroes = select_heroes()
    selected_enemies = enemies_random_selection()

    # converting chosen heroes/enemies to objects of classes
    heroes_as_objects = convert_heroes_to_objects(chosen_heroes)
    enemies_as_objects = convert_enemies_to_objects(selected_enemies)

    print(playing(heroes_as_objects, enemies_as_objects))

def select_heroes():
    heroes = read_csv("heroes.csv")
    display_heroes(heroes)

    chosen_heroes = []
    while len(chosen_heroes) < 2:
        hero_selected = input("Enter the name of the hero you want to select: ")
        hero_exists = False

        for hero in heroes:
            if hero["name"] == hero_selected:
                if hero in chosen_heroes:
                    print("Already selected")
                    hero_exists = True
                    continue
                else:
                    chosen_heroes.append(hero)

                hero_exists = True
                break

        if not hero_exists:
            print("This hero does not exist")
            continue

    print("Done!\n")
    return chosen_heroes

def enemies_random_selection():
    enemies = read_csv("enemies.csv")

    selected_enemies = random.choices(enemies, k=2)

    return selected_enemies

def convert_heroes_to_objects(heroes_list):
    heroes_objects = []

    for hero_data in heroes_list:
        name = hero_data["name"]
        health = hero_data["health"]
        attack1 = hero_data["attack1"]
        attack2 = hero_data["attack2"]
        special = hero_data["special"]

        hero_object = Hero(name, health, attack1, attack2, special)
        heroes_objects.append(hero_object)

    # for hero in heroes_objects:
    #     print(hero)

    return heroes_objects

def convert_enemies_to_objects(enemies_list):
    enemies_objects = []

    for enemy_data in enemies_list:
        name = enemy_data["name"]
        health = enemy_data["health"]
        attack1 = enemy_data["attack1"]
        attack2 = enemy_data["attack2"]

        enemy_object = Enemy(name, health, attack1, attack2)
        enemies_objects.append(enemy_object)

    # for enemy in enemies_objects:
    #     print(enemy)

    return enemies_objects

def playing(heroes, enemies):
    rounds_counter = 1
    first_hero_attack2_available_rounds_counter = 0
    first_hero_special_available_rounds_counter = 0

    second_hero_attack2_available_rounds_counter = 0
    second_hero_special_available_rounds_counter = 0

    print("Battle Started")
    while (heroes[0].health > 0 or heroes[1].health > 0) and (enemies[0].health > 0 or enemies[1].health > 0):
        if rounds_counter == 1:
            if heroes[0].health > 0:
                can_first_hero_use_attack2 = check_first_hero_attack2(first_hero_attack2_available_rounds_counter)
                can_first_hero_use_special = check_first_hero_special(first_hero_special_available_rounds_counter)

                print(f"Name: {heroes[0].name}, Health: {heroes[0].health}, Attack1: {heroes[0].attack1} Damage, Attack2: {heroes[0].attack2} Damage ({can_first_hero_use_attack2}). Special: {heroes[0].special} Damage ({can_first_hero_use_special})")
                attack_choice = hero_attack_choice(can_first_hero_use_attack2, can_first_hero_use_special)
                print("")
                enemy_choice = enemy_to_attack(enemies)
                print("")

                if attack_choice == "Skip":
                    print("Turn Skipped\n")
                    first_hero_attack2_available_rounds_counter += 1
                    first_hero_special_available_rounds_counter += 1
                    rounds_counter += 1
                    continue

                if enemy_choice == "Skip":
                    print("Turn Skipped\n")
                    first_hero_attack2_available_rounds_counter += 1
                    first_hero_special_available_rounds_counter += 1
                    rounds_counter += 1
                    continue

                if attack_choice == "1":
                    if enemy_choice == "1":
                        print("Attacking Enemy 1 with Attack1")
                        enemies[0].health -= heroes[0].attack1
                        print(f"Enemy 1's health = {enemies[0].health}\n")
                    elif enemy_choice == "2":
                        print("Attacking Enemy 2 with Attack1")
                        enemies[1].health -= heroes[0].attack1
                        print(f"Enemy 2's health = {enemies[1].health}\n")
                elif attack_choice == "2":
                    if enemy_choice == "1":
                        print("Attacking Enemy 1 with Attack2")
                        enemies[0].health -= heroes[0].attack2
                        print(f"Enemy 1's health = {enemies[0].health}\n")
                        first_hero_attack2_available_rounds_counter = -1
                    elif enemy_choice == "2":
                        print("Attacking Enemy 2 with Attack2")
                        enemies[1].health -= heroes[0].attack2
                        print(f"Enemy 2's health = {enemies[1].health}\n")
                        first_hero_attack2_available_rounds_counter = -1
                elif attack_choice == "3":
                    if enemy_choice == "1":
                        print("Attacking Enemy 1 with Special Attack")
                        enemies[0].health -= heroes[0].special
                        print(f"Enemy 1's health = {enemies[0].health}\n")
                        first_hero_special_available_rounds_counter = -1
                    elif enemy_choice == "2":
                        print("Attacking Enemy 2 with Special Attack")
                        enemies[1].health -= heroes[0].special
                        print(f"Enemy 2's health = {enemies[1].health}\n")
                        first_hero_special_available_rounds_counter = -1

                first_hero_attack2_available_rounds_counter += 1
                first_hero_special_available_rounds_counter += 1
                rounds_counter += 1
                continue
            else:
                print(f"{heroes[0].name} is dead, next turn\n")
                rounds_counter += 1
                continue
        elif rounds_counter == 2:
            if heroes[1].health > 0:
                can_second_hero_use_attack2 = check_second_hero_attack2(second_hero_attack2_available_rounds_counter)
                can_second_hero_use_special = check_second_hero_special(second_hero_special_available_rounds_counter)

                print(f"Name: {heroes[1].name}, Health: {heroes[1].health}, Attack1: {heroes[1].attack1} Damage, Attack2: {heroes[1].attack2} Damage ({can_second_hero_use_attack2}). Special: {heroes[1].special} Damage ({can_second_hero_use_special})")
                attack_choice = hero_attack_choice(can_second_hero_use_attack2, can_second_hero_use_special)
                print("")
                enemy_choice = enemy_to_attack(enemies)
                print("")

                if attack_choice == "Skip":
                    print("Turn Skipped\n")
                    second_hero_attack2_available_rounds_counter += 1
                    second_hero_special_available_rounds_counter += 1
                    rounds_counter += 1
                    continue

                if enemy_choice == "Skip":
                    print("Turn Skipped\n")
                    second_hero_attack2_available_rounds_counter += 1
                    second_hero_special_available_rounds_counter += 1
                    rounds_counter += 1
                    continue

                if attack_choice == "1":
                    if enemy_choice == "1":
                        print("Attacking Enemy 1 with Attack1")
                        enemies[0].health -= heroes[0].attack1
                        print(f"Enemy 1's health = {enemies[0].health}\n")
                    elif enemy_choice == "2":
                        print("Attacking Enemy 2 with Attack1")
                        enemies[1].health -= heroes[0].attack1
                        print(f"Enemy 2's health = {enemies[1].health}\n")
                elif attack_choice == "2":
                    if enemy_choice == "1":
                        print("Attacking Enemy 1 with Attack2")
                        enemies[0].health -= heroes[0].attack2
                        print(f"Enemy 1's health = {enemies[0].health}\n")
                        second_hero_attack2_available_rounds_counter = -1
                    elif enemy_choice == "2":
                        print("Attacking Enemy 2 with Attack2")
                        enemies[1].health -= heroes[0].attack2
                        print(f"Enemy 2's health = {enemies[1].health}\n")
                        second_hero_attack2_available_rounds_counter = -1
                elif attack_choice == "3":
                    if enemy_choice == "1":
                        print("Attacking Enemy 1 with Special Attack")
                        enemies[0].health -= heroes[0].special
                        print(f"Enemy 1's health = {enemies[0].health}\n")
                        second_hero_special_available_rounds_counter = -1
                    elif enemy_choice == "2":
                        print("Attacking Enemy 2 with Special Attack")
                        enemies[1].health -= heroes[0].special
                        print(f"Enemy 2's health = {enemies[1].health}\n")
                        second_hero_special_available_rounds_counter = -1

                second_hero_attack2_available_rounds_counter += 1
                second_hero_special_available_rounds_counter += 1
                rounds_counter += 1
                continue
            else:
                print(f"{heroes[1].name} is dead, next turn\n")
                rounds_counter += 1
                continue
        if rounds_counter == 3:
            if enemies[0].health > 0:
                chosen_attack = enemy_attack_choice(enemies[0])
                chosen_hero_to_attack = hero_to_attack(heroes)

                if chosen_attack == "1":
                    if chosen_hero_to_attack == "1":
                        print(f"Enemy 1 Attacking {heroes[0].name} with Attack1")
                        heroes[0].health -= enemies[0].attack1
                        print(f"{heroes[0].name}'s health = {heroes[0].health}\n")
                    elif chosen_hero_to_attack == "2":
                        print(f"Enemy 1 Attacking {heroes[1].name} with Attack1")
                        heroes[1].health -= enemies[0].attack1
                        print(f"{heroes[1].name}'s health = {heroes[1].health}\n")
                elif chosen_attack == "2":
                    if chosen_hero_to_attack == "1":
                        print(f"Enemy 1 Attacking {heroes[0].name} with Attack2")
                        heroes[0].health -= enemies[0].attack2
                        print(f"{heroes[0].name}'s health = {heroes[0].health}\n")
                    elif chosen_hero_to_attack == "2":
                        print(f"Enemy 1 Attacking {heroes[1].name} with Attack2")
                        heroes[1].health -= enemies[0].attack2
                        print(f"{heroes[1].name}'s health = {heroes[1].health}\n")


                rounds_counter += 1
                continue
            else:
                print("Enemy 1 is dead, next turn\n")
                rounds_counter += 1
                continue
        if rounds_counter == 4:
            if enemies[1].health > 0:
                chosen_attack = enemy_attack_choice(enemies[1])
                chosen_hero_to_attack = hero_to_attack(heroes)

                if chosen_attack == "1":
                    if chosen_hero_to_attack == "1":
                        print(f"Enemy 2 Attacking {heroes[0].name} with Attack1")
                        heroes[0].health -= enemies[1].attack1
                        print(f"{heroes[0].name}'s health = {heroes[0].health}\n")
                    elif chosen_hero_to_attack == "2":
                        print(f"Enmey 2 Attacking {heroes[1].name} with Attack1")
                        heroes[1].health -= enemies[1].attack1
                        print(f"{heroes[1].name}'s health = {heroes[1].health}\n")
                elif chosen_attack == "2":
                    if chosen_hero_to_attack == "1":
                        print(f"Enemy 2 Attacking {heroes[0].name} with Attack2")
                        heroes[0].health -= enemies[1].attack2
                        print(f"{heroes[0].name}'s health = {heroes[0].health}\n")
                    elif chosen_hero_to_attack == "2":
                        print(f"Enemy 2 Attacking {heroes[1].name} with Attack2")
                        heroes[1].health -= enemies[1].attack2
                        print(f"{heroes[1].name}'s health = {heroes[1].health}\n")


                rounds_counter = 1
                continue
            else:
                print("Enemy 2 is dead, next turn\n")
                rounds_counter = 1
                continue

    if heroes[0].health <= 0 and heroes[1].health <= 0:
        return "You Lost!"
    elif enemies[0].health <= 0 and enemies[1].health <= 0:
        return "You Won!"

def check_first_hero_attack2(first_hero_attack2_counter):
    if first_hero_attack2_counter == 0:
        return "Available after 2 turns"
    elif first_hero_attack2_counter == 1:
        return "Available after 1 turn"
    else:
        return "Available"

def check_first_hero_special(first_hero_special_counter):
    if first_hero_special_counter == 0:
        return "Available after 3 turns"
    elif first_hero_special_counter == 1:
        return "Available after 2 turns"
    elif first_hero_special_counter == 2:
        return "Available after 1 turn"
    else:
        return "Available"

def check_second_hero_attack2(second_hero_attack2_counter):
    if second_hero_attack2_counter == 0:
        return "Available after 2 turns"
    elif second_hero_attack2_counter == 1:
        return "Available after 1 turn"
    else:
        return "Available"

def check_second_hero_special(second_hero_special_counter):
    if second_hero_special_counter == 0:
        return "Available after 3 turns"
    elif second_hero_special_counter == 1:
        return "Available after 2 turns"
    elif second_hero_special_counter == 2:
        return "Available after 1 turn"
    else:
        return "Available"

def hero_attack_choice(attack2_availability, special_availability):
    print("Choose your attack:\n1. Attack1\n2. Attack2\n3. Special Attack\nNote: Choosing an unavailable attack will skip your turn")
    choice = input("What's your choice (Type the number of the attack): ")

    if choice == "1":
        return "1"
    elif choice == "2":
        if attack2_availability != "Available":
            return "Skip"
        else:
            return "2"
    elif choice == "3":
        if special_availability != "Available":
            return "Skip"
        else:
            return "3"

def enemy_to_attack(enemies_objects_list):
    first_enemy = enemies_objects_list[0]
    second_enemy = enemies_objects_list[1]

    print("Available Enemies:")
    if first_enemy.health > 0:
        print(f"Name: Enemy 1, Health: {first_enemy.health}")

    if second_enemy.health > 0:
        print(f"Name: Enemy 2, Health: {second_enemy.health}")

    choice = input("Which enemy do you want to attack (Type the number of the enemy. If the enemy is dead or the number is incorrect, you turn will be skipped): ")

    if choice == "1":
        if first_enemy.health > 0:
            return "1"
        else:
            return "Skip"
    elif choice == "2":
        if second_enemy.health > 0:
            return "2"
        else:
            return "Skip"
    else:
        return "Skip"

def enemy_attack_choice(enemy):
    chosen_attack = random.choice([1, 2])

    if chosen_attack == 1:
        return "1"
    elif chosen_attack == 2:
        return "2"

def hero_to_attack(heroes):
    if heroes[0].health > 0 and heroes[1].health > 0:
        return str(random.choice([1, 2]))
    elif heroes[0].health > 0 and heroes[1].health <= 0:
        return "1"
    elif heroes[0].health <= 0 and heroes[1].health > 0:
        return "2"






def read_csv(file_path):
    data = []
    with open(file_path, newline="") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            data.append(row)

    return data

def write_csv(file_path, data, fieldnames):
    with open(file_path, "w", newline="") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames)
        writer.writeheader()
        writer.writerows(data)

def display_heroes(heroes_list):
    print("\nCurrent Heroes:")
    for hero in heroes_list:
        print(f"Name: {hero['name']}, Health: {hero['health']}, Attack 1: {hero['attack1']}, Attack 2: {hero['attack2']}, Special Attack: {hero['special']}")

def display_enemies(enemies_list):
    print("\nCurrent Enemies:")
    for enemy in enemies_list:
        print(f"Name: {enemy['name']}, Health: {enemy['health']}, Attack 1: {enemy['attack1']}, Attack 2: {enemy['attack2']}")

if __name__ == "__main__":
    main()
