# 1
def leave (func):
    def wrapper(ar):
        result=func(ar)
        b=100%ar
        if b == 0:
            print("We are OK!")
        else:
            print(f'Bad news guys, we got {b}')
        return result
    return wrapper
@leave
def funk(i):
    return i
funk(99)
#2
def so_sad(func):
    def wrappery(py):
      try:
        res=func(py)
        if py == int:
            print(res)
      except:
        if py==str():
          raise ValueError("string type is not supported")
    return wrappery


@so_sad
def ria(a):
    la = [a +1]
    print (la)
print(ria(5))
#3
def so_cache(func):
    cache={}
    func.__count__ = 0

    def wrapper(my):
        res=func(my)
        func.__count__ += 1

        if my not in cache:
            cache[my]=func(my)

            print(f'Function executed with counter = {func.__count__}, function result = {print(res)}')
        else:
            func.__count__ += (1-1)
            print(f'Used cache with counter = {func.__count__}')

    return wrapper
@so_cache
def my_story(a):
    print(f'this is {a}')
my_story(5)
my_story(5)
my_story(5)