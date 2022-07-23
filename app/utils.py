from typing import Tuple

from Crypto.Hash import keccak


def kechash(message: str) -> str:
    k = keccak.new(digest_bits=256)
    k.update(bytes(message, encoding='utf-8'))
    return k.hexdigest()


def first_3_pairs_of_hash(hash: str) -> Tuple[str, str, str]:
    return hash[:2], hash[2:4], hash[4:6]


def pick_lower_order_11_bits(val1: str, val2: str, val3: str) -> Tuple[str, str, str]:
    arr = (val1, val2, val3)

    ret = list()

    for val in arr:
        val1 = ord(val[:1])
        val2 = ord(val[1:2])
        bxval1 = bin(val1)[2:]
        bxval2 = bin(val2)[2:]
        ret.append(f'{bxval1[:]}{bxval2[:5]}')

    return ret 


def decimal_of_11_bits(bits1: str, bits2: str, bits3: str) -> Tuple[str, str, str]:
    return int(bits1, 2), int(bits2, 2), int(bits3, 2)


def modulo_by_2048(deci1: int, deci2: int, deci3: int) -> Tuple[int, int, int]:
    return deci1 % 2048, deci2 % 2048, deci3 % 2048