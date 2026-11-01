from fractions import Fraction as R
from functools import lru_cache
from pathlib import Path
import json,time,sys

ROOT=Path(__file__).resolve().parents[1]
(ROOT/'out').mkdir(exist_ok=True)
COUNT=0
def check(x):
    global COUNT
    assert x
    COUNT+=1
def save(name,x):(ROOT/'out'/name).write_text(json.dumps(x,indent=2),encoding='utf-8')
NEG={0,1,2,4,8,16,32,6,17,40}
H=[-1 if x in NEG else 1 for x in range(64)]
GATES={'h':H,'J':[-H[x^1] for x in range(64)]}
def fwht(a):
    a=list(a);w=1
    while w<len(a):
        for k in range(0,len(a),2*w):
            for j in range(k,k+w):
                x,y=a[j],a[j+w];a[j],a[j+w]=x+y,x-y
        w*=2
    return a
WH={k:[R(x,64) for x in fwht(t)] for k,t in GATES.items()}
def floor(x,bits=64):return R((x.numerator<<bits)//x.denominator,1<<bits)
def ceil(x,bits=64):return -floor(-x,bits)
def ln_series(x):
    z=(x-1)/(x+1);t=z;s=R(0)
    for j in range(24):s+=t/(2*j+1);t*=z*z
    return 2*s,2*s+2*t/(49*(1-z*z))
LN2=ln_series(R(2))
@lru_cache(maxsize=10000)
def log2(x):
    assert x>0
    k=x.numerator.bit_length()-x.denominator.bit_length();x=x/R(2)**k
    if x<1:x*=2;k-=1
    if x>2:x/=2;k+=1
    lo=ln_series(floor(x,80))[0];hi=ln_series(ceil(x,80))[1]
    corners=[u/v+k for u in (lo,hi) for v in LN2]
    return floor(min(corners)),ceil(max(corners))
def ent(masses):
    lo=hi=R(0)
    for p in masses:
        assert p>=0
        if p:
            a,b=log2(p);lo+=floor(-p*b);hi+=ceil(-p*a)
    return floor(lo),ceil(hi)
def scale(a,x):
    assert x>=0
    return floor(a[0]*x),ceil(a[1]*x)
def add(a,b):return a[0]+b[0],a[1]+b[1]
def sub(a,b):return a[0]-b[1],a[1]-b[0]
def avg(a,b):return scale(add(a,b),R(1,2))
def encode(x):return [str(v) for v in x]
def insert(x,j):return (x&((1<<j)-1))|((x>>j)<<(j+1))
def pivotal(k,j,x):
    y=insert(x,j)
    return GATES[k][y]!=GATES[k][y|(1<<j)]
def witness_checks():
    out={}
    for k in GATES:
        check(fwht(fwht(GATES[k]))==[64*x for x in GATES[k]])
        check(sum(x*x for x in WH[k])==1)
        out[k]=[]
        for j in range(6):
            weights=[sum(pivotal(k,j,x) for x in range(32) if x.bit_count()==r) for r in range(6)]
            one=[x for x in range(32) if x.bit_count()==1 and pivotal(k,j,x)]
            minimal=min(r for r in range(6) if weights[r])
            if k=='J':check(minimal<=2)
            out[k].append({'direction':j,'dominant_pivotal':pivotal(k,j,0),'single_negative_witnesses':one,'minimum_pivotal_weight':minimal,'pivotal_counts_by_weight':weights})
        if k=='J':check(sum(r['dominant_pivotal'] for r in out[k])==4)
    check(R(15,16)**4>R(3,4))
    check(1+R(80,99)<2)
    check(R(1,16)+R(16,27)<1 and R(1,16)+R(64,27)<4)
    save('PIVOTAL_WITNESSES.json',out)
    return out

def section(k,j,p):
    m=1-2*p;v=1-m*m;packets=[]
    for T in range(64):
        if T&(1<<j):continue
        degree=T.bit_count();a=d=R(0)
        for W in range(64):
            if W&T!=T:continue
            if W&(1<<j):d+=WH[k][W]*m**(W.bit_count()-degree-1)
            else:a+=WH[k][W]*m**(W.bit_count()-degree)
        packets.append((a,d,v**degree))
    q=sum(z*d*d for a,d,z in packets)
    qp=sum(p**x.bit_count()*(1-p)**(5-x.bit_count()) for x in range(32) if pivotal(k,j,x))
    check(q==qp and q>0)
    if k=='h':check(q==2*p*(1-p)**3*(2-p) and q>=3*p)
    elif pivotal(k,j,0):check(q>=(1-p)**5>=1-5*p)
    else:
        r=min(x.bit_count() for x in range(32) if pivotal(k,j,x))
        check(q>=p**r*(1-p)**(5-r)>=R(3,4)*p**r)
    return packets,q
def partial_C(packets,q,x):
    U=[z*(a+x*d)**2 for a,d,z in packets]
    D=[z*d*d for a,d,z in packets]
    v=1-x*x
    check(sum(U)+v*q==1)
    C=sub(ent(U+[v*d for d in D]),scale(ent([v,1-v]),q))
    # Independent zero-safe raw cancellation of v log(v).
    equivalent=add(ent(U),scale(ent(D),v))
    if x:equivalent=sub(equivalent,scale(ent([x*x]),q))
    check(sub(C,equivalent)[0]<=0<=sub(C,equivalent)[1])
    return C
def scalar_fixtures(witness,pilot):
    cases=[]
    biases=[R(1,16)] if pilot else [R(1,16),R(3,64),R(1,64)]
    for k in GATES:
        for j in range(6):
            for p in biases:
                packets,q=section(k,j,p);m=1-2*p
                for b in [R(0),p,2*p]:
                    delta=sub(partial_C(packets,q,m),avg(partial_C(packets,q,m+b),partial_C(packets,q,m-b)))
                    if b:
                        L=log2(1+R(16,9)*(1-q)/q)
                        upper=q*b*b*L[1]
                        check(delta[1]<=upper)
                        rate=R(1,2) if k=='h' else (R(1,8) if witness[k][j]['dominant_pivotal'] else R(1,4)+R(witness[k][j]['minimum_pivotal_weight'],2))
                        check(delta[1]<=rate*q*b)
                    else:check(delta[0]<=0<=delta[1])
                    cases.append({'gate':k,'direction':j,'p':str(p),'beta':str(b),'q':str(q),'Delta_C_interval':encode(delta)})
    save('SCALAR_FIXTURES_PILOT.json' if pilot else 'SCALAR_FIXTURES.json',cases)
    return len(cases)

def edges(table):
    n=(len(table)-1).bit_length()
    return [R(sum(table[x]!=table[x|(1<<i)] for x in range(len(table)) if not x&(1<<i)),len(table)//2) for i in range(n)]
def core_profile(table):
    N=len(table);w=fwht(table)
    check(fwht(w)==[N*x for x in table]);check(sum(x*x for x in w)==N*N)
    p=R(sum(x<0 for x in table),N);ds=edges(table)
    for i,d in enumerate(ds):check(sum(R(w[T]*w[T],N*N) for T in range(N) if T&(1<<i))==d)
    return p,ent([R(x*x,N*N) for x in w]),sum(ds),ds
@lru_cache(maxsize=100)
def outer(k,ps):
    ms=[1-2*p for p in ps];vs=[1-m*m for m in ms];raw=[];masses=[]
    for T in range(64):
        a=R(0)
        for W in range(64):
            if W&T==T:
                prod=R(1)
                for l in range(6):
                    if (W^T)&(1<<l):prod*=ms[l]
                a+=WH[k][W]*prod
        raw.append(a);prod=R(1)
        for l in range(6):
            if T&(1<<l):prod*=vs[l]
        masses.append(prod*a*a)
    check(sum(masses)==1)
    for y in range(64):
        f=R(0)
        for T in range(64):
            prod=R(1)
            for l in range(6):
                if T&(1<<l):prod*=(-1 if y&(1<<l) else 1)-ms[l]
            f+=raw[T]*prod
        check(f==GATES[k][y])
    qs=[]
    for j in range(6):
        q=R(0)
        for x in range(32):
            if pivotal(k,j,x):
                y=insert(x,j);prob=R(1)
                for l in range(6):
                    if l!=j:prob*=ps[l] if y&(1<<l) else 1-ps[l]
                q+=prob
        qs.append(q)
        check(sum(masses[T] for T in range(64) if T&(1<<j))==vs[j]*q)
    C=ent(masses)
    for l in range(6):C=sub(C,scale(ent([vs[l],1-vs[l]]),qs[l]))
    return C,qs
def physical_fixtures(witness):
    table=[-1 if x in {0,1,2} else 1 for x in range(64)]
    p,Hcore,Icore,ds=core_profile(table);summary=[]
    for k in GATES:
        C,qs=outer(k,(p,)*6)
        for j in [0,1]:
            for i in [0,2]:
                children=[];Cs=[];qcs=[];hc=[];full_children=[];Ichildren=[]
                for bit in [0,1]:
                    child=[table[insert(x,i)|(bit<<i)] for x in range(32)]
                    pc,Hc,Ic,_=core_profile(child)
                    ps=[p]*6;ps[j]=pc
                    Cc,qc=outer(k,tuple(ps));children.append({'p':str(pc),'H_interval':encode(Hc),'I':str(Ic)})
                    Cs.append(Cc);qcs.append(qc);hc.append(Hc)
                    full_children.append(add(Cc,add(scale(Hc,qc[j]),scale(Hcore,sum(qc)-qc[j]))))
                    Ichildren.append(qc[j]*Ic+(sum(qc)-qc[j])*Icore)
                for l in range(6):check((qcs[0][l]+qcs[1][l])/2==qs[l])
                check(qcs[0][j]==qcs[1][j]==qs[j])
                DeltaC=sub(C,avg(Cs[0],Cs[1]));decrement=add(scale(sub(Hcore,avg(hc[0],hc[1])),qs[j]),DeltaC)
                full_parent=add(C,scale(Hcore,sum(qs)))
                full_decrement=sub(full_parent,avg(full_children[0],full_children[1]))
                full_residual=sub(full_decrement,decrement)
                check(full_residual[0]<=0<=full_residual[1])
                check(full_residual[1]-full_residual[0]<R(1,10**12))
                check(sum(qs)*Icore-(Ichildren[0]+Ichildren[1])/2==qs[j]*ds[i])
                rate=R(1,2) if k=='h' else (R(1,8) if witness[k][j]['dominant_pivotal'] else R(1,4)+R(witness[k][j]['minimum_pivotal_weight'],2))
                influence=qs[j]*ds[i];check(DeltaC[1]<=rate*influence)
                check(DeltaC[0]>0 or DeltaC[1]<0)
                check(decrement[0]>4*influence)
                beta=abs(R(children[0]['p'])-R(children[1]['p']))
                packets,q=section(k,j,p);m=1-2*p
                directional=sub(partial_C(packets,q,m),avg(partial_C(packets,q,m+beta),partial_C(packets,q,m-beta)))
                residual=sub(DeltaC,directional);check(residual[0]<=0<=residual[1])
                check(residual[1]-residual[0]<R(1,10**12))
                # Independently weighted physical edge enumeration, not an outer spectral marginal.
                edge=R(0)
                for x in range(32):
                    u=insert(x,i);a=table[u];b=table[u|(1<<i)]
                    if a!=b:
                        for z in range(32):
                            if pivotal(k,j,z):edge+=R(1,32)*p**z.bit_count()*(1-p)**(5-z.bit_count())
                check(edge==influence)
                row={'gate':k,'outer_block':j,'inner_coordinate':i,'core_p':str(p),'core_H_interval':encode(Hcore),'core_I':str(Icore),'children':children,'q_j':str(qs[j]),'beta_abs':str(beta),'Inf_physical':str(influence),'Delta_C_interval':encode(DeltaC),'Delta_H_full_interval':encode(decrement),'parent_H_full_interval':encode(full_parent),'children_H_full_intervals':[encode(x) for x in full_children],'full_terminal_residual':encode(full_residual),'rate_bound':str(rate),'rate_margin_lower':str(rate*influence-DeltaC[1]),'partial_full_residual':encode(residual),'sign':'positive' if DeltaC[0]>0 else 'negative'}
                save('PHYSICAL_'+k+'_'+str(j)+'_'+str(i)+'.json',row);summary.append(row)
    check(sum(x['sign']=='positive' for x in summary)==2)
    save('PHYSICAL_SUMMARY.json',{'cases':8,'positive_curvatures':2,'negative_curvatures':6,'all_complete_decrements_above_rate4':True,'scope':'Eight exact actual36-bit query cases, compressed coefficient/edge verification; no full36-bit enumeration and no universal inherited-core price.'})

if __name__=='__main__':
    start=time.perf_counter();pilot='--pilot' in sys.argv
    witnesses=witness_checks();n=scalar_fixtures(witnesses,pilot)
    if not pilot:physical_fixtures(witnesses)
    elapsed=time.perf_counter()-start;check(elapsed<(55 if pilot else 120))
    result={'mode':'pilot' if pilot else 'full','exact_or_interval_assertions':COUNT,'scalar_diagnostics':n,'actual_physical_query_cases':0 if pilot else 8,'directional_pivotal_profiles':12,'all_checks_passed':True,'runtime_seconds':elapsed,'memory_estimate_MB':100,'continuum_scope':'Analytic all p in(0,1/16], all |beta|<=min(d,2p); source-bound first physical query','independent_review':'pending','full_FEI':'OPEN'}
    save('PILOT_RESULT.json' if pilot else 'VALIDATION.json',result);print(json.dumps(result),flush=True)
