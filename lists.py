from timeit import Timer

def test1():
    l = []
    for i in range(1000):
        l = l + [i]

def test2():
    l = []
    for i in range(1000):
        l.append(i)

def test3():
    l = [i for i in range(1000)]

def test4():
    l = list(range(1000))

t1 = Timer("test1()","from __main__ import test1")
print("Concatenation:",t1.timeit(1000),"milliseconds")

t2 = Timer("test2()","from __main__ import test2")
print("append:",t2.timeit(1000),"milliseconds")

t3 = Timer("test3()","from __main__ import test3")
print("Comprehension:",t3.timeit(1000),"milliseconds")

t4 = Timer("test4()","from __main__ import test4")
print("Range:",t4.timeit(1000),"milliseconds")

