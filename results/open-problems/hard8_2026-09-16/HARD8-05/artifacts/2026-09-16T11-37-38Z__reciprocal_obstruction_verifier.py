#!/usr/bin/env python3

def factor(n):
    out=[]
    d=2
    while d*d<=n:
        while n%d==0:
            out.append(d); n//=d
        d=3 if d==2 else d+2
    if n>1: out.append(n)
    return out

def divisors_from_factors(fs):
    ds=[1]
    for p in sorted(set(fs)):
        e=fs.count(p)
        ds=[d*p**k for d in ds for k in range(e+1)]
    return sorted(ds)

n=1201
assert factor(n)==[1201]
assert n%840==361
N1=2*n+5
N2=5*n+2
assert N1==2407 and factor(N1)==[29,83]
assert N2==6007 and factor(N2)==[6007]
D1=divisors_from_factors(factor(N1))
D2=divisors_from_factors(factor(N2))
assert D1==[1,29,83,2407]
assert [d%40 for d in D1]==[1,29,3,7]
assert [d%40 for d in D2]==[1,7]
assert all(d%40!=39 for d in D1+D2)
K3={1,3,7,9,21,23,27,29}
K5={1,7,9,11,13,19,23,37}
assert all(p%40 in K3 for p in factor(N1))
assert all(p%40 in K3 for p in factor(N2))
assert all(p%40 in K5 for p in factor(N2))
a,u=4,1
N=a*n+u
assert N==4805 and factor(N)==[5,31,31]
s=31
assert N%s==0 and s%(4*a*u)==4*a*u-1
q=N//s
t=(s+1)//(4*a*u)
x=u*q*t
y=a*n*q*t
z=a*n*u*t
assert (q,t,x,y,z)==(155,2,310,1489240,9608)
assert 4*x*y*z==n*(y*z+x*z+x*y)
print('n',n,'mod840',n%840)
print('N1 divisors/residues',[(d,d%40) for d in D1])
print('N2 divisors/residues',[(d,d%40) for d in D2])
print('rescue',{'a':a,'u':u,'s':s,'q':q,'t':t,'x':x,'y':y,'z':z})
print('ALL_CHECKS_PASSED')
