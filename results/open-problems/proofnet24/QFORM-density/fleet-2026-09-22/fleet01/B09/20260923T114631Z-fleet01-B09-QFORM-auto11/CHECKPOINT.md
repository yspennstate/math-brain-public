SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet01, slot B09, 2026-09-23T11:46:31Z.
attacking: the near-coloop two-hub survivor with arbitrary leaf-bank curvature; convert transverse within-bank curvature into a literal rank-three original-coordinate cross volume, leaving only an aligned diagonal-plus-slope-span endpoint.

# Early substantive checkpoint

Status: supporting structural/analytic reduction; FULL QFORM remains OPEN.

Let `H={h1,h2}` be two literal physical hub coordinates and `I` a disjoint leaf bank. Write the actual leaf-to-hub cross matrix as `C=A[I,H]`, assume `rank C=2`, and set `G=C^T C>0`. For a literal leaf `i in I`, write `R=I\{i}`, `c_i=A[i,H] in R^2`, `C_R=A[R,H]`, and `d_i=A[R,i]` (the complete off-diagonal curvature row from `i` into the remaining leaf bank). Define the physical-row leverage

`ell_i=c_i^T G^(-1)c_i`.

When `ell_i<1`, `C_R` has rank two and the matrix-determinant lemma gives the exact identity

`det(C_R^T C_R)=det(G-c_i c_i^T)=det(G)(1-ell_i)`.          (1)

Now expose the ORIGINAL-coordinate cut

`S=H union {i}`,  `T=R`.

Its physical cross block is

`B_i=A[S,T]=[ C_R^T ; d_i^T ]`,                              (2)

viewed as a `3 x |R|` matrix. Put

`delta_i=dist(d_i, col(C_R))`.

The Schur-complement formula for the Gram determinant gives

`det(B_i B_i^T)=det(C_R^T C_R) delta_i^2
               =det(G)(1-ell_i) delta_i^2`.                  (3)

Therefore the product of the three singular values of `B_i` is exactly

`Delta_3(B_i)=sqrt(det G (1-ell_i)) delta_i`.                 (4)

This is the desired bridge from arbitrary within-bank curvature to a product-preserving off-diagonal mechanism: no leaf curvature has been deleted or treated as a small random perturbation.

Apply fleet03/B09's completed grouped-cross theorem, source
`yspennstate/math-open-problems@0257b7a08990f303da16797bcbad0d3e6a1e6538`, path
`proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B09/20260923T104947Z-fleet03-B09-QFORM-r30/REPORT.md`.
It allows arbitrary same-side quadratic blocks and states for any original-coordinate cross block of rank three

`||p_Q||_infinity <= 3e Delta_3(B)^(-1/3)`                    (5)

with a continuous density and the identical coefficient times interval length. Combining (4)-(5), whenever `delta_i>0`,

`||p_Q||_infinity
 <=3e [sqrt(det G (1-ell_i)) delta_i]^(-1/3),                 (6)

and

`P{Q in L} <=3e [sqrt(det G (1-ell_i)) delta_i]^(-1/3)|L|`.  (7)

All quadratic curvature on `S` and `T`, all signs, and all couplings to coordinates conditioned outside `S union T` remain arbitrary.

Exact zero-volume endpoint: if there is no exact cross coloop (`ell_i<1` for every leaf) and every `delta_i=0`, then every deletion keeps cross rank two and every singleton augmentation still has cross rank at most two. Fleet03/B09's exact lemma `QFORM-RANK2-NOAUGMENT-DIAG-PLUS-SPAN-v1` therefore applies and forces

`A[I,I]=C M C^T + Lambda`,                                    (8)

for one symmetric `2 x 2` matrix `M` and one ORIGINAL-coordinate diagonal matrix `Lambda`.

Thus arbitrary leaf curvature has an exact dichotomy at the near-coloop frontier: transverse curvature produces a literal rank-three grouped cut and the direct `O(|L|)` payment (7); complete failure of all such volumes, away from an exact coloop, forces the leaf operator into diagonal-plus-slope-span form (8). The remaining quantitative gap is the near-zero, not exactly zero, volume regime and the exact-coloop endpoint.
