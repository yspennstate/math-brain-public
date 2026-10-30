from fractions import Fraction
from math import comb, factorial
import random


def p(m,a):
    return Fraction(comb(m,a), 2**m) if 0 <= a <= m else Fraction(0)

def nabla(m,a,r):
    return sum(Fraction(((-1)**j)*comb(r,j))*p(m,a-j) for j in range(r+1))

def d(N,k,a):
    assert k%2==0 and 2<=k<=N
    return Fraction(1,2**(k-1))*nabla(N-k,a,k-1)

def poly_mul(a,b):
    out=[Fraction(0)]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b): out[i+j]+=x*y
    return out

def pow_poly(base,e):
    out=[Fraction(1)]
    for _ in range(e): out=poly_mul(out,base)
    return out

def D_coeffs(N,k):
    a=poly_mul(pow_poly([Fraction(1),Fraction(-1)],k-1),pow_poly([Fraction(1),Fraction(1)],N-k))
    return [Fraction(x,2**(N-1)) for x in a]

def beta_half_over_pi(m,N):
    b=N-m-1
    return Fraction(factorial(2*m)*factorial(2*b), (4**(N-1))*factorial(m)*factorial(b)*factorial(N-1))

def coeff_l2_beta(N,cs):
    s=Fraction(0)
    for k,ck in cs.items():
        for l,cl in cs.items():
            m=(k+l-2)//2
            sign = 1 if (((k-l)//2) % 2 == 0) else -1
            s += ck*cl*sign*beta_half_over_pi(m,N)
    return s

def aggregate_b(N,cs):
    out=[Fraction(0)]*N
    for k,c in cs.items():
        Dc=D_coeffs(N,k)
        for a in range(N): out[a]+=c*Dc[a]
    return out

def weighted_I(N,b):
    half=sum(Fraction(4*(N-2*a-1),N*N)*b[a]*b[a] for a in range(N//2))
    allform=Fraction(2,N*N)*sum(abs(N-1-2*a)*b[a]*b[a] for a in range(N))
    assert half==allform
    return half

def L_vec(N,b):
    return [Fraction(N-1-2*a)*b[a] for a in range(N)]

def lincomb_D(N,coefs):
    out=[Fraction(0)]*N
    for k,c in coefs.items():
        arr=[Fraction(x,2**(N-1)) for x in poly_mul(pow_poly([Fraction(1),Fraction(-1)],k-1),pow_poly([Fraction(1),Fraction(1)],N-k))]
        for a in range(N): out[a]+=c*arr[a]
    return out

def test():
    random.seed(20260921)
    counts={"D":0,"gen":0,"anti":0,"brown":0,"beta":0,"L":0,"L2":0,"parent":0}
    for N in [8,16,32]:
        ev=list(range(2,N+1,2))
        for k in ev:
            Dc=D_coeffs(N,k)
            for a in range(N):
                assert d(N,k,a)==Dc[a]
                counts['D']+=1
            for a in range(N):
                assert Dc[N-1-a]==-Dc[a]
                counts['anti']+=1
        for rep in range(50):
            cs={k:Fraction(random.randint(-3,4)) for k in random.sample(ev,min(len(ev),random.randint(1,min(6,len(ev)))))}
            b=aggregate_b(N,cs)
            direct=[sum(c*d(N,k,a) for k,c in cs.items()) for a in range(N)]
            assert b==direct
            counts['gen']+=N
            I=weighted_I(N,b)
            counts['brown']+=1
            l2=sum(x*x for x in b)
            assert l2==coeff_l2_beta(N,cs)
            counts['beta']+=1
            Lv=L_vec(N,b)
            absform=sum(abs(N-1-2*a)*b[a]*b[a] for a in range(N))
            assert I==Fraction(2,N*N)*absform
            assert absform <= (N-1)*l2
            assert absform <= sum(x*x for x in Lv)
            counts['L2']+=1
            lhs=L_vec(N,b)
            odd={}
            for k,c in cs.items():
                if k-1>=1: odd[k-1]=odd.get(k-1,Fraction(0))+(k-1)*c
                if k+1<=N: odd[k+1]=odd.get(k+1,Fraction(0))+(N-k)*c
            rhs=lincomb_D(N,odd)
            assert lhs==rhs
            counts['L']+=1
            eps=Fraction(random.randint(0,7),64)
            r=random.randint(1,5)
            parents=[eps*I/Fraction(r) for _ in range(r)]
            assert sum(parents)==eps*I
            counts['parent']+=1
    print('PASS')
    for k,v in counts.items(): print(k,v)

if __name__=='__main__': test()
