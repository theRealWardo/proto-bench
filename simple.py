import time
import simple_pb2


def serialize(pb):
    pb.SerializeToString()


def simple_string():
    pb = simple_pb2.SimpleString()
    pb.one = "a normal enough length string"
    return pb


def simple_int():
    pb = simple_pb2.SimpleInt()
    pb.one = 1
    return pb


def simple_big_int():
    pb = simple_pb2.SimpleBigInt()
    pb.one = 1
    return pb


def simple_enum():
    pb = simple_pb2.SimpleEnum()
    pb.one = simple_pb2.SimpleEnum.TEST
    return pb


def bench(fname):
    setup = "from __main__ import serialize; from __main__ import %s; pb = %s()" % (fname, fname)
    total = timeit.timeit("serialize(pb)", setup=setup, number=1000)
    average = total / 1000
    print "averaged %s usec" % (average * 1000000)


if __name__ == "__main__":
    import timeit
    print "simple_string serialization"
    bench("simple_string")

    print "simple_int serialization"
    bench("simple_int")

    print "simple_big_int serialization"
    bench("simple_big_int")

    print "simple_enum serialization"
    bench("simple_enum")
