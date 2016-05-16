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

#for i in [1,2,3,4]:
for i in {"concat": 1, "append": 2, "comprehension": 3, "list range": 4}.iteritems():
	v = str(i[1])
	print(str(i[0]) , Timer("test" + v, "from __main__ import test" + v).timeit(number=1000))

