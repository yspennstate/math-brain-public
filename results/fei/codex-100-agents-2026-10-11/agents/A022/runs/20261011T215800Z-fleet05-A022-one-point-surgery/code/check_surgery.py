from pathlib import Path
from fractions import Fraction as Q
from collections import Counter
from functools import lru_cache
import json,time,math
RUN=Path(__file__).resolve().parents[1]
start=time.perf_counter(); assertions=0; cases=Counter()
def ck(x):
    global assertions
    assert x
    assertions+=1
def fwht(f):
    a=list(f); step=1
    while step<len(a):
        for i in range(0,len(a),2*step):
            for j in range(i,i+step):
                u,w=a[j],a[j+step]; a[j]=u+w; a[j+step]=u-w
        step*=2
    return a
def chi(S,v):return -1 if (S&v).bit_count()%2 else 1
def influence(f,i):
    return Q(sum(f[x]!=f[x^(1<<i)] for x in range(len(f))),len(f))
def validate(f,D,kind):
    n=(len(f)-1).bit_length(); N=len(f); delta=Q(1,N)
    a=fwht(f); g=list(f)
    for v in D:g[v]=-g[v]
    b=fwht(g); e_sum=q_sum=Q(0); minority_sum=Q(0)
    for S,(aa,bb) in enumerate(zip(a,b)):
        ts=sum(f[v]*chi(S,v) for v in D)
        ck(bb==aa-2*ts)
        e=Q(ts*ts,N*N); mid=Q((aa-ts)**2,N*N)
        q=mid+e
        ck(q==Q(aa*aa+bb*bb,2*N*N))
        e_sum+=e; q_sum+=q; minority_sum+=min(mid,e)
        if len(D)==1:
            ck(e==delta*delta); ck(e<=mid)
        elif len(D)==2:
            v,u=D; j=(v^u).bit_length()-1; eps=f[u]*f[v]
            ck(ts*ts==2+2*eps*chi(1<<j,S))
    ck(e_sum==len(D)*delta); ck(q_sum==1)
    for i in range(n):
        direct=influence(g,i)-influence(f,i)
        expect=2*delta*sum(f[v]*f[v^(1<<i)] for v in D if (v^(1<<i)) not in D)
        ck(direct==expect)
        ck(influence(f,i)==Q(sum(a[S]**2 for S in range(N) if (S>>i)&1),N*N))
    if len(D)==1:ck(minority_sum==e_sum)
    cases[kind]+=1
    if time.perf_counter()-start>60:raise TimeoutError('frozen 60-second cap')
    return a,b

@lru_cache(None)
def ln_interval(x):
    x=Q(x)
    assert x>0
    k=x.numerator.bit_length()-x.denominator.bit_length()
    y=x/Q(2)**k
    if y<1:k-=1;y*=2
    if y>=2:k+=1;y/=2
    z=(y-1)/(y+1); z2=z*z; power=z; total=Q(0)
    for j in range(50):
        total+=2*power/(2*j+1); power*=z2
    rem=2*power/(101*(1-z2))
    lo,hi=total,total+rem
    l2,h2=ln2_interval()
    if k>=0:return lo+k*l2,hi+k*h2
    return lo+k*h2,hi+k*l2
@lru_cache(None)
def ln2_interval():
    z=Q(1,3); power=z; total=Q(0)
    for j in range(50):total+=2*power/(2*j+1);power*=z*z
    return total,total+2*power/(101*(1-z*z))
def log_interval(x):
    lo,hi=ln_interval(x); l2,h2=ln2_interval()
    values=[lo/l2,lo/h2,hi/l2,hi/h2]
    return min(values),max(values)
def scale(c,ab):
    x,y=ab
    return (c*x,c*y) if c>=0 else (c*y,c*x)
def add(ab,cd):return ab[0]+cd[0],ab[1]+cd[1]
def phi_interval(r):
    A=(r-1)**2+1
    out=scale(A,log_interval(A))
    if A>1:out=add(out,scale(-(A-1),log_interval(A-1)))
    return out
def L_ratio_interval(a,N,fv):
    out=(Q(0),Q(0))
    for r,num in Counter(w*fv for w in a).items():
        out=add(out,scale(Q(num,N),phi_interval(r)))
    return out

for n in range(1,4):
    N=1<<n
    for table in range(1<<N):
        f=[-1 if (table>>x)&1 else 1 for x in range(N)]
        for v in range(N):validate(f,[v],'small_one_point')
        for v in range(N):
            for j in range(n):
                u=v^(1<<j)
                if v<u:validate(f,[v,u],'small_adjacent')

tensor_rows=[]
for table in range(16):
    h=[-1 if (table>>x)&1 else 1 for x in range(4)]
    W=fwht(h); M=sum(w!=0 for w in W);rho=Q(M,4)
    lam=(Q(0),Q(0))
    for w in W:
        if w:lam=add(lam,scale(Q(1,M),log_interval(abs(w))))
    for t in range(1,7):
        N=4**t
        f=[]
        for x in range(N):
            xx=x;y=1
            for j in range(t):y*=h[xx&3];xx>>=2
            f.append(y)
        a,b=validate(f,[0],'tensor_seed_powers')
        predicted=Counter({1:1})
        for j in range(t):
            nextc=Counter()
            for r,count in predicted.items():
                for w in W:nextc[r*w*h[0]]+=count
            predicted=nextc
        ck(Counter(w*f[0] for w in a)==predicted)
        actual=L_ratio_interval(a,N,f[0])
        l2,h2=ln2_interval();log_e=(1/h2,1/l2)
        center=add((2*(1-rho**t),)*2,scale(rho**t,add(scale(2*t,lam),log_e)))
        err=12*(rho/2)**t
        ck(actual[0]>=center[1]-err);ck(actual[1]<=center[0]+err)
        tensor_rows.append({'table':table,'t':t,'rho':str(rho),'L_over_delta_interval_exact':[str(actual[0]),str(actual[1])],'comparison_center_interval_exact':[str(center[0]),str(center[1])],'L_over_delta_interval_decimal_display':[float(actual[0]),float(actual[1])],'certified_error_bound':str(err)})

for n in [4,6,8]:
    N=1<<n
    f=[(-1)**sum(((x>>(2*j))&1)*((x>>(2*j+1))&1) for j in range(n//2)) for x in range(N)]
    root=1<<(n//2)
    for v in [0,1,N-1]:
        a,b=validate(f,[v],'bent_surgeries')
        signs=Counter(w*f[v]*chi(S,v)//root for S,w in enumerate(a))
        ck(signs[1]==(N+root)//2);ck(signs[-1]==(N-root)//2)
        for j in range(n):
            u=v^(1<<j); a,b=validate(f,[v,u],'bent_surgeries')
            eps=f[u]*f[v]
            signs=Counter(w*f[v]*chi(S,v)//root for S,w in enumerate(a) if eps*chi(1<<j,S)==1)
            ck(signs[1]==N//4+root//2);ck(signs[-1]==N//4-root//2)

out={'helper_version':'A022-surgery-v1','assertions_passed':assertions,'cases':dict(cases),'elapsed_seconds':time.perf_counter()-start,'arithmetic':'integer and Fraction; rational outward atanh-series log intervals','tensor_rows':tensor_rows,'full_fei':'OPEN','independent_review':'not performed'}
(RUN/'out'/'EXACT_CHECK.json').write_text(json.dumps(out,indent=2),encoding='utf-8')
print(json.dumps({k:v for k,v in out.items() if k!='tensor_rows'},indent=2))
