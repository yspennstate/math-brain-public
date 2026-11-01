from fractions import Fraction as F
import cmath
import json
import math
import pathlib
import time
from bundle_tools import emit, entry, edge_to_problem, edge_to_attempt

root=pathlib.Path(__file__).resolve().parent
start=time.perf_counter()
tails=[]
for eps in (1,2):
    c=F(1,4)
    for m in (4,8,16,32,64):
        partial=sum(c*F(1,2**(eps*j)*j*j) for j in range(m+1,m+65))
        lower=c*F(1,2**(eps*(m+1))*(m+1)**2)
        upper=c*F(1,2**(eps*m)*m*m)*F(1,2**eps-1)
        assert lower<=partial<=upper
        tails.append({'eps':eps,'m':m,'partial_missing_variance':float(partial),'dyadic_power_normalized':float(partial*2**(eps*m)*m*m),'lower':float(lower),'infinite_tail_upper':float(upper)})
spectra=[]
for n in (2,3,4,8,16,32,64):
    maximum_residual=0.0
    for k in range(n):
        z=cmath.exp(2j*math.pi*k/n)
        v=[z**j for j in range(n)]
        Cv=v[1:]+v[:1]
        maximum_residual=max(maximum_residual,max(abs(Cv[j]-z*v[j]) for j in range(n)))
    assert maximum_residual<1e-10
    gap=1.0
    spectra.append({'n':n,'rank_difference':1,'rank_fraction':1/n,'bounded_lipschitz_test_gap':gap,'eigenvector_max_residual':maximum_residual})
measurement={'command':'python -X utf8 check_c0109.py','exact_dyadic_tail_cases':len(tails),'tail_cases':tails,'nonnormal_spectral_cases':spectra,'elapsed_seconds':round(time.perf_counter()-start,6),'result':'PASS'}
(root/'c0109_measurement.json').write_text(json.dumps(measurement,indent=2),encoding='utf-8')
tail_statement='If eps>0 and M=E|X|^(2+eps)<infinity, then E[|X|^2 1_{|X|>R}]<=M*R^(-eps) for R>0. The power eps is sharp as a scalar envelope: a symmetric atom law with total mass c*2^(-(2+eps)*j)/j^2 at +/-2^j has finite (2+eps)-moment and tail variance of order 2^(-eps*m)/m^2 at R=2^m. This proves neither a lower bound nor an optimal exponent for a circular-law convergence rate.'
tail_proof=(root/'C0109_proof.md').read_text(encoding='utf-8').split('For eps>0,',1)[1].split('\n\nA second trap',1)[0]
tail=entry('c0109-truncation-envelope','probability.random-matrices','finite-two-plus-epsilon-moment-tail-variance-envelope-sharp-power','lemma','Moment truncation controls variance without proving a spectral rate',tail_statement,'For eps>0,'+tail_proof,['eps>0','Finite (2+eps)-moment','Tail sharpness concerns scalar laws only'])
rank_statement='For n>=2, let J_n be the nilpotent matrix with ones on the superdiagonal, and C_n=J_n+e_n e_1^T. Their difference has rank one, but the empirical eigenvalue laws differ by one on the bounded 1-Lipschitz test f(z)=min(|z|,1): J_n has only zero eigenvalues and C_n has all nth roots of unity. Thus a Hermitian-style rank/n bound cannot control nonnormal empirical eigenvalue laws in general. This deterministic example is not an iid circular-law lower bound.'
rank=entry('c0109-nonnormal-rank-obstruction','probability.random-matrices','rank-one-nonnormal-perturbation-unit-spectral-measure-discrepancy','lemma','Rank-one perturbations can move a nonnormal spectral law by one',rank_statement,'J_n^n=0. For every z with z^n=1, C_n(1,z,...,z^(n-1))=z(1,z,...,z^(n-1)); these are n distinct eigenvalues. The perturbation is the single nonzero outer product e_n e_1^T. The radial test is zero at the origin and one at each root of unity.',['Deterministic nonnormal matrices','n>=2','Bounded Lipschitz comparison of eigenvalue laws'])
relations=[edge_to_problem('C0109',tail['key'],'This proves neither a lower bound nor an optimal exponent'),edge_to_attempt('C0109',tail['key'],'tail variance of order 2^(-eps*m)/m^2','which caps delta(eps)','cites'),edge_to_problem('C0109',rank['key'],'This deterministic example is not an iid circular-law lower bound','analogous_to'),{'from_key':rank['key'],'to_key':tail['key'],'kind':'semantic_association','rationale':'Rank card: "a Hermitian-style rank/n bound cannot control nonnormal empirical eigenvalue laws"; tail card: "This proves neither a lower bound nor an optimal exponent". Both limit unsupported transfers in a truncation route.'}]
emit(8,'C0109',[tail,rank],relations,'C0109_proof.md','c0109_measurement.json')
print(json.dumps(measurement),flush=True)
