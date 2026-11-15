import json,mpmath as mp
from symmetric import mask_vector,evaluate
from pathlib import Path
mp.mp.dps=90
r=json.loads(Path('census_24.json').read_text());f=mask_vector(24,r['maxima']['B/I']['mask']);items=[]
for label,g in [('B extremizer',f),('remove isolated weight-1 minus',[1 if t==1 else x for t,x in enumerate(f)]),('replace final positive run by minus',f[:21]+[-1]*4),('pure threshold at 16',[1 if t<16 else -1 for t in range(25)])]:
 v=evaluate(g,90);items.append({'variant':label,'value_vector':v['value_vector'],'A/I':mp.nstr(v['A/I'],60),'B/I':mp.nstr(v['B/I'],60),'Gamma/I':mp.nstr(v['Gamma/I'],60)})
g=mask_vector(24,r['maxima']['Gamma/I']['mask']);v=evaluate(g,90)
items.append({'variant':'Gamma extremizer','value_vector':v['value_vector'],'B/I':mp.nstr(v['B/I'],60),'Gamma/I':mp.nstr(v['Gamma/I'],60),'2Gamma/B':mp.nstr(2*v['Gamma']/v['B'],60)})
large=json.loads(Path('refinement_high_precision.json').read_text())['metrics']
items.append({'variant':'n2000 refined Gamma witness','2Gamma/B':mp.nstr(2*mp.mpf(large['Gamma'])/mp.mpf(large['B']),60)})
print(json.dumps(items,indent=2))
