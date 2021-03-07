# Provided a dictionary with keys and values, create a dict flipping keys and values


def flip_a_dict(dict_orig):
    e = {v: k for k, v in dict_orig.items()}
    return e


if __name__ == '__main__':
    d = {'a': 1, 'b': 2, 'c': 3}
    print(f"Original dictionary {d}")
    print(f"Flipped dictionary {flip_a_dict(d)}")
