from pathlib import Path
import json,time
R=Path(__file__).resolve().parents[1]
source=(R/'code/certify.py').read_text(encoding='utf-8').split('cases=')[0]
exec(compile(source,str(R/'code/certify.py'),'exec'))
m=64;mu=F(1,1<<m);t=(1-mu)/2;v=1-(1-t)**2/4
clo=1-F(15,16)**(2*m);ck(clo>F(1,2))
ck(2*11**2*14**4<15**6)
groups=[(F(1,2),2),(t/2,1),(F(1,8),2*m)]
parts=[]
for d,n in groups:
 low=hb(clo*d/v);high=hb(d/v)
 parts.append(n*min(low[0],high[0]))
# Entropy of a Bernoulli product conditioned to be nonempty:
# H(Q)=h(v)+v/c * (sum h(theta_i)-h(c)).
# Concavity puts each h(theta_i) above the smaller endpoint value;
# c>1/2 implies h(c)<=h(clo), and v/c>=v.
inside=sum(parts)-hb(clo)[1];ck(inside>0)
lower=hb(v)[0]+v*inside;I0=1+t/2+F(m,4);excess=lower-4*I0
ck(excess>F(3,2))
obj={'status':'PASS','cases':1,'assertions':CHECKS,'runtime_seconds':time.perf_counter()-START,'method':'analytic normalizer bound plus conditional product entropy; no bisection','CE_lower':str(lower),'CE_minus_4I_lower':str(excess),'display_only':float(excess),'arithmetic_independence':'same rational log primitive; different mathematical bounding representation'}
(R/'out/ALTERNATE.json').write_text(json.dumps(obj,indent=2),encoding='utf-8');print(json.dumps(obj))
