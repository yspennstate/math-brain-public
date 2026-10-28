SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account02, slot B20, 2026-09-23T20:03:00Z.
attacking: the first unpaid r37 heavy-or-coherent-planar-twist edge after the canonical common-frame compiler; determine whether the exact coherent endpoint itself forces a paid third resource, and if not identify the correct global third-mode escape while retaining original-coordinate product provenance.

# account02/B20 — exact common-Gram third-mode escape and target-valid exterior stress

Programme: `QFORM-DENSITY-3EIG-20260922`  
Run: `20260923T200300Z-account02-B20-QFORM-auto11`  
Role: proof closure and keeper / SYNTHESIS  
Status: **ESSENTIAL STEP APPLIED / EXACT COMMON-GRAM THIRD-MODE ESCAPE / LOCAL-CLOSURE SHORTCUT REFUTED BY TARGET-VALID FAMILY / FULL QFORM OPEN**  
Execution: **WITHOUT_VERIFIED_BRAIN**.

The unrestricted target remains OPEN: for arbitrary dimension, arbitrary independent real original coordinates with probability densities bounded by one, and arbitrary real symmetric `A` with at least three eigenvalues of modulus at least one, prove one universal finite essential density bound for `X^TAX`, or give a valid counterexample. No Gaussianity, log-concavity, moment, support, iid, diagonal-basis, spectral-coordinate-independence, conditional-cap, or post-rotation-independence assumption is introduced. Global continuity remains a separate question.

## 1. Fresh controls and source boundary


Fresh account-local keeper inspection found the same twenty account02 tasks `B01`--`B20`, all enabled, hourly-valid, QFORM-directed and quiet. B20 was available. No native prompt/title/state repair was needed, so no mutation lease, re-enable, duplicate creation or B19 fallback was used.

The required historical source was reread at

`yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`

under

`proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/`,

including `RESULTS.md`, `FOURIER_ROUTE_REPORT.md`, and `COUNTEREXAMPLE_SEARCH.md`. Section 6 below applies its proved Fresnel--Brascamp--Lieb Theorem F to an explicit target-valid stress family and obtains the actual bound `||p_Q||_infinity<=12`. For reference, its unrestricted fifth-volume theorem also gives, on any literal physical cross block `M`,

`e_5(M^T M)>=1/1024  =>  ||p_Q||_infinity<=10 sqrt(2e)<23.317`,   (1.1)

with no fifth-volume marginal condition.

## 2. Newest completed designated partner and canonical peer refinement

The newest compatible completed designated partner at the final partner refresh remained account03/B20 r37,

`yspennstate/math-open-problems@598dae792b4a447492bc318bfa830fece803bb6d`,

`proofnet24/QFORM-density/fleet-2026-09-22/account03/B20/20260923T184417Z-account03-B20-QFORM-r37/REPORT.md`.

Its diffuse branch gives disjoint ORIGINAL-coordinate banks `D_1,D_2,K`, one common two-dimensional physical `K`-plane, and a partition

`K=K_1 disjoint_union K_2 disjoint_union K_3`

such that every one of the six physical arms remains rank two at the exact scale

`boxed: a_D=0.002408434254376076...`,                              (2.1)

namely

`s_2(A[D_r,K_b])>a_D`, `r=1,2`, `b=1,2,3`.                       (2.2)

Its alternative heavy branch is one literal physical `k in K` with both arm norms exceeding

`a_H=0.0017696480672893325`.                                      (2.3)

This run consumes the exact expression (2.1) below.

The freshest compatible completed peer refinement is account01/B20 at

`yspennstate/math-open-problems@1823cacff7116a3c7c2ebb6c9eb3e2dae297e2db`,

`proofnet24/QFORM-density/fleet-2026-09-22/account01/B20/20260923T192349Z-account01-B20-QFORM-auto11/REPORT.md`.

It replaces independent left/right singular frames inside each `K_b` by one canonical physical frame

`W_b=P_(K_b)V (V^T P_(K_b)V)^(-1/2)`,                             (2.4)

so ambient symmetry is exact in the compressed network. Put

`A_b=U_1^T A[D_1,K_b]W_b`,
`B_b=W_b^T A[K_b,D_2]U_2`,
`C=U_1^T A[D_1,D_2]U_2`,
`D_ab=W_a^T A[K_a,K_b]W_b`, `a!=b`.                              (2.5)

Then

`s_2(A_b),s_2(B_b)>a_D`,                                         (2.6)

and

`D_ba=D_ab^T`.                                                    (2.7)

The prior account02/B20 Schur-minor identity survives in these canonical frames. If

`S_ab:=B_a-D_ab A_b^(-1)C`,                                      (2.8)

then for the literal original-coordinate mixed cut `M_ab=A[D_1 union K_a,K_b union D_2]`,

`e_3(M_ab M_ab^T)>a_D^4 ||S_ab||_F^2`.                           (2.9)

A defect `||S_ab||_F>=a_D^2` is already paid by the completed marginal-free physical `E_3` receiver by `<32679.823`. Thus every still-unpaid diffuse state has all six dimensionless maps

`R_ab:=B_a^(-1)D_ab A_b^(-1)C`                                   (2.10)

satisfying

`||R_ab-I_2||_op<a_D`.                                           (2.11)

At the exact endpoint `R_ab=I_2` for all ordered `a!=b`, the peer compiler proves the exact common-Gram factorization: there is one invertible symmetric `2 x 2` matrix `E` and invertible node maps `G_i` for the five nodes

`D_1,K_1,K_2,K_3,D_2`

such that every compressed OFF-DIAGONAL node interaction is

`boxed: block(i,j)=G_i^T E G_j, i!=j.`                            (2.12)

The first live question is whether (2.12), together with the owner's third spectral direction, already forces a paid local third-volume configuration. It does not. The correct deterministic statement is the escape theorem below.

## 3. Main theorem — exact common-Gram third-mode escape

### Theorem `QFORM-R37-EXACT-COMMONGRAM-THIRDMODE-ESCAPE-v1`

Assume the exact endpoint (2.12). Let `V_i` be the five pairwise orthogonal physical two-frames (`U_1`, the three `W_b`, and `U_2`) and let

`P:=sum_i V_i V_i^T`, `Q:=I-P`.                                  (3.1)

Assume only the owner's spectral hypothesis at scale `sigma`,

`s_3(A)>=sigma>0`.                                                (3.2)

Define the five self-defect matrices

`Delta_i:=V_i^T A V_i-G_i^T E G_i`.                              (3.3)

Then at least one of the following holds:

`boxed: ||PAQ||_op >= sigma/2`,                                  (3.4)

or

`boxed: max_i ||Delta_i||_op >= sigma/2`,                         (3.5)

or

`boxed: ||QAQ||_op >= sigma/2.`                                  (3.6)

In particular, at the owner scale `sigma=1`, an exact coherent planar-twist endpoint must expose a fixed `1/2` third-mode resource either across the common two-plane network, in a same-node/self defect, or entirely outside the five canonical two-frames.

### Proof

Form the deterministic rank-at-most-two matrix

`Z:=sum_i V_i G_i^T`,
`S:=Z E Z^T`.                                                     (3.7)

Because the physical node frames are orthogonal, `S=PSP`, `rank S<=2`, and for every `i!=j`,

`V_i^T S V_j=G_i^T E G_j=V_i^T A V_j`                            (3.8)

by the exact common-Gram identity (2.12). Therefore

`P(A-S)P=direct_sum_i Delta_i`.                                  (3.9)

Since `rank S<=2`, the operator-norm Eckart--Young/min-max principle gives

`||A-S||_op>=s_3(A)>=sigma`.                                     (3.10)

Relative to `Ran(P) direct_sum Ran(Q)`, and using `QS=SQ=0`,

`A-S = [[direct_sum_i Delta_i, PAQ],
        [QAP,                    QAQ]].`                           (3.11)

Split (3.11) into its block-diagonal and off-diagonal parts. Their operator norms are respectively

`max{max_i||Delta_i||_op,||QAQ||_op}`                             (3.12)

and

`||PAQ||_op`.                                                     (3.13)

The triangle inequality and (3.10) imply

`sigma <= max{max_i||Delta_i||_op,||QAQ||_op}+||PAQ||_op`.       (3.14)

Hence one of the three quantities in (3.4)--(3.6) is at least `sigma/2`. QED.

This theorem is pure deterministic coefficient geometry. It does not rotate the random source and makes no independence claim about the `P` and `Q` projections. Consequently (3.4)--(3.6) are structural resources, not yet density payments.

## 4. Why this is the right replacement and not a local contradiction

The exact common-Gram network has rank two only after its missing self blocks are filled by the latent Gram values `G_i^T E G_i`. The owner hypothesis says that the actual matrix stays at operator distance at least one from every rank-two matrix. Theorem 3 pinpoints exactly where that distance must appear. Thus any proof that tries to derive a contradiction from the six near-identity cycle relations alone is missing the third spectral mode: the mode may live in a self defect, an off-plane coupling, or exterior curvature.

The near-collar case (2.11) is harder because converting its six relative errors into one absolute rank-two approximant without a condition-number loss is not yet justified. The theorem therefore closes the exact endpoint but does not delete the live `a_D` collar.

## 5. Target-valid diffuse exact-collar stress family

The local-contradiction shortcut can be refuted inside the exact target, while retaining all original-coordinate provenance.

Take three `K` banks, each with `q=32` original coordinates. On each choose a real `32 x 2` flat orthonormal Walsh frame `W_b`; every row then has squared norm `2/32=1/16`. Put

`V|_(K_b)=W_b/sqrt(3)`,                                          (5.1)

so `V^T V=I_2`,

`G_b=V^T P_(K_b)V=(1/3)I_2`,                                    (5.2)

and every physical common-plane leverage is

`||V^T e_k||^2=1/48<1/16`.                                      (5.3)

Let `D_1,D_2` each consist of two original coordinates, with physical frames `U_1=U_2=I_2`. Define the active symmetric matrix by zero same-bank blocks and the following cross blocks:

`A[D_1,D_2]=(9/100)I_2`,                                        (5.4)

`A[D_r,K_b]=(1/100) W_b^T`, `r=1,2`,                             (5.5)

`A[K_a,K_b]=(1/900) W_a W_b^T`, `a!=b`.                          (5.6)

All unlisted active blocks are zero and symmetry supplies transposes.

The combined `D_r`-to-`K` map has exact common-plane right range and

`U_r^T A[D_r,K]V=(sqrt(3)/100)I_2`.                              (5.7)

Numerically

`sqrt(3)/100=0.017320508... > beta=0.016516715...`,               (5.8)

and the off-plane tail is exactly zero. Thus this lies on the partner's diffuse side. Its canonical arms are

`A_b=B_b=(1/100)I_2`,                                            (5.9)

so, using the partner's exact scale,

`boxed: s_2(A_b)=s_2(B_b)=1/100>a_D=0.002408434254376076... .}`   (5.10)

The self edge has

`||C||_F=9sqrt(2)/100=0.1272792206...`,                           (5.11)

above the inherited common-plane self-edge threshold `0.1190742512...`. Finally

`D_ab=(1/900)I_2`,                                                (5.12)

and exactly

`D_ab A_b^(-1) C
 =(1/900) I * 100 I * (9/100)I
 =(1/100)I
 =B_a`.                                                          (5.13)

Hence

`boxed: S_ab=0, R_ab=I_2 for all six ordered a!=b.`               (5.14)

So this is an exact coherent common-Gram endpoint, not merely a limiting sequence.

Now add a completely disjoint exterior bank of `m=1024` original coordinates. Let `R_out` be three flat orthonormal Walsh columns on this bank and put

`A_out=R_out R_out^T`.                                            (5.15)

The full matrix is the direct sum

`A=A_active direct_sum A_out`.                                   (5.16)

The outside block has three eigenvalues exactly `1`, so

`s_3(A)>=1`.                                                      (5.17)

Moreover the full matrix lies in the standard no-pivot chamber `N3(1/64)`. On the active block every physical diagonal is zero and every physical off-diagonal entry has modulus at most `9/100`, so each two-coordinate principal determinant has modulus at most

`(9/100)^2=81/10000=0.0081<1/64`.                                (5.18)

On the outside block every diagonal equals `3/1024<1/64`; since it is positive semidefinite, every two-coordinate determinant is between zero and

`(3/1024)^2=9/1048576<1/64`.                                     (5.19)

Mixed active/outside pairs have determinant zero. Therefore all scalar and pair no-pivot inequalities hold.

This family refutes the structural shortcut

`exact r37 common-Gram collar + N3 + s_3(A)>=1  => local in-plane third-volume contradiction`. (5.20)

The third target mode may sit completely outside the local coherent network.

## 6. The stress family is paid, not a QFORM counterexample

Apply the pinned historical Theorem F to the ACTUAL full matrix (5.16). Use the three outside Walsh columns as the rank-three Fresnel frame, with eigenvalues `lambda_1=lambda_2=lambda_3=1`, and choose `I` to be the 1024-coordinate outside bank. The remainder `B=A_active` has `B_II=0`, hence diagonal on `I`. Also

`G_I=R_out^T R_out=I_3`,                                        (6.1)

and every original outside coordinate has leverage

`rho_i^T G_I^(-1)rho_i=3/1024<1/2`.                              (6.2)

Therefore the source theorem gives the actual full-law inequality

`boxed: ||p_(X^T A X)||_infinity<=12.`                           (6.3)

This applies to every choice of the independent cap-one input laws, with arbitrary fragmentation and unbounded support. No exterior random coordinate was rotated. Thus (5.16) is a source-valid stress family, not a counterexample to QFORM.

The same example also illustrates Theorem 3 exactly. Take the latent Gram approximant `S` built from the five active node maps. The actual active self blocks are zero, so the active self defects are `-(9/100)I_2` on the two `D` nodes and `-(1/900)I_2` on the three `K` nodes, all below `1/2`; `PAQ=0`; while the exterior block has `||QAQ||=1`, so the escape occurs through (3.6).

## 7. Strongest current conditional proof graph and first unpaid implication

The newest source-pinned graph is now:

1. account03/B20 r37 gives either the heavy common physical anchor (2.3) or the diffuse three-fan with the exact arm scale `a_D`;
2. on the diffuse branch, the completed account02/B20 Schur identity plus the marginal-free physical `E_3` receiver pays any canonical Schur defect `>=a_D^2` by `<32679.823`;
3. account01/B20 canonicalizes the surviving six relations, preserving exact physical symmetry and producing the common symmetric Gram factorization at zero defect;
4. the present Theorem 3 proves that the exact common-Gram endpoint cannot absorb the owner's third spectral direction invisibly: a fixed `1/2` self/off-plane/exterior resource must remain;
5. the explicit family (5.1)--(5.16) proves that the third mode need not be local to the coherent network, and the pinned Theorem F pays the exterior realization by `12`.

Accordingly the first current unpaid universal implication is sharpened to

`QFORM-R37-HEAVY-OR-NEARGRAM-THIRDMODE-ROUTING-v1`:

under the full original independent cap-one hypotheses, pay either

**H.** the r37 heavy physical common anchor

`||A[D_1,{k}]||_2, ||A[D_2,{k}]||_2>a_H`,                         (7.1)

or

**P.** the canonical diffuse collar

`||R_ab-I_2||_op<a_D` for all six ordered `a!=b`,                 (7.2)

by routing the mandatory third-mode defect into an already-paid literal physical pair, hub/grouped-square, ridge, or physical `E_3/E_5` receiver. At exact defect zero, Theorem 3 supplies the required `1/2` deterministic escape. The genuinely unpaid analytic/structural step is to make this routing stable throughout the finite `a_D` collar **without condition-number loss and without treating `P,Q` projections as independent random coordinates**.

A useful next mechanism is therefore a condition-number-free robustification of Theorem 3 at the level of exterior powers or physical-coordinate aggregate volumes, not another reciprocal local-minor extraction. The heavy branch remains separate.

## 8. Status and integrity

No valid full-target counterexample was found. Full QFORM remains **OPEN / NOT PROVED / NOT DISPROVED**. The new theorem is not a full proof candidate and therefore does not claim the two independent end-to-end reviews required for closure. Global continuity remains separate; continuity is asserted only for already completed Fourier-paid branches whose source theorem supplies it.

Model self-report: `GPT-5.6 Sol`. Requested reasoning effort: maximum actually supported. Configured reasoning effort: `UNKNOWN_NOT_EXPOSED`. Known actual reasoning effort: `UNKNOWN`. Provider reasoning-token and pure-thinking-time counters were not exposed. Wall-clock execution is recorded separately and is not pure thinking time.
