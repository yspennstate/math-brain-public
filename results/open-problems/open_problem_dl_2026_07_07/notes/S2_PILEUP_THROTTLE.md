# (S2) closed for the amended aimed class: the throttle is aggregate-Lipschitz, not codes
# Status: agent-derived + numerically decisive (seed 20260708). The "spherical-code /
# incoherent-cap packing" framing of (S2) was a RED HERRING: as a pure ledger/incoherence
# statement (R') is FALSE in the window (random-design counterexample, gain ~ n^{1/3}/T).
# It is TRUE only because the true class carries Claim-5 aggregate-Lipschitz, which the
# ledger reduction dropped. Restoring it throttles the multiplicity to O(1) elementarily.

## The counterexample to the UN-amended residual (kills the codes framing)
Random aimed design: m' caps = random k-subsets of the majority class, k = k* = 1/(4 tau_0^2),
poles = normalized block sums. In the window d in [slice, ~n^{2/3} log(m'n)] it is
INCOHERENCE-LEGAL (systematic coherence 2k/n << nu; fluctuation within budget for t* <= 1/2:
numerics 99.9% of pairs <= nu) and captures W ~ Phi_det = (Phi_det/Phi_disj) Phi_disj with
  Phi_det/Phi_disj = 1/(4 T tau_0 delta*) = Theta( n^{1/3} / T )  (GROWS, unbounded).
So no absolute-constant ledger bound W <= C Phi_disj can hold on the window. The earlier
sweeps missed this only because their params (n<=8192, T=16) had the window EMPTY
(slice >= n^{2/3}log <=> T >= 32 c_0^2 n^{2/3}). The J-fold cores are real, legal, and
value-cheap (J v(k*) << B) — nothing in the ledger stops them.

## What stops them: Claim 5 restored (aggregate-Lipschitz), used at ONE point
The net has Lip_S(f) <= L*; the ledger kept only per-ridge slope Lambda + height h_0 and
DROPPED the aggregate gradient. Paper Lemma pileup got stuck comparing gradients at two
points x, x' (pair-realizability + |x-x'| error, uncontrolled for clustered caps). But at an
AIMED co-covered data point the entire active set IS the aligned aiming group (a non-aiming
cap activates x_i with prob ~ (m'n)^{-1} by the def of tau_0 => base empty whp). So a
SINGLE-POINT bound suffices, no pairing:
  grad w(x_i) = y_i Lambda sum_{g rising at x_i} u_g,  poles pairwise nu-incoherent
  => ||sum u_g||^2 >= J(1-(J-1)nu) >= J/2  (J = O(1) << 1/nu)
  => ||grad w(x_i)|| >= (Lambda/sqrt2) sqrt(J);  and <= L* (+ ||v|| <= L*)
  => J_i <= J_max := 8 (L*/Lambda)^2 = O(1/C_L^2).      [C_L = Lambda/L*]

## (S0) survives the deep-peel (gradients change only on deep sets)
f = a + w_1 + w_2, w_2 = above-h_0 excess. grad w_2 is supported on DEEP sets
{s_g > t_g + delta*}. On the rising annuli (t_g < s_g < t_g+delta*) w_2 contributes nothing,
so grad w_1 = grad f - v there, giving ||grad w_1|| <= L* + ||v|| <= 2L* exactly where the
slope-cap pile-up lives. Ceiling own-points (deep) are the only place grad w_1 != grad f - v,
and they are Tier-0 territory. So the amended shallow class legitimately carries
||grad_S w_1|| <= 2L* on the rising annuli.

## THE THROTTLE THEOREM (the prize) — all d above the slice, uniformly
Every legal design in the amended shallow class has
  W = sum_g k_g v(k_g) <= (C_0 + J_max) Phi_disj = O(1/C_L^2) Phi_disj.
Proof. Split ridges: ceiling (k <= k_ceil) => Tier 0, W_ceil <= h_0 m' k_ceil <= C_0 Phi_disj.
Slope (k > k_ceil): v(k) <= h_0, so W_slope = sum k_g v(k_g) <= h_0 sum_{slope} k_g =
h_0 M_slope; and M_slope = sum_i J_i <= n max_i J_i <= n J_max (pile-up); so
W_slope <= h_0 n J_max = J_max Phi_disj. QED. Needs NO d_pair -- subsumes Tiers 0/1/2 and
CLOSES [d_slice, d_pair] outright (given the amended class).

## Numerics (seed 20260708; pileup_throttle.py in agent scratchpad; < 30 s)
(A) ledger sweep T=4,c0=.12,C_L=.5 (J_max=4): unthrottled legal gain W(k*)/Phi_disj =
1.39,1.72,2.13,2.66,3.34,4.19 at n=2k..64k (GROWS ~ n^{1/3}), J_rand 7.8..70.9 >> J_max=4.
(B) sphere n=8000,d=3000 (window (783,6635)): attack k*=23, J=11.5, coherence 99.9%<=nu,
own-depth 0.209 = k*^{-1/2}, W/Phi_disj=1.67, ||grad w||/L* median 2.23 max 2.70 => aggregate-
Lipschitz VIOLATED. Throttled k=8 (J~4): W/Phi_disj=1.40 <= clean bound J_max=4.

## Still open (honest)
- (S1) general->aimed MUST now also carry Lip_S <= L* (not just value+incoherence+slope);
  it also supplies the effective-kink >= tau_0 that makes the base empty (=> single-point
  pile-up replaces the failed two-point Lemma-pileup). The clustered-kink core of (M) is
  now consolidated ENTIRELY into (S1); (S2) is finite/elementary given it.
- pointwise vs average multiplicity: legality is max_i J_i <= J_max (pile-up gives exactly
  this); a design with only AVERAGE J = J_max is not legal (local Poisson excess) and
  captures strictly less -- the bound W <= J_max Phi_disj is for genuinely legal designs.
- exact J_max and tightness: numerics say achieved J_ach = 1 (disjoint), so O(1) is loose
  but sufficient; the throttle needs only C_L = Omega(1), which holds (Lambda <= L*).
