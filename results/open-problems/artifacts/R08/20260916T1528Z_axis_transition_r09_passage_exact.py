#!/usr/bin/env python3
from fractions import Fraction
from itertools import product

DIRS=((1,0),(-1,0),(0,1),(0,-1))
K=5
Z=Fraction(22,7)
LAMBDA=Fraction(2407,500)
MARKOV=Fraction(38141,10000)
C=Fraction(3753,12500)
V=[7645631628, 6388469364, 6388469364, 7628360188, 1222082844, 6390397369, 7628360188, 1222082844, 6390397369, 7644566212, 6389732016, 6307410461, 1174049816, 5509544874, 7624786329, 1273856728, 6394437402, 7644566212, 6307410461, 6389732016, 100000000, 1222082844, 1174049816, 1273856728, 100000000, 5509544874, 1222082844, 1273856728, 1174049816, 100000000, 6307410461, 6394437402, 5509544874, 6390397369, 6388469364, 6388469364, 6389732016, 7628360188, 1222082844, 6390397369, 7628360188, 1222082844, 6390397369, 7644566212, 6389732016, 6307410461, 1174049816, 5509544874, 7624786329, 1273856728, 6394437402, 7644566212, 6307410461, 6389732016, 100000000, 1222082844, 1174049816, 1273856728, 100000000, 5509544874, 1222082844, 1273856728, 1174049816, 100000000, 6307410461, 6394437402, 5509544874, 6390397369, 6388469364, 7624786329, 5509544874, 6307410461, 6389732016, 6388469364, 7624786329, 5509544874, 6307410461, 6389732016, 7624786329, 1174049816, 1273856728, 6394437402, 6389732016, 7624786329, 1174049816, 1273856728, 6394437402, 6389732016, 1174049816, 100000000, 1174049816, 5509544874, 6307410461, 1174049816, 100000000, 1174049816, 5509544874, 6307410461, 1273856728, 1174049816, 100000000, 1222082844, 6394437402, 1273856728, 1174049816, 100000000, 1222082844, 6394437402, 5509544874, 100000000, 1273856728, 1222082844, 6390397369, 5509544874, 100000000, 1273856728, 1222082844, 6390397369, 6307410461, 1273856728, 5509544874, 1174049816, 6389732016, 6307410461, 1273856728, 5509544874, 1174049816, 6389732016, 6389732016, 1174049816, 5509544874, 1273856728, 6307410461, 6389732016, 1174049816, 5509544874, 1273856728, 6307410461, 6394437402, 1222082844, 1273856728, 100000000, 1174049816, 6394437402, 1222082844, 1273856728, 100000000, 1174049816, 6390397369, 1222082844, 1273856728, 100000000, 5509544874, 6390397369, 1222082844, 1273856728, 100000000, 5509544874, 1174049816, 6307410461, 5509544874, 7624786329, 6388469364, 1174049816, 6307410461, 5509544874, 7624786329, 6388469364, 1273856728, 6394437402, 6307410461, 6389732016, 7624786329, 1273856728, 6394437402, 6307410461, 6389732016, 7624786329, 100000000, 1174049816, 1222082844, 6390397369, 7628360188, 100000000, 1174049816, 1222082844, 6390397369, 7628360188, 1222082844, 5509544874, 100000000, 1273856728, 7624786329, 1222082844, 5509544874, 100000000, 1273856728, 7624786329, 1273856728, 6307410461, 6394437402, 1174049816, 7624786329, 1273856728, 6307410461, 6394437402, 1174049816, 7624786329, 5509544874, 6307410461, 6394437402, 7624786329, 6388469364, 5509544874, 6307410461, 6394437402, 7624786329, 6388469364, 6307410461, 6389732016, 1174049816, 1273856728, 7628360188, 6307410461, 6389732016, 1174049816, 1273856728, 7628360188, 6394437402, 6389732016, 1273856728, 1174049816, 7644566212, 6394437402, 6389732016, 1273856728, 1174049816, 7644566212, 6390397369, 1222082844, 100000000, 1174049816, 7628360188, 6390397369, 1222082844, 100000000, 1174049816, 7628360188, 6389732016, 6307410461, 5509544874, 7624786329, 6388469364, 6389732016, 6307410461, 5509544874, 7624786329, 6388469364, 7624786329, 5509544874, 1273856728, 6394437402, 7628360188, 7624786329, 5509544874, 1273856728, 6394437402, 7628360188, 1174049816, 100000000, 1222082844, 6390397369, 7644566212, 1174049816, 100000000, 1222082844, 6390397369, 7644566212, 1273856728, 1174049816, 100000000, 1222082844, 6394437402, 1273856728, 1174049816, 100000000, 1222082844, 6394437402, 5509544874, 1273856728, 100000000, 1222082844, 6390397369, 5509544874, 1273856728, 100000000, 1222082844, 6390397369, 6307410461, 5509544874, 1222082844, 1273856728, 6389732016, 6307410461, 5509544874, 1222082844, 1273856728, 6389732016, 100000000, 1174049816, 1273856728, 5509544874, 6389732016, 100000000, 1174049816, 1273856728, 5509544874, 6389732016]

def build_states():
    states=[]
    for ds in product(range(4), repeat=K):
        x=y=0
        pts={(0,0)}
        ok=True
        for d in ds:
            dx,dy=DIRS[d]
            x+=dx; y+=dy
            if (x,y) in pts:
                ok=False; break
            pts.add((x,y))
        if ok:
            states.append(ds)
    idx={s:i for i,s in enumerate(states)}
    trans=[]
    for s in states:
        x=y=0
        pts={(0,0)}
        for d in s:
            dx,dy=DIRS[d]; x+=dx; y+=dy
            pts.add((x,y))
        row=[]
        for d in range(4):
            dx,dy=DIRS[d]
            nx,ny=x+dx,y+dy
            if (nx,ny) in pts:
                continue
            ns=s[1:]+(d,)
            if ns in idx:
                row.append((idx[ns],d))
        trans.append(row)
    return states,trans

states,trans=build_states()
assert len(states)==284
assert sum(len(r) for r in trans)==780
assert len(V)==284 and min(V)>0

max_ratio=Fraction(0,1)
max_i=-1
for i,row in enumerate(trans):
    mv=Fraction(0,1)
    for j,d in row:
        dx=DIRS[d][0]
        w = Z if dx==1 else (1/Z if dx==-1 else Fraction(1,1))
        mv += w*V[j]
    ratio=mv/V[i]
    if ratio>max_ratio:
        max_ratio=ratio; max_i=i
    assert mv <= LAMBDA*V[i]

X=MARKOV*C
N=7
term=Fraction(1,1)
exp_upper=term
for j in range(1,N+1):
    term = term*X/j
    exp_upper += term
next_term=term*X/(N+1)
qtail=X/(N+2)
assert qtail<1
exp_upper += next_term/(1-qtail)

RHO=LAMBDA/(1+MARKOV)
RHS=Z*(1+MARKOV)/LAMBDA
assert RHO<1
assert exp_upper < RHS
BASE_UPPER=(exp_upper/Z)*RHO
assert BASE_UPPER<1

def is_monotone(mask,n):
    vals=[(mask>>x)&1 for x in range(1<<n)]
    for x in range(1<<n):
        if not vals[x]:
            continue
        for i in range(n):
            if ((x>>i)&1)==0:
                y=x|(1<<i)
                if not vals[y]:
                    return False
    return True

def prob_event(mask,n,s):
    out=Fraction(0,1)
    for x in range(1<<n):
        if ((mask>>x)&1)==0:
            continue
        k=x.bit_count()
        out += s**k * (1-s)**(n-k)
    return out

def pivotal_prob(mask,n,i,s):
    out=Fraction(0,1)
    for x in range(1<<n):
        if (x>>i)&1:
            continue
        y=x|(1<<i)
        if ((mask>>x)&1)==0 and ((mask>>y)&1)==1:
            k=x.bit_count()
            out += s**k * (1-s)**((n-1)-k)
    return out

def derivative_prob(mask,n,s):
    out=Fraction(0,1)
    for x in range(1<<n):
        if ((mask>>x)&1)==0:
            continue
        k=x.bit_count()
        if k:
            out += k*s**(k-1)*(1-s)**(n-k)
        if n-k:
            out -= (n-k)*s**k*(1-s)**(n-k-1)
    return out

SVALS=(Fraction(1,5),Fraction(1,3),Fraction(2,5),Fraction(3,5))
counts={}
checks=0
for n in range(1,5):
    cnt=0
    for mask in range(1<<(1<<n)):
        if not is_monotone(mask,n):
            continue
        cnt+=1
        for s in SVALS:
            a=prob_event(mask,n,s)
            Is=[pivotal_prob(mask,n,i,s) for i in range(n)]
            lhs=s*(1-s)*sum(I*I for I in Is)
            rhs=a*(1-a)
            assert lhs<=rhs
            assert derivative_prob(mask,n,s)==sum(Is)
            checks+=2
    counts[n]=cnt

assert counts=={1:3,2:6,3:20,4:168}

print("PASS")
print("R08-L003 exact transition certificate")
print("states",len(states),"transitions",sum(len(r) for r in trans))
print("z",Z,"Lambda",LAMBDA,"max_collatz_ratio",max_ratio,"at_state",max_i)
print("lambda_markov",MARKOV,"c_axis",C)
print("rho",RHO)
print("exp_upper_N7",exp_upper)
print("rhs_exp_threshold",RHS)
print("base_upper",BASE_UPPER)
print("R09-PASSAGE audit monotone_counts",counts)
print("R09-PASSAGE exact inequalities checked",checks)
