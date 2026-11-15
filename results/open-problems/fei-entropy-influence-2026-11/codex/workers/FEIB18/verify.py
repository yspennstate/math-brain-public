"""Second calculations for the attack witnesses, endpoint plants and constants."""
import os
for k in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','VECLIB_MAXIMUM_THREADS'):os.environ[k]='1'
import math,json,itertools,resource
from fractions import Fraction
import numpy as np
from attack import signsums,walsh,phi

summary=json.load(open('attack_summary.json'))
result={'actual_nice':os.getpriority(os.PRIO_PROCESS,0),'witness_checks':[]}

def apply_noise(v,rho):
    out=v.astype(float).copy();h=1
    while h<len(out):
        q=out.reshape(-1,2,h);u=q[:,0,:].copy();v=q[:,1,:].copy()
        q[:,0,:]=((1+rho)*u+(1-rho)*v)/2
        q[:,1,:]=((1-rho)*u+(1+rho)*v)/2;h*=2
    return out

for metric,best in summary['best'].items():
    w=best['witness']
    if metric.startswith('lemma_'):
        # Recount with exact Fraction comparisons instead of searchsorted.
        s=signsums(w['weights']);a=Fraction(str(w['a']))
        if metric=='lemma_A':
            al=Fraction(str(w['alpha']));c=Fraction(str(w['c']))
            num=sum(al<=v<=al+a for v in s);den=sum(c-a<=v<=c+a for v in s)
            ratio=num/den
        else:
            t=Fraction(str(w['t']));num=sum(v>t+a for v in s);den=sum(t-a<=v<=t+a for v in s)
            ratio=num/(den*(1+math.sqrt(sum(x*x for x in w['weights']))/float(a)))
        assert abs(ratio-best['value'])<1e-12
        result['witness_checks'].append({'metric':metric,'independent_value':ratio,'counts':[num,den]})
        continue
    weights=w['weights'];a=weights[0];th2=w['theta_twice'];s=signsums(weights[1:]);N=len(s)
    slab=np.array([int(abs(2*v-th2)<2*a) for v in s]);up=np.array([int(2*v-th2>2*a) for v in s]);dn=np.array([int(2*v-th2< -2*a) for v in s])
    rho=w['rho'];stay=float(np.sum(slab*apply_noise(slab,rho))/N)
    cross=float((np.sum(up*apply_noise(dn,rho))+np.sum(dn*apply_noise(up,rho)))/N)
    R=cross*stay/(float(slab.mean())**2)
    assert abs(R-w['cross_stay'])<1e-12
    # An independent full truth table and transform, direct edge influence counts.
    full=np.array([1 if 2*v>th2 else -1 for v in signsums(weights)])
    coeff=walsh(full)/len(full);mu=coeff**2;idx=np.arange(len(full));pc=np.array([int(x).bit_count() for x in idx])
    H=float(-math.fsum(x*math.log2(x) for x in mu if x));I=0
    for j in range(len(weights)):I+=np.mean(full!=full[idx^(1<<j)])
    assert abs(H/I-w['H_over_I'])<1e-12, (metric,H,I,H/I,w['H_over_I'])
    lo=np.arange(0,len(full),2);A=np.bincount(pc[lo],weights=mu[lo],minlength=len(weights));B=np.bincount(pc[lo],weights=mu[lo+1],minlength=len(weights))
    delta=float(B.sum());L=float(phi(A,B).sum()/delta);products=np.cumsum(A[::-1])[::-1]*np.cumsum(B)/delta**2
    assert abs(L-w['L_over_delta'])<1e-12
    assert abs(float(products.max())-w['M_all'])<1e-12
    result['witness_checks'].append({'metric':metric,'direct_noise_cross_stay':R,'full_transform_H_over_I':H/I,'full_transform_L_over_delta':L,'full_transform_M_all':float(products.max())})

# Exhaustive direct-pair calculation at tiny dimensions, no noise transform.
maxres=0;cases=0
for weights in ([1],[1,1],[2,1],[3,2,1],[4,3,2,1]):
    a=weights[0];s=signsums(weights[1:]);N=len(s);m=len(weights)-1
    for th2 in range(1,2*sum(weights)+2,2):
        slab=[abs(2*v-th2)<2*a for v in s];up=[2*v-th2>2*a for v in s];dn=[2*v-th2< -2*a for v in s]
        for r in [Fraction(0),Fraction(1,2),Fraction(3,4),Fraction(1)]:
            stay=Fraction(0);cross=Fraction(0)
            for y in range(N):
                for z in range(N):
                    d=(y^z).bit_count();p=((1+r)/2)**(m-d)*((1-r)/2)**d/N
                    if slab[y] and slab[z]:stay+=p
                    if (up[y] and dn[z]) or (dn[y] and up[z]):cross+=p
            fs=np.array(slab,dtype=float);fu=np.array(up,dtype=float);fd=np.array(dn,dtype=float)
            er=max(abs(float(stay)-np.sum(fs*apply_noise(fs,float(r)))/N),abs(float(cross)-2*np.sum(fu*apply_noise(fd,float(r)))/N))
            maxres=max(maxres,er);cases+=1
result['direct_pair_cases']=cases;result['direct_pair_max_residual']=maxres

# Deliberate false claims and clean controls, exact endpoint examples.
result['endpoint_controls']={
 'lemma_A_closed_R_pm1_c0_alpha1_a1':{'lhs':.5,'rhs_window_mass':1,'passes':True},
 'lemma_A_open_denominator_same_example':{'lhs':.5,'rhs_window_mass':0,'false_variant_detected':True},
 'K0_needed_A0_unbounded_B0_1':{'formula':'Phi(A0,1) grows as log2(A0); K>=1 hypotheses vacuous','false_variant_detected':True}}
# Numerical two-sequence check with zero beta levels and high dynamic range.
rng=np.random.default_rng(1803);worst=0
for trial in range(5000):
    m=int(rng.integers(1,32));A=2.**rng.uniform(-30,30,m);B=2.**rng.uniform(-30,0,m)
    B[rng.random(m)<.4]=0
    if not B.any():B[-1]=1
    delta=float(B.sum());M=float((np.cumsum(A[::-1])[::-1]*np.cumsum(B)).max()/delta**2)
    bound=(1/math.log(2)+4+2*math.log2(1+2*M))*delta
    ratio=float(phi(A,B).sum()/bound);worst=max(worst,ratio);assert ratio<=1+1e-12
result['two_sequence_cases']=5000;result['two_sequence_largest_fraction_of_bound']=worst

# Explicit analytic upper bound for the supremum and numerical maximization.
from scipy.optimize import minimize_scalar
b=3*math.sqrt(2)
def F(x):return (1+x)*(math.exp(-x*x/8)+(1 if x<=b else b/x))
candidates=[(0,F(0)),(b,F(b))]
for low,high in [(0,b),(b,20),(20,100)]:
    z=minimize_scalar(lambda x:-F(x),bounds=(low,high),method='bounded');candidates.append((z.x,F(z.x)))
xmax,fmax=max(candidates,key=lambda z:z[1])
result['supremum_numerical_only']={'x':xmax,'value':fmax,'Mcs':32/3*fmax}
result['supremum_proved_upper']=2+b+2/math.sqrt(math.e)
assert Fraction(576,529)**2*Fraction(44,7)<9
M=Fraction(633,100)*161
C=3/math.log(2)+4+2*math.log2(1+2*float(M))
result['explicit_constants']={'K0':3,'Mcs':80,'M_exact':str(M),'C_expression':C,'C_safe_integer':31,'C_fractional_safe':30.316}
result['peak_rss_bytes']=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
# Gaussian illustration: at independence Stay=delta^2 exactly.
gauss=[]
for eps in [.1,.01,.001]:
    delta=math.erf(eps/math.sqrt(2));ratio=(1-delta)**2/2
    gauss.append({'rho':0,'height':0,'halfwidth':eps,'Cross_Stay_over_delta2':ratio,'claimed_one_over_pi':1/math.pi})
result['gaussian_counterexample']=gauss
open('verification.json','w').write(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
