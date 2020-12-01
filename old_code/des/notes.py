# operators order
# https://www.programiz.com/python-programming/precedence-associativity


def derive_keys(key):
    key, = struct.unpack(">Q", key)
    next_key = permute(key, 64, PERMUTED_CHOICE1) # Skrati kljuc
    next_key = next_key >> 28, next_key & 0x0fffffff # 
    for bits in ROTATES:
        next_key = rotate_left(next_key[0], bits), rotate_left(next_key[1], bits)
        yield permute(next_key[0] << 28 | next_key[1], 56, PERMUTED_CHOICE2)

def permute(data, bits, mapper):
    ret = 0
    for i, v in enumerate(mapper):
        # 
        if data & 1 << bits - 1 - v:
            ret |= 1 << len(mapper) - 1 - i
    return ret