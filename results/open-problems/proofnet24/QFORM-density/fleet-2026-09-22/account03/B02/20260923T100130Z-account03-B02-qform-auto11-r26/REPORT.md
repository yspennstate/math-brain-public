SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account 03, slot B02, 2026-09-23T10:01:30Z.
attacking: the heavy mixed-marginal Schur/star residue by an integrated Fourier estimate that spends Frobenius/second-compound mass without selecting a tiny individual minor.

# account03/B02 r26 — Gibbs-balanced disjoint-volume mixed Fourier compiler

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Assignment:** Integrated Fourier estimate  
**Fresh owner control:** revision `2026-09-22.15`; QFORM only  
**Execution:** `WITHOUT_VERIFIED_BRAIN`; `full_brain_connected=false`  
**Full QFORM target:** OPEN  
**Target-wide universal unweighted Fourier L1 criterion:** OPEN; neither proved nor refuted here  
**Continuity:** proved on the new branch because the characteristic function is genuinely in `L1`; full-target continuity remains OPEN.

## 1. Source-pinned inputs and correction boundary

The exact target remains arbitrary independent ORIGINAL real coordinates with one-dimensional probability densities bounded by one, arbitrary real symmetric `A`, and at least three eigenvalues of modulus at least one. Nothing below assumes Gaussianity, moments, log-concavity, bounded/connected support, identical laws, or independence after rotating coordinates.


The main analytic source is this slot's completed weighted mixed theorem

`QFORM-WEIGHTED-MIXED32-FOURIER-L1-v1`,

`yspennstate/math-open-problems@06f29f974c0e593ff6579199610ee2cc91c60115`,

`proofnet24/QFORM-density/fleet-2026-09-22/account03/B02/20260923T085705Z-account03-B02-qform-r25/REPORT.md`.

The new argument below changes its input from the canonical squared-minor laws to entropy-optimal disjoint-conditioned laws. The fresh complementary account02/B02 theorem used for comparison is

`QFORM-EDGE-E2-CROSSDISJOINT-SHARP-HY-L1-v1`,

`yspennstate/math-open-problems@3fbf0b3009498afa3985581e320f39df73b085af`,

`proofnet24/QFORM-density/fleet-2026-09-22/account02/B02/account02-B02-20260923T071011Z-3508bbe2/REPORT.md`.

Its disjointness is *cross-family* between two residual 2-minor laws. The theorem below uses *within-family* iid disjointness, separately for the incident 3-minor law and residual 2-minor law. The two criteria and their failure certificates are therefore genuinely different.

The designated completed partner is account04/B02

`QFORM-ZERO-DIAGONAL-TRIPLE-CONTINUITY-v1`,

`yspennstate/math-open-problems@0b11995430ce407a8852ac3bc5651491f2ee64f7`,

`proofnet24/QFORM-density/fleet-2026-09-22/account04/B02/20260922T193108Z-account04-B02-QFORM-r2/REPORT.md`.

Its `L2` Fourier estimate is applied in Section 7 to a new hybrid inequality.

## 2. Physical mixed-volume setup

Let `I,J` be disjoint ORIGINAL-coordinate banks and let

`B=A[I,J]`.

All same-bank quadratic terms, outside couplings, affine terms and extra spectrum are arbitrary. Fix an actual anchor row `x in I` and anchor column `y in J`.

Let `M3` be the family of nonzero physical `3 x 3` minors `B[S,T]` with `x in S`, `y in T`. Let

`J3 = sum_(S,T in M3) det(B[S,T])^2 >0`.                         (2.1)

Let

`N=B[I\{x},J\{y}]`,

and let `M2` be the nonzero physical `2 x 2` minors of `N`, with

`E2 = sum_(R,U in M2) det(N[R,U])^2 >0`.                         (2.2)

The canonical determinant laws are

`nu3(S,T)=det(B[S,T])^2/J3`,
`nu2(R,U)=det(N[R,U])^2/E2`.                                    (2.3)

For a probability law `mu` on one of these finite minor families define its entropy-weighted determinant volume

`G(mu)=exp(H(mu)+E_mu log(det^2))`.                              (2.4)

Zero determinant terms are simply omitted from the support.

## 3. Weighted mixed theorem for arbitrary minor laws

The r25 proof was written for the canonical normalized squared-minor laws. The determinant calculation actually has the following stronger form.

### Lemma 3.1 — `QFORM-WEIGHTED-MIXED32-ARBITRARY-LAWS-v1`

Let `mu3` be any probability law on `M3`, and `mu2` any probability law on `M2`. Let `alpha^(3),beta^(3)` and `alpha^(2),beta^(2)` be their physical row/column inclusion marginals, extending the `mu2` anchor marginals by zero. For `0<theta<1`, put

`alpha=theta alpha^(3)+(1-theta)alpha^(2)`,
`beta =theta beta^(3) +(1-theta)beta^(2)`.                       (3.1)

Then `sum alpha=sum beta=2+theta`, and the anchor marginals are exactly `theta`.

For every

`1 <= q < (2+theta)/2`,                                         (3.2)

if every mixed row marginal obeys

`alpha_i <= q/2`,                                                (3.3)

then the full ambient quadratic form has an `L1` characteristic function, a continuous density vanishing at infinity, and

`boxed:
 ||p_Q||_infinity
 <= C(theta,q)
    G(mu3)^[-theta/(2(2+theta))]
    G(mu2)^[-(1-theta)/(2(2+theta))],
`                                                                    (3.4)

where

`C(theta,q)
 = e(2+theta)/[(2+theta-2q)sqrt(q)]
   [theta^theta(1-theta)^(1-theta)]^[1/(2(2+theta))].`          (3.5)

The same statement holds if (3.3) is imposed on all mixed COLUMN marginals instead.

### Proof

In the exact diagonal-plus-PSD determinant expansion used in r25, retain the incident `3 x 3` basis family `A3` and residual `2 x 2` basis family `A2`. Weighted AM-GM with an *arbitrary* law gives

`A3 >= G(mu3)
       prod_i d_i^(alpha_i^(3))
       prod_j e_j^(1-beta_j^(3)),`                               (3.6)

`A2 >= G(mu2)
       prod_i d_i^(alpha_i^(2))
       prod_j e_j^(1-beta_j^(2)).`                               (3.7)

This is immediate from

`sum_a z_a >= exp(H(mu)) prod_a z_a^(mu_a)`                     (3.8)

applied to the positive determinant terms `z_a`; the entropy is exactly what replaces the canonical total-volume identity.

Weighted AM-GM between (3.6) and (3.7) gives

`det(D_J+B^T D_I B)
 >= C_theta G(mu3)^theta G(mu2)^(1-theta)
    prod_i d_i^alpha_i prod_j e_j^(1-beta_j),`                  (3.9)

where

`C_theta=theta^(-theta)(1-theta)^(-(1-theta)).`                 (3.10)

The remainder of the r25 proof is unchanged: one-sided ORIGINAL-coordinate Weyl differencing removes same-bank phases only after the legitimate Cauchy--Schwarz step; Lieb's Gaussian Brascamp--Lieb formula uses (3.9); sharp Hausdorff--Young at output exponent `q/alpha_i>=2` is valid under (3.3); the alpha powers cancel; and the row/column entropy factors are bounded by `exp((2+theta)/2)`. The result is

`|phi_Q(t)| <= min(1,K |t|^[-(2+theta)/(2q)])`,                 (3.11)

with the coefficient obtained from r25 after replacing `J3^theta E2^(1-theta)` by `G(mu3)^theta G(mu2)^(1-theta)`. Since (3.2) makes the exponent strictly larger than one, direct integration and Fourier inversion give (3.4)-(3.5). No new conditional density or rotated independence claim is introduced. QED.

At the value used below,

`theta=1/2`, `q=1`,                                               (3.12)

this becomes

`boxed:
 ||p_Q||_infinity
 <= C0 [G(mu3)G(mu2)]^(-1/10),
 C0=5e/2^(1/5)=11.832008884813... .
}`                                                                    (3.13)

Moreover the actual pointwise tail produced by the proof is

`|phi_Q(t)|
 <= min{1,
 2^(-1/4)e^(5/4)pi^(5/4)
 [G(mu3)G(mu2)]^(-1/8)|t|^(-5/4)}.`                             (3.14)

Equation (3.14) is a branch-specific product-space estimate, not the refuted law-uniform scalar van-der-Corput bound.

## 4. Gibbs balancing from within-family disjointness

The new mechanism is an entropy statement which converts a disjointness probability into a marginal gate without selecting any one determinant.

### Lemma 4.1 — `QFORM-DISJOINT-GIBBS-BALANCING-v1`

Let `Omega` be a finite family of physical `k`-row supports, with positive weights `a_omega`, total

`Z=sum_omega a_omega`,

and canonical law `nu_omega=a_omega/Z`. Draw two iid samples `S,S'~nu`, and put

`rho=P(S cap S'=empty)`.                                         (4.1)

If `rho>0`, there is a probability law `mu` on the same weighted support satisfying

`max_i P_mu(i in S) <=1/2`,                                     (4.2)

and

`boxed: G(mu)>= Z sqrt(rho).`                                   (4.3)

Here `G(mu)=exp(H(mu)+E_mu log a_S)`.

### Proof

Condition the iid pair `(S,S')` on the symmetric event `S cap S'=empty`; call the resulting joint law `pi`. By symmetry its two marginals are the same law `mu`. Since the two sets are disjoint under `pi`, for every physical coordinate `i`,

`2 P_mu(i in S)
 =P_pi(i in S)+P_pi(i in S')
 =P_pi(i in S union S') <=1`,                                   (4.4)

which proves (4.2).

The conditional law satisfies

`D(pi || nu tensor nu)=log(1/rho)`.                              (4.5)

By the chain rule for relative entropy,

`D(pi || nu tensor nu)
 = I_pi(S;S') +2 D(mu||nu)
 >=2 D(mu||nu)`.                                                 (4.6)

Therefore

`D(mu||nu)<= (1/2)log(1/rho)`.                                  (4.7)

Finally, because `nu_S=a_S/Z`,

`D(mu||nu)
 = log Z - H(mu)-E_mu log a_S
 = log[Z/G(mu)].`                                                (4.8)

Combining (4.7)-(4.8) proves (4.3). QED.

This argument is exact. It is a finite-dimensional Gibbs/relative-entropy identity, not a numerical or probabilistic heuristic.

## 5. Main new integrated-Fourier theorem

Let

`rho_3^r = P_(nu3 tensor nu3)(S cap S'=empty)`,
`rho_2^r = P_(nu2 tensor nu2)(R cap R'=empty)`                   (5.1)

be the within-family ROW-disjointness probabilities. Define the analogous COLUMN probabilities `rho_3^c,rho_2^c`.

### Theorem 5.1 — `QFORM-MIXED32-WITHIN-DISJOINT-GIBBS-L1-v1`

If

`rho_3^r rho_2^r >0`,                                            (5.2)

then the full ambient quadratic form has a continuous density vanishing at infinity and

`boxed:
 integral_R |phi_Q(t)| dt
 <= [10 pi e/2^(1/5)]
    (J3 E2)^(-1/10)
    (rho_3^r rho_2^r)^(-1/20),
}`                                                                    (5.3)

hence

`boxed:
 ||p_Q||_infinity
 <= [5e/2^(1/5)]
    (J3 E2)^(-1/10)
    (rho_3^r rho_2^r)^(-1/20).
}`                                                                    (5.4)

The identical statements hold with the COLUMN disjointness product `rho_3^c rho_2^c`.

### Proof

Apply Lemma 4.1 separately to the incident three-minor law and the residual two-minor law. This produces laws `mu3,mu2` whose row marginals are all at most `1/2`, while

`G(mu3)>=J3 sqrt(rho_3^r)`,
`G(mu2)>=E2 sqrt(rho_2^r)`.                                     (5.5)

At `theta=1/2`, the mixed anchor marginal is exactly `1/2`; every non-anchor mixed marginal is an average of two numbers at most `1/2`. Thus the `q=1` gate in Lemma 3.1 holds. Apply (3.13), then use (5.5):

`[G(mu3)G(mu2)]^(-1/10)
 <=(J3E2)^(-1/10)(rho_3^r rho_2^r)^(-1/20).`                    (5.6)

The `L1` estimate (5.3) is the corresponding pre-inversion bound. QED.

This is useful precisely when the canonical mixed marginals of r25 are heavy but determinant weight is still spread over disjoint supports. Instead of discarding that state as a marginal failure, one conditions the determinant Gibbs laws on disjointness and pays only the twentieth root of the disjointness probability.

### Uniform threshold form

If, for some `eta in (0,1]`,

`rho_3^r>=eta`, `rho_2^r>=eta`,                                  (5.7)

then

`||p_Q||_infinity
 <=11.832009 eta^(-1/10)(J3E2)^(-1/10).`                        (5.8)

At `eta=1/16`,

`boxed:
 ||p_Q||_infinity
 <15.612430 (J3E2)^(-1/10).
}`                                                                    (5.9)

This is a continuous-density exit.

## 6. Exact structural complement: a small physical transversal

The new Fourier theorem has a compact failure certificate, which is the main structural gain over another abstract marginal obstruction.

### Lemma 6.1 — low disjointness forces a determinant hub

Let a canonical determinant law `nu` be supported on physical `k`-sets and let `rho=P(S cap S'=empty)`. For every `eta>0`, if

`rho<eta`,                                                        (6.1)

there is an actual support set `H`, `|H|=k`, such that

`P_nu(S cap H !=empty)>1-eta`.                                  (6.2)

Proof: `rho=E_H P(S cap H=empty | H)`, so at least one realized support set has conditional disjoint mass at most `rho`. QED.

Consequently, if the `eta`-version of Theorem 5.1 fails on the row side, then at least one of the following is present:

- a fixed physical **three-row** set meeting more than `1-eta` of the incident third determinant weight;
- a fixed physical **two-row** set meeting more than `1-eta` of the residual second determinant weight.                     (6.3)

If the column version also fails, the analogous fixed three-/two-column determinant hub is present. Thus simultaneous Fourier failure compresses the remaining support geometry to at most three physical coordinates on each failed side before any reciprocal minor is paid.

At the exact residual endpoint `rho_2^r=0`, the row supports of all nonzero residual `2 x 2` minors are pairwise intersecting. Every pairwise-intersecting family of two-element sets is either

1. a star: all supports contain one fixed physical row; or
2. a triangle: every support is contained in one fixed three-row set.  (6.4)

Indeed, take two distinct supports `{a,b}` and `{a,c}`. Any support not containing `a` must be `{b,c}`. If `{b,c}` occurs, no support `{a,d}` with `d` outside `{b,c}` can remain intersecting; otherwise all supports contain `a`.

This gives a finite exact endpoint for the residual-E2 failure state rather than an unspecified concentration phenomenon.

## 7. Designated account04/B02 theorem applied to an actual new inequality

Suppose, in addition to the row-disjointness branch of Theorem 5.1, that the full form contains a nonsingular physical `3 x 3` principal block `H0` with an exact zero diagonal entry. The designated account04/B02 theorem gives

`L:=||phi_Q||_2^2
 <=6 pi 2^(2/3)|det H0|^(-1/3).`                                (7.1)

From (3.14) and the Gibbs credit (5.5), the new high-frequency tail is

`|phi_Q(t)|
 <=K |t|^(-5/4),`                                                (7.2)

where

`K=2^(-1/4)e^(5/4)pi^(5/4)
   (J3E2)^(-1/8)
   (rho_3^r rho_2^r)^(-1/16).`                                  (7.3)

For every `T>0`, Cauchy--Schwarz on the low-frequency interval and (7.2) on the tail give

`||phi_Q||_1
 <=sqrt(2LT)+8K T^(-1/4).`                                      (7.4)

The exact minimizer satisfies

`T=[8K/(2sqrt(2L))]^(4/3)`,                                     (7.5)

and substitution yields

`||phi_Q||_1
 <=6sqrt(2) L^(1/6)K^(2/3).`                                   (7.6)

Fourier inversion and (7.1)-(7.3) therefore give the genuine partner-hybrid estimate

`boxed:
 ||p_Q||_infinity
 <= C_hyb |det H0|^(-1/18)
    (J3E2)^(-1/12)
    (rho_3^r rho_2^r)^(-1/24),
}`                                                                    (7.7)

with the exact constant

`C_hyb=2^(11/18) 3^(7/6) e^(5/6)
      =12.662408123937... .`                                     (7.8)

At the clean threshold `rho_3^r,rho_2^r>=1/16`, this is

`boxed:
 ||p_Q||_infinity
 <15.953635 |det H0|^(-1/18)(J3E2)^(-1/12).
}`                                                                    (7.9)

This is an equation-level application of the designated completed partner theorem, not a citation-only mention. The overlap has a continuous density because Theorem 5.1 already gives `phi_Q in L1`.

## 8. Relation to fresh fleet geometry

Fresh account03/B07 r31 proves a dimension-free disjointness lower bound `rho>=1/2` for a physically diffuse, strongly transverse two-frame Pluecker law. Whenever such a two-frame is the residual exact-rank-two determinant law entering `E2`, it supplies the `rho_2>=1/2` half of Theorem 5.1 automatically. The remaining question is then the incident-three disjointness. If that is at least `eta`, Theorem 5.1 is a continuous-density exit; if not, Lemma 6.1 produces a fixed three-row incident-volume hub. Thus the diffuse two-star route and the mixed-volume Fourier route now meet at a concrete invariant rather than at an unspecified marginal gate.

The fresh account02/B04 base-packing theorem gives a compatible support interpretation: its `q=1` third-volume gate is equivalent to two disjoint row bases. The Gibbs lemma above is the quantitative determinant-weighted version: it does not merely ask whether a disjoint pair exists; it charges exactly the relative-entropy cost of conditioning the canonical determinant law on such a pair.

## 9. Deterministic computation check

A seeded finite check sampled 500 random positive weight systems on all 2-subsets of 8 coordinates and 500 on all 3-subsets of 9 coordinates. For each system it formed the iid law, conditioned exactly on disjointness, computed the marginal `mu`, and checked both

`max_i mu(i in S)<=1/2`,
`G(mu)/(Z sqrt(rho))>=1`.

Observed worst ratios were

- `k=2`: `1.2729937409535`, maximum inclusion `0.46684832499996`;
- `k=3`: `1.8630337382774`, maximum inclusion `0.43983268084876`.

The constants were independently evaluated as

`C0=11.832008884813`,
`C_hyb=12.662408123937`,
`C0*(1/16)^(-1/10)=15.612429323846`,
`C_hyb*(1/16)^(-1/12)=15.953634537708`.

These computations are only regression checks; Sections 3-7 are the proof.

## 10. What is and is not solved

The full universal QFORM conjecture remains **OPEN**. This run does not show that the bare three-large-eigenvalue hypothesis forces `J3E2` or the within-family disjointness probabilities to be bounded below at a universal scale. It also does not produce a target-valid counterexample to the stronger global criterion `integral |phi_Q|<infinity`; that full-target criterion remains neither proved nor refuted.

What is new is the first missing implication inside the current mixed-volume route:

> canonical heavy marginals do not themselves block the integrated Fourier argument. If determinant weight can be paired disjointly *within each volume family*, relative-entropy conditioning manufactures balanced minor laws and restores the `q=1`, `|t|^(-5/4)` tail with only a twentieth-root disjointness cost. Failure yields a fixed 2- or 3-coordinate determinant transversal.

The next B02 debt is therefore sharply finite: combine the row/column 2-/3-coordinate transversals from Lemma 6.1 with the existing edge/Schur, two-star, zero-diagonal-triple, fresh-square and grouped-bank receivers, or prove a lower bound on one of the within-family disjointness products from the remaining spectral/compound-volume currency. No new task or easy subclass is substituted for the full target.
