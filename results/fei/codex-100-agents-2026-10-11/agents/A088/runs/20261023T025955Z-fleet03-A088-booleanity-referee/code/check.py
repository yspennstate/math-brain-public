import sys,time,json,hashlib
from pathlib import Path
from fractions import Fraction as F
from functools import lru_cache
R=Path(__file__).resolve().parents[1]
MODE=sys.argv[1] if len(sys.argv)>1 else 'pilot'
START=time.perf_counter(); CHECKS=0
def ck(v,s):
    global CHECKS
    CHECKS+=1
    if not v: raise AssertionError(s)
    if time.perf_counter()-START > (55 if MODE=='pilot' else 180): raise TimeoutError(s)
@lru_cache(None)
def ln(x):
    z=(x-1)/(x+1); assert 0<=z<=F(1,3)
    v=2*sum((z**(2*i+1)/(2*i+1) for i in range(28)),F())
    return v,v+2*z**57/(57*(1-z*z))
@lru_cache(None)
def log(x):
    x=F(x);k=0
    while x<1: x*=2;k-=1
    while x>=2: x/=2;k+=1
    a,b=ln(x);c,d=ln(F(2))
    lo=F(k)+a/d;hi=F(k)+b/c;dd=1<<90
    return F(lo.numerator*dd//lo.denominator,dd), F(-((-hi.numerator*dd)//hi.denominator),dd)
def add(x,y):return x[0]+y[0],x[1]+y[1]
def scale(x,k):return (x[0]*k,x[1]*k) if k>=0 else (x[1]*k,x[0]*k)
def sub(x,y):return add(x,scale(y,-1))
def exact(x):return F(x),F(x)
def contains0(x):return x[0]<=0<=x[1]
def enc(x):return {'lo':str(x[0]),'hi':str(x[1]),'approx':float((x[0]+x[1])/2)}
def ce(terms):
    out=exact(0)
    for p,q,mult in terms:
        if p:out=add(out,scale(log(1/q),p*mult))
    # Outward rounding keeps later denominators small.
    d=1<<90
    return F(out[0].numerator*d//out[0].denominator,d), F(-((-out[1].numerator*d)//out[1].denominator),d)
def entropy(p):return ce([(v,v,1) for v in p if v])
def cross(p,q):return ce([(v,w,1) for v,w in zip(p,q) if v])
def walsh(v):
    v=list(v);h=1
    while h<len(v):
        for i in range(0,len(v),2*h):
            for j in range(i,i+h):v[j],v[j+h]=v[j]+v[j+h],v[j]-v[j+h]
        h*=2
    return [F(a,len(v)) for a in v]
def law(v):return [x*x for x in walsh(v)]
def edges(v,j):return F(sum(v[x]!=v[x^(1<<j)] for x in range(len(v))),len(v))
def totalI(v):return sum((edges(v,j) for j in range((len(v)-1).bit_length())),F())
def project(v,j):
    out=[F() for _ in range(len(v)//2)]
    for x,p in enumerate(v):out[(x&((1<<j)-1))|((x>>(j+1))<<j)]+=p
    return out
def child(v,j,b):return [a for x,a in enumerate(v) if ((x>>j)&1)==b]
def base(m,x):return (-1)**sum(((x>>(2*j))&1)*((x>>(2*j+1))&1) for j in range(m))
def canonical(m):return [base(m,x)-2*(x==0) for x in range(1<<(2*m+1))]
def sign(m,label):return base(m,label)
def formulas(m,t,remaining,label):
    A=F(1,1<<m);delta=A*A/2
    old=sum(((label>>j)&1)<<i for j,i in enumerate(remaining))
    W=bool(old&(1<<(2*m)));J=any(old&(1<<(2*j+1)) for j in range(t))
    sig=sign(m,old)
    q=(1<<t)*((0 if W else A*A)+A**4-(0 if W or J else 2*A**3*sig))
    p=((0 if W or J else (1<<t)*A*sig)-(1<<t)*A*A)**2
    ratio=F(1<<t) if W or not J else F(1<<t)*A*A/(1+A*A)
    return p,q,ratio
literal=[]
for m in ([2] if MODE=='pilot' else range(2,6)):
    v=canonical(m); q=law(v);remaining=list(range(2*m+1));A=F(1,1<<m);delta=A*A/2
    for t in range(m+1):
        p=law(v);ck(sum(p)==sum(q)==1,'literal normalization')
        ck(all(a in (-1,1) for a in v),'Boolean restriction')
        ck(totalI(v)==m-t+2*(2*m+1-t)*(1<<t)*delta,'physical marked edges')
        for s in range(len(p)):
            pp,qq,rr=formulas(m,t,remaining,s)
            ck((p[s],q[s])==(pp,qq),'direct Walsh vs independent grouped formula')
            ck(p[s]==rr*q[s],'likelihood formula')
        if t<m:
            j=remaining.index(2*t); p0=law(child(v,j,0));p1=law(child(v,j,1));qn=project(q,j);pn=project(p,j)
            for s in range(len(p0)):
                ck((p0[s]+p1[s])/2==pn[s],'both actual children mean')
            for s in range(len(p)):
                u=s^(1<<j)
                ck(p[s]*(q[s]+q[u])==q[s]*(p[s]+p[u]),'conditional equality')
            ck(edges(v,j)==F(1,2)+2*(1<<t)*delta,'actual intact influence')
            e=sub(sub(cross(p,q),scale(add(cross(p0,qn),cross(p1,qn)),F(1,2))),exact(2*edges(v,j)))
            ck(e[1]<=-4*(1<<t)*delta,'negative intact debit')
            # Full original-reference clean exit, including potentially negative bank.
            exit_ce=cross(p1,qn)
            expected=sub(exact(2*m-t-1),log(1+A*A))
            ck(contains0(sub(exit_ce,expected)),'signed clean exit CE')
            literal.append({'m':m,'t':t,'debit':enc(e)})
            v=child(v,j,0);q=qn;remaining.pop(j)

# Grouped proof audit: all cells W, exposed-partner occupancy, untouched bent sign.
grouped=[];profiles=[]
for m in ([2] if MODE=='pilot' else range(2,17)):
    A=F(1,1<<m);delta=A*A/2
    for t in range(m+1):
        k=m-t;N=1<<(2*k);multip=[(1,(N+(1<<k))//2),(-1,(N-(1<<k))//2)]
        ps=qs=F()
        for W in (0,1):
            for occupied,countJ in [(False,1),(True,(1<<t)-1)]:
                for sig,n in multip:
                    count=countJ*n
                    q=(1<<t)*((0 if W else A*A)+A**4-(0 if W or occupied else 2*A**3*sig))
                    p=((0 if W or occupied else (1<<t)*A*sig)-(1<<t)*A*A)**2
                    rr=F(1<<t) if W or not occupied else F(1<<t)*A*A/(1+A*A)
                    ck(p==rr*q,'grouped ratio');ps+=count*p;qs+=count*q
        ck(ps==qs==1,'grouped normalized')
        grouped.append([m,t])
    # First intact query uses actual Q0=P0; B is binary erasure.
    # Formula grouped over w, partner Fourier bit and remaining bent sign.
    N=1<<(2*(m-1));sp=[(1,(N+(1<<(m-1)))//2),(-1,(N-(1<<(m-1)))//2)]
    erasure=exact(0);drop1=exact(0);terms_p=[];terms_q=[];terms_q2=[]
    p1s=[];q1s=[];q2s=[]
    for W in (0,1):
        for b in (0,1):
            for sig,n in sp:
                qa=[A**4 if W else (A*sig*((-1)**(a*b))-A*A)**2 for a in (0,1)]
                qm=sum(qa)
                for p in qa: erasure=add(erasure,scale(log(qm/p),p*n))
                q1=2*A**4 if W else 2*(A*A+A**4-(2*A**3*sig if b==0 else 0))
                q2=4*A**4 if W else 4*(A*A+A**4-A**3*sig)
                p1=((2*A*sig if W==b==0 else 0)-2*A*A)**2
                ck(qm==q1,'original marginal direct group')
                drop1=add(drop1,scale(log(q2/q1),p1*n))
                ck(q2/q1>=2*(1-A),'partner log minimum bound')
                p1s.append((p1,n));q1s.append(q1);q2s.append(q2)
    e0=sub(erasure,exact(1+2*A*A));e1=sub(drop1,exact(4*A*A))
    E=add(scale(e0,F(1,2)),scale(e1,F(1,4)))
    ng=1<<(2*m);np=(ng+(1<<m))//2;nn=ng-np
    hg=ce([((A-delta)**2,(A-delta)**2,np),((A+delta)**2,(A+delta)**2,nn),(delta**2,delta**2,3*ng)])
    r=sub(exact(2*(m+(2*m+1)*delta)),hg)
    ck(r[0]>delta/4 and r[1]<F(7,128),'accepted root residual')
    ck(e0[1]<0 and e1[0]>0,'two debit signs')
    ck(E[0]>r[1],'residual plus preceding credit insufficient')
    if m>=4:ck(E[0]>F(99,640),'analytic uniform obstruction bound')
    # Literal full CE/H/KL ledger for the partner query; NEVER reset references.
    if m<=5:
        root=canonical(m);pr=law(root);v=child(root,0,0);q1=project(pr,0);p=law(v)
        va=child(v,0,0);vb=child(v,0,1);pa=law(va);pb=law(vb);q2=project(q1,0)
        ck(edges(v,0)==2*A*A,'partner physical influence')
        direct=sub(sub(cross(p,q1),scale(add(cross(pa,q2),cross(pb,q2)),F(1,2))),exact(4*A*A))
        ck(contains0(sub(direct,e1)),'independent literal partner debit')
        eh=sub(sub(entropy(p),scale(add(entropy(pa),entropy(pb)),F(1,2))),exact(4*A*A))
        kp=sub(cross(p,q1),entropy(p));ka=sub(cross(pa,q2),entropy(pa));kb=sub(cross(pb,q2),entropy(pb))
        release=sub(kp,scale(add(ka,kb),F(1,2)))
        ck(contains0(sub(sub(e1,eh),release)),'full terminal KL release identity')
        ledger={'entropy_debit':enc(eh),'parent_KL':enc(kp),'mean_child_KL':enc(scale(add(ka,kb),F(1,2))),'KL_release':enc(release)}
    else:ledger=None
    profiles.append({'m':m,'e_intact':enc(e0),'e_partner':enc(e1),'root_weighted_two_query_debit':enc(E),'original_residual':enc(r),'ledger':ledger})
out={'status':'PASS','mode':MODE,'checks':CHECKS,'runtime_seconds':time.perf_counter()-START,'literal_queries':literal,'grouped_states':len(grouped),'profiles':profiles,'arithmetic':'Exact Fraction; 28-term positive atanh with rigorous tail; outward CE rounding 2^-90'}
(R/'out').mkdir(exist_ok=True)
(R/'out'/('PILOT.json' if MODE=='pilot' else 'CHECK.json')).write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'status':'PASS','checks':CHECKS,'runtime_seconds':out['runtime_seconds'],'profiles':[{'m':p['m'],'e_partner':p['e_partner']['approx'],'two_query_debit':p['root_weighted_two_query_debit']['approx'],'ledger':p['ledger']} for p in profiles]},indent=2))
