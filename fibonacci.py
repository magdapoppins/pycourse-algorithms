def fib(index):
    if index == 0 or index == 1:
        return index
    else:
        return fib(index-1)+fib(index-2)