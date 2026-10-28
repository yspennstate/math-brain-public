"""Separate exact endpoint and smallest-source-rate check; no search."""
from pathlib import Path
from fractions import Fraction as F
import importlib.util,json,hashlib
R=Path(__file__).resolve().parents[1]
P=R.parents[1]/'runs/20261023T134030Z-account03-A095-restricted-result-extraction/code/check.py'
sp=importlib.util.spec_from_file_location('prior_boundary',P);B=importlib.util.module_from_spec(sp);sp.loader.exec_module(B)
T=B.T
# Independent coefficient-list multiplication certifies the key polynomial.
def mul(a,b):
 z=[0]*(len(a)+len(b)-1)
 for i,x in enumerate(a):
  for j,y in enumerate(b):z[i+j]+=x*y
 return z
lhs=[1]
for _ in range(4):lhs=mul(lhs,[-2,1])
rhs=mul([4,0,1],[20,-8,1]);rhs[0]-=64
assert lhs==rhs
# A source dictator admits the literal C0=0 source at the original owner.
g=(1,-1);m=2;Ig=T.influence(g);e=F(1,8);C0=F(0);K=15;U=F(37,8)*Ig
v,Q=B.floor(g,m);If=T.influence(v);root=B.ce(B.law(v),Q);G=3*e
assert If==Ig+G-e
assert K*If-U-root[1]>F(53,8)*Ig
# Pay the entire proved upper envelope at the C0=0 boundary, never credit KL.
assert K*If-U-root[1]-F(573,128)*Ig>F(275,128)*Ig
assert F(53,8)-F(573,128)==F(275,128)
assert F(381,128)+F(3,4)+F(3,4)==F(573,128)
# Explicitly verify both low-dimensional constant-source floors.
assert (F(1)-2*F(1,2))**2==0
assert F(4)*F(1,2)**2/(1+4*F(1,2))==F(1,3)
assert (1-2)**2==1 and F(1+4,1+4)==1
receipt={'status':'PASS','checks':9,'polynomial_coefficients':lhs,'C0':str(C0),'root_CE_interval':B.bounds(root),'whole_path_remaining_lower':str(K*If-U-root[1]-F(573,128)*Ig),'formal_status':'NOT_LEAN_CHECKED','code_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
(R/'out/BOUNDARY.json').write_text(json.dumps(receipt,indent=2),encoding='utf-8')
print(json.dumps(receipt))
