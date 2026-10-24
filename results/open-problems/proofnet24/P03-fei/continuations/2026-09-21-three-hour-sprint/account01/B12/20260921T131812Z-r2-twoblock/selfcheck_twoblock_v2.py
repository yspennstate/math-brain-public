"""High-precision check of the v2 x-monotonicity reduction; not a certificate."""
import json, random
import mpmath as mp
mp.mp.dps=80
random.seed(20260921)
ln2=mp.log(2); c=mp.mpf('0.003')

def ell(v): return -mp.log(1-v)/v
max_formula=mp.mpf(0); max_deriv=mp.mpf('-inf'); min_gap=mp.inf
N=20000
for _ in range(N):
    x=mp.mpf(str(random.uniform(1,2)))
    y=mp.mpf(str(random.uniform(1.0001,40)))
    p=mp.power(2,-x); v=mp.power(2,-y)
    a=8*(1-v)*ell(v)/ln2
    # Residual x block R=c(1-p)-8[1+p(x-1)]-a(1-p).
    def R(t):
        pp=mp.power(2,-t)
        return c*(1-pp)-8*(1+pp*(t-1))-a*(1-pp)
    analytic=p*(c*ln2-8*(1-ln2*(x-1))-a*ln2)
    numeric=mp.diff(R,x)
    max_formula=max(max_formula,abs(analytic-numeric))
    max_deriv=max(max_deriv,analytic)
    # Uniform proof gap after dropping the extra negative -a ln2 term.
    gap=8*(1-ln2*(x-1))-c*ln2
    min_gap=min(min_gap,gap)
out={
 "status":"SELF_CHECK_ONLY_NOT_CERTIFICATE",
 "samples":N,
 "mp_dps":mp.mp.dps,
 "max_derivative_formula_abs_error":mp.nstr(max_formula,12),
 "largest_sampled_dJdx":mp.nstr(max_deriv,12),
 "minimum_sampled_uniform_negativity_gap":mp.nstr(min_gap,12),
 "analytic_uniform_gap_at_x2":mp.nstr(8*(1-ln2)-c*ln2,12),
 "result":"PASS" if max_formula<mp.mpf('1e-60') and (8*(1-ln2)-c*ln2)>0 else "FAIL"
}
print(json.dumps(out,indent=2))
