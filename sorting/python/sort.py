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
from numpy import reshape
from numpy import append
from numpy import ceil

numpoints = 22
unsorted = random.randint(numpoints, size=numpoints)
alreadysorted = sorted(array(unsorted, copy=True))

def swap(vec,a,b):
	tmp=vec[a]
	vec[a]=vec[b]
	vec[b]=tmp
	return vec

def insertionsort(unsorted):
	numpoints=len(unsorted)
	for i in range(1,numpoints,1):
		for k in range(i,0,-1):
			if unsorted[k] < unsorted[k-1]:
				unsorted = swap(unsorted,k,k-1)
			else:
				print "break"
				break
			print unsorted
	return unsorted	

def selectionsort(unsorted):
	for i in range(0,numpoints,1):
		k=i
		#print range(i,numpoints,1) 
		for j in range(i+1,numpoints,1):
			#print "j:%d, k:%d"%(selsort[j],selsort[k])
			if unsorted[j] < unsorted[k]: # compare with the smallest seen
				k=j	# update the index of the smallest seen
		swap(unsorted,k,i) # swap i with k (the smallest)
		print unsorted
	return unsorted

def bubblesort(unsorted):
	for i in range(0,numpoints-1,1):
		#print range(numpoints-1,i,-1)
		for j in range(numpoints-1,i,-1):
			if unsorted[j] < unsorted[j-1]:
				swap(unsorted,j,j-1)
			print unsorted
	return unsorted

def shellsort(unsorted, gaps):
	for gap in gaps:
		print "gap: %s"%(gap)
		for i in range(0,gap,1):
			points = range(i,numpoints,gap)
			print unsorted[points]
			shellgap = insertionsort(unsorted[points])
			unsorted[points] = shellgap
	return unsorted

def mergesort(unsorted):
	windowsize=1
	while (windowsize < numpoints):	
		windowsize = windowsize * 2
		if windowsize > numpoints:
			windowsize = numpoints
		print "windowsize: %d"%(windowsize)
		for window in range(numpoints/windowsize):
			print "window index: %d"%(window)
			i = range(window*windowsize,window*windowsize+windowsize,1)
			unsorted[i] = insertionsort(unsorted[i])
		print unsorted
	return unsorted

print "----------insertion sort----------"
print "unsorted:"
print unsorted
isort = array(unsorted, copy=True)
isort = insertionsort(isort)
print "completed:"
print isort

print "----------selection sort----------"
print "unsorted:"
print unsorted
selsort = array(unsorted, copy=True)
selsort = selectionsort(selsort)
print "completed:"
print selsort

print "----------bubble sort----------"
print "unsorted:"
print unsorted
bubsort = array(unsorted, copy=True)
bubsort = bubblesort(bubsort)
print "completed:"
print bubsort

print "----------shell's sort----------"
print "unsorted:"
print unsorted
shellsorted = array(unsorted, copy=True)
gaps = [7,5,3,1] # this is fairly arbitrary, always end with 1 though
shellsorted = shellsort(shellsorted, gaps)
print "completed:"
print shellsorted

print "----------merge sort----------"
print "unsorted:"
print unsorted
mergesorted = array(unsorted, copy=True)
mergesorted = mergesort(mergesorted)
print "completed:"
print mergesorted

print "----------test results----------"
if (isort == alreadysorted).all():
    print "insertion sort sorted OK!"
else:
    print "insertion sort failed!"

if (selsort == alreadysorted).all():
    print "selection sort sorted OK!"
else:
    print "selection sort failed!"

if (bubsort == alreadysorted).all():
    print "bubble sort sorted OK!"
else:
    print "bubble sort failed!"

if (shellsorted == alreadysorted).all():
    print "shell's sort sorted OK!"
else:
    print "shell's sort failed!"

if (mergesorted == alreadysorted).all():
    print "merge sort sorted OK!"
else:
    print "merge sort failed!"
