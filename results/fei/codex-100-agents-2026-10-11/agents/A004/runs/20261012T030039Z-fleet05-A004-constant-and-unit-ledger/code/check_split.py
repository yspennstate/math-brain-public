"""Frozen exact physical/spectral split and source-sensitive entropy ledger."""
from pathlib import Path
import importlib.util,json,time,hashlib
from functools import lru_cache
ROOT=Path(__file__).resolve().parents[1]
print('SPLIT_CHECK_START',flush=True)
BASELINE=ROOT.parent/'20261011T223224Z-fleet05-A004-constant-and-unit-ledger/code/check_ledger.py'
COPY=Path(__file__).with_name('ledger_arithmetic.py')
COPY.write_bytes(BASELINE.read_bytes())
spec=importlib.util.spec_from_file_location('ledger_arithmetic',COPY)
M=importlib.util.module_from_spec(spec);spec.loader.exec_module(M)
print('SPLIT_ARITHMETIC_READY',flush=True)
M.log=lru_cache(maxsize=8192)(M.log)
_raw_entropy=M.entropy
@lru_cache(maxsize=8192)
def _entropy_cached(q):return _raw_entropy(q)
M.entropy=lambda q:_entropy_cached(tuple(sorted(q)))
_raw_bounds=M.bounds
@lru_cache(maxsize=8192)
def _bounds_cached(t):return _raw_bounds(dict(t))
M.bounds=lambda t:_bounds_cached(tuple(sorted(t.items())))
F=M.F
checks=0
DEADLINE=None
def ck(x):
    global checks
    assert x
    checks+=1
def form(t):return {str(p):str(c) for p,c in sorted(t.items())}
def nonnegative(t):ck(not t or M.bounds(t)[0]>=0)
def encode(s,i,bit=0):return (s&((1<<i)-1))|((s>>i)<<(i+1))|(bit<<i)
@lru_cache(maxsize=8192)
def pair(a,b):return M.add(M.entropy([a,b]),M.mul(-1,M.entropy([a+b])))
@lru_cache(maxsize=8192)
def directional(a,b):return M.mul(b,M.log(1+a/b)) if b else {}
def erasures(p,n):
    return [M.add(*(pair(p[encode(s,i)],p[encode(s,i,1)]) for s in range(1<<(n-1)))) for i in range(n)]
def directions(p,n):
    return [M.add(*(directional(p[encode(s,i)],p[encode(s,i,1)]) for s in range(1<<(n-1)))) for i in range(n)]
def audit(t,n,label):
    if DEADLINE is not None and time.perf_counter()>DEADLINE:raise TimeoutError('Frozen 58-second pilot guard')
    a=M.walsh(t);ck(a==M.direct_spectrum(t));p=[z*z for z in a];ck(sum(p)==1)
    H=M.entropy(p);Bvec=erasures(p,n);Lvec=directions(p,n)
    d=[sum((p[s] for s in range(1<<n) if s>>i&1),F(0)) for i in range(n)]
    I=sum(d,F(0));v=1-p[0];Dchar=sum((min(z,1-z) for z in d),F(0))
    B=M.add(*Bvec);DTC=M.add(H,M.mul(-1,B));TC=M.add(*(M.h2(z) for z in d),M.mul(-1,H))
    nonnegative(DTC);nonnegative(TC)
    delta=[];js=[];complement=[];slacks=[]
    for i in range(n):
        # Integer FWHT characters are (-1)^bit: physical +1 is bit 0.
        plus=[t[encode(y,i,0)] for y in range(1<<(n-1))]
        minus=[t[encode(y,i,1)] for y in range(1<<(n-1))]
        psi=[(x+y)//2 for x,y in zip(plus,minus)];phi=[(x-y)//2 for x,y in zip(plus,minus)]
        ck(all(x in [-1,0,1] and y in [-1,0,1] and x*y==0 and x*x+y*y==1 for x,y in zip(psi,phi)))
        ck(all(t[encode(y,i,b)]==psi[y]+(1-2*b)*phi[y] for y in range(len(psi)) for b in [0,1]))
        ck(sum((x*x for x in phi),F(0))/len(phi)==d[i])
        up=M.walsh(psi);vp=M.walsh(phi);gp=M.walsh(plus);hp=M.walsh(minus)
        ck(all(up[s]==a[encode(s,i)] and vp[s]==a[encode(s,i,1)] for s in range(len(up))))
        ck(sum((x*y for x,y in zip(up,vp)),F(0))==0)
        ck(sum((x*x for x in up),F(0))==1-d[i])
        ck(sum((x*x for x in vp),F(0))==d[i])
        q=[(g*g+h*h)/2 for g,h in zip(gp,hp)]
        e=[(g-h)**2/4 for g,h in zip(gp,hp)]
        ck(q==[u*u+w*w for u,w in zip(up,vp)])
        ck(e==[w*w for w in vp]);ck(sum(q)==1);ck(sum(e)==d[i])
        mismatch=M.add(*(M.mul(qj,M.h2(ej/qj)) for qj,ej in zip(q,e) if qj))
        ck(mismatch==Bvec[i])
        c=M.add(*(directional(w*w,u*u) for u,w in zip(up,vp)))
        ck(Bvec[i]==M.add(Lvec[i],c));complement.append(c)
        nonnegative(Lvec[i]);nonnegative(c)
        if c:ck(M.bounds(c)[1]<=d[i]/M.ln_interval(F(2))[1])
        js_i=M.add(M.entropy(q),M.mul(-F(1,2),M.add(M.entropy([x*x for x in gp]),M.entropy([x*x for x in hp]))))
        delta_i=M.add(H,M.mul(-F(1,2),M.add(M.entropy([x*x for x in gp]),M.entropy([x*x for x in hp]))))
        ck(delta_i==M.add(Bvec[i],js_i));nonnegative(js_i)
        if js_i:ck(M.bounds(js_i)[1]<=2/M.ln_interval(F(2))[1]*min(d[i],1-d[i]))
        delta.append(delta_i);js.append(js_i)
        slack=M.add(M.h2(d[i]),M.mul(-1,Bvec[i]));nonnegative(slack);slacks.append(slack)
        ck(I==d[i]+sum((s.bit_count()*(gp[s]**2+hp[s]**2)/2 for s in range(len(gp))),F(0)))
    ck(M.add(*slacks)==M.add(TC,DTC))
    if n:
        # Flip just the first character coordinate; full information is invariant,
        # but one-sided L changes orientation at precisely that coordinate.
        tx=[t[x]*(-1 if x&1 else 1) for x in range(1<<n)]
        ax=M.walsh(tx);px=[z*z for z in ax];ck(all(ax[s]==a[s^1] for s in range(1<<n)))
        ck(M.entropy(px)==H);ck(erasures(px,n)==Bvec)
        lx=directions(px,n);ck(lx[0]==complement[0]);ck(lx[1:]==Lvec[1:])
        if label=='point_defect' and n==3:ck(lx[0]!=Lvec[0])
    root=M.add(*(pair(p[0],p[1<<i]) for i in range(n)))
    R_info=None
    if v:
        R=[F(0)]+[x/v for x in p[1:]]
        Br=erasures(R,n);Lr=directions(R,n);DTCr=M.add(M.entropy(R),M.mul(-1,M.add(*Br)))
        ck(B==M.add(M.mul(v,M.add(*Br)),root))
        ck(DTC==M.add(M.h2(v),M.mul(v,DTCr),M.mul(-1,root)))
        ck(all(Bvec[i]==M.add(M.mul(v,Br[i]),pair(p[0],p[1<<i])) for i in range(n)))
        ck(all(Lvec[i]==M.add(M.mul(v,Lr[i]),directional(p[0],p[1<<i])) for i in range(n)))
        nonnegative(DTCr)
        R_info={'H':form(M.entropy(R)),'B':form(M.add(*Br)),'L_down':form(M.add(*Lr)),'DTC':form(DTCr)}
    else:ck(not H and not B and not DTC and not root)
    out={'label':label,'n':n,'P_empty':str(p[0]),'I':str(I),'variance':str(v),'deficit':str(I-v),'D_char':str(Dchar),'influences':[str(z) for z in d],'H':form(H),'B':form(B),'B_i':[form(z) for z in Bvec],'L_down_i':[form(z) for z in Lvec],'C_up_i':[form(z) for z in complement],'Delta_i':[form(z) for z in delta],'JS_i':[form(z) for z in js],'MI_slack_i':[form(z) for z in slacks],'DTC':form(DTC),'TC':form(TC),'empty_root_correction':form(root),'conditional_nonempty':R_info}
    if label in ['AND','OR','point_defect']:
        r=F(1,1<<n);m0=(1-2*r)**2+4*r*r
        expectedB=M.add(pair((1-2*r)**2,4*r*r),{2:4*r*(1-2*r)} if n else {})
        expectedL=M.add(directional((1-2*r)**2,4*r*r),{2:2*r*(1-2*r)} if n else {})
        ck(all(b==expectedB for b in Bvec));ck(all(l==expectedL for l in Lvec))
        ck(I==2*n*r)
        if n>=2:
            expectedR=M.add(M.log((1<<n)-1),{2:-F(n*((1<<n)-2),(1<<n)-1)})
            ck(R_info['DTC']==form(expectedR))
            ellLo=1/M.ln_interval(F(2))[1];ellHi=1/M.ln_interval(F(2))[0]
            low=r*n+n*r*r/(1-r)-ellHi*(r+r*r/(2*(1-r)))
            high=r*n+n*r*r/(1-r)-ellLo*r
            eLo,eHi=M.bounds(expectedR);ck(low<=eLo and eHi<=high)
            b0=pair((1-2*r)**2,4*r*r)
            if b0:ck(M.bounds(b0)[1]<=4*r*r*(2*n-2+ellLo))
    if label=='bent':
        ck(all(x==F(1,1<<n) for x in p));ck(H=={2:F(n)});ck(not DTC and not TC)
        ck(all(x=={2:F(1)} for x in Bvec));ck(all(x=={2:F(1,2)} for x in Lvec))
        ck(all(x=={2:F(1)} for x in js));ck(all(x=={2:F(2)} for x in delta))
    if label=='Maj3':
        ck(H=={2:F(2)});ck(I==F(3,2));ck(not B and not M.add(*delta) and not M.add(*js))
        ck(DTC=={2:F(2)});ck(TC=={2:F(1)})
    return out
def main():
    global DEADLINE
    start=time.perf_counter();counts={};records=[]
    DEADLINE=start+58
    for n in range(4):
        counts[str(n)]=1<<(1<<n)
        for mask in range(counts[str(n)]):audit([1 if mask>>x&1 else -1 for x in range(1<<n)],n,'exhaustive')
        (ROOT/'out/partial_validation.json').write_text(json.dumps({'completed_exhaustive_dimensions':list(counts),'assertions':checks,'elapsed_seconds':time.perf_counter()-start})+'\n',encoding='utf-8')
    endpoint_log=ROOT/'out/endpoint_records.jsonl'
    endpoint_log.write_text('',encoding='utf-8')
    def record(t,n,name):
        row=audit(t,n,name);records.append(row)
        with endpoint_log.open('a',encoding='utf-8') as f:f.write(json.dumps(row)+'\n')
    for n in range(1,9):
        N=1<<n
        families={'constant':[1]*N,'dictator':[-1 if x&1 else 1 for x in range(N)],'parity':[(-1)**x.bit_count() for x in range(N)],'point_defect':[-1]+[1]*(N-1),'AND':[1 if x==0 else -1 for x in range(N)],'OR':[-1 if x==N-1 else 1 for x in range(N)]}
        for name,t in families.items():record(t,n,name)
        if n%2==0:
            t=[(-1)**sum(((x>>(2*j))&1)*((x>>(2*j+1))&1) for j in range(n//2)) for x in range(N)]
            record(t,n,'bent')
    record([1 if x.bit_count()<=1 else -1 for x in range(8)],3,'Maj3')
    and2=next(r for r in records if r['label']=='AND' and r['n']==2)
    ck(and2['DTC']=={});ck(and2['conditional_nonempty']['DTC']=={'2':'-4/3','3':'1'})
    ck(3**3>2**4)
    ck(5**5<2**12);ck(5**4*2**4<3**9)
    witness={'function':'AND2, sign convention','probabilities':['1/4']*4,'variance':'3/4','full_DTC':0,'conditional_nonempty_DTC':'log2(3)-4/3>0','integer_sign_certificate':'3^3=27>16=2^4','root_correction_bits':1,'false_reading':'DTC(P)=v DTC(P conditioned nonempty), or omission of the empty-row correction','scope':'Normalization counterexample, not FEI counterexample'}
    (ROOT/'out/empty_conditioning_witness.json').write_text(json.dumps(witness,indent=2)+'\n',encoding='utf-8')
    (ROOT/'out/nonempty_asymptotics.json').write_text(json.dumps({'family':'Point defects f_n=1-2 indicator of one vertex, n>=2','p':'2^-n','conditional_DTC_exact':'n*p/(1-p)+log2(1-p)','explicit_lower':'p*(n-log2(e))+(n-log2(e)/2)*p^2/(1-p)','explicit_upper':'p*(n-log2(e))+n*p^2/(1-p)','full_DTC_asymptotic':'4*n*p','variance_weighted_conditional_DTC_asymptotic':'4*n*p^2','full_to_weighted_conditional_ratio_asymptotic':'2^n','full_FEI_ratio_limit':4,'scope':'Unbounded error in an omitted-normalization surrogate; not an unbounded FEI family','proof':'REPORT.md Section 5','finite_checks':'n=2..8'})+'\n',encoding='utf-8')
    out={'helper_version':'A004-split-ledger-v2','status':'PASS','assertions':checks,'exhaustive_counts':counts,'exhaustive_cases':sum(counts.values()),'endpoint_cases':len(records),'runtime_seconds':time.perf_counter()-start,'arithmetic_helper_sha256':hashlib.sha256(COPY.read_bytes()).hexdigest(),'arithmetic':'Integer Walsh/direct sums; Fraction; prime-log identities; rational logarithm interval signs; independent 27>16 witness certificate','endpoints':records}
    (ROOT/'out/validation.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:out[k] for k in ['status','assertions','exhaustive_cases','endpoint_cases','runtime_seconds']}))
if __name__=='__main__':main()
