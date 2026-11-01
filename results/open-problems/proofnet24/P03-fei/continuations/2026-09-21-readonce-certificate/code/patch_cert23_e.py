"""patch: the T3 correction term uses the computed bound on |Psi'| instead of the hand constant 12/ln2 + 1"""
p = "fei_cert23.py"; s = open(p, encoding="utf-8", newline="").read()
old = '''def check_T3(cert, max_depth=20):
    """tail p (x > K) with q > 1/2:  G_hat(y')/(1-v) - (ell(v)/ln2) sigma_t - 8(1-v) ell(v)/ln2 - 8 + Psi(1-v)/v - corr >= 0,
       corr = 2^-K (c + 8K + 16 + |Psi'|_max) covers every p-dependent term for p <= 2^-K (|Psi'| <= 12/ln2 + 1 on (0,1/2])"""
    K = cert.K; pK = 2.0 ** -K; sig = Iv(cert.tail_slope)
    corr = Iv(padup(pK * (cert.c + 8 * K + 16 + 12 / math.log(2) + 1.0)))
'''
assert old in s
new = '''def check_T3(cert, max_depth=20, psip_max=None):
    """tail p (x > K) with q > 1/2:  G_hat(y')/(1-v) - (ell(v)/ln2) sigma_t - 8(1-v) ell(v)/ln2 - 8 + Psi(1-v)/v - corr >= 0,
       corr = 2^-K (c + 8K + |Psi'|_max) covers every p-dependent term for p <= 2^-K: the margin part -c p, the term
       -8 p x <= 8 K 2^-K (x 2^-x decreasing for x >= K), and p Psi'(zeta); the factors (1-p) in D and E were kept as 1"""
    K = cert.K; pK = 2.0 ** -K; sig = Iv(cert.tail_slope)
    if psip_max is None: psip_max = psi_prime_abs_max()
    corr = Iv(padup(pK * (cert.c + 8 * K + psip_max)))
'''
s = s.replace(old, new)
s = s.replace('    if which in ("all", "T3"): results["T3"] = check_T3(cert)', '    if which in ("all", "T3"): results["T3"] = check_T3(cert, psip_max=psip_max)')
open(p, "w", encoding="utf-8", newline="").write(s)
import py_compile; py_compile.compile(p, doraise=True); print("T3 correction patched, compiles")
