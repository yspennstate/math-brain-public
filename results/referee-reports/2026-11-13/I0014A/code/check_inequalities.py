"""Exact identities and high precision constant checks; no simulation."""
import os
os.environ.update(OMP_NUM_THREADS='1',OPENBLAS_NUM_THREADS='1',MKL_NUM_THREADS='1',VECLIB_MAXIMUM_THREADS='1')
import resource
# Allocation is tiny; macOS in this sandbox rejects setrlimit changes.
# Measure peak resident memory and fail if the requested cap is exceeded.
from pathlib import Path
from fractions import Fraction as F
import itertools, json
import sympy as S
import mpmath as mp
mp.mp.dps=80
results={}
rows=[]
for b in [F(1,4),F(1,3),F(1,2),F(3,4)]:
 d=F(1,10)
 exponent=1-b*(4+d)/(2+d)
 rows.append({'beta':str(b),'delta':str(d),'threshold_shift_exponent':str(exponent),'delta_upper_bound':str((4*b-2)/(1-b)),'quadratic_sum_power':str(1-2*b)})
results['exponents']=rows
b,d=S.symbols('beta delta',positive=True)
expr=1-b*(4+d)/(2+d)
assert S.simplify(expr.subs(b,S.Rational(1,2))-d/(2*(2+d)))==0
results['beta_half_identity']='1-beta*(4+delta)/(2+delta)=delta/[2*(2+delta)] at beta=1/2'
# All 16 partitions of four variables, retaining arbitrary covariance symbols.
n=4
cov={(i,j):S.Symbol(f'c{i}{j}') for i in range(n) for j in range(i,n)}
def c(i,j):return cov[tuple(sorted((i,j)))]
def var(indices):return sum(c(i,j) for i in indices for j in indices)
V=var(range(n));Q=sum(c(i,i) for i in range(n));av_cov=0;av_vars=0
for bits in itertools.product([0,1],repeat=n):
 A=[i for i in range(n) if bits[i]];B=[i for i in range(n) if not bits[i]]
 av_cov+=sum(c(i,j) for i in A for j in B)/S.Integer(2)**n
 av_vars+=(var(A)+var(B))/S.Integer(2)**n
assert S.expand(av_cov-(V-Q)/4)==0
assert S.expand(av_vars-(V+Q)/2)==0
results['partition_identity']='Verified symbolically with arbitrary covariance entries, n=4, all 16 partitions; general proof in REPORT.md.'
u,v=S.symbols('u v',nonnegative=True)
assert S.expand((1+u)*(1+v)-(1+u+v))==u*v
results['moment_submultiplicativity']='(1+u)(1+v)-(1+u+v)=uv>=0'
x=mp.mpf('0.000001')
literal=-mp.log(1-x,2)
printed=x+x*x/(2*(1-x))
assert literal>printed
results['log_base_audit']={'x':str(x),'minus_log2_1_minus_x':mp.nstr(literal,60),'printed_natural_log_taylor_bound':mp.nstr(printed,60),'limit_ratio':mp.nstr(1/mp.log(2),60),'inequality_as_base2':'fails'}
results['bradley_literal_exponent_example']={'alpha':'1','d':'1','gamma':'0.8','gamma_minus_d_alpha_ln2':mp.nstr(mp.mpf('.8')-mp.log(2),60),'scope':'Checks scalar criterion only; these are not certified construction constants.'}
assert mp.mpf('.8')-mp.log(2)>0
results['dyadic_binary_constant']=mp.nstr(mp.sqrt(2)/(mp.sqrt(2)-1),60)
results['peak_rss_bytes']=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
assert results['peak_rss_bytes'] < 4_000_000_000
results['nice']=os.getpriority(os.PRIO_PROCESS,0)
results['limits']='1 process; library threads capped at 1; peak RSS measured against 4 GB; no setrlimit enforcement on this macOS sandbox; no simulations'
root=Path(__file__).resolve().parents[1]
(root/'data'/'inequality_checks.json').write_text(json.dumps(results,indent=2)+'\n')
print(json.dumps(results,indent=2))
