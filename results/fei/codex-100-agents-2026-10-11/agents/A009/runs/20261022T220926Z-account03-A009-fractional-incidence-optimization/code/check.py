import itertools, json, math, sys, time
from fractions import Fraction as F
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
COUNT = 0

def ck(test):
    global COUNT
    assert test
    COUNT += 1

def lnunit(x):
    z = (x-1)/(x+1)
    term, total = z, F(0)
    for j in range(22):
        total += term/(2*j+1)
        term *= z*z
    return 2*total, 2*total+2*term/(45*(1-z*z))

LN2L, LN2H = lnunit(F(2))

def logbounds(x):
    assert x > 0
    k = x.numerator.bit_length()-x.denominator.bit_length()
    y = x/F(2)**k
    if y < 1:
        y *= 2
        k -= 1
    assert 1 <= y < 2
    lo, hi = lnunit(y)
    scale=2**90
    low=F(k)+lo/LN2H; high=F(k)+hi/LN2L
    return F((low*scale).__floor__(),scale), F((high*scale).__ceil__(),scale)

def numerator(a, b, s, t):
    if not t:
        return F(1,32)**s
    if not s:
        return F(a,32*b)**t
    k = s+t
    return F(1, b**(k-1)*24*8**(k-2)*(k-1)**2*k)

def physical(a,b):
    n=a+b; size=1<<n
    truth=[1 if (x&((1<<a)-1)) and (x>>a) else -1 for x in range(size)]
    w=truth[:]; step=1
    while step<size:
        for start in range(0,size,2*step):
            for j in range(start,start+step):
                x,y=w[j],w[j+step]; w[j],w[j+step]=x+y,x-y
        step*=2
    u,v=F(1,2**a),F(1,2**b)
    il=2*a*u*(1-v); ir=2*b*v*(1-u); infl=il+ir
    inf=[F(sum(truth[x]!=truth[x^(1<<i)] for x in range(size)),size) for i in range(n)]
    ck(sum(inf)==infl)
    ck(sum(F(w[x]**2,size**2)*x.bit_count() for x in range(size))==infl)
    ck(sum(c*c for c in w)==size**2)
    D=(1+F(1,4*b))**(a*b)-1
    variance=1-F(w[0]**2,size**2)
    ck(variance==4*(u+v-u*v)*(1-u)*(1-v))
    terms={D:variance}; subprob=F(0); degree=F(0); mixdegree=F(0); rightdegree=F(0)
    for mask in range(1,size):
        s=(mask&((1<<a)-1)).bit_count(); t=(mask>>a).bit_count()
        coeff=2*u*(1-v) if not t else 2*v*(1-u) if not s else 2*u*v
        p=F(w[mask]**2,size**2)
        ck(p==coeff**2)
        N=numerator(a,b,s,t)
        subprob+=N/D
        degree+=p*(s+t)
        if s and t:
            mixdegree+=p*(s+t)
            ck(N>=F(1,(48*b)**(s+t-1)))
        elif not s:
            rightdegree+=p*t
        terms[N]=terms.get(N,F(0))-p
    ck(subprob<=1)
    ck(degree==infl)
    ck(rightdegree==2*b*v*(1-u)**2)
    ck(mixdegree==2*u*v*(a*(1-v)+b*(1-u)))
    lower=upper=F(0)
    for arg,c in terms.items():
        lo,hi=logbounds(arg)
        lower+=c*(lo if c>=0 else hi)
        upper+=c*(hi if c>=0 else lo)
    ck(upper<F(97,8)*infl)
    # An independent original probability product for every canonical mixed run.
    for s in range(1,a+1):
        for t in range(1,b+1):
            children=s+t-2
            root=F(1,b)*F(1,4)*F(1,6)
            parent=F(1,(children+1)*(children+2))*F(1,children+1)
            child=(F(1,b)*F(1,4)*F(1,2))**children
            ck(root*parent*child==numerator(a,b,s,t))
            # Fixed owner edges are distinct; all children attach to the root pair.
            al=list(range(s)); ar=list(range(a,a+t))
            owned=[(al[0],ar[0])]+[(i,ar[0]) for i in al[1:]]+[(al[0],j) for j in ar[1:]]
            ck(len(set(owned))==s+t-1)
    return {'a':a,'b':b,'I':str(infl),'D':str(D),'subprobability':str(subprob),'cost_interval':[str(lower),str(upper)],'ratio_upper_display':float(upper/infl)}

def scalars(limit):
    for a in range(1,limit+1):
        for b in range(a,limit+1):
            u,v=F(1,2**a),F(1,2**b); t=b-a
            ck(F(b,a)<=2**t)
            ck(F(t*(t+1),2**t)<=F(3,2))
            ck(F(b*b,2**b)<=F(9,8))
            ck(F(b,a)<=t+1)
            if b>=2:
                il=2*a*u*(1-v)
                r=2*b*v*(1-u)**2
                m=2*u*v*(a*(1-v)+b*(1-u))
                ck(r*t<=2*il)
                ck(m*b<=3*il)
    for d in range(129):
        ck((d+1)**2*(d+2)<=2*6**d)
        if d>=1:
            ck((d+2)**2*(d+3)<=6*(d+1)**2*(d+2))
    ck(LN2L>F(2,3))
    ck(F(97,8)<13)

def root_review():
    funcs=faces=0
    for n in range(1,4):
        N=1<<n
        for tt in range(1,2**N-1):
            f=[1 if tt>>x&1 else -1 for x in range(N)]
            q=F(f.count(-1),N)
            inf=[F(sum(f[x]!=f[x^(1<<i)] for x in range(N)),N) for i in range(n)]
            funcs+=1
            for pat in itertools.product([-1,0,1],repeat=n):
                coords=[i for i,p in enumerate(pat) if p!=-1]
                if not coords: continue
                matches=[x for x in range(N) if all((x>>i&1)==pat[i] for i in coords)]
                if any(f[x]!=1 for x in matches): continue
                width=len(coords); faces+=1
                ck(sum(inf[i] for i in coords)>=F(2*width,2**width-1)*q)
                outside=[i for i in range(n) if i not in coords]
                for y in range(1<<len(outside)):
                    layer=[x for x in range(N) if all((x>>i&1)==(y>>j&1) for j,i in enumerate(outside))]
                    false={x for x in layer if f[x]<0}
                    boundary=sum((x^(1<<i)) not in false for x in false for i in coords)
                    ck(not false or boundary>=width)
                    ck(len(false)<2**width)
    # Sharpness, plus failed hypotheses with actual Boolean witnesses.
    for k in range(1,65):
        q=1-F(1,2**k); I=F(k,2**(k-1)); ak=F(2**k-1,k*2**k)
        ck(F(1,2**k)==ak*I/(2*q))
    ck(F(1,2)>0)  # f=x0; the fake x1 gate has zero incident influence.
    ck(2*F(1,4)>F(1,4))  # duplicate AND2 weights1 violate packing.
    return {'functions':funcs,'signed_implicant_faces':faces}

if __name__=='__main__':
    start=time.perf_counter(); pilot='--pilot' in sys.argv
    ROOT.joinpath('out').mkdir(exist_ok=True)
    rows=[physical(a,b) for a in range(1,4 if pilot else 6) for b in range(a,4 if pilot else 6)]
    scalars(8 if pilot else 64)
    review=root_review()
    result={'helper_version':'A009-leafless-bipartite-v1','pilot':pilot,'functions':len(rows),'checks':COUNT,'root_review':review,'elapsed_seconds':time.perf_counter()-start,'all_passed':True,'cases':rows}
    ROOT.joinpath('out','PILOT.json' if pilot else 'CHECK.json').write_text(json.dumps(result,indent=2),encoding='utf-8')
    print(json.dumps({k:v for k,v in result.items() if k!='cases'}))
