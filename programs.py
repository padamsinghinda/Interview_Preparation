# -*- coding: utf-8 -*-
"""
Created on Wed Jan  3 23:56:52 2018

@author: Padam Singh
"""

def star_representation(n) :
    ''' Return star representation using the input number. ''' 
    star = []       
    for i in range(n):
        j = i+1
        while(j>0):
            star.append("*")
            j -= 1
        star.append("\n")
    for i in range(n):
        j = n-i-1
        while(j>0):
            star.append("*")
            j -= 1
        star.append("\n")
    return n,''.join(star)
    
def is_valid_ip_add(ip):
    ''' Return whether given ip_address is a valid IPV4 address or not. '''
    ip = ip.split('.')
    if len(ip) != 4 :
        return ip,"INVALID IP Address"
    else :
        for item in ip :
            if int(item)<0 or int(item)>255 :
                return ip,"INVALID IP Address"
    return ip,"VALID IP Address"

def is_prime(m):
    ''' Return whether given number is a prime number or not. '''
    import math
    for i in range(3,int(math.sqrt(m)+1)):
        if m%i == 0:
            return m,'Not a Prime Number'
    return m,'Prime Number'

def prime_numbers(n):
    ''' Return all the prime numbers till the input number provided as input. '''
    pass

def prime_factors(n):
    ''' Return all the prime factors for the input number provided as input. '''
    pass

def fibonacci(n):
    ''' Return fibonacci numbers till the input number provided as input. '''
    pass
    

if __name__ == '__main__' :
    out1 = star_representation(7)
    print(f"Program-1 : star representation for given number {out1[0]} is as below:\n{out1[1]}")
    
    out2 = is_valid_ip_add('245.543.234.2')
    print(f"Program-2 : Given ip address {out2[0]} is '{out2[1]}'")
    
    out3 = is_prime(97)
    print(f"Program-3 : Given Number {out3[0]} is '{out3[1]}'")