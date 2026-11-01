# Band machinery: Claims 1-7 + the irreducible statement (M) — from the charging agent
# Status: REFEREED (independent adversarial pass, "no fatal errors; sound modulo (M)").
# Fixes 2-5 from the referee are APPLIED below; fix 1 = prove (M) = the campaign itself.
# Verification ledger: agent derivation + independent referee = 2 passes. Before any
# paper integration, add my own line audit as the third pass (house standard).

Setting. Model (S): x_i iid uniform on S^{d-1}, d >= 3; y_i iid +-1 independent of x.
Band: m = n/T, 4 <= T <= log^C n; L* = c0 eps sqrt(T). f canonical: f = <v,x> + c +
sum_{k<=m} alpha_k relu(<u_k,x> - t_k), t_k in [0,1); rigidity |alpha_k| sqrt(1-t_k^2) <= 2L.
Op := lambda_max(sum_i x_i x_i^T); r_k := (relu(<u_k,x_i>-t_k))_i; S_k := ||r_k||_1.
"Fits": (1/n) sum (f(x_i)-y_i)^2 <= 1-eps.

## Claim 1 (fitting identity: penalty, correlation, serving forms)
If f fits: (i) sum_i [y_i f(x_i) - f(x_i)^2/2] >= eps n/2, hence sum_i y_i f(x_i) >= eps n/2;
(ii) same for G := clip.f (clip contracts toward y_i in [-1,1], so G fits too);
(iii) #{i : y_i f(x_i) >= eps/4} >= eps n/2.
Proof. Expand sum(f_i-y_i)^2 = sum f_i^2 - 2 sum y_i f_i + n <= (1-eps)n; rearrange.
(iii): each summand of (i) <= 1/2, and <= eps/4 when y_i f_i < eps/4; eps n/2 <= eps n/4 + |S|/2.

## Claim 2 (occupancy)
Deterministically, every u, t>0: N_u(t) := #{i : <u,x_i> >= t} <= Op/t^2. With prob >= 1-2e^{-n}:
Op <= C_1(1+n/d) =: Opb. Tight: for k <= sqrt(d/(C log n)), u = normalized sum of k data points
gives N_u(1/(4 sqrt k)) >= k.
Proof. N t^2 <= u^T(sum x_i x_i^T)u <= Op. Concentration: rows sqrt(d)x_i isotropic sub-gaussian
(Vershynin 3.4.6 + Thm 4.6.1 at t = sqrt n). Aimed u: whp pairwise |<x_i,x_j>| <= C sqrt(log n/d);
||sum_{j<=k} x_j||^2 <= 2k and <sum, x_j> >= 1/2 for d >= Ck^2 log n => <u,x_j> >= 1/(2 sqrt(2k)).

## Claim 3 (value mass; l1-closure of high thresholds)
On the Op event: S_{u,t} <= min(2 sqrt(n Op), Op/t, (1-t)Op/t^2); with rigidity, uniformly in
t_k in (0,1): |alpha_k| S_k <= 5 L Op/t_k. Hence for every y simultaneously,
sum_{k: t_k >= t_*} |alpha_k <y, r_k>| <= 5 m L Op/t_* <= eps n/64 once t_* >= 320 L Op/(eps T).
In the band t_* = 320 c0 Opb/sqrt(T); nonvacuous (t_* < 1) iff d >= C n c0/sqrt(T), else every
unit is battle zone (t_* capped at 1, g_hi empty).
Proof. Layer cake S = int_t^1 N(s) ds with N <= min(n, Op/s^2). t <= 1/2: |alpha| <= (4/sqrt3)L,
S <= Op/t => <= 3 L Op/t. t > 1/2: |alpha|S <= [2L/sqrt(1-t^2)](1-t)Op/t^2 =
2LOp sqrt(1-t)/(t^2 sqrt(1+t)); writing this as [2 sqrt(1-t)/(t sqrt(1+t))] L Op/t, the
bracketed coefficient is 2.31 at t = 1/2 and decreasing on (1/2, 1), so <= 2.31 L Op/t there.
(The referee note: the un-factored prefactor 2 sqrt(1-t)/(t^2 sqrt(1+t)) equals 4.62 at
t = 1/2 — the 2.31 is the L Op/t coefficient.) Overall constant 5 is safe. |<y,r_k>| <= S_k.

## Claim 4 (per-unit serving capacity, quadratic, tight)
For every h > 0, every unit: #{i : y_i alpha_k relu_k(x_i) >= h} <= Op/(t_k + h/|alpha_k|)^2
<= 6 Op L^2/h^2. Single-domination fitting forces eps n/2 <= m 6 Op L^2 (4/eps)^2 = 96 c0^2 Op n,
impossible for c0 STRICTLY < sqrt(eps/(192 Opb)) (strict, so the contradiction is strict;
referee fix).
Proof. Served => <u_k,x_i> >= t_k + h/|alpha_k|; Claim 2. t_k <= 1/2: Op(|alpha|/h)^2 <=
(16/3)Op L^2/h^2. t_k > 1/2: nonempty serving needs h^2 <= 4L^2(1-t_k)/(1+t_k) <= (4/3)L^2, and
N <= Op/t_k^2 <= 4Op <= 6OpL^2/h^2. Tight: aim at k = (2L/h)^2 points, d >= Ck^2 log n.

## Claim 5 (gradient-cloud rigidity; rigorous pile-up)
Ball model, D = int B_2, Lip_D(f) <= L. At generic x: grad f(x) = v + s_{A(x)},
s_A := sum_{k in A} alpha_k u_k, A(x) = {k : <u_k,x> > t_k}. For ANY two realizable active sets
A, A': ||s_A - s_{A'}|| <= 2L (gradient cloud diameter <= 2L).
Corollary (pile-up). HYPOTHESIS (non-automatic, load-bearing — referee flag): some generic x
activates B u G while some generic x' activates exactly B ("pair-realizability"). If also G has
|alpha_k| in [a, A_max] and pairwise |<u_j,u_l>| <= a^2/(2 A_max^2 |G|), then ||s_G|| <= 2L and
||s_G||^2 >= a^2|G|/2, so |G| <= 8 L^2/a^2. On S^{d-1}, pair-realizability and small |x - x'|
CANNOT be simultaneously secured for clustered kink caps — this is precisely why (M) is
irreducible.
Sphere version. Tangential gradients: ||P_{x^perp}(s_A - s_{A'})|| <= 2L + 2|x-x'|(||v|| +
sum_k |alpha_k|). Error term UNCONTROLLED for clustered kink hyperplanes — exactly how
adversarial stacks evade group rigidity on S^{d-1}; why (M) is the irreducible remainder.
Proof. Rademacher a.e. differentiability on convex open D, ||grad|| <= L, explicit gradient at
generic points; subtract. Corollary: ||s_G|| = ||s_{B u G} - s_B|| <= 2L; cross terms <=
mu (sum|alpha|)^2 <= a^2|G|/2. Sphere: geodesic directional derivatives; ||P_{x^perp} -
P_{x'^perp}||_op <= 2|x-x'|.

## Claim 6 (affine sup identity + tail; consistency evidence — restated per referee)
A = [X 1] (n x (d+1)), P = proj onto col(A). Then sup_{v,c} [sum_i y_i(<v,x_i>+c) -
(1/4) sum_i (<v,x_i>+c)^2] = y^T P y, E_y y^T P y = rank(A) <= d+1, and
P(y^T P y >= C(d + log(1/delta))) <= delta (Hanson-Wright; ||P||_F^2 = tr P, ||P||_op = 1).
INTERPRETATION (per referee): this is a STANDALONE identity + tail — strong consistency
evidence that unbounded (v, c) is not the obstruction, with no harmonic split and no
logarithm. It is NOT load-bearing in Claim 7 (the assembly puts the affine part inside
(M)'s clip). The earlier "contributes <= eps n/8 to the penalty functional of Claim 1"
bridge is WITHDRAWN: the naive split f = a + g leaves an uncontrolled +g^2/2 term
((a+b)^2 >= a^2/2 - b^2 gives penalty <= [affine 1/4-penalty] + sum[y g + g^2/2], and that
last object is precisely what (M) governs — the route collapses back onto (M)).
Proof of the identity. Affine sample-vectors = col(A); sup_{z in col(A)} [<y,z> - ||z||^2/4]
= ||Py||^2 at z = 2Py. E y^T P y = tr P.

## Claim 7 (conditional Band Lemma — assembly)
(M) implies the Band Lemma: for fixed m in the band, w.p. >= 1 - 1/n - 2e^{-n} - e^{-c eps^2 n},
no f with Lip_S(f) <= c0 eps sqrt(n/m) fits eps below the noise floor (dyadic T union routine).
Proof. Fit + canonical + rigidity => band class; Claim 1(ii): sum y_i clip(f) >= eps n/2.
Split f = a + g_hi + g_lo at t_* (Claim 3). Pointwise |clip(f) - clip(f - g_hi)| <= |g_hi|:
sum y_i clip(f) <= sum y_i clip(a+g_lo) + sum_i |g_hi(x_i)| <= [(M)-sup] + eps n/64 (Claim 3,
deterministic in y). (M): E_y sup <= eps n/4; bounded differences <= 2 => McDiarmid: sup <=
3 eps n/8 whp; 3/8 + 1/64 < 1/2 — contradiction.

## (M) — THE EXACT MISSING SUB-STATEMENT (mesoscopic clipped multiplier bound)
There are absolute C, c0 > 0 such that in the band (4 <= T <= log^C n, m = n/T,
L* = c0 eps sqrt(T)), for d >= eps^{-2} log^C n, w.p. >= 1 - 1/n over x:
  E_y sup sum_i y_i clip( <v,x_i> + c + sum_{k: t_k <= t_*} alpha_k relu(<u_k,x_i> - t_k) )
      <= eps n/4,
sup over all (v, c, (alpha_k,u_k,t_k)) arising as the affine-plus-low-threshold part of a
canonical f = a + g_hi + g_lo with Lip_S(f) <= L*, sup_S |f| <= 2+2L*, rigidity, and
t_* = min(1, 320 L* Opb/(eps T)).
Pinning: (a) per-unit rigidity, unit budget m, t_k <= t_* inherited by (a,g_lo); global Lip and
value bounds hold only for full f — usable only through g_lo = f - a - g_hi. (b) bulk sub-range
t_k <= sqrt(C log n/d) should reduce via population ellipsoid/harmonic route with polylog loss
absorbed into the d-condition (F9) — not written, so (M) stated on all [0, t_*]. (c) Consistency:
aimed-stack attack yields <= 2 m L* Opb/t_* = eps n/160 < eps n/4 — (M) survives all known
constructions; Claims 4+5 close single-domination and organized near-orthogonal stacks; the open
core = unorganized/clustered stacks, where sphere group-rigidity error (Claim 5) is uncontrolled.

## Numerics (n=4096, d=256, m=256, T=16, L=1; script band_checks.py in agent scratchpad)
Op = 25.08 vs (1+sqrt(n/d))^2 = 25.0; occupancy sup t^2 N(t) <= 0.118 Op (8x slack).
Claim 3 worst ratio 0.14 (bound 5); Claim 4 worst 0.040 (bound 1).
Claim 6: y^T P y mean 256.1, max 318.5 (200 draws) vs d+1 = 257.
Aimed-cluster attack (greedy, interference incl.): best corr/n = 0.518 at k=16; corr/(mL) = 8.3;
attack reaches noise floor at L = sqrt(n/m)/4 at Op = 25 — consistent with c0 ~ sqrt(eps/Op)
degradation; asymptotic band (Op = O(1)): attacks ~sqrt(T) below conjectured threshold.
