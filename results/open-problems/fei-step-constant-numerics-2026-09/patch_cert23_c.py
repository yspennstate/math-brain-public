"""patch: conservative constants in the two region-3 beyond-grid lemmas"""
p = "fei_cert23.py"; s = open(p, encoding="utf-8", newline="").read()
old = '''    p3 = 8 * 1.0 + 8 * 0.5 * ell_pt(0.5).hi / math.log(2) + 4 + 0.5 * psitp_max + 4 / math.log(2) + 1
'''
assert old in s
new = '''    # E/u = T1 + T2 + T3 + T4 - T5 with T1 <= 8 v ell(u)/ln2 <= 4 ell(2^-Xmax)/ln2, T2 <= 8 (1-v) v ell(v)/ln2 <= 8 ell(1/2)/ln2 (v <= 1/2),
    # T3 <= 4, T4 = (1-v) Psit'(xi) <= max|Psit'| over (0, 3/4], -T5 <= 0
    p3 = 4 * ell_pt(2.0 ** -Xmax).hi / math.log(2) + 8 * ell_pt(0.5).hi / math.log(2) + 4 + psitp_max
'''
s = s.replace(old, new)
old = '''    """region 3 with u <= v <= 2^-K:  Phi/u >= (1-v) sigma_t/ln2 - 2 v G_hat(y') - c ln2 2^-K - (4/ln2)(3u + 2v) - 30 v"""
    K = cert.K; v = 2.0 ** -K
    GY = cert.G[-1] + cert.tail_slope / (math.e * math.log(2)) + cert.c   # max of 2^-(y'-K) G_hat(y') scaling: G_hat(y') 2^-(y'-K) <= G_J + sigma_t/(e ln2) + c
    val = (1 - v) * cert.tail_slope / math.log(2) - 2 * v * GY - cert.c * math.log(2) * v - (4 / math.log(2)) * 5 * v - 30 * v
'''
assert old in s
new = '''    """region 3 with u <= v <= 2^-K (both p, q above 1 - 2^-K).  In the linear tail G_hat(xi) <= G_hat(y') <= G_hat(x') for
    xi in [L(w), L(v)] and G_hat' >= sigma_t, and 1/(1-z) <= 1 + 2w <= 1 + 4v for z <= w <= 2v, so
       P1 + P2 >= G_hat(y') - (1-v)[(G_hat(y') - sigma_t/ln2)(1 + 4v) + 2v (1 + 4v)^2 G_hat(y')] >= (1-v) sigma_t/ln2 - 12 v G_hat(y'),
       E/u <= T1 + T2 + T3 + T4 - T5 <= 12v + 12v + 8v + (4/ln2)(3u - v)^+ <= 32v + (4/ln2) 2v <= 45 v,
    and 2^-(y'-K) G_hat(y') <= G_J + sigma_t/(e ln2) + c for y' >= K, so v G_hat(y') <= 2^-K (G_J + sigma_t/(e ln2) + c)."""
    K = cert.K; v = 2.0 ** -K
    GY = cert.G[-1] + cert.tail_slope / (math.e * math.log(2)) + cert.c
    val = (1 - v) * cert.tail_slope / math.log(2) - 12 * v * GY - 45 * v
'''
s = s.replace(old, new)
open(p, "w", encoding="utf-8", newline="").write(s)
import py_compile; py_compile.compile(p, doraise=True); print("lemma constants patched, compiles")
