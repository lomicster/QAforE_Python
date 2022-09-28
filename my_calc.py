def sum_it(x, y):
    return x + y

def subs(x, y):
    return x - y

def prod(x, y):
    return x*y

def div(x, y):
    try:
        return x / y
    except:
        return "Can't divide by 0"
# (Здесь нужно будет прописать обработку исключения - что делать в случае появления ислючения)