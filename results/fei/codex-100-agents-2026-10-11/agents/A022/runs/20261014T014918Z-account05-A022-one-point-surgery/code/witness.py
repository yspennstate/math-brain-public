from pathlib import Path
from fractions import Fraction as Q
import json,time
RUN=Path(__file__).resolve().parents[1];source=RUN/'code/check.py'
ns={'__file__':str(source),'__name__':'witness_kernel'}
exec(source.read_text(encoding='utf-8').split('\ncases=0')[0],ns)
START=time.perf_counter();results=[];checks=0
for k in (4,6,8):
    # Direct controller-first truth ordering: controller bit0, then natural data.
    f=tuple(ns['bent'](u>>1,k)*(-1 if not (u&1) and (u>>1)==0 else 1) for u in range(1<<(k+1)))
    raw,dnum=ns['ns']['ns']['packet_expr'](f);N=len(f);B=tuple((p,Q(c,N*N)) for p,c in raw)
    d=Q(dnum,N*N);assert d==Q(1,1<<k);checks+=1
    lo,hi=ns['interval'](B);assert lo/d>=k-2;checks+=1
    if k==8:assert lo>4*d;checks+=1
    results.append({'kind':'controller-first point switch','k':k,'d':str(d),
        'B_over_d_interval':[str(lo/d),str(hi/d)],'B_prime_expression':[(p,str(c)) for p,c in B],
        'K4_bad_certified':lo>4*d,'counterclaim':'No refutation of tree payment: data-first paired access is good.'})
for op in ('OR','XOR'):
    mask=0
    for z in range(16):
        x=[(z>>j)&1 for j in range(4)];events=[x[1]*x[2],x[1]*x[3],x[0]*x[2]*x[3]]
        active=any(events) if op=='OR' else sum(events)%2
        if active:mask|=1<<z
    for k in (4,8):
        a=tuple(-1 if (mask>>z)&1 else 1 for z in range(16));Ha,ia=ns['stats'](a);Ia=sum(ia);alpha=Q(mask.bit_count(),16)
        f=ns['truth'](k,4,0,mask);H,inf=ns['stats'](f)
        removed,leafdata,leafctrl,_,leafH=ns['walk'](f,k,4,0,mask,Ha,Ia,alpha)
        assert sum(inf[:k])==removed+leafdata and sum(inf[k:])==leafctrl;checks+=1
        assert ns['interval'](ns['add']((1,H),(-Q(1,1<<k),Ha)))[1]<=7*sum(inf[:k]);checks+=1
        results.append({'kind':'three overlapping events','operator':op,'controller_mask':mask,'k':k,'t':4,
            'alpha':str(alpha),'I_data':str(sum(inf[:k])),'I_ctrl':str(sum(inf[k:])),
            'I_terminal_data':str(leafdata),'inherited_H_coefficient':str(Q(1,1<<k)),'access_bad_credit':'0'})
result={'cases':7,'checks':checks+ns['CHECKS']+ns['ns']['CHECKS']+ns['ns']['ns']['ASSERTIONS'],
    'runtime_seconds':time.perf_counter()-START,'verdict':'PASS','records':results}
(RUN/'out/CONTRAST_OVERLAP_WITNESSES.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:v for k,v in result.items() if k!='records'}))
