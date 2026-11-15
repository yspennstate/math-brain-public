"""Independent invariant-tensor check; no files outside this folder are written."""
import os
for key in ('OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','VECLIB_MAXIMUM_THREADS','NUMEXPR_NUM_THREADS'):
    os.environ[key] = '1'
from fractions import Fraction as F
import signal
signal.alarm(60)
assert os.getpriority(os.PRIO_PROCESS,0) >= 15
count = 0
for n in (1,2,3,7,101):
    for vs in ([],[F(0)]*5,[F(1,4)]*13,[F(1),F(2,7),F(0),F(3,2)]):
        Q, U = F(n), F(n*n)  # E Tr X^2, E (Tr X)^2
        product=F(1)
        for v in vs:
            if n == 1:
                Q, U = (1+v)*Q, (1+v)*U
            else:
                den=n*(n-1)*(n+2)
                a=((n+1)*U-2*Q)/den
                b=(n*Q-U)/den
                # Conjugation tensor, followed by independent diagonal averaging.
                Q, U = (a+b)*n*(1+v)+b*(n*n+n*v), a*(n*n+n*v)+2*b*n*(1+v)
            product *= 1+3*v/(n+2)
        z=F(n+2,3)*(product-1)
        assert Q/n == 1+z
        assert U/(n*n) == 1+z/n
        count += 1
print(f'{count} exact rational invariant-tensor product checks passed')
print('Earlier main claim holds, including n=1, empty depth, zero and inhomogeneous variances.')
