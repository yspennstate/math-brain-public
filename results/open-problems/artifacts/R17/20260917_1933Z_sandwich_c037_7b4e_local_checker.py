#!/usr/bin/env python3
from itertools import product
from collections import deque

def bar(c): return 1-c
def mp(c,l):
    if l>=0: return (str(bar(c))*l+str(c), str(c))
    return (str(c), str(bar(c))*(-l)+str(c))
def cat(l):
    if l<=-2:return '-H'
    if l==-1:return '-1'
    if l==0:return '0'
    if l==1:return '+1'
    return '+H'
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
    a,b=pair(w);return lcs(a,b)>len(w)

F=0
for c,s,a,b,d in product((0,1),(-1,1),range(2,8),range(-7,8),range(2,8)):
    w=((c,s*a),(bar(c),b),(c,-s*d))
    aa,bb=pair(w);L=lcs(aa,bb)
    assert L>=4,(w,aa,bb,L)
    assert not deficient(w[:2]) and not deficient(w[1:]),w
    F+=1
assert F==2160

P=0
for c,s,a,d in product((0,1),(-1,1),range(2,8),range(2,8)):
    w=((c,s*a),(c,-s*d))
    assert deficient(w),w
    P+=1
assert P==144

cats=['-H','-1','0','+1','+H']
symbols=[(c,t) for c in (0,1) for t in cats]
si={s:i for i,s in enumerate(symbols)}
forbidden=[]
for c in (0,1):
    forbidden += [((c,'+H'),(c,'-H')),((c,'-H'),(c,'+H'))]
    for a,b in [('+H','-H'),('-H','+H')]:
        for mid in cats:
            forbidden.append(((c,a),(bar(c),mid),(c,b)))
assert len(forbidden)==24

tr=[{}];fail=[0];bad=[False]
for pat in forbidden:
    q=0
    for x in pat:
        j=si[x]
        if j not in tr[q]:
            tr[q][j]=len(tr);tr.append({});fail.append(0);bad.append(False)
        q=tr[q][j]
    bad[q]=True
Q=deque()
for j in range(10):
    if j in tr[0]:Q.append(tr[0][j])
    else:tr[0][j]=0
while Q:
    r=Q.popleft();bad[r]|=bad[fail[r]]
    for j in range(10):
        if j in tr[r]:
            q=tr[r][j];Q.append(q);f=fail[r]
            while j not in tr[f]:f=fail[f]
            fail[q]=tr[f][j]
        else:tr[r][j]=tr[fail[r]][j]
non=[q for q in range(len(tr)) if not bad[q]];ix={q:i for i,q in enumerate(non)};R=len(non)
T=[[R]*10 for _ in range(R+1)]
for q in non:
    for j in range(10):
        z=tr[q][j];T[ix[q]][j]=R if bad[z] else ix[z]
T[R]=[R]*10
parts=[set(range(R)),{R}]
while True:
    cl={q:k for k,p in enumerate(parts) for q in p};np=[]
    for p in parts:
        buckets={}
        for q in p:
            sig=tuple(cl[T[q][j]] for j in range(10))
            buckets.setdefault(sig,set()).add(q)
        np.extend(buckets.values())
    if len(np)==len(parts):break
    parts=np
cl={q:k for k,p in enumerate(parts) for q in p};reject=cl[R];start=cl[ix[0]]
TT=[[cl[T[next(iter(parts[k]))][j]] for j in range(10)] for k in range(len(parts))]
order=[start]+[k for k in range(len(parts)) if k not in (start,reject)]+[reject]
ren={q:i for i,q in enumerate(order)};M=[[ren[TT[q][j]] for j in range(10)] for q in order];RJ=len(M)-1
assert RJ==17

EXPECTED=[
[4,0,0,0,1,16,0,0,0,14],[-1,0,0,0,1,6,2,2,2,8],[-1,0,0,0,1,16,0,0,0,14],[4,0,0,0,-1,16,0,0,0,14],[4,0,0,0,-1,9,3,3,3,11],[-1,0,0,0,1,6,2,2,2,-1],[-1,15,15,15,5,16,0,0,0,-1],[-1,0,0,0,1,-1,2,2,2,8],[-1,13,13,13,7,-1,0,0,0,14],[10,15,15,15,-1,16,0,0,0,-1],[4,0,0,0,-1,9,3,3,3,-1],[12,13,13,13,-1,-1,0,0,0,14],[4,0,0,0,-1,-1,3,3,3,11],[4,0,0,0,1,-1,0,0,0,14],[12,13,13,13,7,-1,0,0,0,14],[4,0,0,0,1,16,0,0,0,-1],[10,15,15,15,5,16,0,0,0,-1]]
MC=[[(-1 if x==RJ else x) for x in row] for row in M[:-1]]
assert MC==EXPECTED,(MC,EXPECTED)

def comp_symbol(x):return (bar(x[0]),x[1])
CP=[None]*len(M);CP[0]=0;Q=deque([0])
while Q:
    q=Q.popleft()
    for j,x in enumerate(symbols):
        a=M[q][j];cj=si[comp_symbol(x)];b=M[CP[q]][cj]
        if CP[a] is None:CP[a]=b;Q.append(a)
        else:assert CP[a]==b
assert CP==[0,14,13,15,16,11,12,8,7,10,9,5,6,2,1,3,4,17]
assert all(CP[CP[q]]==q for q in range(len(M)))

def direct(seq):
    return not any(any(tuple(seq[i:i+len(p)])==p for i in range(len(seq)-len(p)+1)) for p in forbidden)
def dfa(seq):
    q=0
    for x in seq:
        q=M[q][si[x]]
        if q==RJ:return False
    return True
checked=0
for n in range(1,6):
    for seq in product(symbols,repeat=n):
        assert direct(seq)==dfa(seq),seq
        checked+=1
assert checked==111110

print('R17 C037 exact local-family and minimized-DFA checker')
print('outer_hook_sandwich_representatives_checked =',F)
print('adjacent_long_hook_representatives_checked =',P)
print('forbidden_coarse_words =',len(forbidden))
print('dfa_nonrejecting_states =',RJ)
print('dfa_language_sequences_checked =',checked)
print('complement_automorphism =',CP)
print('EXACT_LOCAL_LCS_FAMILY_REGRESSION_PASS')
print('EXACT_MINIMIZED_DFA_TABLE_PASS')
print('EXACT_COMPLEMENT_AUTOMORPHISM_PASS')
print('ALL_EXACT_CHECKS_PASS')
