#!/usr/bin/env python3
import math
import numpy as np

C = 6.5218512
N = 512
T = np.array([78,79,113,121,228,484,170,186,149,151,338,466,284,316,291,295,393,457], dtype=np.int64)
SOURCE = {(78,79),(113,121),(228,484),(170,186),(149,151),(338,466),(284,316),(291,295),(393,457)}
SOURCE = {tuple(sorted(p)) for p in SOURCE}

# Exact induced-edge check.
edges=set()
for i in range(len(T)):
    for j in range(i+1,len(T)):
        if int(T[i]^T[j]).bit_count()==1:
            edges.add(tuple(sorted((int(T[i]),int(T[j])))))
assert edges == SOURCE

# Algebraic constants.
q0=(5*C-16)/N
c0=9*math.log2(3)/8
assert C>4 and c0>1
odd_min=(C/2-2)/N
assert odd_min>0

# Exhaustive unsigned-group sanity check.  This is not needed by the symbolic proof:
# it tests all 2^18-1 subsets using the exact Walsh integer sums.
S=np.arange(N,dtype=np.int64)
pc=np.array([int(i).bit_count() for i in range(N)],dtype=np.int8)
signs=np.empty((18,N),dtype=np.int8)
for j,x in enumerate(T):
    signs[j]=1-2*(pc[S & x]&1)

arr=np.zeros((1,N),dtype=np.int8)
for j in range(18):
    arr=np.concatenate([arr, arr+signs[j]],axis=0)

hlookup=np.zeros(19,dtype=float)
for z in range(1,19):
    q=(z/N)**2
    hlookup[z]=q*math.log2(1/q)

H=np.empty(1<<18,dtype=float)
chunk=8192
for a in range(0,1<<18,chunk):
    H[a:a+chunk]=hlookup[np.abs(arr[a:a+chunk])].sum(axis=1)

idx=np.arange(1<<18,dtype=np.uint32)
r=np.array([int(i).bit_count() for i in range(1<<18)],dtype=np.int16)
e=np.zeros(1<<18,dtype=np.int16)
for j in range(0,18,2):
    e += ((((idx>>j)&1)&((idx>>(j+1))&1))).astype(np.int16)
I=(11*r-2*e)/(2*N)
gap=C*I-H-r*q0
nonzero=np.arange(1,1<<18)
mingap=float(gap[nonzero].min())
eq=np.where((r>0)&(np.abs(gap)<1e-12))[0]
expected=np.array([3<<(2*j) for j in range(9)],dtype=np.int64)
assert mingap > -2e-13
assert np.array_equal(eq,expected)

print("PASS")
print(f"induced_edges={len(edges)}")
print(f"unsigned_groups_checked={(1<<18)-1}")
print(f"q0_per_exceptional_row={q0:.15f}")
print(f"odd_symbolic_margin_floor={odd_min:.15f}")
print("zero_gap_unsigned_groups=9_source_pairs")
