"""Read only the independently produced referee artifacts and enforce consistency."""
import csv,json,math
from pathlib import Path
from fractions import Fraction
import mpmath as mp_math

finite=list(csv.DictReader(open('referee_finite.csv')))
diag=list(csv.DictReader(open('referee_diagnostics.csv')))
cats=list(csv.DictReader(open('referee_categories.csv')))
quad=json.load(open('referee_quadrature.json'))[-1]
exact=json.load(open('referee_exact.json'))
mp=json.load(open('referee_mp.json'))
assert len(finite)==3*29
assert len(cats)==3*8*5
assert exact['max_float_relative_error']<1e-10
assert mp['cpp_vs_mp_max_relative_error']<1e-10
assert mp['double_vs_mp_max_relative_error']<1e-10
max_cat=max(abs(float(r['toll_direct'])-float(r['toll_from_defect'])) for r in cats)
max_linear=max(abs(float(r['linear_canceled'])-float(r['linear_uncanceled'])) for r in cats)
assert max_cat<1e-10 and max_linear<1e-10
psi_exact={}
for k in range(2,31):
    # Divide 1-x^k-(1-x)^k by x(1-x), then integrate its polynomial exactly.
    previous=0;coefficients=[]
    for j in range(k-1):
        previous=previous-(-1)**(j+1)*math.comb(k,j+1)
        coefficients.append(previous)
    psi=sum((Fraction(v,2*(j+1)) for j,v in enumerate(coefficients)),Fraction(0))
    harmonic=sum((Fraction(1,j) for j in range(1,k)),Fraction(0))
    assert psi==harmonic
    psi_exact[str(k)]=str(psi)
mp_math.mp.dps=50
moments=[mp_math.mpf(1),mp_math.mpf(0)]+[mp_math.mpf(r['a']) for r in quad['moments']]
hankel=mp_math.matrix([[moments[i+j] for j in range(5)] for i in range(5)])
chol=mp_math.cholesky(hankel)
cholesky_diagonal=[str(chol[i,i]) for i in range(5)]
table=[]
for r in finite:
    if r['n'] in ['1000','2000','4000','8000']:
        table.append({k:v for k,v in r.items() if k!='mean_over_n'})
summary={'max_category_identity_absolute_error':max_cat,'max_linear_centering_identity_error':max_linear,
    'sampled_sizes_max_prob_error':max(abs(float(r['prob_error'])) for r in diag),
    'sampled_sizes_max_centering_error':max(abs(float(r['centering_over_n'])) for r in diag),
    'max_float_vs_exact_relative_error':exact['max_float_relative_error'],
    'max_cpp_vs_mp_relative_error':mp['cpp_vs_mp_max_relative_error'],
    'max_python_double_vs_mp_relative_error':mp['double_vs_mp_max_relative_error'],
    'limit_moments':quad['moments'],'finite_table':table,
    'exact_polynomial_psi':psi_exact,'hankel_cholesky_diagonal':cholesky_diagonal}
json.dump(summary,open('referee_summary.json','w'),indent=2)
print(json.dumps({k:v for k,v in summary.items() if k not in ['limit_moments','finite_table','exact_polynomial_psi']},indent=2))
