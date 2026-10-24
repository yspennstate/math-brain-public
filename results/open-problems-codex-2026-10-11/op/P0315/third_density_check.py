import pathlib,sympy as S,json
b,r,z=S.symbols('b r z',nonzero=True);I=S.I
C={(0,0):S.Integer(1)}
for k in range(1,6):C[k,0]=0;C[k,1]=I*(1+2/b) if k==1 else 0
for j in range(1,3):
 for k in range(1,5):
  C[k,j+1]=S.factor(((4*k*k/b-j)*C.get((k,j),0)-(2*k*k/b-k)*C.get((k+1,j),0)-(2*k*k/b+k)*C.get((k-1,j),0))/(I*k))
F=S.Integer(1)
for k in range(1,4):
 for j in range(1,4):
  ck=C[k,j]
  assert ck==0 or (j%2==0 and not ck.has(I)) or (j%2==1 and not S.simplify(ck/I).has(I))
  conj=ck if j%2==0 else -ck
  F+=(ck*z**(-k)+conj*z**k)/r**j
D=lambda f:I*z*S.diff(f,z);co=(z+z**-1)/2;si=(z-z**-1)/(2*I)
res=S.factor(S.diff(F,r)+D(F)-(4/b*D(D((1-co)*F))+2*D(si*F))/r)
pol=S.expand(res*r**4)
assert not pol.has(r)
assert S.expand(pol).coeff(z,0)==0
assert all(abs(int(term.as_powers_dict().get(z,0)))<=4 for term in S.expand(pol).as_ordered_terms())
p=pathlib.Path('second_checks.json');d=json.loads(p.read_text());d['third_column_coefficients']={str(k):str(C[k,3]) for k in range(1,4)};d['third_density_residual']='exactly r^(-4), zero mass, Fourier degree at most 4';p.write_text(json.dumps(d,indent=2),encoding='utf8');print('Third-density actual residual and imaginary parity verified exactly.')
