from fractions import Fraction
import random


def mul(a, b): return tuple(x*y for x, y in zip(a, b))
def q(p, x, u, v): return p[x]*p[x^u]*p[x^v]*p[x^u^v]
def P(p, u, v): return Fraction(sum(q(p, x, u, v) == -1 for x in range(len(p))), len(p))
def phase(mask, d): return tuple(-1 if (mask >> x) & 1 else 1 for x in range(1 << d))

def pair(H, h0, h1, u, v):
    g = mul(h0, h1)
    return P(H,u,v)+P(mul(H,g),u,v)-P(mul(H,h0),u,v)-P(mul(H,h1),u,v)

def triple(H, f, h0, h1, u, v): return pair(H,h0,h1,u,v)-pair(mul(H,f),h0,h1,u,v)

def exact_rhs(H, f, h0, h1, u, v):
    z = sum(q(H,x,u,v)*(1-q(h0,x,u,v))*(1-q(h1,x,u,v))*(1-q(f,x,u,v)) for x in range(len(H)))
    return -Fraction(z, 2*len(H))

def slices(n_old, c):
    out=[]; d=n_old+1
    for b in (0,1):
        p=[]
        for x in range(1<<d):
            ina=all(((x>>j)&1)==0 for j in range(c))
            p.append(-1 if ina and ((x>>n_old)&1)==b else 1)
        out.append(tuple(p))
    return tuple(out)

def parent(n_old,c):
    return tuple(-1 if all(((x>>j)&1)==0 for j in range(c)) else 1 for x in range(1<<n_old))
def J(g):
    n=(len(g)).bit_length()-1; ans=Fraction(0)
    for i in range(n):
        p=Fraction(sum(g[x]!=g[x^(1<<i)] for x in range(1<<n)),1<<n)
        ans += min(p,1-p)
    return ans

def nw(mask,d,p):
    k=mask.bit_count(); return p**k*(1-p)**(d-k)

random.seed(20260921)
h0,h1=slices(2,2); d=3
ident=support=0
for _ in range(2500):
    H=phase(random.randrange(256),d); f=phase(random.randrange(256),d)
    u=random.randrange(8); v=random.randrange(8)
    assert triple(H,f,h0,h1,u,v)==exact_rhs(H,f,h0,h1,u,v); ident+=1
    tp=Fraction(sum(q(h0,x,u,v)==q(h1,x,u,v)==q(f,x,u,v)==-1 for x in range(8)),8)
    pp=Fraction(sum(q(h0,x,u,v)==q(h1,x,u,v)==-1 for x in range(8)),8)
    assert abs(triple(H,f,h0,h1,u,v)) <= 4*tp <= 4*pp; support+=1

assert J(parent(2,2))==1
ps=[Fraction(1,8),Fraction(1,4),Fraction(3,8),Fraction(1,2)]
noise=0; worst=Fraction(0)
for _ in range(64):
    H=phase(random.randrange(256),d); f=phase(random.randrange(256),d)
    for s in ps:
        for t in ps:
            lhs=sum(nw(u,d,s)*nw(v,d,t)*abs(triple(H,f,h0,h1,u,v)) for u in range(8) for v in range(8))
            rhs=8*s*t*(1-s*t)
            assert lhs<=rhs
            worst=max(worst,lhs/rhs); noise+=1

aff=0
for lin in range(4):
    for c in (0,1):
        f=tuple(-1 if (((lin&(x&3)).bit_count()&1)^c) else 1 for x in range(8))
        for Hm in range(64):
            H=phase(Hm,d)
            for u,v in ((1,2),(1,4),(3,5),(7,6)):
                assert triple(H,f,h0,h1,u,v)==0; aff+=1

c10,c11=slices(1,1)
obs=abs(triple((1,1,1,1),c10,c10,c11,1,2))
assert obs==4 and J(parent(1,1))==0
assert 8*(Fraction(1,4)-Fraction(1,64))==Fraction(15,8)

print('PASS')
print('identity_checks',ident)
print('support_checks',support)
print('noise_checks',noise)
print('worst_noise_ratio',f'{worst.numerator}/{worst.denominator}',float(worst))
print('affine_zero_checks',aff)
print('integrated_envelope_constant 15/8 1.875')
print('generic_c1_obstruction_abs 4 parent_J 0')
