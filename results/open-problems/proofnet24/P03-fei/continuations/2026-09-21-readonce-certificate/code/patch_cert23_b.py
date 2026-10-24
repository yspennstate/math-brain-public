"""patch: attribute the P2 (Lambda difference) width in region 3 to the v axis through the direct form"""
p = "fei_cert23.py"; s = open(p, encoding="utf-8", newline="").read()
old = '''    wx = P1.width() + T1.width() + T5.width() + cert.Ghat_range(Xp).width()
    wy = T2.width() + T3.width() + 2 * cert.Ghat_range(Yp).width() + (1 - v.lo) * psit_prime_iv(Zw).width()
    return P1.lo + P2_lo - P3_hi, wx, wy
'''
assert old in s
new = '''    lam_v = Lambda_range(cert, Iv(v.lo, np.minimum(v.hi, 0.5)))
    wx = P1.width() + T1.width() + T5.width() + np.abs(P2_lo) * (u.width() / np.maximum(u.lo, 1e-300))
    wy = T2.width() + T3.width() + 2 * lam_v.width() / np.maximum(u.lo, 1e-300) + (1 - v.lo) * psit_prime_iv(Zw).width()
    return P1.lo + P2_lo - P3_hi, wx, wy
'''
s = s.replace(old, new); open(p, "w", encoding="utf-8", newline="").write(s)
import py_compile; py_compile.compile(p, doraise=True); print("patched, compiles")
