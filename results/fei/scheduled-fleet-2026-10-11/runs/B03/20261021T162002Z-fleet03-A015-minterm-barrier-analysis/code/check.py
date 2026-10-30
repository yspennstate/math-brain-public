"""A015 one-control-v1. Independent attachment enumeration; rational intervals."""
from pathlib import Path
from fractions import Fraction as F
from itertools import product, combinations
from math import factorial, prod
import argparse, json, time

ROOT=Path(__file__).resolve().parents[1]
START=time.perf_counter()
C={'assertions':0,'tables':0,'sectors':0,'assignments':0,'forest_shapes':0,
   'chronological_events':0,'leafless_tables':0,'positive_spectral_sectors':0}

def check(b):
    C['assertions']+=1
    assert b
    assert time.perf_counter()-START<55,'frozen runtime'

def dump(name,obj):
    (ROOT/'out'/name).write_text(json.dumps(obj,indent=2)+'\n',encoding='utf-8')

def fifth(x,bits=48):
    # Return an exact outward interval for x^(6/5).
    if not x:return F(0),F(0)
    y=x**6; scale=1<<bits
    target=y.numerator*scale**5//y.denominator
    lo,hi=0,1
    while hi**5<=target:hi*=2
    while hi-lo>1:
        m=(lo+hi)//2
        if m**5<=target:lo=m
        else:hi=m
    return F(lo,scale),F(hi,scale)

_cache={}
def fp(x):
    if x not in _cache:_cache[x]=fifth(x)
    return _cache[x]

def isum(terms):
    low=high=F(0)
    for base,coefficient in terms:
        a,b=fp(base);low+=a*coefficient;high+=b*coefficient
    return low,high

def subsets(n):return [m for m in range(1,1<<n)]

def antichains(n):
    # All nonconstant monotone Boolean functions, labelled (no symmetry quotient).
    S=subsets(n)
    for bits in range(1,1<<len(S)):
        tab=tuple(S[i] for i in range(len(S)) if bits>>i&1)
        if all((a&b)!=a and (a&b)!=b for a,b in combinations(tab,2)):
            yield tab

def truth(tab,n):return [1 if any(x&a==a for a in tab) else -1 for x in range(1<<n)]

def walsh(a):
    a=list(a);h=1
    while h<len(a):
        for i in range(0,len(a),2*h):
            for j in range(i,i+h):a[j],a[j+h]=a[j]+a[j+h],a[j]-a[j+h]
        h*=2
    return a

def influence(a,n):
    return F(sum(a[x]!=a[x^(1<<j)] for x in range(1<<n) for j in range(n)),1<<n)

def forests(owned,tab):
    V=tuple(owned)
    edges={(a,b) for a in V for b in V if a!=b and owned[a]&tab[b]}
    reach={(a,a) for a in V}|edges
    for h in V:
        for a in V:
            for b in V:
                if (a,h) in reach and (h,b) in reach:reach.add((a,b))
    comps=[];todo=set(V)
    while todo:
        a=min(todo); comp={b for b in todo if (a,b) in reach and (b,a) in reach}
        comps.append(comp);todo-=comp
    sources=[x for x in comps if not any(a not in x and b in x for a,b in edges)]
    for roots in product(*(tuple(sorted(x)) for x in sources)):
        nonroots=[a for a in V if a not in roots]
        for parents in product(*(tuple(a for a in V if (a,b) in edges) for b in nonroots)):
            parent=dict(zip(nonroots,parents));belong={};valid=True
            for a in V:
                seen=set();b=a
                while b not in roots:
                    if b in seen:valid=False;break
                    seen.add(b);b=parent[b]
                if not valid:break
                belong[a]=b
            if not valid:continue
            for attach in product(*(tuple(j for j in range(max(tab).bit_length()) if owned[parent[b]]&tab[b]>>0 & (1<<j)) for b in nonroots)):
                # Every ordering of children sharing an attachment is a distinct run.
                groups={}
                for b,j in zip(nonroots,attach):
                    key=(parent[b],j);groups[key]=groups.get(key,0)+1
                multiplicity=prod(factorial(x) for x in groups.values())
                yield roots,belong,multiplicity

def sector(tab,T,lam,beta):
    Vtotal=len(tab);pi=[F(1,1<<x.bit_count()) for x in tab]
    js=[j for j in range(T.bit_length()) if T>>j&1]
    old=[];zero=[];joint=[]
    for owners in product(*(tuple(l for l,R in enumerate(tab) if R>>j&1) for j in js)):
        owned={}
        for j,l in zip(js,owners):owned[l]=owned.get(l,0)|(1<<j)
        C['assignments']+=1
        k=len(owned);s={l:x.bit_count() for l,x in owned.items()}
        kap={l:(tab[l]&T).bit_count() for l in owned}
        check(0<=k-1<=len(js)-1)
        check(all(1<=s[l]<=kap[l]<=len(js) for l in owned))
        check(sum(F(s[l],kap[l]) for l in owned)>=1)
        z=prod(F(s[l],kap[l])**s[l] for l in owned)
        # Ranks use the SAME increasing physical coordinate order for each prime.
        for l,x in owned.items():
            R=[j for j in range(tab[l].bit_length()) if tab[l]>>j&1]
            for j in js:
                if x>>j&1:
                    rank=R.index(j)+1;previous=sum(h<j and bool(T>>h&1) for h in R)
                    z*=F(previous+1,rank)
        ratios={}
        for owner in owned:
            ratios[owner]=prod(F(s[l]+(l==owner),kap[l]+1)**(s[l]+(l==owner))/F(s[l],kap[l])**s[l] for l in owned)
        Zlo,Zhi=isum([(ratios[l],F(1)) for l in owned])
        # e<11/4; this is a slightly weaker rational version of the analytic bound.
        check(Zlo**5>=F(4,11)**(6*k)/k)
        if k==1:
            check(list(ratios.values())==[F(1)])
        else:
            check(Zlo**5>=F(4,11)**(12*(k-1))/2**(k-1))
        # Boundary k=1,s=kappa has positive surplus, not an equality interval issue.
        for roots,belong,multiplicity in forests(owned,tab):
            C['forest_shapes']+=1;C['chronological_events']+=multiplicity
            weight=prod(lam[l] for l in owned)*prod(pi[a] for a in roots)*multiplicity
            old.append((z,weight));zero.append((z,weight*beta**k))
            c=len(roots)
            rf={l:F(1) if c==1 else factorial(c-1)*pi[belong[l]]/prod(pi[a] for a in roots) for l in owned}
            check(all(x>=1 for x in rf.values()))
            Glo,Ghi=isum([(ratios[l],beta**k*rf[l]) for l in owned])
            check(Glo**5>=beta**(5*k)*F(4,11)**(6*k)/k)
            if k==1:check(Glo==beta)
            joint.extend((z*ratios[l],weight*beta**k*rf[l]) for l in owned)
    C['sectors']+=1
    den=isum(old);L=isum(zero);J=isum(joint)
    check(den[0]>0 and L[0]>0 and J[0]>0)
    # k<=|T| gives direct SAME-posterior uniform lower bounds, all events included.
    s=len(js)
    check(L[0]>=beta**s*den[0])
    # Ratio interval certified lower bound: beta^s*(4/11)^(6s/5)/s^(1/5).
    check((J[0]/den[1])**5>=beta**(5*s)*F(4,11)**(6*s)/s)
    return {'T':T,'records':len(old),'L_interval':[str(L[0]/den[1]),str(L[1]/den[0])],
            'J_interval':[str(J[0]/den[1]),str(J[1]/den[0])]}

def run(n):
    count=0
    for tab in antichains(n):
        count+=1;C['tables']+=1
        read=max(sum(bool(R>>j&1) for R in tab) for j in range(n))
        lam=[F(1,read)]*len(tab);beta=min(F(1),1/sum(lam))
        check(all(sum(lam[l] for l,R in enumerate(tab) if R>>j&1)<=1 for j in range(n)))
        check(beta*sum(lam)<=1)
        if all(sum(R.bit_count()==1 and bool(R>>j&1) for R in tab)==0 for j in range(n)) and all(sum(bool(R>>j&1) for R in tab)>=2 for j in range(n)):
            C['leafless_tables']+=1
        pi=[F(1,1<<R.bit_count()) for R in tab]
        D=prod(1+l*p for l,p in zip(lam,pi))-1
        Dp=prod(1+beta*l*p/2 for l,p in zip(lam,pi))-1
        check(0<Dp<=beta*D/2)
        g=truth(tab,n);gh=walsh(g);I=influence(g,n)
        check(sum(x*x for x in gh)==1<<(2*n))
        check(sum(F(x*x*T.bit_count(),1<<(2*n)) for T,x in enumerate(gh))==I)
        # Activation of B=(g+1)/2, i.e. fresh-control AND B, retaining all spectra.
        act=[g[x>>1] if x&1 else -1 for x in range(1<<(n+1))];ah=walsh(act)
        b=F(sum(x==1 for x in g),1<<n)
        check(influence(act,n+1)==I/2+b)
        check(F(ah[0],1<<(n+1))==b-1)
        check(sum(x*x for x in ah)==1<<(2*(n+1)))
        check(F(ah[1],1<<(n+1))==-b)
        v=1-F(gh[0],1<<n)**2
        check(sum(F(ah[T]*ah[T],1<<(2*(n+1))) for T in range(2,1<<(n+1)))==v/2)
        check(F(ah[1]*ah[1],1<<(2*(n+1)))==b*b)
        check(I>=v)
        for T in range(1,1<<n):
            for u in (0,1):check(ah[(T<<1)|u]==(-1 if u else 1)*gh[T])
        rows=[]
        for T in range(1,1<<n):
            if all(any(R>>j&1 for R in tab) for j in range(n) if T>>j&1):
                row=sector(tab,T,lam,beta)
                if gh[T]:C['positive_spectral_sectors']+=1
                rows.append(row)
        dump('CHECKPOINT.json',{'n':n,'last_table':tab,'counts':C,'elapsed':time.perf_counter()-START})
        if tab==tuple([3,5,6]) or (n==4 and tab==tuple([3,5,6,9,10,12])):
            dump('LEAFLESS_'+str(n)+'.json',{'tab':tab,'beta':str(beta),'D':str(D),'Dprime':str(Dp),'influence':str(I),'rows':rows})
    check(count=={1:1,2:4,3:18,4:166}[n])

if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--pilot',action='store_true');args=ap.parse_args()
    for n in ([1,2] if args.pilot else [1,2,3,4]):run(n)
    check(F(87,32)<F(11,4) and F(11,4)**2<8)
    result={'status':'PASS','helper_version':'A015-one-control-v1','counts':C,
            'elapsed_seconds':time.perf_counter()-START,'arithmetic':'Fraction; outward 48-bit rational fifth-root intervals; integer Walsh',
            'scope':'finite validation of analytic arbitrary-incidence one-control transfer, not FEI'}
    dump('PILOT.json' if args.pilot else 'EXACT_CHECK.json',result)
    print(json.dumps(result))
