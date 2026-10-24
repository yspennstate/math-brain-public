#!/usr/bin/env python3
from itertools import permutations

W=10
V='0'; C='C'
pairs=[(2*k,2*k+1) for k in range(W//2)]

def initial():
    s={}
    # two-row vacant strip
    for x in range(W):
        s[(x,0)]=V; s[(x,1)]=V
    # lateral guards for current and next top rows
    for y in (1,2):
        s[(-1,y)]=V; s[(W,y)]=V
    # consumable rail and next rail
    for x in range(W):
        s[(x,2)]=C; s[(x,3)]=C
    return s

def nbrs(x,y):
    return [(x+1,y),(x-1,y),(x,y+1),(x,y-1)]

def fire(s,a,b):
    # O2 adsorbs on horizontal edge (a,1)-(b,1); each O must have exactly
    # one CO neighbor, directly above, so instantaneous reaction restores
    # the adsorption site to vacant and consumes that rail CO.
    for x in (a,b):
        assert s[(x,1)]==V
        co=[z for z in nbrs(x,1) if s.get(z)==C]
        assert co==[(x,2)], (x,co)
    for x in (a,b):
        s[(x,2)]=V
        s[(x,1)]=V

def shifted_seed(s):
    return (
        all(s[(x,1)]==V and s[(x,2)]==V for x in range(W))
        and s[(-1,2)]==V and s[(W,2)]==V
        and all(s[(x,3)]==C for x in range(W))
    )

for order in permutations(pairs):
    s=initial()
    for e in order:
        fire(s,*e)
    assert shifted_seed(s)

print('orders_checked=120')
print('designated_edges=',pairs)
print('PASS: every order of the five disjoint top-row O2 events deterministically consumes the width-10 CO fuel rail and produces the one-row-up translated vacant-strip seed; the next CO rail is untouched.')
