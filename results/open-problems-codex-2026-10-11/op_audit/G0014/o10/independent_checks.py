from pathlib import Path
from math import log, exp, e, ceil, floor, isclose
from fractions import Fraction as Q
import json, urllib.request
from scipy.optimize import brentq
from pypdf import PdfReader

root = Path(__file__).resolve().parent
theta = brentq(lambda x: log(2/(1+x)) + x/(1+x), 1, 10, xtol=1e-14)
f = log(2/(1+theta))
a = -f/theta
c = 1/a
b = 3/(2*theta)
results = {'binary_exp': {'theta':theta,'boundary_residual':f+theta/(1+theta), 'a':a,'c':c,'printed_c':-c,'correct_log_coefficient':b*c,'sign_repaired_printed_coefficient':b/c}}
# Exact first-generation mean cancellation at theta=3, Exp(1) edges.
t = Q(3)
rho = Q(2)/(1+t)
results['exact_mean_D1_at_theta3'] = str(Q(2)/rho * (1/(1+t)**2 - Q(1)/(1+t)*Q(1)/(1+t)))
# Exact row-parent countercheck: phi is a left eigenvector, not right.
M = [[Q(2),Q(1)],[Q(2),Q(1)]]
phi = [Q(2),Q(1)]
results['left_right_test'] = {'phi_T_M':[str(sum(phi[i]*M[i][j] for i in range(2))) for j in range(2)],'rho_phi':[str(3*x) for x in phi],'M_phi':[str(sum(M[i][j]*phi[j] for j in range(2))) for i in range(2)]}
# Independent inversion test on exact deterministic T_n=a*n+b*log(n).
def T(n): return a*n+b*log(n) if n else 0
inverse=[]
for time in [1e3,1e4,1e5,1e6]:
    lo,hi=0,ceil(time/a)+2
    while hi-lo>1:
        mid=(lo+hi)//2
        if T(mid)<=time: lo=mid
        else: hi=mid
    inverse.append({'t':time,'F':lo,'correct_residual':lo-c*time+b*c*log(time),'wrong_residual':lo-c*time+b/c*log(time)})
results['inversion'] = inverse
# Bounded-displacement moment inequalities on a dense grid including ell.
ell = f
points = [ell+(20-ell)*i/10000 for i in range(10001)]
results['moment_bounds'] = {'max_positive_v_exp_minus_v':max(max(v,0)*exp(-v) for v in points),'one_over_e':1/e,'max_v2_exp_minus_v_on_grid':max(v*v*exp(-v) for v in points)}
assert abs(results['binary_exp']['boundary_residual'])<1e-12
assert results['exact_mean_D1_at_theta3']=='0'
assert results['left_right_test']['phi_T_M']==results['left_right_test']['rho_phi']
assert results['left_right_test']['M_phi']!=results['left_right_test']['rho_phi']
assert max(abs(row['correct_residual']) for row in inverse)<4
assert results['moment_bounds']['max_positive_v_exp_minus_v']<=1/e+1e-12
try:
    url='https://arxiv.org/pdf/2609.27972'
    with urllib.request.urlopen(url,timeout=30) as r: data=r.read()
    p=root/'recent_decoupling.pdf'; p.write_bytes(data)
    text='\n'.join('PAGE '+str(i+1)+'\n'+p.extract_text() for i,p in enumerate(PdfReader(p).pages))
    (root/'recent_decoupling_extracted.txt').write_text(text,encoding='utf-8')
    results['recent_paper']={'url':url,'bytes':len(data),'keyword_lines':[line for line in text.splitlines() if any(k in line.lower() for k in ['bramson','derivative','theorem 3.1','theorem 4.6'])]}
except Exception as ex: results['recent_paper']={'error':str(ex)}
(root/'independent_checks.json').write_text(json.dumps(results,indent=2),encoding='utf-8')
print(json.dumps(results,indent=2))
