# fleet02/B13 auto11 — spectral pruning removes the small-pdet exit

Status: proved addendum to `REPORT.md`; full QFORM remains OPEN. The source status of the fleet03/B13 r30 decomposition is unchanged: it inherits the stated grouped-projected-crossing dependency.

## 1. Why prune

The main report left, in the diffuse rank-`>=3` branch, a possible escape through a very small determinant scale

`Lambda_R=|pdet R|^(1/rank R)`.

Because the latest partner already gives `rank R<=8`, that escape can be removed without deleting any quadratic term: move only eigencomponents below a slab-dependent spectral threshold into the genuine residual and charge their whole Frobenius norm.

## 2. Exact finite-rank spectral pruning

Start from

`A=D+R+E`, `rank R<=8`, `||E||F<=K/rho`,                           (2.1)

where `K=K0=72(9sqrt(3e))^3` in the generic r30 branch and `K=6` in its sharper Case B.

Fix `c>0` and set

`tau=c/rho`.

Because `R` is symmetric, write

`R=R_hi+R_lo`,                                                     (2.2)

where `R_hi` is the sum of eigendirections with `|lambda|>tau` and `R_lo` the sum of the remaining nonzero eigendirections. Put

`E_c=E+R_lo`.                                                      (2.3)

This is an **identity of the coefficient matrix**, not a perturbative deletion:

`boxed: A=D+R_hi+E_c.`                                             (2.4)

Since `rank R<=8`,

`||R_lo||F <= sqrt(8) tau`,                                       (2.5)

and therefore

`boxed:
 ||E_c||F <= (K+c sqrt(8))/rho.
}`                                                                  (2.6)

No support or moment enters.

If `d_c=rank R_hi>=1`, every nonzero eigenvalue of `R_hi` has magnitude `>c/rho`, hence

`boxed:
 Lambda_c:=|pdet R_hi|^(1/d_c) > c/rho.
}`                                                                  (2.7)

Also `range(R_hi) subset range(R)`, so its range projection satisfies

`P_(R_hi) <= P_R`                                                  (2.8)

in Loewner order. Thus any diffuse leverage gate enjoyed by `R` is inherited by `R_hi`. More importantly, even when the original `R` was not diffuse, one can simply test the leverage gate on the pruned range itself.

## 3. Choose the canonical threshold c=48

Take

`c=48`.                                                           (3.1)

Then

`K_48=K+48 sqrt(8)`.                                               (3.2)

If `d_48>=3` and

`max_j(P_(R_hi))jj<=1/2`,                                         (3.3)

the source-proved diffuse range-curvature theorem applies to the exact base `D+R_hi` with

`M_hi <= 12/Lambda_48 < rho/4`,                                   (3.4)

because `rho Lambda_48>48`.

Apply `QFORM-AFFINE-UNIFORM-RESIDUAL-PAIR-COUNT-v1` from the main report with residual `E_48`. For a slab `J` of length `L`, conditional on two independent copies both lying in the slab,

`Delta_(E_48,1/2)
 >= (L/2)(rho/(2M_hi)-1)
 >= (L/2)(rho Lambda_48/24-1).`                                   (3.5)

Since `rho Lambda_48>48`,

`rho Lambda_48/24-1 > rho Lambda_48/48`.                           (3.6)

On the other hand

`|y^T E_48 y| <= ||E_48||F ||y||2^2
                <= (K_48/rho)||y||2^2`.                            (3.7)

Hence the median slab-pair distance satisfies

`boxed:
 median(||X-X'||2 | both in slab)/sqrt(L)
 > rho sqrt( Lambda_48/(96 K_48) )
 > sqrt( rho/(2 K_48) ).
}`                                                                  (3.8)

The second inequality uses `Lambda_48>48/rho` and is the useful new point: **after pruning, the diffuse rank-at-least-three branch forces a scale-normalized Euclidean pair separation diverging at least like sqrt(rho), with no lower bound on the original pdet.**

Numerically,

`K_48 = 1,222,452.1388621256...` in the generic partner branch, so

`median distance/sqrt(L) > 0.0006395419986... sqrt(rho)`.          (3.9)

In the partner's sharper Case B,

`K_48 = 6+48sqrt(8)=141.764501987817...`,                          (3.10)

and therefore

`median distance/sqrt(L) > 0.0593883492536... sqrt(rho)`.          (3.11)

These constants are not claimed sharp.

## 4. High-leverage complement becomes a physical range-volume star

If `d_48>=3` but (3.3) fails, the fleet01/B13 range-volume identity gives a physical coordinate `j_*` for which more than half of the complete squared `d_48`-coordinate volume of `range(R_hi)` lies on subsets containing `j_*`.

Concretely, let `U` be any `d_48 x n` matrix with orthonormal rows spanning `range(R_hi)`. Then

`sum_(|I|=d_48) det(U[:,I])^2=1`,                                 (4.1)

and the exact leverage identity says

`sum_(I contains j_*) det(U[:,I])^2=(P_(R_hi))_(j_*j_*)>1/2`.      (4.2)

Thus the non-diffuse escape is not an abstract spectral orientation: it is a **single original physical coordinate volume star**.

No coefficient minor is inverted in (4.2), and no independence is asserted after choosing the deterministic range basis.

## 5. Pruned trichotomy

### Theorem 5.1 — `QFORM-RANK8-SPECTRAL-PRUNING-TRICHOTOMY-v1`

Subject to the latest partner r30 decomposition, every sufficiently high-ratio witness admits the exact decomposition

`A=D+R_hi+E_48`,
`||E_48||F <= (K+48sqrt(8))/rho`,                                 (5.1)

where every nonzero eigenvalue of `R_hi` has magnitude `>48/rho`, and at least one of the following holds:

1. `rank R_hi<=2`;
2. `rank R_hi>=3` and one original physical coordinate carries more than half of the complete range-volume currency as in (4.2);
3. `rank R_hi>=3`, the range is diffuse, and the actual slab satisfies the residual-energy bound (3.5) and the scale-free pair separation (3.8).

Therefore the `Lambda_R=O(rho^-1)` exit in the main report is not a separate obstruction. Small eigencomponents can be retained exactly inside the Frobenius residual at only an `O(rho^-1)` cost because there are at most eight of them.

## 6. Updated first unpaid implication

The first unpaid implication is sharpened to

`QFORM-PRUNED-RANK2-OR-VOLUMESTAR-OR-FRAGMENTATION-GLUE-v1`:

> Starting from Theorem 5.1 and the pinned global fifth-volume collapse, pay either the rank-at-most-two retained model or the single physical high-leverage range-volume star; in the diffuse branch, turn the forced `Omega(sqrt(rho))` scale-normalized pair separation in the actual residual energy into a product-geometric contradiction without a support-diameter/fragment-count hypothesis. Otherwise construct a genuine bounded-finite-union product-indicator counterexample sequence satisfying all three constraints.

This is strictly narrower than the unpruned `QFORM-SCALEFREE-FROBENIUS-TWIST-GLUE-v1`: small pdet is no longer a separate branch.
