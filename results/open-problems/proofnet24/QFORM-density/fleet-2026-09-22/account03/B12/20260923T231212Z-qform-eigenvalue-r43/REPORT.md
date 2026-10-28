SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B12, 2026-09-23T23:12:12.669240Z.
attacking: change mechanism from the r40-r42 cross-volume sequence. The r42 rank-two tube is now partly superseded by the fresh Schur spectral-count theorem, so this run composes that exact physical Schur inheritance with an arbitrary unbounded signed spectral packet plus a full-rank small spectral tail, and then applies account04/B12 r7 at an actual new inequality.

# account03/B12 r43 — spectral-packet Schur budget under arbitrary signed additions

Programme: `QFORM-DENSITY-3EIG-20260922`  
Role: Additional eigenvalue control  
Run: `20260923T231212Z-qform-eigenvalue-r43`  
Status: **PROVED SUPPORTING STABILITY THEOREM / FULL QFORM OPEN**  
Execution: `WITHOUT_VERIFIED_BRAIN`  
Continuity: **not claimed for the new general compiler; full-target continuity remains open.**

## 1. Scope and source boundary

The target remains the unrestricted original-coordinate statement: `X_1,...,X_n` independent with scalar probability densities at most one, arbitrary real symmetric `A`, and at least three eigenvalues of modulus at least one. No moment, bounded-support, connected-support, log-concavity, Gaussianity, iid, spectral-coordinate independence, or convolution treatment of an added quadratic term is used.


The immediate own predecessor is account03/B12 r42,

`yspennstate/math-open-problems@cf95b153d479d110ce0205017bf66ba0e333aef8`,

`proofnet24/QFORM-density/fleet-2026-09-22/account03/B12/20260923T214400Z-qform-eigenvalue-r42/REPORT.md`.

That run reduced one three-square-mode chamber to a quantitative rank-two physical common-plane tube. I do **not** repeat that mechanism here.

Two fresh source-matching facts were found before deriving:

1. `yspennstate/math-open-problems@742ac943440e41925fe09db9a8c02a96cbd83dbc`, `proofnet24/QFORM-density/interactive/20260922T180015Z-pair-log/FULL_MATRIX_PAIR_EXTENSION.md`, already proves the `r=2,k=1` Schur-scale fact used in the arbitrary-rank physical-pair theorem. I do not claim that special case as new.
2. The newer report `yspennstate/math-open-problems@93d2aedf7856c66f42a4ece7156b773db2589efe`, `proofnet24/QFORM-density/interactive/20260923T220000Z-all-fixed-dimension-density/REPORT.md`, explicitly records the general exact rank-perturbation identity

   `s_{j+r}(A) <= s_j(S)`

   for an `r x r` invertible physical pivot and its Schur complement `S`. It also records the completed dimension-free lower-level half-potential theorem for a quadratic with at least two singular values at scale one. Therefore the exact Schur-profile step itself is source-matching completed work and is treated as an input, not a new claim.

The new result below is the **pre-Schur arbitrary spectral-packet composition**: an arbitrary number `q` of added eigenmodes may have completely unbounded magnitude, either sign and arbitrary orientation, while every remaining added eigenvalue is charged only through the first unreserved singular value. The leading packet is never treated probabilistically.

The designated partner actually applied is account04/B12 r7,

`yspennstate/math-open-problems@3df1475f988c811570dc5c249a7756d24adb51bf`,

`proofnet24/QFORM-density/fleet-2026-09-22/account04/B12/20260923T191531Z-account04-B12-hybrid-square-defect-r7/REPORT.md`.

Its full proof was read. In its explicit hostile-spectrum family it proves, for an eleven-coordinate physical carrier `H`,

`sqrt(lambda_6((A_p^2)[H,H])) >= 7/4`,

and also `s_3(A_p)>=7/4`. Section 5 below spends the stronger six-mode consequence at an actual new inequality.

## 2. Main deterministic theorem

Let `A_0=A_0^T` and let `E=E^T` be an arbitrary added matrix. Fix an integer `q>=0`. Write the singular values of `E` in decreasing order as

`s_1(E)>=s_2(E)>=...`,

and set

`delta_q=s_{q+1}(E)`

(with `delta_q=0` if `rank(E)<=q`). Since `E` is symmetric, its first `q` singular modes are genuine signed eigenmodes; their eigenvalues may have either sign and arbitrarily large magnitude.

Put

`A=A_0+E`.

Choose any set `I` of `r` ORIGINAL coordinates such that the final physical principal block

`B=A[I,I]`

is invertible. Let `J=I^c` and let

`S=A[J,J]-A[J,I] B^{-1} A[I,J]`

be the exact Schur complement. No random coordinate is rotated.

### Theorem 2.1 — `QFORM-SPECTRAL-PACKET-SCHUR-BUDGET-v1`

For every integer `k>=1` with

`q+r+k<=n`, one has

`boxed:
 s_k(S) >= ( s_{q+r+k}(A_0) - delta_q )_+ .`                    (2.1)

Equivalently, for every `a>delta_q`,

`boxed:
 N_abs(S; a-delta_q)
 >= N_abs(A_0;a)-q-r,
}`                                                                 (2.2)

where negative right sides are interpreted as zero and `N_abs(M;t)` counts eigenvalues of `M` with modulus at least `t`.

Thus:

- the first `q` added eigenmodes are completely free in magnitude, sign and orientation;
- all remaining added eigenvalues, however numerous and of either sign, cost only `delta_q`;
- a subsequent physical Schur completion of `r` ORIGINAL coordinates costs only `r` spectral reserve modes;
- no term `X^T E X` is separated as independent noise or convolved with the old law.

#### Proof

Take the spectral truncation

`E=R+T`,

where `rank(R)<=q` and `||T||op=delta_q`. This is deterministic coefficient algebra.

For singular values, the rank-`q` perturbation inequality gives, for every admissible `j`,

`s_{j+q}(A_0)
 <= s_j(A_0+R)`.                                                  (2.3)

One direct proof is the singular-value Weyl inequality

`s_{u+v-1}(X+Y)<=s_u(X)+s_v(Y)`

applied to `A_0=(A_0+R)-R` with `v=q+1`, because `s_{q+1}(R)=0`.

Adding the full-rank tail `T` and applying the reverse Weyl bound gives

`s_j(A)
 >= s_j(A_0+R)-||T||op
 >= s_{j+q}(A_0)-delta_q`.                                       (2.4)

Now use the exact final physical pivot. The matrix

`A-diag(0_I,S)
 = [[B, A[I,J]],
    [A[J,I], A[J,I]B^{-1}A[I,J]]]`

factors as

`[I_r; A[J,I]B^{-1}] B [I_r, B^{-1}A[I,J]]`,                    (2.5)

so its rank is at most `r`. A second rank-perturbation inequality therefore gives

`s_{k+r}(A)<=s_k(diag(0_I,S))=s_k(S)`.                            (2.6)

Insert (2.4) with `j=k+r` into (2.6):

`s_k(S)
 >= s_{k+r}(A)
 >= s_{q+r+k}(A_0)-delta_q`,                                     (2.7)

which proves (2.1); (2.2) is the threshold-count form. QED.

### Sign-specific threshold form

The same rank-budget argument with Hermitian eigenvalue counting gives, for every `a>delta_q`,

`boxed:
 N_+(S;a-delta_q) >= [N_+(A_0;a)-q-r]_+,
 N_-(S;a-delta_q) >= [N_-(A_0;a)-q-r]_+ .`                       (2.8)

Indeed a rank-`q` Hermitian perturbation changes either threshold count by at most `q`; an operator perturbation of norm `delta_q` shifts the threshold by at most `delta_q`; and the final rank-`r` latent Schur completion changes either count by at most `r`. At threshold zero one has the stronger exact inertia identity from Schur congruence,

`inertia(A)=inertia(B)+inertia(S)`.                               (2.9)

So signs are tracked separately rather than being silently discarded.

## 3. Sharpness of the reserve count

The losses `q+r` and the coefficient one in (2.1) cannot be improved in general.

Take a diagonal baseline whose first `q+r` entries have magnitudes much larger than

`a_1>=a_2>=...>=a_k>0`,

followed by the entries `a_1,...,a_k`. Let the rank-`q` part of `E` cancel exactly the first `q` large diagonal modes, take `T=0`, and choose the next `r` large physical coordinates as the invertible pivot. The Schur complement is exactly

`diag(a_1,...,a_k)`,

so

`s_k(S)=a_k=s_{q+r+k}(A_0)`.                                     (3.1)

Thus an arbitrary hostile rank-`q` packet really can consume `q` reserve modes and the physical pivot can consume another `r`; no uniform theorem can charge fewer without extra structure.

## 4. Dependence-safe density corollaries

The theorem is deterministic, but it compiles directly into the two completed original-product receivers that are useful for QFORM.

### 4.1 Scalar physical pivot

Use the lower-level theorem recorded in the fresh fixed-dimension report at commit `93d2aedf7856c66f42a4ece7156b773db2589efe`: there is an absolute `G_2<infinity` such that every independent cap-one quadratic whose coefficient matrix has at least two singular values at least one, with arbitrary affine terms, obeys

`sup_t E[ |R-t|^{-1/2}; |R-t|<=1 ] <= G_2`.                      (4.1)

The contribution from `|R-t|>1` is at most one. By scaling, if `s_2(S)>=sigma>0`, then

`sup_t E |R-t|^{-1/2} <= (G_2+1)/sqrt(sigma)`.                    (4.2)

Now take `r=1`. If

`s_{q+3}(A_0)>=a>delta_q`

and a final ORIGINAL diagonal pivot satisfies

`beta=|A_ii|>0`,

then Theorem 2.1 gives

`s_2(S)>=a-delta_q`.                                              (4.3)

Completing the scalar square keeps `X_i` as an original independent variable. Its conditional square-map density is bounded by

`|A_ii|^{-1/2}|t-R|^{-1/2}`.

Averaging and using (4.2) gives the explicit dependence-safe stability estimate

`boxed:
 ||p_Q||_(infinity,ess)
 <= (G_2+1)/sqrt( beta (a-delta_q) ).`                            (4.4)

All leading added spectral modes and every tail coordinate remain inside the same final quadratic law. No convolution statement is used. This theorem gives essential boundedness; no new continuity claim is made.

### 4.2 Invertible indefinite physical pair

Take `r=2` and again assume `s_{q+3}(A_0)>=a>delta_q`. If a final two-coordinate physical principal block `B` is invertible indefinite, put

`D_B=|det B|`, `kappa=sigma_min(B)`.

Theorem 2.1 gives for its Schur remainder

`||S||op>=a-delta_q`.                                             (4.5)

The completed physical-pair logarithmic theorem at commit `742ac943440e41925fe09db9a8c02a96cbd83dbc` then gives

`boxed:
 ||p_Q||_(infinity,ess)
 <= 3*400^(1/3)
    [D_B^2 kappa (a-delta_q)]^(-1/6).`                           (4.6)

The analytic receiver in (4.6) is source-matching existing work; the new input is the packet-stable Schur scale (4.5). A definite pair is handled by its separate existing definite-pair estimate. Continuity is not asserted here.

## 5. Required account04/B12 application at an actual inequality

Use the completed account04/B12 r7 family exactly as proved at

`yspennstate/math-open-problems@3df1475f988c811570dc5c249a7756d24adb51bf`.

Call its final matrix `A_p`. For every chosen eleven-coordinate carrier `H`, the partner proves

`sqrt(lambda_6((A_p^2)[H,H]))>=7/4`.                              (5.1)

Since `(A_p^2)[H,H]` is a principal compression of the positive semidefinite matrix `A_p^2`, Cauchy interlacing gives

`lambda_6(A_p^2)
 >= lambda_6((A_p^2)[H,H])
 >=49/16`.

Therefore the partner result supplies the **global six-mode reserve**

`boxed: s_6(A_p)>=7/4.`                                          (5.2)

Now add a completely new symmetric matrix `E`, with no commutation, support, sign or orientation restriction, subject only to

`boxed: s_4(E)<=1/4.`                                            (5.3)

The first three eigenmodes of `E` may have arbitrary signs and arbitrarily large magnitude. Put

`A=A_p+E`.

Apply Theorem 2.1 with `q=3`, `delta_q<=1/4`.

**Scalar completion.** For any final nonzero physical scalar pivot (`r=1`), take `k=2`. Since `q+r+k=6`,

`boxed:
 s_2(S_scalar)
 >= s_6(A_p)-1/4
 >= 3/2.`                                                        (5.4)

Thus the partner hostile-spectrum family remains a two-large-mode Schur remainder even after **three additional completely unbounded signed eigenmodes plus an arbitrary full-rank tail of norm at most one quarter**. If the pivot has magnitude `beta`, (4.4) becomes

`boxed:
 ||p_Q||_(infinity,ess)
 <= (G_2+1)/sqrt((3/2) beta).`                                   (5.5)

**Two-coordinate completion.** For any final invertible physical pair (`r=2`), take `k=1`. Again `q+r+k=6`, so

`boxed:
 ||S_pair||op>=3/2.`                                             (5.6)

If the pair is indefinite, (4.6) gives

`boxed:
 ||p_Q||_(infinity,ess)
 <=3*400^(1/3)[(3/2)D_B^2 kappa]^(-1/6).`                        (5.7)

This is the requested equation-level partner application. The partner theorem supplies (5.2); the new compiler spends it after a further arbitrary signed spectral packet and a physical completion. Nothing in `E` is modeled as an independent random error.

For comparison, the same ledger gives other exact reserve allocations from the partner six-mode gate: with `q=2,r=2`, two residual singular modes survive at scale `3/2`; with `q=2,r=1`, three survive. The reserve arithmetic is `q+r+k<=6` and does not depend on the magnitudes of the leading hostile modes.

## 6. Finite consistency checks

A deterministic fixed-seed checker accompanies this report. It does **not** prove the theorem.

- 10,000 random symmetric tests, dimensions 7 through 16, mixed `q,r,k`, with the leading `q` eigenmodes of the added matrix amplified by factors up to `10^4`, found **zero violations** of (2.1). The smallest numerical margin `s_k(S)-[s_{q+r+k}(A_0)-delta_q]` was approximately `0.0807216989`.
- 5,000 separate mixed-sign tests found **zero violations** of both sign-specific threshold counts (2.8). The minimum integer slack was zero, so equality cases occurred numerically.

The proof is the rank-perturbation argument in Section 2, not the computation.

## 7. Relation to r42 and the current remaining gap

The fresh source at commit `93d2aedf7856c66f42a4ece7156b773db2589efe` changes the interpretation of the r42 tube. Once a scalar physical pivot has a quantitative lower bound, exact Schur inheritance plus the completed two-large-mode half-potential theorem pays the residual **without needing to delete or probabilistically approximate the common-plane tail**. Therefore continuing to attack the same r42 tube solely by ever finer cross-volume perturbation would duplicate a now-completed source interface.

The new theorem isolates what remains genuinely difficult for the unrestricted target: matrices for which no uniformly large physical scalar/pair pivot is available and for which the baseline three-mode reserve cannot be enlarged to a `q+r+3` packet before arbitrary hostile additions. Equivalently, the bare `s_3(A)>=1` case still needs a product-preserving diffuse/grouped mechanism; Theorem 2.1 cannot manufacture reserve modes that are not present.

A useful next B12 question is therefore:

`QFORM-SPECTRAL-PACKET-TO-DIFFUSE-CARRIER-v1`: when the packet budget is exhausted at exactly three final large modes and all quantitative physical pivots are small, prove that the remaining spectral mass forces one of the already-paid grouped-bank/ridge/projected-crossing mechanisms, with no reliance on a single good minor.

This is a different mechanism from r40-r42 and retains every current correction. Full QFORM remains **OPEN / NOT PROVED / NOT DISPROVED**. The full continuous-density conclusion remains open as well.
