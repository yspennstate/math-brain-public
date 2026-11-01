from fractions import Fraction as Q
from pathlib import Path
import hashlib,json,sys,time
start=time.perf_counter(); checks=0; nodes=0
def test(v):
    global checks
    checks+=1
    assert v, checks
    assert time.perf_counter()-start<55
def bitslog(v):
    test(v>0)
    a,b=v.numerator,v.denominator
    test(a&(a-1)==0 and b&(b-1)==0)
    return a.bit_length()-b.bit_length()
def D(p,q):
    return sum((a*bitslog(a/b) for a,b in zip(p,q) if a),Q(0))
def H(p):
    return sum((-a*bitslog(a) for a in p if a),Q(0))
def spectrum(table):
    N=len(table)
    return [Q(sum(a*(-1 if (x&t).bit_count()%2 else 1) for x,a in enumerate(table)),N) for t in range(N)]
def true_tables(k,L):
    n=2*k*L
    tabs=[[],[]]
    for a in range(1<<n):
        xy=[sum((a>>(j*L+t))&1 for t in range(L))%2 for j in range(2*k)]
        tabs[0].append((-1)**sum(xy[2*j]*xy[2*j+1] for j in range(k)))
        tabs[1].append((-1)**sum((1-xy[2*j])*xy[2*j+1] for j in range(k)))
    return tabs
def model(tabs):
    g,h=tabs;N=len(g)
    a=spectrum(g);b=spectrum(h)
    f=spectrum(g+h)
    p=[v*v for v in f]
    q=[(u*u+v*v)/4 for u,v in zip(a,b)]*2
    test(sum(p)==sum(q)==1)
    return f,p,q
def one(k,L):
    global nodes
    tabs=true_tables(k,L); N=len(tabs[0]); totals=[Q(0)]*4
    f,p,q=model(tabs)
    test(H(p)==2*k)
    test(sum(Q(i.bit_count())*v for i,v in enumerate(p))==L*k+Q(1,2))
    # Independent breadth-by-depth enumeration of all physical prefix assignments.
    for depth in range(2*k*L+1):
        local=[Q(0)]*4
        for hist in range(1<<depth):
            child_tabs=[[t[(i<<depth)|hist] for i in range(N>>depth)] for t in tabs]
            f,p,q=model(child_tabs);d=D(p,q)
            ds=[];es=[];hs=[]
            rem=len(f)//2
            for s in (0,1):
                if len(child_tabs[0])>1:
                    _,pp,qq=model([t[s::2] for t in child_tabs])
                else:
                    pp=qq=[Q(1)]
                measure=[]
                for t in range(rem):
                    a,b=f[2*t:2*t+2]
                    norm=a*a+b*b
                    measure.append((q[2*t]+q[2*t+1])*((a+(-1)**s*b)**2/(2*norm) if norm else Q(1,2)))
                rho=sum(measure);test(rho==Q(1,2))
                inherited=[a/rho for a in measure]
                ds.append(D(pp,qq));es.append(D(pp,inherited));hs.append(H(pp))
            raw=sum(ds)/2-sum(es)/2
            loss=d-sum(es)/2
            net=sum(ds)/2-d
            dh=H(p)-sum(hs)/2
            test(d in (0,1) and loss>=0)
            test(raw-loss==net)
            for j,v in enumerate((raw,loss,net,dh)):local[j]+=v
            nodes+=1
        for j,v in enumerate(local):totals[j]+=v/(1<<depth)
    test(totals==[k,k+1,-1,2*k])
    test(Q(3*k+1,L*k+Q(1,2))<3)
    return {'k':k,'L':L,'raw':str(totals[0]),'query_loss':str(totals[1]),'net':str(totals[2]),'entropy_drop':str(totals[3])}
domain=[(1,1)] if '--pilot' in sys.argv else [(1,1),(2,1),(1,2),(1,3)]
rows=[one(k,L) for k,L in domain]
out={'status':'PASS','rows':rows,'internal_nodes':nodes,'exact_predicates':checks,'elapsed_seconds':time.perf_counter()-start,'code_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
dest=Path(__file__).resolve().parents[1]/'out'/('INDEPENDENT_PILOT.json' if '--pilot' in sys.argv else 'INDEPENDENT.json')
dest.write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps(out))
