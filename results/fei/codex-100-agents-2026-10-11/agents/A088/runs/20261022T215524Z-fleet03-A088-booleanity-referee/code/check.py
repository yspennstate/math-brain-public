import sys,time,json,hashlib,itertools,math
from pathlib import Path
from fractions import Fraction as F
from functools import lru_cache
from collections import Counter

RUN=Path(__file__).resolve().parents[1]
MODE=sys.argv[1] if len(sys.argv)>1 else 'pilot'
LIMIT=60 if MODE=='pilot' else 180
START=time.perf_counter();checks=0
def ck(ok,label):
    global checks
    checks+=1
    if not ok:raise AssertionError(label)
    if time.perf_counter()-START>LIMIT:raise TimeoutError('frozen runtime exceeded')

@lru_cache(None)
def ln_interval(x):
    x=F(x);assert x>0
    z=(x-1)/(x+1);assert 0<=z<=F(1,3)
    val=2*sum((z**(2*k+1)/F(2*k+1) for k in range(28)),F())
    return val,val+2*z**57/(57*(1-z*z))

@lru_cache(None)
def log2_interval(x):
    x=F(x);k=0
    while x<1:x*=2;k-=1
    while x>=2:x/=2;k+=1
    a,b=ln_interval(x);c,d=ln_interval(F(2))
    return F(k)+a/d,F(k)+b/c

def rnd(a,b):
    scale=1<<80
    return F(a.numerator*scale//a.denominator,scale),F(-((-b.numerator*scale)//b.denominator),scale)
def entropy(groups):
    lo=hi=F()
    for p,mult in groups:
        if not p:continue
        a,b=log2_interval(F(1,p));lo+=mult*p*a;hi+=mult*p*b
    return rnd(lo,hi)
def sub(a,b):return a[0]-b[1],a[1]-b[0]
def add(a,b):return a[0]+b[0],a[1]+b[1]
def mul(a,k):
    return (a[0]*k,a[1]*k) if k>=0 else (a[1]*k,a[0]*k)
def enc(a):return {'lower':str(a[0]),'upper':str(a[1]),'approx':float(sum(a)/2)}
def grouped(m):
    n=1<<(2*m);a=F(1,1<<m);delta=F(1,2*n)
    pos=(n+(1<<m))//2;neg=n-pos
    g=[((a-delta)**2,pos),((a+delta)**2,neg),(delta**2,3*n)]
    c=[((a-2*delta)**2,pos),((a+2*delta)**2,neg),(4*delta**2,n)]
    t=[((a-delta)**2+delta**2,pos),((a+delta)**2+delta**2,neg),(2*delta**2,n)]
    for law in [g,c,t]:ck(sum(p*k for p,k in law)==1,'group normalization')
    return delta,g,c,t
def fwht(values):
    a=list(values);step=1
    while step<len(a):
        for base in range(0,len(a),2*step):
            for j in range(base,base+step):
                x,y=a[j],a[j+step];a[j],a[j+step]=x+y,x-y
        step*=2
    return a
def spectrum(values):
    den=len(values)
    return [F(x,den) for x in fwht(values)]
def influences(values):
    n=(len(values)-1).bit_length();den=len(values)
    return [F(sum(values[x]!=values[x^(1<<i)] for x in range(den)),den) for i in range(n)]
def table(m,tilt=0,zvalue=None):
    n=2*m+1+(zvalue is None);out=[]
    for x in range(1<<n):
        y=x&((1<<(2*m))-1);w=(x>>(2*m))&1
        bit=sum(((y>>(2*j))&1)*((y>>(2*j+1))&1) for j in range(m))+(y&tilt).bit_count()
        base=(-1)**bit;z=(-1)**((x>>(2*m+1))&1) if zvalue is None else zvalue
        out.append(base+(z-1 if y==0 and w==0 else 0))
    return out

rows=[]
for m in ([2] if MODE=='pilot' else range(1,9)):
    delta,g,c,t=grouped(m);hg,hc,ht=map(entropy,[g,c,t]);hb=(F(2*m),F(2*m));hbar=mul(add(hb,hc),F(1,2))
    ix=F(m)+(2*m+1)*delta
    bank=sub((2*ix,2*ix),hbar);decrement=sub(hg,hbar);r=sub((2*ix,2*ix),hg)
    b=sub(hg,ht);js=sub(ht,hbar)
    difference=sub(add(b,js),decrement)
    ck(difference[0]<=0<=difference[1],'B+JS identity interval consistency')
    if m>=2:
        ck(r[0]>delta/4,'canonical source residual')
        ck(bank[0]>0,'both source terminals certified')
        ck(r[1]<F(1,16),'frozen residual cannot pay 1/4')
        ck(r[1]<delta*(F(m)-F(1,4)),'analytic residual upper bound')
    else:ck(r[1]<0,'excluded m1 guard')
    if m in ([2] if MODE=='pilot' else range(1,5)):
        root=table(m);plus=table(m,zvalue=1);minus=table(m,zvalue=-1)
        p=[x*x for x in spectrum(root)];pc=[x*x for x in spectrum(minus)]
        ck(all(x in [-1,1] for x in root+plus+minus),'actual Boolean values')
        ck(Counter(p)==Counter({q:sum(k for qq,k in g if qq==q) for q,_ in g}),'full root groups')
        ck(Counter(pc)==Counter({q:sum(k for qq,k in c if qq==q) for q,_ in c}),'full terminal groups')
        inf=influences(root);ip=influences(plus);ic=influences(minus)
        ck(inf[-1]==delta and sum(inf[:-1])==ix,'physical root influences')
        ck(sum(ip)==m and sum(ic)==m+(4*m+2)*delta,'both physical terminal influences')
        sp=spectrum(root)
        ck(sum(F(s.bit_count())*p[s] for s in range(len(p)))==sum(inf),'spectral physical energy agreement')
        # Both z branches remain in the final frontier; split only clean z=+.
        y0=[plus[x] for x in range(len(plus)) if not x&1]
        y1=[plus[x] for x in range(len(plus)) if x&1]
        for yy,hh,ii in [(y0,2*m-2,m-1),(y1,2*m-2,m)]:
            ph=[v*v for v in spectrum(yy)]
            ck(sum(influences(yy))==ii,'clean query terminal I')
            ck(entropy(Counter(ph).items())[0] <= hh <= entropy(Counter(ph).items())[1],'clean query terminal H')
        final_h=add(mul(hc,F(1,2)),(F(m-1),F(m-1)))
        final_i=F(m)-F(1,4)+(2*m+1)*delta
        final_bank=sub((2*final_i,2*final_i),final_h)
        ck(sub(final_bank,bank)[0]<=F(1,2)<=sub(final_bank,bank)[1],'exact transported bank increment')
        final_spare=sub(final_bank,add(decrement,(F(1,2),F(1,2))))
        ck(final_spare[0]<=r[1] and r[0]<=final_spare[1],'same original residual preserved')
    rows.append({'m':m,'delta':str(delta),'residual':enc(r),'residual_over_delta':enc(mul(r,1/delta)),'bank':enc(bank),'decrement':enc(decrement)})

states=transitions=0
for m in ([1] if MODE=='pilot' else range(1,5)):
    for s in itertools.product([-1,0,1],repeat=2*m):
        states+=1
        def pairdata(state):
            h=i=0
            for j in range(m):
                a,b=state[2*j:2*j+2]
                if a==b==-1:h+=2;i+=1
                elif (a==-1 and b==1) or (b==-1 and a==1):i+=1
            return F(h),F(i)
        h,i=pairdata(s);surplus=2*i-h
        ck(surplus>=0,'all actual clean terminals C2 certified')
        ck(surplus==2*sum((a==-1 and b==1) or (b==-1 and a==1) for a,b in zip(s[::2],s[1::2])),'open character count')
        for q in range(2*m):
            if s[q]!=-1:continue
            transitions+=1;data=[]
            for value in [0,1]:
                child=list(s);child[q]=value;data.append(pairdata(child))
            hc=(data[0][0]+data[1][0])/2;ic=(data[0][1]+data[1][1])/2
            # Boolean pair formulas give Inf=1/2 for full pair, 1 for live character.
            partner=s[q^1];inf=F(1,2) if partner==-1 else F(partner)
            ck(i-ic==inf,'physical influence telescopes')
            ck((2*ic-hc)-surplus==(h-hc)-2*inf,'same-owner exact signed transport')
            qce=F(sum(v==-1 for v in s));childce=qce-1
            ck((2*ic-childce)-(2*i-qce)==1-2*inf,'inherited uniform reference signed transport')

phase_hist=Counter();guard={}
if MODE=='full':
    delta,g,c,t=grouped(2);hg=entropy(g);hc=entropy(c);hbar=mul(add((F(4),F(4)),hc),F(1,2));decrement=sub(hg,hbar)
    boolean_phases=matched_jet_real=0
    for neg in itertools.combinations(range(16),6):
        degree_sum=sum(x.bit_count() for x in neg);jet=degree_sum-11;phase_hist[jet]+=1
        ix=F(2)+delta*jet;bank=sub((2*ix,2*ix),hbar);r=sub((2*ix,2*ix),hg)
        ck((bank[0]>=0)==(jet>=2),'all phases terminal certification classification')
        ck((r[0]>delta/4)==(jet>=5),'all phases source payment classification')
        vals=fwht([-1 if u in neg else 1 for u in range(16)])
        boolean=all(abs(v)==4 for v in vals)
        boolean_phases+=boolean
        if jet==5 and not boolean:matched_jet_real+=1
    neg={15,7,11,3,5,1};coeff=[F(-1 if x in neg else 1,4) for x in range(16)]
    physical=fwht(coeff)
    ck(physical[0]==1 and sum(v*v for v in physical)/16==1,'real flat marked-point normalization')
    ck(any(v not in [-1,1] for v in physical),'guard is genuinely nonBoolean')
    jet=1+sum(physical[1<<j] for j in range(4));ck(jet==4,'retained local neighbor jet')
    ix=F(2)+delta*jet;bank=sub((2*ix,2*ix),hbar);r=sub((2*ix,2*ix),hg)
    ck(bank[0]>0 and r[1]<0,'certified real children still fail source payment extension')
    hfull=physical+physical
    cfull=list(hfull);cfull[0]-=2
    realroot=hfull+cfull
    for values in [hfull,cfull,realroot]:
        ck(sum(v*v for v in values)/len(values)==1,'displayed real physical child/root norm one')
    def real_i(values):
        return sum(sum((values[x]-values[x^(1<<q)])**2 for x in range(len(values)))/(4*len(values)) for q in range((len(values)-1).bit_length()))
    ck(real_i(hfull)==2 and real_i(cfull)==2+2*delta*jet,'displayed real physical Dirichlet energy')
    pguard=[v*v for v in spectrum(realroot)]
    ck(Counter(pguard)==Counter({p:sum(k for pp,k in g if pp==p) for p,_ in g}),'real full spectrum matches grouped entropy')
    convolution=[sum(coeff[s]*coeff[s^u] for s in range(16)) for u in range(1,16)]
    ck(any(convolution),'full nonempty Boolean convolution violated')
    guard={'negative_masks':sorted(neg),'physical_values':list(map(str,physical)),'bank':enc(bank),'residual':enc(r),'first_nonzero_convolution':next({'shift':u,'value':str(v)} for u,v in enumerate(convolution,1) if v),'boolean_phases':boolean_phases,'nonBoolean_phases_with_same_summed_jet':matched_jet_real}
    for m in [2,3]:
        root=table(m,tilt=1);plus=table(m,tilt=1,zvalue=1);minus=table(m,tilt=1,zvalue=-1)
        delta,g,c,t=grouped(m);ix=F(m)+(2*m-1)*delta
        hgr=entropy(g);hcr=entropy(c);hb=(F(2*m),F(2*m));bar=mul(add(hb,hcr),F(1,2))
        ck(all(v in [-1,1] for v in root),'tilted guard actual Boolean')
        ck(sum(influences(root)[:-1])==ix,'tilted physical incidence')
        pp=[v*v for v in spectrum(root)]
        ck(Counter(pp)==Counter({p:sum(k for qq,k in g if qq==p) for p,_ in g}),'tilted actual Boolean root spectrum')
        ck(sub((2*ix,2*ix),bar)[0]>0,'tilted two terminal C2 certificates')
        ck(sub((2*ix,2*ix),hgr)[1]<0,'all-bent generalization fails')

elapsed=time.perf_counter()-START
output={'status':'PASS','mode':MODE,'checks':checks,'runtime_seconds':elapsed,'formula_rows':rows,'clean_states':states,'clean_transitions':transitions,'real_phase_count':sum(phase_hist.values()),'real_phase_jet_histogram':dict(sorted(phase_hist.items())),'real_guard':guard,'helper_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
(RUN/'out').mkdir(exist_ok=True)
with (RUN/'out'/('CHECK_pilot.json' if MODE=='pilot' else 'CHECK.json')).open('w',encoding='utf-8',newline='\n') as f:json.dump(output,f,indent=2)
print(json.dumps({k:output[k] for k in ['status','mode','checks','runtime_seconds','clean_states','clean_transitions','real_phase_count']}))
