from pathlib import Path
from fractions import Fraction as Q
from itertools import permutations
import json, sys, time
R = Path(__file__).resolve().parents[1]
pilot = '--pilot' in sys.argv
checks = 0
def ck(v):
    global checks
    assert v
    checks += 1
def fw(a):
    a = list(a); h = 1
    while h < len(a):
        for j in range(0, len(a), 2*h):
            for i in range(j, j+h):
                x,y=a[i],a[i+h]; a[i]=x+y; a[i+h]=x-y
        h *= 2
    return a
def span_add(span, v):
    return span | {x^v for x in span}
def profile(n,m):
    N=1<<n; den=N*N
    vals=[1 if m>>x&1 else -1 for x in range(N)]
    ws=fw(vals); weights=[x*x for x in ws]
    corr=fw(weights)
    pn=[(den-corr[1<<i])//2 for i in range(n)]
    costs=[min((den-corr[v])//2,(den+corr[v])//2) for v in range(N)]
    if n<=3:
        assert pn==[sum(w for s,w in enumerate(weights) if s>>i&1) for i in range(n)]
        assert costs==[min(sum(w for s,w in enumerate(weights) if (s&v).bit_count()%2),sum(w for s,w in enumerate(weights) if not (s&v).bit_count()%2)) for v in range(N)]
    sp={0}; basis=[]; best=0
    for v in sorted(range(1,N),key=lambda x:(costs[x],x)):
        if v not in sp:
            best+=costs[v];basis.append(v);sp=span_add(sp,v)
    return {'n':n,'m':m,'vals':vals,'ws':ws,'pn':pn,'I':sum(pn),'char':sum(min(x,den-x) for x in pn),'aff':best,'basis':basis,'costs':costs,'den':den}
def affine_min(p):
    if any(x*2>p['den'] for x in p['pn']):return False
    return all(p['costs'][v]>=max(p['pn'][i] for i in range(p['n']) if v>>i&1) for v in range(1,1<<p['n']))
def child_mask(n,m,i,b):
    out=0
    for y in range(1<<(n-1)):
        x=(y&((1<<i)-1))|((y>>i)<<(i+1))|(b<<i)
        out|=((m>>x)&1)<<y
    return out
def add(a,b,scale=Q(1)):
    d=dict(a)
    for k,v in b.items():
        d[k]=d.get(k,Q(0))+scale*v
        if not d[k]:del d[k]
    return d
def factorlog(q):
    q=Q(q);assert q>0;d={}
    for v,sg in [(q.numerator,1),(q.denominator,-1)]:
        p=2
        while p*p<=v:
            while v%p==0:d[p]=d.get(p,0)+sg;v//=p
            p+=1
        if v>1:d[v]=d.get(v,0)+sg
    return {p:Q(x) for p,x in d.items() if x}
def raw(q):
    q=Q(q)
    return {k:-q*v for k,v in factorlog(q).items()} if q else {}
def entropy(p):
    d={}
    for w in p['ws']:d=add(d,raw(Q(w*w,p['den'])))
    return d
def scale(a,x):return {k:v*x for k,v in a.items() if v*x}
def deep(p,children):
    n=p['n'];N=1<<n;den=p['den'];h=entropy(p);I=Q(p['I'],den)
    ck(p['ws']==[sum(p['vals'][x]*(-1 if (s&x).bit_count()%2 else 1) for x in range(N)) for s in range(N)])
    ck(p['I']==N*sum(p['vals'][x]!=p['vals'][x^(1<<j)] for x in range(N) for j in range(n)))
    B={};JS={};avgh=[];taus=[]
    for i,cp in enumerate(children):
        bi={}
        for s in range(N):
            if not s>>i&1:
                x=Q(p['ws'][s]**2,den);y=Q(p['ws'][s|1<<i]**2,den)
                bi=add(add(add(bi,raw(x)),raw(y)),raw(x+y),Q(-1))
        hh=scale(add(entropy(cp[0]),entropy(cp[1])),Q(1,2))
        L=add(h,hh,Q(-1));js=add(L,bi,Q(-1));B=add(B,bi);JS=add(JS,js);avgh.append(hh)
        tau=sum(Q(c['I']-c['char'],c['den']) for c in cp)/2;taus.append(tau)
        ck(I==Q(p['pn'][i],den)+sum(Q(c['I'],c['den']) for c in cp)/2)
    dtc=add(h,B,Q(-1))
    for K in [0,2,7]:
        D=add(h,{2:K*I},Q(-1));left=add(dtc,D,n-1)
        for cp,hh,tau in zip(children,avgh,taus):
            reserve=add({2:K*sum(Q(c['char'],c['den']) for c in cp)/2},hh,Q(-1))
            left=add(add(left,reserve),{2:K*tau})
        ck(left==JS)
    return {'H':{str(k):str(v) for k,v in h.items()},'I':str(I),'tau_total':str(sum(taus,Q(0)))}
start=time.perf_counter()
cache={}
for n in range(4):
    for m in range(1<<(1<<n)):
        p=profile(n,m);cache[n,m]=p
        if n<=2:
            costs=p['costs'];options=[]
            for bs in permutations(range(1,1<<n),n):
                sp={0}
                for v in bs:sp=span_add(sp,v)
                if len(sp)==1<<n:options.append(sum(costs[v] for v in bs))
            ck(p['aff']==min(options,default=0))
roots=0;affcounts={};weakcounts={};weakaffcounts={};charpositive=0;witnesses=[];banks=0
for n in range(4 if pilot else 5):
    N=1<<n;affcounts[n]=weakcounts[n]=weakaffcounts[n]=0
    for m in range(1<<N):
        p=cache[n,m] if n<4 else profile(n,m);den=p['den'];roots+=1
        amin=affine_min(p);weak=all(4*x<=den for x in p['pn'])
        affcounts[n]+=amin;weakcounts[n]+=weak;weakaffcounts[n]+=amin and weak
        children=[];charrel=0;affrel=0
        for i in range(n):
            cp=[cache[n-1,child_mask(n,m,i,b)] for b in [0,1]];children.append(cp)
            tn=2*sum(c['I']-c['char'] for c in cp)
            an=2*sum(c['I']-c['aff'] for c in cp)
            ck(an>=tn>=0);charrel+=tn;affrel+=an
            form2=0;simp2=0
            for j in range(n):
                if i==j:continue
                co=sum(p['ws'][s]*p['ws'][s|1<<i] for s in range(N) if not s>>i&1 and s>>j&1)
                pj=p['pn'][j];jj=j if j<i else j-1
                ck(4*cp[0]['pn'][jj]==pj+2*co)
                ck(4*cp[1]['pn'][jj]==pj-2*co)
                ck(2*abs(co)<=pj)
                form2+=max(0,2*pj+4*co-den)+max(0,2*pj-4*co-den)
                simp2+=max(0,2*pj+4*abs(co)-den)
            ck(form2==2*tn)
            if all(2*x<=den for x in p['pn']):ck(simp2==2*tn)
            if weak:ck(tn==0)
        charpositive+=charrel>0
        if n<=3:
            deep(p,children);banks+=1
        if amin and weak and affrel>0 and len(witnesses)<8:
            # A proper child affine improvement with zero character release.
            ck(charrel==0)
            detail=deep(p,children);banks+=1
            witnesses.append({'n':n,'mask':m,'root':detail,'affine_release':str(Q(affrel,den)),'basis':p['basis'],'p':[str(Q(x,den)) for x in p['pn']],'children':[{'i':i,'b':b,'mask':c['m'],'I':str(Q(c['I'],c['den'])),'char':str(Q(c['char'],c['den'])),'aff':str(Q(c['aff'],c['den'])),'basis':c['basis']} for i,cp in enumerate(children) for b,c in enumerate(cp)]})
        assert time.perf_counter()-start<55
out={'status':'PASS','pilot':pilot,'roots':roots,'assertions':checks,'affine_minimal_counts':affcounts,'weak_counts':weakcounts,'weak_affine_counts':weakaffcounts,'positive_character_release_roots':charpositive,'bank_identity_roots':banks,'weak_affine_full_basis_witnesses':witnesses,'seconds':time.perf_counter()-start,'arithmetic':'integer Walsh/Fraction/canonical prime-log identities'}
(R/'out'/('PILOT.json' if pilot else 'CHECK.json')).write_text(json.dumps(out,indent=2),encoding='utf-8')
print(json.dumps({k:v for k,v in out.items() if k!='weak_affine_full_basis_witnesses'}))
print('witnesses',len(witnesses),[(w['n'],w['mask'],w['affine_release']) for w in witnesses])
