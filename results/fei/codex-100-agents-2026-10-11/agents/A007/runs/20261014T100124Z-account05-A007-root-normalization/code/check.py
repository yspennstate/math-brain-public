from pathlib import Path
from fractions import Fraction as Q
import itertools as it, math, json, time, argparse
ROOT=Path(__file__).resolve().parents[1]
AGENT=ROOT.parents[1]
ns={'__name__':'own_independent_helper'}
src=AGENT/'runs/20261013T220854Z-account05-A007-root-normalization/code/check_lift.py'
exec(compile(src.read_text(encoding='utf-8'),str(src),'exec'),ns)
start=time.perf_counter(); count={'assertions':0,'tables':0,'assignments':0,'old_forests':0,'occupation_cases':0,'tree_cases':0}
def chk(b):
    count['assertions']+=1
    assert b
    assert time.perf_counter()-start<60
def add(d,z,a):
    if a: d[z]=d.get(z,Q(0))+a
def times(a,b):
    d={}
    for z,x in a.items():
        for y,t in b.items(): add(d,z*y,x*t)
    return d
def plus(a,b):
    d=dict(a)
    for z,x in b.items(): add(d,z,x)
    return d
def conv(a,b,u):
    out=[{} for _ in range(u+1)]
    for i in range(len(a)):
        for j in range(len(b)):
            if i+j<=u: out[i+j]=plus(out[i+j],times(a[i],b[j]))
    return out
def components(owned,roots,groups):
    belong={a:a for a in roots}; todo=list(roots)
    while todo:
        a=todo.pop()
        for (l,j),vs in groups.items():
            if l==a:
                for v in vs: belong[v]=belong[a]; todo.append(v)
    chk(set(belong)==set(owned))
    return belong
def weight(sl,kap,u,v):
    return Q(sl+v,kap+u)**(sl+v)/Q(sl,kap)**sl
def coefficient(owned,tab,T,roots,belong,u):
    P=[{Q(1):Q(1)}]+[{} for _ in range(u)]; R=[{} for _ in range(u+1)]
    for l,js in owned.items():
        s=len(js); k=len(set(tab[l])&set(T))
        f=[{weight(s,k,u,v):Q(1,math.factorial(v))} for v in range(u+1)]
        d=[{z:a*v*Q(1,2**len(tab[belong[l]])) for z,a in f[v].items()} if v else {} for v in range(u+1)]
        R=[plus(x,y) for x,y in zip(conv(R,f,u),conv(P,d,u))]
        P=conv(P,f,u)
    c=len(roots)
    factor=math.factorial(u) if c==1 else math.factorial(u)*math.prod(range(u+1,u+c-1))/math.prod(Q(1,2**len(tab[a])) for a in roots)
    return {z:a*factor for z,a in (P[u] if c==1 else R[u]).items()}
def tree_counts(roots,belong,owners):
    # Enumerate rooted component trees, actual parent GATES and labelled-core attachment;
    # explicitly count every permutation of children sharing an attachment coordinate.
    m={a:0 for a in roots}; c=len(roots)
    if c==1: return {roots[0]:1}
    core_by_comp={a:[(j,l) for j,l in enumerate(owners) if belong[l]==a] for a in roots}
    for root in roots:
        children=[a for a in roots if a!=root]
        choices=[[(a,j,l) for a in roots if a!=v for j,l in core_by_comp[a]] for v in children]
        for data in it.product(*choices):
            par={v:a for v,(a,j,l) in zip(children,data)}; good=True
            for v in children:
                seen=set(); t=v
                while t!=root:
                    if t in seen: good=False; break
                    seen.add(t); t=par[t]
                if not good: break
            if not good: continue
            groups={}
            for v,(a,j,l) in zip(children,data): groups.setdefault((l,j),[]).append(v)
            for orders in it.product(*(it.permutations(vs) for vs in groups.values())):
                m[root]+=1
    return m
def record(owned,tab,T,roots,groups,us):
    V=tuple(owned); belong=components(owned,roots,groups); c=len(roots)
    for u in us:
        direct={}
        for owners in it.product(V,repeat=u):
            v={l:owners.count(l) for l in V}
            z=math.prod(weight(len(owned[l]),len(set(tab[l])&set(T)),u,v[l]) for l in V)
            if c==1: factor=Q(1)
            else:
                factor=math.prod(range(u+1,u+c-1))*sum(Q(1,2**len(tab[a]))*sum(v[l] for l in V if belong[l]==a) for a in roots)/math.prod(Q(1,2**len(tab[a])) for a in roots)
            add(direct,z,factor)
            if u<=2 and c<=3:
                m=tree_counts(roots,belong,owners)
                expected={a:1 if c==1 else sum(v[l] for l in V if belong[l]==a)*math.prod(range(u+1,u+c-1)) for a in roots}
                chk(m==expected); count['tree_cases']+=1
        chk(direct==coefficient(owned,tab,T,roots,belong,u)); count['occupation_cases']+=1
        if u==1:
            exact={}; A=math.prod(Q(len(set(tab[l])&set(T)),len(set(tab[l])&set(T))+1)**len(owned[l]) for l in V)
            for l in V:
                s=len(owned[l]); k=len(set(tab[l])&set(T))
                t=Q((s+1)**(s+1),s**s*(k+1))
                f=Q(1) if c==1 else math.factorial(c-1)*Q(1,2**len(tab[belong[l]]))/math.prod(Q(1,2**len(tab[a])) for a in roots)
                add(exact,A*t,f)
            chk(exact==direct)
def run(n,us):
    for tab in ns['tables'](n):
        count['tables']+=1
        truth=ns['truth'](tab,n); ft=ns['fwht'](truth)
        chk(sum(x*x for x in ft)==1<<(2*n))
        chk(Q(sum(i.bit_count()*x*x for i,x in enumerate(ft)),1<<(2*n))==ns['influence'](truth,n))
        covered=set().union(*map(set,tab))
        for T in ns['subsets'](n):
            if not set(T)<=covered: continue
            for owners in it.product(*[[l for l,R in enumerate(tab) if j in R] for j in T]):
                owned={}
                for j,l in zip(T,owners): owned.setdefault(l,[]).append(j)
                count['assignments']+=1
                rootsets,edges=ns['roots_and_graph'](owned,tab)
                for roots in rootsets:
                    events,_=ns['base_events'](owned,tab,roots,edges)
                    for groups,key in events:
                        count['old_forests']+=1
                        record(owned,tab,T,roots,groups,us)
def witness():
    tab=((0,1,4),(2,3,4,5)); T=(0,1,2); owned={0:(0,1),1:(2,)}
    rootsets,edges=ns['roots_and_graph'](owned,tab)
    chk(rootsets==[(0,1)] and not edges)
    truth=ns['truth'](tab,6); ft=ns['fwht'](truth)
    chk(Q(ft[7],64)==Q(-1,32)); chk(9**6<2**5*8**6)
    chk(512>243 and 4**11>9**6)
    D=(1+Q(1,16))*(1+Q(1,32))-1
    Dp=(1+Q(1,32))*(1+Q(1,64))-1
    chk(D==Q(49,512) and Dp==Q(97,2048) and Dp/(D/2)==Q(97,98))
    # Brute check exact prime table via every positive/negative ternary implicant.
    primes=[]
    for literals in it.product((-1,0,1),repeat=6):
        if not any(literals): continue
        def implicant(L):
            return all(truth[x]==1 for x in range(64) if all(t==0 or bool(x>>j&1)==(t==1) for j,t in enumerate(L)))
        if implicant(literals):
            if all(not implicant(literals[:j]+(0,)+literals[j+1:]) for j,t in enumerate(literals) if t): primes.append(literals)
    chk(set(primes)=={tuple(1 if j in R else 0 for j in range(6)) for R in tab})
    record(owned,tab,T,(0,1),{},[1,2,3])
    out={'supports':tab,'T':T,'owned':owned,'spectral_coefficient':'-1/32','pi':['1/8','1/16'],'false_root_average':'5/48','ratio_fifth_power_certificate':[9**6,2**5*8**6],'root_multiplier':'16*2^(-6/5)+8*(4/9)^(6/5)>8','signed_normalizer_ratio':'97/98','status':'EXACT_FACTORISATION_FALSIFIER_AND_ROOT_REFUND'}
    (ROOT/'out/WITNESS.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
if __name__=='__main__':
    ap=argparse.ArgumentParser(); ap.add_argument('--pilot',action='store_true'); a=ap.parse_args()
    witness()
    for n in ([2] if a.pilot else [2,3]): run(n,[1] if a.pilot else [1,2,3])
    out={'status':'PASS','helper_version':'A007-joint-occupation-v1','counts':count,'helper_assertions':ns['COUNTS']['assertions'],'elapsed_seconds':time.perf_counter()-start,'arithmetic':'Fraction formal positive rational powers; integer Walsh/prime census/signs','unpaid':'whole signed spectral expectation and inherited pR_g'}
    (ROOT/('out/PILOT.json' if a.pilot else 'out/EXACT_CHECK.json')).write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(out))
