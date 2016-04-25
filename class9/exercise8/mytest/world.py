def func1():
    print "Hello world"

class MyClass(object):
    def __init__(self, var_a, var_b, var_c):
        self.var_a = var_a
        self.var_b = var_b
        self.var_c = var_c

    def hello(self):
        print "Hello world: %s %s %s" % (self.var_a, self.var_b, self.var_c)

    def not_hello(self):
        print "Bye Bye: %s %s %s" % (self.var_a, self.var_b, self.var_c)


class NewClass(MyClass):

    def __init__(self, var_a, var_b, var_c):
        print "The child class should do something additional in the __init__()"
        MyClass.__init__(self, var_a, var_b, var_c)

    def hello(self):
        print "Hello new world: %s %s %s" % (self.var_a, self.var_b, self.var_c)


if __name__ == "__main__":
    print "Program hello world"

