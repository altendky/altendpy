import altendpy.timeit


def test_runner():
    short = altendpy.timeit.Example(statement="time.sleep(0.1)")
    long = altendpy.timeit.Example(statement="time.sleep(0.2)")

    runner = altendpy.timeit.Runner(
        examples=(short, long),
        repeats=1,
        interleave=True,
        cycles=10,
    )

    runner.run()
    assert 1.8 < runner.results[long] / runner.results[short] < 2.2
