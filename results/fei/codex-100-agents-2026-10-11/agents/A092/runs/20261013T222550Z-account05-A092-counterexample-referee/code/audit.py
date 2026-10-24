from fractions import Fraction as Q
from functools import lru_cache
from pathlib import Path
import json,time,sys
ROOT=Path(__file__).resolve().parents[1]
START=time.perf_counter(); ASSERTIONS=0
def check(x):
    global ASSERTIONS
    ASSERTIONS+=1
    if not x:raise AssertionError(ASSERTIONS)
def save(name,x):(ROOT/'out'/name).write_text(json.dumps(x,indent=2)+'\n',encoding='utf-8')
def guard():check(time.perf_counter()-START<120)
@lru_cache(None)
def factors(n):
    d=2;result={}
    while d*d<=n:
        while n%d==0:result[d]=result.get(d,0)+1;n//=d
        d+=1
    if n>1:result[n]=result.get(n,0)+1
    return result
def add(*args):
    r={}
    for a in args:
        for p,c in a.items():r[p]=r.get(p,Q(0))+c
    return {p:c for p,c in r.items() if c}
def mul(a,c):return {p:v*c for p,v in a.items() if v*c}
def sub(a,b):return add(a,mul(b,-1))
@lru_cache(None)
def H(law):
    check(sum(law)==1 and min(law)>=0)
    r={}
    for x in law:
        if not x:continue
        for p,e in factors(x.numerator).items():r[p]=r.get(p,Q(0))-x*e
        for p,e in factors(x.denominator).items():r[p]=r.get(p,Q(0))+x*e
    return {p:c for p,c in r.items() if c}
def hb(p):return H((p,1-p))
@lru_cache(None)
def stats(table,ps):
    n=len(ps);vals=list(map(Q,table));N=len(vals)
    for i,p in enumerate(ps):
        for s in range(N):
            if s>>i&1:continue
            a,b=vals[s],vals[s|(1<<i)];vals[s]=(1-p)*a+p*b;vals[s|(1<<i)]=b-a
    law=[]
    for s,c in enumerate(vals):
        mass=c*c
        for i,p in enumerate(ps):
            if s>>i&1:mass*=p*(1-p)
        law.append(mass)
    weights=[]
    for x in range(N):
        w=Q(1)
        for i,p in enumerate(ps):w*=p if x>>i&1 else 1-p
        weights.append(w)
    prob=sum(w for w,v in zip(weights,table) if v==-1)
    inf=tuple(sum(w for x,w in enumerate(weights) if table[x]!=table[x^(1<<i)]) for i in range(n))
    check(sum(law)==1)
    return tuple(law),prob,inf
def child(table,i,b):
    return tuple(table[(x&((1<<i)-1))|((x>>i)<<(i+1))|(b<<i)] for x in range(len(table)//2))
@lru_cache(None)
def ln_unit(x):
    z=(x-1)/(x+1);power=z;v=Q(0)
    for j in range(96):v+=2*power/(2*j+1);power*=z*z
    return v,v+2*power/(193*(1-z*z))
@lru_cache(None)
def log2(x):
    check(x>0)
    if Q(1,2)<=x<1:
        a,b=log2(1/x);return -b,-a
    k=0
    while x<1:x*=2;k-=1
    while x>=2:x/=2;k+=1
    a,b=ln_unit(x);c,d=ln_unit(Q(2));return k+a/d,k+b/c
def interval(v):
    lo=hi=Q(0)
    for p,c in v.items():
        a,b=log2(Q(p))
        lo+=c*(a if c>=0 else b);hi+=c*(b if c>=0 else a)
    return lo,hi
def iscale(a,c):return (a[0]*c,a[1]*c) if c>=0 else (a[1]*c,a[0]*c)
def iadd(*args):return sum(a[0] for a in args),sum(a[1] for a in args)
def entropy_interval(law):
    return iadd(*(iscale(log2(p),-p) for p in law if p))
def outward(a,bits=512):
    den=1<<bits
    return [str(Q(a[0].numerator*den//a[0].denominator,den)),str(Q(-((-a[1].numerator*den)//a[1].denominator),den))]

def tree(table,ps,policy):
    initial=stats(table,ps);sums={'M':{},'J':{},'h':{},'j':{},'c':{},'leafH':{},'leafY':{}};leaves=[];nodes=[];removed=Q(0)
    def walk(t,p,labels,w,path):
        nonlocal removed
        law,neg,inf=stats(t,p);active=[i for i,d in enumerate(inf) if d]
        stop=not active or (policy=='partial' and len(path)>=1)
        if stop:
            leaves.append((path,w,neg));sums['leafH']=add(sums['leafH'],mul(H(law),w));sums['leafY']=add(sums['leafY'],mul(hb(neg),w));return
        i=active[-1] if policy=='reverse' else (max(active,key=lambda j:(inf[j],-j)) if policy=='max' else active[0])
        pp=p[i];rest=p[:i]+p[i+1:];remain=labels[:i]+labels[i+1:]
        ts=[child(t,i,b) for b in [0,1]];ss=[stats(c,rest) for c in ts]
        marginal=tuple(law[x&((1<<i)-1)|((x>>i)<<(i+1))]+law[(x&((1<<i)-1)|((x>>i)<<(i+1)))|(1<<i)] for x in range(len(law)//2))
        check(all(q==(1-pp)*ss[0][0][x]+pp*ss[1][0][x] for x,q in enumerate(marginal)))
        M=sub(H(law),H(marginal));J=sub(H(marginal),add(mul(H(ss[0][0]),1-pp),mul(H(ss[1][0]),pp)))
        j=sub(hb(neg),add(mul(hb(ss[0][1]),1-pp),mul(hb(ss[1][1]),pp)));c=sub(hb(pp),j)
        for key,v in [('M',M),('J',J),('h',hb(pp)),('j',j),('c',c)]:sums[key]=add(sums[key],mul(v,w))
        removed+=w*inf[i]
        nodes.append((path,labels,i,marginal,ss,pp))
        for b,ww in [(0,1-pp),(1,pp)]:walk(ts[b],rest,remain,w*ww,path+((labels[i],b),))
    walk(table,ps,tuple(range(len(ps))),Q(1),())
    ht=H(tuple(w for path,w,y in leaves));hy=hb(initial[1])
    joint=H(tuple(q for path,w,y in leaves for q in [w*y,w*(1-y)] if q))
    bank=sub(joint,hy);iy=sub(add(ht,hy),joint)
    check(ht==sums['h']);check(bank==sums['c']);check(iy==sums['j']);check(iy==sub(hy,sums['leafY']))
    check(H(initial[0])==add(sums['leafH'],sums['M'],sums['J']))
    S=add(mul(sums['h'],Q(1,2)),sub(sums['M'],sums['J']))
    check(H(initial[0])==add(sums['leafH'],mul(sums['M'],2),mul(bank,Q(1,2)),mul(iy,Q(1,2)),mul(S,-1)))
    leaf_inf=Q(0)
    # Influence telescope independently by recovering each leaf restriction from its physical path.
    for path,w,y in leaves:
        tt=table;pp=ps;labels=list(range(len(ps)))
        for label,b in path:
            i=labels.index(label);tt=child(tt,i,b);pp=pp[:i]+pp[i+1:];labels.pop(i)
        leaf_inf+=w*sum(stats(tt,pp)[2])
    check(removed==sum(initial[2])-leaf_inf)
    # Root-output Efron-Stein bound: signs enclosed or exact rational prime-log cancellation.
    slack=sub(add(*(mul(hb(p),d) for p,d in zip(ps,initial[2]))),hy)
    if slack:check(interval(slack)[0]>=0)
    conversion=None
    if all(p==Q(1,2) for p in ps):
        records=[]
        node_map={x[0]:x for x in nodes}
        for rootS,mass in enumerate(initial[0]):
            if not mass:continue
            def lift(path,w):
                if path not in node_map:records.append((rootS,path,w));return
                _,labels,i,marginal,ss,pp=node_map[path];remain=labels[:i]+labels[i+1:]
                T=sum(((rootS>>a)&1)<<j for j,a in enumerate(remain));q=marginal[T]
                check(q>0)
                for b in [0,1]:
                    branch=(1-pp if b==0 else pp)*ss[b][0][T]/q
                    if branch:lift(path+((labels[i],b),),w*branch)
            lift((),mass)
        joint_lift=H(tuple(w for S,path,w in records))
        for path,w,y in leaves:check(sum(v for s,h,v in records if h==path)==w)
        info=sub(add(H(initial[0]),ht),joint_lift);spectral_bank=sub(joint_lift,H(initial[0]))
        check(info==sums['J'])
        conversion=sub(bank,spectral_bank);check(conversion==sub(sums['J'],iy))
        check(sub(H(initial[0]),info)==add(sums['M'],sums['leafH']))
        if info:
            check(interval(info)[0]>=0)
            _,ln2_hi=ln_unit(Q(2))
            check(interval(info)[1]<=2*removed/ln2_hi)
    return {'bank':bank,'conversion':conversion,'info_output':iy,'J':sums['J'],'removed':removed,'I':sum(initial[2]),'leafH':sums['leafH'],'leaves':len(leaves)}

def underrefund():
    q=1-(Q(2**128-1,2**128))**2;s=Q(1,2**129);lam=Q(49,100)
    scalar=iadd(entropy_interval((q,1-q)),iscale(entropy_interval((s,1-s)),-2))
    total=1+q+q*q+q**3
    bank=iadd(iscale(entropy_interval((q,1-q)),total),iscale(entropy_interval((q**4,1-q**4)),-1))
    net=iadd(iscale(scalar,total),iscale(bank,-lam));influence=4*q**3
    check(net[0]>influence)
    # Recover all physical weights and all Fourier squares from the original table.
    t=tuple(-1 if x==15 else 1 for x in range(16));law,neg,inf=stats(t,(q,)*4)
    check(neg==q**4 and sum(inf)==influence)
    row={'q':str(q),'symmetric_angle_small_mass':str(s),'lambda':str(lam),'truth_table':t,'physical_I':str(influence),'net_tax_lower_bound_interval':outward(net),'net_gt_I':True,'spectrum':list(map(str,law)),'spectrum_sha256':__import__('hashlib').sha256(json.dumps(list(map(str,law))).encode()).hexdigest()}
    save('UNDERREFUND.json',row)
    return row

def main():
    pilot='--pilot' in sys.argv;underrefund();roots=trees=0;controls=[]
    for n in range(3 if pilot else 4):
        for mask in range(1<<(1<<n)):
            guard();t=tuple(1-2*((mask>>x)&1) for x in range(1<<n))
            for ps in [(Q(1,2),)*n,(Q(1,8),Q(1,4),Q(3,8))[:n]]:
                roots+=1
                for policy in ['forward','reverse','max','partial']:
                    v=tree(t,ps,policy);trees+=1
        save('PILOT_COUNTS.json' if pilot else 'COUNTS.json',{'completed_n':n,'roots':roots,'trees':trees,'assertions':ASSERTIONS})
    for name,t in [('character',(1,-1)),('AND',(1,1,1,-1))]:
        v=tree(t,(Q(1,2),)*(len(t).bit_length()-1),'forward');controls.append({'name':name,'conversion':{str(k):str(c) for k,c in v['conversion'].items()},'interval':outward(interval(v['conversion']))})
    if not pilot:
        for kind in range(3):
            t=[]
            for x in range(32):
                z,a,b,u,v=[(x>>i)&1 for i in range(5)]
                g=(-1)**u if kind!=1 else -1;h=(-1)**v if kind!=2 else -(-1)**v
                t.append(g if z and a else (h if z and b else 1))
            for policy in ['forward','reverse','max','partial']:
                r=tree(tuple(t),(Q(1,2),)*5,policy);trees+=1
                controls.append({'name':'priority_shared_control_'+str(kind),'policy':policy,'truth_table':t,'I':str(r['I']),'I_removed':str(r['removed']),'terminal_H_vector':{str(k):str(c) for k,c in r['leafH'].items()},'conversion_vector':{str(k):str(c) for k,c in r['conversion'].items()},'conversion_interval':outward(interval(r['conversion']))})
                save('SHARED_CONTROL.json',controls)
    save('CONTROLS.json',controls)
    result={'status':'PASS','pilot':pilot,'roots':roots,'trees':trees,'assertions':ASSERTIONS,'runtime_seconds':time.perf_counter()-START,'arithmetic':'exact Fraction laws; prime-log identity vectors; reciprocal-stabilized 96-term rational logarithm certificates','source_theorem':'A050-OUTPUT-CONDITIONAL-TAX-REPAIR@1','sharp_scalar_optimizer_used':False}
    save('PILOT.json' if pilot else 'RESULT.json',result);print(json.dumps(result))
if __name__=='__main__':main()
