import argparse, hashlib, json, time
from fractions import Fraction as F
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
START = time.perf_counter()
CHECKS = 0
NODES = 0

def require(ok):
    global CHECKS
    CHECKS += 1
    assert ok, CHECKS
    assert time.perf_counter() - START < 55, 'frozen runtime guard'

def plus(*items):
    out = {}
    for z in items:
        for p, a in z.items():
            out[p] = out.get(p, F(0)) + a
    return {p:a for p,a in out.items() if a}

def scale(z, a):
    return {p:a*b for p,b in z.items() if a*b}

def logq(q):
    assert q > 0
    out = {}
    for v, sign in ((q.numerator,1),(q.denominator,-1)):
        p = 2
        while p*p <= v:
            while v % p == 0:
                out[p] = out.get(p,0) + sign
                v //= p
            p += 1
        if v > 1:
            out[v] = out.get(v,0) + sign
    return {p:F(a) for p,a in out.items() if a}

def kl(p,q):
    return plus(*(scale(logq(a/q[t]),a) for t,a in enumerate(p) if a))

def entropy(p):
    return plus(*(scale(logq(a),-a) for a in p if a))

def walsh(table):
    w = list(table)
    stride = 1
    while stride < len(w):
        for b in range(0,len(w),2*stride):
            for i in range(b,b+stride):
                a,c=w[i],w[i+stride]
                w[i],w[i+stride]=a+c,a-c
        stride *= 2
    return [F(a,len(w)) for a in w]

def restrict(table,s):
    return table[s::2]

def build(k,L):
    n=2*k*L
    gs=[[],[]]
    for x in range(1<<n):
        for source in (0,1):
            out=1
            for j in range(k):
                a=((x>>(2*j*L))&((1<<L)-1)).bit_count()%2
                b=((x>>((2*j+1)*L))&((1<<L)-1)).bit_count()%2
                out *= -1 if (a^source) and b else 1
            gs[source].append(out)
    return gs

def profile(gs, selector):
    # Remaining physical order: source data, then final selector bit.
    if not selector:
        w=walsh(gs[0]); p=[a*a for a in w]
        return w,p,p
    a,b=map(walsh,gs)
    w=[(x+y)/2 for x,y in zip(a,b)]+[(x-y)/2 for x,y in zip(a,b)]
    q=[(x*x+y*y)/4 for x,y in zip(a,b)]*2
    p=[x*x for x in w]
    require(sum(p)==1 and sum(q)==1)
    return w,p,q

def channel(w,q):
    refs=[[],[]]; ws=[[],[]]
    for t in range(len(w)//2):
        a,b=w[2*t],w[2*t+1]
        den=2*(a*a+b*b)
        for s in (0,1):
            v=a+((-1)**s)*b
            kernel=v*v/den if den else F(1,2)
            refs[s].append((q[2*t]+q[2*t+1])*kernel)
            ws[s].append(v)
    rho=[sum(r) for r in refs]
    require(sum(rho)==1 and all(r>0 for r in rho))
    return [[a/rho[s] for a in refs[s]] for s in (0,1)],rho,ws

def run(k,L):
    global NODES
    gs=build(k,L)
    sums={x:{} for x in ('raw','query','net','drop','outcome')}
    maxc=0
    rootw,rootp,rootq=profile(gs,True)
    require(entropy(rootp)=={2:F(2*k)})
    inf=sum(F(t.bit_count())*p for t,p in enumerate(rootp))
    require(inf==F(L*k)+F(1,2))
    def visit(gs,depth,weight):
        nonlocal maxc
        global NODES
        w,p,q=profile(gs,True)
        c=kl(p,q); h=entropy(p)
        completed=depth//L
        wantc=1 if completed%2==0 else 0
        require(c==({2:F(wantc)} if wantc else {}))
        maxc=max(maxc,wantc)
        NODES+=1
        refs,rho,cw=channel(w,q)
        incoming=[]; childc=[]; childh=[]
        remaining=(len(gs[0]).bit_length()-1)
        for s in (0,1):
            if remaining:
                child=[restrict(g,s) for g in gs]
                ww,pp,qq=profile(child,True)
            else:
                child=None
                # lowest remaining bit is now selector.
                ww=[F(gs[s][0])]; pp=[F(1)]; qq=[F(1)]
            require(ww==cw[s])
            require(sum(a*a for a in cw[s])==1)
            incoming.append(kl(pp,refs[s])); childc.append(kl(pp,qq)); childh.append(entropy(pp))
            if remaining:
                visit(child,depth+1,weight/2)
        avg=lambda zz:scale(plus(*zz),F(1,2))
        refund=plus(c,scale(avg(incoming),-1))
        raw=plus(avg(childc),scale(avg(incoming),-1))
        net=plus(avg(childc),scale(c,-1))
        drop=plus(h,scale(avg(childh),-1))
        outcome=kl([F(1,2),F(1,2)],rho)
        is_x_pulse=remaining>0 and completed%2==0 and depth%L==L-1
        is_y_pulse=remaining>0 and completed%2==1 and depth%L==L-1
        final=remaining==0
        require(refund==({2:F(1)} if is_x_pulse or final else {}))
        require(raw==({2:F(1)} if is_y_pulse else {}))
        require(drop==({2:F(2)} if is_y_pulse else {}))
        require(outcome=={})
        require(plus(raw,scale(refund,-1))==net)
        for name,val in [('raw',raw),('query',refund),('net',net),('drop',drop),('outcome',outcome)]:
            sums[name]=plus(sums[name],scale(val,weight))
    visit(gs,0,F(1))
    expected={'raw':k,'query':k+1,'net':-1,'drop':2*k,'outcome':0}
    for key,v in expected.items():
        require(sums[key]==({2:F(v)} if v else {}))
    require(plus(entropy(rootp),kl(rootp,rootq),sums['raw'])=={2:F(3*k+1)})
    return {'k':k,'L':L,'physical_n':2*k*L+1,'H':2*k,'I':str(inf),'max_current_KL':maxc,
            'raw_replacements':k,'query_KL_contractions':k+1,'net_replacements':-1,
            'endpoint_functional':2*k,'raw_transaction':3*k+1,'all_physical_outcomes_checked':True}

parser=argparse.ArgumentParser();parser.add_argument('--pilot',action='store_true');args=parser.parse_args()
domain=[(1,1)] if args.pilot else [(1,1),(2,1),(3,1),(1,2),(1,3),(2,2)]
rows=[run(k,L) for k,L in domain]
out={'status':'PASS','domain':rows,'internal_nodes':NODES,'exact_predicates':CHECKS,
     'elapsed_seconds':time.perf_counter()-START,'code_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
dest=ROOT/'out'/('PILOT.json' if args.pilot else 'VALIDATION.json')
dest.write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps(out))
