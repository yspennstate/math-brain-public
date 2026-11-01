from pathlib import Path
from fractions import Fraction as F
import json,time
import audit as A
ROOT=Path(__file__).resolve().parents[1]
start=time.perf_counter();fixtures=0
for mask in range(16):
 g=tuple(1 if (mask>>i)&1 else -1 for i in range(4))
 for R in [tuple([F(1,4)]*4),tuple(F(x,11) for x in [1,2,3,5]),A.stats(g)[0]]:
  bs=A.book(g,R,2)
  A.ge(A.lin((1,A.stats(g)[3]),(-1,bs[2])),'ALL physical policies bounded by single full-M owner')
  fixtures+=1
field=json.loads((ROOT/'out/FIELD.json').read_text(encoding='utf-8'))
physical=json.loads((ROOT/'out/PHYSICAL.json').read_text(encoding='utf-8'))
def expr(x):return {int(k):F(v) for k,v in x.items()}
for row in field['rows']:
 S=expr(row['Sbar']);W1=expr(row['W'][1]);W2=expr(row['W'][2]);l=row['l']
 A.gt(A.lin((F(1,50),S),(-1,W1)),'every first ordinary direction fits ORIGINAL S/50')
 A.gt(A.lin((F(5,7),S),(-1,A.const(3*l+2))),'new all-physical owner cap')
 A.gt(A.lin((F(3,4),S),(-1,A.const(3*l+2)),(F(-1,28),S)),'same owner old quarter and new remainder')
 if l==2:A.eq(W1,A.lin((F(1,2),expr(physical['new_H_booking']))),'actual interposed query attains complete first-query maximum')
h=A.core(2)
for g in [(1,)*64,h]:A.eq(A.stats(A.carrier(g,63))[3],A.const(8),'full actual GF4 child marginal envelope')
# For l>=3, write l=3+t, t>=0: 3l-8=1+3t>=1.
A.ck(F(5,7)*F(23,2)-8==F(3,14),'l2 exact original owner guard')
A.ck(F(5,7)*F(31,2)-11==F(1,14),'l3 lower-bound endpoint guard')
A.ck(F(5,7)*F(9,2)-3==F(3,14)>0,'positive all-l affine slope')
A.ck(field['queries']==219 and field['nodes']==440,'field policy coverage')
A.ck(time.perf_counter()-start<55,'extension frozen cap')
out={'status':'PASS','fixtures':fixtures,'assertions':A.COUNT,'seconds':time.perf_counter()-start,'new_all_physical_cap':'3l+2<5Sbar/7','remaining_after_old_quarter':'>Sbar/28','all_l_guard':'l=3+t implies 3l-8=1+3t>=1, t>=0','one_final_conversion_only':True}
(ROOT/'out/EXTENSION.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8',newline='\n');print(json.dumps(out))
