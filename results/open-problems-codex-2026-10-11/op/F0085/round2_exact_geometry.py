from pathlib import Path
p=Path('round2_experiment.py');s=p.read_text(encoding='utf8')
s=s.replace('import numpy as np,json,time,math','import numpy as np,json,time,math\nfrom fractions import Fraction')
s=s.replace('allrows=[]','''delta=Fraction(71,1000);delta2=delta*delta
qfrac=[Fraction(float(t)) for t in qa];qpoints=[(x,y) for y in qfrac for x in qfrac]
gap=max(y-x for x,y in zip(qfrac,qfrac[1:]));assert gap*gap<=2*delta2
assert qfrac[0]==Fraction(-3,2) and qfrac[-1]==Fraction(3,2)
allrows=[]''')
s=s.replace("margin=float(np.max(np.sqrt(r2)[None,:]-dq,axis=1).min())",'''margins=np.max(np.sqrt(r2)[None,:]-dq,axis=1);margin=float(margins.min())
   cfrac=[(Fraction(float(x)),Fraction(float(y))) for x,y in centres];rfrac=[Fraction(float(x)) for x in r2]
   exact_cover=False;exact_hole=False
   if margin>float(delta):
    best=np.argmax(np.sqrt(r2)[None,:]-dq,axis=1);exact_cover=True
    for qi,(x,y) in enumerate(qpoints):
     ci=int(best[qi]);cx,cy=cfrac[ci];d2=(x-cx)**2+(y-cy)**2;b=rfrac[ci]-d2-delta2
     if not (b>0 and b*b>4*d2*delta2):exact_cover=False;break
   elif margin<=0:
    x,y=qpoints[int(np.argmin(margins))]
    exact_hole=all((x-cx)**2+(y-cy)**2>=rfrac[ci] for ci,(cx,cy) in enumerate(cfrac))''')
s=s.replace("'certified_by_net' if margin>net_radius else 'uncovered_witness' if margin<=0 else 'inconclusive'","'certified_by_net' if exact_cover else 'uncovered_witness' if exact_hole else 'inconclusive'")
s=s.replace("query_net_radius=net_radius,domain=","query_net_radius=net_radius,exact_net_radius='71/1000',geometry_check='Exact Fraction inequalities for cover margins and uncovered witnesses, for the floating squared radii interpreted as rationals',domain=")
p.write_text(s,encoding='utf8')
print('Added exact rational geometry verification to the surrogate experiment.')
