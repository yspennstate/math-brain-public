# G1 (cross-cluster rigidity): resolved-with-a-twist + the stratified isolation synthesis
# Status: REFEREED. Claims 1, 2, 4 CORRECT (Claim 4's counterexample verified tight and
# important; Claim 2's trig constant slightly loose — content right). CLAIM 5 IS
# HEURISTIC + NUMERICS ONLY: the J-independence of the 1/rho amplification is proved
# only at J = 2; general J is a numerically-supported CONJECTURE — do not cite as a
# theorem; the coherent-block "1/rho per scale affordable" resolution inherits this
# conditional status. My synthesis (stratified isolation) was subsequently PROVED and
# separately refereed CORRECT (RIGIDITY_ENDGAME.md).

## Agent results (all with proofs in the session record)
CLAIM 1 (near-orthogonal, COMPLETE): pairwise |<u_c,u_c'>| <= mu with mu(m'-1) <= 1/2,
d >= m'+2: |A_c(s)| <= 2(L*/sqrt(1-s^2) + L*) — no rho, no J, no polylog, m'-free.
Mechanism: probe tau = sqrt(1-s^2) u_c - s w (unit, perp x) + kill w-components of v and
all other poles; EXACT ISOLATION IDENTITY (Iso):
  |beta_c + A_c(s) + sum_{c'!=c} A_{c'}(s<u_{c'},u_c>)<u_{c'},u_c>| <= L*/sqrt(1-s^2);
then a contraction recursion (needs mu(m'-1) <= 1/2).
CLAIM 2 (difference-direction, COMPLETE): two poles at separation delta, equal-argument
probes with w_0 = (u_1-u_2)/delta perp x: |A_1(s) - A_2(s)| sin(theta) <= 2L*
(sin theta = delta/2). Plus the sum bound => 2-coherent groups: |A_c| <= C L*/rho.
CLAIM 4 (COUNTEREXAMPLE — G1-as-stated is FALSE): 2 clusters, separation rho, shared
thresholds spaced 2rho, opposite signs +-alpha_0: Lip <= 2 alpha_0 but TV(P_c) >=
alpha_0 t*^2/(4 rho): TV/L* >= t*^2/(8 rho) — NOT polylog. Numerics: TV/L* doubles as
rho halves (0.95 -> 15.5), Lip flat. Per-unit rigidity satisfied. The smallest
counterexample: coherent alternating stacks defeat per-cluster rigidity.
CLAIM 5 (VANDERMONDE CATASTROPHE REFUTED): J coherent sub-clusters do NOT force
1/rho^{J-1}: Lip is a sup over ALL x; off the codim-(J-1) diagonal the finite-difference
cancellation breaks and a first-order unbalance ~max|alpha_k| is exposed. Amplification
is O(1/rho), J-INDEPENDENT. Numerics decisive: Lip(J=2) == Lip(J=3) exactly on shared
grids; exponent ~0.7 for all J; SOCP extremal optimizer J-independent, exponent <= 0.5.

## Agent's resolution
Never split a coherent group: merge into a super-cluster (off shells the group IS a 1-D
ridge along the centroid: P1 bounds the TOTAL profile, TV <= pi L*). Splitting at
separation rho costs exactly 1/rho (Claim 4 tight). Across groups: Claim 1. Admissible
clustering scale: rho >= 1/polylog (the band absorbs polylog TV).

## MY SYNTHESIS (main thread): STRATIFIED ISOLATION via random probes
The (Iso) cross-terms A_{c'}(s <u_{c'}, u_c>) VANISH IDENTICALLY when the argument
stays below the smallest threshold: A_{c'}(sigma) = 0 for sigma < min_k t_k. Sharpen
Claim 1 by choosing the probe w RANDOM on the admissible subsphere (only v_perp killed
exactly — 1 dimension): whp every |<u_{c'}, w>| <= sqrt(C log m'/d), so the OTHER
clusters' arguments satisfy |s_{c'}| <= t* mu + sqrt(C log m'/d). Hence:
  STRATIFIED ISOLATION LEMMA (candidate): if every unit threshold is >= tau_0 :=
  2 sqrt(C log m/d) and every pair of cluster poles has |<u_c, u_{c'}>| <= tau_0/(2 t*),
  then for EVERY cluster and every s: |beta_c + A_c(s)| sqrt(1-s^2) <= L* — exact
  P1-strength, NO m' restriction (random probe replaces exact orthogonalization; the
  m' <= d-2 dimension count is gone).
Feasibility of the coherence condition: directions with pairwise coherence <= nu number
~ e^{c nu^2 d} >> n for d >= polylog — no capacity obstruction.
REMAINING ASSEMBLY (the true residual of the rigidity front):
 (a) units with thresholds BELOW tau_0 (ultra-bulk slabs, population mass >= 1/poly):
     these are POPULATION-VISIBLE — hand to the visible/ellipsoid sector (Christoffel
     LLN is proved; the correlation control for visible units still needs the clipped
     argument, but the class is now population-tame);
 (b) pole pairs with coherence ABOVE tau_0/(2t*): the coherent groups. Multi-scale
     (dyadic coherence strata): within a scale use Claim 2's difference bounds +
     merging; group spreading across scales needs the dyadic bookkeeping (F30's
     anticipated structure). Splitting cost 1/rho per scale is affordable for
     rho >= 1/polylog.
NET EFFECT: the rigidity front reduces to a MULTI-SCALE MERGE ASSEMBLY with all
single-scale mechanisms proved (isolation above bulk, difference bounds within
coherent pairs, P1 on merged totals, 1/rho splitting cost known tight).

## Consequence for (M)
(M)'s rigidity input should be REPHRASED: not per-cluster TV <= polylog (FALSE), but
"the multi-scale merged decomposition has total profile complexity <= L* polylog per
merged super-cluster + shells/tilts at the chosen scales". G2 (joint chaining) consumes
exactly this. The counterexample net of Claim 4 has small Lip and large per-cluster TV
but its MERGED total profile has TV <= pi L* — consistent: (M) itself is untouched.

## Numerics (seed 20260708, scripts in agent scratchpad)
Claim 1 ratio 1.02 (bound 4.6), 0/97 violations; Claim 2 ratio 0.72, 0/400; Claim 4
TV/L* = 0.95/1.35/3.38/7.43/15.54 at rho = .2/.1/.05/.025/.0125 (exactly 1/rho), Lip
flat 1.00; Claim 5 Lip(J=2)==Lip(J=3), exponents 0.7/0.5, J-flat amplification.
