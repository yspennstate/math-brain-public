SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B11, 2026-09-23T09:15:49Z.
attacking: exact-rank-three indefinite pair completion — cancel the local pair determinant against the third Schur curvature, then splice the resulting exterior-area certificate with bank aggregation and the current volume exit.

# account01/B11 — pair-extension mass cancellation and an exterior-area compiler

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Run:** `20260923T091549Z-account01-B11-QFORM-auto11`  
**Status:** `ESSENTIAL_STEP_APPLIED / PROVED_SUPPORTING_THEOREM / FULL_TARGET_OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`  
**Continuity:** the new pair-area theorem proves essential boundedness only; the volume-stability subbranch below has a continuous `C_0` density.

## 1. Source boundary

The owner target is unchanged: independent real original coordinates with probability densities bounded by one, arbitrary symmetric `A` with at least three eigenvalues of modulus at least one, no moments, bounded support, log-concavity, connected support, Gaussianity, or post-rotation independence.

This run uses the following completed results at their exact scopes.

1. **Orientation-free scalar pivot / rank-two half-Riesz**, source  
   `yspennstate/math-open-problems@e542b1a6ef471b329e4e88a6553e1aacb45acc1a`,  
   `proofnet24/QFORM-density/interactive/20260922T161801Z-rank-two-fusion/REPORT.md`.  
   If an original-coordinate exact-rank-three block is `V M V^T`, `V^T V=I_3`, row `i` has leverage `c_i`, and its physical diagonal is `a!=0`, then the FULL ambient quadratic form, including arbitrary outside blocks/couplings and induced affine terms, satisfies

   `||p_Q||_inf <=128 [c_i |a| |det M|]^(-1/4)`.                 (1.1)

2. **Physical indefinite-pair logarithmic smoothing**, source  
   `yspennstate/math-open-problems@f7f0fedb2d93b46824f96cac1164af6f8a55626f`,  
   `proofnet24/QFORM-density/interactive/20260922T180015Z-pair-log/PAIR_LOG_THEOREM.md`.  
   For an invertible indefinite original-coordinate pair `B`, `D=|det B|`, `kappa=sigma_min(B)`, after pair completion a rank-one remainder `lambda(h dot X)^2+affine` has the small-ball constant `H<=10/sqrt(|lambda|)`. Equations (1.3), (4.2) and Section 5 of that source therefore give the more precise pre-simplification

   `||p_Q||_inf <=8 sqrt(5) [D kappa |lambda|]^(-1/4)`.          (1.2)

   The source normally replaces `|lambda|` by the global spectral scale; this run keeps the exact `lambda` and proves a cancellation identity for it.

3. **Designated partner `account02/B11`**, source  
   `yspennstate/math-open-problems@f2835c54b9f384f8f83e34c46bef5c40953e32a7`,  
   `proofnet24/QFORM-density/fleet-2026-09-22/account02/B11/20260923T042112Z-account02-B11-QFORM-2f47d35a/REPORT.md`.  
   Its `QFORM-INDEFINITE-PAIR-DIFFUSE-SQUARE-v1` theorem states that an independent cap-one physical pair with invertible matrix `B`, plus an independent scalar `W` of density cap `L` and coefficient `d!=0`, obeys

   `||p||_inf <=16 sqrt(30) L |det B|^(-1/4)|d|^(-1/2)`.        (1.3)

4. **Current volume-stability theorem**, source  
   `yspennstate/math-open-problems@c2414ef633b9d4b7f04a83e1aeefbe713ed82bba`,  
   `proofnet24/QFORM-density/interactive/20260923T002323Z-volume-stability/REPORT.md`.  
   For an original-coordinate cross block `C` with `s_3(C)>=a` and row-range leverage at most `1/2`, the specialization `M_0=C,E=0` gives a continuous density `<23/a`, retaining arbitrary self blocks and outside couplings.

5. **Newest Claude ruled one-sheet theorem**, source  
   `yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`,  
   `proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/COUNTEREXAMPLE_SEARCH.md`, Theorem C. For exact rank three with signature `(2,1)` and spectral scale at least one, `p_Q(t)<=pi sqrt(2)` on `t>=0`; reflection gives the `(1,2)` statement on `t<=0`. Scaling gives `pi sqrt(2)/s` at spectral scale `s`.

The live corrections are retained: no arbitrary-joint rank-three coarea, no positive moment of worst conditional projection heights, no law-uniform pointwise quadratic-phase decay, no conditional-density-as-independence substitution, and no rotation of the product law.

## 2. Exact pair-extension identity

Let

`A=R M R^T`, `R^T R=I_3`,                                      (2.1)

where `M` is invertible symmetric. The argument below is algebraic and does not yet use its signature. Fix distinct original-coordinate rows `r_i,r_j` and write

`P=[r_i^T; r_j^T]`, `G=P P^T`, `g_ij=det G=||r_i wedge r_j||^2`. (2.2)

Assume `g_ij>0`, so the two spectral rows are linearly independent, and let

`B=P M P^T=A[{i,j},{i,j}]`.                                      (2.3)

### Theorem 2.1 — `QFORM-PAIR-EXTENSION-MASS-CANCELLATION-v1`

If `B` is invertible, let `lambda` denote the signed coefficient of the rank-one Schur remainder after completing the physical pair `B`, in the normalized spectral construction of the pair-log theorem. Then

`boxed: det(B) lambda = det(M) g_ij.`                              (2.4)

Moreover

`boxed:
 |det(B)| |lambda|
 = |det M| g_ij
 = sum_(k notin {i,j}) |det A[{i,j,k},{i,j,k}]|.`                 (2.5)

Thus the local pair determinant and the third Schur curvature are reciprocal pieces of one invariant: the total physical three-volume extending the pair.

### Proof

Make an orthogonal change of basis **only in the three-dimensional deterministic spectral space**, not in the random input coordinates, so that

`P O=[F,0]`,                                                       (2.6)

with `F` invertible `2x2`. Then

`g_ij=det(PP^T)=det(F)^2`.                                        (2.7)

Write

`O^T M O = [[L,k],[k^T,d]]`.                                      (2.8)

Since `B=F L F^T`, invertibility of `B` is equivalent to invertibility of `L`, and

`det B = det(F)^2 det L = g_ij det L`.                            (2.9)

The scalar Schur coefficient is exactly

`lambda=d-k^T L^(-1) k`,                                         (2.10)

while the block determinant formula gives

`det M=det L * lambda`.                                           (2.11)

Equations (2.9)--(2.11) prove (2.4).

For the second identity, set `n=r_i x r_j`. For every `k` distinct from `i,j`,

`det A[{i,j,k},{i,j,k}]
 = det M * det(R_{ijk})^2
 = det M * (n dot r_k)^2`.                                        (2.12)

All these determinants have the sign of `det M`. Parseval now gives

`sum_k (n dot r_k)^2
 = n^T (sum_k r_k r_k^T) n
 = ||n||^2
 = g_ij`.                                                         (2.13)

Taking absolute values proves (2.5). QED.

A useful equivalent Hodge identity, obtained directly from `adj(M)=det(M)M^(-1)`, is

`det B = det M * n^T M^(-1)n`.                                   (2.14)

For signature `(2,1)`, an indefinite physical pair has `det B<0` and `det M<0`, so `lambda>0`; for signature `(1,2)` the signs reverse and `lambda<0`. The third Schur direction therefore has exactly the majority sign required by inertia additivity.

## 3. The local logarithmic singularity loses its determinant cost

Assume now that `B` is invertible and indefinite and write

`D=|det B|`, `kappa=sigma_min(B)`.                                (3.1)

Apply the exact pre-simplification (1.2), not the weaker replacement `|lambda|>=s`. By (2.5),

`D |lambda|=|det M|g_ij`,                                        (3.2)

and therefore

`boxed:
 ||p_Q||_inf
 <=8 sqrt(5) [kappa |det M| g_ij]^(-1/4).`                       (3.3)

This is the first main gain of the run. A tiny physical determinant is no longer itself a loss. If `D` tends to zero while the two spectral rows retain area, the third Schur curvature necessarily tends to infinity in exactly the compensating amount.

The only local degeneration left in (3.3) is the small singular value `kappa` of the pair. The next step shows that this degeneration forces a scalar pivot unless the pair is quantitatively indefinite.

## 4. Area-only local compiler for every physical row pair

Assume that `M` has signature `(2,1)` or `(1,2)` and

`min_j |lambda_j(M)| >= s>0`.                                    (4.1)

### Theorem 4.1 — `QFORM-INDEFINITE-PAIR-AREA-COMPILER-v1`

For every original row pair with `g_ij>0`, the full quadratic form covered by the exact-rank-three block satisfies

`boxed:
 ||p_Q||_inf <= 128 sqrt(2) / (s sqrt(g_ij))
             < 181.020 / (s sqrt(g_ij)).`                        (4.2)

The conclusion permits arbitrary outside blocks/couplings and affine terms whenever the pair lies in an original-coordinate principal block to which the source theorems (1.1)--(1.2) apply. In particular it applies to every full exact-rank-three target matrix.

### Proof

Let the eigenvalues of `G` be `gamma_1>=gamma_2>0`. Since `RR^T` is an orthogonal projection, its principal `2x2` block `G` satisfies `G<=I_2`, hence

`gamma_1<=1`, `gamma_2=g_ij/gamma_1>=g_ij`.                       (4.3)

Both row leverages are diagonal entries of `G`, so

`||r_i||^2, ||r_j||^2 >= gamma_2>=g_ij`.                          (4.4)

Define the orthonormal spectral two-frame

`V=P^T G^(-1/2)`, `V^T V=I_2`,                                   (4.5)

and its compression

`C=V^T M V`.                                                      (4.6)

By Cauchy interlacing, in signature `(2,1)` the larger eigenvalue of `C` is at least the second positive eigenvalue of `M`, hence at least `s`; in signature `(1,2)` the smaller eigenvalue of `C` is at most the second negative eigenvalue of `M`, hence at most `-s`. Thus in either signature

`||C||_op>=s`.                                                     (4.7)

Since

`B=G^(1/2) C G^(1/2)`,                                            (4.8)

we have `C=G^(-1/2)BG^(-1/2)` and therefore, with `L=||B||_op`,

`L>=gamma_2 ||C||_op >= s g_ij`.                                 (4.9)

Let `kappa=sigma_min(B)`, allowing `kappa=0` if `B` is singular.

**Pivot branch.** If `kappa<L/2`, the two eigenvalues of `B` either have the same sign, in which case `|tr B|>=L`, or opposite signs, in which case `|tr B|=L-kappa>L/2`. Hence some diagonal entry `a` of `B` satisfies

`|a|>|tr B|/2 > L/4 >= s g_ij/4`.                                (4.10)

If instead `kappa>=L/2` but `B` is definite, then `|tr B|=L+kappa>=L`, so again some diagonal obeys the stronger `|a|>=L/2`. Thus every case except an invertible indefinite well-conditioned pair has a physical scalar pivot satisfying (4.10).

For that pivot, its spectral row leverage `c` is at least `g_ij` by (4.4), and `|det M|>=s^3`. Apply (1.1):

`||p_Q||_inf
 <=128 [c |a| |det M|]^(-1/4)
 <=128 [g_ij * (s g_ij/4) * s^3]^(-1/4)
 =128 sqrt(2)/(s sqrt(g_ij)).`                                    (4.11)

**Indefinite-pair branch.** The only remaining case is invertible indefinite `B` with

`kappa>=L/2>=s g_ij/2`.                                          (4.12)

Apply the determinant-cancelled logarithmic estimate (3.3):

`||p_Q||_inf
 <=8sqrt(5)[(s g_ij/2)*s^3*g_ij]^(-1/4)
 =8sqrt(5) 2^(1/4)/(s sqrt(g_ij))
 <21.274/(s sqrt(g_ij)),`                                         (4.13)

which is smaller than (4.11). This proves (4.2). QED.

Theorem 4.1 is sign-specific in its proof but symmetric under `A -> -A`: the same constant holds for `(2,1)` and `(1,2)`.

## 5. Exact exterior-frame bookkeeping

The quantity `g_ij` has two useful global identities that show exactly what remains after Theorem 4.1:

`boxed: sum_(i<j) g_ij = 3,`                                      (5.1)

and, with `h_i=||r_i||^2`,

`boxed: sum_(j!=i) g_ij = 2 h_i.`                                 (5.2)

For (5.1), apply Cauchy--Binet to the second exterior power of `R`: the eigenvalues of `R^T R` are `1,1,1`, so `e_2(R^TR)=3`, while each row-pair contribution is `det(PP^T)=g_ij`. For (5.2), expand

`g_ij=h_i h_j-(r_i dot r_j)^2`,                                   (5.3)

sum in `j`, use `sum_j h_j=3`, and use

`sum_j (r_i dot r_j)^2=r_i^T(R^TR)r_i=h_i`.                       (5.4)

Thus a hard sequence for the local compiler cannot lose two-dimensional spectral area globally; it can only distribute the fixed total area `3` over more and more physical pairs. This is the exact aggregation debt.

In particular, for any threshold `gamma>0`, if some `g_ij>=gamma` then

`||p_Q||_inf <181.020/(s sqrt(gamma)).`                            (5.5)

The remaining exact-rank-three frames satisfy `max g_ij<gamma` and hence are genuinely diffuse in the **exterior** frame, even if some one-row leverages are large.

## 6. Current volume theorem applied to the complementary balanced-cut exit

The newest volume-stability theorem gives a second, genuinely collective exit from that exterior-diffuse chamber.

For a coordinate cut `S,T=S^c`, write

`G_S=R_S^T R_S`, `G_T=I-G_S`.                                    (6.1)

Assume for some `0<eta<=1/2` that

`eta I <= G_S <= (1-eta)I`,                                      (6.2)

and that every normalized row leverage on the `S` side obeys

`r_i^T G_S^(-1) r_i <=1/2,  i in S`.                             (6.3)

The actual cross block is

`C=A[S,T]=R_S M R_T^T`.                                           (6.4)

Put

`U_S=R_S G_S^(-1/2)`, `U_T=R_T G_T^(-1/2)`.                      (6.5)

Both have orthonormal columns, and

`C=U_S [G_S^(1/2) M G_T^(1/2)] U_T^T`.                           (6.6)

Therefore

`s_3(C)>=s sqrt(lambda_min(G_S)lambda_min(G_T))>=s eta`.          (6.7)

Because the middle `3x3` factor is invertible, `range(C)=range(R_S)`, whose orthogonal projection has diagonal exactly the normalized leverages in (6.3). Applying the current volume theorem with `M_0=C,E=0,a=s eta` yields

`boxed:
 ||p_Q||_inf <23/(s eta),`                                        (6.8)

and this subbranch has a continuous density vanishing at infinity.

Consequently, at fixed `gamma,eta`, the only exact-rank-three frame geometry not covered by either (5.5) or (6.8) is:

- every physical row-pair area satisfies `g_ij<gamma`, **and**
- every spectrally balanced cut (6.2) has a normalized row leverage exceeding `1/2` on the chosen side.

This is a sharper product-preserving formulation of the remaining high-leverage/grouped-coordinate obstruction; no small physical determinant remains in the statement.

For the concrete bookkeeping choice `gamma=1/64`, `eta=1/8`, the two paid bounds are respectively `<1448.155/s` and `<184/s`. These constants are not proposed as sharp; the point is the structural separation.

## 7. Designated partner applied to an actual family: local area can vanish while bank smoothing stays uniform

The partner theorem is useful precisely because Theorem 4.1 cannot finish by selecting one physical pair.

Take three disjoint original-coordinate banks of size `m`, with normalized bank vectors

`u=(1,...,1)/sqrt(m)`, `v=(1,...,1)/sqrt(m)`, `w=(1,...,1)/sqrt(m)`, (7.1)

and let

`Y_1=u dot X_(bank1)`, `Y_2=v dot X_(bank2)`, `Y_3=w dot X_(bank3)`. (7.2)

For real `a,d` with `|a|,|d|>=s>0`, consider

`Q=2a Y_1Y_2+dY_3^2`.                                             (7.3)

Its reduced `3x3` spectrum is exactly `{a,-a,d}`, so it realizes either indefinite signature according to the sign of `d` and has three eigenvalue magnitudes at least `s`.

Each normalized product-bank projection has density at most `sqrt(2)`, and the three are genuinely independent because their ORIGINAL coordinate supports are disjoint. Set `Z_k=sqrt(2)Y_k`; then the `Z_k` are independent cap-one variables and

`Q=Z_(1,2)^T [[0,a/2],[a/2,0]] Z_(1,2) +(d/2) Z_3^2`.            (7.4)

Apply designated partner `account02/B11`, equation (1.3), with

`|det B|=a^2/4`, `L=1`, `|d_partner|=|d|/2`.                     (7.5)

This gives the actual uniform inequality

`boxed:
 ||p_Q||_inf
 <=32 sqrt(30)/sqrt(|a d|)
 <=32 sqrt(30)/s
 <175.272/s,`                                                     (7.6)

independently of `m` and of all admissible fragmented cap-one product laws.

Yet every spectral row in the first bank has direction `e_1/sqrt(m)` and every row in the second bank has direction `e_2/sqrt(m)`, so an individual cross-bank physical pair has

`g_ij=1/m^2`.                                                      (7.7)

The local area compiler (4.2) therefore deteriorates at least linearly in `m`; the sharper pair-log branch still deteriorates. Equation (7.6) stays uniform because the partner theorem aggregates the whole independent banks **before** paying the rank-two singularity. This is a concrete proof that the next structural step must aggregate exterior area rather than seek one uniformly large physical pair.

The mandatory rank-two logarithmic control survives inside the same family. If the first two banks are singletons with centered unit uniforms, then

`p_(2aX_1X_2)(t)=|a|^(-1) log(|a|/(2|t|)),  0<|t|<|a|/2`.         (7.8)

The third independent square bank removes that genuine logarithmic singularity by the partner half-Riesz smoothing mechanism; it does not make the rank-two receiver itself bounded.

## 8. Newest Claude one-sheet theorem applied at the exact sign boundary

For an exact-rank-three `(2,1)` target with spectral scale `s`, Claude's ruled Theorem C gives

`boxed: p_Q(t)<=pi sqrt(2)/s,  t>=0.`                              (8.1)

For `(1,2)`, apply it to `-Q`:

`boxed: p_Q(t)<=pi sqrt(2)/s,  t<=0.`                              (8.2)

Thus in a sign-spliced exact-rank-three proof, the one-sheet side is already uniformly paid independently of `g_ij`; Theorem 4.1 is relevant to the opposite two-sheet side and to a full-side bound on any frame with a nonnegligible pair area. The unbounded rank-two control (7.8) lives exactly at the two-sheet/hyperbolic mechanism and is therefore not contradicted by (8.1)--(8.2).

## 9. What changed and the first unpaid implication

Before this run, a good physical indefinite pair carried the cost

`( |det B| * sigma_min(B) * spectral_scale )^(-1/4)`,             (9.1)

so a tiny local pair determinant appeared to be an independent obstruction. The exact identity (2.5) shows that this is false in exact rank three: `|det B|` is paired with the third Schur curvature, and their product is the invariant extension mass `|det M|g_ij`. Combining this with a scalar-pivot fallback removes also the small-`kappa` branch, leaving the single local currency `g_ij`.

The first unpaid B11 implication is therefore sharpened to

**`QFORM-EXTERIOR-AREA-BANK-AGGREGATION-v1`.** In an exact-rank-three Parseval frame with every individual `g_ij` small and no balanced cut satisfying the current volume leverage gate, aggregate the fixed total exterior mass `sum g_ij=3` into disjoint ORIGINAL-coordinate banks and feed one of the already-paid three-bank / pair-plus-square / mixed-Fresnel receivers, without conditioning correlated same-bank transverse statistics. The family (7.1)--(7.7) shows why one physical pair cannot suffice.

After that exact-rank-three aggregation issue is closed, arbitrary extra nonseparable spectrum remains a separate interface to the full owner target. A small matrix tail cannot be deleted as a small random quadratic perturbation under the stated unbounded-support laws.

No full solution or counterexample is claimed. The new theorem has not received an independent end-to-end review in this run.
