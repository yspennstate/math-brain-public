from pathlib import Path
from fractions import Fraction as F
from collections import Counter
import json, time, sys
RUN=Path(__file__).resolve().parents[1]
spec=json.loads((RUN/'FROZEN_SPEC.json').read_text())
start=time.perf_counter(); checks=0
def ck(ok, label):
    global checks
    if not ok: raise AssertionError(label)
    checks+=1
    if time.perf_counter()-start>60: raise RuntimeError('Frozen runtime exceeded')
def fwht(v):
    v=list(v); step=1
    while step<len(v):
        for k in range(0,len(v),2*step):
            for j in range(k,k+step):
                u,w=v[j],v[j+step]; v[j]=u+w;v[j+step]=u-w
        step*=2
    return v
def coreln(q):
    z=(q-1)/(q+1); p=z; out=F(0)
    for k in range(36):out+=2*p/F(2*k+1);p*=z*z
    return out,out+2*p/(73*(1-z*z))
ln2lo,ln2hi=coreln(F(2)); cache={}
def lg(q):
    q=F(q)
    if q in cache:return cache[q]
    original=q;k=0
    while q>=2:q/=2;k+=1
    while q<1:q*=2;k-=1
    lo,hi=coreln(q);lo=k+lo/ln2hi;hi=k+hi/ln2lo
    D=1<<90; result=(F((lo*D).__floor__(),D),F((hi*D).__ceil__(),D))
    cache[original]=result;return result
def add(x,y):return x[0]+y[0],x[1]+y[1]
def sub(x,y):return x[0]-y[1],x[1]-y[0]
def mul(x,y):return (x[0]*y,x[1]*y) if y>=0 else (x[1]*y,x[0]*y)
def ent(masses,den):
    result=(F(0),F(0))
    for mass,count in Counter(masses).items():
        if mass:result=add(result,mul(lg(F(den,mass)),F(mass*count,den)))
    return result
def influence(ws,bit):return F(sum(v*v for s,v in enumerate(ws) if s&(1<<bit)),len(ws)**2)
def totalI(ws):return F(sum(v*v*s.bit_count() for s,v in enumerate(ws)),len(ws)**2)
def H(ws):return ent([v*v for v in ws],len(ws)**2)
def B(ws,i):
    b=1<<i
    if all(ws[s]*ws[s|b]==0 for s in range(len(ws)) if not s&b):return (F(0),F(0))
    return sub(H(ws),ent([ws[s]**2+ws[s|b]**2 for s in range(len(ws)) if not s&b],len(ws)**2))
def status(b,d):
    if d==0:return 'GOOD_ZERO'
    if b[1]<=4*d:return 'GOOD'
    if b[0]>4*d:return 'BAD'
    raise AssertionError('Unresolved exact K4 sign')
def display(x):return {'lower':str(x[0]),'upper':str(x[1]),'approx':float((x[0]+x[1])/2)}
records=[]; pilot='--pilot' in sys.argv
domain=spec['pilot_domain'] if pilot else spec['domain']
for a,m,masks in domain:
    delta=F(1,1<<m); P=F(sum(x.bit_count() for x in masks),4)
    n=2+a*m; N=1<<n; tmask=(1<<m)-1
    core=[]
    for t in range(1<<m):
        exponent=0
        for i in range(0,m,2):exponent^=((t>>i)&1)*((t>>(i+1))&1)
        core.append(1-2*exponent)
    truth=[]
    for word in range(N):
        zw=word&3; value=1
        for j,mask in enumerate(masks):
            t=(word>>(2+j*m))&tmask
            value*=core[t]-2*((mask>>zw)&1)*int(t==0)
        truth.append(value)
    ws=fwht(truth); den=N*N
    ck(sum(v*v for v in ws)==den,'Parseval')
    J=F(a*m,2)+2*m*delta*P
    d=[]
    for i in range(2):
        expected=F(0)
        for context in range(2):
            u=(context<<1) if i==0 else context
            v=u|(1<<i)
            s=sum(((mask>>u)&1)!=((mask>>v)&1) for mask in masks)
            expected+=(1-(1-2*delta)**s)/4
        direct=F(sum(truth[x]!=truth[x^(1<<i)] for x in range(N)),N)
        ck(direct==expected==influence(ws,i),'physical shared influence')
        d.append(expected)
    ds=sum(d,F(0));I=totalI(ws)
    ck(I==J+ds,'physical owner I')
    ck(ds<=4*delta*P,'activation owner bound')
    ck(J==sum(influence(ws,i) for i in range(2,n)),'private influences')
    # Compute each shared edge from four independently Walsh-transformed actual leaves.
    leaves=[];lws=[]; leafI=[]
    for zw in range(4):
        leaf=[truth[(t<<2)|zw] for t in range(1<<(a*m))]
        leaves.append(leaf);lws.append(fwht(leaf));leafI.append(totalI(lws[-1]))
        c=sum((mask>>zw)&1 for mask in masks)
        ck(leafI[-1]==F(a*m,2)+2*m*delta*c,'terminal private I')
        ck(H(lws[-1])[1]<=a*m,'paid terminal uniform code')
    ck(sum(leafI,F(0))/4==J,'terminal partition influence')
    t_sum=F(0); allocations=[F(0)]*a
    for i in range(2):
        for context in range(2):
            u=(context<<1) if i==0 else context; v=u|(1<<i)
            changed=[((mask>>u)&1)!=((mask>>v)&1) for mask in masks]
            derivative=[(x-y)//2 for x,y in zip(leaves[u],leaves[v])]
            dw=fwht(derivative);dden=len(dw)**2
            for j,mask in enumerate(masks):
                Q=(1-2*delta)**(sum(changed)-int(changed[j]))
                A0=(mask>>u)&1;A1=(mask>>v)&1
                Jedge=F(m,2)+m*delta*(A0+A1)
                kappa=F(m,2)*delta*int(changed[j])
                t=(1-Q)*Jedge/2+Q*kappa
                # Different representation: block energy of signed physical leaf difference.
                energy=F(sum(x*x*((s>>(j*m))&tmask).bit_count() for s,x in enumerate(dw)),dden)
                ck(energy==t,'exclusive private derivative account')
                ck(0<=t<=Jedge/2,'half-private account')
                allocations[j]+=t/2;t_sum+=t/2
    Tprivate=2*t_sum
    spectral_private=F(2*sum(v*v*(s>>2).bit_count()*(s&3).bit_count() for s,v in enumerate(ws)),den)
    ck(Tprivate==spectral_private,'two-query private bill')
    E=F(sum(v*v for s,v in enumerate(ws) if s&3==3),den)
    T=Tprivate+2*E
    ck(Tprivate<=2*J,'one private reserve')
    ck(2*E<=ds,'one shared cross account')
    ck(T<=2*I,'raw boundary budget')
    c_hi=3/ln2lo
    bound=F(a*m)+T+c_hi*ds
    ck(bound<=4*I,'terminal-inclusive four-I payment')
    # Actual prescribed physical tree: query z, then w; retain all leaves.
    rootB=B(ws,0);rootstatus=status(rootB,d[0]);localized=F(0)
    rootD=F(2*sum(v*v*(s.bit_count()-1) for s,v in enumerate(ws) if s&1),den)
    if rootstatus=='BAD':localized+=rootD
    nodes=[{'node':'root_z','Inf':str(d[0]),'B':display(rootB),'status':rootstatus,'2I_D':str(rootD)}]
    for z in range(2):
        child=[truth[(r<<1)|z] for r in range(N//2)];cw=fwht(child);ci=influence(cw,0)
        cb=B(cw,0);cs=status(cb,ci)
        bill=F(2*sum(v*v*(s.bit_count()-1) for s,v in enumerate(cw) if s&1),len(cw)**2)
        if cs=='BAD':localized+=bill/2
        nodes.append({'node':'w_after_z='+str(z),'Inf':str(ci),'B':display(cb),'status':cs,'2I_D':str(bill)})
    ck(rootD+sum(F(x['2I_D']) for x in nodes[1:])/2==T,'actual tree bill')
    ck(localized<=T,'exact bad-node localization')
    # One fixed whole-set reference: uniform private law times actual shared conditional.
    rows=[sum(ws[(r<<2)|s]**2 for s in range(4)) for r in range(1<<(a*m))]
    ck(all(rows),'no undefined positive private rows')
    deterministic_shared=all(sum(ws[(r<<2)|s]!=0 for s in range(4))==1 for r in range(1<<(a*m)))
    Bblock=(F(0),F(0)) if deterministic_shared else sub(H(ws),ent(rows,den))
    CE=add((F(a*m),F(a*m)),Bblock)
    qmass=sum((F(sum(ws[(r<<2)|s]**2 for s in range(4)),row*(1<<(a*m))) for r,row in enumerate(rows)),F(0))
    ck(qmass==1,'normalized full reference')
    ck(CE[1]<=a*m+2,'complete shared label cost')
    ck(a*m+2<=3*I,'three-I reference cost')
    ck(CE[1]<=bound,'owned bound pays same reference')
    rec={'a':a,'m':m,'masks':masks,'n':n,'P':str(P),'private_I':str(J),'shared_I':list(map(str,d)),'I':str(I),'private_boundary_bill':str(Tprivate),'shared_cross_energy':str(E),'raw_boundary_bill':str(T),'localized_K4_bill':str(localized),'per_private_block_allocations':list(map(str,allocations)),'terminal_code_cost':a*m,'complete_reference_CE':display(CE),'complete_reference_CE_over_I':display(mul(CE,1/I)),'raw_bill_over_I':str(T/I),'owned_payment_upper':str(bound),'Q_mass':str(qmass),'nodes':nodes}
    records.append(rec)
    (RUN/'out'/('PILOT_PARTIAL.json' if pilot else 'PARTIAL.json')).write_text(json.dumps({'records':records},indent=2)+'\n')
result={'helper_version':spec['helper_version'],'pilot':pilot,'cases':len(records),'assertions':checks,'failures':0,'elapsed_seconds':time.perf_counter()-start,'records':records,'full_FEI':'OPEN'}
(RUN/'out'/('PILOT.json' if pilot else 'CHECK.json')).write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({k:result[k] for k in ['helper_version','pilot','cases','assertions','failures','elapsed_seconds']}))
