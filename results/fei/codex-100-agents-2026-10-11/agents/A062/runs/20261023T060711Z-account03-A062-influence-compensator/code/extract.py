"""Recheck exact executed witness signs and independently reproduce A061's guard."""
from pathlib import Path
from fractions import Fraction as F
import json,sys
sys.dont_write_bytecode=True
import kernel as k
from check import plus,scale,log,hb,kl_atoms,serial
from coupled import spectrum,marginals,marginal_product
r=Path(__file__).resolve().parents[1]
o=json.loads((r/'out/COUPLED.json').read_text(encoding='utf-8'))
candidates=[(rr,c) for rr in o['results'] for c in rr['children'] if all(rr['root_block_eligible']) and c['coupling'][0]>0]
k.check(bool(candidates))
financial=[(rr,c) for rr,c in candidates if c['T'][0]>0 and sum(t[1] for t in c['block_T'])<0]
rr,c=max(financial or candidates,key=lambda pair:pair[1]['coupling'][0])
lo=F((c['coupling'][0]*65536)//k.SCALE,65536)
k.check(lo>0 and F(c['coupling'][0],k.SCALE)>lo)
negative=min(((rr,c) for rr in o['results'] for c in rr['children'] if c['coupling'][1]<0),key=lambda pair:pair[1]['coupling'][1])
nr,nc=negative
hi=F(-((-nc['coupling'][1]*65536)//k.SCALE),65536)
k.check(F(nc['coupling'][1],k.SCALE)<hi<0)
selected={'eligible_root_positive_tax_rows':len(candidates),'eligible_root_positive_global_negative_local_rows':len(financial),'positive':{'widths':rr['widths'],'flip':rr['flip'],'original_reference':rr['original_reference'],'root':rr['root'],'child':c,'strict_coupling_lower':lo},'negative':{'widths':nr['widths'],'flip':nr['flip'],'original_reference':nr['original_reference'],'child':nc,'strict_coupling_upper':hi},'warning':'positive witnesses do not retain all local eligibility; no fully eligible correlated extension is refuted or paid'}
k.check(F(c['T'][0],k.SCALE)>F(1,32))
k.check(F(sum(t[1] for t in c['block_T']),k.SCALE)<-F(1,4))
# Exact finite one-query stopping budget; no newly computed physical source/reference.
ALO=F(1)/k.L2[1];AHI=F(1)/k.L2[0];ledgers=[]
for row in o['results']:
 root=row['root'];I=F(root['I']);B=k.pos(tuple(root['T']));queries=[]
 for i in range(sum(row['widths'])):
  cc=[c for c in row['children'] if c['query']==i];k.check(len(cc)==2)
  predictions={c['outcome']:F(c['prediction']) for c in cc}
  O=kl_atoms({0:F(1,2),1:F(1,2)},predictions)
  E=k.sub(tuple(root['K']),plus(O,scale(plus(*(tuple(c['K']) for c in cc)),F(1,2))))
  k.check(E[1]>=0);E=(max(0,E[0]),E[1])
  influence=F(root['marginals'][i]);charge=(k.floor(ALO*influence*k.SCALE),k.ceil(AHI*influence*k.SCALE))
  candidate=plus(charge,k.sub(scale(plus(*(k.pos(tuple(c['T'])) for c in cc)),F(1,2)),E))
  B=(max(B[0],candidate[0]),max(B[1],candidate[1]));queries.append({'query':i,'E':E,'O':O,'Inf':influence,'charged_candidate':candidate})
 margin=3*ALO*I/4-F(B[1],k.SCALE);k.check(margin>0)
 ledgers.append({'widths':row['widths'],'flip':row['flip'],'original_reference':row['original_reference'],'I':I,'charged_one_query_B':B,'margin_after_old_quarter_lower':margin,'queries':queries})
normalized=min(v['margin_after_old_quarter_lower']/v['I'] for v in ledgers)
margin_bound=F((normalized*65536).numerator//(normalized*65536).denominator,65536)
k.check(normalized>margin_bound>0)
budget={'status':'PASS','roots':len(ledgers),'physical_child_rows':o['child_rows'],'original_owner':'a I_initial, a=log2(e)','old_consumption':'omega<=a I_initial/4 retained','charged_costs':'full inherited/product terminal KL plus actual O and a Inf for the one allowed query; root/child choices optimized','strict_residual_over_I_lower':margin_bound,'ledgers':ledgers,'scope':'frozen finite coupled sources only; no varying-width theorem'}
# Independently form the actual4-bit non-affine pivot control.
tt=bytes(int(bool(x&1) and ((x>>1)&7)==7) for x in range(16));p=spectrum(tt);R=p.copy();k.check(kl_atoms(p,R)==(0,0))
a,b=k.children(tt,0);q={s:F(0) for s in range(8)}
for s,v in p.items():q[s>>1]+=v
children=[]
for child in [a,b]:
 pc=spectrum(child);un={s:R.get(2*s,F(0))+R.get(2*s+1,F(0)) for s in q}
 un={s:un[s]*(pc[s]/(2*q[s]) if q[s] else F(1,2)) for s in q};pi=sum(un.values());k.check(pi==F(1,2));rc={s:v/pi for s,v in un.items()};k.check(rc==pc)
 product=marginal_product(marginals(pc,3));TC=kl_atoms(pc,product);H=plus(*(scale(log(v),-v) for v in pc.values() if v));children.append({'p':pc,'inherited_reference':rc,'actual_product':product,'TC':TC,'H':H})
cost=scale(plus(*(row['TC'] for row in children)),F(1,2));formula=plus((k.SCALE,k.SCALE),scale(log(F(3)),-F(9,16)))
diff=k.sub(cost,formula);k.check(diff[0]<=0<=diff[1] and cost[0]>0 and 2**16>3**9)
guard={'function':'F(v,y)=(-1)^(v*y0*y1*y2), v bit0','initial_reference':'actual source p_F','initial_K_exact':0,'initial_core_M_exact':0,'expected_actual_reset_KL':cost,'exact_formula':'1-(9/16)log2(3)','positive_integer_certificate':'2^16>3^9','children':children,'scope':'A061 non-affine extension guard only; not FEI counterexample'}
(r/'out/SELECTED_WITNESSES.json').write_text(json.dumps(serial(selected),indent=2)+'\n',encoding='utf-8')
(r/'out/A061_GUARD.json').write_text(json.dumps(serial(guard),indent=2)+'\n',encoding='utf-8')
(r/'out/COUPLED_LEDGER.json').write_text(json.dumps(serial(budget),indent=2)+'\n',encoding='utf-8')
print(json.dumps({'positive_tax_rows_from_eligible_roots':len(candidates),'positive_global_negative_local_rows':len(financial),'positive_witness':{s:selected['positive'][s] for s in ['widths','flip','original_reference']},'coupling_strict_lower':str(lo),'negative_coupling_strict_upper':str(hi),'one_query_budget':'PASS','strict_residual_over_I_lower':str(margin_bound),'auxiliary_assertions':k.ASSERTIONS,'guard':'PASS'}))
