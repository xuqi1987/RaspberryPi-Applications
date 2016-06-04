def test1():
    print "hello"
    raise Exception("Error")
    print "hello2"

try:
    test1()
except Exception,X:
    print(X)
finally:
    print("hello3")