"""Independent disk/positive-law/kernel/harmonicity checks, with infinite tails.

No author code is imported. Let b_m=(m+1)a_{m+1}, sum b_m=1, q_1=0.
Then Z=1/(1-sum b_m/(m+1)), and
q_{m+1}=b_m/((m+1)*binom(2m+1,m)*Z**m).
The two regular examples use the Sibuya law with generating function
sum b_m*r**m=1-(1-r)**alpha. The third has m_j=16**(j-1),
b_{m_j}=(3/5)*(2/5)**(j-1), j>=1, with infinitely many atoms.
"""
import json
import math
import resource
import signal
import time
from fractions import Fraction as F
from pathlib import Path
import mpmath as mp

signal.alarm(240)
resource.setrlimit(resource.RLIMIT_CPU, (220, 230))
mp.mp.dps = 65
started = time.monotonic()

def d_exact(n):
    return F(math.comb(2*n, n), 4**n)

def h_exact(n):
    return 2*n*d_exact(n) if n > 0 else F(0)

def beta_integer(k, alpha):
    # Exact integral int_0^1 r**(k-1)*(1-r)**alpha dr.
    ans = F(1, 1)/ (alpha+1)
    for j in range(1, k):
        ans *= F(j, 1)/(alpha+1+j)
    return ans

def residues(p):
    # h(p+m)/h(m+1)=1+sum_j A_j/(m+j), identically as a rational function.
    answer = []
    for j in range(1, p):
        aj = F(1, 2)
        for ell in range(1, p):
            if ell != j:
                aj *= F(2*(ell-j)+1, 2*(ell-j))
        answer.append((j, aj))
    return answer

def mm(x):
    return mp.mpf(x.numerator)/x.denominator if isinstance(x, F) else mp.mpf(x)

def d_mp(n):
    if n == 0:
        return mp.mpf(1)
    n = mp.mpf(n)
    if n < 10000:
        return mp.exp(mp.loggamma(n+mp.mpf('.5'))-mp.loggamma(n+1))/mp.sqrt(mp.pi)
    # Stirling expansion of log(binomial(2n,n)/4**n); 16 terms.
    logd = -mp.log(mp.pi*n)/2
    for j in range(1, 17):
        logd += mp.bernoulli(2*j)/(2*j*(2*j-1))*(mp.power(2, 1-2*j)-2)/n**(2*j-1)
    return mp.exp(logd)

results = {}
for alpha in [F(1, 2), F(19, 20), F(1)]:
    name = 'sibuya_'+str(alpha)
    a = mm(alpha)
    Z = 1+a
    # sum a_k = alpha/(1+alpha); Z*sum (k-1)a_k = 1.
    fZ = a/(1+a)
    print(name, 'type a=', mp.nstr(a+mp.mpf('1.5'), 8), 'Z=', mp.nstr(Z, 10))
    print('critical residuals:', mp.nstr(fZ-(1-1/Z), 4), mp.nstr(Z*(1-fZ)-1, 4))
    # Check q -> nu(m) using rational arithmetic (not a fitted negative law).
    b = F(1)
    max_q_res = F(0)
    for m in range(1, 81):
        b = alpha if m == 1 else b*F(m-1-alpha, m)
        q = b / ((m+1)*math.comb(2*m+1, m)*(alpha+1)**m)
        nu_from_q = q*(4*(alpha+1))**m
        nu_from_b = b / ((2*m+1)*d_exact(m))
        max_q_res = max(max_q_res, abs(nu_from_q-nu_from_b))
    print('q-to-positive-law exact residual:', max_q_res)
    max_kernel_rel = mp.mpf(0)
    for k in [1, 2, 3, 8, 31, 100, 1000]:
        # W uses J'(r)=Z*(1-r)**alpha directly; nu(-k)=d(k-1)*I/(2Z).
        disk_integral = mp.quad(lambda r: r**(k-1)*Z*(1-r)**a, [0, mp.mpf('.5'), 1])
        neg_disk = d_mp(k-1)*disk_integral/(2*Z)
        # T = int sum m*b_m*r**(m+x-1) dr, with a substitution removing its singularity.
        T = mp.quad(lambda t: (1-t**(1/a))**k, [0, mp.mpf('.5'), 1])
        neg_kernel = d_mp(k)*T/(2*k-1)
        rel = abs(neg_disk/neg_kernel-1)
        max_kernel_rel = max(max_kernel_rel, rel)
        print('k', k, 'nu(-k)', mp.nstr(neg_disk, 14), 'kernel rel', mp.nstr(rel, 3))
    harmonic_exact = True
    for p in [1, 2, 3, 4, 8, 16, 32]:
        # Positive part of sum nu(m)*h(p+m), summed analytically from b's pgf.
        positive = F(1)
        for j, aj in residues(p):
            positive += aj*(F(1, j)-beta_integer(j, alpha))
        # Negative part comes solely from the disk integral, not from T.
        negative = sum((F(1, 2)*d_exact(k-1)*beta_integer(k, alpha)*h_exact(p-k)
                        for k in range(1, p)), F(0))
        error = positive+negative-h_exact(p)
        harmonic_exact &= error == 0
        print('harmonic p', p, 'exact residual', error)
    # Sum negative disks by the central-binomial generating function.
    negmass = mp.quad(lambda t: t**(2*a), [0, 1])
    # Positive mass: 1/h(m+1)=1/2 int r**m/(sqrt(1-r)) dr.
    posmass = mp.quad(lambda t: 1-t**(2*a), [0, 1])
    print('mass positive', mp.nstr(posmass, 18), 'negative', mp.nstr(negmass, 18), 'residual', mp.nstr(posmass+negmass-1, 4))
    results[name] = dict(Z=str(Z), type=str(a+mp.mpf('1.5')),
                         max_kernel_relative=str(max_kernel_rel), harmonic_exact=harmonic_exact)

rho = mp.mpf(2)/5
J = 170
atoms = [(16**j, (1-rho)*rho**j) for j in range(J)]
tail = rho**J
fZ = mp.fsum(b/(m+1) for m, b in atoms)
Z = 1/(1-fZ)
print('lacunary_infinite rho=2/5 m_j=16**j, j>=0')
print('Z', mp.nstr(Z, 30), 'omitted beta mass <=', mp.nstr(tail, 4))
print('critical residuals', mp.nstr(fZ-(1-1/Z), 4), mp.nstr(Z*(1-fZ)-1, 4), '(tail bounds included below)')
max_kernel_rel = mp.mpf(0)
for k in [1, 2, 3, 8, 31, 100, 1000]:
    # Integrate each monomial in J'=Z*sum b_m*(1-r**m).
    # 1/k-1/(k+m) is nonnegative; omitted integral <= tail/k.
    I = Z*mp.fsum(b*(mp.mpf(1)/k-mp.mpf(1)/(k+m)) for m, b in atoms)
    disk = d_mp(k-1)*I/(2*Z)
    T = mp.fsum(m*b/(m+k) for m, b in atoms)
    kern = d_mp(k)*T/(2*k-1)
    rel = abs(disk/kern-1)
    max_kernel_rel = max(max_kernel_rel, rel)
    print('k', k, 'nu(-k)', mp.nstr(disk, 14), 'kernel rel', mp.nstr(rel, 3))
max_harm = mp.mpf(0)
for p in [1, 2, 3, 4, 8, 16, 32]:
    pos = mp.mpf(0)
    for m, b in atoms:
        ratio = mp.mpf(1)
        for j in range(1, p):
            ratio *= 1+mp.mpf(1)/(2*(m+j))
        pos += b*ratio
    neg = mp.fsum(d_mp(k-1)/2 * mp.fsum(b*(mp.mpf(1)/k-mp.mpf(1)/(k+m)) for m, b in atoms)
                 * mm(h_exact(p-k)) for k in range(1, p))
    err = abs((pos+neg)/mm(h_exact(p))-1)
    max_harm = max(max_harm, err)
    # All components are positive. Each missing component's harmonic row is 1
    # algebraically; without using that fact, h(p+m)/h(m+1)<=h(p), and the
    # missing finite negative terms are bounded separately by tail times p.
    err_bound = (1+p)*tail
    print('harmonic p', p, 'row residual', mp.nstr(err, 3), 'omission bound', mp.nstr(err_bound, 3))
posmass = mp.fsum(b/(2*(m+1)*d_mp(m+1)) for m, b in atoms)
# Integral of each term: (1/2)int(1-r**m)/sqrt(1-r) dr.
def half_beta_integral(m):
    # 1/2 B(m+1,1/2) = int_0^1 (1-t*t)**m dt.
    # Scaled quadrature avoids catastrophic gamma subtraction at huge m.
    if m < 256:
        return mp.quad(lambda t: (1-t*t)**m, [0, 1])
    denom = mp.mpf(m+1)
    return mp.quad(lambda s: mp.exp(m*mp.log1p(-s*s/denom)), [0, 2, 6, 16])/mp.sqrt(denom)

negmass = mp.fsum(b*(1-half_beta_integral(m)) for m, b in atoms)
print('mass positive', mp.nstr(posmass, 20), 'negative', mp.nstr(negmass, 20), 'residual', mp.nstr(posmass+negmass-1, 4), 'omission <=', mp.nstr(tail, 3))
print('T(1)-1/Z', mp.nstr(mp.fsum(m*b/(m+1) for m, b in atoms)-1/Z, 4))
results['lacunary'] = dict(Z=str(Z), omitted_beta_mass=str(tail), max_kernel_relative=str(max_kernel_rel), max_harmonic_residual=str(max_harm))
print('seconds', round(time.monotonic()-started, 3), 'peak_rss_bytes', resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
Path('audit_exact_results.json').write_text(json.dumps(results, indent=2)+'\n')
