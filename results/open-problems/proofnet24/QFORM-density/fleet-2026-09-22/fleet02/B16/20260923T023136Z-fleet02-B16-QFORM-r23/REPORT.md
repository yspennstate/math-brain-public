SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet02, slot B16, 2026-09-23T02:31:36Z.
attacking: distributed approximate-coloop banks—compress the whole original-coordinate line bank before the curved quadratic pushforward, retain genuine independence from the transverse dependent pair, and remove the reciprocal leakage loss.

# QFORM-DISJOINT-SPECTRAL-LINE-PLANE-44-v1

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Assignment:** Projection-product interaction  
**Status:** `NEW SUPPORTING THEOREM / FULL QFORM OPEN / CONTINUITY OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`.

## 1. First unpaid implication and source boundary

The latest completed designated-partner result is fleet03/B16 r21, `QFORM-CROSS-TRANSVERSE-PROJECTION-PRODUCT-v2` and `QFORM-EXACT-SPECTRAL-COLOOP-34-v1`, canonical source

`yspennstate/math-open-problems@715e0a1445a9cd363b2793e6d982633fbc1c3362:proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B16/20260923T021400Z-fleet03-B16-QFORM-r21/REPORT.md`.

It pays a leverage-one physical spectral coloop, and names as the next B16 debt a leverage `c in (1/2,1)` approximate coloop whose residual `1-c` leakage has to be aggregated with product provenance before a reciprocal pivot is paid.

This report proves that interpolation **uniformly** when the leaked coloop direction occupies an original-coordinate spectral line bank source-disjoint from the transverse spectral plane. The constant does not depend on `c` or on the number of coordinates in the leaked line bank. The genuinely overlapping case remains open.

The required Claude package is used at an equation, not bibliographically: at

`yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837:proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/COUNTEREXAMPLE_SEARCH.md`,

Theorem C uses the sharp two-dimensional product-marginal estimate `||p_Y||_infinity<=2` and proves the global one-sheet estimate `pi sqrt(2)` for every exact-rank-three `(2,1)` form. The same product-marginal estimate is inserted below into the partner cross-transverse inequality. The Fourier report's volume theorem is also tested below: on the natural line/plane cut its 3-volume is identically zero, so volume-only decoupling does not pay this class.

Live corrections retained: no independence after spectral rotation; no arbitrary-joint 3D coarea theorem; no normalized conditional projection-height suprema/moments; no law-uniform pointwise quadratic-phase decay; and no treatment of a small matrix term as a small random quadratic perturbation on unbounded inputs.

## 2. Geometry: a distributed coloop bank

Let the whole target matrix have exact rank three,

`A=R B R^T`, `R^T R=I_3`,                                      (2.1)

where `B` is real symmetric and all three eigenvalues of `B` have modulus at least one. Equivalently,

`D:=|det B|>=1`, `s_min(B)>=1`.                                  (2.2)

Assume there is an ORIGINAL-coordinate partition

`I disjoint_union J=[n]`                                         (2.3)

and a unit vector `e in R^3` such that

`r_i in span(e)` for every `i in I`,
`r_j in e^perp` for every `j in J`,                              (2.4)

where `r_k` is row `k` of `R`.

Choose spectral coordinates with `e=e_1`. Write

`r_i=(a_i,0,0)`, `i in I`,
`r_j=(0,b_j,c_j)`, `j in J`.                                    (2.5)

Parseval, `sum_k r_k r_k^T=I_3`, gives the exact identities

`sum_(i in I) a_i^2=1`,
`sum_(j in J) (b_j,c_j)^T(b_j,c_j)=I_2`.                         (2.6)

Define

`S=sum_(i in I) a_i X_i`,
`Y=(U,V)=sum_(j in J) (b_j,c_j) X_j`.                            (2.7)

Then

`R^T X=(S,Y)`,
`Q=X^TAX=(S,Y)^T B (S,Y)`.                                      (2.8)

Most importantly, `S` is independent of the **whole pair** `Y`, because they use disjoint original-coordinate banks. No independence between `U` and `V` is asserted.

By the one-dimensional Rogozin--Ball/Livshyts--Paouris--Pivovarov projection estimate and (2.6),

`L:=||p_S||_infinity <= sqrt(2)`.                                (2.9)

By the two-dimensional product-marginal estimate used in Claude Theorem C,

`M:=||p_Y||_infinity <=2`.                                       (2.10)

These are the only stochastic compression facts used below.

### Approximate-coloop interpretation

If one coordinate `i_0 in I` has leverage `a_(i_0)^2=c in (1/2,1)`, then the remaining line-bank mass is exactly

`sum_(i in I\{i_0}) a_i^2=1-c`.                                  (2.11)

Thus (2.4) is an actual approximate-coloop model with arbitrary distributed leakage, except that the leakage remains on the same spectral line and is source-disjoint from the transverse plane. No bound below deteriorates as `c ->1` or as `c ->1/2`.

## 3. Scalar-cap extension of the partner cross-transverse theorem

Fleet03/B16 r21 proves for a cap-one scalar independent of a possibly dependent receiver pair of joint density cap `M` that, after rotating only inside the receiver plane,

`||p_Q||_infinity <= Cx M^(2/3)(D P)^(-1/6)`,
`Cx=3*2^(8/3)`,                                                   (3.1)

where `P=beta^2|e_22|` is its transverse resource.

For completeness, if the scalar density cap is `L` rather than one, set

`S_tilde=L S`.                                                     (3.2)

Then `p_(S_tilde)<=1`. In the coefficient matrix the first row/column is scaled by `1/L`, so

`D_tilde=D/L^2`, `P_tilde=P/L^2`.                                 (3.3)

Applying (3.1) to `(S_tilde,Y)` yields the exact rescaled form

`boxed: ||p_Q||_infinity
 <= Cx L^(2/3) M^(2/3)(D P)^(-1/6).`                              (3.4)

No stochastic assumption changes under this deterministic rescaling.

The partner's completed cross-resource lemma says that, for `s_min(B)>=1`, if `a=B_00` obeys `|a|<1`, then after rotating only the receiver plane,

`P >= (1-|a|)D`.                                                   (3.5)

Therefore, for any fixed `tau in (0,1)` and `|a|<=tau`, (2.9)--(2.10), (3.4)--(3.5), and `D>=1` give

`||p_Q||_infinity
 <=3*2^(8/3)*(sqrt(2)*2)^(2/3)*(1-tau)^(-1/6)
 =3*2^(11/3)(1-tau)^(-1/6).`                                     (3.6)

At `tau=4/7`,

`near <= 3*2^(11/3)*(7/3)^(1/6)
      =43.8760345408... <44.`                                    (3.7)

This includes the exact null scalar pivot `a=0`; the transverse resource is then forced rather than divided by the pivot.

## 4. Non-small pivot: square peel plus rank-two product half-Riesz

Suppose now `a=B_00 !=0`. Complete the square only in the **genuinely independent bank scalar** `S`:

`Q=a(S+a^(-1)b^T Y)^2 + Y^T C_sch Y`,                             (4.1)

where

`C_sch=C-bb^T/a`,
`|det C_sch|=D/|a|`.                                              (4.2)

For a scalar density cap `L`, the conditional density of `a(S+h)^2` is bounded by

`L (|a| |w|)^(-1/2)`                                              (4.3)

on the appropriate half-line, uniformly in the deterministic shift `h`.

The completed rank-two product-projection half-Riesz theorem used by fleet03/B16 r21 gives, for the orthonormal product projection `Y`,

`sup_t E |t-Y^T C_sch Y|^(-1/2)
 <= C2 |det C_sch|^(-1/4)`,
`C2=16*2^(3/4)`.                                                   (4.4)

Combining (4.1)--(4.4),

`||p_Q||_infinity
 <= L C2 |a|^(-1/2)(D/|a|)^(-1/4)
 = L C2 (|a|D)^(-1/4).`                                          (4.5)

With `L<=sqrt(2)`, `D>=1`, and `|a|>=4/7`,

`far <= sqrt(2)*16*2^(3/4)*(7/4)^(1/4)
     =43.7690367958... <44.`                                     (4.6)

## 5. The theorem

### Theorem 5.1 — `QFORM-DISJOINT-SPECTRAL-LINE-PLANE-44-v1`

Under (2.1)--(2.4), for arbitrary independent original inputs with probability densities bounded by one,

`boxed: ||p_(X^T A X)||_infinity <44.`                            (5.1)

The bound is independent of dimension, the number of coordinates in either bank, the split of the line-bank mass, the support shapes of the input laws, and the signs/orientation of the three eigenvalues of `B` subject only to their moduli being at least one.

**Proof.** If `|a|<=4/7`, use (3.7). If `|a|>4/7`, use (4.6). These cases are exhaustive. QED.

The proof establishes essential boundedness. It does not claim a continuous representative.

### Corollary 5.2 — distributed approximate coloop

Suppose a physical row has leverage `c in (1/2,1)` and the remaining `1-c` mass of that spectral direction is supported on original coordinates that carry no transverse spectral component, while all transverse spectral rows live on the complementary original-coordinate bank. Then (5.1) holds uniformly in `c`.

This is precisely the partner r21 approximate-coloop interpolation in the source-disjoint leakage subcase. It improves the preceding finite-line-bank bound because the transverse plane here may have arbitrarily many row directions.

## 6. Two equation-level applications of the required Claude package

### 6.1 Product marginal inserted into the curved receiver

The two-dimensional product-marginal estimate in Claude's Theorem C supplies (2.10), `M<=2`. Substituting that **actual product-projection cap** into the partner curved inequality (3.4), while retaining independence only between original banks, is the step that produces (3.6). The receiver coordinates remain dependent.

For signature `(2,1)`, Claude Theorem C also gives the sharper one-sided statement

`ess sup_(majority-sign levels) p_Q <= pi sqrt(2)`.                 (6.1)

Thus the new `<44` theorem is needed only to make the bank class two-sided; on the ruled one-sheet side (6.1) is stronger. The sign-reversed statement holds for signature `(1,2)`.

### 6.2 A real obstruction to volume-only decoupling

On the natural original-coordinate cut `I|J`, (2.5) gives

`A_IJ = (a_i)_(i in I) [e_1^T B R_J^T]`,                           (6.2)

so

`rank(A_IJ)<=1`.                                                    (6.3)

Therefore Claude Theorem D/D' has

`Z=e_3(A_IJ^T A_IJ)=0`,                                           (6.4)

and its five-volume extension also vanishes. Hence the completed volume route supplies no certificate on this cut, while aggregation of the line bank first gives `<44`. This is a concrete example of why product compression must precede reciprocal local-volume payment in a near-coloop branch.

## 7. Why the older disjoint-Pluecker certificate can blow while (5.1) stays fixed

Let `p_i=a_i^2` on the line bank, so `sum p_i=1`. Every nonzero rank-three Pluecker basis contains exactly one line-bank coordinate and two plane-bank coordinates. For two independent Pluecker bases to be disjoint, their line coordinates must be distinct. Consequently their disjoint mass satisfies the elementary upper bound

`D_disj <= P(line choices are distinct)
        =1-sum_i p_i^2`.                                          (7.1)

If one physical row has leverage `c=p_0 ->1`, then

`D_disj <=1-c^2 ->0`.                                             (7.2)

Thus any certificate proportional to `D_disj^(-1/6)` can diverge at the exact-coloop endpoint even though Theorem 5.1 remains below `44` for the entire path. The loss is a certificate artifact: sampling physical bases before grouping the line bank pays the tiny leakage separately.

## 8. Exact remaining gap

The new theorem requires the source partition (2.4). The genuinely unpaid approximate-coloop configuration is **overlapping leakage**: some original leaf coordinates carry both the residual heavy-direction component and transverse-plane components. Then the scalar projection and transverse pair are no longer source-disjoint, and neither their marginal density caps nor a conditional scalar cap may be promoted to independence. The live conditional-cap counterexample forbids that shortcut.

A useful next statement would be a grouped overlap transducer that keeps the common original-coordinate factors through the cross-transverse near-slope integral, or a structural alternative routing the overlap to a volume/mixed-Fresnel certificate. Arbitrary additional spectrum remains a separate full-target debt. No QFORM counterexample is produced here.

## 9. Source pins and review status

Control source at invocation start: `yspennstate/math-research-brain@1e5d04862685b227e6e7cae93d22347672011a70`, owner revision `2026-09-22.15`.

Required Claude baseline actually used: `yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`, files `RESULTS.md`, `FOURIER_ROUTE_REPORT.md`, `COUNTEREXAMPLE_SEARCH.md` under `proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/`.

Designated partner actually used: fleet03/B16 r21 at `yspennstate/math-open-problems@715e0a1445a9cd363b2793e6d982633fbc1c3362`.

The theorem is a new supporting argument from this slot and has not received an independent end-to-end review in this run. Full QFORM remains open.
