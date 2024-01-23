def add(*args):
    sum = 0
    for _ in args:
        sum += _
    # print(type(args))
    #<class 'tuple'>
    print(args[0])  #tuples are Indexed, so you can access whichever index you want from the Tuple list.
    return sum


print(add(4,8,89,103,333,456,789,8657))