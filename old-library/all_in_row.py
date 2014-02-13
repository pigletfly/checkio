
def checkio(data):
    return flat(data)


def flat(mlist):
    result = []
    for i in mlist:
        if type(i) is list:
            result.extend(flat(i))
        else:
            result.append(i)
    return result


if __name__ == '__main__':
    assert checkio([1, 2, 3]) == [1, 2, 3], 'First example'
    assert checkio([1, [2, 2, 2], 4]) == [1, 2, 2, 2, 4], 'Second example'
    assert checkio([[[2]], [4, [5, 6, [6], 6, 6, 6], 7]]) ==\
        [2, 4, 5, 6, 6, 6, 6, 6, 7], 'Third example'
