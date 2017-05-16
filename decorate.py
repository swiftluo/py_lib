from functools import wraps
import time


def timing_func(func):
    '''
    函数计时器
    '''
    @wraps(func)
    def wrapps(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(func.__name__ + " 耗时:" + str(end-start))
        return result
    return wrapps


if __name__ == "__main__":
    @timing_func
    def add(x, y):
        return x + y

    add(1, 2)
