from math import ceil
from typing import Set, Dict


class CamelotWheel:

    __WHEEL: Dict[str, Set[str]] = None

    @classmethod
    def keys_are_harmonic(cls, key1: str, key2: str) -> bool:
        return key2 in cls.__wheel()[key1]

    @classmethod
    def __wheel(cls):
        if not cls.__WHEEL: cls.__set_up_wheel()
        return cls.__WHEEL

    @classmethod
    def __set_up_wheel(cls):
        cls.__WHEEL = dict()
        for n, key_letter in zip([x + 1 for x in range(24)], ['A', 'B'] * 12):
            # This makes it 1, 1, 2, 2, ..., 11, 11, 12, 12
            key_number = ceil(n / 2)
            # Create a set with the current key's harmonic neighbors. For example -> 1A: {1B, 2A, 12A}
            harmonic_neighbors = {
                f'{key_number}{key_letter}',
                f'{key_number}{cls.__complement(key_letter)}',
                f'{cls.__next(key_number)}{key_letter}',
                f'{cls.__previous(key_number)}{key_letter}'
            }
            # Add entry to wheel dict
            cls.__WHEEL[f'{key_number}{key_letter}'] = harmonic_neighbors

    @classmethod
    def __next(cls, key_number):
        return key_number + 1 if key_number < 12 else 1

    @classmethod
    def __previous(cls, key_number):
        return key_number - 1 if key_number > 1 else 12

    @classmethod
    def __complement(cls, key_letter):
        return {'A': 'B', 'B': 'A'}[key_letter]
