from pathlib import Path
from fractions import Fraction as Q
import json,sys,time
run=Path(__file__).resolve().parents[1]
old=run.parent/'20261014T012949Z-account05-A066-semigroup-dissipation/code/check_refund_independent.py'
ns={'__file__':str(__file__)}
exec(compile(old.read_text().split('seeds=[]')[0],str(old),'exec'),ns)
test,logadd,combine=[ns[x] for x in ['test','logadd','combine']]
oldlogs=run.parent/'20261011T233317Z-account05-A066-semigroup-dissipation/code/check_restrictions.py'
lns={'__file__':str(__file__)}
exec(compile(oldlogs.read_text().split('mode=sys.argv[1]')[0],str(oldlogs),'exec'),lns)
mode=sys.argv[1]; started=time.perf_counter()

def bound(expr): return lns['enclosure']({Q(p):c for p,c in expr.items()})
def physical_spectrum(values):
    N=len(values); a=list(values); width=1
    while width<N:
        for start in range(0,N,2*width):
            for j in range(width):
                u,v=a[start+j],a[start+j+width]
                a[start+j],a[start+j+width]=u+v,u-v
        width*=2
    return [Q(v,N) for v in a]

def bent(y,d):
    return (-1)**sum(((y>>(2*j))&1)*((y>>(2*j+1))&1) for j in range(d//2))

def check(q,d,spectator=None):
    r=(len(q)-1).bit_length(); delta=Q(1,1<<d); t=Q(1,1<<(d//2))
    qa=physical_spectrum(q); a=qa[0]; alpha=1-a
    f=tuple(q[x&((1<<r)-1)] if x>>r==0 else bent(x>>r,d) for x in range(1<<(d+r)))
    if spectator is not None:
        size=len(f); f=tuple(f[x%size]*spectator[x//size] for x in range(size*len(spectator)))
    fa=physical_spectrum(f); p=[x*x for x in fa]; N=len(f)
    test(sum(p)==1)
    totalI=sum(Q(sum(f[x]!=f[x^(1<<i)] for x in range(N)),N) for i in range(N.bit_length()-1))
    Iq=sum(sum(qa[S]**2 for S in range(1<<r) if S>>i&1) for i in range(r))
    expectedI=Q(d,2)+d*delta*(1-a)+delta*Iq
    if spectator is not None:
        sa=physical_spectrum(spectator)
        expectedI+=sum(S.bit_count()*v*v for S,v in enumerate(sa))
    test(totalI==expectedI)
    loss_total={}; records=[]
    for i in range(r):
        bit=1<<i; eiq=sum(qa[S]**2 for S in range(1<<r) if S&bit)
        ei=delta*eiq
        test(ei==sum(p[S] for S in range(N) if S&bit))
        test(ei==Q(sum(f[x]!=f[x^bit] for x in range(N)),N))
        residual={}; derivative={}; fullD={}; fullM={}; rsum=musum=Q(0)
        for S in range(N):
            if S&bit: continue
            low,high=p[S],p[S|bit]; row=low+high
            U=S&((1<<r)-1)
            residual[U]=residual.get(U,Q(0))+row
            derivative[U]=derivative.get(U,Q(0))+high
            rsum+=row
            if high:
                musum+=high/ei
                logadd(fullD,high/(ei*row),high)
                logadd(fullM,row/high,high)
        test(rsum==1)
        if not ei:
            test(musum==0); test(not fullD); continue
        test(musum==1)
        quotientD={}; quotientM={}
        for U,rr in residual.items():
            high=derivative.get(U,Q(0))
            if high:
                logadd(quotientD,high/(ei*rr),high)
                logadd(quotientM,rr/high,high)
            expected=1+delta*(a*a+qa[bit]**2-1) if U==0 else delta*(qa[U]**2+qa[U|bit]**2)
            test(rr==expected)
            test(high==delta*qa[U|bit]**2)
        loss=combine((fullD,1),(quotientD,-1))
        test(loss==combine((quotientM,1),(fullM,-1)))
        beta=qa[bit]; R=1+delta*(a*a+beta*beta-1)
        D0={}
        if beta:
            for sigma in [-1,1]:
                c=1-2*alpha*sigma*t+delta*(alpha*alpha+beta*beta)
                logadd(D0,R/c,(1+sigma*t)/2)
        test(loss==combine((D0,delta*beta*beta)))
        low,high=bound(loss)
        if loss: test(low>=0)
        if d>=4: test(high<=Q(256,9)*delta*delta*beta*beta)
        loss_total=combine((loss_total,1),(loss,1))
        if q==(1,1,1,-1):
            jensen=(1+delta-3*delta*delta/4)/(1+delta*delta/4)
            J={}; logadd(J,jensen,1)
            # Bits allowance L/e<1/8 is equivalent to natural loss<e*ln2/8.
            margin=combine(({2:ei/Q(8)},1),(loss,-1))
            test(bound(margin)[0]>0)
            test(bound(combine((J,delta*beta*beta),(loss,-1)))[0]>=0)
        records.append({'i':i,'e':str(ei),'loss_prime_logs':{str(k):str(v) for k,v in loss.items()}})
    _,totalhi=bound(loss_total)
    if d>=4: test(totalhi<=Q(256,9)*delta*delta*Iq)
    if q==(1,1,1,-1):
        # A100 loss is <delta^2/(2ln2) bits, equivalent to <delta^2/2 nats.
        test(totalhi<delta*delta/2)
        test(bound(combine(({2:delta/Q(8)},1),(loss_total,-1)))[0]>0)
        test(delta/Q(8)<=(1+delta)/40)
    return r,records

cases=rows=0
for d in ([4] if mode=='pilot' else [4,6]):
    for r in ([1,2] if mode=='pilot' else [1,2,3]):
        for mask in range(1<<(1<<r)):
            q=tuple(1 if mask>>x&1 else -1 for x in range(1<<r))
            rr,recs=check(q,d)
            cases+=1; rows+=rr
test(cases==(20 if mode=='pilot' else 552))
special=0
if mode=='full':
    for d in [2,4,6]:
        check((1,1,1,-1),d); special+=1
        for mask in range(16):
            spectator=tuple(1 if mask>>x&1 else -1 for x in range(4))
            check((1,1,1,-1),d,spectator); special+=1
    test(special==51)
    test(77**4<2*65**4)
out={'mode':mode,'gate_cases':cases,'control_rows_including_irrelevant':rows,'special_AND_spectator_cases':special,
     'assertions':ns['assertions'],'elapsed_seconds':time.perf_counter()-started,
     'arithmetic':'Direct signed truth tables, integer Walsh, Fraction physical edges, exact prime-log identities, 24-term rational enclosures for inequalities',
     'independence':'Own checker; no A073/A100 code loaded; full residual law and quotient both checked from actual spectra.'}
(run/'out').mkdir(exist_ok=True)
(run/'out'/('CHECK_'+mode.upper()+'.json')).write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps(out))
