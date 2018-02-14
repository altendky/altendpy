import contextlib
import locale

import attr


@attr.s
class Values:
    initial = attr.ib()
    input = attr.ib()
    expected = attr.ib()
    collected = attr.ib(default=attr.Factory(list))

    def collect(self, value):
        self.collected.append(value)

    def check(self):
        return all(x == y for x, y in zip(self.expected, self.collected))


@contextlib.contextmanager
def use_locale(*s):
    if len(s) == 0:
        s = ('',)

    old = locale.getlocale(locale.LC_ALL)

    for name in s:
        try:
            locale.setlocale(locale.LC_ALL, name)
        except locale.Error:
            continue

        break
    else:
        assert False, 'Unable to set locale to any of {}'.format(s)

    yield

    locale.setlocale(locale.LC_ALL, old)
