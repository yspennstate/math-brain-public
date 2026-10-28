from pathlib import Path
helper=Path(__file__).resolve().parents[2]/'20261026T205916Z-account04-A014-overlap-beyond-worst-case-read/code/check.py'
source=helper.read_text(encoding='utf-8')
exec(compile(source.split('direct=0;generic_atoms=0')[0],str(helper),'exec'))
from functools import lru_cache

@lru_cache(None)
def J(a,b):return F(factorial(a)*factorial(b),(a+b+1)**2*(a+b+2))

def masses(m,u,d,alpha,beta):
    F0=((alpha+beta)/32)**u*(alpha/48)**d
    F1=F(0)
    if u==0:F1+=(alpha/48)**d*beta*(F(m-d,16)+F(d,24))
    if u:
        z=sum((F(comb(u-1,k))*(alpha/32)**(u-1-k)*(beta/8)**k*J(k,0) for k in range(u)),F(0))
        F1+=u*(beta/24)*(alpha/48)**d*z
    if d:
        z=sum((F(comb(u,k))*(alpha/32)**(u-k)*(beta/8)**k*((beta/8)*J(k+1,0)+(alpha/8)*J(k,1)) for k in range(u+1)),F(0))
        F1+=2*d*(beta/24)*(alpha/48)**(d-1)*z
    return F0,F1

def weightings(n,edges):
    deg=[sum(j in e for e in edges) for j in range(n)]
    yield {e:F(1,max(deg)) for e in edges}
    yield {e:F(1,deg[e[0]]+deg[e[1]]) for e in edges}
    seed={e:j+1 for j,e in enumerate(edges)}
    scale=max(sum(v for e,v in seed.items() if j in e) for j in range(n))
    yield {e:F(v,scale) for e,v in seed.items()}

graphfixtures=0;graphatoms=0
for n in ([2,3] if PILOT else [2,3,4]):
    universe=list(combinations(range(n),2))
    for mask in range(1,1<<len(universe)):
        edges=[e for j,e in enumerate(universe) if mask>>j&1]
        for weights in weightings(n,edges):
            ck(all(sum((v for e,v in weights.items() if j in e),F(0))<=1 for j in range(n)))
            total=sum((raw({j for j in range(n) if a>>j&1},n,weights) for a in range(1<<n)),F(0))
            W=sum(weights.values());x=W/8
            # Positive exponential series is a rigorous LOWER bound for exp(x).
            exp_lower=sum((x**j/factorial(j) for j in range(21)),F(0))
            ck(total<=exp_lower);ck(total>=1);graphfixtures+=1;graphatoms+=1<<n

ck(raw(set(),2,{(0,1):F(0)})==1)
ck(sum((raw({j for j in range(2) if a>>j&1},2,{(0,1):F(0)}) for a in range(4)),F(0))==1)
# Missing row-feasibility is false: full selected star on64 leaves, all activities1.
bad=F(factorial(64),24*8**63*64**2*65)
ck(bad>3**8) # exp(W/8)=exp(8)<3^8 < this ONE atom.

windmillatoms=0;truthinputs=0;directtables=0
for m in ([1,2] if PILOT else [1,2,3,4]):
    n=2*m+1;edges=[e for j in range(m) for e in [(0,2*j+1),(0,2*j+2),(2*j+1,2*j+2)]]
    C=[int(not any((x>>u&1) and (x>>v&1) for u,v in edges)) for x in range(1<<n)]
    f=[1-2*x for x in C];fw=fwht(f);a=F(3,4)**m;b=F(1,4)**m;s=(a+b)/2;v=4*s*(1-s)
    I=(1+F(2*m,3))*a+(2*m-1)*b
    ck(F(sum(C),1<<n)==s)
    directI=F(sum(f[x]!=f[x^(1<<j)] for x in range(1<<n) for j in range(n)),1<<n)
    ck(directI==I);ck(F(sum(f[x]!=f[x^1] for x in range(1<<n)),1<<n)==a-b)
    for local in [False,True]:
        alpha=F(1,2) if local else F(1,2*m);beta=F(1,2*m)
        weights={e:beta if 0 in e else alpha for e in edges}
        ck(all(sum((w for e,w in weights.items() if j in e),F(0))<=1 for j in range(n)))
        total=F(0)
        for mask in range(1<<n):
            hub=mask&1;U={j for j in range(n) if mask>>j&1}
            u=sum(len(U&{2*j+1,2*j+2})==1 for j in range(m))
            d=sum({2*j+1,2*j+2}<=U for j in range(m))
            actual=raw(U,n,weights);closed=masses(m,u,d,alpha,beta)[hub]
            ck(actual==closed);total+=actual;windmillatoms+=1
            if mask:
                ahat=(-1)**d*F(3,4)**(m-u-d)*F(1,4)**(u+d)
                ck(F(fw[mask]**2,4**n)==(ahat+(-1)**hub*b)**2)
        ck(total>1)
    directtables+=1;truthinputs+=1<<n

rows=[];profilecount=0
for m in ([4,8] if PILOT else [4,8,12,16]):
    a=F(3,4)**m;b=F(1,4)**m;s=(a+b)/2;v=4*s*(1-s);I=(1+F(2*m,3))*a+(2*m-1)*b
    tables=[]
    for local in [False,True]:
        alpha=F(1,2) if local else F(1,2*m);beta=F(1,2*m);Z=F(0);profiles=[]
        for u in range(m+1):
            for d in range(m+1-u):
                mult=comb(m,u)*comb(m-u,d)*2**u
                ahat=(-1)**d*F(3,4)**(m-u-d)*F(1,4)**(u+d)
                for hub,Fvalue in enumerate(masses(m,u,d,alpha,beta)):
                    if not(hub or u or d):continue
                    p=(ahat+(-1)**hub*b)**2
                    ck(Fvalue>0);Z+=mult*Fvalue
                    profiles.append((u,d,hub,mult,p,Fvalue));profilecount+=1
        ck(sum(mult*p for u,d,h,mult,p,z in profiles)==v)
        ck(sum(mult*p*(u+2*d+h) for u,d,h,mult,p,z in profiles)==I)
        ck(sum(mult*p for u,d,h,mult,p,z in profiles if h)==a-b)
        v0=sum(mult*p for u,d,h,mult,p,z in profiles if not h)
        act0=sum(mult*p*(u+d) for u,d,h,mult,p,z in profiles if not h)
        ck(v0==a+3*b-(a+b)**2);ck(act0==F(m,4)*(a+5*b))
        low,high=entropy_binary(v)
        for u,d,hub,mult,p,z in profiles:
            ck(z<=Z)
            if p:
                lo,hi=lg(Z/z);low+=mult*p*lo;high+=mult*p*hi
            if local:
                base=F(1,64)**u*F(1,96)**d
                ck(z>=base/(48*m) if hub else z>=base)
        if local:
            W=F(m,2)+1
            exp_lower=sum(((W/8)**j/factorial(j) for j in range(41)),F(0))
            ck(1+Z<=exp_lower)
            kappa=(a-b)*lg(48*m)[1]/I
            ck(kappa<=3);ck(high<28*I);ck(high<=(F(1763,72)+kappa)*I)
        else:
            ck(Z>=F(3,32))
            bound=F(1,4)*lg(2*m)[0]+1-F(56,9*m)
            ck(low/I>=bound)
        tables.append({'activity':'local' if local else 'global','Z':str(Z),'CE_over_I_interval':[str(low/I),str(high/I)]})
    rows.append({'m':m,'tables':tables})

scalars=0
for m in range(4,257):
    a=F(3,4)**m;b=F(1,4)**m;v=2*(a+b)*(1-(a+b)/2);I=(1+F(2*m,3))*a+(2*m-1)*b
    ck(F(2*m,3)*a<=I<=m*a);ck(v/I<=F(82,27*m));ck(b/a<=F(1,81))
    ck(48*m<=2**(2*m));ck(m<=2**(F(m,2).__floor__()) if m%2==0 else m*m<=2**m)
    ck(F(m,8)+F(1,4)<=F(3*m,16));scalars+=1
ck(F(1,16)+F(8,147)==F(275,2352));ck(F(275,2352)<F(1,8))
ck(F(129,16)*F(82,27)==F(1763,72));ck(F(1763,72)+3<28)
out={'helper_version':'A014-fractional-normalizer-windmill-v1','mode':'pilot' if PILOT else 'main','graph_activity_fixtures':graphfixtures,'generic_graph_raw_atoms':graphatoms,'windmill_raw_atoms':windmillatoms,'direct_truth_tables':directtables,'actual_truth_inputs':truthinputs,'large_profiles':profilecount,'scalar_m_values':scalars,'assertions':CHECKS,'elapsed_seconds':time.monotonic()-START,'profiles':rows}
(RUN/'out'/('pilot.json' if PILOT else 'check.json')).write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8',newline='\n')
print(json.dumps({k:v for k,v in out.items() if k!='profiles'}))
