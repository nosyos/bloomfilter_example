from typing import List

from utils import (
    kechash,
    first_3_pairs_of_hash,
    pick_lower_order_11_bits,
    decimal_of_11_bits,
    modulo_by_2048
)


def calc_bloom_filter(message: str, filter: list) -> List[int]:
    hash = kechash(message)
    (val1, val2, val3) = first_3_pairs_of_hash(hash)
    bits1, bits2, bits3 = pick_lower_order_11_bits(val1, val2, val3)
    deci1, deci2, deci3 = decimal_of_11_bits(bits1, bits2, bits3)
    mod1, mod2, mod3 = modulo_by_2048(deci1, deci2, deci3)
    for i in [mod1, mod2, mod3]:
        filter[i] += 1

    return filter


def main():
  filter = [0] * 2048
  while 1:
    print("input number:")
    input_text = input()
    if input_text == "1":
        print('add text:')
        message = input()
        filter = calc_bloom_filter(message, filter)
    elif input_text == "2":
        print('check input text below:')
        check_filter = [0] * 2048
        check_message = input()
        check_filter = calc_bloom_filter(check_message, check_filter)
        for v in [(i, x) for i, x in enumerate(check_filter) if x != 0]:
            if filter[v[0]] == 0:
                print('not included.')
                break
            elif filter[v[0]] < v[1]:
                print('not included')
                break
        else:
            print('may be included?')
    elif input_text == '3':
        print("exit:")
        exit(0)
    elif input_text == 'help':
        print("""
        --- help ---
        input number:
        1: add text into bloomfilter.
        2: verify text.
        3: exit.
        help: display this text.
        """)
    else:
        print('unknown command')


if __name__ == '__main__':
  main()