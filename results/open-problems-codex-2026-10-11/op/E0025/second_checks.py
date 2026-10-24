import fractions,json,pathlib,mpmath as mp
F=fractions.Fraction
grid=[F(1,10),F(1,4),F(1,2),F(3,4),F(9,10),F(99,100)]
parameter_checks=[]
for a in grid:
 for b in grid:
  if not a<b: continue
  crit=b*(1-a)/(a*(1-b)); K=crit+F(1,2)
  lo=b/a; hi=K*(1-b)/(1-a)
  p=(2*lo+hi)/3; q=(lo+2*hi)/3; t=(1+q/p)/2
  assert b<p*a and p<q and q*(1-a)<K*(1-b)
  assert 1<t and p*t<q
  parameter_checks.append({k:str(v) for k,v in dict(alpha=a,beta=b,K=K,Kcrit=crit,p=p,q=q,window_power=t).items()})
atomic_checks=[]
for a in grid:
 m=1
 while (2*m*m-m)/a <= F(m)/(1-a): m+=1
 exact_gap=F(2*m*m-m)/a-F(m)/(1-a)
 assert exact_gap>0
 atomic_checks.append({'alpha':str(a),'first_incompatible_m_for_C_1':m,'log2_u_lower_minus_log2_v_upper':str(exact_gap)})
mp.mp.dps=80
affinity_checks=[]
for a,b in [(mp.mpf('.1'),mp.mpf('1')),(mp.mpf('1'),mp.mpf('10')),(mp.mpf('10'),mp.mpf('100'))]:
 exact=mp.exp(-(mp.sqrt(a)-mp.sqrt(b))**2/2)
 partial=mp.exp(-(a+b)/2)*sum((mp.sqrt(a*b))**k/mp.factorial(k) for k in range(500))
 rel=abs(partial-exact)/exact
 assert rel<mp.mpf('1e-70')
 affinity_checks.append({'a':str(a),'b':str(b),'relative_error':mp.nstr(rel,12)})
out={'parameter_grid':'Exact Fraction arithmetic; 15 ordered alpha,beta pairs',
 'parameter_checks':parameter_checks,'atomic_C1_checks':atomic_checks,
 'poisson_affinity_checks_80_digits':affinity_checks}
pathlib.Path('second_checks.json').write_text(json.dumps(out,indent=2),encoding='utf8')
print('Exact parameter cases:',len(parameter_checks),'atomic cases:',len(atomic_checks),'Poisson affinity cases:',len(affinity_checks))
print(json.dumps(atomic_checks))
