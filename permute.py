'''class A:
    def f(self):
        return a.g()

    def g(self):
        return 'A'

class B(A):
    def g(self):
        return 'B'

a = A()
b = B()
print a.f(), b.f()
print a.g(), b.g()'''

'''width = 2
height = 3
data = [['*'] * width for i in range(height)]
print data

def display():
        print "\n".join(["".join(row) for row in data])

display()'''
def f():
    try:
        print "a"
        return
    except:
        print "b"
    else:
        print "c"
    finally:
        print "d"

f()