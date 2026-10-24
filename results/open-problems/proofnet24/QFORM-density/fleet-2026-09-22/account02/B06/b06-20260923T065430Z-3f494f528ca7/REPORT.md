SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account02, slot B06, 2026-09-23T06:54:30Z.
attacking: a product-weighted receiver for the anchored zero-cross fiber, retaining arbitrary background quadratic curvature, and testing the first opposite-sign extension.

# account02/B06 — weighted mixed parabola-line receiver and a resonant obstruction

**Run:** `b06-20260923T065430Z-3f494f528ca7`  
**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Assignment:** Curved fiber integration / complementary constructions and source-valid counterexamples  
**Classification:** `ESSENTIAL_STEP_APPLIED + CANDIDATE_REFUTED`; full QFORM remains **OPEN / NOT PROVED / NOT DISPROVED**.  
**Execution:** `WITHOUT_VERIFIED_BRAIN`; authenticated repository transport occurred, but verified native learned-memory retrieval plus receiver use was not established.  
**Continuity:** not claimed below; all positive conclusions are essential-density bounds.

## 0. Exact target, current controls, and source pins

The target is unchanged: for arbitrary independent real coordinates with probability densities bounded by one, and every real symmetric matrix having at least three eigenvalues of modulus at least one, prove a universal essential bound for the density of the quadratic form, or give a valid target counterexample. No moments, support restriction, log-concavity, identical-law hypothesis, diagonal-basis assumption, or post-rotation independence is used.

Fresh owner control was reread during the run and remained revision `2026-09-22.15`, QFORM only, with no applicable B06 stop. The live programme corrections were consumed: no law-uniform pointwise quadratic-phase decay, no independence after spectral rotation, no arbitrary-joint rank-three coarea bound, no positive moment of a worst conditional projection-density cap, no dimension-free unrestricted fiber supremum, and no universal good physical minor/cross-rank-three selector.

The concrete B06 continuation says to extend the genuine scalar/dependent-pair kernel into a non-null or coupled regime while retaining its actual independence hypotheses. The exact card asks for weighted product structure in place of a dimension-losing fiber maximum.

Source-valid inputs used at equations:

1. **Designated partner account03/B06 r28**, canonical mathematics `yspennstate/math-open-problems@36cc5730f42c76c15fdc330dc4b47beec060b8fd`, path `proofnet24/QFORM-density/fleet-2026-09-22/account03/B06/20260923T061939Z-account03-B06-qform-r28/REPORT.md`. It proves the two-hub anchor currency and the exact identity
   `Z_(i,a)=||bD-cr^T||_F^2`, with the zero-anchor specialization `Z_(i,a)=||c||_2^2||r||_2^2`.
2. **Own completed weighted affine-fiber Brascamp--Lieb theorem**, `yspennstate/math-open-problems@8dd33c1abd4fd64140f59032feda2b13d4351da5`, path `proofnet24/QFORM-density/fleet-2026-09-22/account02/B06/b06-20260922T155426Z-9fd56fa68a65/REPORT.md`. For a normalized one-dimensional linear projection of independent cap-one coordinates, the density is at most `sqrt(e)`; more generally the theorem derives projection caps by integrating the original product law along the affine fiber before taking any supremum.
3. **Newest-Claude package required by the owner**, `yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`, directory `proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/`. `RESULTS.md`, `FOURIER_ROUTE_REPORT.md`, and `COUNTEREXAMPLE_SEARCH.md` were read. Section 4 / Theorem C of the counterexample report gives the one-sheet ruled rank-three bound used in Section 5 below.
4. Immediate predecessor account02/B06 `yspennstate/math-open-problems@e8bd09a6e9c8dbe964b87f52ff9b5b6d13421958`, which paid a zero-diagonal hyperbola followed by a whole-row quarter-Riesz receiver and left the nonzero-diagonal/diagonal-Schur branch open.

An early substantive checkpoint for the present run was already committed at `52e151a962e11b98608c84368dc817bc573fb786` in this same run directory.

## 1. A weighted mixed parabola-line theorem

The first unpaid implication can be paid in a zero-cross physical fiber without taking any conditional fiber supremum.

### Theorem 1 — `QFORM-MIXED-PARABOLA-LINE-WEIGHTED-v1`

Let `X,Y` be independent real random variables with densities bounded by one. Let `Omega` be independent of `(X,Y)`. Let `A=A(Omega)`, `B=B(Omega)`, and `R=R(Omega)` be arbitrary measurable real random variables. Assume only that `B` has an absolutely continuous law with density bounded by `L<infinity`. For every fixed `a!=0`,

`T = a X^2 + 2 A X + 2 B Y + R`

has an essentially bounded density satisfying

`boxed: ||p_T||_infinity <= 6 L^(2/3) |a|^(-1/3).`                    (1.1)

The theorem allows arbitrary dependence among `A,B,R`. The only product provenance used is that the two physical anchor variables `X,Y` are independent of the background `Omega` and of each other. In particular, no conditional density cap is invented by a rotation or nonlinear change of variables.

### Proof

Condition on `Omega`, so `A,B,R` are fixed numbers. The term `R` is a translation. Complete the square in the genuine original coordinate `X`:

`aX^2+2AX = a(X+A/a)^2-A^2/a`.                                      (1.2)

A translate of `X` still has a density `f<=1` and mass one. Let `G` be the density of `a(X+c)^2`. For `1<q<2`, writing `r=sqrt(|u|/|a|)` on the supported half-line gives

`G(u)=[f(c+r)+f(c-r)]/(2|a|r)`.                                     (1.3)

Therefore

`int G(u)^q du
 <= |a|^(1-q) int f(x)^q |x-c|^(1-q) dx
 <= |a|^(1-q) int f(x)|x-c|^(-(q-1)) dx`.                           (1.4)

The last integral is maximized under `0<=f<=1`, `int f=1`, by filling the unit-length interval closest to `c`. Hence

`int f(x)|x-c|^(-(q-1)) dx <= 2^(q-1)/(2-q)`.                       (1.5)

At `q=3/2`, (1.4)-(1.5) give the uniform, translation-free estimate

`boxed: ||G||_(3/2) <= 2 |a|^(-1/3).`                               (1.6)

For fixed `B=b`, the density `H_b` of `2bY` satisfies

`||H_b||_3 = (2|b|)^(-2/3)||f_Y||_3 <= (2|b|)^(-2/3)`,               (1.7)

because `int f_Y^3<=1`. Young's convolution inequality with exponents `(3/2,3,infinity)` gives, conditionally on `Omega`,

`||p_(T|Omega)||_infinity
 <= 2^(1/3)|a|^(-1/3)|B|^(-2/3).`                                   (1.8)

Now average with the actual background law instead of replacing it by a worst fiber. If `p_B<=L`, the one-dimensional bathtub inequality gives

`E |B|^(-2/3)
 <= L int_(-1/(2L))^(1/(2L)) |b|^(-2/3) db
 = 6*2^(-1/3)L^(2/3).`                                              (1.9)

Combining (1.8) and (1.9) proves (1.1). QED.

### Why this is the assigned weighted replacement

The conditional bound (1.8) genuinely blows up at `B=0`; its supremum is infinite. The theorem succeeds only because the original product law supplies a quantitative density bound for the random coefficient `B`, and the singular power `|B|^(-2/3)` is integrated against that weight. This is precisely the operation forbidden by the old dimension-losing fiber-sup route and requested by the B06 card.

## 2. Matrix-level zero-cross corollary retaining every other quadratic coefficient

Let `Q(x)=x^T A x + ell^T x + c` in independent cap-one original coordinates. Pick two physical coordinates `i,j` such that

`A_ii=a!=0`, `A_jj=0`, `A_ij=0`.                                    (2.1)

Put

`sigma_j = (sum_(k notin {i,j}) A_jk^2)^(1/2)`.                      (2.2)

If `sigma_j>0`, then

`boxed: ||p_Q||_infinity <= 6 e^(1/3)|a|^(-1/3)sigma_j^(-2/3).`      (2.3)

### Proof

Let `Omega=X_{-{i,j}}`. Then exactly, with no approximation,

`Q=aX_i^2+2A(Omega)X_i+2B(Omega)X_j+R(Omega)`,                       (2.4)

where every other diagonal, off-diagonal, outside coupling and affine term is retained inside the arbitrary functions `A,B,R`. The coefficient

`B(Omega)=sum_(k notin {i,j}) A_jk X_k + constant`                   (2.5)

is a scaled one-dimensional linear projection of the original product law. By `QFORM-WEIGHTED-AFFINE-FIBER-BL-v1`, after normalization its density is at most `sqrt(e)`, so

`||p_B||_infinity <= sqrt(e)/sigma_j`.                               (2.6)

Insert `L=sqrt(e)/sigma_j` into Theorem 1. This yields (2.3). QED.

No spectral hypothesis was needed for the lemma itself, so it can be inserted into any target branch that produces the physical pattern (2.1).

### A genuine target family paid uniformly

Let `N>=1`, `v=(N^(-1/2),...,N^(-1/2))`, and

`A_N = [1] direct_sum [[0,v^T],[v,0_N]].`                            (2.7)

Its nonzero spectrum is exactly `{1,1,-1}`. Thus it is a full target-valid family even though every individual star edge is `N^(-1/2)->0`. Here `a=1` and `sigma_j=||v||=1`, so (2.3) gives for every collection of independent cap-one input laws

`boxed: ||p_(X^T A_N X)||_infinity <= 6 e^(1/3) = 8.3736745505...`   (2.8)

uniformly in `N`. This is a new diffuse zero-cross payment: it aggregates the entire star row before taking the reciprocal exponent.

## 3. A two-null disjoint-coefficient receiver

The partner's zero-anchor `b=0` branch suggests a second exact weighted theorem. It is deliberately stated only at the independence scope actually proved.

### Theorem 2 — `QFORM-DOUBLE-NULL-DISJOINT-COEFFICIENT-v1`

Let `X,Y` be independent cap-one variables. Let `U,V` be independent random objects, independent also of `(X,Y)`. Let `Z=z(U)` and `W=w(V)` have one-dimensional densities bounded by `L_Z,L_W`. For arbitrary measurable `R=R(U,V)`,

`T=2XW+2YZ+R`

has

`boxed: ||p_T||_infinity <= 4 sqrt(L_Z L_W).`                         (3.1)

### Proof

Fix `(U,V)`, hence fix `z,w,R`. The two random variables `2wX` and `2zY` are independent. Their `L^2` density norms are bounded by `(2|w|)^(-1/2)` and `(2|z|)^(-1/2)`. Cauchy--Schwarz/Young therefore gives

`||p_(T|U,V)||_infinity <= 1/(2 sqrt(|WZ|)).`                         (3.2)

For a scalar variable with density cap `L`, the bathtub principle gives

`E|Z|^(-1/2) <= 2 sqrt(2L)`.                                        (3.3)

Since `Z` and `W` are functions of independent banks, their negative moments factor. Averaging (3.2) and applying (3.3) twice yields (3.1). QED.

If `Z=c^T U` and `W=r^T V` are nonzero linear projections of independent cap-one coordinate banks, the weighted affine-fiber theorem gives

`L_Z<=sqrt(e)/||c||`, `L_W<=sqrt(e)/||r||`,

and hence

`boxed: ||p_T||_infinity <= 4 sqrt(e) / sqrt(||c|| ||r||).`           (3.4)

All quadratic curvature inside `R(U,V)`, including arbitrary within-bank and cross-bank terms among the leaves, is retained. The hypothesis that the two anchor coefficients come from disjoint product banks is essential to this proof; arbitrary same-side anchor couplings are not silently discarded.

## 4. Real application of the designated partner r28 result

The partner's live low-disjointness chamber has `Z2>16G^4/25`, row and column hub errors below `1/256`, and hence an anchor with

`Z_(i,a)>127G^4/800`.                                                (4.1)

In its exact zero-cross-anchor subbranch `b=0`, the partner identity becomes

`Z_(i,a)=||c||^2||r||^2`,

so

`||c||||r|| > sqrt(127/800) G^2 =0.3984344362...G^2.`                (4.2)

If, additionally, the two anchor coefficients are supported on the opposite disjoint original-coordinate banks (equivalently the same-side anchor-to-leaf couplings vanish in this split), Theorem 2 applies with the whole leaf quadratic remainder left untouched. Combining (3.4) and (4.2) yields the actual partner-spliced inequality

`boxed: ||p_Q||_infinity
 < [4 sqrt(e)/(127/800)^(1/4)] G^(-1)
 =10.4478949866.../G.`                                               (4.3)

This is a genuine use of the completed account03/B06 result at a new receiver, not a copied citation. It pays an infinite-dimensional diffuse double-star subbranch without selecting one local minor. The remaining difficulty is exactly the same-side anchor-coupling case, in which the two random coefficients can share background coordinates and (3.3) can no longer be factorized.

## 5. The first tempting opposite-sign extension is false

One might hope that random linear coefficients by themselves regularize the branch obtained when a nonzero cross anchor is completed into two opposite-sign squares. That mechanism is false under the unchanged product hypotheses once arbitrary background curvature is allowed to recenter both critical values.

Let `X,U,Y,V` be independent `Uniform[-1/2,1/2]`. Then

`X^2-Y^2+2UX+2VY+(U^2-V^2)=(X+U)^2-(Y-V)^2`.                        (5.1)

Put `S=X+U` and `T=Y-V`. Both have the triangular density `g(s)=1-|s|` on `[-1,1]`, so their joint density is positive near `(0,0)`. With

`P=S-T`, `R=S+T`,

we have `S^2-T^2=PR`, and the joint density of `(P,R)` is

`h(p,r)=1/2 g((p+r)/2)g((r-p)/2)`,                                  (5.2)

so `h(0,0)=1/2`. Therefore for sufficiently small `delta>0`, `h>=c>0` on `[-delta,delta]^2`. The product-density formula gives, for small nonzero `w`,

`p_(PR)(w)=int h(p,w/p) dp/|p|
 >= 2c log(delta^2/|w|)`,                                           (5.3)

up to shrinking the fixed neighborhood. Thus the density is logarithmically unbounded at zero.

This is **not** a counterexample to QFORM: the quadratic matrix of (5.1) has only the two nonzero eigenvalues `+2,-2`. It is a source-valid counterexample to the proposed intermediate receiver “two random affine coefficients regularize an opposite-sign physical pair regardless of the remainder.” The third large direction must be consumed jointly, not merely cited.

## 6. Required newest-Claude result applied to the obstruction

Add an independent cap-one coordinate `Z` and consider

`Q_*=(X+U)^2-(Y-V)^2+Z^2`.                                          (6.1)

Its physical matrix has spectrum exactly `{2,-2,1,0,0}`, hence (6.1) is a genuine target matrix with three large eigenvalues. The newest-Claude `COUNTEREXAMPLE_SEARCH.md`, Theorem C, is a completed ruled one-sheet estimate for exact rank three. Apply it with positive eigenvalues `lambda_1=2`, `lambda_2=1` and negative magnitude `mu=2`. For every `s>=0` and every independent cap-one input law,

`p_(Q_*)(s)
 <= (1/sqrt(2*1*2)) int_0^(2pi)
       dtheta / sqrt(sin(theta)^2/2 + cos(theta)^2 + 1/2)
 = (1/2) int_0^(2pi) dtheta/sqrt(1+cos(theta)^2/2)
 =2.8314744169... < pi.`                                            (6.2)

So the exact third large direction really does repair the **one-sheet side** of the resonant construction even though the rank-two core has the logarithmic singularity (5.3). The two-sheet side is outside the stated scope of Theorem C and is not declared solved here. This concrete splice identifies the unpaid geometry more sharply: in the remaining opposite-sign anchor branch, the third spectral direction must enter before the absolute fiber singularity is paid.

## 7. What changed and the first unpaid implication

This run makes three concrete advances.

* A zero-cross physical pair with one nonzero diagonal is now paid by a weighted `L^(3/2)*L^3` fiber argument, with arbitrary remaining quadratic/affine structure retained. The coefficient singularity is averaged against its genuine product-projection law rather than replaced by a supremum.
* The partner r28 zero-anchor double-star currency is paid in the disjoint-coefficient subbranch by a whole-bank negative-moment argument, giving the explicit new bound `10.448/G`.
* A stronger naive extension to opposite-sign completed squares is rigorously false; a target-valid third-square extension is then fed into the required newest-Claude ruled theorem, producing the actual one-sheet bound `2.832`.

The first unpaid implication is therefore:

`QFORM-ZERO-ANCHOR-SHARED-COEFFICIENT-OR-OPPOSITE-SIGN-THIRD-DIRECTION-v1`:

> In the partner r28 anchored state, after the one-null and disjoint-double-null receivers above are removed, retain arbitrary same-side anchor couplings and every complementary spectral component, and prove either (i) a product-preserving joint negative-moment estimate for the two shared linear coefficient forms using a genuine transverse/third-direction currency, or (ii) an exact reduction of the opposite-sign completed pair to the already-paid ruled / aggregate-volume / ridge exits. No worst conditional coefficient-density supremum, single-minor selection, or post-rotation independence is permitted.

The counterexample (5.1)-(5.3) shows that this implication cannot be obtained by simply deleting the third direction after it has generated random translations.

## 8. Verification status

The full conjecture is still open. The two new analytic lemmas above have not yet received an independent mathematical review. A deterministic checker in this run directory verifies the constants, the two target spectra used in Sections 2 and 6, and the numerical value of the exact one-sheet integral; it is a consistency check, not a proof certificate.