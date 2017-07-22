import time
import complex_pb2


def serialize(pb):
    pb.SerializeToString()


def build_a_thing():
    pb = complex_pb2.Thing()
    pb.one = "a normal enough length string"
    pb.two = "another string"
    pb.three = 1
    pb.four = 2
    pb.five = 1
    pb.six = 2
    pb.seven = complex_pb2.Thing.TEST 
    pb.eight = complex_pb2.Thing.TEST 
    return pb


def build_multiple_things(thing, multiple=1, depth=0):
    thing.more.extend([build_a_thing() for _ in range(0, multiple)])
    if depth > 0:
        for i in range(0, multiple):
            build_multiple_things(thing.more[i], multiple=multiple, depth=depth-1)


def bench(things=1, depth=0):
    building_things = ("build_multiple_things(thing, multiple=%s, depth=%s)" % (things, depth)) if things > 1 else ""
    setup = """
from __main__ import serialize
from __main__ import build_a_thing
from __main__ import build_multiple_things
thing = build_a_thing()
%s
""" % building_things
    total = timeit.timeit("serialize(thing)", setup=setup, number=1000)
    average = total / 1000
    print "averaged %s usec" % (average * 1000000)


if __name__ == "__main__":
    import timeit
    print "one thing"
    bench(things=1)

    print "two things"
    bench(things=2)

    print "three things"
    bench(things=3)

    print "four things"
    bench(things=4)

    print "five things"
    bench(things=5)

    print "six things"
    bench(things=6)

    print "1 lot of things"
    bench(things=1, depth=2)

    print "3 lots of things"
    bench(things=3, depth=3)

    print "4 lots of things"
    bench(things=4, depth=4)
