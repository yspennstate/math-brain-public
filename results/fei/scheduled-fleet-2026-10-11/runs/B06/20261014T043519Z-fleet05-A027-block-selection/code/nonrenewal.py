import json,time
from pathlib import Path
import exact as x
Q=x.Q; ROOT=Path(__file__).resolve().parents[1]; START=time.monotonic(); checks=0; records=[]
def check(ok):
    global checks
    assert ok; checks+=1
    if time.monotonic()-START>60: raise RuntimeError('frozen60-second cap')
for m in range(2,9):
    for r in [1,2,3]:
        p=Q(1,1<<r); delta=Q(1,1<<m); original=2*r*p*delta
        future=sum((Q(1,1<<k)*r*p*Q(1,1<<(m-k-1)) for k in range(m-1)),Q(0))
        check(future==(m-1)*original)
        terminal_ctrl=Q(1,1<<(m-1))*r*p
        check(terminal_ctrl==original)
        core_queries=2*(m-1)*p*delta; terminal_total=2*(r+1)*p*delta; rootI=2*(m+r)*p*delta
        check(rootI==core_queries+terminal_total)
        if m<=5 and r<=2:
            core=tuple(-1 if t==0 else 1 for t in range(1<<m)); ctrl=tuple(-1 if t==0 else 1 for t in range(1<<r)); F=x.activate(core,ctrl)
            check(x.I(F)==rootI); actual_drop={}; leafH={}; actualI=Q(0)
            for k in range(m-1):
                f=x.restrict(F,tuple((j,0) for j in range(k))); g=x.restrict(f,((0,0),)); h=x.restrict(f,((0,1),)); weight=Q(1,1<<k)
                check(set(h)=={1})
                drop=x.add((1,x.H(f)),(-Q(1,2),x.H(g)))
                bill=x.inf(f,0); actualI+=weight*bill
                check(x.bounds(drop)[1]<=6*bill)
                actual_drop=x.add((1,actual_drop),(weight,drop))
            final=x.restrict(F,tuple((j,0) for j in range(m-1)))
            leafH=x.add((Q(1,1<<(m-1)),x.H(final)))
            check(x.I(final)*Q(1,1<<(m-1))==terminal_total)
            check(actualI==core_queries)
            check(x.H(F)==x.add((1,actual_drop),(1,leafH)))
            check(x.bounds(actual_drop)[1]<=6*core_queries)
        records.append({'m':m,'r':r,'control_bank':str(original),'accumulated_future_debit':str(future),'ratio':m-1,'terminal_control_bank':str(terminal_ctrl)})
out={'status':'PASS','cases':21,'assertions':checks,'records':records,'elapsed_seconds':time.monotonic()-START,'arithmetic':'exact rational compressed boundary formulas; independent explicit integer Walsh/physical-edge checks at m2..5 r1,2','refuted_helper':'sum w B_future<=original unqueried control bank for every proper core-only tree','minimal_record':{'m':3,'r':1,'ratio':2},'scope':'unsigned sufficient-reserve renewal fails; actual entropy tree is paid at6; not an FEI disproof'}
(ROOT/'out'/'nonrenewal.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'status':out['status'],'cases':out['cases'],'assertions':checks,'elapsed_seconds':out['elapsed_seconds'],'minimal_record':out['minimal_record']}))
