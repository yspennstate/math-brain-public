import itertools,random,fractions,math,cmath,json,pathlib
F=fractions.Fraction;rng=random.Random(87)
def parity(p):return (-1)**sum(p[i]>p[j] for i in range(len(p)) for j in range(i+1,len(p)))
exact=0;worst=0
for n in range(1,5):
 for trial in range(15):
  a=rng.sample(range(-100,100),2*n);x=list(map(F,a[:n]));y=list(map(F,a[n:]));D=sum(F(parity(p))*math.prod(1/(x[i]-y[p[i]]) for i in range(n)) for p in itertools.permutations(range(n)))
  formula=F((-1)**(n*(n-1)//2))*math.prod(x[j]-x[i] for i in range(n) for j in range(i+1,n))*math.prod(y[j]-y[i] for i in range(n) for j in range(i+1,n))/math.prod(xi-yj for xi in x for yj in y)
  assert D==formula;exact+=1
checks=0
for n in range(1,6):
 for trial in range(30):
  x=[complex(rng.random(),rng.random()) for _ in range(n)];y=[complex(rng.random(),rng.random()) for _ in range(n)]
  if trial%3==0:y[0]=x[0]+(1+1j)*10**(-min(8,trial+1))
  for p in [.1,.32,.49]:
   logF=p*(sum(math.log(abs(x[j]-x[i]))+math.log(abs(y[j]-y[i])) for i in range(n) for j in range(i+1,n))-sum(math.log(abs(xi-yj)) for xi in x for yj in y))
   lhs=math.exp(logF);rhs=sum(math.prod(abs(x[i]-y[perm[i]])**(-p) for i in range(n)) for perm in itertools.permutations(range(n)))
   assert lhs<=rhs*(1+1e-12);worst=max(worst,lhs/rhs);checks+=1
res={'exact_rational_Cauchy_identity_checks':exact,'complex_matching_bound_checks':checks,'maximum_LHS_over_RHS':worst,'seed':87,'scope':'Gaussian power kernel only; no dimer collision bound tested'}
pathlib.Path('cauchy_checks.json').write_text(json.dumps(res,indent=2),encoding='utf8');print(res)
