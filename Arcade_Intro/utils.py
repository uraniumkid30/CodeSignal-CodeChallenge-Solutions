import time
import functools


def timefunc(module_name):
    def timer(func):
        """timefunc's doc"""

        @functools.wraps(func)
        def time_closure(*args, **kwargs):
            """time_wrapper's doc string"""
            start = time.perf_counter()
            result = func(*args, **kwargs)
            time_elapsed = time.perf_counter() - start
            print(
                "%s Input args:[%s, %s] took: %2.8f sec"
                % (f"{module_name} {func.__name__}", args, kwargs, time_elapsed)
            )
            return result

        return time_closure

    return timer
