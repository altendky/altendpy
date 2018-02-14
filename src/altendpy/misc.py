import itertools


def identifier_path(it):
    return '__' + '_'.join(
        it.__module__.split('.') + [it.__qualname__]
    )


# https://docs.python.org/3/library/itertools.html
def pairwise(iterable):
    's -> (s0,s1), (s1,s2), (s2, s3), ...'
    a, b = itertools.tee(iterable)
    next(b, None)
    return zip(a, b)


# https://docs.python.org/3/library/itertools.html
def grouper(iterable, n, fillvalue=None):
    "Collect data into fixed-length chunks or blocks"
    # grouper('ABCDEFG', 3, 'x') --> ABC DEF Gxx"
    args = [iter(iterable)] * n
    return itertools.zip_longest(*args, fillvalue=fillvalue)
