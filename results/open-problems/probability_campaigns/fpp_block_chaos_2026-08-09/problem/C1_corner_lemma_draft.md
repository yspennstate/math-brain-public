# (C1): the corner case of BSS Lemma 2.8 on Z^2 - MAJOR REVISION REQUIRED

Status after the hostile referee (2026-08-09 21:1x): THE CONSTRUCTION SURVIVES, THE BOOKKEEPING DOES
NOT. Referee verdict verbatim: "Nothing here is fatal; the mathematics survives, the bookkeeping does
not. Do not export any claim from this document in its present form." The L3 construction was
attacked four separate ways (one-shot shift, independence improvement, wall-proximity skip,
reflection folding) and survived all four; the numerical table was reproduced exactly. What follows
is the corrected reading. Do not cite the uncorrected sections below without these amendments.

REFEREE CORRECTIONS, in order of consequence:
1. THE THRESHOLD IS NOT 1/3. The alpha > 1/3 criterion assumed alignment error C Q_s log s, i.e.
   Alexander's estimate AT THE ENVELOPE SCALE - which is open whenever Q_r << sqrt(r). On the
   PUBLISHED bound (Alexander 1997: C sqrt(s) log s) the optimisation gives s = l^{2/(2+alpha)} and
   the criterion alpha^2 + 2 alpha - 1 > 0, i.e. alpha > sqrt(2) - 1 = 0.4142. So the workable window
   is (0.414, 1/2], not (1/3, 1/2], and alpha = 1/3 fails by a wide margin rather than marginally.
2. THE REDUCTION IS INCOMPLETE BY TWO CLAUSES. L3's sub-geodesics run at the direction of v-u, which
   is arbitrary, so it needs H1a (concentration) and H1b (alignment) with their angular windows
   removed as well as H1c. The correct statement: (C1) reduces to H1a+H1b+H1c with windows removed,
   at scales up to n^{2(beta+(1+alpha)/2)/(3-alpha)}, for alpha above the threshold in item 1.
   Confirmed independently: the source's own (96) proof needs an all-direction g-centred lower bound
   through its event B (Proposition 2.2), which the draft did not charge for.
3. "(C1) BECOMES THE WHOLE OF LEMMA 2.8" IS FALSE - and the draft contradicts itself on this (its own
   last paragraph flags (97)/(98) as not done). Residue after (96): (97) plus the Theorem-2.4 gluing
   event D. But (98) IS free on Z^2 by the lattice reflection x -> n-x, which the draft was
   over-cautious about. Honest residue: (96) + (97) + glue.
4. "DEVICE (a) AND NOTHING ELSE" / "(b) AND NOTHING ELSE" ARE BOTH FALSE AS READINGS OF THE SOURCE:
   Lemma A.3 invokes Theorem 2.4 twice, and the (93) branch's own reduction step IS (92), i.e. device
   (a). The seam is not clean in the source. It IS clean on Z^2, where (92) is an identity - so the
   operational conclusion survives while the stated reading of the source does not.
5. "THE SINGLE ROTATION-CONSUMING STEP" IS FALSE: there is a SECOND one the draft missed - event B's
   appeal to Proposition 2.2, which is stated only for slope <= 1 parallelograms and centred at the
   Euclidean norm, i.e. isotropy again.
6. "EVERY INCREMENT IS PARALLEL TO v-u" IS FALSE (the draft concedes the rounding ten lines earlier
   and then asserts exactness). The no-curvature conclusion SURVIVES but for a different reason:
   g is a norm, so |g(w_i) - g((v-u)/K)| <= 2b, total O(K), under budget. Replace the reason.
7. A PROOF STEP IS MISSING: Sum_i g(w_i) <= g(v-u) + O(K), the link between the per-increment
   Alexander bound and E T(u,v). Repairable without new hypotheses, but absent as written.
8. "SCALE RANGE CUT TO MICRO SCALES" IS AN ILLUSORY WEAKENING: Z^2 bond FPP is scale-free and the
   target is asymptotic in n, so requiring the hypothesis for all s <= n^{0.6} for every large n
   requires it for all large s. Strike the claim; the only genuine weakening is that no
   conforming-geodesic version is needed.
9. "STRICTLY NARROWER THAN H2" IS A NON-SEQUITUR AND PROBABLY BACKWARDS. Not using curvature in a
   derivation says nothing about hypothesis strength. H2-pointwise is curvature at ONE direction;
   the all-direction wandering this needs has, under every published route, only been proved under
   curvature on an ARC. On the evidence (C1) is plausibly STRONGER than H2-pointwise, not narrower.
   This propagates: MG2A's classification of (C1) as a narrow instantiation caveat must be revised.
10. THE DRAFT'S SIDE FINDING (i) IS CORRECT AND IS ITS MOST VALUABLE OUTPUT: MG2A's H1 window is a
   factor n^beta too narrow for MG2A's OWN consumption accounting. Fix in MG2A: omega_r >= C_M n^beta
   W_r / r (still o(1) since beta < 1/4).

WHAT STANDS UNCHANGED: L1 (verified, including the sign-symmetry attack the referee ran), L2
(verified by brute-force Dijkstra at six sizes), the shortfall arithmetic, the L1+L3 range tiling,
the numerical table, and the structural DIRECTION of the inversion (the independence half is the
Z^2 tautology; the confinement half carries the content).

## 1. What the corner argument delivers (agent's READ of the source)

The source's restricted distance serves TWO purposes, implemented by TWO devices: (a) block
independence, via the enlarged field with per-column independent copies; (b) the conforming
(no-backtrack, column-contained) path class. Lemma 2.8 splits along exactly that seam:
- display (87) (X <= Xbar + n^{-eps} Q_n) reduces to an exchangeable-pair environment comparison -
  this branch is device (a) and nothing else;
- display (93) (Xbar <= X + n^{-eps} Q_n) reduces, by the source's own step "by (92) it suffices to
  replace X_uv by X^{Lambda_i}_uv", to a statement where BOTH sides live in the same field and the
  only difference is the geometric constraint gamma contained in Lambda_1 - this branch is device
  (b) and nothing else.
(96) is the corner case of the (b) branch: for u,v in the left-edge box [0,h] x [-2h,2h] with
h = n^beta W_n, at ARBITRARY relative direction, bound Xbar_uv - X^{Lambda_1}_uv from above by
n^{-3eps} Q_n off an event of probability exp(-4 n^{theta_1}). Consumed via (95) -> Lemma A.4 ->
(93) -> Lemma 2.8 -> PROPOSITION 2.9, which is the restricted-distance form of the entire imported
estimate package and the workhorse of Sections 4-9.

The single rotation-consuming step is localized to one sentence: "there exists an |u-v| x W_{|u-v|}
rectangle R contained in Lambda_1 such that one of the sides of R is the straight line segment
joining u and v", followed by an appeal to Proposition 2.6, which is stated for an AXIS-ALIGNED box
and applied to a rectangle tilted to an arbitrary angle.

## 2. Is it needed on Z^2? THE ANSWER INVERTS THE CAMPAIGN'S EXPECTATION

Not vacuous. The lattice's free block independence kills the (87) branch entirely (conforming paths
are a subfamily in the same field, so T <= Tbar is a tautology) - but (96) lives in the (93) branch,
which is about CONFINEMENT geometry, not independence. So on Z^2, (C1) does not shrink: it becomes
the WHOLE of Lemma 2.8. The half that dies is the other half.
Nor can conformity simply be dropped: from the source's line ~803 onward every event in Sections
4-9 is a restricted-distance event, and Proposition 2.9 (their basis) is derived FROM Lemma 2.8.
Dropping conformity is not a repair to Appendix A; it is a different proof of Sections 4-9.

## 3. The proposed axis-respecting replacement

Setting: Z^2 bond FPP, iid weights in [a,b], d = l1 distance, g the time-constant norm,
Lambda = {0 <= x <= n}, T_Lambda the confined passage time, h = n^beta W_n, corner box
B = [0,h] x [-2h,2h], envelope Q_r ~ r^alpha, W_r = sqrt(r Q_r) = r^{(1+alpha)/2}.
TARGET: whp, max over u,v in B of [T_Lambda(u,v) - T(u,v)] <= n^{-3eps} Q_n.

LEMMA L1 (deterministic confinement bound). 0 <= T_Lambda(u,v) - T(u,v) <= (b-a) d(u,v).
Proof: fewer paths gives the left; a monotone staircase inside the bounding box (which lies in
Lambda since both x-coordinates are in [0,n]) has d(u,v) edges of weight <= b, and every path has
>= d(u,v) edges of weight >= a. Uses only l1 geometry and the axes - no rotation.

LEMMA L2 (L1 is unimprovable). For each m there is an admissible configuration with d(u,v) = m and
T_Lambda - T >= (b-a)m - 2a: weight b on every edge with both endpoints in {x >= 0}, a elsewhere;
the confined distance is bm, the detour through the column {x = -1} costs a(m+2).
Consequence: no deterministic route beats L1; any improvement must be probabilistic.

SHORTFALL: L1 delivers (b-a)*diam_1(B) ~ n^beta W_n against a requirement n^{-3eps} Q_n; the ratio
is n^{(1-alpha)/2 + beta + 3eps}. Since Q_n = O(sqrt n) forces alpha <= 1/2, the deterministic route
misses by at least n^{1/4} (n^{1/3} at the conjectured alpha = 1/3). Structurally W_n >= Q_n always,
so L1 cannot even reach Q_n. L1 does settle all pairs with d(u,v) <= n^{-3eps} Q_n/(b-a), covering a
small-scale range the source's Prop 2.6 ("r sufficiently large") passes over.

LEMMA L3 (shifted parallel chain). Assume (W) micro-scale all-direction wandering at scale W_s,
(C) concentration at Q_s, (A) Alexander alignment, (R) the H3 ratio bounds. If alpha > 1/3 and
beta, eps, delta_1 are small enough depending on alpha, the TARGET holds.
Construction: fix u,v in B with l = d(u,v); set s = l^{2/(3-alpha)}, K = ceil(l/s), z_1 = n^{delta_1},
D = ceil(z_1 W_s) + 1; put u^{(i)} = u + floor((i/K)(v-u)) + D e_1, so the whole chain is TRANSLATED
into the column by D in the +e_1 direction and every increment is PARALLEL to v-u. On the event that
each sub-geodesic stays within z_1 W_s of its own segment, the concatenation lies in Lambda, so
T_Lambda(u,v) <= 2bD + sum_i T(u^{(i)}, u^{(i+1)}). Telescoping the increments (they sum exactly to
v-u, each within 1 per coordinate of (v-u)/K), subadditivity and (A) give
sum_i E T(u^{(i)},u^{(i+1)}) <= E T(u,v) + C K Q_s log s, whence on the good event
  T_Lambda(u,v) - T(u,v) <= 2bD + C K z_1 Q_s log s + z_1 Q_l.
The two live terms are the shift ~ z_1 W_s = z_1 s^{(1+alpha)/2} and the chaining cost
~ z_1 (l/s) Q_s log s; minimising over s gives s = l^{2/(3-alpha)} and common value l^{(1+alpha)/(3-alpha)}.
With l ~ n^{beta + (1+alpha)/2} and target n^{alpha - 3eps}, the criterion at beta = eps = delta_1 = 0 is
  (1+alpha)^2 < 2 alpha (3 - alpha)  <=>  3 alpha^2 - 4 alpha + 1 < 0  <=>  1/3 < alpha < 1.
Numerical checks: alpha = 1/2 gives l = n^{0.75}, s = n^{0.6}, shift = chaining = n^{0.45} against
budget n^{0.5} - closes with slack. alpha = 1/3 gives shift = chaining = n^{1/3} against budget
n^{1/3} - exactly critical, does NOT close.
WHAT L3 CONSUMES: translations, l1/l-infinity metrics, subadditivity, Alexander alignment,
concentration, micro-scale wandering. NO rotation, NO reflection, NO FKG, and - because every
increment is parallel to v-u - NO CURVATURE of g at any direction. That last is the construction's
main advantage over a literal transplant of the source's dyadic corridor climb, whose increments
vary in slope and would require an all-direction upper C^{1,1} bound on g, an input strictly beyond
pointwise curvature.

## 4. The reduction, stated exactly

(C1) REDUCES TO (W-micro): for every direction and every s up to about n^{(beta + (1+alpha)/2) *
2/(3-alpha)}, the geodesic between two points at distance s stays within z W_s of the segment
joining them with probability at least 1 - C exp(-z^theta). This is the lattice form of the source's
Theorem 2.4, i.e. H1c WITH ITS o(1) ANGULAR WINDOW REMOVED but with its scale range cut to micro
scales. It is NOT implied by H1 as MG2A states it (H1's clauses are quantified over directions
within omega_r of the reference direction, while the corner box realises every direction), so (C1)
is either a widening of H1c or a standalone axiom. Still strictly narrower than H2 - under L3 it
needs no curvature at all - but not free.

## 5. Two side findings offered by the agent (unsettled)

(i) H1's window may be stated too narrow for its own consumption: the source's transversal range is
|y| <= n^beta W_n over spans down to r, so the consumed slope reaches n^beta W_r/r - polynomially
larger than a constant multiple of W_r/r, still o(1). Suggests restating H1 with omega_r >= n^beta W_r/r.
(ii) The alpha > 1/3 threshold is forced by the shift-versus-chaining trade, and degenerates exactly
at the conjectured KPZ envelope. If the campaign ever reaches alpha = 1/3, (C1) would need the
source's corridor construction and therefore an all-direction upper C^{1,1} bound on g - a curvature
obligation invisible at Kesten scale and appearing only at the true envelope.

NOT DONE: displays (97) and (98) (bulk and right strip) carry their own all-direction obligations; a
complete lattice Lemma 2.8 needs them too. Flagged, not claimed.
