#!/usr/bin/env python3
from collections import defaultdict

MAX_TOTAL = 18

def lcs(a,b):
    d=[0]*(len(b)+1)
    for x in a:
        prev=0
        for j,y in enumerate(b,1):
            old=d[j]
            if x==y:
                d[j]=prev+1
            elif d[j-1]>d[j]:
                d[j]=d[j-1]
            prev=old
    return d[-1]

def minimal_match_generic(a,b):
    return bool(a and b and a[-1]==b[-1] and lcs(a,b)==1
                and lcs(a[:-1],b)==0 and lcs(a,b[:-1])==0)

def hook_minimal(a,b):
    if not a or not b or a[-1]!=b[-1]:
        return False
    c=a[-1]
    oc='1' if c=='0' else '0'
    return (a==c and b[:-1]==oc*(len(b)-1)) or \
           (b==c and a[:-1]==oc*(len(a)-1))

# Small independent validation of the binary-hook lemma from the source definition.
for total in range(2,8):
    for n in range(1,total):
        m=total-n
        for x in range(1<<n):
            a=''.join('1' if (x>>i)&1 else '0' for i in range(n))
            for y in range(1<<m):
                b=''.join('1' if (y>>i)&1 else '0' for i in range(m))
                assert minimal_match_generic(a,b)==hook_minimal(a,b)

def string_from_mask(mask,n):
    return ''.join('1' if (mask>>i)&1 else '0' for i in range(n-1))+'0'

def next_cuts(X,Y,i,j):
    if i==len(X) or j==len(Y): return ()
    if X[i]==Y[j]:
        return ((i+1,j+1),)
    out=[]
    jj=Y.find(X[i],j)
    if jj!=-1: out.append((i+1,jj+1))
    ii=X.find(Y[j],i)
    if ii!=-1: out.append((ii+1,j+1))
    return tuple(out)

def all_paths(X,Y):
    n,m=len(X),len(Y)
    out=[]
    stack=[(0,0,())]
    while stack:
        i,j,p=stack.pop()
        if i==n and j==m:
            out.append(p); continue
        for q in next_cuts(X,Y,i,j):
            stack.append((q[0],q[1],p+(q,)))
    return out

def skey(p):
    return tuple(i+j for i,j in reversed(p))
def rkey(p):
    return tuple((i+j,i-j) for i,j in reversed(p))

pairs=0
scalar_collision_groups=0
saturated_collisions=0
max_def=0
first=None
counts={}
for total in range(2,MAX_TOTAL+1):
    ct=0
    for n in range(1,total):
        m=total-n
        if n>m: continue
        for xm in range(1<<(n-1)):
            X=string_from_mask(xm,n)
            for ym in range(1<<(m-1)):
                Y=string_from_mask(ym,m)
                pairs+=1
                ps=all_paths(X,Y)
                # refined coordinate key must distinguish distinct cut paths
                keys=[rkey(p) for p in ps]
                assert len(keys)==len(set(keys))
                if len(ps)<2: continue
                ell=lcs(X,Y)
                G=defaultdict(list)
                for p in ps:
                    G[(len(p),skey(p))].append(p)
                for (r,k),grp in G.items():
                    if len(grp)>=2:
                        ct+=1; scalar_collision_groups+=1
                        deficiency=ell-r
                        assert deficiency>=1
                        max_def=max(max_def,deficiency)
                        if deficiency==0: saturated_collisions+=1
                        if first is None:
                            first=(total,X,Y,r,ell,k,grp)
    counts[total]=ct
    print(f"total={total} scalar_collision_groups={ct}")

assert saturated_collisions==0
assert first is not None
total,X,Y,r,ell,k,grp=first
assert total==13 and (X,Y)==('110110','0010110') and r==4 and ell==5
assert k==(13,10,7,4)
assert rkey(grp[0])!=rkey(grp[1])
print("MAX_TOTAL=",MAX_TOTAL,sep="")
print("PAIRS_CHECKED=",pairs,sep="")
print("SCALAR_COLLISION_GROUPS=",scalar_collision_groups,sep="")
print("SATURATED_SCALAR_COLLISION_GROUPS=0")
print("MAX_COLLISION_DEFICIENCY=",max_def,sep="")
print("FIRST_SCALAR_COLLISION_TOTAL=13")
print("FIRST_X=110110")
print("FIRST_Y=0010110")
print("FIRST_ORDER=4")
print("FIRST_LCS=5")
print("FIRST_SCALAR_KEY=13,10,7,4")
print("FIRST_REFINED_KEY_1=",rkey(grp[0]),sep="")
print("FIRST_REFINED_KEY_2=",rkey(grp[1]),sep="")
print("BINARY_HOOK_DEFINITION_CHECK_TOTAL_LE_7=PASS")
print("REFINED_KEY_INJECTIVITY_TOTAL_LE_18=PASS")
print("NO_SATURATED_SCALAR_KEY_COLLISION_TOTAL_LE_18=PASS")
print("ALL_EXACT_CHECKS_PASS")
