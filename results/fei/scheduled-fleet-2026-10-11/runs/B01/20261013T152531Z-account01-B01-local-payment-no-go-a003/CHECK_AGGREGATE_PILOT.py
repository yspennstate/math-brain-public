#!/usr/bin/env python3
"""Bounded search for violations of G <= H+I; numerical evidence only."""
from math import log2
import random

def fwht(a):
    a=list(a);h=1
    while h<len(a):
        for i in range(0,len(a),2*h):
            for j in range(i,i+h):
                x,y=a[j],a[j+h];a[j],a[j+h]=x+y,x-y
        h*=2
    return a

def hu(v):
    N=len(v);n=N.bit_length()-1;w=fwht(v);p=[z*z/(N*N) for z in w];q=p[:]
    for j in range(n):
        for s in range(N):
            if not((s>>j)&1):q[s]+=q[s|(1<<j)]
    H=sum(-x*log2(x) for x in p if x)
    U=sum(x*log2(q[s]/x) for s,x in enumerate(p) if x)
    return H,U

def child(v,j,b):return [v[x] for x in range(len(v)) if ((x>>j)&1)==b]

def evaluate(v):
    n=len(v).bit_length()-1;H,U=hu(v);I=0.;G=0.
    for j in range(n):
        I+=sum(v[x]!=v[x^(1<<j)] for x in range(len(v)))/len(v)
        G+=U-(hu(child(v,j,0))[1]+hu(child(v,j,1))[1])/2
    return G-H-I,(H,U,I,G)

total=0;best=(-1e100,None)
for n in range(1,5):
    N=1<<n
    for mask in range(1<<(N-1)):
        v=[1 if (mask>>x)&1 else -1 for x in range(N)]
        d,data=evaluate(v);total+=1
        if d>best[0]:best=(d,(n,mask,data))
        assert d<=1e-10
print(f"exhaustive_mod_output_sign={total}")
print(f"exhaustive_max_G_minus_H_minus_I={best[0]}")

rng=random.Random(20261013);random_total=0
for n,trials in [(5,20000),(6,5000),(7,1000)]:
    rb=(-1e100,None);N=1<<n
    for t in range(trials):
        v=[rng.choice((-1,1)) for _ in range(N)]
        d,data=evaluate(v);random_total+=1
        if d>rb[0]:rb=(d,(t,data))
        assert d<=1e-10
    print(f"random_dimension_{n}_trials={trials}")
    print(f"random_dimension_{n}_max_G_minus_H_minus_I={rb[0]}")
print(f"random_total={random_total}")
print("NUMERICAL_PASS_NOT_PROOF")

