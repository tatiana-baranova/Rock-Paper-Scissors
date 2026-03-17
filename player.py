from variants import Variants
class Player:
    def __init__(self, variant=Variants.ROCK, name="Bot"):
        self.variant = variant
        self.name = name

    def whoWins(self, other):
        first = self
        second = other
        if first.variant == second.variant:
            return "Нічія"
        elif first.variant == Variants.ROCK and second.variant == Variants.PAPER:
            return f"Переміг гравець з ім'ям: {second.name}"
        elif first.variant == Variants.PAPER and second.variant == Variants.SCISSORS:
            return f"Переміг гравець з ім'ям: {second.name}"
        elif first.variant == Variants.ROCK and second.variant == Variants.SCISSORS:
            return f"Переміг гравець з ім'ям: {first.name}"
        elif first.variant == Variants.SCISSORS and second.variant == Variants.PAPER:
            return f"Переміг гравець з ім'ям: {first.name}"
        elif first.variant == Variants.PAPER and second.variant == Variants.ROCK:
            return f"Переміг гравець з ім'ям: {first.name}"
        elif first.variant == Variants.SCISSORS and second.variant == Variants.ROCK:
            return f"Переміг гравець з ім'ям: {second.name}"
        