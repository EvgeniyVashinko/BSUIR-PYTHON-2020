def cached(func) :
    dict_arg = {}

    def wrapper(*args) :
        if args not in dict_arg :
            dict_arg[args] = func(*args)
        return dict_arg[args]

    return wrapper


@cached
def sum_(*args) :
    return sum(args)


@cached
def mul_(*args) :
    res = 1
    for i in args :
        res *= i
    return res
