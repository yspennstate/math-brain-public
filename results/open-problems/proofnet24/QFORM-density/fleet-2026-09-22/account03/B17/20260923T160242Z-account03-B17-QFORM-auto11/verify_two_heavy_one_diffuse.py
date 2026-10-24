#!/usr/bin/env python3
from fractions import Fraction as F
from math import comb, sqrt

def add(a,b):
    n=max(len(a),len(b)); c=[F(0)]*n
    for i,x in enumerate(a): c[i]+=x
    for i,x in enumerate(b): c[i]+=x
    while len(c)>1 and c[-1]==0: c.pop()
    return c

def scale(a,s): return [x*s for x in a]

def mul(a,b):
    c=[F(0)]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b): c[i+j]+=x*y
    return c

def power(a,n):
    r=[F(1)]
    for _ in range(n): r=mul(r,a)
    return r

def affine(a,L,R):
    out=[F(0)]; base=[L,R-L]
    for j,aj in enumerate(a): out=add(out,scale(power(base,j),aj))
    return out

def bernstein(a,L,R):
    pw=affine(a,L,R); n=len(a)-1
    pw += [F(0)]*(n+1-len(pw))
    return [sum(pw[j]*F(comb(k,j),comb(n,j)) for j in range(k+1)) for k in range(n+1)]

def cert(a,L,R,N):
    vals=[]
    for i in range(N):
        l=L+(R-L)*F(i,N); r=L+(R-L)*F(i+1,N)
        b=bernstein(a,l,r)
        assert all(x>0 for x in b), (i,min(b))
        vals += b
    return min(vals)

P=[F(197,200),F(-9,50),F(533,25),F(-141),F(330),F(-3353,10),F(2517,20)]
P2=mul(P,P)
Pmhalf=P[:]; Pmhalf[0]-=F(1,2)
Q1=add(scale(mul([F(1),F(-1)],P2),F(157,50)),[F(-3)])
Q2=add(mul([F(0),F(4)],P2),[F(-1)])

mP=cert(Pmhalf,F(0),F(1),4)
mQ1=cert(Q1,F(0),F(26,125),4)
mQ2=cert(Q2,F(207,1000),F(1),4)

def moment(k):
    out=[F(0)]
    for j in range(k+1):
        qpow=[F(0)]*(k-j)+[F(1)]
        om=power([F(1),F(-1)],j)
        coeff=F(comb(2*k,2*j)*comb(2*j,j),(4**j)*(2**k))
        out=add(out,scale(mul(qpow,om),coeff))
    return out

A=[F(0)]
for k,ck in enumerate(P): A=add(A,scale(moment(k),ck))
expected=[F(6131407,6553600),F(1574823,3276800),F(-64418143,6553600),F(3233529,65536),F(-26538519,262144),F(60340859,655360),F(-40697373,1310720)]
assert A==expected
Gap=scale(A,F(-1)); Gap[0]+=F(21,22)
mGap=cert(Gap,F(0),F(1),8)
Tcert=F(21,22)-mGap
assert Tcert==F(1595634387,1677721600)
assert Tcert < F(21,22)

M=[[F(1,3),F(-2,3),F(-2,3)],[F(-2,3),F(1,3),F(-2,3)],[F(-2,3),F(-2,3),F(1,3)]]
M2=[[sum(M[i][k]*M[k][j] for k in range(3)) for j in range(3)] for i in range(3)]
assert M2==[[F(int(i==j)) for j in range(3)] for i in range(3)]
assert sum(M[i][i] for i in range(3))==F(1)

print('PASS QFORM_TWO_HEAVY_ONE_DIFFUSE_CONE')
print('min Bernstein P-1/2 =',mP)
print('min Bernstein Q1 =',mQ1)
print('min Bernstein Q2 =',mQ2)
print('min Bernstein 21/22-E[P(U)] =',mGap)
print('Tcert =',Tcert,'=',float(Tcert))
print('certified density bound using pi<22/7 =',float(F(22,7)*Tcert)*sqrt(2))
print('3sqrt2 =',3*sqrt(2))
