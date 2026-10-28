SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account02, slot B02, 2026-09-24T01:10:09Z.
attacking: aggregate the newest partner's three-physical-leaf hub estimate before selecting one leaf triple, use D'/D5 on that live physical star block, and reduce the remaining shared-hub debt to a genuinely small aggregate rank-three star volume / rank-two internal-curvature collar.

# account02/B02 auto11 — aggregate star-volume Fourier compiler and diffuse-triple obstruction

Programme: `QFORM-DENSITY-3EIG-20260922`  
Role: Integrated Fourier estimate / complementary constructions and source-valid counterexamples  
Status: **ESSENTIAL_STEP_APPLIED / NEW SUPPORTING COMPILER / FULL QFORM OPEN / TARGET-WIDE FOURIER L1 OPEN-NOT-REFUTED**

The exact owner target is unchanged: independent ORIGINAL real coordinates with one-dimensional probability densities at most one, arbitrary real symmetric `A`, and at least three eigenvalues of modulus at least one. No moment, support, log-concavity, iid, diagonal-basis, or post-rotation-independence hypothesis is inserted. Continuity is asserted only on branches where an actual unweighted Fourier-`L1` estimate is proved.

## 1. Fresh control and sources actually used


Required pinned base package:

- `yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`;
- `proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/{RESULTS.md,FOURIER_ROUTE_REPORT.md,COUNTEREXAMPLE_SEARCH.md}`.

Reviewed sharp Hausdorff--Young refinement:

- `yspennstate/math-open-problems@c2414ef633b9d4b7f04a83e1aeefbe713ed82bba`;
- `proofnet24/QFORM-density/interactive/20260923T002323Z-volume-stability/REPORT.md`.

For a literal physical cross block `M=A[I,J]`, `Z=E3(M)>0`, `1<=q<3/2`, and third-volume row marginals `alpha_i<=q/2`, it proves

`||p_Q||_infinity <= [3e/((3-2q)sqrt(q))] Z^(-1/6)`,             (1.1)

with `phi_Q in L1`. Its reviewed fifth-volume branch is

`||p_Q||_infinity <= (5e/sqrt(2)) E5(M)^(-1/10)`,                (1.2)

again with `phi_Q in L1`, and has no marginal gate.

The completed B02 heavy-row cascade combined with (1.1) already gives the marginal-free physical third-volume estimate

`||p_Q||_infinity <= C3 E3(M)^(-1/6)`,
`C3=10.3450832321475...`,                                       (1.3)

with `phi_Q in L1`, for every physical original-coordinate cross block with positive `E3`.

Newest completed designated partner: `account03/B02` r42,

- report creation commit `561b250f8e0d09101392837debb75e8cbf3851ea`, with later deterministic-check commits through `95f538bbf0fd22fe2a50deaa336beb4babbb3d38`;
- `proofnet24/QFORM-density/fleet-2026-09-22/account03/B02/20260924T003335Z-account03-B02-qform-r42/REPORT.md`;
- theorem `QFORM-THREE-PHYSICAL-LEAF-HUB-L1-v1`.

If `H` is an original-coordinate hub bank, `I` is a three-element physical leaf set, `M=A[I,H]`, and

`Delta=sqrt(det(M M^T))>0`,                                     (1.4)

then the partner proves

`|phi_Q(t)| <=2^(3/4) pi^(3/2) Delta^(-1/2)|t|^(-3/2)`,         (1.5)
`integral |phi_Q| <=6sqrt(2)pi Delta^(-1/3)`,                    (1.6)
`||p_Q||_infinity <=3sqrt(2) Delta^(-1/3)`.                      (1.7)

The proof keeps arbitrary leaf-leaf curvature and all outside coefficients by conditioning only on ORIGINAL coordinates and using a genuine three-dimensional Plancherel step.

The new Fisher-information continuation explicitly assigned this B02 a scoped independent check. The source is

- `yspennstate/math-open-problems@4a65677d185d35154dc3dfae320c5df9f939b8a2`;
- `proofnet24/QFORM-density/interactive/20260923T184054Z-fisher-continuation/FISHER_INFORMATION.md`, blob `8a562d0d8c8c47679b83c33d1e0bbe9390387f4d`.

The separate file `FISHER_REVIEW.md` in this run records a PASS on the assigned weak-IBP/cutoff/inverse-distance/primitive-normalization/density-domination scope only.

## 2. Main exact identity: aggregate the partner leaf triples before selection

Let `K,H` be disjoint ORIGINAL-coordinate banks and put

`B=A[K,H]`.                                                      (2.1)

For every physical leaf triple `I subset K`, `|I|=3`, define

`Delta_I^2=det(B[I,:]B[I,:]^T)`.                                (2.2)

Cauchy--Binet gives

`Delta_I^2=sum_{J subset H, |J|=3} det B[I,J]^2`.                (2.3)

Summing (2.3) over all physical leaf triples gives

`boxed:
 Z3:=E3(B)=e3(B^T B)=sum_{I subset K, |I|=3} Delta_I^2.
`                                                                   (2.4)

This is exactly the aggregate resource that the partner r42 report leaves as its 'diffuse third-star-volume' issue.

### Theorem 2.1 — `QFORM-AGGREGATE-STAR-VOLUME-L1-v1`

For every such physical star block `B`, if `Z3>0`, then the full ambient quadratic form satisfies

`boxed:
 ||p_Q||_infinity <= C3 Z3^(-1/6),
 integral_R |phi_Q(t)|dt <= 2pi C3 Z3^(-1/6),
 C3=10.3450832321475... .
`                                                                   (2.5)

If additionally `Z5:=E5(B)>0`, then

`boxed:
 ||p_Q||_infinity <= (5e/sqrt(2)) Z5^(-1/10),
`                                                                   (2.6)

also with `phi_Q in L1`. Therefore the live combined estimate is

`boxed:
 ||p_Q||_infinity
 <= min{ C3 Z3^(-1/6),
          (5e/sqrt(2)) Z5^(-1/10),
          3sqrt(2) Delta_*^(-1/3) },
`                                                                   (2.7)

where `Delta_*=max_I Delta_I` and the last term is the newest designated-partner theorem.

#### Proof

Identity (2.4) is Cauchy--Binet. Apply the already completed marginal-free physical-`E3` compiler (1.3) directly to the **whole actual block** `B`; this gives (2.5) without selecting a row triple. Apply the reviewed D5 theorem (1.2) to the same `B`; this gives (2.6). Apply partner r42 to the maximizing literal leaf triple to obtain the third term. All three estimates retain arbitrary same-bank curvature and arbitrary coefficients outside the two physical banks. QED.

The D5 term improves the `E3` term precisely when

`Z5 >= kappa5 Z3^(5/3)`,
`kappa5=((5e/sqrt(2))/C3)^10
       =0.478800937867911... .`                                  (2.8)

Thus D' and D5 are simultaneously active on the same physical star block, but neither is substituted for the other.

## 3. Why aggregation is essential: an exact-target diffuse-triple family

The partner r42 theorem is powerful for a fixed physical leaf triple, but selection of a single triple cannot be the universal structural step.

For every integer `k>=1`, let `B_k` be the `(3k) x 3` matrix whose rows consist of

- `k` copies of `e1/sqrt(k)`,
- `k` copies of `e2/sqrt(k)`,
- `k` copies of `e3/sqrt(k)`.

Then

`B_k^T B_k=I_3`,                                                 (3.1)

so

`E3(B_k)=e3(I_3)=1`.                                             (3.2)

For a physical leaf triple `I`, the Gram determinant in (2.2) vanishes unless `I` contains one row from each of the three groups. In the nonzero case

`Delta_I^2=k^(-3)`, hence `Delta_*=k^(-3/2)`.                    (3.3)

Embed this block in the symmetric original-coordinate matrix

`A_k = [[0,B_k],[B_k^T,0]]`.                                    (3.4)

Because the three nonzero singular values of `B_k` are all one, the nonzero spectrum of `A_k` is

`+1,+1,+1,-1,-1,-1`.                                            (3.5)

Thus (3.4) is an exact-target family, with no limiting or approximate spectral hypothesis.

Applying the completed partner r42 theorem (1.7) to its best physical triple gives only

`||p_Q||_infinity <=3sqrt(2) k^(1/2)`,                           (3.6)

which deteriorates without bound as a **certificate**. In contrast, the aggregate theorem (2.5) gives for every admissible product law

`boxed: ||p_(X^T A_k X)||_infinity <=10.3450832321475... ,}`      (3.7)

uniformly in `k`, with a continuous `C0` density from Fourier `L1`.

The reviewed D5 route is identically unavailable on this witness because `rank(B_k)=3`, so `E5(B_k)=0`. This makes the example a source-valid obstruction to both 'select one uniformly good physical leaf triple' and 'let D5 rescue the selection loss'. It is **not** a counterexample to QFORM or to the target-wide Fourier-L1 conjecture; it is instead a family where aggregate D' succeeds exactly when one-triple extraction fails.

Equation (3.6) is the required equation-level application of the newest designated partner theorem to a real obstruction.

## 4. Application to the live r39/r42 shared-hub partition

The preceding designated-partner chain starts from the overlap-one third-compound mass `V1`. Account03/B02 r39 constructs an actual original-coordinate partition `H,L,R` satisfying

`W >=(16/3125)V1`,                                               (4.1)

and its grouped pivot/two-star identity gives

`max{ E2(N) sum_h A_hh^2, sum_h T_h }
 >= W/4 >=(4/3125)V1`,                                          (4.2)

where `N=A[L,R]` and `T_h` is the exact projected two-star resource.

On this SAME partition form the physical total star block

`B_*=A[L union R,H]`,                                            (4.3)

and let

`Z3_*=E3(B_*)`, `Z5_*=E5(B_*)`.                                 (4.4)

Theorem 2.1 immediately gives

`||p_Q||_infinity <= C3 (Z3_*)^(-1/6)` whenever `Z3_*>0`,        (4.5)

and the D5 alternative (2.6) whenever `Z5_*>0`.

Choose the clean bookkeeping threshold `eta=1/64`. If

`Z3_* >= V1/64`,                                                 (4.6)

then

`boxed:
 ||p_Q||_infinity
 <= 20.6901664643 V1^(-1/6).
`                                                                   (4.7)

On the target-scale overlap branch `V1>1/4`,

`boxed: ||p_Q||_infinity <26.067977.`                            (4.8)

Hence the newest partner's phrase 'diffuse third-star-volume collar' no longer denotes an analytic selection problem. Diffusion among arbitrarily many tiny physical triples is paid by (2.5). The actual remaining star obstruction at this threshold is quantitatively

`boxed: E3(B_*) < V1/64,`                                       (4.9)

possibly together with the exact/near total-star-rank-two internal-curvature packet already isolated by r39/r40.

D5 gives an independent exit before entering that packet whenever

`Z5_* >=0.478800937867911 (Z3_*)^(5/3)`.                         (4.10)

No claim is made that (4.10) follows from (4.2); it is a genuine complementary certificate.

## 5. Criticality of the next rank-two mechanism

If the star block has only two effective directions and one forgets all original-coordinate structure except the two-dimensional projected density caps, the direct bilinear Plancherel estimate is scale-critical: a rank-two bilinear phase supplies only `|t|^(-1)`. More generally, Hölder plus Hausdorff--Young for arbitrary two-dimensional projected densities cannot improve the power beyond one: using `L^p` on one projected bank and `L^(p')` on its Fourier transform produces the scaling exponent `2/p'<=1` for `1<=p<=2`.

Therefore the next receiver must use a **third physical smoothing resource** rather than merely repeat a two-dimensional projection estimate. In the current r39/r40 geometry that third credit can come from a transverse `L-R` crossing/internal-curvature factor, exactly as the completed grouped Schur theorem does in the coherent-star rank-one subcase. This explains why (4.9) should now be coupled to the internal-curvature packet instead of attacked by another max-triple extraction.

This is a mechanism obstruction, not a QFORM counterexample and not a proof that target-wide Fourier L1 fails.

## 6. Independent check of the new Fisher-information continuation

The assigned account02/B02 scope was checked independently in `FISHER_REVIEW.md`. Summary:

- `sqrt(f_i) in H1` implies the weak product-score identity with finite `E|S_i|` and `E S_i^2=I_i`;
- for `W_delta=Uz/(R^2+delta)`, the exact divergence bound and cutoff-first weak integration by parts give
  `E(R^2+delta)^(-1)<=J_E/(r-2)^2` with no moment assumption;
- for `V_delta=U Lambda^(-1)z/[2(R^2+delta)]`, the spectral contraction is exactly `R^2/(R^2+delta)`;
- the centered primitive has norm `m/2`, and together with the `1/2` in `V_delta` gives the source's exact factor `1/4`;
- domination against all nonnegative compactly supported smooth tests gives measure domination and hence the claimed essential density bound.

Verdict: **PASS on the assigned weak-IBP/cutoff/inverse-distance/primitive/density-domination scope.** This does not review the separately assigned compact-kernel/spectral/smoothing components and does not remove the Fisher-information hypothesis.

## 7. Correction boundaries

No step above uses law-uniform scalar quadratic pointwise decay, post-rotation independence, arbitrary conditional density caps, arbitrary-joint coarea, a uniformly good single minor, deletion of a small nonzero matrix tail, or replacement of a physical coefficient row by an abstract exterior-feature row. All Fourier estimates are applied to literal original-coordinate cross blocks or literal physical leaf triples.

The exact-target family (3.4) additionally shows that the full spectral hypothesis does not force one uniformly large physical three-leaf star certificate even when the entire third exterior volume is exactly one.

## 8. Exact status and next unpaid implication

The unrestricted three-large-eigenvalue QFORM conjecture remains **OPEN**. Full-target continuity remains **OPEN**. The target-wide universal unweighted Fourier-`L1` assertion remains **OPEN / not refuted**.

This run pays the **diffusion** aspect of the partner r42 third-star-volume residue by aggregating before selection. The next B02 implication is now

`QFORM-SMALL-STAR-E3-RANK2-INTERNAL-CURVATURE-L1-v1`:

on the r39 physical partition, assume `E3(A[L union R,H])<V1/64` and retain the grouped resource (4.2); route its surviving two-star / `L-R` internal-curvature mass through a product-preserving rank-two-star plus transverse-crossing Fourier receiver, without deleting any nonzero tail and without reducing to a law-uniform `|t|^-1` critical estimate.

No task identity, schedule, enabled/paused state, notification, email, public-release, paid-API/model, installation, permission, or cross-account-authentication state was changed.
