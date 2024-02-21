from project import main_menu, check_login, check_first_hero_attack2, check_first_hero_special
from project import check_second_hero_attack2, check_second_hero_special

def main():
    test_main_menu()
    test_login()
    test_check_first_hero_attack2()
    test_check_first_hero_special()
    test_check_second_hero_attack2()
    test_check_second_hero_special()

def test_main_menu(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: "1")
    assert main_menu() == "1"

    monkeypatch.setattr('builtins.input', lambda _: "log in")
    assert main_menu() == "1"

    monkeypatch.setattr('builtins.input', lambda _: "LoG IN")
    assert main_menu() == "1"

    monkeypatch.setattr('builtins.input', lambda _: "2")
    assert main_menu() == "2"

    monkeypatch.setattr('builtins.input', lambda _: "play")
    assert main_menu() == "2"

    monkeypatch.setattr('builtins.input', lambda _: "PLaY")
    assert main_menu() == "2"

    monkeypatch.setattr('builtins.input', lambda _: "3")
    assert main_menu() == "3"

    monkeypatch.setattr('builtins.input', lambda _: "exit")
    assert main_menu() == "3"

    monkeypatch.setattr('builtins.input', lambda _: "ExIT")
    assert main_menu() == "3"

    monkeypatch.setattr('builtins.input', lambda _: "4")
    assert main_menu() == "Invalid"

    monkeypatch.setattr('builtins.input', lambda _: "Other")
    assert main_menu() == "Invalid"

    monkeypatch.setattr('builtins.input', lambda _: "hello")
    assert main_menu() == "Invalid"

def test_login():
    assert check_login("Admin", "main123") == "Success"
    assert check_login("Admin", "123") == "Failed"
    assert check_login("David", "main123") == "Failed"
    assert check_login("David", "Malan") == "Failed"

def test_check_first_hero_attack2():
    assert check_first_hero_attack2(0) == "Available after 2 turns"
    assert check_first_hero_attack2(1) == "Available after 1 turn"
    assert check_first_hero_attack2(2) == "Available"
    assert check_first_hero_attack2(3) == "Available"
    assert check_first_hero_attack2(4) == "Available"

def test_check_first_hero_special():
    assert check_first_hero_special(0) == "Available after 3 turns"
    assert check_first_hero_special(1) == "Available after 2 turns"
    assert check_first_hero_special(2) == "Available after 1 turn"
    assert check_first_hero_special(3) == "Available"
    assert check_first_hero_special(4) == "Available"
    assert check_first_hero_special(5) == "Available"

def test_check_second_hero_attack2():
    assert check_second_hero_attack2(0) == "Available after 2 turns"
    assert check_second_hero_attack2(1) == "Available after 1 turn"
    assert check_second_hero_attack2(2) == "Available"
    assert check_second_hero_attack2(3) == "Available"
    assert check_second_hero_attack2(4) == "Available"

def test_check_second_hero_special():
    assert check_second_hero_special(0) == "Available after 3 turns"
    assert check_second_hero_special(1) == "Available after 2 turns"
    assert check_second_hero_special(2) == "Available after 1 turn"
    assert check_second_hero_special(3) == "Available"
    assert check_second_hero_special(4) == "Available"
    assert check_second_hero_special(5) == "Available"

if __name__ == "__main__":
    main()