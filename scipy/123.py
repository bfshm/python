#%%
def decorate(func):
    cache = {}
    def wrap(n):
        if n not in cache:
            cache[n] = func(n)
        return cache[n]
    return wrap

@decorate
def fib(n):
    if n == 0 or n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

print([fib(n) for n in range(10)])