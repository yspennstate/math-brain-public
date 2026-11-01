from fractions import Fraction
import itertools

EPS = Fraction(56721646463783, 2500000000000000)
BIAS = [Fraction(1,3), Fraction(1,2), Fraction(2,3)]
MUX_BIAS = [Fraction(1,4), Fraction(1,3), Fraction(1,2), Fraction(2,3), Fraction(3,4)]

def eta(p):
    m = 1 - 2*p
    V = 4*p*(1-p)
    return 1 - m**4 - EPS*V**3

def phi(p):
    return p*(1-p)

def weight(x, ps):
    w = Fraction(1)
    for b,p in zip(x,ps):
        w *= p if b else 1-p
    return w

def outprob(f, ps):
    return sum((weight(x,ps) for x in itertools.product([0,1], repeat=len(ps)) if f[x]), Fraction(0))

def influence(f, ps, i):
    n=len(ps)
    rem=[j for j in range(n) if j != i]
    d=Fraction(0)
    for ys in itertools.product([0,1], repeat=n-1):
        x0=[0]*n; x1=[0]*n; w=Fraction(1)
        for j,y in zip(rem,ys):
            x0[j]=x1[j]=y
            w *= ps[j] if y else 1-ps[j]
        x0[i]=0; x1[i]=1
        if f[tuple(x0)] != f[tuple(x1)]:
            d += w
    V=4*ps[i]*(1-ps[i])
    return V*d, d

def E(f, ps, fun):
    q=outprob(f,ps)
    ans=-fun(q)
    for i,p in enumerate(ps):
        It,_=influence(f,ps,i)
        V=4*p*(1-p)
        ans += It*fun(p)/V
    return ans

def cofactor(f,n,i,b):
    rem=[j for j in range(n) if j != i]
    g={}
    for ys in itertools.product([0,1], repeat=n-1):
        x=[0]*n
        for j,y in zip(rem,ys): x[j]=y
        x[i]=b
        g[ys]=f[tuple(x)]
    return g,rem

count=0
for n in (1,2,3):
    xs=list(itertools.product([0,1], repeat=n))
    for mask in range(1 << (2**n)):
        f={x:(mask>>k)&1 for k,x in enumerate(xs)}
        for ps in itertools.product(BIAS, repeat=n):
            for i in range(n):
                s=ps[i]
                g0,rem=cofactor(f,n,i,0); g1,_=cofactor(f,n,i,1)
                psr=tuple(ps[j] for j in rem)
                q=outprob(f,ps)
                q0=outprob(g0,psr) if n>1 else Fraction(g0[()])
                q1=outprob(g1,psr) if n>1 else Fraction(g1[()])
                E0=E(g0,psr,eta) if n>1 else Fraction(0)
                E1=E(g1,psr,eta) if n>1 else Fraction(0)
                _,d=influence(f,ps,i)
                L=(1-s)*eta(q0)+s*eta(q1)-eta(q)+d*eta(s)
                assert E(f,ps,eta) == (1-s)*E0+s*E1+L
                count += 1

mux={}
for x in itertools.product([0,1], repeat=3):
    A,D0,D1=x
    mux[x]=D1 if A else D0
mux_count=0
for t,q0,q1 in itertools.product(MUX_BIAS, repeat=3):
    ps=(t,q0,q1)
    V0=4*q0*(1-q0); V1=4*q1*(1-q1)
    W=E(mux,ps,phi)
    assert W == t*(1-t)*(V0+V1)/4
    for i,Vj in ((1,V0),(2,V1)):
        s=ps[i]
        g0,rem=cofactor(mux,3,i,0); g1,_=cofactor(mux,3,i,1)
        psr=tuple(ps[j] for j in rem)
        q=outprob(mux,ps); qa=outprob(g0,psr); qb=outprob(g1,psr)
        _,d=influence(mux,ps,i)
        L=(1-s)*phi(qa)+s*phi(qb)-phi(q)+d*phi(s)
        omega=t*(1-t)*Vj/4
        assert L == omega
        assert W == L + (1-s)*E(g0,psr,phi) + s*E(g1,psr,phi)
        mux_count += 1

print('PASS')
print('exact_eta_cocycle_cases', count)
print('exact_mux_quadratic_bank_cases', mux_count)
