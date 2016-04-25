#!/usr/bin/env python

from mytest import func1, func2, func3, MyClass

def main():
    func1()
    func2()
    func3()

    my_obj = MyClass('Bilbao', 'Igorre', 'Leioa')
    my_obj.hello()
    my_obj.not_hello()

if __name__ == "__main__":
    main()