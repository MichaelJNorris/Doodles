# -*- coding: utf-8 -*-
"""
Created on Tue Dec  2 17:57:18 2014

@author: michaelnorris
"""
from functools import reduce
import matplotlib.pyplot as plt
import numpy as np

def collatz(n):
    L = [n]
    while n > 1: 
        if n%2 == 0:
            n = int(n/2)
        else:
            n = 3*n+1
        L.append(n)
    return L
    
def collatz_jumps(n):
    ups = 0
    downs = 0
    while n > 1: 
        if n%2 == 0:
            n = int(n/2)
            downs += 1
        else:
            n = 3*n+1
            ups += 1
    return (downs,ups)
    
def collatz_ratchet(x):
    L = [x]
    n = x
    while n >= x: 
        if n%2 == 0:
            n = int(n/2)
        else:
            n = 3*n+1
        L.append(n)
    return L
    
def collatz_ratchet_jumps(x):
    ups = 0
    downs = 0
    n = x
    while n >= x: 
        if n%2 == 0:
            n = int(n/2)
            downs += 1
        else:
            n = 3*n+1
            ups += 1
    return (downs,ups)
        
def inv_collatz(n):
    s = set([2*n])
    if n > 3 and n%3 == 1:
        s.add(int((n-1)/3))
    return s
    
def flatten(list_of_sets):
    return reduce(lambda left, right: left.union(right), list_of_sets)
    
def cthru(s,n):
    if n <= 0:
        return s
    else:
        return s.union(cthru(flatten([inv_collatz(x) for x in s]), n-1))
        
def plot1():
    N = [len(collatz(3+2*x)) for x in range(100000)]
    plt.plot(N, marker='.', linestyle=' ')
    plt.show()
    
def plot2():    
    N = [collatz_jumps(3+2*x) for x in range(100000)]
    X = np.array(N).transpose()
    plt.plot(np.log(X[0]/X[1]), marker='.', linestyle=' ')
    plt.show()
    
def plot3():
    N = [len(collatz_ratchet(3+2*x)) for x in range(100000)]
    plt.plot(N, marker='.', linestyle=' ')
    plt.show()
    
def plot4():    
    N = [collatz_ratchet_jumps(3+2*x) for x in range(100000)]
    X = np.array(N).transpose()
    plt.plot(np.log(X[0]/X[1]), marker='.', linestyle=' ')
    plt.show()

def plot5():
    """
    Noticing that the lengths of sequence from a number to any 
    lower number ("ratchet") only seem to have specific lengths.
    I'm wondering whether the pattern of those lengths can be
    used in some sort of inductive argument to say something
    about the collatz process. The differences are 2 or 3,
    alternating in an interesting binary pattern. Can that
    pattern be predicted and extrapolated?
    -> https://oeis.org/A122437
    """
    N = [len(collatz_ratchet(3+2*x))-1 for x in range(400000)]
    L = list(set(N))
    L.sort()
    plt.plot(np.diff(L))
    plt.show()
    
