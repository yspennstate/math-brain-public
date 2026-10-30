SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet03, slot B14, 2026-09-23T00:36:43Z.
attacking: exact affine-core/ambient localization and continuity transfer without a uniform modulus; rule out Arzela-style continuity localization on phase-aligned finite-fragment laws.

# fleet03/B14 — exact affine-core localization, continuity mixing, and a non-equicontinuity obstruction

Programme: QFORM-DENSITY-3EIG-20260922
Run: 20260923T003643Z-fleet03-B14-QFORM-r22
Status: SUPPORTING TARGET-LEVEL THEOREMS PROVED; ONE LOCALIZATION/REGULARITY MECHANISM REFUTED; FULL QFORM OPEN
Execution: WITHOUT_VERIFIED_BRAIN

## 1. Exact target and source boundary

The target remains: for every n, independent real X_i with probability densities 0<=f_i<=1, and every real symmetric A with at least three eigenvalues of modulus at least one, prove that Q=X^TAX has a density with universal essential-supremum bound, or give a valid counterexample. Continuity is a separate desired conclusion.


The designated partner input is fleet04/B14's affine-family localization compiler, with canonical proof

yspennstate/math-open-problems@19d9434e07142e6b9fe19b4a88bbd46ccec8eeee
proofnet24/QFORM-density/fleet-2026-09-22/fleet04/B14/20260923T001323Z-fleet04-B14-affine-mixture-compiler-r5/REPORT.md
blob 3af36c47726d1aabb2a9cb0281818d9d3bb3297c.

The n=3 theorem used below is Theorem 2.1 / Corollary 2.2 in

yspennstate/math-open-problems@29e682234ef18500588293f4e947e79ca768a251
proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/GEOMETRIC_ROUTE_REPORT.md.

It proves that every 3x3 symmetric B with min_j |lambda_j(B)|>=1, arbitrary affine terms, and independent cap-one coordinates has density <=20; after scaling, min_j |lambda_j(B)|>=gamma gives <=20/gamma. This is a proved supporting theorem, not the full n-dimensional conjecture.

## 2. Exact affine-core / ambient concentration equality

Fix a real symmetric m x m matrix B. Let D_m be the class of product probability laws on R^m whose one-dimensional marginal densities are at most one. Let F_m be the subclass whose marginal densities are indicators 1_E of compact finite unions of intervals E with |E|=1.

For an interval I with |I|>0 define the affine-core constant

C_aff(B) := sup_{mu in D_m} sup_{ell in R^m,c in R} sup_I P_mu{U^TBU+ell^TU+c in I}/|I|.

Define C_ff(B) by the same formula with mu restricted to F_m.

Define C_amb(B) as follows. Take any k>=0, any symmetric block matrix

A = [ B  C ; C^T  D ],

any affine term a^T U+b^T V+c, any independent product law for (U,V) with every marginal density at most one, and any interval I. Then C_amb(B) is the supremum of

P{(U,V)^T A (U,V)+a^TU+b^TV+c in I}/|I|

over all such choices.

### Theorem 2.1 (exact ambient localization)

For every symmetric B, allowing +infinity,

C_amb(B) = C_aff(B) = C_ff(B).                                      (2.1)

In particular, fixing a physical principal block B completely separates the localization problem from all outside translations, tails, fragments, dimensions and couplings: the exact best interval constant is the affine-core constant, and fleet04/B14 reduces that constant with zero loss to compact finite-fragment indicator products.

### Proof

First, C_aff(B)<=C_amb(B) by taking k=0.

For the converse, condition on V=v. Write

F(U,v)=U^TBU + ell(v)^T U + r(v),
ell(v)=a+2Cv,
r(v)=v^TDv+b^Tv+c.

The conditional law of U is unchanged, because U and V consist of disjoint original independent coordinates. Hence, for every v,

P{F(U,v) in I | V=v} <= C_aff(B)|I|.

Integrating in v gives the identical ambient inequality, so C_amb(B)<=C_aff(B). This argument remains valid when B is singular. In that case a kernel component of ell(v) is retained inside the affine-core supremum rather than being silently removed by completing the square.

Next C_ff(B)<=C_aff(B) is immediate. Conversely, fleet04/B14 proves that every cap-one product law on the core is an L1 limit of finite convex mixtures of F_m laws, and that any estimate uniform in the affine parameters ell,c passes through those mixtures and the total-variation limit with exactly the same constant. Thus every C>C_ff(B) is valid for all D_m laws, so C_aff(B)<=C_ff(B). Let C decrease to C_ff(B). This proves (2.1). QED.

### Concrete target-level application of the partner theorem

Let B be a physical 3x3 principal block with

gamma := min_j |lambda_j(B)| > 0.

The proved n=3 theorem, applied to B/gamma and to the correspondingly rescaled affine terms, gives

C_aff(B) <= 20/gamma.

Combining with (2.1), for every ambient dimension, arbitrary outside block D, arbitrary cross coupling C, arbitrary affine terms, and arbitrary independent cap-one laws,

P{Q in I} <= (20/gamma)|I|,

hence

||p_Q||_infinity <= 20/gamma.                                   (2.2)

Equation (2.2) is the actual inequality to which the completed fleet04/B14 localization result is applied. There is no support-radius, tail, translation, fragment-count, fragment-separation, outside-dimension or moment loss. The unresolved global structural issue is unchanged: s_3(A)>=1 need not furnish a physical 3x3 principal block with gamma bounded below universally.

## 3. Continuity mixes through original-coordinate conditioning with no common modulus

The previous localization work correctly kept continuity separate, because total-variation approximation of laws does not by itself preserve continuity of densities. There is nevertheless a clean positive transfer principle at the physical-core level.

### Theorem 3.1 (continuity-by-conditioning compiler)

Fix B and C<infinity. Assume that for every mu in D_m and every affine pair (ell,c), the random variable

U^TBU+ell^TU+c

has a continuous density p_{mu,ell,c}, and

sup_t p_{mu,ell,c}(t) <= C                                      (3.1)

uniformly over mu,ell,c.

Then every ambient quadratic form having B as that original-coordinate principal block, with arbitrary outside dimension/couplings and arbitrary cap-one product laws, has a continuous density p satisfying ||p||_infinity<=C.

### Proof

Condition on V=v as in Section 2. Let p_v denote the continuous conditional density supplied by the assumption. There is no need to assume a modulus of continuity uniform in v.

For measurability one may canonically recover p_v pointwise from the conditional law:

p_v(t) = lim_{q->infinity} (q/2) P{|F(U,v)-t|<1/q | V=v}.       (3.2)

Because p_v is continuous, the symmetric local averages converge at every t. For each finite q the right side before the limit is jointly measurable in (v,t), hence (v,t)->p_v(t) is measurable.

Define

p(t)=E[p_V(t)].

Tonelli/Fubini and conditional disintegration show that p is a density of F(U,V), while 0<=p<=C. If t_n->t, then p_v(t_n)->p_v(t) for every v. The uniform domination |p_v(t_n)|<=C allows dominated convergence, so p(t_n)->p(t). Thus p is continuous and has the same constant C. QED.

This theorem identifies a valid route to the owner's continuity conclusion: prove affine-uniform continuous densities on one physical core, then average. It does NOT say that continuity can be transferred from finite-fragment approximants to an arbitrary rough law by a compactness argument. The next theorem shows why a uniform-modulus version of that idea is impossible.

## 4. No universal output-density translation modulus, already for A=I_3

### Theorem 4.1 (`QFORM-NO-UNIFORM-OUTPUT-MODULUS-v1`)

There is no function omega(h)->0 as h->0 such that every target-valid output density p obeys either

||p(.+h)-p||_1 <= omega(|h|)

or

||p(.+h)-p||_infinity <= omega(|h|).

This remains false after restricting to the solved diagonal matrix A=I_3, iid marginal densities that are indicators of compact finite unions of intervals contained in [1,10], and output densities that are individually continuous.

### Construction

Fix delta=pi/3. For s>0 define

G_s={x in [1,10] : dist(s x^2,2pi Z)<=delta}.

This is a finite union of intervals. We first record that

|G_s| -> 3 as s->infinity.                                     (4.1)

Indeed, with y=x^2 and w(y)=1/(2sqrt(y)),

|G_s|=int_1^100 w(y) H(sy) dy,

where H is 2pi-periodic and equals one on the arc {dist(theta,2pi Z)<=pi/3}. Its period mean is 1/3. Partition [1,100] into periods of length 2pi/s. On every complete period, replacing w by its value at the left endpoint incurs at most (2pi/s)^2 sup|w'| times an absolute constant; summing O(s) periods gives O(1/s), and the two partial boundary periods also contribute O(1/s). Hence the integral tends to

(1/3) int_1^100 dy/(2sqrt(y))=(1/3)(10-1)=3.

Therefore, for all sufficiently large s, |G_s|>1. Choose a finite-union set E_s subset G_s with |E_s|=1 (take components successively and, if necessary, truncate the last component), and let X have density f_s=1_{E_s}.

Since cos(sx^2)>=cos(delta)=1/2 on E_s,

Re E exp(i s X^2) >= 1/2.                                    (4.2)

Let X_1,X_2,X_3 be iid copies and set

Q_s=X_1^2+X_2^2+X_3^2.

Then, with phi_s the characteristic function of Q_s,

|phi_s(s)| = |E exp(i s X^2)|^3 >= 1/8.                       (4.3)

Each Y=X^2 has density

h_s(y)=1_{E_s}(sqrt(y))/(2sqrt(y)),  1<=y<=100,

so h_s is an L1 probability density with ||h_s||_infinity<=1/2. Consequently

p_s=h_s*h_s*h_s

is a bounded continuous density, supported in [3,300]. For example h_s*h_s is continuous by the standard L1-Linfinity convolution continuity argument (approximate the L1 factor by continuous compact functions), and convolution once more with h_s preserves continuity.

Now put a_s=pi/s. Then a_s->0, while the Fourier transform of the translated difference satisfies, at frequency s,

|widehat{p_s(.-a_s)-p_s}(s)|
 = |exp(i s a_s)-1| |phi_s(s)|
 = 2|phi_s(s)| >= 1/4.

Since the Fourier transform is bounded by the L1 norm,

||p_s(.-a_s)-p_s||_1 >= 1/4.                                 (4.4)

For all sufficiently large s, a_s<1 and the difference in (4.4) is supported in an interval of length at most 298. Hence

||p_s(.-a_s)-p_s||_infinity >= 1/(4*298)=1/1192.              (4.5)

Equations (4.4)-(4.5), with a_s->0, prove the theorem. QED.

### Scope of the obstruction

This is not a counterexample to QFORM: the p_s are bounded continuous densities in a solved diagonal case. It also does not contradict continuity of any fixed p_s. It refutes only a uniform equicontinuity/translation-modulus interface over the whole target class, including over compact finite-fragment extreme laws. Therefore an Arzela-Ascoli style argument that tries to get the rough-law continuity conclusion from a universal output modulus of finite-fragment approximants cannot work under the bare hypotheses.

The construction is consistent with the earlier B14 result that positive polynomial weighted Fourier moments are not uniformly bounded. The present statement is strictly more direct at the output-density level: even continuity itself carries no uniform modulus across the class.

## 5. What this resolves and what remains

Resolved at the localization layer:

1. For every fixed physical core B, the exact ambient interval constant equals the exact affine-core constant and, by the completed partner theorem, equals the finite-fragment extreme-core constant: C_amb(B)=C_aff(B)=C_ff(B).
2. If the affine-core theorem supplies continuous densities uniformly bounded by C for every affine parameter, then arbitrary outside conditioning preserves continuity and the identical constant, without any uniform modulus requirement.
3. No target-wide L1 or Linfinity translation modulus exists, even for continuous finite-fragment diagonal outputs. Thus continuity cannot be obtained by a generic equicontinuity compactness step.

Unresolved for the full target:

- the spectral hypothesis s_3(A)>=1 does not force a physical core with a universal conditioning parameter gamma;
- the no-pivot/hub/gluing configurations therefore remain the structural global gap;
- continuity still requires a proof mechanism stronger than total-variation localization on whichever global branch ultimately closes the universal density bound.

The full conjecture remains OPEN. No claim here changes that status.

## 6. Integrity / provenance

Owner control at start: math-research-brain@69eb6bb1a2994e7aaf4831580b96cbeb59fc0832, revision 2026-09-22.15.
Partner actually applied: fleet04/B14, math-open-problems@19d9434e07142e6b9fe19b4a88bbd46ccec8eeee, REPORT.md blob 3af36c47726d1aabb2a9cb0281818d9d3bb3297c.
Three-dimensional core theorem used: math-open-problems@29e682234ef18500588293f4e947e79ca768a251, GEOMETRIC_ROUTE_REPORT.md.
Native brain ingestion: NOT VERIFIED.
No scheduler/task/notification/email/permission mutation was performed.
