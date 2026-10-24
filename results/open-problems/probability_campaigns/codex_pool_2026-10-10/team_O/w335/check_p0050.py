from fractions import Fraction as F
from math import comb
import json
import pathlib
import time
from bundle_tools import emit, entry, edge_to_problem, edge_to_attempt

root=pathlib.Path(__file__).resolve().parent
start=time.perf_counter()
cases=0
diagnostics=[]
for n in range(1,41):
    delta=F(1,2)
    D=n*delta**2
    variance=n*delta**2*F(3,4)*F(1,4)
    assert variance<=D/4
    mu_error=sum(F(comb(n,k)*3**k,4**n) for k in range(n+1) if 2*k<=n)
    nu_error=sum(F(comb(n,k)*3**(n-k),4**n) for k in range(n+1) if 2*k>n)
    assert mu_error<=1/D and nu_error<=1/D
    if n in (4,8,16,32,40):
        diagnostics.append({'n':n,'squared_gap_sum':float(D),'mu_midpoint_error':float(mu_error),'nu_midpoint_error':float(nu_error),'chebyshev_upper':float(1/D)})
    cases+=1
mu_first,nu_first=F(3,5),F(2,5)
assert mu_first/nu_first==F(3,2)
assert (1-mu_first)/(1-nu_first)==F(2,3)
assert (mu_first-nu_first)**2==F(1,25)
measurement={'command':'python -X utf8 check_p0050.py','exact_binomial_midpoint_cases':cases,'finite_coordinate_density_values':['3/2','2/3'],'diagnostics':diagnostics,'elapsed_seconds':round(time.perf_counter()-start,6),'result':'PASS'}
(root/'p0050_measurement.json').write_text(json.dumps(measurement,indent=2),encoding='utf-8')
statement='Let mu and nu be laws of countably many zero-one indicators X_i, pairwise negatively correlated under each law. Suppose delta_i=E_mu X_i-E_nu X_i>=0 and sum_i delta_i^2=infinity. Then mu and nu are mutually singular. The criterion needs no common invariant group action. Its application to distinct free and wired spanning-forest laws requires checking the ordered-marginal, negative-correlation and divergent-squared-gap hypotheses; that divergence is not proved for arbitrary networks here.'
proof=(root/'P0050_proof.md').read_text(encoding='utf-8').split('Proof. ',1)[1].split('\n\nThis applies',1)[0]
new=entry('p0050-square-gap-singularity','probability.random-graphs','negative-correlation-divergent-squared-marginal-gap-singularity','lemma','Singularity from a divergent squared marginal gap',statement,proof,['Countable indicator coordinates','Pairwise nonpositive covariances under both laws','Ordered marginal probabilities','Divergent sum of squared marginal differences'])
boundary=entry('p0050-finite-gap-boundary','probability.random-graphs','finite-coordinate-bernoulli-change-equivalent-measures','lemma','Finite marginal differences need not imply singularity','The independent Bernoulli product laws with first-coordinate parameters 3/5 and 2/5 and all other parameters 1/2 are distinct but equivalent. Their squared marginal-gap sum is 1/25. This example shows the preceding sufficient criterion cannot discard its divergence hypothesis or replace it by distinctness alone.','Only the first-coordinate density changes. The Radon-Nikodym derivative is 3/2 on X_1=1 and 2/3 on X_1=0, strictly positive and finite everywhere.',['Independent Bernoulli coordinates','Exactly one changed coordinate'])
relations=[edge_to_problem('P0050',new['key'],'The criterion needs no common invariant group action'),edge_to_attempt('P0050',new['key'],'sum_i delta_i^2=infinity','Arbitrary networks may lack it','analogous_to'),{'from_key':boundary['key'],'to_key':new['key'],'kind':'semantic_association','rationale':'Boundary card: "squared marginal-gap sum is 1/25"; criterion card: "sum_i delta_i^2=infinity". The boundary prevents dropping the divergence hypothesis.'}]
emit(4,'P0050',[new,boundary],relations,'P0050_proof.md','p0050_measurement.json')
print(json.dumps(measurement),flush=True)
