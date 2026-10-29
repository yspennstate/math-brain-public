"""Independent re-derivation of every load-bearing number in referee1_window_report.md.
Nothing here reads the document; all quantities are recomputed from the definitions.
    W_r = r^xi ; d(r) = sigma*(r/K)^xi ; C_K = 1/(1-K^(xi-1)) ; window(h) = {0} u [sigma*(h/K)^xi, C_K*sigma*h^xi]
"""
import math

def CK(K, xi): return 1.0/(1.0 - K**(xi-1.0))

print("=== constants at K=5, xi=3/4 ===")
K, xi = 5, 0.75
print("K^(xi-1)=%.6f  C_K=%.6f  K^xi=%.6f  2^xi=%.6f  2^(1-xi)=%.6f  C_K*K^xi=%.6f"
      % (K**(xi-1), CK(K,xi), K**xi, 2**xi, 2**(1-xi), CK(K,xi)*K**xi))

print()
print("=== ITEM 1: brute-force step stability of child 0 over the whole class ===")
# member: class scale s, height h in [s/2,s], far-depth D in {0} u [sig*(h/K)^xi, CK*sig*h^xi]
# child : class scale s/K, height h/K, far-depth d(s)=sig*(s/K)^xi
# require d(s) in child window(h/K) = [sig*(h/K^2)^xi, CK*sig*(h/K)^xi]
sig, s = 1.0, 1.0
worst_bot, worst_top = math.inf, math.inf
for K in (5, 6, 8, 10, 12, 20, 37, 38, 50):
    for xi in (0.05,0.1,0.2,0.3,0.35,0.37,0.4,0.5,0.6,0.7,0.75):
        ck = CK(K, xi)
        bad = False
        for i in range(0, 501):
            h = s*(0.5 + 0.5*i/500.0)
            child_lo = sig*(h/K**2)**xi
            child_hi = ck*sig*(h/K)**xi
            Dc = sig*(s/K)**xi                     # child 0 far-depth
            if not (child_lo <= Dc <= child_hi): bad = True; break
        flag = "FAILS" if bad else "ok"
        if K == 5 and xi == 0.75:
            print("   K=5 xi=0.75 -> %s (bottom slack %.4f, top slack %.4f)"
                  % (flag, (sig*(s/K)**xi)/(sig*(s/2/K**2)**xi), (ck*sig*(s/2/K)**xi)/(sig*(s/K)**xi)))
        if bad and K in (37,38,50) or (bad and K==12) or (bad and K==10):
            print("   K=%-3d xi=%.2f -> %s" % (K, xi, flag))

print()
print("=== ITEM 1.4: the K threshold, solved and bisected independently ===")
def ok(K, xi): return 2**xi <= CK(K, xi)          # binding case h = s/2
for xi in (0.1,0.2,0.3,0.35,0.37,0.4,0.5,0.6,0.75):
    lo, hi = 2.0, 1e9
    for _ in range(200):
        mid = math.sqrt(lo*hi)
        if ok(mid, xi): lo = mid
        else: hi = mid
    closed = (1.0/(1.0-2**(-xi)))**(1.0/(1.0-xi))   # closed form
    print("   xi=%.2f  Kmax(bisect)=%9.4f  Kmax(closed)=%9.4f  int Kmax=%d" % (xi, lo, closed, int(math.floor(lo))))
print("   K=37,xi=.75:", ok(37,0.75), " C_K=%.6f vs 2^xi=%.6f" % (CK(37,0.75), 2**0.75))
print("   K=38,xi=.75:", ok(38,0.75), " C_K=%.6f vs 2^xi=%.6f" % (CK(38,0.75), 2**0.75))

print()
print("=== ITEM 1.2: minimum chord clearance of the FAR child vs its own-scale quantile ===")
# far child: (d(s), (K-1)h/K) -> (D, h). own scale h/K, quantile q = sig*(h/K)^xi
K, xi = 5, 0.75
worst = math.inf
for i in range(0, 501):
    h = 0.5 + 0.5*i/500.0
    q = sig*(h/K)**xi
    ds = sig*(1.0/K)**xi
    for D in (sig*(h/K)**xi, CK(K,xi)*sig*h**xi):     # bottom edge, top edge
        worst = min(worst, min(ds, D)/q)
print("   min over class of (min clearance)/(own-scale quantile) = %.6f   (>=1 required)" % worst)

print()
print("=== ITEM 2.3: unstratified base exponent, recomputed ===")
K = 5
log_K_2 = math.log(2)/math.log(K)
for c in (0.10, 0.12, 0.1217647, 0.125, 0.15):
    e = log_K_2*(1-c) + c
    print("   c=%.7f -> exponent %.7f  %s" % (c, e, "clears sqrt" if e < 0.5 else "FAILS"))
print("   log_5 2 = %.7f ; break-even c = %.7f" % (log_K_2, (0.5-log_K_2)/(1-log_K_2)))
# direct simulation of the unrolled recursion, no closed form
l = 10.0**40
r0 = l**0.12
J = math.log(l/r0)/math.log(K)
print("   direct: J=%.4f  2^J=%.6e  l^0.3789954=%.6e  (should match)" % (J, 2**J, l**0.3789954))
print("   forcing sums: 1/(1-1/sqrt5)=%.6f   1/(1-2/sqrt5)=%.6f" % (1/(1-5**-0.5), 1/(1-2*5**-0.5)))

print()
print("=== ITEM 2.5: touching sum with level-dependent crude, branching 2 ===")
for K in (5,):
    tot = sum((2.0/K)**j for j in range(0, 400))
    print("   sum (2/K)^j = %.6f  (finite iff 2<K) -> total touching = O(b l^(1-A))" % tot)

print()
print("=== ITEM 1.7 / V5-3 cross-checks ===")
for K in (4, 5, 6, 10):
    xi = 0.75; ck = CK(K, xi)
    tight = K*(ck**2 + 2**(2*xi) * K**(-2*xi))     # [d(s)^2 + (C_K d(Ks'))^2] K/s' at s'=s/2 worst
    printed = K**(1+2*xi)
    print("   K=%2d  tight bracket=%8.4f  printed K^(1+2xi)=%8.4f  %s (ratio %.4f)"
          % (K, tight, printed, "valid" if printed >= tight else "FAILS", printed/tight))
K, xi = 5, 0.75
print("   far-child tilt const: K*C_K*2^(1-xi)=%.4f vs printed K^(1+xi)=%.4f  -> short by %.2f%%"
      % (K*CK(K,xi)*2**(1-xi), K**(1+xi), 100*(K*CK(K,xi)*2**(1-xi)/K**(1+xi)-1)))
print("   class tilt: C_K*2^(1-xi)=%.4f vs printed 2*C_K=%.4f -> valid, slack %.3fx"
      % (CK(K,xi)*2**(1-xi), 2*CK(K,xi), 2*CK(K,xi)/(CK(K,xi)*2**(1-xi))))
print("   D=0 GEOM vs band GEOM at s'=s: ratio=%.3f"
      % ((K**(-2*xi) + CK(K,xi)**2)/(2*K**(-2*xi))))

print()
print("=== ITEM 3.3: dead-band rho thresholds ===")
A = 2.0
for theta in (1.0, 2.0, 4.0):
    print("   theta=%.0f  o(1) needs rho > %.4f ; sqrt(l) main claim needs rho > %.4f"
          % (theta, A**(-1.0/theta), (2*A)**(-1.0/theta)))
