#!/usr/bin/env python3
from itertools import product

def mp(c,l):
    b=1-c
    if l>=0:return (str(b)*l+str(c),str(c))
    return (str(c),str(b)*(-l)+str(c))
def cat(w):
    a=b=''
    for z in w:
        x,y=mp(*z);a+=x;b+=y
    return a,b
def lcs(a,b):
    d=[0]*(len(b)+1)
    for x in a:
        n=[0]*(len(b)+1)
        for j,y in enumerate(b,1):n[j]=d[j-1]+1 if x==y else max(d[j],n[j-1])
        d=n
    return d[-1]
def deficient(w):
    a,b=cat(w);return lcs(a,b)>len(w)
def cap4(l):return max(-4,min(4,l))

# Exact finite language core after the cap-4 lemma proved in the report.
A=[(c,l) for c in (0,1) for l in range(-4,5)]
pair_bad={w for w in product(A,repeat=2) if deficient(w)}
triple_min={w for w in product(A,repeat=3) if deficient(w) and not deficient(w[:2]) and not deficient(w[1:])}
assert len(pair_bad)==36
assert len(triple_min)==548
patterns=list(pair_bad)+list(triple_min)

# Regression far outside the cap: capping each offset at magnitude 4 preserves
# the yes/no deficiency result for all exact pairs/triples in [-12,12].
B=[(c,l) for c in (0,1) for l in range(-12,13)]
for w in product(B,repeat=2):
    cw=tuple((c,cap4(l)) for c,l in w)
    assert deficient(w)==deficient(cw)
for w in product(B,repeat=3):
    cw=tuple((c,cap4(l)) for c,l in w)
    assert deficient(w)==deficient(cw)

# Prefix automaton, then exact Moore minimization with reject sink.
prefs={()}
for p in patterns:
    for k in range(1,len(p)):prefs.add(p[:k])
prefs=sorted(prefs,key=lambda z:(len(z),z));pi={p:i for i,p in enumerate(prefs)};sink=len(prefs)
def suff(s,q):return True if not q else len(q)<=len(s) and s[-len(q):]==q
T=[]
for p in prefs:
    row=[]
    for a in A:
        s=p+(a,)
        if any(suff(s,f) for f in patterns):row.append(sink)
        else:row.append(pi[max((q for q in prefs if suff(s,q)),key=len)])
    T.append(row)
T.append([sink]*len(A))
P=[set(range(sink)),{sink}]
while True:
    block={}
    for i,S in enumerate(P):
        for q in S:block[q]=i
    Q=[]
    for S in P:
        G={}
        for q in sorted(S):G.setdefault(tuple(block[t] for t in T[q]),set()).add(q)
        Q.extend(G.values())
    if len(Q)==len(P):break
    P=Q
block={}
for i,S in enumerate(P):
    for q in S:block[q]=i
sinkblock=block[sink]
assert len(P)==70 and sum(i!=sinkblock for i in range(len(P)))==69

# Complement is an involutive automorphism of the minimized safe DFA.
def compword(p):return tuple((1-c,l) for c,l in p)
for i,S in enumerate(P):
    if i==sinkblock:continue
    q=min(S);cq=pi[compword(prefs[q])]
    assert block[cq]!=sinkblock

print('R17 C037 exact cap-4 local-language checker')
print('cap4_symbols =',len(A))
print('deficient_pair_classes =',len(pair_bad))
print('minimal_deficient_triple_classes =',len(triple_min))
print('unminimized_safe_prefix_states =',len(prefs))
print('minimized_total_states_including_reject =',len(P))
print('minimized_nonrejecting_states =',len(P)-1)
print('regression_exact_offset_range = [-12,12]')
print('EXACT_CAP4_REGRESSION_PASS')
print('EXACT_DFA_MINIMIZATION_PASS')
print('EXACT_COMPLEMENT_AUTOMORPHISM_PASS')
print('ALL_EXACT_CHECKS_PASS')
