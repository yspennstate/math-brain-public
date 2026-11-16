"""PROVED: strict certificates are impossible on nine inherited OPEN boxes.

The witnesses are in Q[s]/(s^2-d), d in {5,15}, s>0. Arithmetic below uses
integer/rational coefficients only; enclosure comparisons square rationals.
These witnesses have connected=0 and are NOT feasible counterexamples.
"""
import json
from pathlib import Path
from fractions import Fraction as F
from math import prod
from exact_bernstein import data,active_constraints

HERE=Path(__file__).resolve().parent
ZERO=(F(0),F(0));ONE=(F(1),F(0))

def add(x,y):return x[0]+y[0],x[1]+y[1]
def mul(x,y,d=5):return x[0]*y[0]+d*x[1]*y[1],x[0]*y[1]+x[1]*y[0]
def power(x,n,d=5):
    out=ONE
    for _ in range(n):out=mul(out,x,d)
    return out
def sign(x,d=5):
    a,b=x
    if not b:return (a>0)-(a<0)
    if not a:return (b>0)-(b<0)
    if a>0 and b>0:return 1
    if a<0 and b<0:return -1
    difference=a*a-d*b*b
    assert difference != 0 # Both supported radicands are nonsquares.
    return ((difference>0)-(difference<0))*((a>0)-(a<0))
def evaluate(p,point,d=5):
    out=ZERO
    for m,c in p.items():
        v=(F(c),F(0))
        for x,n in zip(point,m):v=mul(v,power(x,n,d),d)
        out=add(out,v)
    return out
def in_box(point,box,d=5):
    return all(sign(add(x,(-F(a),F(0))),d)>=0 and
               sign(add((F(b),F(0)),(-x[0],-x[1])),d)>=0
               for x,(a,b) in zip(point,box))
def encode(point):return [[str(a),str(b)] for a,b in point]

def witnesses():
    rat=lambda x:(F(x),F(0));root=lambda x:(F(0),F(x))
    five=[
        [rat(4),rat(-1),root(-1),rat(-1),root(-1),root(1)],
        [rat(4),rat(-1),root(-1),rat(-1),root(1),root(1)],
        [rat(4),rat(-1),root(1),rat(-1),root(-1),root(1)],
        [rat(F(3,2)),rat(-1),root(-1),rat(-1),root(F(1,2)),root(F(1,2))],
        [rat(F(3,2)),rat(-1),root(F(1,2)),rat(-1),root(-1),root(F(1,2))],
    ]
    fifteen=[
        [rat(4),rat(-1),root(F(-1,3)),rat(-1),root(F(-1,3)),root(1)],
        [rat(4),rat(-1),root(-1),rat(-1),root(F(1,3)),root(F(1,3))],
        [rat(4),rat(-1),root(F(1,3)),rat(-1),root(-1),root(F(1,3))],
        [rat(4),rat(-1),root(F(1,3)),rat(-1),root(F(1,3)),root(F(1,3))],
    ]
    return [(5,p) for p in five]+[(15,p) for p in fifteen]
