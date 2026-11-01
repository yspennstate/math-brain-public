#!/usr/bin/env python3
# Exact finite regression for R17-C034 maximal length-two deficiency filter.
from itertools import product

def pair(c,l):
    if l>=0: return ((str(1-c)*l)+str(c), str(c))
    return (str(c), (str(1-c)*(-l))+str(c))

def lcs(a,b):
    d=[0]*(len(b)+1)
    for x in a:
        e=[0]*(len(b)+1)
        for j,y in enumerate(b,1):
            e[j]=d[j-1]+1 if x==y else max(d[j],e[j-1])
        d=e
    return d[-1]
labels=[(c,l) for c in (0,1) for l in range(-7,8)]
def predicted(a,b):
    c,l=a; d,m=b
    return c==d and l*m<0 and abs(l)>=2 and abs(m)>=2
bad=[]; deficient=[]
for a,b in product(labels,repeat=2):
    x1,y1=pair(*a); x2,y2=pair(*b)
    L=lcs(x1+x2,y1+y2)
    q=L>2
    if q: deficient.append((a,b,L-2))
    if q!=predicted(a,b): bad.append((a,b,L,predicted(a,b)))
assert not bad
assert len(deficient)==144
from collections import Counter
cnt=Counter(d for _,_,d in deficient)
assert cnt==Counter({1:44,2:36,3:28,4:20,5:12,6:4})
print('R17 C034 exact h=8 length-two deficiency classification')
print('labels=',len(labels),'ordered_pairs=',len(labels)**2)
print('deficient_pairs=',len(deficient))
print('deficiency_histogram=',dict(sorted(cnt.items())))
print('criterion= same c, opposite signs, min(|l1|,|l2|)>=2')
print('ALL_900_REPRESENTATIVE_LABEL_PAIRS_CLASSIFIED_EXACTLY=PASS')
print('ALL_EXACT_CHECKS_PASS')
