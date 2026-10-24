import json
import math
import pathlib
import random
import statistics
import time
from bundle_tools import emit, entry, edge_to_problem, edge_to_attempt

root=pathlib.Path(__file__).resolve().parent
start=time.perf_counter()
rho=0.5
rng=random.Random(3350127)
samples=[]
for m in (16,64,256,1024):
    maxima=[]
    peak_counts=[]
    for repeat in range(300):
        common=math.sqrt(rho)*rng.gauss(0,1)
        zs=[rng.gauss(0,1) for _ in range(m)]
        high=max(zs)
        maxima.append(common+math.sqrt(1-rho)*high)
        peak_counts.append(sum(math.sqrt(1-rho)*(high-z)<=1 for z in zs))
    samples.append({'m':m,'repeats':300,'max_variance_sample':statistics.variance(maxima),'mean_near_peak_count_deficit_1':statistics.mean(peak_counts),'median_near_peak_count_deficit_1':statistics.median(peak_counts)})
tail_controls=[]
for log_m in (10,100,1000,10000,1000000):
    delta=log_m**(-0.25)
    b=math.sqrt(2*log_m)
    d=delta/(2*math.sqrt(1-rho))
    x=b-d
    assert x>=1
    log_mean_lower=b*d-d*d/2-math.log(x)-1.5-math.log(2*math.pi)/2
    tail_controls.append({'log_m':log_m,'delta_m':delta,'log_binomial_mean_lower':log_mean_lower,'maximum_exceedance_upper':math.exp(-b*d-d*d/2)})
assert tail_controls[-1]['log_binomial_mean_lower']>tail_controls[-2]['log_binomial_mean_lower']
measurement={'command':'python -X utf8 check_c0127.py','rho':rho,'exact_variance_lower':rho,'sample_diagnostics':samples,'shrinking_deficit_tail_controls':tail_controls,'two_peak_probability_deficit_1':math.erf(0.5),'elapsed_seconds':round(time.perf_counter()-start,6),'result':'PASS; samples are illustrative only'}
(root/'c0127_measurement.json').write_text(json.dumps(measurement,indent=2),encoding='utf-8')
statement='Fix 0<rho<1 and independent standard normal Z_0,...,Z_m. Let X_i=sqrt(rho)*Z_0+sqrt(1-rho)*Z_i and M_m=max_i X_i. Coordinates have variance one and distinct covariance rho. Var(M_m)>=rho, so the field is not superconcentrated. Nevertheless the number of coordinates at deficit at most delta_m=(log m)^(-1/4) from M_m tends to infinity in probability. Thus growing near-peaks with pairwise covariance merely bounded away from one, even at vanishing absolute deficit, are insufficient for superconcentration. This does not refute a criterion requiring overlaps to tend to zero.'
proof=(root/'C0127_proof.md').read_text(encoding='utf-8').split('Fix 0<rho<1.',1)[1].split('\n\nThis refutes',1)[0]
new=entry('c0127-common-factor-peaks','probability.gaussian','common-gaussian-factor-growing-near-peaks-without-superconcentration','lemma','Common-factor obstruction to a growing-peaks criterion',statement,'Fix 0<rho<1.'+proof,['Independent standard Gaussian coordinates','Fixed positive common covariance rho','Candidate uses overlap bounded away from one, not overlap tending to zero'])
quantifier=entry('c0127-two-peak-quantifier','probability.gaussian','two-independent-gaussian-peaks-fixed-deficit-probability','lemma','Two-peak counterexample needs a probability quantifier','For independent standard normal Z_1,Z_2 and fixed d>0, the probability both coordinates are within d of max(Z_1,Z_2) equals erf(d/2)<1. Repeating coordinates in two blocks does not change this probability. Such replication alone cannot establish near-maximal low-overlap peaks with probability tending to one.','Both coordinates are within d exactly when |Z_1-Z_2|<=d. Their difference is N(0,2), giving erf(d/2). Its Gaussian tail is strictly positive for finite d.',['Fixed finite deficit d','Two independent standard normal block values'])
relations=[edge_to_problem('C0127',new['key'],'This does not refute a criterion requiring overlaps to tend to zero'),edge_to_attempt('C0127',new['key'],'Var(M_m)>=rho','two-peak version disproved as an equivalence','generalizes'),edge_to_attempt('C0127',quantifier['key'],'erf(d/2)<1','with probability tending to 1','cites')]
emit(3,'C0127',[new,quantifier],relations,'C0127_proof.md','c0127_measurement.json')
print(json.dumps(measurement),flush=True)
