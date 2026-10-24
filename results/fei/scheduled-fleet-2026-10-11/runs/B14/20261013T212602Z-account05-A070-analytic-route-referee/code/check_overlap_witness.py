from pathlib import Path
from fractions import Fraction as Q
import json
run=Path(__file__).resolve().parents[1]
def char(v):return [sum(t*(-1 if (s&x).bit_count()%2 else 1) for x,t in enumerate(v)) for s in range(8)]
g=[(1-2*(x&1))*(1-2*((x>>2)&1)) for x in range(8)]
D1={x for x in range(8) if x&3==0};D2={x for x in range(8) if x&3==1}
e1=[-2*t if x in D1 else 0 for x,t in enumerate(g)]
e2=[-2*t if x in D2 else 0 for x,t in enumerate(g)]
f=[t+u+v for t,u,v in zip(g,e1,e2)]
L=[1+2*bool(s)+2*bool(s&3) for s in range(8)]
a,b,c,d=[char(v) for v in [g,e1,e2,f]]
energy=lambda v:Q(sum(t*t*l for t,l in zip(v,L)),64)
cross=Q(sum(u*v*l for u,v,l in zip(b,c,L)),64)
assert D1.isdisjoint(D2)
assert all(abs(t)==1 for t in f)
assert cross==Q(1,2)
assert energy(b)==energy(c)==Q(9,2)
assert energy([u+v for u,v in zip(b,c)])==10
assert energy(a)==energy(d)==5
assert f==[-(1-2*(x&1))*(1-2*((x>>1)&1))*(1-2*((x>>2)&1)) for x in range(8)]
out={'status':'PASS','exact_assertions':7,'cases':1,'truth_g':g,'truth_f':f,'D1':sorted(D1),'D2':sorted(D2),'physical_intersection_density':'0','retained_cores':['y','-y'],'signed_cross':str(cross),'single_energies':[str(energy(b)),str(energy(c))],'total_difference_energy':'10','Gamma_g':str(energy(a)),'Gamma_f':str(energy(d)),'lengths':L}
(run/'out/PROPER_SUBCUBE_WITNESS.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps(out))
