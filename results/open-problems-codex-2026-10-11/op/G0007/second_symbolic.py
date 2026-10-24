import sympy as S,json,pathlib
l,d,h=S.symbols('l d h',positive=True); q=1-h
P2=h-q/(l*d)
P3=P2-q/(l*l*d*(d-1))
m=d*P2/h
fac=d*(d-1)*P3/h
var=S.factor(fac+m-m*m)
cov=S.factor(P3/h-(P2/h)**2)
assert S.simplify(var-(d-m)*(m-1/l))==0
assert S.simplify(cov-(d-m)*(l*(d-1)*m-d)/(l*d*d*(d-1)))==0
print('P2=',P2,'P3=',P3,'var=',var,'cov=',cov)
pathlib.Path('second_symbolic_checks.json').write_text(json.dumps({'healthy_pair_identity':str(P2),'healthy_path_triple_identity':str(P3),'conditional_degree_variance_identity_verified':True,'conditional_branch_covariance_identity_verified':True},indent=2))
