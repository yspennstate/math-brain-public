import numpy as np, scipy.linalg as la, json,pathlib
out=[]
for a in [6.,20.]:
 vals=[]
 for n in [10000,20000]:
  x=np.linspace(-6,100,n+2)[1:-1];dx=106/(n+1);y=2*np.exp(-x)
  es=la.eigh_tridiagonal(2/dx**2+(a-y)**2/4-y/2,np.full(n-1,-1/dx**2),select='i',select_range=(0,1))[0]
  vals.append(float(es[1]-es[0]))
 out.append({'a':a,'N10000_gap':vals[0],'N20000_gap':vals[1],'richardson_gap':(4*vals[1]-vals[0])/3,'exact_gap_for_a_ge_2':a-1})
pathlib.Path('morse_refinement.json').write_text(json.dumps(out,indent=2),encoding='utf8');print(json.dumps(out,indent=2))
