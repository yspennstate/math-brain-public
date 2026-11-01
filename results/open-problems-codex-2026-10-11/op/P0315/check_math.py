import pathlib, json, mpmath as mp, sympy as sp
mp.mp.dps=80
records=[]
for r in [mp.mpf(1),mp.mpf(3),mp.mpf(10),mp.mpf(100),mp.mpf(1000), 100*mp.pi,100*mp.pi+mp.mpf('1e-10'),100*mp.pi+mp.pi/2]:
 s,c=mp.sin(r),mp.cos(r)
 exact=-s*s/r**2+(c/r-s/r**2)*mp.si(r)
 appr=mp.pi*c/(2*r)-(1+mp.pi*s/2)/r**2+(2*c*c+s*s)/r**4
 err=abs(exact-appr);ratio=err*r**5/26
 assert ratio<=1
 records.append(dict(r=str(r),beta4_error=str(err),bound=str(26/r**5),fraction_of_bound=str(ratio)))
b=sp.Symbol('b',positive=True);I=sp.I
C={(0,0):sp.Integer(1)}
for k in range(1,7):C[k,0]=sp.Integer(0);C[k,1]=I*(1+2/b) if k==1 else sp.Integer(0)
for j in range(1,4):
 for k in range(1,6):
  D=4*k*k/b;A=2*k*k/b-k;B=2*k*k/b+k
  C[k,j+1]=sp.factor(((D-j)*C.get((k,j),0)-A*C.get((k+1,j),0)-B*C.get((k-1,j),0))/(I*k))
w=lambda k:sp.rf(-b/2,k)/sp.rf(1+b/2,k)
coeff={j:sp.factor(sum(w(k)*C[k,j] for k in range(1,j+1))) for j in [2,4]}
assert sp.simplify(coeff[2]+2/b)==0
for j in range(1,5):
 for k in range(1,6):
  if k>j:assert C[k,j]==0
pathlib.Path('checks.json').write_text(json.dumps({'beta4_remainders':records,'formal_weighted_coefficients':{str(j):str(v) for j,v in coeff.items()},'formal_coefficients':{f'{k},{j}':str(v) for (k,j),v in C.items() if j>0 and v!=0}},indent=2),encoding='utf8')
print('beta4 remainder checks passed:',len(records));print('Formal weighted coefficients',coeff)
