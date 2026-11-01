import a091_math as m
from a091_math import Q,add,entropy,logform,interval,nonnegative,check
from pathlib import Path
from functools import lru_cache
import json,time,sys,math
ROOT=Path(__file__).resolve().parents[1]; START=time.perf_counter()
def S(t):return m.spec(t,(Q(1,2),)*((len(t)-1).bit_length()))[1]
def Phi(a,b):return add((-a,logform(a)) if a else (0,{}),(-b,logform(b)) if b else (0,{}),(a+b,logform(a+b)) if a+b else (0,{}))
def erasure(P,i):
    q=[Q(0)]*(len(P)//2)
    for s,v in enumerate(P):q[(s&((1<<i)-1))|((s>>(i+1))<<i)]+=v
    return add((1,entropy(P)),(-1,entropy(tuple(q))))
def bounds(d):return interval(d)
def summ(a,b):return m.plus(a,b)
def scaled(c,a):return m.scale(c,a)
def sub(a,b):return summ(a,scaled(-1,b))
def div(a,b):
    assert b[0]>0
    z=[x/y for x in a for y in b];return m.mesh((min(z),max(z)))
e0=sum(Q(1,math.factorial(j)) for j in range(33)); ei=(e0,e0+Q(1,math.factorial(33))/(1-Q(1,34)))
ci=div((Q(1),Q(1)),m.LN2); c0i=div((Q(2),Q(2)),(ei[0]*m.LN2[0],ei[1]*m.LN2[1])); Ki=summ((Q(4),Q(4)),c0i)
@lru_cache(None)
def activation(t,r):
    return tuple(t[x>>r] if (x&((1<<r)-1))==0 else 1 for x in range(len(t)*(1<<r)))
@lru_cache(None)
def coretree(t,r,rule,cut,depth=0):
    P=S(t); n=(len(t)-1).bit_length();p=Q(1,1<<r)
    if n==0 or len(set(t))==1 or (cut>=0 and depth>=cut):
        return {'cap':(Q(0),Q(0)),'pi':Q(0),'t':Q(0),'Vleaf':m.var(P),'suffix':{},'inner':{},'terminal':entropy(S(activation(t,r))) if cut>=0 else {},'leaves':[(Q(1),t)]}
    ds=[sum(v for s,v in enumerate(P) if s>>i&1) for i in range(n)]
    i=0 if rule==0 else n-1 if rule==1 else max(range(n),key=lambda j:ds[j])
    mean=Q(sum(t),len(t));raw,_=m.spec(t,(Q(1,2),)*n);beta=raw[1<<i]/Q(1,2);t0=beta*beta;v=m.var(P);d=ds[i]
    def M(z):return add((1,Phi((1-p+p*mean)**2,p*p*z)),(p*(1-p),Phi((1-mean)**2,z)))
    zero=(Q(0),Q(0))
    cap=zero if not t0 or not v else tuple(min(x,y) for x,y in zip(bounds(M(v)),bounds(add((t0/v,M(v)),(p*t0,logform(v/t0))))))
    parent=S(activation(t,r));check(erasure(parent,r+i),add((p,erasure(P,i)),(-p,Phi(mean*mean,t0)),(1,M(t0))))
    nonnegative(add((1,M(v)),(-1,M(t0))))
    children=[m.restrict(t,[i],b)[0] for b in range(2)]
    subs=[coretree(c,r,rule,cut,depth+1) for c in children]
    out={'cap':summ(cap,scaled(Q(1,2),summ(subs[0]['cap'],subs[1]['cap']))),'pi':d+sum(z['pi'] for z in subs)/2,'t':t0+sum(z['t'] for z in subs)/2,'Vleaf':sum(z['Vleaf'] for z in subs)/2,'inner':add((1,erasure(P,i)),(-1,Phi(mean*mean,t0)),*[(Q(1,2),z['inner']) for z in subs]),'terminal':add(*[(Q(1,2),z['terminal']) for z in subs]),'leaves':[(w/2,c) for z in subs for w,c in z['leaves']]}
    check(m.var(P)-out['Vleaf'],out['t'])
    return out
@lru_cache(None)
def pointtail(r):
    if not r:return {},Q(0)
    t=tuple(-1 if x==0 else 1 for x in range(1<<r)); P=S(t)
    local=erasure(P,0);d=Q(1,1<<(r-1));nonnegative(add((3*d,logform(Q(2))),(-1,local)))
    b,i=pointtail(r-1);return add((1,local),(Q(1,2),b)),d+i/2
def certificate(t,r,rule,cut):
    P=S(t);p=Q(1,1<<r);a=1-Q(sum(t),len(t)); z=coretree(t,r,rule,cut)
    Ip=m.inf(S(activation(t,r)));check(Ip,p*m.inf(P)+r*p*a)
    check(m.var(P)-z['Vleaf'],z['t'])
    upper=summ(scaled(z['pi'],summ((4*p*(1-p),)*2,summ(scaled(p*p,ci),scaled(p,c0i)))),(2*r*p*p*z['t'],)*2)
    assert z['cap'][1]<=upper[0] or (z['cap']==(0,0) and upper==(0,0))
    if cut<0:
        check(z['pi'],m.inf(P));check(z['Vleaf'],Q(0))
        tail,tailI=pointtail(r); suffix=add((a/2,tail));check(a/2*tailI,r*p*a)
        total=summ(z['cap'],bounds(suffix)); budget=summ(scaled(p*m.inf(P),Ki),(5*r*p*a,)*2)
        assert total[1]<=budget[0] or total==budget==(0,0)
        assert budget[1]<=scaled(Ip,Ki)[1] or not Ip
    return z

def physical_tree(t,labels,order,stop_after=None,depth=0):
    P=S(t);n=len(labels)
    choices=[j for j in order if j in labels]
    if not choices or len(set(t))==1 or (stop_after is not None and depth>=stop_after):
        return {'Hleaf':entropy(P),'Ileaf':m.inf(P),'spent':Q(0),'M':{},'J':{},'L':{},'leaves':[(Q(1),t,labels)],'nodes':0}
    label=choices[0]; i=labels.index(label)
    kids,L,M,J,tax,IA,spent,norm=m.experiment(t,(Q(1,2),)*n,[i])
    nextlabels=tuple(j for j in labels if j!=label)
    subs=[physical_tree(child,nextlabels,order,stop_after,depth+1) for _,child,_,_ in kids]
    out={k:add(*[(Q(1,2),z[k]) for z in subs]) for k in ['Hleaf','M','J','L']}
    for k,v in [('M',M),('J',J),('L',L)]:out[k]=add((1,v),(1,out[k]))
    out['Ileaf']=sum(z['Ileaf'] for z in subs)/2;out['spent']=IA+sum(z['spent'] for z in subs)/2
    out['leaves']=[(w/2,c,ls) for z in subs for w,c,ls in z['leaves']];out['nodes']=1+sum(z['nodes'] for z in subs)
    check(m.inf(P),out['spent']+out['Ileaf']);check(entropy(P),add((1,out['Hleaf']),(1,out['L'])))
    return out

def lift(t,order,stop_after=None):
    P=S(t); n=(len(t)-1).bit_length();joint=[]
    def go(child,labels,mass,depth):
        reach=sum(mass); PP=S(child)
        current=[Q(0)]*len(PP)
        for s,w in enumerate(mass):current[m.compressed(s,labels)]+=w
        for a,b in zip(current,PP):check(a,reach*b)
        choices=[j for j in order if j in labels]
        if not choices or len(set(child))==1 or (stop_after is not None and depth>=stop_after):joint.append(tuple(mass));return
        i=labels.index(choices[0]);nextlabels=tuple(j for j in labels if j!=choices[0]); qq=[Q(0)]*(len(PP)//2)
        for s,w in enumerate(PP):qq[m.compressed(s,[j for j in range(len(labels)) if j!=i])]+=w
        for b in range(2):
            ch=m.restrict(child,[i],b)[0];C=S(ch)
            nextmass=[]
            for s,w in enumerate(mass):
                T=m.compressed(s,nextlabels);nextmass.append(w*C[T]/(2*qq[T]) if qq[T] else Q(0))
            check(sum(nextmass),reach/2);go(ch,nextlabels,nextmass,depth+1)
    go(t,tuple(range(n)),list(P),0)
    for s in range(len(P)):check(sum(row[s] for row in joint),P[s])
    HP=entropy(tuple(sum(row) for row in joint));HScond=add((1,entropy(tuple(w for row in joint for w in row))),(-1,entropy(P)))
    return HP,HScond

def shared(u,v,r,s,orient):
    n=1+r+s+2
    def value(x):
        c=x&1;A=((x>>1)&((1<<r)-1))==0;B=((x>>(1+r))&((1<<s)-1))==0
        return u[(x>>(1+r+s))&1] if c==0 and A else v[(x>>(2+r+s))&1] if c==orient and B else 1
    return tuple(value(x) for x in range(1<<n))
def overlap_case(u,v,r,s,orient):
    t=shared(u,v,r,s,orient);n=1+r+s+2;p=Q(1,1<<r);q=Q(1,1<<s)
    w1=p/2;w2=q*(1-p)/2 if orient==0 else q/2
    dataI=w1*m.inf(S(u))+w2*m.inf(S(v));terminal=add((w1,entropy(S(u))),(w2,entropy(S(v))))
    controls=tuple(range(1+r+s)); rows=[]
    for rule in range(3):
        order=controls if rule!=1 else (0,)+tuple(range(1+r,1+r+s))+tuple(range(1,1+r))
        cut=1 if rule==2 else None;z=physical_tree(t,tuple(range(n)),order,cut)
        if cut is None:check(z['Hleaf'],terminal);check(z['Ileaf'],dataI)
        HP,HScond=lift(t,order,cut)
        check(add((1,HP),(-1,HScond)),z['J'])
        Houtput=entropy((Q(t.count(1),len(t)),Q(t.count(-1),len(t))))
        EHout=add(*[(w,entropy((Q(c.count(1),len(c)),Q(c.count(-1),len(c))))) for w,c,_ in z['leaves']])
        IY=add((1,Houtput),(-1,EHout));HYcond=add((1,HP),(-1,IY))
        gap=add((1,HYcond),(-1,HScond));check(gap,add((1,z['J']),(-1,IY)))
        # A050's allocation-free complete residual, retaining partial leaves.
        slack=add((len([]),{}),(Q(1,2),HP),(-1,z['J']),(1,z['M']))
        check(entropy(S(t)),add((1,z['Hleaf']),(2,z['M']),(Q(1,2),HYcond),(Q(1,2),IY),(-1,slack)))
        rows.append({'orient':orient,'widths':[r,s],'u':u,'v':v,'rule':rule,'exclusive_control_influence':str(z['spent']),'terminal_influence':str(z['Ileaf']),'bank_conversion_bits':[str(x) for x in bounds(gap)],'terminal_entropy_prime_log':{str(k):str(x) for k,x in z['Hleaf'].items()}})
    return rows

def main():
    pilot='--pilot' in sys.argv;cases=trees=0;over=[]
    ns=range(3) if pilot else range(4);rs=[1] if pilot else [1,2,3]
    for n in ns:
        for mask in range(1<<(1<<n)):
            t=m.tab(mask,n)
            for r in rs:
                cases+=1
                for rule,cut in [(0,-1),(1,-1),(2,-1),(0,1)]:certificate(t,r,rule,cut);trees+=1
            if time.perf_counter()-START>110:raise RuntimeError('frozen main watchdog')
    cores=[m.tab(mask,1) for mask in range(4)]
    pairs=[(cores[0],cores[3]),(cores[1],cores[2])] if pilot else [(u,v) for u in cores for v in cores]
    for u,v in pairs:
        for r,s in ([(1,1)] if pilot else [(1,1),(1,2),(2,1),(2,2)]):
            for orient in [0,1]:over+=overlap_case(u,v,r,s,orient)
    output={'status':'PASS','activation_roots':cases,'activation_tree_checks':trees,'shared_tree_checks':len(over),'exact_assertions':m.COUNT,'K_rational_interval':[str(x) for x in Ki],'runtime_seconds':time.perf_counter()-START,'shared_rows':over,'scope':'A057 cap payment reviewed; shared rows certify exact ledger and common-space bank conversion only, not overlapping-cap payment.'}
    path=ROOT/'out'/('PILOT.json' if pilot else 'CHECK.json');path.write_text(json.dumps(output,indent=2)+'\n');print(json.dumps({k:v for k,v in output.items() if k!='shared_rows'}))
if __name__=='__main__':main()
