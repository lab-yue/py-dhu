import time
import timeit
import signal


# from https://stackoverflow.com/a/22348885
class timeout:
    def __init__(self, seconds=1, error_message='Timeout'):
        self.seconds = seconds
        self.error_message = error_message

    def handle_timeout(self, signum, frame):
        raise TimeoutError(self.error_message)

    def __enter__(self):
        signal.signal(signal.SIGALRM, self.handle_timeout)
        signal.alarm(self.seconds)

    def __exit__(self, type, value, traceback):
        signal.alarm(0)


def run(name, size, number=100):
    try:
        with timeout(seconds=10):
            t = timeit.timeit(
                f"{name}.Maze({size},{size})", setup=f"import {name}", number=number
            )
        print(f"run {name} {size}x{size} {number} times, created in {t}s avg")
    except TimeoutError:
        print(f"run {name} {size}x{size} {number} times, timeout in 10s")


for size in [50, 100, 500, 1000]:
    run("MazeYue", size, 1000 // size)
    run("MazeYueOld", size, 1000 // size)
    run("MazeYama", size, 1000 // size)
    print("-" * 20)
