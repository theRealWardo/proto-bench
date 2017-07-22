# Proto Bench

A quick and rough example of how Protobuf performance is affected by message size.

```
python simple.py
```

```
simple_string serialization
averaged 5.30099868774 usec
simple_int serialization
averaged 4.469871521 usec
simple_big_int serialization
averaged 4.7459602356 usec
simple_enum serialization
averaged 7.65991210938 usec
```


```
python two.py
```

```
two_string serialization
averaged 7.64107704163 usec
two_int serialization
averaged 6.16502761841 usec
two_big_int serialization
averaged 9.50288772583 usec
two_enum serialization
averaged 5.70797920227 usec
```


```
python complex.py
```

```
one thing
averaged 17.2991752625 usec
two things
averaged 65.2959346771 usec
three things
averaged 87.9311561584 usec
four things
averaged 106.728076935 usec
five things
averaged 121.932983398 usec
six things
averaged 146.115064621 usec
1 lot of things
averaged 17.5409317017 usec
3 lots of things
averaged 2329.63895798 usec
4 lots of things
averaged 27911.8249416 usec
```
