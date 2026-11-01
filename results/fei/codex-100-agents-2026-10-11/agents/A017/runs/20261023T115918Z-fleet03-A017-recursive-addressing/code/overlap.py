import json,hashlib
from pathlib import Path
from fractions import Fraction as F
from check import split,derivative_metrics,H,influence,totalI
R=Path(__file__).resolve().parents[1]
spec=json.loads((R/'out/overlap_spec.json').read_text(encoding='utf-8'))
assert spec['helper_version']=='A017-overlapping-character-counterexample-v1'
b=[1,1,1,-1];c=[1,1,-1,-1];f=[a*z for a,z in zip(b,c)]
assert f==[1,1,-1,1]
a,z,_=split(f,[0,1],0);p,e=derivative_metrics(a,z)
assert p==F(1,2) and e==F(1,4) and totalI(c)==1
assert H(f)==H(f,True)=={2:F(2)} and H(a)==H(z)=={}
ab,bb,_=split(b,[0,1],0);pb,eb=derivative_metrics(ab,bb)
assert pb==p and eb==F(1,4) and e!=eb+p*totalI(c)
# ln2>2/3 implies3/(2ln2)-1/2<7/4<Delta=2.
assert F(7,4)<2
d=[F(x-y,2) for x,y in zip(ab,bb)]
cv=[1,-1];dc=[x*y for x,y in zip(d,cv)]
edge_shift=sum(d[x]*d[x^1] for x in range(2) if cv[x]!=cv[x^1])/2
assert edge_shift==e-eb==0
result=dict(status='PASS',b=b,c=c,f=f,selected_influence=str(p),derivative_energy=str(e),
 actual_entropy_debit_bits='2',context_influence='1',false_product_energy='3/4',
 invalid_refunded_bound_strict_upper='7/4',signed_edge_correction=str(edge_shift),
 interpretation='Disjoint spectator subtraction does not extend to overlapping unqueried characters.',
 helper_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())
(R/'out/overlap_counterexample.json').write_bytes((json.dumps(result,indent=2)+'\n').encode('utf-8'))
print('PASS: actual two-bit overlap counterexample, exact entropy/edge energies, signed correction')
