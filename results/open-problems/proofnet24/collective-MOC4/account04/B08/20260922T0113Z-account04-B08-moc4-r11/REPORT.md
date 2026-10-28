# MOC4 account04/B08 — pair-flat boundary reduction

Run: `20260922T0113Z-account04-B08-moc4-r11`  
Candidate: `MOC4-PAIR-FLAT-BOUNDARY-v1`  
Outcome: `ESSENTIAL_STEP_APPLIED`  
Parent target: **MOC4 remains open**.  
Execution context: `WITHOUT_VERIFIED_BRAIN_RESEARCH`.

## Target and role

For complex normal `4 x 4` matrices, after diagonalizing one matrix write

`D(U) = det(D_a + U D_b U*)`, `U in U(4)`.

For each support direction `eta` with `|eta|=1`, put `h_eta(U)=Re(eta D(U))`. The MOC4 support inequality is

`h_eta(U) <= max_{sigma in S4} Re(eta product_i(a_i+b_{sigma(i)}))`.

This report addresses the assigned extremal/boundary question. It does **not** assert the global support inequality.

## Exact dependencies consumed


2. **account02/B07, `MOC4-BIRAYLEIGH-ORBIT-v1`**: shared blob `f0bcc37f9bb492433b6ec9e7ad9e6428ed39a5c1`. It proves the singular-safe `2 x 2` Rayleigh formula for every true-unitary row/column pair orbit and the resulting twelve pair-top conditions at every global support maximizer.

3. **account02/B09, `MOC4-BIPAIR-MAX-v1`**: shared blob `2ec549889d7e103e731b94cd6789eefb0a55038a`. It gives the exact full row-pair ellipse formula used below and refutes the stronger but false claim that a pair orbit is bounded by its identity/swap endpoints.

4. **Prior account04/B08, `MOC4-GENERIC-STRICT-SUPPORT-v1`**: shared blob `dadbc3f9ca7e7d0ab3fac85a0fd85418dfeaa62f`. It shows that any genuine target counterexample may be perturbed to a strict-support generic spectral/unitary locus, while recording separately the compound boundaries `r=|d|` and `r=(1+d^2)/2`.

5. **Current team-lead computation, account03/B07 r11b**: at the snapshot read there was not yet a complete lead `REPORT.md`, so I do not call it a complete lead version. Its exact `VERIFICATION.txt` blob `9560568dea6e396204efecf311ff40942ecc66a0` and verifier blob `b626d19b8c0e2e9c9d52dd1a7b4f61e2f69887cf` prove that arbitrary nonnegative cylinder functions are too large a cone for a determinantal-quasiprobability positivity proof. This run therefore keeps the actual spectral/adjugate structure rather than replacing it by arbitrary nonnegative endpoint data.

## Compact conditional end-to-end chain

A target counterexample gives a support direction `eta` and a global maximizer `U` with support strictly above all 24 permutation vertices. By the earlier generic strict-support reduction and the singular perturbation argument in `MOC4-BIRAYLEIGH-ORBIT-v1`, the unresolved proof may be concentrated on simple spectra, a unique maximizing permutation vertex, positive support gap, and nonsingular determinant point, provided all boundary branches are genuinely closed. Every such global maximizer is top on each of its six row-pair and six column-pair true-unitary orbits. The first boundary issue is therefore: **what exactly happens when one of these pair maxima has zero curvature / a tied opposite endpoint?**

The theorem below pays that implication exactly. It turns every tied pair endpoint at a global maximizer into a whole continuous flat orbit and then into an equal-support zero-entry boundary representative. Thus a putative violating maximizer has a sharp dichotomy: it is strict on every pair orbit, or the same violation already occurs on a `1 x 1` unitary-minor boundary.

## Theorem — pair-flat boundary dichotomy

Fix a row pair `I={i,j}`. Let

`m=(a_i+a_j)/2`, `delta=(a_i-a_j)/2`,

and let `N` denote the matrix obtained from `D_a+U D_b U*` by replacing the two diagonal spectral entries `a_i,a_j` by `m,m`. For an embedded `G in SU(2)` acting on rows `I`, write

`G* sigma_z G = n_x sigma_x + n_y sigma_y + n_z sigma_z`, `n in S^2`.

Then, with `tilde(sigma_r)` denoting the Pauli matrix embedded in rows/columns `I`,

`D(GU) = d0 + delta sum_{r=x,y,z} q_r n_r`,

where

`d0 = det(N) - delta^2 det(N[I^c,I^c])`,  
`q_r = tr(adj(N) tilde(sigma_r))`.

This is a polynomial identity, so no invertibility is required.

Put

`alpha = Re(eta d0)`, `c_r = Re(eta delta q_r)`.

Then the support on the complete pair orbit is exactly

`h_eta(GU) = alpha + c dot n`.

Assume now that `U` is a **global** maximizer of `h_eta` on `U(4)`. At `G=I` we have `n=e_z`. Hence `e_z` maximizes `alpha+c dot n` on the whole sphere. Therefore

`c_x=c_y=0`, `c_z>=0`.                                                  (1)

The opposite pole has the same determinant value as the row-transposed endpoint, because the determinant after left pair rotation depends only on `G* D_a G`, and both choices send `sigma_z` to `-sigma_z`. Thus

`h_eta(U)-h_eta(P_ij U) = 2 c_z`.                                        (2)

Consequently exactly one of the following holds for this row pair:

- **strict pair:** `h_eta(U)>h_eta(P_ij U)`. Then `c_z>0`, and `e_z` is the unique maximizer of the entire row-pair sphere, not merely better than the swapped endpoint;
- **flat pair:** `h_eta(U)=h_eta(P_ij U)`. Then (1)-(2) give `c_x=c_y=c_z=0`, so `h_eta(GU)=h_eta(U)` for **every** embedded `G in SU(2)`.

The identical statement holds for every column pair, with `a,b` interchanged.

### Exact adjugate characterization

Let

`K_I = eta delta (adj(N))[I,I]`.

For Hermitian Pauli matrices,

`c_r = Re tr(K_I sigma_r) = tr(Herm(K_I) sigma_r)`.

Since `{I,sigma_x,sigma_y,sigma_z}` is an orthogonal real basis of Hermitian `2 x 2` matrices, global pair maximality is equivalent to

`Herm(K_I) = tau I + (c_z/2) sigma_z`, with `c_z>=0`.                     (3)

The flat-pair condition is equivalently

`Herm(K_I) = tau I`.                                                       (4)

Thus the pair degeneracy is an explicit algebraic adjugate condition, valid at singular `N` as well.

### Flat pair forces an equal-support zero-entry boundary representative

Suppose a global support maximizer `U` violates the MOC4 support bound and row pair `I` is flat. The whole `SU(2)` pair orbit is then made of global maximizers with the **same violating support value**. Choose any column `k` for which the two-vector `(u_ik,u_jk)` is nonzero; such a column exists because the two rows have norm one. Transitivity of `SU(2)` on the unit sphere in `C^2` gives an embedded `G` sending that two-vector to `(rho,0)` (or `(0,rho)`). Then

`U' = G U`

is unitary, has the same spectra and same 24 target vertices, has the same violating support, and has `u'_{jk}=0`. Hence a flat row pair transfers the violation to the `1 x 1`-minor boundary. The column version is identical.

This proves the exact branch reduction:

> Every support-violating global maximizer is either strict on all twelve row/column pair spheres, or an equal-support violating global maximizer exists with a zero entry of `U`.

No claim is made here that the zero-entry boundary is already harmless.

## Why this is stronger than checking the twelve swaps

At a global maximizer the transverse pair coefficients vanish automatically. Therefore strictness against the opposite endpoint is equivalent to strictness on the **entire** pair sphere. This equivalence is special to a genuine global maximizer and uses the exact pair-ellipse geometry; it is not true for an arbitrary point.

The named partner account01/B09 example is decisive here: it is strict for all twelve pair competitors yet nonmonomial. Therefore the surviving interior branch cannot be replaced by "strict on every pair => monomial". Its rank-two sum also explains why a nonsingular hypothesis remains a plausible extra ingredient, but this report does not assert such a rigidity theorem.

## Relation to the other known boundary slacks

The earlier generic reduction gave, for each `2 x 2` compound block with squared singular values `lambda_1,lambda_2`,

`r+d=2 lambda_1 lambda_2`,  
`r-d=2(1-lambda_1)(1-lambda_2)`,  
`(1+d^2)/2-r=(lambda_1-lambda_2)^2/2`.

Those equations classify the compound rank/complement-rank and equal-angle boundaries. The new theorem classifies a different extremal degeneracy: **flatness of the determinant support along an actual row/column `U(2)` orbit**. A proof of MOC4 must either close the zero-entry branch produced above or prove the support bound on the nonsingular, generic, bi-pair-strict interior branch.

## First essential remaining implication

`MOC4-BIPAIR-STRICT-OR-BOUNDARY-v1`:

For simple nonzero spectra and a support direction with a unique maximizing permutation vertex, prove the support inequality for every nonsingular global maximizer that is strict on all twelve row/column pair spheres, **and** close the zero-entry boundary branch; equivalently, show no support-violating global maximizer can survive either branch.

The partner's nonmonomial example blocks monomial classification as a general substitute. The current lead's exact cylinder-cone separator blocks positivity against every arbitrary nonnegative endpoint-space test function as a substitute. The remaining mechanism therefore has to use the structured spectral coefficients together with the common-unitary / `SO(6)` / Pluecker constraints, or a comparably strong true-unitary argument.

## Failure / non-claims

- This is not a proof of MOC4.
- A nonmonomial stationary point or maximizer is not declared a counterexample.
- The zero-entry branch is identified but not closed.
- No arbitrary bistochastic or arbitrary nonnegative-function relaxation is assumed realizable.
- No numerical search or floating tolerance is used for the new theorem; it is an exact algebraic consequence of the pair-ellipse identity.

## Source/provenance and privacy review

Inputs were the owner-scoped private MOC4 target and the exact peer artifacts named above. The report contains no benchmark gold, answer keys, encryption keys, credentials, scheduler identifiers, machine paths, email/Drive material, unrelated private data, or public-release action. No paid model/API, remote workflow, or additional account action was used.
