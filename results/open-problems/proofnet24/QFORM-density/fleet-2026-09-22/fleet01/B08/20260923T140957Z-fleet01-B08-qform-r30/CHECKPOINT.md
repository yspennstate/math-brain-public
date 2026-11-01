SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet01, slot B08, 2026-09-23T14:09:57.398564Z.
attacking: diffuse selected-three eigenspace — turn deletion of localized physical coordinates into a quantitative conservation of the remaining large directions, then combine this with the one-scale ridge theorem and fleet02/B08's current k=1 router.

# Substantive checkpoint — physical-deletion rank-loss conservation

Full QFORM remains OPEN. This checkpoint records the first proved step of run `20260923T140957Z-fleet01-B08-qform-r30`; it is not a full-solution claim.

Let `A=A^T`, let `R in R^{n x 3}` have orthonormal columns and satisfy

`A R = R Lambda`,  `min_j |Lambda_jj| >= L>0`.

For a physical coordinate set `H`, `|H|=h in {1,2}`, put `T=H^c`, `C=A[T,T]`, and

`delta_H=||R_H^T R_H||op`.

Then

`boxed: s_{3-h}(C) >= L sqrt(1-delta_H).`

Indeed the T-row block of the eigen-equation is

`C R_T = R_T Lambda - A[T,H] R_H`.                              (1)

The second term has rank at most h. Since

`R_T^T R_T = I_3-R_H^T R_H`,

` s_3(R_T Lambda) >= L sqrt(1-delta_H).`                         (2)

For a rank-h perturbation, the singular-value Weyl inequality gives

` s_{3-h}(C R_T) >= s_3(R_T Lambda).`                            (3)

Finally `||R_T||op<=1` and `s_k(CR_T)<=s_k(C)||R_T||op`, hence (1)-(3) prove the box.

If every selected row has leverage `||R_i||^2<=mu`, then `delta_H<=h mu`, so

`boxed: s_{3-h}(A[T,T]) >= L sqrt(1-h mu).}`                     (4)

At the inherited B08 diffuse threshold `mu=1/48`, deletion of ANY one original coordinate leaves

`boxed: s_2(A[-i,-i]) >= sqrt(47/48)L =0.989528507253... L.}`   (5)

This is a full-matrix statement: no complementary spectrum is removed, no random quadratic remainder is declared small, and no rotation of the product source is used.

## Actual application of designated partner fleet02/B08

The current completed partner report `fleet02/B08 r27` is canonical at

`yspennstate/math-open-problems@41ee49f6e9c3383e4c3a322bdc52779768a17eb7`,
`proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B08/20260923T130941Z-fleet02-B08-qform-diffuse-r27/REPORT.md`.

On its inherited selected-three `mu<=1/48` k=1 gate,

`beta=(3/16)sqrt(3/5)`, `s_2(B)>=beta L`.

Its high-top-two-leverage branch supplies a physical row i with cross-row `g=B^T e_i` satisfying

`||g|| > beta L/sqrt(2) = (3/16)sqrt(3/10)L`.

Because `g` is a subvector of the full off-diagonal row of A, (5) gives the simultaneous literal physical resource

`boxed: ||A[i,-i]|| > (3/16)sqrt(3/10)L =0.102697979532...L,`
`boxed: s_2(A[-i,-i]) >= sqrt(47/48)L =0.989528507253...L.}`     (6)

Thus the partner's heavy-row survivor is not merely a star: at the SAME physical coordinate the deleted full principal child retains two almost-L singular directions. This is the first quantitative bridge this run will feed into the diffuse/localized compiler.
