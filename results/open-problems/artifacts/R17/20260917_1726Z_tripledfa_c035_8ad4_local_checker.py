#!/usr/bin/env python3
from itertools import product

def bar(c): return 1-c
def mp(c,l):
    if l>=0: return ((str(bar(c))*l)+str(c), str(c))
    return (str(c), (str(bar(c))*(-l))+str(c))
def pair(word):
    a=b=''
    for c,l in word:
        x,y=mp(c,l);a+=x;b+=y
    return a,b
def lcs(a,b):
    d=[0]*(len(b)+1)
    for x in a:
        n=[0]*(len(b)+1)
        for j,y in enumerate(b,1):
            n[j]=d[j-1]+1 if x==y else max(d[j],n[j-1])
        d=n
    return d[-1]
def deficient(w):
    a,b=pair(w); return lcs(a,b)>len(w)
def minimal_triple(w):
    return deficient(w) and not deficient(w[:2]) and not deficient(w[1:])

labels=[(c,l) for c in (0,1) for l in range(-7,8)]
# C034 adjacent regression.
pair_bad=[]
for u,v in product(labels,repeat=2):
    got=deficient((u,v))
    c1,l1=u;c2,l2=v
    want=(c1==c2 and l1*l2<0 and abs(l1)>=2 and abs(l2)>=2)
    assert got==want,(u,v,got,want)
    if got: pair_bad.append((u,v))
assert len(pair_bad)==144

# New family A: unit zigzags, four symmetry copies.
A=[]
for c in (0,1):
    for s in (-1,1):
        w=((c,s),(c,-s),(bar(c),-s))
        aa,bb=pair(w); L=lcs(aa,bb)
        assert L==4 and minimal_triple(w)
        A.append(w)
assert len(A)==4

# New family B on every h=8 exact representative magnitude 2..7.
B=[]
for c in (0,1):
    for s in (-1,1):
        for a in range(2,8):
            for b in range(2,8):
                w=((c,s*a),(bar(c),0),(c,-s*b))
                aa,bb=pair(w); L=lcs(aa,bb)
                assert L>=4 and minimal_triple(w)
                B.append(w)
assert len(B)==144

# Count every representative minimal deficient triple exactly.
count=0
for w in product(labels,repeat=3):
    if minimal_triple(w): count+=1
assert count==3032

# Coarse forbidden language and specialized 17-state DFA equivalence through length 5.
def coarse(l):
    if l<=-2:return '-H'
    if l==-1:return '-1'
    if l==0:return '0'
    if l==1:return '+1'
    return '+H'
coarse_symbols=[(c,t) for c in (0,1) for t in ('-H','-1','0','+1','+H')]
rep={'-H':-2,'-1':-1,'0':0,'+1':1,'+H':2}
forb2=[]
for c in (0,1):
    forb2 += [((c,'+H'),(c,'-H')),((c,'-H'),(c,'+H'))]
forb3=[]
for c in (0,1):
    for s in (-1,1):
        ts='+' if s>0 else '-'; tn='-' if s>0 else '+'
        forb3.append(((c,ts+'1'),(c,tn+'1'),(bar(c),tn+'1')))
        forb3.append(((c,ts+'H'),(bar(c),'0'),(c,tn+'H')))
forbidden=forb2+forb3

def H(c,s):return 1+2*c+(s<0)
def U(c,s):return 5+2*c+(s<0)
def P(c,s):return 9+2*c+(s<0)
def Q(c,s):return 13+2*c+(s<0)
def step(m,c,l):
    if abs(l)>=2:
        s=1 if l>0 else -1
        if 1<=m<=4:
            z=m-1;c0=z//2;s0=1 if z%2==0 else -1
            if c0==c and s0==-s:return -1
        if 13<=m<=16:
            z=m-13;c0=z//2;s0=1 if z%2==0 else -1
            if c0==c and s0==-s:return -1
        return H(c,s)
    if abs(l)==1:
        s=1 if l>0 else -1
        if 9<=m<=12:
            z=m-9;c0=z//2;s0=1 if z%2==0 else -1
            if c==bar(c0) and s==-s0:return -1
            if c==c0 and s==s0:return P(c0,-s0)
        if 5<=m<=8:
            z=m-5;c0=z//2;s0=1 if z%2==0 else -1
            if c==c0 and s==-s0:return P(c0,s0)
        return U(c,s)
    if 1<=m<=4:
        z=m-1;c0=z//2;s0=1 if z%2==0 else -1
        if c==bar(c0):return Q(c0,s0)
    return 0

def direct(seq):
    for f in forbidden:
        L=len(f)
        if any(tuple(seq[i:i+L])==f for i in range(len(seq)-L+1)):return False
    return True
def dfa(seq):
    m=0
    for c,t in seq:
        m=step(m,c,rep[t])
        if m<0:return False
    return True
checked=0
for n in range(1,6):
    for seq in product(coarse_symbols,repeat=n):
        assert direct(seq)==dfa(seq),seq
        checked+=1

print('R17 C035 exact local-deficiency and DFA checker')
print('h8_representative_labels =',len(labels))
print('length2_deficient_representative_words =',len(pair_bad))
print('family_A_unit_zigzag_words =',len(A))
print('family_B_h8_representative_words =',len(B))
print('all_minimal_deficient_length3_representative_words =',count)
print('new_family_representative_words =',len(A)+len(B))
print('dfa_nonrejecting_states = 17')
print('dfa_equivalence_sequences_checked =',checked)
print('EXACT_LOCAL_LCS_CLASSIFICATION_PASS')
print('EXACT_DFA_LANGUAGE_REGRESSION_PASS')
print('ALL_EXACT_CHECKS_PASS')
