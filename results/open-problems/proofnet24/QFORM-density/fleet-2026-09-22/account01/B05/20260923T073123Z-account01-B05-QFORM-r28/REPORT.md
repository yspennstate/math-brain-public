SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B05, 2026-09-23T07:31:23Z.
attacking: the uncovered indefinite two-sheet curved integral; condition away genuinely mixed physical rows only when their spectral Gram mass is small, then use the completed support-separated heavy-row theorem on the surviving product frame.

# account01/B05 QFORM r28 — overlap-Gram conditioning exit for a heavy exact-rank-three row

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Assignment:** quadratic coarea bound / uncovered indefinite two-sheet curved integral.  
**Execution:** `WITHOUT_VERIFIED_BRAIN`.  
**Outcome:** `ESSENTIAL_STEP_APPLIED / SUPPORTING_STRUCTURAL_THEOREM_PROVED / PRECISE_REMAINING_FACTOR_IDENTIFIED`.  
**Full QFORM:** `OPEN_NOT_PROVED`.  
**Continuity:** `NOT_PROVED` for the full target; the theorem below proves an interval bound and hence an essentially bounded density in its exact scope.

## 1. Exact obligation attacked

The current B05 debt is the two-sheet / convex-side coarea geometry with original-coordinate product structure retained.  The previous B05 run showed that a bounded three-dimensional residual density, even together with all coordinate marginal caps, is insufficient: a reciprocal quadratic shear can straighten the two-sheet curvature and resurrect a logarithmic product singularity.  Thus a successful reduction must preserve the simultaneous linear-product provenance of the active projections.

The designated partner account02/B05 has now proved an exact endpoint with that provenance intact.  Its source is

`yspennstate/math-open-problems@ad7874e3ee0f4541714b2376aa09154517e60867`

`proofnet24/QFORM-density/fleet-2026-09-22/account02/B05/20260923T062009Z-account02-B05-QFORM-r23/REPORT.md`.

Its theorem `QFORM-HEAVY-ROW-SUPPORT-SEPARATED-CLOSURE-v1` says: for an exact-rank-three target `A=R Lambda R^T`, if a physical row has leverage at least `1/2` and, after aligning it with `e1`, every other physical row is either parallel to `e1` or orthogonal to `e1`, then for arbitrary independent cap-one input laws

`||p_(X^TAX)||_infinity < 248`.                                    (1.1)

The purpose of this run is to turn (1.1) into a quantitative exit when same-coordinate overlap is present but its **spectral Gram operator mass** is not too large.

## 2. Heavy-row coordinates and the exact overlap Gram

Let

`A = R Lambda R^T`, `R^T R=I_3`,                                   (2.1)

with `Lambda` real symmetric and

`min_k |lambda_k(Lambda)| >= 1`.                                   (2.2)

Assume a physical row `i` of `R` is heavy:

`c=||r_i||^2 > 1/2`.                                                (2.3)

Rotate only the deterministic three-dimensional active basis so that

`r_i = sqrt(c) e1`.                                                  (2.4)

For `j!=i`, write uniquely

`r_j = u_j e1 + v_j`, `v_j in e1^perp`.                             (2.5)

Define the genuinely mixed support

`H={j!=i: u_j!=0 and v_j!=0}`                                      (2.6)

and its positive-semidefinite spectral Gram matrix

`K_H = sum_(j in H) r_j r_j^T`,
`kappa = ||K_H||_op`.                                                (2.7)

The point of (2.7) is that it measures the amount of the three-dimensional active frame carried by coordinates that simultaneously contain longitudinal and transverse coefficients.  It does **not** use moments or the sizes of the random variables.

## 3. Main theorem

### Theorem 3.1 — `QFORM-HEAVY-ROW-OVERLAP-GRAM-EXIT-v1`

Under (2.1)--(2.7), if `kappa<1`, then for every independent real input vector whose coordinate densities are bounded by one,

`boxed:  ||p_(X^TAX)||_infinity < 248/(1-kappa).`                   (3.1)

Equivalently, every interval `J` satisfies

`P(X^TAX in J) < [248/(1-kappa)] |J|`.                              (3.2)

In particular,

`boxed: kappa<=1/2  ==>  ||p_(X^TAX)||_infinity <496.`              (3.3)

No compact-support, moment, log-concavity, connected-support, Gaussian or post-rotation independence assumption is used.

### Proof

Condition on all original coordinates `X_H`.  This is legitimate product conditioning: the unconditioned coordinates remain independent and retain their original density caps.

Let `U=H^c` denote the unconditioned coordinates (including the heavy coordinate `i`) and set

`G = sum_(j in U) r_j r_j^T = I_3-K_H`.                              (3.4)

Every unconditioned residual row is now either purely longitudinal (`v_j=0`) or purely transverse (`u_j=0`).  Hence relative to

`R e1 direct_sum e1^perp`,

`G` is block diagonal.                                               (3.5)

Moreover `K_H` is positive semidefinite and `||K_H||op=kappa`, so

`G >= (1-kappa) I_3`.                                                (3.6)

In particular `G` is invertible.  Whiten the deterministic surviving frame by

`R_tilde = R_U G^(-1/2)`.                                           (3.7)

Then

`R_tilde^T R_tilde = I_3`.                                          (3.8)

Because `G^(-1/2)` is block diagonal by (3.5), (3.7) preserves the exact support separation: each surviving residual row is still parallel or orthogonal to `e1`.

Write `g11=e1^T G e1`.  The heavy row of the whitened frame is

`r_tilde_i = sqrt(c/g11)e1`.                                        (3.9)

Since `G<=I`, `g11<=1`, and therefore

`||r_tilde_i||^2 = c/g11 >= c >1/2`.                               (3.10)

(The Parseval identity (3.8) also gives `c/g11<=1` automatically.)

The conditioned quadratic core on the unconditioned coordinates is

`R_U Lambda R_U^T
 = R_tilde M R_tilde^T`,
`M=G^(1/2) Lambda G^(1/2)`.                                         (3.11)

For arbitrary matrices, `s_min(ABC)>=s_min(A)s_min(B)s_min(C)`.  Hence from (2.2) and (3.6),

`s_min(M)
 >= s_min(G^(1/2))^2 s_min(Lambda)
 >= 1-kappa`.                                                        (3.12)

Since `M` is symmetric, every eigenvalue of `M` has absolute value at least `1-kappa`.

Conditioning `X_H=h` creates a linear term in the surviving variables, but crucially it lies in the same active three-dimensional range.  Indeed

`2 A_(U,H) h
 =2 R_U Lambda R_H^T h
 =2 R_tilde b_h`,
`b_h=G^(1/2)Lambda R_H^T h`.                                        (3.13)

Thus, if `Y=R_tilde^T X_U`, the conditional form has the shape

`Y^T M Y +2 b_h^T Y+d_h`.                                           (3.14)

Because `M` is invertible, complete the square:

`Y^T M Y+2b_h^T Y+d_h
 =(Y+M^(-1)b_h)^T M (Y+M^(-1)b_h)+d'_h`.                            (3.15)

The support-separated frame decomposes `Y` exactly as the partner theorem requires: one scalar variable from the longitudinal original-coordinate bank, independent of the dependent two-dimensional projection of the disjoint transverse bank.  The deterministic translation in (3.15) preserves that scalar-versus-pair independence and all scalar/pair density caps.  Thus the partner theorem (1.1), applied to

`M/(1-kappa)`,                                                       (3.16)

and then rescaled back in the output, gives for every `h`

`P(Q in J | X_H=h)
 < 248 |J|/(1-kappa).                                                (3.17)

The constant is uniform in `h`; averaging (3.17) over the conditioned product coordinates proves (3.2), hence (3.1).  QED.

### Affine-stability audit of the partner input

The partner statement is written for the homogeneous form, but (3.15) does not add a new analytic hypothesis.  Its proof uses only: (i) the scalar density cap and scalar-versus-pair independence, (ii) a joint density cap for the transverse pair, and (iii) the active coefficient matrix.  Translating the scalar and pair by deterministic constants preserves (i)--(ii).  In its square-peel branch the residual two-dimensional affine term is exactly the in-range affine term covered by the source rank-two half-Riesz theorem

`yspennstate/math-open-problems@e542b1a6ef471b329e4e88a6553e1aacb45acc1a`

`proofnet24/QFORM-density/interactive/20260922T161801Z-rank-two-fusion/REPORT.md`,

whose sharper in-range estimate is

`sup_t E |Y^T S Y+b^T Y-t|^(-1/2)
 <=16 sqrt(30)|det S|^(-1/4)`.                                     (3.18)

In the partner's scalar/dependent-pair branches, deterministic translation of the scalar and of the pair leaves the hypotheses of `QFORM-NEARNULL-SCALAR-DEPENDENT-PAIR-v1` unchanged.  Therefore the conditional affine term in (3.13) is genuinely paid rather than silently discarded.

## 4. A sharper structural description of every survivor

The support separation of the surviving rows has an additional consequence.  Since `G` is block diagonal and `I_3` is block diagonal,

`K_H=I_3-G` is block diagonal as well.                               (4.1)

Expanding its two diagonal blocks gives

`K_H = [ sum_(j in H) u_j^2 ] e1e1^T
        direct_sum
        [ sum_(j in H) v_j v_j^T ].`                                (4.2)

The total longitudinal residual Parseval mass is

`sum_(j!=i) u_j^2 =1-c <1/2`,                                      (4.3)

so in particular

`sum_(j in H)u_j^2 <1/2`.                                           (4.4)

Consequently (4.2) implies the exact dichotomy

`kappa<=1/2`

or

`boxed: ||sum_(j in H) v_j v_j^T||op >1/2.`                         (4.5)

Thus after Theorem 3.1 the only heavy-row exact-rank-three survivor has a transverse unit direction `w in e1^perp` for which

`sum_(j in H) (v_j dot w)^2 >1/2`.                                  (4.6)

In words: **more than half of one transverse spectral direction is carried by physical coordinates that also contain a nonzero longitudinal coefficient.**

This is stronger and more precise than the previous overlap currency

`Omega=sum |u_j| ||v_j||`.                                          (4.7)

Indeed (4.6) can hold while `Omega` is arbitrarily small: distribute order-one transverse Parseval mass over many rows and give each such row an arbitrarily small but nonzero longitudinal coefficient, with the required signed cross cancellations.  Therefore the remaining two-sheet obstruction is not controlled by coefficient-size perturbation.  What matters is **hard support incidence of infinitesimal overlaps**.

## 5. Required newest-Claude result applied at an actual inequality

The required newest source

`yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`

`proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/COUNTEREXAMPLE_SEARCH.md`

proves its Theorem C: for every exact-rank-three signature `(+,+,-)` form with active eigenvalue magnitudes at least one, the majority-sign one-sheet half-line satisfies

`boxed: p_Q(s) <= pi sqrt(2),  s>=0.`                               (5.1)

Hence in the indefinite exact-rank-three branch, (5.1) already pays the one-sheet side independently of Theorem 3.1.  The new overlap-Gram exit is useful precisely on the remaining full-line/two-sheet side: whenever `kappa<=1/2`, that unpaid side is now bounded by `<496`; a true survivor must satisfy (4.6).  This is an equation-level application of the newest source, not a reproof of its ruled geometry.

## 6. Designated partner result applied at the decisive inequality

The completed account02/B05 r23 theorem is used exactly at (3.17), after a product-valid conditioning and deterministic frame normalization.  The chain is

`G=I-K_H >=(1-kappa)I`

`=> s_min(M)>=1-kappa`

`=> ||p_(Q | X_H=h)||infinity <248/(1-kappa)`

`=> boxed: ||p_Q||infinity <248/(1-kappa).`                         (6.1)

This is the requested actual application of the designated partner result.  No conclusion is transferred merely from a citation.

## 7. First unpaid implication after this run

The remaining exact-rank-three heavy-row two-sheet state is now

`QFORM-INFINITESIMAL-OVERLAP-SUPPORT-STABLE-TWOSHEET-v1`:

> Assume a heavy row `c>1/2`, and after alignment let `H` be the same-coordinate mixed support.  The only survivor of the overlap-Gram conditioning exit has
>
> `||sum_(j in H) v_j v_j^T||op>1/2`
>
> while the longitudinal mixed mass is `<1/2` and may be arbitrarily small coefficient-by-coefficient.  Prove a full-line interval/coarea bound using the original product factorization that is stable when the nonzero `u_j` on this transverse-majority support tend to zero, without conditioning those coordinates away and without treating their random contribution as a small perturbation.

This is the exact transition that the previous hidden-shear falsifier says must retain product-linear provenance.  It is also genuinely different from the `Omega=0` support-separated endpoint: a vanishing sequence of nonzero longitudinal coefficients can carry an order-one transverse Gram direction and therefore cannot be deleted by a coefficient-norm argument under arbitrary unbounded input laws.

A plausible next mechanism is a product-coordinate Carleson estimate for the reciprocal-shear transform in which the longitudinal coefficients enter only through the selector/root geometry, not through moments of the variables.  Any proof that first relaxes the mixed block to an arbitrary bounded joint density is ruled out by the previous B05 correction.

## 8. Scope and integrity

- Theorem 3.1 is an exact-rank-three supporting theorem, not the full arbitrary-rank QFORM theorem.
- It proves an essentially bounded density in its scope; it does not establish continuity.
- It conditions only original independent coordinates and never asserts independence after a spectral rotation.
- It does not use a generic arbitrary-joint coarea lemma, a worst conditional-density supremum, or a small-random-perturbation step.
- It retains all signs of the active matrix; Theorem C is invoked only for its stated indefinite one-sheet scope.
- Full QFORM remains open and still requires two independent complete reviews of any eventual end-to-end candidate.
