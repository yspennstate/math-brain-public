from fractions import Fraction


def pc(x): return x.bit_count()
def odd_masks(m): return [r for r in range(1,1<<m) if pc(r)%2]

def phi(S,b):
    return sum((c*(-1 if pc(S&R)%2 else 1) for R,c in b.items()), Fraction(0))

def edelta(v,p,b,m):
    others=[j for j in range(m) if j!=v]
    ans=Fraction(0)
    for z in range(1<<len(others)):
        S=0; k=0
        for a,j in enumerate(others):
            if z>>a&1: S|=1<<j; k+=1
        prob=p**k*(1-p)**(len(others)-k)
        ans += prob*(phi(S,b)-phi(S|(1<<v),b))
    return ans

def mv(v,t,b):
    return sum((c*t**(pc(R)-1) for R,c in b.items() if R>>v&1), Fraction(0))

def integrate_square(poly,T=Fraction(1,2)):
    return sum((ca*cb*T**(a+d+1)/Fraction(a+d+1)
                for a,ca in poly.items() for d,cb in poly.items()), Fraction(0))

def low_direct(b,m):
    ans=Fraction(0)
    for v in range(m):
        h={}
        for R,c in b.items():
            if R>>v&1:
                q=pc(R); h[q-1]=h.get(q-1,Fraction(0))+c*Fraction(q-1,q)
        ans += integrate_square(h)
    return ans

def variance_form(b,m):
    U=Fraction(0); refund=Fraction(0); T=Fraction(1,2)
    for v in range(m):
        p={}; mean=Fraction(0)
        for R,c in b.items():
            if R>>v&1:
                q=pc(R); p[q-1]=p.get(q-1,Fraction(0))+c
                mean += c*T**q/q
        U += integrate_square(p); refund += 2*mean*mean
    return U,refund,U-refund

def noise_slope(p,b,m):
    base={(0,0):(1-p)**2,(0,1):(1-p)*p,(1,0):p*(1-p),(1,1):p*p}
    der={(0,0):p*(1-p),(0,1):-p*(1-p),(1,0):-p*(1-p),(1,1):p*(1-p)}
    ans=Fraction(0)
    for X in range(1<<m):
      for Y in range(1<<m):
        val=phi(X,b)*phi(Y,b)
        if not val: continue
        c=Fraction(0)
        for v in range(m):
            z=der[((X>>v)&1,(Y>>v)&1)]
            for u in range(m):
                if u!=v: z*=base[((X>>u)&1,(Y>>u)&1)]
            c+=z
        ans += val*c
    return ans

families=0; assertions=0
for m in (2,3,4):
    masks=odd_masks(m); fs=[]
    for R in masks: fs.append({r:Fraction(int(r==R)) for r in masks})
    for seed in range(1,13):
        fs.append({R:Fraction(((seed*(i+3)+7*pc(R)+i*i)%5)-2) for i,R in enumerate(masks)})
    for b in fs:
        families+=1
        for t in (Fraction(1,5),Fraction(1,3),Fraction(1,2)):
            p=(1-t)/2; ms=[]
            for v in range(m):
                x=mv(v,t,b); assert 2*x==edelta(v,p,b,m); assertions+=1; ms.append(x)
            W1=p*(1-p)*sum((edelta(v,p,b,m)**2 for v in range(m)),Fraction(0))
            assert W1==(1-t*t)*sum((x*x for x in ms),Fraction(0)); assertions+=1
            assert noise_slope(p,b,m)==W1; assertions+=1
        L=low_direct(b,m); U,R,C=variance_form(b,m)
        assert L==C and U>=0 and R>=0; assertions+=3

print('families_checked=',families)
print('exact_assertions_passed=',assertions)
for q in (3,5,7,9,15,25):
    L=Fraction((q-1)**2,q)*Fraction(1,(2*q-1)*2**(2*q-1))
    V=sum((Fraction(1,(2*k+1)*2**(2*k+1)) for k in range(q)),Fraction(0))
    print('q=',q,' exact_low=',float(L),' var_surrogate=',float(V),' ratio=',float(V/L))
print('status=PASS')
