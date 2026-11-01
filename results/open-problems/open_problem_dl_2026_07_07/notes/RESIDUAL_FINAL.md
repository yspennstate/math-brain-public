# The residual in final form: forced-depth, deep-peel, and (R')
# Status: Lemmas FD + DP + disjoint-case: agent proofs, MY AUDIT PASSED (all elementary);
# the negative results numerically decisive; (R') = the one remaining open statement.

Constants: delta* := 32 A Lambda m'/(eps n) (= 32 A C_L c_0/sqrt(T)); h_0 := Lambda
delta* = 32 A C_L^2 c_0^2 eps; tau_0 = sqrt(2 log(m'n)/d); nu <= tau_0/(2 t*).

## LEMMA FD (forced depth — complete, audited)
u_1..u_K pairwise nu-incoherent, x with <u_g, x> >= sigma > 0 for all g:
  K sigma <= ||sum u_g|| <= sqrt(K(1 + (K-1) nu))  =>  sigma <= sqrt(1/K + nu),
equivalently K <= (1 - nu)/(sigma^2 - nu) for sigma^2 > nu. Constraint ONLY above the
coherence floor sigma > sqrt(nu); VACUOUS at the anchor (tau_0^2 < nu) — shallow
overlaps are NOT forbidden (see N1).

## LEMMA DP (deep-peel — complete, audited)
Height-split at h_0: w = w_1 + w_2 (w_2 = the above-h_0 parts). Then UNCONDITIONALLY
(every y, every admissible config):
  ||w_2||_1 <= m' Lambda A/delta* = eps n/32,
valid whenever delta* >= tau_0, i.e. d > c_slice T log(m'n)/c_0^2 — the EXACT complement
of the deterministic slice. Residual class after the peel: shallow, per-ridge height
ceiling h_0 = Theta(c_0^2 eps), slope Lambda, anchored, incoherent poles, |w| <= B.

## DISJOINT-CAP CASE OF THE RESIDUAL: CLOSED (unconditional)
Pairwise-disjoint data caps: |w_1(x_i)| <= h_0 pointwise => l1 <= h_0 n <= eps n/32
for c_0 <= c*. No chaining, no randomness.

## NEGATIVE RESULTS (rigorous constructions + decisive numerics)
N1 (no disjointness lemma): two nu-incoherent poles can share ~1/(2 tau_0^2) data
points: u_+- = b c +- sqrt(1-b^2) r, b = tau_0 sqrt(p), coherence 2 tau_0^2 p - 1 <= nu
at p ~ 1/(2 tau_0^2). Verified: 62 shared points, legal coherence -0.014.
N2 (deterministic surrogates all vacuous above the slice): multiply-covered set can be
Theta(n); incidence bound h_0 I and solo/overlap split h_0 n + B|M| both >> eps n; raw
l1 = the deterministic optimum. The third triangle leg is now quantitative for the
SHARPEST surrogates, not just raw l1.
N3 (structural): Rademacher/Gaussian width is ADDITIVE over Minkowski sums — the
sqrt(m') gain CANNOT come from an orthogonal-subspace gamma_2-Pythagoras; it lives in
the VALUE-BALL INTERSECTION, realized only in the label average.
Attack search: no legal attack beats eps n/16; breaking it needs nu 7-12x over budget.
Legal overlap captures 6.6-20.7 vs target 46.9; ||w_1||_inf <= 0.12.

## (R') — THE one remaining statement (the shallow P4-lift)
  E_y sup over the shallow class of <y, w_1> <= C( h_0 sqrt(m' n) + B sqrt(n log(m'n)) ).
Given (R'): h_0 sqrt(m'n) = 32 A C_L^2 c_0^2 eps n/sqrt T and the additive term is
affordable => residual <= eps n/32 => with DP: E_y sup_W <= eps n/16 => (M) on
d > c_slice T log/c_0^2, content zone, c_0 <= c* => (with the deterministic slice below
and BAND_CLAIMS Claims 1-7 + F24) THE LOG-FREE PL LAW AT ALL WIDTHS for
d >= eps^{-2} log^C n. What (R') needs: a uniform-over-configs Talagrand two-part
decomposition (pole-aiming freedom into the l1 part, height-h_0 spread into the gamma_2
part). Preconditions all proved; the disjoint case closed; energy input ||w_1||_2 <=
C B sqrt(n) proved (numerics 0.14 -> 0.016).

## Assembled conditional theorem
cap-mass + occupancy + (R') => E_y sup_W sum y_i w(x_i) <= eps n/16 on
d > c_slice T log(m'n)/c_0^2, T >= 2/(c_0 eps)^2, c_0 <= c*. Unconditional content:
DP + the reduction + the disjoint case + the negative map.

## Numerics (seed 20260708, scripts in agent scratchpad, < 30 s each)
FD holds all trials (ratios 0.4-0.9); DP ||w_2||_1 = 0.11-0.21 << 23.4; legal attacks
~ c_0^2 eps n/2; energy 0.14 B sqrt n.
