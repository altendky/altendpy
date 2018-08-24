import collections
import timeit

import attr


@attr.s(frozen=True)
class Example:
    statement = attr.ib()


@attr.s
class Runner:
    examples = attr.ib()
    setup = attr.ib(default='')
    repeats = attr.ib(default=3)
    interleave = attr.ib(default=False, convert=bool)
    cycles = attr.ib(default=1000)
    raw_results = attr.ib(
        default=attr.Factory(lambda: collections.defaultdict(list)))
    results = attr.ib(default=attr.Factory(dict))

    def run(self):
        if self.interleave:
            for _ in range(self.repeats):
                for example in self.examples:
                    self.raw_results[example].append(timeit.timeit(
                        stmt=example.statement,
                        setup=self.setup,
                        number=self.cycles,
                    ))
        else:
            for example in self.examples:
                self.raw_results[example].append(min(timeit.repeat(
                    stmt=example.statement,
                    setup=self.setup,
                    repeat=self.repeats,
                    number=self.cycles,
                )))

        self.results = {
            example: min(self.raw_results[example])
            for example in self.examples
        }

    def tabulate(self):
        minimum = min(self.results.values())
        lines = [
            'Repeats interleaved: {}'.format(self.interleave)
        ]
        for example in sorted(self.examples, key=lambda e: self.results[e]):
            lines.append('{percent:5}%   {statement} : {minimum}'.format(
                percent=round(100 * self.results[example] / minimum),
                statement=example.statement,
                minimum=self.results[example],
            ))

        return '\n'.join(lines)
