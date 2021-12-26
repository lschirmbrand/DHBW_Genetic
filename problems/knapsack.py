from typing import List
from algorithms import genetic
from algorithms.genetic import Genome
from collections import namedtuple

Item = namedtuple('Item', ['itemname', 'value', 'weight'])

items = [
    Item('Item1', 300, 220),
    Item('Item2', 150, 16),
    Item('Item3', 60, 80),
    Item('Item4', 40, 35),
    Item('Item5', 160, 20),
    Item('Item6', 301, 221),
    Item('Item7', 151, 17),
    Item('Item8', 61, 81),
    Item('Item9', 41, 36),
    Item('Item10', 161, 21),
    Item('Item11', 302, 222),
    Item('Item12', 152, 12),
    Item('Item13', 62, 82),
    Item('Item14', 42, 37),
    Item('Item15', 162, 22),
    Item('Item16', 302, 223),
    Item('Item17', 155, 19),
    Item('Item19', 153, 19),
    Item('Item20', 63, 83),
    Item('Item21', 43, 38),
    Item('Item22', 168, 23),
    Item('Item23', 303, 223),
    Item('Item24', 157, 19),
    Item('Item25', 151, 11),
    Item('Item26', 62, 86),
    Item('Item27', 48, 33),
    Item('Item28', 143, 25),
]

moreItems = [
    Item('Item30', 68, 36),
    Item('Item31', 47, 53),
    Item('Item32', 123, 21),
    # Item('Item33', 48, 36),
    # Item('Item34', 41, 63),
    # Item('Item35', 173, 41),
    # Item('Item30', 68, 36),
    # Item('Item31', 57, 63),
    # Item('Item32', 133, 31),
    # Item('Item33', 68, 42),
    # Item('Item34', 41, 63),
    # Item('Item35', 173, 41),
    # Item('Item36', 147, 19),
    # Item('Item37', 111, 11),
    # Item('Item38', 68, 86),
] + items


def generateItems(num: int) -> List[Item]:
    return [Item(f"item{i}", i, i) for i in range(1, num+1)]


def fitness(genome: Genome, items: List[Item], weight_limit: int) -> int:
    if len(genome) != len(items):
        raise ValueError("Genome and Item have to be the same length.")

    weight = 0
    value = 0
    for i, item in enumerate(items):
        if genome[i] == 1:
            weight += item.weight
            value += item.value

            if weight > weight_limit:
                return 0

    return value


def fromGenome(genome: Genome, items: List[Item]) -> List[Item]:
    result = []
    for i, item in enumerate(items):
        if genome[i] == 1:
            result += [item]

    return result


def toString(items: List[Item]):
    return f"[{', '.join([item.itemname for item in items])}]"


def value(items: List[Item]):
    return sum([t.value for t in items])


def weight(items: List[Item]):
    return sum([p.weight for p in items])


def print_stats(items: List[Item]):
    print(f"Items: {toString(items)}")
    print(f"Value {value(items)}")
    print(f"Weight: {weight(items)}")
    if weight(items) > 300:
        print("Useless population has led to no valueable result. Darwinism.")