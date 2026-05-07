#!/usr/bin/env python3

def pow(a, b):

    if b == 0:
        return 1
    
    exponent = b if b > 0 else -b
    result = 1
    
    for _ in range(exponent):
        result *= a
        
    if b < 0:
        return 1 / result
        
    return result
