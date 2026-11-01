from pathlib import Path
from fractions import Fraction as Q
from math import comb
import json,time
RUN=Path(__file__).resolve().parents[1]
(RUN/'out').mkdir(exist_ok=True)
start=time.perf_counter(); assertions=0
def ck(p):
    global assertions
    assert p
    assertions+=1

def fwht(v):
    v=list(v); h=1
    while h<len(v):
        for i in range(0,len(v),2*h):
            for j in range(i,i+h):
                u,w=v[j],v[j+h];v[j]=u+w;v[j+h]=u-w
        h*=2
    return v

cache={}
def lncore(q,terms=36):
    z=(q-1)/(q+1); power=z; z2=z*z; total=Q(0)
    for k in range(terms):
        total+=2*power/Q(2*k+1);power*=z2
    err=2*power/(Q(2*terms+1)*(1-z2))
    return total,total+err
L2,H2=lncore(Q(2))
def lg(q):
    q=Q(q);ck(q>=1)
    if q in cache:return cache[q]
    original=q;k=0
    while q>=2:q/=2;k+=1
    l,h=lncore(q)
    lower,upper=Q(k)+l/H2,Q(k)+h/L2
    D=1<<100
    out=(Q((lower*D).__floor__(),D),Q((upper*D).__ceil__(),D))
    ck(out[0]<=lower<=upper<=out[1]);cache[original]=out
    return out
def add(x,y):return x[0]+y[0],x[1]+y[1]
def mul(x,q):return (x[0]*q,x[1]*q) if q>=0 else (x[1]*q,x[0]*q)
def entropy(ps):
    out=(Q(0),Q(0))
    for p in ps:
        if p:out=add(out,mul(lg(1/p),p))
    return out
def render(x):return {'lower':str(x[0]),'upper':str(x[1]),'display':[float(x[0]),float(x[1])]}
def ratio(x,y):
    ck(y[0]>0);ck(x[0]>=0)
    return x[0]/y[1],x[1]/y[0]

def theta(s,r,bits=48):
    if s>=r:return Q(1),Q(1)
    D=1<<bits;target=s**6*D**5;den=r**6
    lo,hi=0,D
    while hi-lo>1:
        mid=(lo+hi)//2
        if mid**5*den<=target:lo=mid
        else:hi=mid
    ck(lo**5*den<=target<=hi**5*den)
    return Q(lo,D),Q(hi,D)

def normalizer(n,s):
    l=[Q(0)]*(s+1);h=l.copy();l[0]=h[0]=Q(1)
    for r in range(1,n+1):
        tl,th=theta(s,r)
        for k in range(min(s,r),0,-1):
            l[k]+=l[k-1]*tl;h[k]+=h[k-1]*th
    ck(l[s]>=1);ck(l[s]<=h[s]);ck(h[s]<=comb(n,s))
    return lg(l[s])[0],lg(h[s])[1]

def bent(z,m):return 1-2*((sum(((z>>(2*k))&1)*((z>>(2*k+1))&1) for k in range(m//2)))&1)
def base_truth(m):
    return [bent(z>>1,m)-2*(z&1)*int((z>>1)==0) for z in range(1<<(m+1))]
records=[]
for m in [2,4,6]:
    d=m+1; base=base_truth(m);walsh=fwht(base);den=len(base)
    pb=[Q(v*v,den*den) for v in walsh]
    g0=[bent(y,m) for y in range(1<<m)];g1=g0.copy();g1[0]*=-1
    p0=[Q(v*v,2**(2*m)) for v in fwht(g0)]
    p1=[Q(v*v,2**(2*m)) for v in fwht(g1)]
    avgH=mul(add(entropy(p0),entropy(p1)),Q(1,2))
    Hb=entropy(pb);Delta=(Hb[0]-avgH[1],Hb[1]-avgH[0])
    delta=Q(1,2**m);u=Q(1,2**(m//2))
    dataH=entropy([pb[2*t]+pb[2*t+1] for t in range(1<<m)])
    B=(Hb[0]-dataH[1],Hb[1]-dataH[0])
    ck(B[0]>=delta*(m-1))
    ck(pb[0]==(u-delta)**2)
    for t in range(1<<m):
        sign=1 if fwht(g0)[t]>0 else -1
        ck(pb[2*t]==(sign*u-delta)**2)
        ck(pb[2*t+1]==delta**2)
    ck(sum(pb)==1)
    Ib=sum((p*k.bit_count() for k,p in enumerate(pb)),Q(0))
    ck(Ib==Q(m,2)+(m+1)*delta)
    ck(sum((p for k,p in enumerate(pb) if k&1),Q(0))==delta)
    base_sizes=[sum((p for k,p in enumerate(pb) if k.bit_count()==s),Q(0)) for s in range(d+1)]
    for a in [1,2]:
        n=a*d;size=1<<n
        truth=[]
        for z in range(size):
            v=1
            for j in range(a):v*=base[(z>>(j*d))&((1<<d)-1)]
            truth.append(v)
        w=fwht(truth);p=[Q(x*x,size*size) for x in w]
        Ps=[Q(0)]*(n+1);joint=[[Q(0)]*n for _ in range(n+1)]
        for mask,prob in enumerate(p):
            expected=Q(1)
            for j in range(a):expected*=pb[(mask>>(j*d))&((1<<d)-1)]
            ck(prob==expected)
            s=mask.bit_count();Ps[s]+=prob
            for r in range(n):
                if mask&(1<<r):joint[s][r]+=prob
        ck(sum(Ps)==1);ck(Ps[0]==pb[0]**a)
        I=sum((s*Ps[s] for s in range(n+1)),Q(0));ck(I==a*Ib)
        # Independent edge counts, including the rare selector and every data coordinate.
        for r in range(n):
            edge=Q(sum(truth[z]!=truth[z^(1<<r)] for z in range(size)),size)
            si=sum((joint[s][r] for s in range(n+1)),Q(0))
            ck(edge==si);ck(edge==(delta if r%d==0 else Q(1,2)+delta))
        H=mul(Hb,a);De=mul(Delta,a)
        queue=entropy([Ps[0],1-Ps[0]])
        for s in range(1,n+1):
            if not Ps[s]:continue
            zcost=normalizer(n,s)
            queue=add(queue,mul(add(lg(2*s*(s+1)),zcost),Ps[s]))
            for r in range(1,n+1):
                if r>s and joint[s][r-1]:queue=add(queue,mul(lg(Q(r,s)),Q(6,5)*joint[s][r-1]))
        ck(queue[0]>=H[1]);ck(De[0]>0)
        # A coarse universal-in-(a,m) bound for this family, with the analytic K in REPORT.
        ck(queue[1]<9*I)
        flat=(Q(n),Q(n))
        Idata=Ib-delta
        # Expected charges in the actual selector-first tree retain independent spectator factors.
        boundary=a*m*delta+2*delta*a*(a-1)*Idata+a*(a-1)*delta**2
        direct_boundary=Q(0)
        for j in range(a):
            for prefix in range(1<<j):
                remaining=[r for r in range(n) if r not in [t*d for t in range(j+1)]]
                dv=[]
                for residual in range(1<<len(remaining)):
                    z=sum(((prefix>>t)&1)<<(t*d) for t in range(j))
                    z+=sum(((residual>>t)&1)<<r for t,r in enumerate(remaining))
                    dv.append(Q(truth[z]-truth[z|(1<<(j*d))],2))
                dw=fwht(dv);ds=len(dv)
                DI=sum((Q(v*v,ds*ds)*mask.bit_count() for mask,v in enumerate(dw)),Q(0))
                direct_boundary+=2*DI/Q(1<<j)
        ck(boundary==direct_boundary)
        records.append({'a':a,'m':m,'n':n,'rows':size,'I':str(I),'I_sel':str(a*delta),'I_data':str(I-a*delta),'Delta':render(De),'H':render(H),'flat_code':render(flat),'queue_code':render(queue),'flat_over_Delta':render(ratio(flat,De)),'flat_over_I':str(Q(n)/I),'queue_over_Delta':render(ratio(queue,De)),'queue_over_I':render(mul(queue,1/I)),'boundary_charge_2I_D':str(boundary),'boundary_over_I':str(boundary/I),'factor_removed_boundary':str(a*m*delta),'factor_removed_boundary_over_I':str(a*m*delta/I),'B_single_selector_over_Inf':render(mul(B,1/delta)),'empty_mass':str(Ps[0])})
        (RUN/'out'/'PARTIAL.json').write_text(json.dumps({'records':records},indent=2)+'\n',encoding='utf8')
out={'helper_version':'A016-bent-code-v1','assertions':assertions,'failures':0,'elapsed_seconds':time.perf_counter()-start,'records':records,'arithmetic':'integer/Fraction, rational logarithm intervals, certified algebraic fifth-root normalizers','full_fei':'OPEN'}
(RUN/'out'/'CHECK.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf8')
print(json.dumps({k:out[k] for k in ['assertions','failures','elapsed_seconds']}))
for r in records:print(json.dumps({k:r[k] for k in ['a','m','I','flat_over_Delta','flat_over_I','queue_over_Delta','queue_over_I']},ensure_ascii=False))
