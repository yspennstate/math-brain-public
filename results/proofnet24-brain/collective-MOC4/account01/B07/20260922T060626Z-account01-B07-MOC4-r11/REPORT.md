# MOC4 — spectral-conditioned flat-pair rigidity and the fully saturated stratum

Run: `20260922T060626Z-account01-B07-MOC4-r11`  
Worker: `account01/B07`  
Outcome: **ESSENTIAL_STEP_APPLIED**. Parent MOC4 remains **OPEN**.  
Execution: `WITHOUT_VERIFIED_BRAIN`.

## 1. Source-bound inputs actually consumed

Fresh owner control was read at `c56d5b15a89fd0b58fa29e92da0fcec4bf2458bf`; revision `2026-09-22.2` keeps B07 on MOC4 and stops new installation/benchmark work.

Latest complete campaign-lead handoff consumed: account03/B07 `MOC4-MIXED-CONFORMAL-HESSIAN-GATE-v1`, shared blob `8ff513a0355006854065775e0a614f4857846097`. For a row-plane pair `(alpha,gamma)`, with `A_beta=B_{alpha beta}`, `G_beta=B_{gamma beta}`, `deltaX_beta=X_{alpha beta}-X_{gamma beta}`, it proves at every true-unitary global support maximizer

`(rho(Abar)+rho(Gbar))^2 <= 4(T^2-C^2)`,

where `Abar=sum_beta deltaX_beta A_beta A_beta^T`, `Gbar=sum_beta deltaX_beta G_beta G_beta^T`, and `rho(S)=||tf(S)||_F/sqrt(2)`. In particular `T>=|C|`.

Assigned partner result consumed: account02/B08 `MOC4-COMMON-BLOCK-EDGE-PAYMENT-v1`, shared blob `73a4822805fdb2e620f8a7fed20bafa16d96fcc8`. It proves exact one-edge convexity off proper common reducing blocks and gives the exact two-edge payment criterion on a `2+2` boundary. I use it only to keep those already-controlled common-block faces separate from the strict mixed-minor interior; no boundary claim below overrides it.

Also used as a consistency dependency: account03/B08 `MOC4-PAIR-BLOCH-ENVELOPE-v1`, shared blob `734da3d26e5444f410cd64d0d82e1024ca091e2d`, which confirms that the pair variations used by the lead are genuine embedded `SU(2)`/true-unitary variations rather than an independent transport relaxation.

## 2. Exact exterior-square normalization

Diagonalize the normal pair and write `A=diag(a_1,...,a_4)`, `B=diag(b_1,...,b_4)`, with relative unitary `U`. Cauchy-Binet gives the exact identity

`det(A+U B U*) = sum_{k=0}^4 sum_{|S|=|T|=k} a_{S^c} b_T |det U[S,T]|^2`.

For the middle layer `k=2`, group the six two-subsets into the three complementary pairings

`P1={12,34}`, `P2={13,24}`, `P3={14,23}`.

After the standard self-dual/anti-self-dual real basis change, `O=Lambda^2 U in SO(6)` is a `3 x 3` matrix of real `2 x 2` blocks `B_{alpha beta}`. Put

`R_{alpha beta}=(1/2)||B_{alpha beta}||_F^2`,  `D_{alpha beta}=det(B_{alpha beta})`.

The nonconstant support functional has the inherited exact form

`s(O)=<D,K>+(1/2)<R,X>`

(up to the same support-direction-dependent constant at every point and every Weyl endpoint).

For the symmetric middle coefficients define

`p_1=a1*a2+a3*a4`, `p_2=a1*a3+a2*a4`, `p_3=a1*a4+a2*a3`,

`q_1=b1*b2+b3*b4`, `q_2=b1*b3+b2*b4`, `q_3=b1*b4+b2*b3`.

Then, with support direction `eta`,

`X_{alpha beta}=Re(eta p_alpha q_beta)`.

This follows directly by adding the four complementary `k=2` coefficients in a block; the alternating combination gives the `K` channel.

## 3. New quantitative theorem: `MOC4-SPECTRAL-CONDITIONED-FLAT-RIGIDITY-v1`

Fix a row plane `alpha`, and let `gamma,delta` be the other two row planes. Define the two coefficient-difference vectors

`x^{alpha gamma}=(X_{alpha1}-X_{gamma1}, X_{alpha2}-X_{gamma2}, X_{alpha3}-X_{gamma3})`,

`x^{alpha delta}=(X_{alpha1}-X_{delta1}, X_{alpha2}-X_{delta2}, X_{alpha3}-X_{delta3})`,

and the `3 x 3` spectral conditioning matrix

`L_alpha = [ 1 1 1 ; x^{alpha gamma} ; x^{alpha delta} ]`.

Let `sigma_alpha=sigma_min(L_alpha)`. For the lead pair gates write

`Q_{alpha gamma}=T_{alpha gamma}^2-C_{alpha gamma}^2 >=0`,
`Q_{alpha delta}=T_{alpha delta}^2-C_{alpha delta}^2 >=0`.

**Theorem.** At every true-unitary global support maximizer, whenever `sigma_alpha>0`,

`sum_beta (R_{alpha beta}^2-D_{alpha beta}^2)
 <= (4/sigma_alpha^2) (Q_{alpha gamma}+Q_{alpha delta}).`       (3.1)

In particular, if the two pair gates adjacent to row `alpha` are saturated (`T=|C|` for both), then

`|D_{alpha beta}|=R_{alpha beta}` for beta=1,2,3.                 (3.2)

Thus every nonzero `2 x 2` exterior block in that row is a scalar multiple of an orthogonal matrix.

### Proof

For every real `2 x 2` block `B`, set

`V(B)=tf(BB^T)=BB^T-(tr(BB^T)/2)I_2`.

Identify the two-dimensional real space of traceless symmetric `2 x 2` matrices isometrically with `R^2` using the norm `rho(S)=||S||_F/sqrt(2)`. If `v_{alpha beta}` is the vector corresponding to `V(B_{alpha beta})`, block-row orthogonality of `O` gives

`sum_beta B_{alpha beta}B_{alpha beta}^T=I_2`, hence `sum_beta v_{alpha beta}=0`.   (3.3)

The lead mixed-conformal Hessian theorem gives, separately for the `alpha` row contribution,

`|| sum_beta x^{alpha gamma}_beta v_{alpha beta} || <= 2 sqrt(Q_{alpha gamma})`,

`|| sum_beta x^{alpha delta}_beta v_{alpha beta} || <= 2 sqrt(Q_{alpha delta})`.   (3.4)

Let `V_alpha` be the `2 x 3` matrix whose beta-th column is `v_{alpha beta}`. Equations (3.3)-(3.4) say

`V_alpha L_alpha^T = [0, y_gamma, y_delta]`,

with `||y_gamma||^2<=4Q_{alpha gamma}` and `||y_delta||^2<=4Q_{alpha delta}`. Therefore

`sigma_alpha^2 ||V_alpha||_F^2 <= ||V_alpha L_alpha^T||_F^2
 <=4(Q_{alpha gamma}+Q_{alpha delta}).`                         (3.5)

For a `2 x 2` real matrix with singular values `s1,s2`,

`rho(V(B))^2=((s1^2-s2^2)^2)/4
 = ((s1^2+s2^2)/2)^2-(s1*s2)^2
 = R(B)^2-D(B)^2`.                                               (3.6)

Thus `||V_alpha||_F^2=sum_beta(R^2-D^2)`, proving (3.1). Saturation makes the right side zero, proving (3.2). QED.

A completely symmetric column version holds with the transposed coefficient-difference conditioning matrix.

## 4. Exact spectral meaning of the conditioning determinant

The conditioning determinant factorizes exactly. For example, for `alpha=1`, `gamma=2`, `delta=3`, write `z=eta(p1-p2)` and `w=eta(p1-p3)`. Then

`det L_1 = Im(z conjugate(w)) * det[ 1 1 1 ; Re(q1) Re(q2) Re(q3) ; Im(q1) Im(q2) Im(q3) ].`   (4.1)

Hence, up to sign,

`|det L_1| = |eta|^2 |Im((p1-p2) conjugate(p1-p3))|
                    * |Im((q1-q2) conjugate(q1-q3))|`.          (4.2)

The elementary difference identities are

`p1-p2=(a2-a3)(a1-a4)`,
`p1-p3=(a2-a4)(a1-a3)`,

and analogously for `q` and the `b` spectrum. Therefore for simple spectra the first area factor vanishes exactly when

`((a2-a3)(a1-a4))/((a2-a4)(a1-a3))` is real,                    (4.3)

and similarly for `b`. This is precisely the real-cross-ratio (generalized-circle/line) degeneracy. So away from repeated spectra and real-cross-ratio spectral loci, all three row conditioning matrices are invertible.

For a fully explicit quantitative version, the elementary singular-value estimate

`sigma_min(L) >= 2|det L|/||L||_F^2`

gives

`sum_beta(R_{alpha beta}^2-D_{alpha beta}^2)
 <= (||L_alpha||_F^4/|det L_alpha|^2)
    (Q_{alpha gamma}+Q_{alpha delta}).`                          (4.4)

This makes the only loss explicit: the estimate deteriorates exactly as the spectral cross-ratio approaches the real axis.

## 5. New exact closure of the fully row-saturated generic stratum

Assume the spectral conditioning is nondegenerate and **all three row-pair Hessian gates saturate**:

`T_12=|C_12|`, `T_13=|C_13|`, `T_23=|C_23|`.                    (5.1)

Applying (3.2) to each row yields

`|D_{alpha beta}|=R_{alpha beta}` for all alpha,beta.             (5.2)

I now prove this whole stratum is MOC4-safe; no density assumption is needed.

For every nonzero block define its orientation sign

`epsilon_{alpha beta}=D_{alpha beta}/R_{alpha beta} in {+1,-1}`.

Take two distinct block rows `alpha,gamma`. Orthogonality gives

`sum_beta B_{alpha beta} B_{gamma beta}^T=0`.                    (5.3)

Every nonzero summand is a positive scalar times an element of `O(2)`, and its determinant sign is `epsilon_{alpha beta} epsilon_{gamma beta}`. The orientation-preserving and orientation-reversing `2 x 2` matrices lie in the two orthogonal two-dimensional subspaces

`span{I,J}` and `span{diag(1,-1), [[0,1],[1,0]]}`.

Because there are only three beta-values, if both determinant-sign classes occurred among the nonzero summands in (5.3), one class would contain exactly one term (for two terms it is `1+1`; for three terms it is `1+2`). Projecting (5.3) to that subspace would leave one nonzero matrix equal to zero, impossible. Hence for every pair of rows the relative sign `epsilon_{alpha beta}epsilon_{gamma beta}` is constant over their common nonzero columns. The symmetric column statement follows identically.

Consequently every 4-cycle of the bipartite support graph of `R` has positive sign product. An induced 6-cycle is impossible: in a `3+3` bipartite graph it would make some two block rows have exactly one common nonzero column, contradicting (5.3). Thus every cycle has positive sign product, and the edge signs factor on each component:

`epsilon_{alpha beta}=s_alpha t_beta` on every nonzero block,     (5.4)

for signs `s_alpha,t_beta in {+1,-1}`. Equation (5.4) also gives `D_{alpha beta}=s_alpha t_beta R_{alpha beta}` on zero blocks because both sides vanish.

Choose block-diagonal real plane reflections with determinants `s_alpha` and `t_beta` and multiply `O` on the left/right. By (5.4) every resulting `2 x 2` block is orientation-preserving, so the transformed real `6 x 6` matrix is complex-linear. Since it is orthogonal and invertible, its real determinant is `|det_C M|^2=+1`. As `det O=+1`, this forces

`(product_alpha s_alpha)(product_beta t_beta)=+1`.               (5.5)

Also `R` is doubly stochastic, because the block row and column Frobenius norms each sum to `2`. Therefore

`s(O)=sum_{alpha,beta} R_{alpha beta}
      [s_alpha t_beta K_{alpha beta}+X_{alpha beta}/2]
 <= max_{rho in S3} sum_alpha
      [s_alpha t_{rho(alpha)} K_{alpha,rho(alpha)}
       +X_{alpha,rho(alpha)}/2]`.                                (5.6)

For fixed `rho`, the three signs `e_alpha=s_alpha t_{rho(alpha)}` have product `+1` by (5.5). Under the exact exterior-square Weyl action `S4 -> S3` on the three complementary pairings, the kernel is the Klein four group; its four lifts of a fixed `rho` give exactly the four sign triples with product `+1`. Hence every right-hand assignment value in (5.6) is an actual one of the 24 MOC4 Weyl endpoint support values. Thus

`s(O) <= max_{sigma in S4} s(O_sigma)`.                           (5.7)

This proves:

**Corollary `MOC4-FULLY-SATURATED-ROW-STRATUM-v1`.** A positive-gap MOC4 support maximizer with non-real-cross-ratio spectral conditioning cannot have all three row mixed-conformal Hessian gates saturated. The same holds with rows and columns interchanged.

## 6. Compact conditional end-to-end argument

Assume a source-valid MOC4 counterexample exists for a fixed support direction. Compactness gives a true-unitary global support maximizer with positive gap over the 24 Weyl endpoints.

1. Repeated/common-reducing-block faces stay under the partner account02/B08 boundary machinery; its exact edge-payment theorem is not bypassed here.
2. In the remaining simple-spectrum irreducible core, the campaign lead gives `T_{alpha gamma}>=|C_{alpha gamma}|` and the mixed-conformal Hessian bound for every pair.
3. If both spectra avoid the real-cross-ratio locus and all three row gates are saturated, Sections 3-5 force `|D|=R`, factor the orientation signs, and reduce the support to a genuine six-assignment Weyl subfamily, contradicting positive gap.
4. Therefore every generic positive-gap maximizer must have at least one **strict** mixed-conformal row margin `T>|C|`; quantitatively, any nonconformality `R^2-D^2` is paid by the adjacent `T^2-C^2` margins through (3.1)/(4.4).

So the fully flat/saturated generic interior is no longer an open obstruction.

## 7. First surviving implication

The first unpaid generic implication is now the **strict-margin payment problem**:

`MOC4-STRICT-MARGIN-SPECTRAL-PAYMENT-v1` — combine the quantitative bound

`sum_beta(R_{alpha beta}^2-D_{alpha beta}^2)
 <= 4(Q_{alpha gamma}+Q_{alpha delta})/sigma_alpha^2`

with the lead V4/subgroup roofs, pair-gap ceiling and the exact structured spectral formulas for `(K,X)` to show that a positive support gap cannot afford the required strict `Q`-mass. The separate exceptional spectral locus is exactly the repeated/real-cross-ratio locus identified by (4.2)-(4.3), rather than an unspecified algebraic degeneracy.

No claim is made that this final strict-margin implication has been proved. MOC4 remains open.

## 8. Verification note

The identities (3.6), (4.1), and the two `p`-difference factorizations were independently checked in exact rational arithmetic during this run. The checks are diagnostic only; the proofs above are algebraic and do not depend on numerical sampling.
