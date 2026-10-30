from pathlib import Path
from fractions import Fraction as F
import hashlib,json,time,sys
from exact_math import L,log,sumL,transform,cube,nat_bounds,ln_bounds
RUN=Path(__file__).resolve().parents[1]; OUT=RUN/'out'; pilot='--pilot' in sys.argv
ds=[2] if pilot else [2,4,6]
spec={'helper':'A100-positive-erasure-binary-v1','math_helper_sha256':hashlib.sha256((RUN/'code/exact_math.py').read_bytes()).hexdigest(),
      'family':'A073 positive-erasure bent/AND boundary; tensor with each labeled two-bit Boolean spectator',
      'domain':{'d':ds,'spectator_masks':[None,1] if pilot else [None]+list(range(16))},
      'case_count':2 if pilot else 51,'symmetry':'none; both physical query rows retained','arithmetic':'integer FWHT, physical flip counts, Fraction, exact formal prime-log identities, 24-term range-reduced rational atanh intervals; integer power signs',
      'memory_estimate_MB':40,'max_runtime_seconds':60,'maximum_enumerated_dimension':6 if pilot else 10,'automatic_dimension_escalation':False}
(RUN/('PILOT_SPEC.json' if pilot else 'CHECK_SPEC.json')).write_text(json.dumps(spec,indent=2)+'\n',encoding='utf-8')
t0=time.perf_counter(); assertions=0; output=[]
def check(ok,name):
    global assertions
    assert ok,name
    assertions+=1
def positive(x): return nat_bounds(x)[0]>0
def nonnegative(x): return nat_bounds(x)[0]>=0
def pack_bits(x):
    lo,hi=nat_bounds(x); a,b=ln_bounds(2)
    endpoints=[lo/a,lo/b,hi/a,hi/b]; scale=2**80
    left=min(endpoints);right=max(endpoints)
    return {'lower':str(F((left*scale).numerator//(left*scale).denominator,scale)),
            'upper':str(F(-((-right*scale).numerator//(-right*scale).denominator),scale))}
check(77**4<2*65**4,'uniform Jensen half-log price strictly below 1/8')
check(7**128<2**63*5**128,'original source 1/256 uniform margin')
check((1-F(1,2)-F(1,64))==F(31,64),'monotonicity derivative numerator positive throughout delta<=1/4')
outpath=OUT/('PILOT_CASES.jsonl' if pilot else 'CASES.jsonl')
with outpath.open('w',encoding='utf-8') as sink:
    for d in ds:
        delta=F(1,2**d);t=F(1,2**(d//2)); e=delta/2
        R=(1+delta-3*delta*delta/4)/(1+delta*delta/4)
        check(1<R<=F(77,65),'exact Jensen rational envelope')
        check(R<1+delta,'quadratic loss envelope')
        Np=(2**d+2**(d//2))//2; Nm=2**d-Np
        D0=Np*delta*log((1-delta/2)/(1-t+delta/2))+Nm*delta*log((1-delta/2)/(1+t+delta/2))
        check(positive(D0),'strict positive conditional remainder')
        check(positive(log(R)-D0),'Jensen bound without discarding unequal sign weights')
        check(positive(log(2)*F(1,8)-D0/2),'strict half-sized uniform allowance')
        check(positive(log(2)*F(1,4)-D0/2-log(2)*F(1,256)),'unchanged original source allowance')
        binary=F(1,2)*log(1/(2*(1-e)))+F(1,2)*log(1/(2*e))
        for mask in spec['domain']['spectator_masks']:
            extra=0 if mask is None else 2; N=d+2+extra; tab=[]
            for x in range(1<<N):
                y=x&((1<<d)-1); b=1
                for j in range(0,d,2):
                    if ((y>>j)&1) and ((y>>(j+1))&1): b=-b
                u=(x>>d)&1;v=(x>>(d+1))&1
                val=(-1 if u and v else 1) if y==0 else b
                if extra: val*=1-2*((mask>>(x>>(d+2)))&1)
                tab.append(val)
            a,p,inf=cube(tab)
            for i in range(N):
                check(inf[i]==sum((p[s] for s in range(len(p)) if s&(1<<i)),F(0)),'independent physical/spectral influence')
            if mask is None:
                check(all(p),'actual positive Fourier support')
                check(sum(inf,F(0))==F(d,2)+(F(d,2)+1)*delta,'actual total influence')
                check(all(inf[i]==(1+delta)/2 for i in range(d)),'actual core physical reserve')
                entropy=sumL(-v*log(v) for v in p if v)
                check(nonnegative(log(2)*(2+F(4,d))*sum(inf,F(0))-entropy),'original source H/I upper bound')
                bhat=transform([1-2*(sum(((y>>j)&1)*((y>>(j+1))&1) for j in range(0,d,2))%2) for y in range(1<<d)])
                for T,v0 in enumerate(bhat):
                    check(abs(v0)==t,'direct quadratic Fourier magnitude')
                    for U,coef in [(0,v0-delta/2),(1,delta/2),(2,delta/2),(3,-delta/2)]:
                        check(a[T|(U<<d)]==coef,'actual four signed row amplitudes')
            row_values=[]
            for i,j in [(d,d+1),(d+1,d)]:
                check(inf[i]==e,'queried physical influence')
                ib=1<<i;jb=1<<j; r={s:p[s]+p[s|ib] for s in range(len(p)) if not s&ib}
                mu={s:p[s|ib]/e for s in r}
                check(sum(r.values())==sum(mu.values())==1,'complete probability laws normalize')
                qr=[sum((z for s,z in r.items() if bool(s&jb)==bool(v)),F(0)) for v in [0,1]]
                qm=[sum((z for s,z in mu.items() if bool(s&jb)==bool(v)),F(0)) for v in [0,1]]
                check(qr==[1-e,e] and qm==[F(1,2),F(1,2)],'binary quotient keeps reference outside derivative support')
                full=sumL(z*log(z/r[s]) for s,z in mu.items() if z)
                quotient=sumL(qm[v]*log(qm[v]/qr[v]) for v in [0,1])
                conditional=sumL(z*log((z/qm[int(bool(s&jb))])/(r[s]/qr[int(bool(s&jb))])) for s,z in mu.items() if z)
                check(quotient==binary,'exact partner-only divergence')
                check(full==binary+D0/2 and conditional==D0/2,'complete conditional KL chain and spectator cancellation')
                M=sumL(p[s|ib]*log(r[s]/p[s|ib]) for s in r if p[s|ib])
                check(M==e*(log(1/e)-full),'retained original row price')
                check(positive(M-e*(F(d,2)+F(3,4))*log(2)),'large surviving retained row price')
                erasure=sumL(p[s]*log(r[s]/p[s])+p[s|ib]*log(r[s]/p[s|ib]) for s in r if p[s] and p[s|ib])
                check(positive(erasure),'strict actual erasure, not parity duplication')
                loss=e*(full-quotient)
                check(loss==e*D0/2,'exact lost influence-weighted refund')
                check(positive(e*log(R)/2-loss),'new Jensen weighted allowance')
                row_values.append(loss)
            total=sumL(row_values)
            check(positive(log(2)*delta/8-total),'two losses uniformly below delta/8')
            if mask is None: check(positive(log(2)*inf[0]/20-total),'two losses fit dedicated core fraction 1/20')
            # Natural-log remainder <delta^2/2 implies bit remainder <delta^2/(2 ln2).
            check(nat_bounds(total)[1]<delta*delta/2,'quadratic-in-delta total remainder')
            row={'d':d,'spectator_mask':mask,'I':str(sum(inf,F(0))),'row_influence':str(e),
                 'Jensen_R':str(R),'loss_over_row_influence':pack_bits(D0/2),
                 'total_weighted_loss':pack_bits(total),'retained_M_over_row_influence':pack_bits(log(1/e)-binary-D0/2)}
            output.append(row); sink.write(json.dumps(row)+'\n');sink.flush()
result={'helper':spec['helper'],'status':'PASS','assertions_passed':assertions,'failures':0,'cases':len(output),
        'runtime_seconds':time.perf_counter()-t0,'maximum_enumerated_dimension':spec['maximum_enumerated_dimension'],
        'bound':'0<L/e<=log2(R(delta))/2<=log2(77/65)/2<1/8; total<delta^2/(2ln2)',
        'scope':'All-even-d conclusions use REVIEW.md analytic proof, not extrapolation; no universal quotient ownership or terminal payment.'}
(OUT/('PILOT_CHECK.json' if pilot else 'INDEPENDENT_CHECK.json')).write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result,indent=2),flush=True)
