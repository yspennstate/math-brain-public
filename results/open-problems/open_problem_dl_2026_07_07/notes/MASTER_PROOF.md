# MASTER PROOF — Law of robustness for two-layer networks with arbitrary weights
# (Bubeck–Li–Nagaraj Conjecture 1, piecewise-linear activations; Bubeck–Sellke open problem)

Status tags: every numbered claim below is intended PROVED; referee passes must attack each.

---------------------------------------------------------------------------
## 0. Setting and main statement

Domain/data. d >= 2. Two data models:
(S) mu = uniform on the unit sphere S^{d-1} in R^d;
(G) mu = N(0, I_d/d) (so ||x|| concentrates at 1).
(x_i, y_i)_{i<=n} iid: x_i ~ mu, y_i in [-1,1], sigma^2 := E[Var(y|x)] > 0.
BLN's generic-data case: y_i iid uniform {+-1} independent of x_i; then g == 0, sigma^2 = 1.

Networks. psi: R -> R piecewise linear with K >= 2 pieces (finitely many breakpoints;
ReLU: K = 2). Width-m class (arbitrary real weights, biases, skip connection, offset):
  NN_m := { f(x) = sum_{k=1}^m a_k psi(<w_k, x> + b_k) + <v, x> + c :
            a_k, b_k, c in R, w_k, v in R^d }.
(The skip term <v,x>+c only enlarges the class; BLN's class is the sub-class v=0, c=0.
Parameter count p = m(d+2) + d + 1 = Theta(md).)

MAIN THEOREM. There are absolute constants C0, c0 > 0 (with C_psi := K-1 entering only
multiplicatively in m) such that the following holds. Let eps in (0, sigma^2], delta in (0,1),
and assume n >= C0 eps^{-2} log(4/delta), and in model (G) additionally d >= C0 log(4n/delta).
Then with probability >= 1 - delta, EVERY f in NN_m satisfying
  (1/n) sum_{i<=n} (f(x_i) - y_i)^2 <= sigma^2 - eps
has
  Lip_D(f) >= c0 * eps * sqrt( n / ( m' * log(C0 m' n d / eps) ) ),   m' := (K-1) m + 1,
where D = S^{d-1} in model (S) and D = B(0,2) in model (G), and Lip_D is the Euclidean
Lipschitz constant on D. [Log factor: single log, explicit. For m' d >= n the bound is
below the trivial O(1) floor and the statement is vacuous-but-true.]

COROLLARY (Conjecture 1 of BLN, PL case). y_i iid uniform {+-1} independent of x_i
(sigma^2 = 1, take eps = 1/2): w.h.p. every width-m psi-network that fits the data exactly
(f(x_i) = y_i for all i; more generally with MSE <= 1/2) satisfies
  Lip(f) >= c1 sqrt( n / (m log(C1 m n d)) ).
This is the conjectured bound sqrt(n/m) up to a single logarithmic factor, with NO
assumption on the magnitudes of the weights — removing the poly(n,d)-boundedness
assumption of Bubeck–Sellke for the two-layer case. By BS Appendix A the analogous
statement at depth >= 3 with unbounded weights is FALSE, so depth two is the critical case.

---------------------------------------------------------------------------
## 1. Reduction to ReLU kinks (exact, all of R^d)

LEMMA 1 (PL expansion). Let psi be CPWL with breakpoints tau_1 < ... < tau_{K-1} and slopes
s_0, ..., s_{K-1}. Then for all s in R:
  psi(s) = psi(0) + s_0- s?? -- CAREFUL, write correctly:
Take the standard identity: with jumps D_kappa := s_kappa - s_{kappa-1},
  psi(s) = psi(tau_1) + s_0 (s - tau_1) + sum_{kappa=1}^{K-1} D_kappa ReLU(s - tau_kappa)
           - ??? check at s < tau_1: ReLU terms vanish, psi(s) = psi(tau_1) + s_0(s-tau_1). OK
           for s in (tau_kappa, tau_{kappa+1}): slope = s_0 + sum_{j<=kappa} D_j = s_kappa. OK.
           Values continuous. So identity holds exactly on R.  [PROVED — elementary]
Hence a_k psi(<w_k,x> + b_k) = affine(x) + sum_{kappa=1}^{K-1} a_k D_kappa ReLU(<w_k,x> + b_k - tau_kappa),
and NN_m (activation psi) is contained in NN'_{(K-1)m} := ReLU networks with skip+offset of
width (K-1)m. FROM NOW ON: psi = ReLU, width m' <= (K-1)m; write m for m'.

LEMMA 2 (canonical form on a domain). Let D be either S^{d-1} or the closed ball B_R
(R = 2), d >= 2. Every f in NN'_m can be written ON D as
  f(x) = <v, x> + c + sum_{j=1}^{m0} alpha_j ReLU(<u_j, x> - t_j),   m0 <= m,
with: ||u_j|| = 1; the sets H_j := {x : <u_j,x> = t_j} pairwise DISTINCT AS SETS and each
meeting the relative interior of D transversally in the sense:
 (ball case)   t_j in (-R, R)  [H_j cap int B_R is a nonempty (d-1)-disk];
 (sphere case) t_j in [0, 1)   [H_j cap S^{d-1} is a nonempty (d-2)-sphere, not a point].
Proof of reducibility:
 - neurons with w_k = 0 are constants -> absorb in c.
 - normalize u = w/||w||, t = -b/||w||, absorb ||w|| into alpha.
 - ReLU(-z) = ReLU(z) - z: flip (u,t) -> (-u,-t) at the cost of an affine term. Use this to
   enforce: (ball) a fixed orientation convention only for merging (see below); (sphere)
   t_j >= 0.
 - neurons whose kink set misses the required region: (ball) |t| >= R => ReLU(<u,x> - t) is
   affine (identically 0 or <u,x> - t) on B_R -> absorb. (sphere) t >= 1 => the active cap
   {x in S: <u,x> > t} is empty or a single point (t=1): the function ReLU(<u,x>-t) is 0 on
   S minus at most one point, and by continuity 0 on S -> drop. (After flipping to t >= 0,
   t in [0,1) remains.)
 - merge neurons with the same kink SET: two pairs (u,t), (u',t') give the same hyperplane
   iff (u',t') = (u,t) or (u',t') = (-u,-t). Using the flip identity, rewrite all on a common
   orientation and add coefficients; the residual affine parts go to (v,c). On the sphere the
   convention t >= 0 makes same-set pairs literally equal, except the equatorial case t = 0
   where (u,0) and (-u,0) both occur: merge via ReLU(-z) = ReLU(z) - z again.
 [PROVED — bookkeeping; referee should verify the equatorial merge and the t=1 point case.]

---------------------------------------------------------------------------
## 2. Rigidity (the crux): kink coefficients are bounded by the Lipschitz constant

LEMMA 3 (rigidity, ball). Let f be in canonical form on B_R with m0 distinct kink
hyperplanes meeting int B_R, and Lip_{B_R}(f) =: L < infty. Then |alpha_j| <= 2L for all j.
PROOF. Fix j. A := H_j cap int(B_R) is a nonempty relatively open (d-1)-dim disk. For l != j,
H_l cap H_j is an affine subspace of dimension <= d-2 (distinct hyperplanes), so
U := A \ union_{l != j} H_l is open in H_j and nonempty (a (d-1)-disk is not a finite union
of (d-2)-dim affine slices: e.g. by Lebesgue measure on H_j). Pick x* in U and r > 0 with
B(x*, r) subset int(B_R) and B(x*, r) cap H_l = empty for all l != j. On B(x*, r):
  f(x) = A(x) + alpha_j ReLU(<u_j, x> - t_j),  A affine.
phi(s) := f(x* + s u_j) for |s| < r: phi(s) = A(x*) + s <grad A, u_j> + alpha_j ReLU(s)
(using <u_j, x*> = t_j). phi is L-Lipschitz; its right and left derivatives at 0 are
<grad A, u_j> + alpha_j and <grad A, u_j>, both in [-L, L]. Subtract: |alpha_j| <= 2L. QED

LEMMA 3' (rigidity, sphere). Same, D = S^{d-1}, d >= 2 wait d >= 2 gives S^1: handle d >= 2
with the (d-2)-sphere possibly 0-dimensional (two points) when d = 2 — the argument below
needs only ONE good point. Claim: |alpha_j| sqrt(1 - t_j^2) <= 2L for all j.
PROOF. Sigma_j := H_j cap S^{d-1} is a (d-2)-sphere of radius sqrt(1-t_j^2) > 0 (t_j in [0,1)).
For l != j: H_l cap Sigma_j is a proper closed subset of Sigma_j: indeed H_l superset Sigma_j
would give two distinct hyperplanes containing a (d-2)-sphere; for d >= 3 that sphere spans
H_j (affine hull = H_j), contradiction; for d = 2, Sigma_j = two antipodal-in-H_j points
{P, Q}, and a distinct line H_l contains at most one of them UNLESS H_l = H_j (two points
determine the line) — so at least one of P, Q avoids all other H_l... CAREFUL: different
l could each eat one of the two points? l1 contains P, l2 contains Q: then NO good point in
Sigma_j!! FIX for d = 2: perturbation argument: instead of a point ON other kinks being
fatal, note we only need x* in Sigma_j with x* notin H_l for all l != j. If d = 2 and both
points of Sigma_j are covered by other lines: |Sigma_j| = 2, need finer argument:
  Alternative unified argument (works all d >= 2, AVOIDS the covering issue): choose x* in
  Sigma_j arbitrary with the property that x* notin H_l for all l != j whose hyperplane does
  not contain x*... circular. Real fix: use one-sided derivatives along the GEODESIC and
  allow x* to lie on finitely many OTHER kinks: at such x*, crossing s = 0 the jump of
  phi'(s) equals the SUM of the jumps of all kinks whose hyperplane is crossed at s = 0
  transversally AND passes through x*. That sum mixes coefficients — bad.
  Clean fix for d = 2 (and harmless for all d): PERTURB THE DOMAIN POINT ALONG Sigma_j
  is impossible (finite set); instead note: for d = 2 the sphere case of the MAIN THEOREM
  can be DEDUCED from the ball case: hmm, Lip on S^1 does not control anything off S^1.
  SIMPLEST CORRECT FIX for d = 2: in the merging step, work with kink POINTS on the circle:
  canonical form on S^1: f restricted to S^1 is CPWL in angle theta with kink points =
  union over j of Sigma_j; each Sigma_j = {two points}; a point P on the circle may belong
  to SEVERAL Sigma_j; the angular one-sided-derivative jump at P equals
  sum_{j : P in Sigma_j} alpha_j * (angular kink weight of j at P), and the L-Lipschitz bound
  gives only the SUM. So individual alpha_j are NOT recoverable for d = 2 — BUT the entropy
  argument does not need individual bounds: it needs a re-parameterization of f|_{S^1} with
  bounded description. For d = 2: f|_{S^1} is a CPWL function of angle with at most 2 m0
  kinks and angular-slope everywhere <= L (Lipschitz), PLUS values bounded after clipping:
  the class of such functions has entropy <= C m0 log(C L m0 / eps') DIRECTLY (univariate
  CPWL with <= 2m0 kinks, slopes <= L on the circle of circumference 2 pi: parameterize by
  kink angles + kink slope-jumps with total-variation of derivative <= ... hmm slopes
  bounded by L => derivative is a function of bounded RANGE, kinks 2m0: cover by choosing
  kink locations on an eps-grid + slopes on an eps-grid: entropy m0 log(L/eps): FINE).
  => The theorem for d = 2 (sphere) holds via this direct univariate covering; d = 2 is
  anyway trivial for the conjecture regime (bound sqrt(n/(m log)) <= Lip forced already by
  data separation ~ 1/n on the circle...). DECISION: present sphere case for d >= 3 via
  Lemma 3', and d = 2 via the univariate remark (or simply assume d >= 3 in the sphere
  model and note d = 2 separately). REFEREE: check.
For d >= 3: U := Sigma_j \ union_{l != j} H_l is relatively open and nonempty in Sigma_j
(each H_l cap Sigma_j is a proper closed subsphere/slice of dimension <= d-3, or empty;
a (d-2)-sphere is not a finite union of closed proper slices — Baire or measure). Pick
x* in U. Tangential direction xi := (u_j - t_j x*) / ||u_j - t_j x*||; note <xi, x*> = 0 and
||u_j - t_j x*||^2 = 1 - 2 t_j <u_j,x*> + t_j^2 <x*,x*>?? compute: <u_j, x*> = t_j, ||x*||=1:
||u_j - t_j x*||^2 = 1 - 2 t_j^2 + t_j^2 = 1 - t_j^2. So <u_j, xi> = (1 - t_j^2)/sqrt(1-t_j^2)
= sqrt(1 - t_j^2) > 0.
Geodesic gamma(s) = cos(s) x* + sin(s) xi (unit-speed on S^{d-1}). Then
  h_j(s) := <u_j, gamma(s)> - t_j = t_j (cos s - 1) + sqrt(1-t_j^2) sin s,
h_j(0) = 0, h_j'(0) = sqrt(1-t_j^2) > 0, so the ReLU_j term switches at s = 0 transversally.
For l != j: <u_l, gamma(0)> - t_l != 0, so no switching near s = 0; all other terms are C^1
(actually analytic) in s near 0. phi(s) := f(gamma(s)) is L-Lipschitz in s (unit-speed
geodesic, Euclidean chord <= arc: |gamma(s)-gamma(s')| <= |s - s'|; f L-Lip w.r.t. Euclidean
on S => |phi(s)-phi(s')| <= L|s-s'|. NOTE: Euclidean Lip on the sphere and geodesic Lip
differ by at most a factor pi/2 in the other direction; we use only this direction. GOOD).
One-sided derivatives at 0 differ by alpha_j h_j'(0) = alpha_j sqrt(1-t_j^2); both sides
bounded by L => |alpha_j| sqrt(1-t_j^2) <= 2L. QED

LEMMA 4 (affine part and offset bounds, ball case). In the setting of Lemma 3, suppose
additionally |f(x_bar)| <= B0 for some x_bar in B_{R/2}?? — simplest: 0 in B_R:
 (i) ||v|| <= L(1 + 2 m0)  [at a generic point x0 in int B_R avoiding all H_j:
     grad f(x0) = v + sum_{j active at x0} alpha_j u_j, ||grad f(x0)|| <= L, triangle ineq];
 (ii) |c| <= |f(0)| + sum_j |alpha_j| ReLU(-t_j)?? c = f(0) - sum_j alpha_j ReLU(-t_j) - 0:
     |c| <= |f(0)| + 2 L m0 R.
Sphere case: (i') ||v|| <= L (1 + 2 m0 / min_j sqrt(1-t_j^2))?? — AVOID: don't bound v via
alphas on the sphere. Instead: Lip_S(<v,.>) = ||v||?? PROOF: <= clear; >=: pick x,x' on the
great circle through v-direction... |<v, x - x'>| with x - x' parallel to v: x, x' on sphere
with x - x' = lambda v/||v||: exists (chord in direction v) => Lip_S(<v,.>) = ||v||. Then
||v|| = Lip_S(<v,.>) <= Lip_S(f) + Lip_S(f - <v,.>) — no, triangle needs the other part's
Lip which involves alphas again. ALTERNATIVE for sphere: we do NOT need (i') at all if we
treat the affine part as one more "profile": cover v directly using the CLASS bound:
hmm the covering needs a compact parameter range for v. Get it from function values:
after clipping (Section 4) we cover the CLIPPED functions; still need v-range for the
pre-clip parameterization... CLEANEST: bound v on the sphere via averaging:
v = (d / |S|?) * integral of f(x) x dmu0(x)?? For f = <v,x> + c: E_{mu0}[f(x) x] = v / d
(since E[x x^T] = I/d, E[x] = 0). For the kink terms: E[ReLU(<u,x> - t) x] = some vector
parallel to u with norm <= E|ReLU| <= 1: gives ||v|| <= d (E|f| + sum_j |alpha_j| ...) — has
a d factor and alpha sum: acceptable inside a LOG. With |alpha_j| <= 2L/sqrt(1-t_j^2) and
caps possibly tiny... E[ReLU_j] <= (1 - t_j)*P(cap) — product |alpha_j| E[ReLU_j x] <=
2L sqrt(1-t_j) * 1: <= 2L. So ||v|| <= d(E|f| + 2 L m0) <= d(1 + 2 L m0) after clipping —
wait E|f| of the TRUE f pre-clip... use f's boundedness ON THE SPHERE from fit+Lip:
|f(x)| <= |f(x_1)| + L*diam <= 1 + noise + 2L... f(x_1) close to y_1 only in AGGREGATE MSE
=> (1/n)sum (f(x_i)-y_i)^2 <= 1 => exists i: |f(x_i) - y_i| <= 1 => |f(x_i)| <= 2 =>
sup_S |f| <= 2 + 2L =: B0. THEN ||v|| <= d(B0 + 2 L m0). Log-only cost. OK.
 c on sphere: |c| <= sup|f| + ||v|| + sum_j |alpha_j|(1-t_j) <= B0 + d(B0 + 2Lm0) + 2Lm0.
All these enter ONLY inside logarithms of the entropy bound. [PROVED modulo referee check]

---------------------------------------------------------------------------
## 3. Entropy of the Lipschitz-constrained class

Fix domain D (sphere d >= 3, or ball B_2 for model (G)), width m0 <= m, level L > 0, value
bound B0 = 2 + 2L (justified above for fitting functions; make it part of the class def).

CLASS DEFINITION. G_{m,L} := set of functions on D of the canonical form of Lemma 2
satisfying the conclusions of Lemmas 3/3'/4 (coefficient, v, c bounds as proved).
By Sections 1–2, every f in NN_m with Lip_D(f) <= L and (fit-normalization |f(x_i0)| <= 2
for at least one point of D... make it: sup_D |f| <= B0) has f|_D in G_{m,L}.

LEMMA 5 (metric entropy). For eps' in (0,1):
  log N( G_{m,L}, ||.||_{infty(D)}, eps' ) <= C (m d + d) log( C (2+L)(2+B0) m n?? no n here:
  ... <= C m d log( C m d (2 + L) / eps' ).
PROOF (ball case). Parameters: (alpha_j, u_j, t_j)_{j<=m0}, v, c with |alpha_j| <= 2L,
u_j in S^{d-1}, t_j in [-2,2], ||v|| <= L(1+2m), |c| <= B0 + 4Lm. Perturbation sensitivities
on B_2 (R=2): |Delta f| <= sum_j [ |Delta alpha_j| * 4 + |alpha_j| * 2 ||Delta u_j|| * ??
ReLU difference: |ReLU(<u,x>-t) - ReLU(<u',x>-t')| <= |<u-u',x>| + |t-t'| <= 2||u-u'|| + |t-t'|.
So |Delta f| <= sum_j [4|Delta alpha_j| + 2L(2||Delta u_j|| + |Delta t_j|)] + 2||Delta v|| + |Delta c|.
Grids: |Delta alpha_j| <= eps'/(16m); ||Delta u_j|| <= eps'/(16 L m); |Delta t_j| <= eps'/(8Lm);
||Delta v|| <= eps'/8; |Delta c| <= eps'/4. Counts: alpha: (64Lm/eps')^m; u: net of S^{d-1} at
rho: (1 + 2/rho)^d each => (C L m / eps')^{m d}; t: (C L m /eps')^m; v: ball radius L(1+2m) in
R^d at eps'/8: (C L m / eps')^d; c: C(B0 + Lm)/eps'. Also the DISCRETE choice m0 in {0..m}
and (for general PL psi) nothing else. Total log <= (md + 2m + d + 1) log(C L m (B0+2)/eps')
+ log(m+1) <= C m d log(C m d (2+L)/eps') using B0 = 2 + 2L. Internal-covering fix: replace
each grid net function by a nearest CLASS member (doubles eps'). QED
PROOF (sphere case, d >= 3): same, with the refined (alpha_j, t_j) treatment:
split kinks into bulk (t_j <= 1/2: |alpha_j| <= 4L/sqrt(3) <= 3L: as in the ball case) and
cap kinks (t_j in (1/2,1)): constraint |alpha_j| <= 2L/sqrt(1-t_j^2) <= 2L/sqrt(1-t_j).
 Cap kinks: sup of the neuron over S = |alpha_j| (1 - t_j) <= 2L sqrt(1-t_j). If
 sqrt(1-t_j) <= eps'/(16 L m) =: gamma_min, DROP the neuron (cost <= eps'/(16m) each? cost
 2L*gamma_min^2?? sup <= 2L sqrt(1-t_j) <= 2L gamma_min = eps'/(8m). ok).
 Else parameterize gamma_j := sqrt(1 - t_j) in [gamma_min, 1]: sensitivities:
 d f / d t at fixed alpha: <= |alpha_j| <= 2L/gamma_j; t-grid step eps' gamma_j /(16 L m):
 number of grid points across (1/2,1): integral (16Lm/eps') dt/gamma(t), dt = 2 gamma dgamma
 => integral 2 dgamma * (16Lm/eps') <= 32Lm/eps' — log-size ✓.
 alpha-grid: |Delta alpha| * sup ReLU_j <= |Delta alpha| (1-t_j) = |Delta alpha| gamma^2 <=
 eps'/(16m) => step eps'/(16 m gamma^2), range 4L/gamma: count 64Lm gamma/eps' <= 64Lm/eps' ✓.
 u-net: |alpha| * (cap diameter??) careful: |Delta_u neuron| <= |alpha| |<u-u',x>| over the
 active cap only — crude |alpha| ||u-u'|| * 1?? that gives step eps' gamma/(CLm): count
 (CLm/(eps' gamma))^d <= (CLm/(eps' gamma_min))^d = (C L^2 m^2 /eps'^2)^d — log picks up a
 factor 2: fine ✓.
 v: ||v|| <= d(B0 + 2Lm): count (C d L m (B0)/eps')^d: log <= d log(C d L m/eps') ✓.
Total: log N <= C m d log(C m d (2+L)/eps') again. QED [REFEREE: verify cap bookkeeping]

---------------------------------------------------------------------------
## 4. Probabilistic core (self-contained, c-isoperimetric mu)

DEFINITION (BS). mu is c-isoperimetric if every bounded L'-Lipschitz h: R^d -> R (resp. on
S^{d-1}) satisfies P(|h - E h| >= t) <= 2 exp(- d t^2 / (2 c L'^2)).
FACTS: (S) uniform sphere measure is c-isoperimetric with absolute c (Levy; e.g. c = 2??
check standard constant: P >= t <= 2 e^{-(d-1)t^2/(2L'^2)}?? use c-isoperimetric with c = 4
covering d >= 2: (d-1) >= d/2. cite Ledoux). (G) N(0, I_d/d): h L'-Lip in x is (L'/sqrt d)-Lip
in g ~ N(0,I_d) => P(|h - Eh| >= t) <= 2 e^{-d t^2/(2 L'^2)} (Tsirelson–Ibragimov–Sudakov),
c = 1. [Both PROVED/classical with citations.]

Throughout: F is a FINITE set of functions D -> [-1, 1] each L-Lipschitz on D, extended...
NOTE (G): functions defined on all R^d (our nets are global; clipping keeps them global,
Lip <= L global?? Lip of the canonical form on ALL R^d may exceed Lip_{B_2}: the rigidity
bounds were derived from Lip_{B_2} but then |alpha_j| <= 2L etc. make the GLOBAL Lipschitz
of the canonical representative <= ||v|| + sum |alpha_j| <= L(1+2m) + 2Lm <= 5Lm — a
factor m: the isoperimetry exponent would lose m^2!! FIX: apply concentration NOT to the
canonical net but to the 1-Lipschitz-CLIPPED-AND-LOCALIZED modification:
   f_tilde := clip_{[-1,1]}( f ) composed with radial retraction pi: R^d -> B_2,
   pi(x) = x min(1, 2/||x||): pi is 1-Lipschitz (retraction onto convex ball), so
   f_tilde := clip(f(pi(x))) is L-Lipschitz on ALL R^d, equals clip(f) on B_2, values [-1,1].
 In model (G), P(exists i: x_i notin B_2) <= n e^{-c d} (chi-square tail: P(||g||^2 >= 4d)
 <= e^{-d/2}?? use standard: P(||g|| >= 2 sqrt d) <= e^{-d/2}); on the complement event,
 f_tilde(x_i) = clip(f)(x_i) for all i. Fit transfers: |y| <= 1 => clipping only reduces
 (f(x_i) - y_i)^2. So WLOG the finite class consists of such GLOBAL L-Lip [-1,1]-valued
 f_tilde. Sphere: just clip; domain is the sphere itself. GOOD — this closes the gap.]

LEMMA 6 (noise decomposition; BS Lemma 2.1, reproved). g(x) := E[y | x] (|g| <= 1),
z_i := y_i - g(x_i) (|z_i| <= 2, E[z_i | x_i] = 0, E z_i^2 = sigma_i^2 with E sigma^2 = sigma^2).
For any finite F as above and eps in (0, sigma^2]:
 P( exists f in F: (1/n) sum (f(x_i) - y_i)^2 <= sigma^2 - eps )
   <= 2 exp(- n eps^2 / 1152) + P( exists f in F: (1/n) sum z_i f(x_i) >= eps/4 ).
PROOF. Events E1 := {(1/n) sum z_i^2 >= sigma^2 - eps/6}, E2 := {(1/n) sum z_i g(x_i) >= -eps/6}.
(1/n)sum z_i^2: iid, mean sigma^2, range [0,4]: Hoeffding: P(not E1) <= exp(-2n(eps/6)^2/16)
= exp(-n eps^2/288). (1/n)sum z_i g(x_i): iid mean 0 (tower), range [-2,2]: P(not E2) <=
exp(-2n(eps/6)^2/16) = exp(-n eps^2/288). [Constants: keep 2exp(-n eps^2/288) total bound
2 exp(-n eps^2 / 288) — fix numbers at write-up.]
On E1 cap E2, if (1/n)||Y - F_vec||^2 <= sigma^2 - eps with Y = G + Z:
 sigma^2 - eps >= (1/n)||G - F_vec||^2 + (2/n)<Z, G - F_vec> + (1/n)||Z||^2
             >= 0 + (2/n)<Z,G> - (2/n)<Z,F_vec> + sigma^2 - eps/6
             >= sigma^2 - eps/6 - eps/3 - (2/n)<Z, F_vec>
 => (1/n) <Z, F_vec> >= (eps - eps/2)/2 = eps/4. QED

LEMMA 7 (single-function concentration). f: R^d -> [-1,1], L-Lipschitz (global in (G);
on S in (S)). Then W_i := z_i (f(x_i) - E f) are iid, mean zero, and
  P( (1/n) sum W_i >= eps/8 ) <= 2 exp( - n eps^2 d / (C c (min(L, sqrt d))^2 ) )
  — unify: <= 2 exp( - c2 n eps^2 min( 1, d / (c L^2) ) ).
PROOF. Mean zero: E[W_i] = E[ E[z_i|x_i] (f(x_i)-Ef) ] = 0. Tail of W_i:
|W_i| <= 2|f(x_i) - Ef| and |f - Ef| <= 2 (values in [-1,1]) so |W| <= 4; also isoperimetry:
P(|W_i| >= t) <= P(|f - Ef| >= t/2) <= 2 exp(-d t^2/(8 c L^2)). So ||W||_{psi_2} <=
C' min(1, sqrt(c/d) L)^{-1}?? — careful: psi2 norm <= C' * min( 4 / sqrt(log 2)?? , ... ):
||W||_psi2 <= C' min( 1, sqrt(c) L / sqrt(d) ) * const + bounded-part: both bounds give
subgaussian with parameter K := C'' min(1, sqrt(c) L/sqrt(d)). General Hoeffding
(Vershynin Thm 2.6.2): P(sum W_i >= s) <= exp(- c3 s^2 / (n K^2)); s = n eps/8. QED

LEMMA 8 (mean term). P( exists f in F: (Ef)(1/n) sum z_i >= eps/8 ) <=
P( |(1/n) sum z_i| >= eps/8 ) <= 2 exp(- n eps^2 / 512) (Hoeffding, z in [-2,2], mean 0),
uniformly in f since |Ef| <= 1. QED

THEOREM 9 (finite-class law). F finite, values [-1,1], L-Lip. eps in (0, sigma^2]:
 P( exists f in F: fit <= sigma^2 - eps )
   <= 4 exp(- n eps^2 / 1152) + |F| 2 exp(- c2 n eps^2 min(1, d/(c L^2)))
   [combining L6, split z_i f = z_i(f - Ef) + z_i Ef with thresholds eps/8 + eps/8 = eps/4,
    L7 union over F, L8.]

---------------------------------------------------------------------------
## 5. Assembly

THEOREM 10 (main). Setting of Section 0, model (S) with d >= 3 or model (G) with
d >= C log(4n/delta). Let L > 0 and define the good event Omega_L := {no f in NN_m with
sup-normalization... } — assemble:
 Given L, let N_L := internal eps/32-net of clip(G_{(K-1)m+1, L}) (Lemma 5 with
 eps' = eps/32; note clipping is 1-Lipschitz on values so the same net works).
 On the event {all x_i in D-effective} (prob >= 1 - n e^{-d/2} in (G), = 1 in (S)):
 if some f in NN_m has Lip_D(f) <= L, sup_D|f| <= B0 handled, and fit <= sigma^2 - eps,
 then its clipped-localized f_tilde has fit <= sigma^2 - eps, and the net neighbor f_hat
 (||f_hat - f_tilde||_{infty(D)} <= eps/16) has:
   (1/n) sum (f_hat(x_i) - y_i)^2 <= sigma^2 - eps + 2 * (eps/16) * (1/n) sum |f_tilde - y_i|
     <= sigma^2 - eps + (eps/8) * 3?? |f_hat - y| <= |f_tilde - y| + eps/16, squares:
     (a+h)^2 <= a^2 + 2h a + h^2, a <= 2, h = eps/16: fit(f_hat) <= fit(f_tilde) +
     2*(eps/16)*2 + eps^2/256 <= sigma^2 - eps + eps/4 + eps/16 <= sigma^2 - eps/2.
 Apply Theorem 9 to F = N_L at level eps/2:
  P(bad) <= n e^{-d/2} + 4 exp(-n eps^2/4608) + exp( C m d log(C m d (2+L)/eps)
            - c2 n eps^2 min(1, d/(c L^2))/4 ).
 CHOOSE L = L*(m, n, d, eps) := the largest L <= sqrt(d/c) such that
   C m d log(C m d (2+L)/eps) <= c2 n eps^2 d / (8 c L^2):
 explicit sufficient choice: L*^2 := c2 n eps^2 / (8 c C m log(C m n d / eps)) capped at d/c,
 [check: with L <= sqrt(nd...)/... <= poly(n,d,1/eps) => log(2+L) <= C log(nmd/eps) ✓]
 then the third term <= exp(- c2 n eps^2 /8 * min(1, ...)) <= exp(- c4 n eps^2) hmm:
 in the unsaturated regime the third term <= exp(- (c2/8) n eps^2 d/(cL*^2) ) with
 n eps^2 d/L*^2 = 8 c C m d log(.)/c2 * ... — just: third term <= exp(- C m d log(...)) <=
 exp(- m d) — anyway all three terms <= delta/2 provided n >= C0 eps^{-2} log(8/delta) and
 (G) d >= 2 log(4n/delta). CONCLUSION: w.p. >= 1 - delta every fitting f has
 Lip_D(f) > L* = c0 eps sqrt( n / (m'' log(C0 m'' n d/eps)) ), m'' := (K-1)m + 1, capped:
 min( that, sqrt(d/c) ). NOTE THE CAP: for m'' <= c n eps^2/(d log), the bound saturates at
 sqrt(d/c) — for the BLN regime the conjectured value sqrt(n/m) <= sqrt(d) iff m >= n/d,
 i.e. p = md >= n: EXACTLY the overparameterized regime where the conjecture was posed
 (interpolation requires p >= n anyway for exact fit — cite BLN's remark). For m < n/d
 state the saturated bound Lip >= c0 eps sqrt(d) — hmm the conjecture claims sqrt(n/m) >
 sqrt(d) there. Can we do better in the underparameterized regime? The saturation at
 sqrt(d) comes from |f| <= 1 clipping (fluctuations can't exceed O(1)); values of f near
 data are in [-2,2] necessarily-ish; the conjecture for m < n/d claims Lip >~ sqrt(n/m) >>
 sqrt(d): TRUE?? For exact interpolation: yes plausibly (a width-m net exactly hitting n
 pure-noise values...) — but our covering argument genuinely stalls at sqrt(d)
 (isoperimetric fluctuation floor). RESOLUTION: BLN Conjecture 1 says "fitting the data"
 = EXACT fit; in the regime p = md < n, exact fit of n iid CONTINUOUS?? labels are +-1
 discrete — exact fit is not dimension-counting-impossible... Hmm. HONEST SCOPE: our
 theorem proves the conjectured bound sqrt(n/m) for m >= n/d (p >= n, the overparameterized
 regime, which is the regime of interest of the conjecture: BLN pose it as "overparam is
 necessary for robustness"; for m < n/d we still give Lip >= c eps sqrt(d), new and
 nontrivial but weaker than conjectured). CHECK what BLN Conjecture 1 exactly quantifies:
 if it asserts for ALL k, then we resolve it in the regime k >= n/d and give sqrt(d)
 otherwise: the paper must state this honestly. Hmm — BS Theorem also has this cap
 (their d >= C1 c L^2 sigma^2/eps^2 condition = exactly L <= sqrt(d) eps/(sigma sqrt(C1 c))).
 So the BS resolution-under-poly-weights has the SAME cap: "full conjecture for the
 two-layer case" as they mean it = their-theorem-for-two-layer-without-weight-bounds =
 EXACTLY what we prove. State this comparison explicitly in the paper. GOOD.

---------------------------------------------------------------------------
## 6. Sharpness / scope remarks (to include)
 (a) Depth: BS Appendix A — with unbounded weights the law FAILS for three-layer networks;
     cite (and sketch their construction in one paragraph). Depth two is critical.
 (b) Activation: the rigidity is a kink phenomenon. For smooth activations the canonical-
     coefficient bound FAILS: explicit family a[sigma(<w,x>+b) - sigma(<w,x>+b')] with
     a(b'-b) = 1: function converges to the ridge sigma'(<w,x>+b) with tiny sup norm...
     gives width-2 sub-families whose Lip-1 slice is parameterized by unbounded (a):
     BUT does it break the ENTROPY, or just this proof? For FIXED analytic sigma the class
     may still be small. Honest statement: our method is specific to piecewise-linear psi;
     the conjecture for general Lipschitz psi remains open. Optionally: a PROPOSITION that
     for a suitably constructed (pathological, still 1-Lipschitz) activation psi*, the
     width-1 class with unbounded weights has infinite Lip-constrained entropy — showing
     entropy alone cannot decide the general conjecture. [Construct psi* = primitive of a
     +-1 pattern encoding all finite patterns; the class {psi*(s<u,x> + b)} realizes 2^M
     eps-separated functions with Lip <= 1?? CHECK: Lip of psi*(s t + b) in t is s — to keep
     Lip <= L must have s <= L: the patterns live at scale 1/s >= 1/L: on the ball of radius
     2, a Lip-L 1-D profile at resolution eps has at most (C L/eps)^{C L/eps}?? finite —
     entropy <= (L/eps) log(L/eps) FINITE. So width-1 entropy is FINITE after all (profile
     is a 1-D L-Lip function!) — the blow-up needs CANCELLATION across neurons: width-2
     same-direction pairs: g(t) = a[psi(st+b) - psi(st+b')]: as a FUNCTION it is a 1-D
     profile with Lip <= L: ALL of these are covered by "1-D L-Lip profiles": entropy of
     {L-Lip profiles on [-2,2]}: (C L/eps)^{CL/eps} — log = (L/eps) log(L/eps) NOT m d log:
     for ONE direction the profile entropy is L/eps — compare needed budget n eps^2 d/L^2
     per... the union: class = {sum of m ridges with arbitrary L-Lip profiles}?? For
     GENERAL psi the reachable per-direction profiles are {a psi(s t + b)}-combinations —
     a SUBSET of all L-Lip profiles. Entropy of all-L-Lip-profile ridge sums: m directions
     (md log) + m profiles (m L/eps log(L/eps)): total <= C(md + mL/eps)log(.): plug into
     Thm 9: need <= c n eps^2 d/L^2: extra term m L eps^{-1} log <= c n eps^2 d / L^2 <=>
     L^3 <= c n eps^3 d/(m log): L <= (n d eps^3/(m log))^{1/3}: a WEAKER but NONTRIVIAL
     bound for ARBITRARY activations?! sqrt(n/m) vs (nd/m)^{1/3}: for m ~ n, d ~ 1?? sphere
     d large: (nd/m)^{1/3} vs (n/m)^{1/2}: ratio: which regime... at m = n: (d)^{1/3} vs 1:
     the cube-root bound is BETTER?! no wait conjecture at m=n gives O(1); cube-root gives
     d^{1/3} >> — CONTRADICTS the achievability?? Achievable Lip at m = n is O(1)*(sqrt d??)
     hmm BS Remark 1.1: p = n(d+1) params achieve Lip O(1)... p = md: m = n: p = nd:
     achieve O(1): but cube-root bound says Lip >= (nd/n)^{1/3} = d^{1/3} > O(1)?!
     CONTRADICTION => my profile-entropy sketch is WRONG somewhere: the all-profile class
     {sum_m ridges, L-Lip profiles} with L = O(1)... the RBF construction is NOT a sum of
     m ridges — it's a deep/RBF net — no contradiction with TWO-LAYER achievability:
     is sqrt(n/m) ACHIEVABLE by two-layer?? BLN think yes-ish (their Fig 2?). If yes at
     m = n with Lip O(1): a two-layer ReLU net, width n, Lip O(1), fitting noise: its
     ridge profiles are L-Lip: consistent with profile-entropy n * (L/eps) = n:
     budget n eps^2 d / L^2 = n d: n <= nd ✓ NO contradiction: I mis-derived: with L = O(1),
     m = n: extra entropy term m L/eps = C n <= c n eps^2 d/L^2 = c n d ✓ HOLDS. The
     cube-root bound: L^3 <= c n eps^3 d/(m log) at m = n: L <= (eps^3 d/log)^{1/3} = c d^{1/3}:
     the bound says Lip >= min over... NO WAIT direction: the argument RULES OUT L only
     while entropy(L) <= budget(L): rules out all L <= L* with L* = that root: bound
     Lip > L* requires... entropy INCREASES in L, budget DECREASES: rule out L iff
     entropy(L) <= budget(L) i.e. small L: we rule out ALL L <= L* and conclude Lip > L*:
     at m = n: L* ~ d^{1/3}: says Lip > c d^{1/3} for ANY activation?? but achievability
     says exists two-layer (ReLU) width-n net with Lip O(1) fitting!! CONTRADICTION unless
     the ReLU achievability at m = n, Lip O(1) is FALSE... hmm hmm. Which is wrong?
     Check the union-bound logic: to rule out L, need EVERY f in the L-slice to fail:
     P(exists f in slice fitting) <= net-size * per-function-prob: need
     log Nentropy(L) <= c n eps^2 min(1, d/L^2): at L = O(1) <= sqrt d: need
     C(md + m/eps) log <= c n eps^2 d?? with m = n: C n(d + 1/eps) log <= c n eps^2 d ⟺
     C log(.)/eps <= c eps^2 d?? — FAILS for d fixed large?? no: holds iff d >= C'/eps^3 log:
     fine for large d. SO at m = n we CANNOT rule out L = O(1) — wait we need entropy <=
     budget: n d log <= c n eps^2 d ⟺ log(.) <= c eps^2?? FAILS! log factor kills it:
     C m d log(Lmd/eps) <= c n eps^2 d at m = n: C n d log <= c n eps^2 d ⟺ C log <= c eps^2:
     FALSE. => at m = n even the ReLU argument rules out NOTHING (L* ~ sqrt(n/(m log)) =
     sqrt(1/log) < 1: sub-constant: vacuous) ✓✓ CONSISTENT with achievability. And the
     cube-root claim similarly evaporates at m ~ n. My scare was wrong: L* formulas already
     encode it. So: BONUS RESULT possible for ARBITRARY Lipschitz activations:
     Lip >= c min( (n d eps^3 / (m log))^{1/3}, eps sqrt(n/(m log)), eps sqrt(d) )?? via
     covering profiles directly!! Wait but profiles of a_k psi(s_k t + b_k) with |a_k| s_k
     unbounded: the FUNCTION-level profile g_k(t) := a_k psi(s_k t + b_k): is each g_k
     L-Lip?? NO — cancellation across DIFFERENT directions (my old obstruction): the
     per-direction profile of f is sum of same-direction neurons only; profiles of
     different directions cancel only via... ridge uniqueness says up to POLYNOMIALS —
     for non-poly parts profiles are determined; polynomial parts can be huge with
     cancellation. Pinkus: sum_l g_l(<u_l, x>) == 0 on R^d, g_l locally integrable?? =>
     g_l polynomials of degree <= m-1?? (need continuity assumptions; classical result:
     Diaconis–Shahshahani / Logan–Shepp / Pinkus Ch 5?). If f is Lip-L and = sum g_l ridges:
     hmm the profiles are determined mod polys of degree <= m: the poly parts:
     coefficient sizes NOT controlled by L (cancellations!): profile g_l = h_l + P_l,
     P_l poly deg <= m: the P_l's can be astronomically large yet sum of ridges of P_l's
     cancels... e.g. d >= 2: <u1,x>^2 - <u2,x>^2 - ... Legendre stuff: sums of squares
     identities: M[<u1,x>^2 + <u2,x>^2 - <u3,x>^2 - <u4,x>^2] == 0 identically for suitable
     frames!! ((u1,u2) and (u3,u4) two orthonormal bases of the same 2-plane: sum sq =
     ||P x||^2 both): so P-parts unbounded with ZERO function contribution => the MAP from
     (profiles) to functions has kernel: for COVERING PURPOSES kernel is harmless (cover
     the FUNCTIONS, choose canonical representatives with minimal-norm profiles!): the
     class of FUNCTIONS = {sum ridges, Lip <= L}: canonical representative: profiles :=
     h_l + Q_l with Q_l the MINIMAL polynomial completion... is there always a
     representative with ALL profiles C(m,d)L-Lipschitz?? Quantitative ridge rigidity:
     OPEN-ish, condition-number of the direction set enters (clustered directions =>
     ill-conditioned). This is the genuinely hard part for general psi — CONFIRM scope
     decision: PL only + honest discussion. [Optional Prop for the paper: the width-2
     smooth-activation cancellation shows the CANONICAL-COEFFICIENT bound (Lemma 3) has no
     analogue for any activation with a point of twice-differentiability with sigma'' != 0...
     statement: for sigma in C^2 nonlinear, the map (a, b) -> a[sigma(t + b) - sigma(t)] - ...
     produces, in the Lip-1 ball of the width-2 class, functions requiring unbounded
     parameters: i.e. PARAMETER-boundedness fails, so BS's route (and ours) needs the kink.
     That's a clean true statement: prove by exhibiting f_a = a[sigma(<w,x> + 1/a) -
     sigma(<w,x>)]: as a -> infty, f_a -> sigma'(<w,x>) uniformly on compacts, each f_a has
     Lip <= 2 sup|sigma'| =: L0, and NO representation with bounded parameters converges to
     sigma' since sigma' notin closure of bounded-parameter width-2 class?? sigma' IS in the
     closure of width-2... e.g. sigma = tanh: sigma' = sech^2 — is sech^2 a finite two-layer
     tanh net? generally NO (different function). And bounded-parameter classes are closed
     (compactness) => sigma' has NO exact width-2 representation but is a LIMIT: so the
     Lip-L0 slice of width-2 class is NOT compact in sup norm => not totally bounded =>
     INFINITE entropy at some resolution?? Hmm: non-closedness != infinite entropy at fixed
     eps. The eps-entropy of {f_a} alone is finite (1-param family!). The honest cheap
     statement: parameter norms are NOT controlled by function norms for smooth sigma
     (unlike Lemma 3) — demonstrate with f_a; leave entropy question open. OK.]
 (c) Log factor: our bound has a single log; the conjecture is stated without one; note BS
     is also lossy (Omega-tilde) and leave sharpening open.
 (d) Optimality in m: matching upper-bound side: cite BS Remark 1.1 (p ~ n(d+1) at O(1)) —
     note their construction is not two-layer; two-layer achievability of sqrt(n/m) is
     discussed in BLN (numerics; cite as open side question).

---------------------------------------------------------------------------
## 6.5 CORRECTIONS MADE IN THE PAPER (main.tex is now the source of truth)
- Theorem 9 exponent: max(1, d/(kappa^2 L^2)) — the psi_2 parameter is C min(1, kappa L/sqrt d),
  so the exponent IMPROVES for small L. (The "min" written in Sec 4 above was a typo.)
- Net members must themselves be L-Lipschitz for Lemma 7: fixed by taking a maximal
  eps/32-separated subset S of the TRUE class A_{m,L} = {network restrictions with Lip<=L,
  sup<=B0} (internal net by maximality), with |S| <= N(G_{m,L}, eps/64) by packing-covering
  duality and A subset G. Grid functions serve only as external covering centers of G.
- Assembly delta-bookkeeping: delta/8 (localization, model G) + delta/2 (noise events) +
  delta/4 (union term); conditions n >= C0 eps^-2 log(8/delta), d >= 2 log(8n/delta) (G only).
- B0 = 2 + 4L (diam <= 4).
- Sphere v-bound via E[f(x)x] = v/d + sum alpha_j lambda(t_j) u_j, lambda(t) <= 1-t, and
  |alpha_j| lambda(t_j) <= 2L; ||v|| <= d(B0 + 2Lm0).
- All-m uniformity: delta_m = delta/(2m^2), n >= C0 eps^-2 log(8n/delta).
- Numerics: rigidity 27/27 PASS (incl. 1e6 same-hyperplane cancellation plants merged, and
  near-parallel 1e4 plants saturating |alpha|/2L = 0.50); sphere cap factor sqrt(1-t^2)
  verified EXACT (ratio 1.000 for t in {0,.5,.9,.99,.999}).

---------------------------------------------------------------------------
## 7. TODO / verification ledger
 - [x] Referee pass 1 (adversarial subagent) COMPLETE: "mathematical core is sound... no
       fatal error"; every attack on rigidity + cap entropy failed; independently verified
       numerically to 2e-12. Its 8 required fixes reconciled against the PAPER:
       (1) statement/cap alignment — paper's two-case budget proves the UNCAPPED L* (the
           notes' cap was an artifact of the notes' weaker assembly); verified again by hand;
       (2) min->max in Lemma 7/Thm 9 — already correct in paper;
       (3) class must include Lip<=L + internal net — already correct in paper (A-class +
           packing duality);
       (4) d=2: notes' CPWL-in-angle fallback was FALSE (piecewise trigonometric); WORSE,
           referee CONSTRUCTED an even-cycle counterexample proving rigidity genuinely fails
           at d=2 (all |alpha|sqrt(1-t^2)=1000, jumps cancel, Lip~200, ratio 5). Paper now
           restricts (S) to d>=3 ON PRINCIPLE and records the counterexample
           (numerics/check_d2_rigidity_fails.py REPRODUCED: ratio 5.00, jumps ~1e-3);
       (5) constants — paper's B0=2+4L, grid budgets sum to eps'/2: checked;
       (6) continuity of psi — stated in paper;
       (7) Levy/TIS citations in psi_2-mean form (Vershynin 5.1.4/5.2.2) — fine;
       (8) garbled notes prose — notes superseded by paper (Sec 6.5).
 - [x] Numerics: rigidity 27/27; sphere cap factor exact (1.000 across t); d=2 failure
       reproduced; empirical-law training table IN FLIGHT.
 - [ ] Referee pass 2 on the LaTeX (in flight; first attempt died on session limit, relaunched).
 - [x] BUDGET INEQUALITY re-verified by hand (the referee-flagged "does it need a sqrt(d) cap?"
       question). Paper proves the UNCAPPED bound. Both cases close with one c0 <= c2/(8 kappa^2 C'):
       Case A (L* <= sqrt(d)/kappa): d/(kappa^2 L*^2) branch, RHS = (c2/(8 kappa^2 c0^2)) m d log
         >= E = C' m d log.
       Case B (L* > sqrt(d)/kappa): "1" branch, RHS = (c2/8) n eps^2; the case condition
         m log < c0^2 kappa^2 eps^2 n/d MULTIPLIES BY d to give m d log < c0^2 kappa^2 eps^2 n,
         so E = C' m d log < C' c0^2 kappa^2 eps^2 n <= (c2/8) n eps^2. The d in E is absorbed
         by the d in the Case-B threshold => no cap. (The notes' earlier cap was an artifact of
         a weaker single-case assembly; the paper's two-case argument is what removes it.)
       Also L* <= c0 eps sqrt(n) <= eps sqrt(n) => 2+L* <= 3 sqrt(n) => log(2+L*) collapses into
       log(C0 m n d/eps). One application at L=L* rules out ALL fitting f with Lip<=L*
       (rigidity bounds monotone in L), giving Lip>L* for every fitting f.
 - [x] Exact-fit corollary bookkeeping (eps = 1/2, sigma^2 = 1).
 - [x] d >= 3 sphere; d = 2 honest remark w/ counterexample.
 - [x] Skip connection: included, noted as enlargement of BLN class.
