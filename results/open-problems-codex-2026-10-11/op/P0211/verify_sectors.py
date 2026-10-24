import numpy as np, math,json,pathlib
from verify import cert

def radial(n,b,l):
 ks=np.arange(max(1,l),n-l+1); A=np.zeros((len(ks),len(ks)))
 for z,k in enumerate(ks):
  up=b*(n-k-l); down=(k-1)*(k-l)/n; kill=l*b+l*(k-1)/n
  A[z,z]=up+down+kill
  if z+1<len(ks):A[z,z+1]=-up
  if z>0:A[z,z-1]=-down
 return np.sort(np.linalg.eigvals(A).real)
def edge(n,b):
 masks=list(range(1,2**n));Q=np.zeros((len(masks),len(masks)))
 for z,m in enumerate(masks):
  k=m.bit_count()
  for i in range(n):
   target=m^(1<<i);rate=(k-1)/n if m>>i&1 else b
   if rate>0:Q[z,target-1]-=rate;Q[z,z]+=rate
 return np.sort(np.linalg.eigvals(Q).real)
rows=[]
for n in range(2,10):
 for b in [1e-5,1/n,1,100]:
  actual=edge(n,b);pieces=[]
  for l in range(n//2+1):
   ev=radial(n,b,l); mult=math.comb(n,l)-(math.comb(n,l-1) if l else 0);pieces.extend(list(ev)*mult)
  pred=np.sort(pieces);error=max(abs(pred-actual));
  rows.append({'n':n,'beta':b,'sector_spectrum_error':float(error),'radial_gap':float(radial(n,b,0)[1]),'radial_lower':b+2/n,'radial_upper':b+2})
print(json.dumps(rows,indent=2));pathlib.Path('sector_checks.json').write_text(json.dumps(rows,indent=2),encoding='utf8')
