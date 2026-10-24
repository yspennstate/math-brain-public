SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B14, 2026-09-23T14:14:44Z.
attacking: Lp physical-space translation localization — hyperbolic-product smoothing plus a square term, with arbitrary outside-induced shifts and support geometry.

# account01/B14 r38 — hyperbolic Lp translation localization

Programme: `QFORM-DENSITY-3EIG-20260922`  
Run: `20260923T141444Z-account01-B14-QFORM-r38`  
Status: `NEW TARGET-LEVEL SUPPORTING THEOREM + ZERO-LOSS TRANSLATION/OUTSIDE LOCALIZATION / FULL QFORM OPEN`  
Execution: `WITHOUT_VERIFIED_BRAIN`.

## 1. Control and correction scope

Fresh brain control was read from `yspennstate/math-research-brain@41949ba63fc63c006d1b23fe34aaeadf5d3c04ed` before this mathematical write. OWNER CONTROL remains revision `2026-09-22.15`, QFORM-only, with no B14 pause/stop. The full conjecture remains open. The live corrections forbid law-uniform pointwise quadratic Fourier decay, post-rotation independence, bounded-diameter/fixed-fragment localization, arbitrary-joint 3D coarea, and worst normalized spectral-fiber caps. None is used below.

The newest completed designated-partner result consumed is account02/B14 r37, canonical `yspennstate/math-open-problems@66d12f0c2a0691601221d8e827736d24c56ca4f0:proofnet24/QFORM-density/fleet-2026-09-22/account02/B14/20260923T135912Z-account02-B14-QFORM-r37/REPORT.md`, read-back blob `8dc939d26c3055ccda1e662ae79c27769dbce2e0`. Its exact active-interval partition identity is applied in Section 6.

## 2. A sharp fractional bathtub bound

Let `X` have probability density `f` with `0<=f<=1`. For every shift `a` and `0<=alpha<1`,

`E |X-a|^(-alpha) <= 2^alpha/(1-alpha)`.                         (2.1)

Proof. The kernel `|x-a|^(-alpha)` is symmetric decreasing about `a`. Among densities bounded by one and of total mass one, the bathtub/rearrangement maximum is the indicator of the centered interval `[a-1/2,a+1/2]`. Hence

`int f(x)|x-a|^(-alpha) dx <= 2 int_0^(1/2) r^(-alpha)dr = 2^alpha/(1-alpha)`.

No support, moment, connectedness or centering hypothesis appears. In particular arbitrary remote fragments and arbitrary translations are already absorbed by (2.1).

## 3. Product Lp lemma, uniform in both translations

Let `X,Y` be independent cap-one variables. For `c!=0`, shifts `a,b` and every `1<=p<infinity`, set

`T=2c(X-a)(Y-b)`.

Then `T` has a density and

`boxed: ||p_T||_p <= p |c|^(-1+1/p).`                           (3.1)

Proof. Translate the input densities, writing them again as `f,g`. The density of `XY` is

`p_0(t)=int f(x) g(t/x) dx/|x|`.

Minkowski and scaling give

`||p_0||_p <= ||g||_p int f(x)|x|^(-1+1/p)dx`.

Since `0<=g<=1` and `int g=1`, `||g||_p<=1`. Apply (2.1) with `alpha=1-1/p`:

`int f(x)|x|^(-1+1/p)dx <= p 2^(1-1/p)`.

Finally density scaling by the factor `2c` contributes `(2|c|)^(-1+1/p)`, and the powers of two cancel, proving (3.1).

Two useful cases are

`||p_(2c(X-a)(Y-b))||_2 <= 2 |c|^(-1/2)`,                       (3.2)

`||p_(2c(X-a)(Y-b))||_3 <= 3 |c|^(-2/3)`.                       (3.3)

This is a purely physical-space estimate. It does not use pointwise Fourier decay and is completely insensitive to fragment locations.

## 4. Square L^(3/2) lemma, uniform in translation

Let `Z` be cap-one, `d!=0`, `r` arbitrary and

`S=d(Z-r)^2`.

Then

`boxed: ||p_S||_(3/2) <= 2 |d|^(-1/3).`                         (4.1)

For `d>0`, the square-map density obeys

`p_S(s) <= (d s)^(-1/2)`, `s>0`;

for `d<0` reflect the output. Therefore

`int p_S(s)^(3/2) ds
 <= |d|^(-1/4) int |s|^(-1/4)p_S(s)ds
 = |d|^(-1/2) E|Z-r|^(-1/2)
 <= 2sqrt(2)|d|^(-1/2)`

by (2.1) with `alpha=1/2`. Raising to power `2/3` gives (4.1).

## 5. Main target-level theorem: one hyperbolic block plus one square

Let the original independent coordinates be `(X1,X2,X3,W)`, where `W` is any possibly high-dimensional collection of the remaining independent coordinates. Assume the principal block of the symmetric matrix on `(X1,X2,X3)` is exactly

`B(c,d)=[[0,c,0],[c,0,0],[0,0,d]]`, `c d !=0`.                  (5.1)

All coefficients inside the outside `W` block and all couplings from `W` to the three active coordinates are arbitrary. Then

`boxed: ||p_(X^T A X)||_infinity <= 6 |c|^(-2/3)|d|^(-1/3).`    (5.2)

In particular, if `|c|>=1` and `|d|>=1`,

`boxed: ||p_(X^T A X)||_infinity <= 6.`                          (5.3)

Proof. Condition only on the outside ORIGINAL coordinates, `W=w`. The active quadratic becomes

`2c X1 X2 + d X3^2 + 2u1(w)X1+2u2(w)X2+2u3(w)X3 + C(w)`.

Complete the hyperbolic and square terms:

`2c[X1+u2/c][X2+u1/c] + d[X3+u3/d]^2 + C'(w)`.                 (5.4)

Conditional on `W=w`, the first bracketed term depends only on `(X1,X2)` and the second only on `X3`, hence they remain independent. By (3.3), (4.1), and Holder/Young convolution `L^3 * L^(3/2) -> L^infinity`,

`||p_(Q|W=w)||_infinity
 <= [3|c|^(-2/3)] [2|d|^(-1/3)]
 = 6|c|^(-2/3)|d|^(-1/3)`.                                     (5.5)

The bound is pointwise in `w`; averaging the conditional small-ball inequality gives the same constant unconditionally. Thus arbitrary outside translations, outside quadratic curvature, outside couplings, remote fragments, unbounded supports and all moments cost exactly zero.

The eigenvalues of the active principal block are `{c,-c,d}`. If `|c|,|d|>=1`, it has three eigenvalues of modulus at least one. Cauchy interlacing therefore guarantees that the full ambient matrix is in the owner's exact three-large-eigenvalue target. This is a genuine rotated/nonseparable original-coordinate family; diagonalizing the hyperbolic block would mix independent coordinates, and no such rotation is used.

### Zero-loss translation/localization statement

Equation (5.5) is uniform in the arbitrary shifts `u_i(w)`. Hence any finite or countable localization/decomposition of the outside law, including pieces translated arbitrarily far apart, may be conditioned and recombined with no change in the constant. The proof never normalizes an active fragment. This is the localization order required by the live correction record.

## 6. Two-hyperbolic corollary and completed partner r37 applied to an actual inequality

The same mechanism with two disjoint hyperbolic blocks uses (3.2) twice. If an active four-coordinate principal block is

`H(c,e)= [[0,c],[c,0]] direct_sum [[0,e],[e,0]]`,                (6.1)

with arbitrary outside couplings/self block, then conditioning outside coordinates, completing the two affine hyperbolic shifts, and applying `L^2*L^2 -> L^infinity` gives

`boxed: ||p_(X^TAX)||_infinity <= 4 / sqrt(|c e|).`              (6.2)

For the exact stress form from completed partner account02/B14 r37,

`Q=2X1X2+2ZV`,                                                   (6.3)

with `Z~Unif[1,2]`, `V~Unif[0,1]` and arbitrary cap-one independent `X1,X2`, we therefore obtain the actual target inequality

`boxed: ||p_Q||_infinity <= 4.`                                  (6.4)

Partner r37 proves that if the unchanged `V~Unif[0,1]` law is artificially partitioned into `N` equal cells before its absolute critical-Fourier certificate is paid, the exact effective parameter is

`K_eff,N=(12-8sqrt(2))N`,                                        (6.5)

and the optimized partner-r35 envelope satisfies

`F_(1,1)(K_eff,N) -> infinity`.                                  (6.6)

Combining the completed partner identity (6.5)-(6.6) with the genuine density bound (6.4) yields the concrete comparison

`boxed: ||p_Q||_infinity <=4  while  F_(1,1)((12-8sqrt(2))N)->infinity.` (6.7)

Thus the partner's divergence is conclusively a fragment-first proof-order artifact on the same fixed law. The physical-space L2 mechanism retains the full active law and is exactly translation/support insensitive. This improves the comparison constant used in partner r37 and requires no auxiliary all-eigenvalues theorem.

## 7. Abstract outside-translation compiler

The preceding proof illustrates a general zero-loss fact useful to B14. Let `I` be an active original-coordinate set. Suppose for the active quadratic matrix `A_II` one has, uniformly over every affine vector `b` and scalar `c`,

`P{x_I^T A_II x_I+b^T x_I+c in J} <= C |J|`                  (7.1)

for every cap-one product law on the active coordinates. Then for every full ambient matrix with this principal block, arbitrary outside block and arbitrary active-outside couplings, the full quadratic form obeys the same `C`.

Indeed condition on the outside original coordinates. They generate only an affine vector and constant in the active variables, so (7.1) applies pointwise and averaging preserves `C`. Consequently arbitrary translations, distant outside fragments and unbounded outside support never alter the constant. The target eigenvalue certificate supplied by a principal block is preserved by interlacing.

The key distinction exposed by partner r37 is that this compiler localizes OUTSIDE a completed affine-uniform active theorem. It does not justify recursively normalizing a certificate-active fragment before the analytic estimate.

## 8. Remaining gap

Full QFORM is still OPEN. The new theorem closes the branch in which an original-coordinate principal triple contains an exact hyperbolic block plus a disjoint nonzero square at universal scale, and it closes arbitrary outside couplings/translations for that branch. The bare hypothesis `s_3(A)>=1` does not force such a principal pattern with `|c|,|d|` universally bounded below; diffuse/no-pivot and dense three-way active blocks remain. The next structural question is whether one can obtain a comparable `L^p-L^q` factorization after a product-preserving grouped-coordinate reduction, without rotating the independent inputs.

## 9. Integrity

- Full QFORM: `OPEN / NOT PROVED / NOT DISPROVED`.
- New proved theorem: (5.2), with exact-target corollary (5.3).
- New proved two-hyperbolic theorem: (6.2), with actual partner stress inequality (6.4).
- Completed partner account02/B14 r37 applied at equations (6.5)-(6.7).
- No pointwise quadratic Fourier decay, post-rotation independence, support diameter, fragment count, moment, centering or log-concavity assumption is used.
- Essential boundedness is proved in the stated scopes; continuity is not separately claimed.
- Changed-file allowlist is this report only in `math-open-problems`; content was manually reviewed for secrets/private nonmathematical material. Repository access used only the authorized GitHub connector. No paid/remote model or workflow call, email, notification, scheduler, visibility or permission mutation was made.
