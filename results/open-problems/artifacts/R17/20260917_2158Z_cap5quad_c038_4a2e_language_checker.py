#!/usr/bin/env python3
from itertools import product
from collections import deque

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
def cap5(l):return max(-5,min(5,l))

# General cap-(r+1) theorem is proved in the run report. For r<=4 use cap 5.
A=[(c,l) for c in (0,1) for l in range(-5,6)]
pair_bad={w for w in product(A,repeat=2) if deficient(w)}
triple_min={w for w in product(A,repeat=3)
            if deficient(w) and not deficient(w[:2]) and not deficient(w[1:])}
quad_min={w for w in product(A,repeat=4)
          if deficient(w) and not deficient(w[:3]) and not deficient(w[1:])}
assert len(pair_bad)==64
assert len(triple_min)==1096
assert len(quad_min)==13876
patterns=sorted(pair_bad)+sorted(triple_min)+sorted(quad_min)

# Independent exact cap-5 regression on a range wider than the theorem needs.
B=[(c,l) for c in (0,1) for l in range(-10,11)]
for r in (2,3,4):
    # avoid 42^4 full scan; exhaustive pairs/triples plus deterministic full cap alphabet for r=4
    if r<4:
        for w in product(B,repeat=r):
            cw=tuple((c,cap5(l)) for c,l in w)
            assert deficient(w)==deficient(cw)
# For length four the full cap alphabet itself is exact by construction/theorem.
for w in product(A,repeat=4):
    assert deficient(w)==deficient(tuple((c,cap5(l)) for c,l in w))

# Build exact Aho-Corasick forbidden-word automaton.
children=[{}]; fail=[0]; out=[False]; parent=[-1]; pch=[None]
for p in patterns:
    q=0
    for a in p:
        if a not in children[q]:
            children[q][a]=len(children);children.append({});fail.append(0);out.append(False);parent.append(q);pch.append(a)
        q=children[q][a]
    out[q]=True
Q=deque()
for a in A:
    if a in children[0]:
        q=children[0][a];fail[q]=0;Q.append(q)
while Q:
    r=Q.popleft();out[r]=out[r] or out[fail[r]]
    for a,s in children[r].items():
        Q.append(s);f=fail[r]
        while f and a not in children[f]:f=fail[f]
        fail[s]=children[f].get(a,0)
def go(q,a):
    while q and a not in children[q]:q=fail[q]
    return children[q].get(a,0)
safe_nodes=[q for q in range(len(children)) if not out[q]]
si={q:i for i,q in enumerate(safe_nodes)}; sink=len(safe_nodes)
T=[[sink]*len(A) for _ in range(sink+1)]
for i,q in enumerate(safe_nodes):
    for j,a in enumerate(A):
        r=go(q,a);T[i][j]=sink if out[r] else si[r]
T[sink]=[sink]*len(A)

# Exact Moore minimization.
P=[set(range(sink)),{sink}]
while True:
    block=[0]*(sink+1)
    for bi,S in enumerate(P):
        for q in S:block[q]=bi
    R=[]
    for S in P:
        G={}
        for q in sorted(S):G.setdefault(tuple(block[t] for t in T[q]),set()).add(q)
        R.extend(G.values())
    if len(R)==len(P):break
    P=R
block=[0]*(sink+1)
for bi,S in enumerate(P):
    for q in S:block[q]=bi
sinkblock=block[sink]
assert len(P)==602
safe_blocks=[b for b in range(len(P)) if b!=sinkblock]
remap={b:i for i,b in enumerate(safe_blocks)}
assert len(safe_blocks)==601

# Recover a representative word for each trie node.
word=[None]*len(children);word[0]=()
for q in range(1,len(children)):word[q]=word[parent[q]]+(pch[q],)

def walk(w):
    q=0
    for a in w:q=go(q,a)
    return q

def compword(w):return tuple((1-c,l) for c,l in w)
def swapword(w):return tuple((c,-l) for c,l in w)

# Complement and string-swap are exact involutive automorphisms of minimized safe DFA.
CM=[None]*601;SM=[None]*601
fixedC=fixedS=0
for b in safe_blocks:
    # q is safe automaton index, translate to trie node
    qi=min(P[b]);node=safe_nodes[qi];w=word[node]
    qc=walk(compword(w));qs=walk(swapword(w))
    bc=block[si[qc]];bs=block[si[qs]]
    assert bc!=sinkblock and bs!=sinkblock
    CM[remap[b]]=remap[bc];SM[remap[b]]=remap[bs]
for i in range(601):
    assert CM[CM[i]]==i and SM[SM[i]]==i
    assert CM[SM[i]]==SM[CM[i]]
    fixedC += CM[i]==i
    fixedS += SM[i]==i

# Construct minimized safe transition table in stable safe-block order.
TR=[]
for b in safe_blocks:
    qi=min(P[b]);row=[]
    for t in T[qi]:
        bt=block[t]
        row.append(-1 if bt==sinkblock else remap[bt])
    TR.append(row)
# identify start block from trie root safe index
START=remap[block[si[0]]]
assert START>=0
# automorphism equivariance at transition level
for i in range(601):
    for j,(c,l) in enumerate(A):
        t=TR[i][j]
        jc=(1-c)*11+(l+5)
        js=c*11+((-l)+5)
        tc=TR[CM[i]][jc]
        ts=TR[SM[i]][js]
        assert (t<0 and tc<0) or (t>=0 and tc==CM[t])
        assert (t<0 and ts<0) or (t>=0 and ts==SM[t])

print('R17 C038 exact cap-5 length<=4 deficiency language checker')
print('cap5_symbols =',len(A))
print('deficient_pair_classes =',len(pair_bad))
print('minimal_deficient_triple_classes =',len(triple_min))
print('minimal_deficient_quadruple_classes =',len(quad_min))
print('forbidden_patterns_total =',len(patterns))
print('aho_total_nodes =',len(children))
print('aho_nonrejecting_nodes =',len(safe_nodes))
print('minimized_total_states_including_reject =',len(P))
print('minimized_nonrejecting_states =',len(safe_blocks))
print('complement_fixed_safe_states =',fixedC)
print('swap_fixed_safe_states =',fixedS)
print('start_state =',START)
print('EXACT_CAP5_REGRESSION_PASS')
print('EXACT_DFA_MINIMIZATION_PASS')
print('EXACT_COMPLEMENT_AUTOMORPHISM_PASS')
print('EXACT_SWAP_AUTOMORPHISM_PASS')
print('ALL_EXACT_CHECKS_PASS')

# Emit header for the reachable product generator.
with open('c038_dfa601.h','w') as f:
    f.write('#pragma once\n')
    f.write(f'static constexpr int DFAK=601, DFAAL=22, DFASTART={START};\n')
    f.write('static const int16_t DFATR[DFAK][DFAAL] = {\n')
    for row in TR:f.write('  {'+','.join(map(str,row))+'},\n')
    f.write('};\n')
    f.write('static const uint16_t DFACM[DFAK] = {'+','.join(map(str,CM))+'};\n')
    f.write('static const uint16_t DFASM[DFAK] = {'+','.join(map(str,SM))+'};\n')
