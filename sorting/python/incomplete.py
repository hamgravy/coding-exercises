#!/usr/bin/python
'''
The MIT License (MIT)

Copyright (c) 2015 Elliot Briggs

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

Is this helpful?
BTC: 1GKejoQRRNmhJz6hZetTd6J3xaKQMzVBAN
Proof of ownership: https://keybase.io/elliotbriggs
'''

from numpy import random
from numpy import array

numpoints = 16
unsorted = random.randint(numpoints, size=numpoints)
alreadysorted = sorted(array(unsorted, copy=True))

def swap(vec,a,b):
	return vec

def insertionsort(unsorted):
	return unsorted	

def selectionsort(unsorted):
	return unsorted

def bubblesort(unsorted):
	return unsorted

def shellsort(unsorted, gaps):
	return unsorted

print "----------insertion sort----------"
print "unsorted:"
print unsorted
isort = array(unsorted, copy=True)
isort = insertionsort(isort)
print "completed:"
print isort
if (isort == alreadysorted).all():
    print "sorted OK!"
else:
    print "sort failed!"

print "----------selection sort----------"
print "unsorted:"
print unsorted
selsort = array(unsorted, copy=True)
selsort = selectionsort(selsort)
print "completed:"
print selsort
if (selsort == alreadysorted).all():
    print "sorted OK!"
else:
    print "sort failed!"

print "----------bubble sort----------"
print "unsorted:"
print unsorted
bubsort = array(unsorted, copy=True)
bubsort = bubblesort(bubsort)
print "completed:"
print bubsort
if (bubsort == alreadysorted).all():
    print "sorted OK!"
else:
    print "sort failed!"

print "----------shell's sort----------"
print "unsorted:"
print unsorted
shellsorted = array(unsorted, copy=True)
gaps = [5,3,1] # this is fairly arbitrary, always end with 1 though
shellsorted = shellsort(shellsorted, gaps)
print "completed:"
print shellsorted
if (shellsorted == alreadysorted).all():
    print "sorted OK!"
else:
    print "sort failed!"


