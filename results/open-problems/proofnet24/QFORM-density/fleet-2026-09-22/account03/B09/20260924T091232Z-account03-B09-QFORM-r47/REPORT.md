SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B09, 2026-09-24T09:12:32Z.
attacking: the punctured near-singular DEFINITE physical-pair survivor; retain the small Schur square and the entire original-coordinate Schur star jointly, and obtain a determinant-free O(interval length) bound.

# account03/B09 r47 — one-sided arcsine maximal closure for definite Schur stars

## Status

This run proves a new full-ambient supporting theorem for a literal original-coordinate **definite** physical pair.  The theorem is uniform as the pair determinant tends to zero and uses the same polynomial star currency that paid the exact singular face in r46.  It closes the `det B>0` punctured-definite branch left by r46/account02-B08.  It does **not** solve the unrestricted QFORM conjecture.  Essential boundedness and a linear interval bound are proved in the stated branch; continuity is not separately proved.

Execution status: `WITHOUT_VERIFIED_BRAIN`.  Repository retrieval and use were real; separate native learned-memory ingestion was not verified.

Full target remains:

> For independent real inputs with one-dimensional densities bounded by one and arbitrary real symmetric A with at least three eigenvalues of modulus at least one, prove that X^TAX has density bounded by one universal constant, or give a valid counterexample.

No moment, support, log-concavity, identical-law, diagonal-basis, or post-rotation independence hypothesis is introduced below.

## 1. Sources actually consumed

Fresh control was resolved from `yspennstate/math-research-brain` main at startup (`0ac493113c8ca9f98d75b25dbfb2a0f6e587153d`) and refreshed before publication (`697942d6bd38e3cd1cbcf3d33cd7813069d84855`).  OWNER CONTROL remained revision `2026-09-22.15`, QFORM-exclusive, with no B09 pause.

Required programme sources consumed: `AGENTS.md`, `scheduled_tasks/README.md` including the full OWNER MESSAGE, `scheduled_tasks/fleet.json`, `scheduled_tasks/roles.json`, `scheduled_tasks/PROTOCOL.md`, `MANIFEST.json`, `CURRENT_RESEARCH.md`, `CLAIMS.json`, the live `CORRECTION_INBOX.json`, `MEMORY_PROTOCOL.md`, and `assignments/account03/B09.json`.

The direct predecessor is account03/B09 r46:

- `yspennstate/math-open-problems@0ec2761c15a4699ff4d7208f59f19b7e025e4305`
- `proofnet24/QFORM-density/fleet-2026-09-22/account03/B09/20260924T064711Z-account03-B09-QFORM-r46/REPORT.md`.

The exact singular-face theorem used for comparison is account02/B08:

- `yspennstate/math-open-problems@cdd0eb22227a505e827a658038a1512897c0ad56`
- `proofnet24/QFORM-density/fleet-2026-09-22/account02/B08/account02-B08-20260924T034000Z-7c4f/REPORT.md`.

It proves, for a singular physical pair with polynomial star H, the full-ambient bound

`||p_Q||_infinity <= 2^(11/4) ||H||^(-1/2)`.

The designated partner result actually applied below is account04/B09:

- `yspennstate/math-open-problems@c0d3f34e557a374f41b2639994c43af4f950b682`
- `proofnet24/QFORM-density/fleet-2026-09-22/account04/B09/20260923T101659Z-account04-B09-dense-self-cross-fourier-r1/REPORT.md`.

Its completed theorem gives, for a literal disjoint original-coordinate invertible r x r cross block C with r>2,

`||p_Q||_infinity <= r/(r-2) |det C|^(-1/r)`,

with arbitrary same-side curvature and a continuous density.

## 2. Exact physical-pair setup

Use two ORIGINAL coordinates p,q and write every remaining original coordinate as the vector Z.  After conditioning on no variables, and allowing arbitrary affine terms, write

Q = a X^2 + 2 c X Y + b Y^2
    + 2 X <u,Z> + 2 Y <v,Z>
    + Z^T C Z + alpha X + beta Y + <gamma,Z> + q0.          (2.1)

Here X=X_p and Y=X_q are independent of Z and of each other, and every one-dimensional source density is bounded by one.  C is an arbitrary symmetric matrix; in particular its rank, sign, norm and internal couplings are unrestricted.

Let

B = [[a,c],[c,b]],                                                   (2.2)

and assume a != 0.  Define

H := a v - c u,                                                     (2.3)

g := v - (c/a)u = H/a,                                             (2.4)

delta := b - c^2/a = det(B)/a.                                     (2.5)

The vector H is the **polynomial Schur star** introduced in r46.  It has matrix-coefficient scale squared and remains well defined as det(B)->0.

Completing only the ORIGINAL coordinate X gives the exact identity

Q = a (X+h(Y,Z))^2 + S(Y,Z),                                       (2.6)

where

h(Y,Z) = [cY + <u,Z> + alpha/2]/a                                  (2.7)

and

S(Y,Z) = delta Y^2 + 2Y( <g,Z> + eta ) + W(Z),                     (2.8)

with

eta = (beta-c alpha/a)/2                                           (2.9)

and W an arbitrary quadratic-plus-affine function of Z.  Crucially, W is retained exactly.

If B is positive definite then a>0 and delta>0.  If B is negative definite, replace Q by -Q; density height is unchanged and H is unchanged.  Thus the only new analytic case is a>0, delta>0.

## 3. Arcsine maximal lemma

For a probability density f on R with 0<=f<=1 define

A f(c) := sup_{R>0} int_{c-R}^{c+R}
          f(y) / sqrt(R^2-(y-c)^2) dy.                             (3.1)

Also let M_c f be the centered Hardy-Littlewood maximal function,

M_c f(c) := sup_{R>0} [1/(2R)] int_{c-R}^{c+R} f(y)dy.             (3.2)

### Lemma 3.1

For every c,

A f(c) <= pi sqrt(M_c f(c)).                                      (3.3)

Consequently, for every lambda>0,

|{c: A f(c)>lambda}| <= 3 pi^2 / lambda^2.                        (3.4)

#### Proof

Fix c,R and set

m = int_{c-R}^{c+R} f(y)dy,

so 0<=m<=2R.  On the interval, the kernel

k_R(u)=(R^2-u^2)^(-1/2)

is symmetric and increases with |u|.  Under the constraints 0<=f<=1 and total interval mass m, the bathtub principle maximizes the weighted integral by filling the two endpoint pieces of total length m.  Therefore

int_{c-R}^{c+R} f(y)/sqrt(R^2-(y-c)^2) dy
 <= 2 int_{R-m/2}^{R} du/sqrt(R^2-u^2)
 = 2 arccos(1-m/(2R)).                                             (3.5)

Put x=m/(2R) in [0,1].  The elementary inequality

2 arccos(1-x) <= pi sqrt(x)                                       (3.6)

follows by writing x=1-cos(theta)=2 sin^2(theta/2), 0<=theta<=pi/2, and observing that theta/sin(theta/2) increases to pi/sqrt(2).  Hence (3.5) is at most

pi sqrt(m/(2R)).                                                   (3.7)

Taking the supremum in R proves (3.3).

The centered one-dimensional Hardy-Littlewood weak-(1,1) estimate, obtained by the usual disjoint-interval/Vitali selection and triple-cover argument, gives

|{M_c f > alpha}| <= 3 ||f||_1/alpha = 3/alpha.                   (3.8)

Combining (3.3) and (3.8) gives (3.4).  QED.

### Lemma 3.2 — cap-weighted arcsine maximal estimate

If q is any probability density on R with ||q||_infinity<=K, then

int q(c) A f(c) dc <= 2 pi sqrt(3K).                              (3.9)

#### Proof

First A f<=pi because f<=1 and the full arcsine kernel has integral pi.  By layer cake and (3.4),

int q A f
 <= int_0^pi min(1, 3 pi^2 K/lambda^2) d lambda.                  (3.10)

If K<=1/3, split at lambda_0=pi sqrt(3K):

(3.10)
 <= lambda_0 + 3 pi^2 K int_{lambda_0}^pi lambda^(-2) d lambda
 <= 2 pi sqrt(3K).                                                (3.11)

If K>1/3, the trivial bound pi is smaller than the right side of (3.9).  QED.

## 4. New one-sided Schur-star potential estimate

The absolute half-Riesz potential is the wrong object in the definite punctured case: for a nonzero scalar quadratic coefficient, the absolute kernel can have a logarithmic vertex divergence.  The first square in (2.6), however, supplies a **one-sided** kernel.  Retaining that sign is the essential step.

### Theorem 4.1 — one-sided scalar-star potential

Let Y be independent of a random vector Z, with density f_Y<=1.  Let L=L(Z) be a scalar random variable with probability density bounded by M.  Let W(Z) be arbitrary measurable.  For every delta>0 define

S = delta Y^2 + 2 Y L + W(Z).                                    (4.1)

Then

boxed:
 sup_t E[(t-S)_+^(-1/2)] <= 2 pi sqrt(3M),                        (4.2)

where r_+^(-1/2) means r^(-1/2) for r>0 and 0 for r<=0.

#### Proof

Complete the Y square exactly:

S = delta (Y + L/delta)^2 + V(Z),
V(Z)=W(Z)-L(Z)^2/delta.                                           (4.3)

Fix Z=z.  Put

c(z)=-L(z)/delta,
r(z)=t-V(z).                                                       (4.4)

If r(z)<=0 the conditional contribution to (4.2) vanishes.  If r(z)>0, put R=sqrt(r(z)/delta).  Then

E_Y[(t-S)_+^(-1/2) | Z=z]
 = delta^(-1/2)
   int_{|y-c(z)|<R} f_Y(y)/sqrt(R^2-(y-c(z))^2) dy
 <= delta^(-1/2) A f_Y(c(z)).                                    (4.5)

The random center c=-L/delta has density

q_c(s)=delta p_L(-delta s),                                      (4.6)

so ||q_c||_infinity<=delta M.  Lemma 3.2 now gives

E[(t-S)_+^(-1/2)]
 <= delta^(-1/2) 2 pi sqrt(3 delta M)
 = 2 pi sqrt(3M),                                                 (4.7)

uniformly in t, delta and the arbitrary W.  QED.

The cancellation of delta in (4.7) is the punctured-singular interpolation that was missing in r46.

## 5. Main theorem: definite physical pair with arbitrary remaining curvature

### Theorem `QFORM-DEFINITEPAIR-POLYNOMIAL-STAR-UNIFORM-v1`

In the full ambient setup (2.1), suppose the literal physical pair B is definite and H=a v-c u is nonzero.  Then Q has an essentially bounded density and

boxed:
 ||p_Q||_infinity
 <= 2^(5/4) pi sqrt(3) ||H||_2^(-1/2)
 = 12.941898654808462... ||H||_2^(-1/2).                          (5.1)

Consequently, for every interval I,

boxed:
 P(Q in I)
 <= 12.941898654808462... ||H||_2^(-1/2) |I|.                    (5.2)

No lower bound on det(B) is required.  In particular the estimate is uniform as det(B)->0 through the definite side.

#### Proof

By replacing Q by -Q if necessary, assume B is positive definite.  Then a>0 and delta>0.

Conditional on (Y,Z), the only remaining random coordinate in (2.6) is the ORIGINAL coordinate X.  The pushforward of a cap-one density by x -> a(x+h)^2 has, for u>0, density at most

1/sqrt(a u).                                                       (5.3)

Indeed the two inverse branches contribute at most

[1+1]/[2 sqrt(a u)].                                              (5.4)

Therefore averaging the conditional densities gives

p_Q(t)
 <= a^(-1/2) E[(t-S)_+^(-1/2)].                                  (5.5)

In (2.8), let

L=<g,Z>+eta.                                                       (5.6)

The standard one-dimensional product-projection density theorem used by account02/B08 gives

||p_L||_infinity <= sqrt(2)/||g||_2.                             (5.7)

No stochastic coordinate is rotated here: (5.7) is a marginal-density theorem for a linear form of the original independent coordinates.

Apply Theorem 4.1 with

M=sqrt(2)/||g||_2.                                                (5.8)

Then

||p_Q||_infinity
 <= a^(-1/2) 2 pi sqrt(3) [sqrt(2)/||g||_2]^(1/2)
 = 2^(5/4) pi sqrt(3) [|a| ||g||_2]^(-1/2).                      (5.9)

Finally |a| ||g||_2=||a g||_2=||H||_2.  This is (5.1).  Absolute continuity follows from the conditional square pushforwards and Tonelli/Fubini; the bound then gives (5.2).  QED.

### Scope and continuity

The theorem allows:

- arbitrary dimension;
- arbitrary signs and sizes outside the displayed pair;
- arbitrary same-bank and outside quadratic curvature C;
- arbitrary affine terms generated by conditioning;
- arbitrary fragmented or unbounded supports;
- arbitrary independent one-dimensional input laws satisfying only density<=1.

The proof establishes an essentially bounded density.  It does **not** separately prove that a continuous representative exists.

## 6. Unified nonindefinite star face

Combine (5.1) with the exact singular theorem from account02/B08/r46.  Whenever a!=0, H!=0 and det(B)>=0,

- det(B)>0: Theorem 5.1 gives constant 12.9418986549;
- det(B)=0: the singular-hub theorem gives the smaller constant 2^(11/4)=6.72717132203.

Thus the entire definite-plus-singular physical-pair side is paid by the same polynomial currency ||H|| without any reciprocal power of det(B).

This does **not** extend to det(B)<0: a rank-two opposite-sign form can have a logarithmically unbounded density.  Section 9 records a precise star-preserving obstruction.

## 7. Application to the live punctured survivor

Account02/B08's live two-hub state has, after its earlier gates fail,

|a| > (4031/8192) L                                               (7.1)

and a two-row physical arm M with

s_2(M) >= L/8.                                                     (7.2)

For the other hub q,

g = m_q-(c/a)m_p = (-c/a,1)M,                                   (7.3)

hence

||g|| >= s_2(M) sqrt(1+(c/a)^2) >= L/8.                          (7.4)

If det(B)>0, the pair is definite.  Theorem 5.1 therefore yields

||H||=|a| ||g|| > (4031/8192)(1/8)L^2,                           (7.5)

and hence

boxed:
 ||p_Q||_infinity < 52.1833025296 / L.                           (7.6)

This is uniform in the puncture size

0 < |det(B)/a| < 0.0317461548003 L                               (7.7)

and, in fact, does not use its upper bound at all.  The determinant may tend to zero through the definite side with no loss.

At det(B)=0 the preceding singular theorem gives the sharper `<27.1247693734/L` under the same gates.  Thus the exact singular face and the entire punctured **definite** side are now both closed.

The punctured **indefinite** side remains a genuinely different object; a local two-resource theorem cannot simply be inferred by continuity.

## 8. Target-valid stress family through det(B)->0+

For delta>0 define

A_delta =
[[2, 2,           0, 0],
 [2, 2+delta/2,   1, 0],
 [0, 1,          -5, 0],
 [0, 0,           0, 1]].                                       (8.1)

Use the physical pair {1,2}.  Then

B_delta=[[2,2],[2,2+delta/2]],                                   (8.2)

det(B_delta)=delta>0,                                            (8.3)

u=(0,0), v=(1,0), and

H=2v-2u=(2,0),  ||H||=2.                                        (8.4)

Thus Theorem 5.1 gives, for every delta>0,

boxed:
 ||p_Q||_infinity <= 12.941898654808462/sqrt(2)
                  = 9.15130430024412.                            (8.5)

The coefficient is completely independent of delta.

The deterministic checker verifies for delta=1, 10^-2, 10^-4, 10^-8, 10^-12 that A_delta has at least three eigenvalues of modulus at least one.  At delta=10^-12 the eigenvalues are approximately

{-5.15169024111, 0.095716118369, 1, 4.05597412274}.               (8.6)

Thus this is an actual target-valid family passing arbitrarily close to the singular physical-pair face while the new bound stays fixed.

## 9. Why the same local statement is false on the indefinite side

The sign in Theorem 4.1 is essential.  A star-preserving rank-two obstruction shows that one cannot replace `definite` by `arbitrary signature` while keeping only ||H|| as local currency.

Fix d>0 and g!=0 and consider three original coordinates with

A =
[[1, 0,       0],
 [0,-d,       g],
 [0, g, -g^2/d]].                                                 (9.1)

For the physical pair (1,2),

B=diag(1,-d),
H=(g),                                                            (9.2)

so H is nonzero and can be held fixed while d->0.  But

Q = X^2 - d (Y-(g/d)Z)^2.                                       (9.3)

Take X,Y,Z independent Uniform[-1/2,1/2].  The variable

T=Y-(g/d)Z                                                       (9.4)

is independent of X and has a continuous density strictly positive near zero.  Hence X^2 has density comparable to u^(-1/2) near zero and dT^2 has density comparable to v^(-1/2) near zero.  Therefore the density of their difference at zero contains

int_0^epsilon u^(-1/2) u^(-1/2) du = infinity.                   (9.5)

So the local rank-two output has the standard logarithmic singularity.

Appending an independent +R^2 coordinate gives a target-valid four-dimensional form with eigenvalues containing +1,+1 and the negative eigenvalue -(d+g^2/d), while the full output is bounded because X^2+R^2 already has density<=pi and convolution cannot increase the sup.  This illustrates the correct structural lesson: on the indefinite side the **third smoothing resource must be retained before a full density conclusion**.  The local pair-star subsystem alone cannot supply it.

This is not a counterexample to QFORM.

## 10. Required designated-partner application

Apply account04/B09's completed physical-cross theorem to

K=diag(4,2,1),
A_*=[[0,K],[K,0]].                                                (10.1)

The spectrum is

{-4,-2,-1,1,2,4},                                                (10.2)

so this is target-valid.  Since det K=8, the partner theorem gives the actual inequality

boxed:
 ||p_{X^T A_* X}||_infinity <= 3 * 8^(-1/3) = 3/2,              (10.3)

and

P(X^T A_* X in I) <= (3/2)|I|.                                  (10.4)

That branch has a continuous density.  This is a direct application of the designated partner result to an explicit equation, not a renamed theorem.

## 11. Deterministic checks

`CHECK.py` and `CHECK_OUTPUT.txt` beside this report perform:

1. 1000 seeded exact algebra checks of (2.6)-(2.9) and H=a g;
2. a deterministic numerical regression of the sharp bathtub inequality behind Lemma 3.1 on random finite unions of intervals;
3. target-spectrum checks for the stress family (8.1) down to delta=10^-12;
4. the live constant calculation (7.6);
5. the account04/B09 partner calculation (10.3).

Observed maxima/results:

- maximum square-completion error: `1.2079226507921703e-13`;
- maximum polynomial-star identity error: `4.399061727369025e-15`;
- maximum arcsine-bound numerical ratio: `1.00000000000001`;
- definite-star constant: `12.941898654808462`;
- stress-family bound: `9.15130430024412`;
- live punctured-definite bound: `52.18330252952394/L`;
- partner bound: `1.5`.

All assertions passed.  The numerical regression is not used as proof; Lemmas 3.1-3.2 and Theorem 4.1 are analytic.

## 12. Exact remaining B09 debt

The next B09 implication is now

`QFORM-NEAR-SINGULAR-INDEFINITE-PAIR-THIRD-RESOURCE-COMPILER-v1`:

> in the punctured det(B)<0 survivor, retain the third genuine spectral/crossing resource **jointly** with the logarithmic two-resource pair, and route it into an O(interval length) bound without assuming an independent extra square, without deleting the small Schur coefficient, and without rotating the source variables.

Section 9 proves that a theorem depending only on the indefinite pair plus its star is false; the third resource is mathematically necessary.  Candidate routes are the already-paid physical 3x3 cross determinant theorem, aggregate third-volume/projected-crossing receivers, or a three-resource logarithmic convolution in original coordinates.  The structural compiler must state which resource is actually present and preserve arbitrary remaining curvature.

Full unrestricted QFORM remains **OPEN**.  Full-target continuity remains **OPEN**.

## 13. Integrity / privacy / scope

Changed-file allowlist for this run is restricted to this B09 run directory in math-open-problems and this worker's own handoff/memory/status paths in math-research-brain.  Manual fallback privacy review found only mathematical formulas, public repository commit identifiers, logical account/slot labels and nonsecret run metadata; no credentials, scheduler IDs, signed URLs, machine paths, private personal data, trading/company/client material, or unrelated source excerpts are included.

No task identity, cadence, enabled/paused state, notification setting, email setting, permission, public visibility, cross-account authentication, paid API/model/Codex call, or remote workflow was changed.
