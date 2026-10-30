"""A017-quinary-maximum-physical-v2: direct maximum-profile Boolean realization."""
import sys
sys.dont_write_bytecode=True
from pathlib import Path
import importlib.util,json
R=Path(__file__).resolve().parents[1]
p=R.parent/'20261011T234546Z-fleet05-A017-recursive-addressing/code/check.py'
s=importlib.util.spec_from_file_location('u',p);U=importlib.util.module_from_spec(s);s.loader.exec_module(U)
certificate=json.loads((R/'out/quinary_certificate.json').read_text(encoding='utf8'));H=certificate['maximum_profile']
child=[1 if (x&3)<2+H[x>>2] else -1 for x in range(32)]
g=[-child[x>>1] if (x&1 and x>>3==0) else child[x>>1] for x in range(64)]
W=U.fwht(g);P=Q=1;mass=0
for s in range(0,64,2):
 a,b=W[s]//4,W[s+1]//4;t,u=a*a,b*b;mass+=u
 if t+u:P*=(t+u)**(t+u)
 if t:Q*=t**t
 if u:Q*=u**u
assert P*int(certificate['maximum_ratio_integer_form']['Q'])==Q*int(certificate['maximum_ratio_integer_form']['P']) and mass==32 and P<(Q<<128)
sp=U.spectrum(g,[0]*64);inf,pairs,C,dc=U.spectral_metrics(sp,6);physical=U.physical(g,[0]*64,6)
assert (inf,pairs,dc)==physical
result=dict(status='PASS',helper='A017-quinary-maximum-physical-v2',profile=H,actual_six_control_truth=g,influences=[str(t) for t in inf],B=U.erasure(sp,6,0).json(),C_selected=str(C[0]),certificate_positive_slack=str((Q<<128)-P),assertions=6,scope='maximum of all78125 normalized affine-plane/affine-phase selected erasures, physically realized')
(R/'out/QUINARY_PHYSICAL_MAXIMUM.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf8');print(json.dumps({k:result[k] for k in ['status','helper','influences','C_selected','assertions']}))
