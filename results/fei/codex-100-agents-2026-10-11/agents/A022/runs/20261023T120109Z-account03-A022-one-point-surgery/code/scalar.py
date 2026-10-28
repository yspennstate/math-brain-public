import json,time
from pathlib import Path
from exact import *
ROOT=Path(__file__).resolve().parents[1]; start=time.monotonic(); count=0;rows=[]
for m in range(3,13):
    n=2**m;a=(-1,)+(1,)*(n-1);P=spectrum(a);p0=Q((n-2)**2,n*n);p1=Q(4,n*n)
    assert P==[p0]+[p1]*(n-1);count+=1
    I=Q(2*m,n);assert sum(inf(a,i) for i in range(m))==I;count+=1
    r=[(p+Q(1,n))/2 for p in P];C=ce(P,r);H=entropy(P)
    assert bounds(plus(C,const(-Q(9,32))))[0]>0;count+=1
    assert bounds(plus(const(4*I),mul(H,-1)))[0]>0;count+=1
    vacuum=[p0]+[(1-p0)/Q(n-1)]*(n-1);assert vacuum==P;count+=1
    rows.append({'m':m,'I':str(I),'uniform_CE_lower_bound':'9/32','actual_H_over_I_upper_bound':'4','vacuum_calibrated_source_KL':'0'})
    assert time.monotonic()-start<60
assert Q(3,64)-Q(26,576)==Q(1,576);count+=1
for t in range(3,129):
    assert Q(t,16)-Q(1,8**t)>=Q(13*t,576);count+=1
out={'status':'PASS','point_family_cases':10,'assertions':count,'elapsed_seconds':time.monotonic()-start,'domain':'actual point functions m3..12; all-t analytic bound is in PROOF','rows':rows}
(ROOT/'out/scalar.json').write_text(json.dumps(out,indent=2),encoding='utf-8');print(json.dumps({k:v for k,v in out.items() if k!='rows'}))
