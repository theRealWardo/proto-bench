import time
import two_pb2


def serialize(pb):
    pb.SerializeToString()


def two_string():
    pb = two_pb2.TwoString()
    pb.one = "a normal enough length string"
    pb.two = "another string"
    return pb


def two_int():
    pb = two_pb2.TwoInt()
    pb.one = 1
    pb.two = 2
    return pb


def two_big_int():
    pb = two_pb2.TwoBigInt()
    pb.one = 1
    pb.two = 2
    return pb


def two_enum():
    pb = two_pb2.TwoEnum()
    pb.one = two_pb2.TwoEnum.TEST
    pb.two = two_pb2.TwoEnum.TEST
    return pb


def bench(fname):
    setup = "from __main__ import serialize; from __main__ import %s; pb = %s()" % (fname, fname)
    total = timeit.timeit("serialize(pb)", setup=setup, number=1000)
    average = total / 1000
    print "averaged %s usec" % (average * 1000000)


if __name__ == "__main__":
    import timeit
    print "two_string serialization"
    bench("two_string")

    print "two_int serialization"
    bench("two_int")

    print "two_big_int serialization"
    bench("two_big_int")

    print "two_enum serialization"
    bench("two_enum")

