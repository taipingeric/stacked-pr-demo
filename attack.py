from hp import lose_hp


def attack(hp, power):
    return lose_hp(hp, power * 2)
