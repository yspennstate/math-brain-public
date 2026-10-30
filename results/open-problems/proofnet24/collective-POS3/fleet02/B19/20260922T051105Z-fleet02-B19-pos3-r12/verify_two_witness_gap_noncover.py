#!/usr/bin/env python3
from collections import Counter
from fractions import Fraction

NAMES=("r","x","p","s","y","a","t","q","z")
I={x:i for i,x in enumerate(NAMES)}
covers=(("r","x"),("r","s"),("r","a"),("x","y"),("p","y"),("p","a"),
        ("s","q"),("s","z"),("y","t"),("a","t"),("a","z"))
n=len(NAMES)
reach=[0]*n
for u,v in covers: reach[I[u]] |= 1<<I[v]
changed=True
while changed:
    changed=False
    for u in range(n):
        nr=reach[u]
        b=nr
        while b:
            bit=b&-b; v=bit.bit_length()-1
            nr |= reach[v]; b-=bit
        if nr!=reach[u]:
            reach[u]=nr; changed=True
pred=[0]*n
for u in range(n):
    b=reach[u]
    while b:
        bit=b&-b; v=bit.bit_length()-1
        pred[v] |= 1<<u; b-=bit

ext=[]
def rec(mask,seq):
    if mask==(1<<n)-1:
        ext.append(tuple(seq)); return
    for u in range(n):
        if not (mask>>u)&1 and pred[u]&~mask==0:
            rec(mask|(1<<u),seq+[u])
rec(0,[])
assert len(ext)==499

pat=Counter()
for L in ext:
    pos={v:k for k,v in enumerate(L)}
    H=pos[I["x"]]<pos[I["a"]]<pos[I["y"]]
    Ep=pos[I["x"]]<pos[I["p"]]
    Ez=pos[I["z"]]<pos[I["y"]]
    pat[(H,Ep,Ez)] += 1

H=sum(c for (h,ep,ez),c in pat.items() if h)
Ep=sum(c for (h,ep,ez),c in pat.items() if ep)
Ez=sum(c for (h,ep,ez),c in pat.items() if ez)
union=sum(c for (h,ep,ez),c in pat.items() if ep or ez)
H_out=sum(c for (h,ep,ez),c in pat.items() if h and not(ep or ez))
assert (H,Ep,Ez,union,H_out)==(201,126,125,229,90)
assert H_out>0
assert Fraction(Ep,499)<Fraction(1,3)
assert Fraction(Ez,499)<Fraction(1,3)

print("POS3_TWO_WITNESS_HEAVY_GAP_NONCOVER")
print("extensions",499)
print("H=x<a<y",Fraction(H,499))
print("Ep=x<p",Fraction(Ep,499))
print("Ez=z<y",Fraction(Ez,499))
print("Ep_union_Ez",Fraction(union,499))
print("H_outside_Ep_union_Ez",Fraction(H_out,499))
print("pattern_counts bits=(H,Ep,Ez)")
for bits,c in sorted(pat.items()):
    print(" ","".join("1" if b else "0" for b in bits),c)
print("conclusion","relation-witness export is not an event-cover/pigeonhole partition of the >1/3 heavy gap")
print("POS3_TWO_WITNESS_HEAVY_GAP_NONCOVER_PASS")
