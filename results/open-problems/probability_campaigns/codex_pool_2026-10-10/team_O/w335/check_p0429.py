from fractions import Fraction as F
from math import comb, exp, prod
import json
import pathlib
import time
from bundle_tools import emit, entry, edge_to_problem, edge_to_attempt

root = pathlib.Path(__file__).resolve().parent
start = time.perf_counter()
cases = 0
for n in range(2, 19):
    for k in range(1, n+1):
        distribution = {h:F(comb(k,h)*comb(n-k,k-h),comb(n,k)) for h in range(max(0,2*k-n),k+1)}
        assert sum(distribution.values()) == 1
        moments = []
        for r in (1,2,3):
            lhs = sum(probability * prod(range(h-r+1,h+1)) if h>=r else 0 for h,probability in distribution.items())
            rhs = F(prod(range(k-r+1,k+1))**2,prod(range(n-r+1,n+1))) if k>=r and n>=r else F(0)
            assert lhs == rhs
            moments.append(rhs)
        multiple = sum(probability for h,probability in distribution.items() if h>=2)
        assert moments[1]/2-moments[2]/2 <= multiple <= moments[1]/2
        rate = F(n,k)
        assert rate*moments[1] == F(k*(k-1)**2,n-1)
        cases += 1
boundary = []
for k in (5,10,20,40,80):
    n = k**3
    total = comb(n,k)
    multiple = 1-F(comb(n-k,k),total)-F(k*comb(n-k,k-1),total)
    beta = F(n,k)*multiple
    boundary.append({'n':n,'k':k,'beta_for_lambda_1':float(beta),'path_tv_lower_for_T_1':1-exp(-float(beta))})
measurement = {'command':'python -X utf8 check_p0429.py','exhaustive_hypergeometric_cases':cases,'boundary':boundary,'limiting_lower_c_1':1-exp(-0.5),'elapsed_seconds':round(time.perf_counter()-start,6),'result':'PASS'}
(root/'p0429_measurement.json').write_text(json.dumps(measurement,indent=2),encoding='utf-8')
statement = 'For n servers, Poisson jobs of rate lambda*n/k routing to uniform k-subsets, and k tagged arrival streams observed exactly on [0,T], let H count tagged servers hit per job and beta=(lambda*n/k)*P(H>=2). Their joint path total variation from independent rate-lambda Poisson streams is at least 1-exp(-beta*T). If k tends to infinity with k=o(sqrt(n)), beta~lambda*k^3/(2*n). At k/n^(1/3)->c>0, the liminf is at least 1-exp(-lambda*T*c^3/2). Conversely k=o(n^(1/3)) gives path TV tending to zero by the delete-and-restore coupling. This proves a path-coupling obstruction, not a necessary threshold for a stationary queue vector at a single time.'
proof = (root/'P0429_proof.md').read_text(encoding='utf-8').split('The total variation distance',1)[1].split('\n\nIf each arrival',1)[0]
new = entry('p0429-path-collision-obstruction','probability.queueing','uniform-batch-arrival-path-cubic-collision-obstruction','lemma','Sharp cubic collision scale for batch arrival paths',statement,'The total variation distance'+proof,['Poisson jobs with independent uniform routing','lambda,T fixed and positive','Exact continuous arrival paths','For the asymptotic formula: k tends to infinity and k=o(sqrt(n))'])
emit(2,'P0429',[new],[edge_to_problem('P0429',new['key'],'This proves a path-coupling obstruction'),edge_to_attempt('P0429',new['key'],'beta~lambda*k^3/(2*n)','A finite-horizon input coupling suggests a cubic collision scale')],'P0429_proof.md','p0429_measurement.json')
print(json.dumps(measurement),flush=True)
