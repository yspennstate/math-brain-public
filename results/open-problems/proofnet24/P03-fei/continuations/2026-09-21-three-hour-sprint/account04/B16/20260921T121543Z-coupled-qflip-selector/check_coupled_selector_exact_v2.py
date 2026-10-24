#!/usr/bin/env python3
from fractions import Fraction
import itertools, math, random, json

def shapley(v,m):
    F=[math.factorial(i) for i in range(m+1)]; den=F[m]; out=[0]*m
    for i in range(m):
        for S in range(1<<m):
            if S>>i&1: continue
            k=S.bit_count()
            out[i]+=Fraction(F[k]*F[m-k-1],den)*(v[S|1<<i]-v[S])
    return out

def block(v,g):
    out=[Fraction(0)]*(2*g)
    for perm in itertools.permutations(range(g)):
        for flips in range(1<<g):
            S=0; w=Fraction(1,math.factorial(g)*(1<<g))
            for j in perm:
                a,b=2*j,2*j+1
                if flips>>j&1: a,b=b,a
                out[a]+=w*(v[S|1<<a]-v[S]); S|=1<<a
                out[b]+=w*(v[S|1<<b]-v[S]); S|=1<<b
    return out

def mobius(v,m):
    d=list(v)
    for i in range(m):
        for S in range(1<<m):
            if S>>i&1: d[S]-=d[S^(1<<i)]
    return d

def exact_game_checks():
    rng=random.Random(160921); cases=0
    for g in (2,3,4):
        m=2*g
        for _ in range(8):
            v=[Fraction(rng.randint(-7,7)) for _ in range(1<<m)]; v[0]=0
            fine=shapley(v,m); blk=block(v,g)
            coarse=[]
            for A in range(1<<g):
                S=sum(((3<<(2*j)) if A>>j&1 else 0) for j in range(g))
                coarse.append(v[S])
            coarse_phi=shapley(coarse,g)
            d=mobius(v,m); delta=[Fraction(0)]*g
            for T in range(1,1<<m):
                touched={j:((T>>(2*j))&1)+((T>>(2*j+1))&1) for j in range(g)}
                touched={j:t for j,t in touched.items() if t}
                s=len(touched); q=T.bit_count(); r=sum(t==2 for t in touched.values())
                coeff=[]
                for j,t in touched.items():
                    w=Fraction(t,q)-Fraction(1,s); delta[j]+=d[T]*w; coeff.append(w)
                assert sum(coeff)==0
                if 0<r<s:
                    assert sum(w*w for w in coeff)==Fraction(r*(s-r),s*(s+r)*(s+r))
                    assert sum(w*w for w in coeff)<=Fraction(1,8*s)
            for j in range(g):
                assert blk[2*j]+blk[2*j+1]==coarse_phi[j]
                assert fine[2*j]+fine[2*j+1]-coarse_phi[j]==delta[j]
            assert sum(delta)==0; cases+=1
    return cases

def parity_checks():
    checks=0
    for g in (2,3,4):
        m=2*g
        for R in range(1,1<<m):
            if R.bit_count()%2==0: continue
            c=Fraction(-3 if R%3==0 else 5,7)
            v=[c if (S&R).bit_count()%2 else Fraction(0) for S in range(1<<m)]
            p=block(v,g)
            odd=sum((((R>>(2*j))&1)+((R>>(2*j+1))&1))%2 for j in range(g))
            for j in range(g):
                t=((R>>(2*j))&1)+((R>>(2*j+1))&1)
                assert p[2*j]+p[2*j+1] == (c/Fraction(odd) if t%2 else 0)
            checks+=1
    return checks

def fwht(a):
    a=[float(x) for x in a]; h=1
    while h<len(a):
        for i in range(0,len(a),2*h):
            for j in range(i,i+h): a[j],a[j+h]=a[j]+a[j+h],a[j]-a[j+h]
        h*=2
    return [x/len(a) for x in a]

def H(a):
    return -sum((x*x)*math.log2(x*x) for x in fwht(a) if abs(x)>1e-15)

def gens(n):
    out=[]
    for v in range(1,1<<n):
        if v.bit_count()<2: continue
        p=(v&-v).bit_length()-1
        z=[-1 if all(((x>>j)&1)==((v>>j)&1) for j in range(p,n)) else 1 for x in range(1<<n)]
        out.append((v,p,z))
    return out

def game(vals,n):
    act=[]
    for v,p,z in gens(n):
        if vals[0]*vals[1<<p]*vals[v]*vals[v^(1<<p)]==-1: act.append((v,z))
    V=[0.0]*(1<<len(act)); phases={0:[1]*(1<<n)}
    for S in range(1,1<<len(act)):
        b=S&-S; j=b.bit_length()-1; prev=S^b
        phases[S]=[a*bv for a,bv in zip(phases[prev],act[j][1])]; V[S]=H(phases[S])
    F=[math.factorial(i) for i in range(len(act)+1)]; phi=[]
    for j in range(len(act)):
        x=0.0
        for S in range(1<<len(act)):
            if S>>j&1: continue
            k=S.bit_count(); x+=F[k]*F[len(act)-k-1]/F[len(act)]*(V[S|1<<j]-V[S])
        phi.append(x)
    return [v for v,_ in act],phi

def boolean_counterexample():
    f=[1,-1,1,-1,1,-1,-1,-1]
    a,p=game(f,3); up=[f[x&7] for x in range(16)]; b,q=game(up,4)
    assert a==[6,7] and b==[6,7,14,15]
    coarse=dict(zip(a,p)); fine=dict(zip(b,q))
    agg={6:fine[6]+fine[14],7:fine[7]+fine[15]}
    assert abs(coarse[6]-1.0)<1e-12
    assert abs(coarse[7]-1.2169171866886992)<1e-12
    assert abs(agg[6]-1.4547869923250596)<1e-12
    assert abs(agg[7]-0.7621301943636398)<1e-12
    return {"coarse":coarse,"fine_orbit":agg,"delta":{k:agg[k]-coarse[k] for k in coarse}}

out={"status":"PASS","exact_generic_games":exact_game_checks(),"exact_signed_parity_games":parity_checks(),"counterexample":boolean_counterexample(),"l2_bound":"sum w^2 <= 1/(8s)"}
print(json.dumps(out,sort_keys=True,indent=2))
