import altendpy.misc


def test_pairwise():
    values = 4
    iterable = tuple(range(values))
    expected = tuple(zip(iterable[:-1], iterable[1:]))

    actual = tuple(altendpy.misc.pairwise(iterable))

    assert actual == expected
