import itertools, json, math, sys, time
from fractions import Fraction as F
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
checks=0
def ck(x):
    global checks
    assert x
    checks+=1
def rat(x): return str(x)
def oddfac(k): return math.prod(range(k,0,-2))
def pairings(A):
    if not A:
        yield ()
        return
    j=A[0]
    for k in A[1:]:
        for rest in pairings(tuple(x for x in A if x not in (j,k))):
            yield ((j,k),)+rest
def lnunit(x):
    z=(x-1)/(x+1); zz=z*z; power=z; total=F(0)
    for k in range(30):
        total+=power/(2*k+1); power*=zz
    return 2*total,2*total+2*power/(61*(1-zz))
LN2=lnunit(F(2))
def log2int(x):
    shift=0
    while x>=2: x/=2; shift+=1
    while x<1: x*=2; shift-=1
    lo,hi=lnunit(x)
    return F(shift)+lo/LN2[1],F(shift)+hi/LN2[0]
def spectrum(n):
    vals=[1 if b.bit_count()>=2 else -1 for b in range(1<<n)]
    w=vals[:]; d=1
    while d<len(w):
        for j in range(0,len(w),2*d):
            for k in range(j,j+d): w[k],w[k+d]=w[k]+w[k+d],w[k]-w[k+d]
        d*=2
    ck(sum(x*x for x in w)==(1<<n)**2)
    I=F(sum(vals[b]!=vals[b^(1<<j)] for b in range(1<<n) for j in range(n)),1<<n)
    ck(I==F(n*(n-1),2**(n-1)))
    for b in range(1,1<<n): ck(w[b]*w[b]==4*(n+1-2*b.bit_count())**2)
    v=sum(F(x*x,4**n) for x in w[1:])
    ck(v==4*F(n+1,2**n)*(1-F(n+1,2**n)))
    return I,v
def W(n,a):
    L=48*(n-1); J=32*(n-1)
    if a%2==0: return F(oddfac(a-1),L**(a//2))
    if a<n: return F(a*(n-a)*oddfac(a-2),J*L**((a-1)//2))
    return F(n*(n-1)*oddfac(n-2),L**((n+1)//2))
def event_counts(n,a):
    A=tuple(range(a)); events=set(); mass=F(0); lam=F(1,n-1); pi=F(1,4)
    if a%2==0:
        for pairs in pairings(A):
            event=(pairs,None,None); ck(event not in events); events.add(event)
            mass+=(lam*pi*F(1,6)*F(1,2))**len(pairs)
    else:
        for j in A:
            for pairs in pairings(tuple(x for x in A if x!=j)):
                for k in (range(a,n) if a<n else (x for x in A if x!=j)):
                    event=(pairs,j,k); ck(event not in events); events.add(event)
                    base=(lam*pi*F(1,6)*F(1,2))**len(pairs)
                    if a<n:
                        ck(all(k not in p and j not in p for p in pairs))
                        mass+=base*lam*pi*F(1,4)*F(1,2)
                    else:
                        ck(sum(k in p for p in pairs)==1)
                        mass+=base*F(1,3)*F(1,2)*lam*F(1,4)*F(1,2)
    ck(mass==W(n,a))
    ck(W(n,a)>=F(math.factorial(a//2),(48*(n-1))**(a//2+1)))
    return len(events)
def certificate(n):
    N=n*(n-1)//2; lam=F(1,n-1); pi=F(1,4)
    D=(1+lam*pi)**N-1; p=lam*pi/(1+lam*pi); Z=1-(1-p)**N
    v=4*F(n+1,2**n)*(1-F(n+1,2**n)); I=F(n*(n-1),2**(n-1))
    c0=sum(math.comb(n,a)*F((n+1-2*a)**2,4**(n-1))*((a+1)//2) for a in range(1,n+1))/N
    rho=p/Z; price=F(n-1,2)*(c0-v*rho)
    ck(price>0); ck(v*rho-c0+lam*2*price==0); ck(lam*(n-1)==1)
    ck(N*rho<=1+N*p); ck(c0*N>=I/2)
    return {'n':n,'c0':rat(c0),'v':rat(v),'I':rat(I),'root_marginal':rat(rho),'coordinate_price':rat(price),'KKT_exact':True}
def run(pilot):
    start=time.perf_counter(); cases=[]; counts=[]
    for n in ([4,5] if pilot else [4,5,6,7,8]):
        I,v=spectrum(n); N=n*(n-1)//2; D=(1+F(1,4*(n-1)))**N-1
        costlo=F(0); costhi=F(0); offhi=F(0); qtotal=F(0)
        for a in range(1,n+1):
            count=event_counts(n,a); q=W(n,a)/D; ck(0<q<=1)
            qtotal+=math.comb(n,a)*q
            lo,hi=log2int(1/q); P=math.comb(n,a)*F((n+1-2*a)**2,4**(n-1))
            costlo+=P*lo; costhi+=P*hi
            if a>=3: offhi+=P*hi
            ck(hi<=F(37*n,4))
            counts.append({'n':n,'a':a,'actual_event_count':count,'W':rat(W(n,a)),'Q':rat(q)})
        ck(qtotal<=1); ck(costhi<=F(185,6)*I); ck(offhi<=F(185,6)*I)
        cases.append({'n':n,'density':rat(F(N,4)),'cross_entropy_over_I_interval':[rat(costlo/I),rat(costhi/I)],'off_support_over_I_upper':rat(offhi/I),'display_upper':float(costhi/I),'subprobability_total':rat(qtotal),'KKT':certificate(n)})
        (ROOT/'out'/'PARTIAL.json').write_text(json.dumps(cases,indent=2),encoding='utf-8')
    scalars=[] if pilot else [certificate(n) for n in [4,5,6,7,8,9,10,11,12,16,32,64,128]]
    result={'helper_version':'A009-matching-v1','checks':checks,'elapsed_seconds':time.perf_counter()-start,'cases':cases,'scalar_certificates':scalars,'all_passed':True}
    (ROOT/'out'/('PILOT.json' if pilot else 'CHECK.json')).write_text(json.dumps(result,indent=2),encoding='utf-8')
    (ROOT/'out'/'MATCHING_COUNTS.json').write_text(json.dumps(counts,indent=2),encoding='utf-8')
    print(json.dumps({'checks':checks,'elapsed_seconds':result['elapsed_seconds'],'all_passed':True,'ratio_upper':[x['display_upper'] for x in cases]}))
def graphs():
    start=time.perf_counter(); rows=[]; possible=list(itertools.combinations(range(4),2)); zero_positive=0
    for mask in range(1,64):
        edges={e for k,e in enumerate(possible) if mask>>k&1}; delta=max(sum(j in e for e in edges) for j in range(4))
        lam=F(1,delta); L=48*delta; J=32*delta; D=(1+lam/4)**len(edges)-1
        vals=[1 if any(all(b>>j&1 for j in e) for e in edges) else -1 for b in range(16)]
        w=vals[:]
        for d in [1,2,4,8]:
            for j in range(0,16,2*d):
                for k in range(j,j+d): w[k],w[k+d]=w[k]+w[k+d],w[k]-w[k+d]
        ck(sum(x*x for x in w)==256)
        ck(sum(F(w[b]**2,256)*b.bit_count() for b in range(16))==F(sum(vals[b]!=vals[b^(1<<j)] for b in range(16) for j in range(4)),16))
        qtotal=F(0)
        for b in range(1,16):
            A=tuple(j for j in range(4) if b>>j&1); a=len(A); m=a//2
            def pm(B): return sum(all(tuple(sorted(e)) in edges for e in pairs) for pairs in pairings(tuple(B)))
            if a%2==0: expected=F(pm(A),L**m)
            else:
                ext=sum(sum(tuple(sorted((j,k))) in edges for k in range(4) if k not in A)*pm(tuple(x for x in A if x!=j)) for j in A)
                inside=sum(sum(tuple(sorted((j,k))) in edges for k in A if k!=j)*pm(tuple(x for x in A if x!=j)) for j in A)
                expected=F(ext,J*L**m)+F(inside,L**(m+1))
            actual=F(0); events=set()
            if a%2==0:
                for pairs in pairings(A):
                    if all(tuple(sorted(e)) in edges for e in pairs):
                        event=(pairs,None,None); ck(event not in events); events.add(event)
                        actual+=(lam*F(1,4)*F(1,6)*F(1,2))**m
            else:
                for j in A:
                    for pairs in pairings(tuple(x for x in A if x!=j)):
                        if not all(tuple(sorted(e)) in edges for e in pairs): continue
                        for k in range(4):
                            if k==j or tuple(sorted((j,k))) not in edges: continue
                            event=(pairs,j,k); ck(event not in events); events.add(event)
                            base=(lam*F(1,4)*F(1,6)*F(1,2))**m
                            actual+=base*(lam*F(1,4)*F(1,4)*F(1,2) if k not in A else F(1,3)*F(1,2)*lam*F(1,4)*F(1,2))
            ck(actual==expected); qtotal+=expected/D
            if not expected and w[b]: zero_positive+=1
            if edges=={(0,1),(0,2),(0,3)} and b==14:
                ck(expected==0); ck(F(w[b]**2,256)==F(1,64))
                witness={'edges':sorted(edges),'A':list(A),'P':str(F(w[b]**2,256)),'Q_matching':str(expected)}
        ck(qtotal<=1); rows.append({'graph_mask':mask,'maximum_degree':delta,'matching_subprobability':str(qtotal)})
    result={'all_passed':True,'graph_tables':63,'sets':945,'checks':checks,'elapsed_seconds':time.perf_counter()-start,'positive_mass_zero_matching_sets':zero_positive,'star_witness':witness,'tables':rows}
    (ROOT/'out'/'GRAPH_CHECK.json').write_text(json.dumps(result,indent=2),encoding='utf-8')
    print(json.dumps({k:v for k,v in result.items() if k!='tables'}))
if __name__=='__main__':
    sys.set_int_max_str_digits(0)
    if '--graphs' in sys.argv: graphs()
    else: run('--pilot' in sys.argv)
