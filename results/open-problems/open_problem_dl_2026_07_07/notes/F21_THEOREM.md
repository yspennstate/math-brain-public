# F21' — localized projection floor (final form from the write-up agent)
# Status: derived + numerics-verified by the agent; REFEREE PENDING before paper insertion.
# KEY CORRECTIONS vs the F21/F27 plan (both verified):
#  1. "all m at d >= Cn" is FALSE: psi(t) = t gives a min-norm exact interpolant with
#     Lip <= C sqrt(n) at EVERY width for d >= Cn (sigma_min(X) >= c) — conjecture TIGHT
#     there; any floor beyond C sqrt(n) impossible; the method needs n >= C(m+1) d Lambda.
#  2. Negative association (Joag-Dev--Proschan; Dubhashi--Ranjan Chernoff transfer)
#     replaces McDiarmid: no d >= sqrt(nm) condition; full n^{2/(m+1)} exponent survives.

THEOREM (localized projection floor). Model (S), y iid signs. p := m+1, Lambda := log(nd).
Assume d >= Cp and n >= C p d Lambda. Then w.p. >= 1 - C e^{-d/C}, for EVERY Lipschitz psi
and every width-m exact interpolant:
  (I)  Lip >= (c sqrt(d)/p) n^{1/p};
  (II) if p <= c log n:  Lip >= (c sqrt(d)/p) (n^2/(p d Lambda))^{1/p}.
Proof skeleton: factorization + fiber transport (from thm:genact, eq:fibertransport);
localization: for every rank-p projector Q, sum_i ||Q x_i||^2 <= p Op, so at most n/8
points above tau = (8 C_1 p (1/n + 1/d))^{1/2}; r_0 := 2 sqrt(p/d) <= tau <= 1/8.
Net of rank-p projectors at delta/4, |N| <= e^{C p d log(C/delta)} <= e^{C p d Lambda}.
(I): pigeonhole at radius tau with delta = 4 sqrt(p) tau (8/n)^{1/p}: >= 3n/8 disjoint
same-cell pairs.
(II): birthday pairing at radius r_0: N* = ceil(C_0 p d Lambda), delta = 14 sqrt(p) r_0
(N*/(c_2 n^2))^{1/p}; light/mid/heavy cell trichotomy; light: second moment mu >= 2^{p+1}
N* via P(n_c >= 2) >= n^2 q_c^2/(4e^2) + Cauchy-Schwarz; NEGATIVE ASSOCIATION of
multinomial occupancy (Joag-Dev--Proschan) + monotone-preservation + Chernoff transfer
(Dubhashi--Ranjan) gives lower tail e^{-mu/8}; mid: >= n/128 cells with P(n_c>=2) >= 1/5;
heavy: Bin(n, 1/4) domination. All cases: |Pi| >= N* w.p. 1 - 2 e^{-c N*}.
Labels: disjoint pairs, P(no opposite pair | x) <= 2^{-|Pi|}; union e^{C p d Lambda}
absorbed by N* (C_0 large). Conclusion via fiber transport: L >= 2/(3 delta).

COROLLARY (per-width curve, verified). F_m >= c sqrt(n/m) iff d >= n^{(m-3)/(m-1)} gamma,
gamma <= (C(m+1) Lambda)^{2(m+2)/(m-1)} <= polylog inside the admissible window.
m=1: floor c n/sqrt(Lambda) — conjecture met with margin sqrt(n/Lambda), all C <= d <=
n/(C Lambda). m=2: floor c d^{1/6} n^{2/3}/Lambda^{1/3} — closes on the ENTIRE admissible
range once n >= C Lambda^2 (no d-condition beyond d >= C). m=3: closes for d >= C
Lambda^5. m >= 4: window [n^{(m-3)/(m-1)} gamma, n/(C(m+1) Lambda)], nonempty iff
m <= c log n/loglog n.

REMARK (scope; the linear-activation ceiling). n >= C p d Lambda is NOT an artifact:
psi(t) = t at d >= Cn gives Lip <= C sqrt(n) interpolants at every width (min-norm
solve, sigma_min(X) >= c whp); the projector net e^{c p d Lambda} vs label budget e^n
confines ANY variant to p d Lambda <= n/C. For m >= 2, general psi, the regime
d >~ n/(m Lambda) remains open (PL covered by the main theorem).

NUMERICS (agent, seeds 20260707/8): pair-count law verified d in {50,100,200}, m in
{1,2,3} (constant 0.19-0.24, 2x tracking at N*); NA lower tail: 300 draws, mu = 51.4,
min 32, zero at mu/2; adversarial-W search m=1: best opposite gaps 8x above random-W,
all below the predicted ceiling 2 sqrt(Lambda)/n; implied floors 322/473/670 vs old
sqrt(n) ~ 32 at d = 30/60/120.

BIB (to verify at insertion): Joag-Dev & Proschan, Ann. Statist. 11 (1983) no. 1,
286-295; Dubhashi & Ranjan, Random Structures & Algorithms 13 (1998) no. 2, 99-124.

[Full LaTeX for thm:genact2 + cor:genactcurve + rem:genact2scope is in the agent report,
transcribed in the session; to be inserted into sec:genact after the referee pass.]
