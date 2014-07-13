#!/usr/bin/env python
__author__ = 'stvn'

class Calculate(object):
    def add(self, x, y):
        """Takes two integers and adds them together to produce the result.
        
        >>> c = Calculate()
        >>> c.add(1, 1)
        3

        >>> c.add(25, 125)
        150

        >>> c.add(1.0, 1.0)
        Traceback (most recent call last):
         ...
        TypeError: Invalid type: <type 'float'> and <type 'float'>
        """

        if type(x) == int and type(y) == int:
            return x + y
        else:
            raise TypeError("Invalid type: {} and {}"
                    .format(type(x), type(y)))

if __name__ == '__main__': #pragma: no coverage
    import doctest
    doctest.testmod()
    calc = Calculate()
    result = calc.add(2, 2)
    print result
