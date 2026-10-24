SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account02, slot B04, 2026-09-23T01:47:17Z.
attacking: bridge ridge leverage to admissible fractional three-volume weights at an intrinsic scale, then optimize and compare both certificates on one explicit rotated indefinite matrix with q=1 volume failure.

# account02/B04 auto11 continuation — KL-optimal volume repair and an intrinsic ridge-volume bridge

**Programme:** QFORM-DENSITY-3EIG-20260922  
**Outcome:** PROVED_SUPPORTING_THEOREMS / EXPLICIT TARGET-VALID COMPARISON / FULL TARGET OPEN  
**Execution:** WITHOUT_VERIFIED_BRAIN (authenticated repository retrieval occurred; no native learned-memory receiver use was observed).

## 1. First unpaid implication

The full theorem still needs a product-preserving structural implication from the bare hypothesis `s_3(A)>=1`. The previous B04 run showed that a local physical-pair certificate can diverge while both aggregate three-volume and ridge certificates remain uniformly strong. This run sharpens the aggregate side:

> **QFORM-KL-BALANCED-VOLUME-OR-RIDGE-ROUTING-v1 (OPEN).** Find an original-coordinate cross cut for which either (i) the squared-minor Gibbs law can be moved into the row-marginal cap by universally bounded KL cost while retaining a target-scale third volume, or (ii) a ridge scale has leverage at most `1/2`, effective dimension greater than two, and a target-scale determinant; otherwise route the surviving high-leverage/low-tail hub into an already completed grouped-coordinate mechanism.

The new point is that raw failure of the volume-sampling gate `max alpha_i<=1/2` is not itself the right obstruction: the relevant quantity is the **KL distance of the squared-minor Gibbs law to the admissible marginal polytope**. An explicit target-valid matrix below has `alpha_max>1/2`, but the globally optimal admissible repair costs only `0.00195` nats and gives a stronger certificate than simply increasing the Fourier exponent `q`.

No law-uniform pointwise quadratic-phase decay, arbitrary-joint coarea, conditional projection-density moment, post-rotation independence, or uniformly good physical minor is used.

## 2. Sources actually used at equations

1. Claude Fourier package `yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`, `proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/FOURIER_ROUTE_REPORT.md` and `RESULTS.md`. Its audited Theorem D proves the volume-sampling estimate and, importantly here, records the arbitrary-weight determinant/entropy replacement. It also shows why only row marginals are constrained.

2. Sharp fractional-volume package `yspennstate/math-open-problems@c2414ef633b9d4b7f04a83e1aeefbe713ed82bba`, `proofnet24/QFORM-density/interactive/20260923T002323Z-volume-stability/REPORT.md`. For the squared-minor volume law it proves, for `1<=q<3/2`,

   `||p_Q||_inf <= [3e/((3-2q)sqrt(q))] E3^(-1/6)`

   under `alpha_i<=q/2`. Its status is complete supporting proof, independent review pending.

3. Ridge theorem `yspennstate/math-open-problems@9c1167db05c7b0f520f060796fde921ed769a4e7`, `proofnet24/QFORM-density/interactive/20260922T151048Z-ridge-window/REPORT.md`. For

   `K_gamma=MM^T(gamma^2 I+MM^T)^(-1)`, `theta=tr K_gamma`, `D_gamma=det(I+MM^T/gamma^2)`,

   if `max diag K_gamma<=q/2` and `theta>2q`, then

   `||p_Q||_inf <= e/(sqrt(2q)gamma) * theta/(theta-2q) * D_gamma^(-1/(2theta))`.

4. Designated partner account03/B04, run `20260923T004843Z-account03-B04-qform-auto11`, source commit `48c622953108fd3e77f7b3f5e155e082337804d7`. Its `QFORM-SQUARE-PHYSICAL-PAIR-DETERMINANT-v1` gives

   `||p_Q||_inf <= C_HR |a|^(-1/2)|det B|^(-1/4)`,
   `C_HR=63.11383495773493...`,

   for an outer original-coordinate square over an arbitrary contaminated invertible physical pair. I apply it to the same explicit matrix in Section 6.

## 3. Weighted sharp fractional-volume theorem

Let `I,J` be disjoint ORIGINAL coordinate sets and put `M=A[I,J]`. Index nonzero `3x3` minors by `omega=(S,T)` and set

`a_omega=det(M[S,T])^2`.

Let `w=(w_omega)` be any probability law supported on these nonzero minors. Write

`alpha_i=P_w(i in S)`, `beta_j=P_w(j in T)`,

and define the entropy-adjusted volume

`G(w)=exp( sum_omega w_omega log a_omega + H(w) )`
`    =exp( sum_omega w_omega log(a_omega/w_omega) ).`           (3.1)

Zero weights are omitted in the usual entropy convention.

### Theorem 3.1 — `QFORM-WEIGHTED-FRACTIONAL-VOLUME-SHARP-v1`

For `1<=q<3/2`, if

`max_i alpha_i <= q/2`,                                          (3.2)

then, for arbitrary independent cap-one original-coordinate laws and arbitrary self blocks, outside couplings and affine terms,

`boxed(
 ||p_(X^TAX+b^TX+c)||_inf
 <= [3e/((3-2q)sqrt(q))] G(w)^(-1/6).
)`                                                               (3.3)

The characteristic function is integrable, hence the proof also gives a continuous density vanishing at infinity.

#### Proof

Use the same decoupling as the cited fractional-volume theorem. The only place the squared-minor Gibbs law is used is the determinant lower bound in the Gaussian Brascamp--Lieb constant. For positive row Gaussian parameters `d_i` and active column parameters `e_j`, the diagonal-plus-PSD expansion contains

`Sigma := sum_omega a_omega prod_(i in S)d_i prod_(j notin T)e_j`.

Insert the arbitrary probability weights `w_omega` and apply weighted AM--GM:

`Sigma
 = sum_omega w_omega [ (a_omega/w_omega)
       prod_(i in S)d_i prod_(j notin T)e_j ]`
` >= G(w) prod_i d_i^(alpha_i) prod_j e_j^(1-beta_j).`          (3.4)

Thus the Gaussian BL constant is bounded by

`G(w)^(-1/2)
 prod_i alpha_i^(-alpha_i/2)
 prod_j (1-beta_j)^(-(1-beta_j)/2).`                            (3.5)

All endpoint columns with `beta_j=1` are handled exactly as in the source proof: they belong to every minor of positive weight and are dropped before the BL application, so no inverse zero parameter is introduced.

Now apply Jensen with exponent `q` and the same sharp Hausdorff--Young estimate as in the source theorem. Condition (3.2) is exactly the requirement that the Fourier output exponent `q/alpha_i` be at least two. The powers of `alpha_i` cancel, and the two entropy products are each controlled by the same tangent inequalities, yielding

`|phi_Q(t)| <= min(1,K |t|^(-3/(2q)))`,                         (3.6)

where

`K=[e^3 q^(-3/2) pi^3 G(w)^(-1/2)]^(1/(2q)).`                  (3.7)

Since `3/(2q)>1`, integration of (3.6) and Fourier inversion give exactly (3.3). QED.

For the squared-minor Gibbs law

`w*_omega=a_omega/Z`, `Z=sum_omega a_omega=e3(M^TM)`,           (3.8)

the Gibbs identity is

`log G(w)=log Z-KL(w||w*).`                                    (3.9)

Thus (3.3) makes the price of repairing bad row marginals explicit.

## 4. A ridge-volume matrix bridge at an intrinsic scale

Let `C=MM^T` have eigenvalues `lambda_j>=0`, let

`E2=e2(lambda)`, `E3=e3(lambda)>0`, `rho=E3/E2`,                (4.1)

and let `W` be the third-volume row-marginal matrix, so in a singular-vector basis

`W=U diag(p_j)U^T`,
`p_j=lambda_j e2(lambda without j)/E3`.                         (4.2)

For `a>0`, set

`gamma_a^2=a rho`,
`K_a=C(C+gamma_a^2 I)^(-1).`                                   (4.3)

### Proposition 4.1 — `QFORM-INTRINSIC-RIDGE-VOLUME-BRIDGE-v1`

For every `a>0`,

`boxed(W <= (1+a)K_a).`                                        (4.4)

Consequently

`alpha_i <= (1+a)(K_a)_ii`,
`theta_a:=tr K_a >= 3/(1+a).`                                  (4.5)

In particular, if `0<a<1/2` and

`max_i (K_a)_ii <=1/2`,                                        (4.6)

then the SAME physical cross block simultaneously satisfies:

- the ridge theorem with `q=1`, because `theta_a>2`;
- Theorem 3.1 with the volume-sampling law and `q=1+a`, because `alpha_i<=(1+a)/2`.

#### Proof

From (4.2),

`p_j<=1`,
`p_j<=lambda_j E2/E3=lambda_j/rho`,                             (4.7)

so `p_j<=min(1,x_j)` with `x_j=lambda_j/rho`. For every `x>=0`,

`min(1,x) <= (1+a)x/(a+x)`.                                    (4.8)

The right side of (4.8) is the corresponding eigenvalue of `(1+a)K_a`, proving (4.4). Taking diagonals yields the first part of (4.5); taking traces and using `tr W=sum alpha_i=3` gives the second. If `a<1/2`, `3/(1+a)>2`, and the two stated gates follow. QED.

This does not assert that a suitable cross cut or intrinsic ridge scale always exists under `s_3(A)>=1`; that is the structural obligation in Section 1.

## 5. Explicit target-valid matrix where volume sampling fails at q=1 but KL repair succeeds

Let `H_8` be the Sylvester Hadamard matrix and let `U_0` be its first three columns divided by `sqrt(8)`. Rows 1 and 5 of `U_0` coincide. Put `P_0=U_0U_0^T`. Rotate just those two ORIGINAL coordinate rows by a Givens rotation whose angle satisfies

`sin(2 theta)=5/12`, `cos(2 theta)=sqrt(119)/12`,               (5.1)

and write `P=R_theta P_0 R_theta^T`. Then `P` is a rank-three orthogonal projection and its diagonal is, up to order,

`17/32, 7/32, 3/8,3/8,3/8,3/8,3/8,3/8.`                       (5.2)

Take

`delta=1/100`,
`M_0=delta I_8+(1-delta)P`,
`M=2M_0`.                                                       (5.3)

Thus `M` has singular values `2,2,2,0.02,0.02,0.02,0.02,0.02`. The cross entries are genuinely rotated in the original coordinates. Define the 16-coordinate residual form

`R(X,Y)=2 X^T M Y`.                                              (5.4)

Its matrix `[[0,M],[M,0]]` has eigenvalues `+2` and `-2`, each three times, and `+0.02` and `-0.02`, each five times.

For the volume marginal computation it is convenient to divide all singular values by two and put `epsilon=delta^2=10^-4`. Then

`Z_0=e3(M_0^TM_0)`
`   =1+15 epsilon+30 epsilon^2+10 epsilon^3`
`   =1.00150030001,`                                            (5.5)

while the two spectral weights of `W` are

`p_H=(1+10epsilon+10epsilon^2)/Z_0`
`   =0.9995005493158663...`,

`p_L=epsilon(3+12epsilon+6epsilon^2)/Z_0`
`   =0.0002996704104801599... .`                                (5.6)

Therefore a row with `P_ii=d` has

`alpha(d)=p_L+(p_H-p_L)d`.                                      (5.7)

At the heavy row `d=17/32`,

`alpha:=alpha_max=0.5311251373289666... >1/2`.                  (5.8)

So the sharp `q=1` volume-sampling theorem genuinely does NOT apply. The other seven marginals are `3/8` six times and `0.21887486267103337...` once.

The actual third volume for `M` is

`Z=e3(M^TM)=2^6 Z_0=64.09601920064.`                            (5.9)

### 5.1 Direct fractional-q repair

For the unmodified Gibbs law, the smallest admissible exponent is

`q_*=2 alpha=1.0622502746579332...`.                            (5.10)

The prefactor `3e/[(3-2q)sqrt(q)]` is increasing for `q>1/2`, so this is the best direct choice. Theorem 3.1 at `w=w*` gives

`||p_R||_inf <=4.517601542839662.`                              (5.11)

The older audited D' constant from `e5f71...` gives `5.480127688194701...` on the same data.

### 5.2 Globally KL-optimal q=1 repair

Let `H(omega)=1` when the heavy row belongs to the row triple and zero otherwise. Tilt only this inclusion event:

`w_t(omega)=w*(omega)t^{H(omega)}/Z_t`,
`t=(1-alpha)/alpha`,
`Z_t=(1-alpha)+t alpha=2(1-alpha).`                              (5.12)

Then `P_(w_t)(H=1)=1/2`. For every other row `j`,

`alpha'_j
 =[alpha_j-(1-t)P_(w*)(j in S,H=1)]/Z_t
 <= alpha_j/Z_t.`                                               (5.13)

Numerically

`Z_t=0.9377497253420668...`,
`(3/8)/Z_t=0.3998934788951388...<1/2`,                          (5.14)

and the seventh small marginal is smaller still. Hence **all** row marginals of `w_t` are at most `1/2`.

This tilt is not merely feasible; it is the global optimizer of `G(w)` over the full `q=1` admissible polytope. Indeed, by (3.9) maximizing `G` is minimizing `KL(w||w*)`. Data processing under the map `omega -> H(omega)` gives, for every feasible `w` with `r=P_w(H=1)<=1/2`,

`KL(w||w*) >= D_Ber(r||alpha) >= D_Ber(1/2||alpha)`,             (5.15)

because `alpha>1/2`. The tilt (5.12) preserves the two conditional laws given `H` and sets `r=1/2`, so equality holds. Thus

`KL_min
 =-1/2 log(4 alpha(1-alpha))
 =0.001941312167684154...`,                                     (5.16)

and

`G_opt
 =Z exp(-KL_min)
 =Z*2sqrt(alpha(1-alpha))
 =63.97170951965423... .`                                       (5.17)

The new weighted `q=1` theorem therefore gives the rigorous all-product-law bound

`boxed(||p_R||_inf <= 3e G_opt^(-1/6)
                     =4.077723216651394... .)`                  (5.18)

Thus a tiny entropy tilt repairs an actual failure of the raw `q=1` volume gate and improves substantially over paying a larger Fourier exponent.

## 6. Ridge and designated-partner comparison on one genuinely rotated indefinite target matrix

To make the partner's outer-square theorem directly applicable while leaving the aggregate cross block unchanged, add one fresh original coordinate `Z` and a small coupling on the left bank:

`Q_*(Z,X,Y)=(Z+X_1/100)^2+2 X^T M Y.`                           (6.1)

The corresponding `17x17` physical matrix has the left-right cross block `M`; the added rank-one square changes only the left self block after conditioning on `Z`. Hence both Theorem 3.1 and the ridge theorem apply to `Q_*` with exactly the same cross certificate as above, uniformly in `Z`. In particular (5.18) also gives `||p_(Q_*)||_inf<=4.078`.

This is an exact target-valid rotated indefinite matrix. Relative to `diag(1,[[0,M],[M,0]])`, the added coupling has operator norm

`(tau^2+sqrt(tau^4+4tau^2))/2 < tau+tau^2=0.0101`, `tau=0.01`.   (6.2)

The base matrix has six singular values equal to two. Weyl therefore gives at least six eigenvalues of modulus greater than `1.9899`, so the required three-large-eigenvalue hypothesis holds with room to spare.

### 6.1 Ridge certificate

Choose `q=1` and the rational scale

`gamma=127/250=0.508`.                                          (6.3)

Because `MM^T` is a two-level spectral function of `P`,

`K_gamma=k_L I+(k_H-k_L)P`,
`k_H=4/(4+gamma^2)`,
`k_L=0.0004/(0.0004+gamma^2).`                                  (6.4)

Hence, using the heavy diagonal `17/32`,

`max_i(K_gamma)_ii=0.49977853031393765...<1/2`,                 (6.5)

while

`theta=3k_H+5k_L=2.8259201813223074...>2`,                      (6.6)

and

`D_gamma=(1+4/gamma^2)^3(1+0.0004/gamma^2)^5`
`       =4527.072645707498... .`                                (6.7)

The completed ridge theorem therefore gives

`boxed(||p_(Q_*)||_inf <2.919449306754837.)`                    (6.8)

This is the strongest of the three aggregate certificates on this matrix.

For comparison with Proposition 4.1, here `rho=E3/E2=1.3346663556799483...`, and (6.3) corresponds to `a=gamma^2/rho=0.1933546904...<1/2`; thus the intrinsic bridge itself certifies both ridge admissibility and a (nonoptimal) fractional-volume exponent `q=1+a`.

### 6.2 Applying the designated partner result to an actual inequality

The largest physical coefficient in `M` is the heavy diagonal cross coefficient

`m_*=2[0.01+0.99(17/32)]=1.071875.`                             (6.9)

Select the corresponding left/right original-coordinate pair and place every other residual coordinate in `W`. Its physical `2x2` block is

`B_*=[[0,m_*],[m_*,0]]`, `|det B_*|=m_*^2`.                     (6.10)

The outer square in (6.1) is a genuine independent original scalar; its shift is allowed to reuse the selected left coordinate. Account03/B04's completed overlap-safe theorem therefore applies directly and gives

`boxed(
 ||p_(Q_*)||_inf
 <=63.11383495773493... / sqrt(1.071875)
 =60.9610584534435... .
)`                                                               (6.11)

This is a valid but much weaker local-pair certificate on exactly the same physical matrix. It quantitatively reinforces the aggregate-before-inversion lesson: weighted three-volume gives `4.078`, ridge gives `2.920`, while selecting the best physical pair through the partner endpoint gives `60.962`.

## 7. What changed

This run pays three pieces that were not present in the preceding B04 comparison:

1. a **sharp-HY arbitrary-weight fractional-volume theorem**, combining the e5 determinant/entropy idea with the current q-dependent Fourier constants;
2. an **intrinsic matrix bridge** `W<=(1+a)K_a` that converts one ridge-leverage certificate into simultaneous ridge and fractional-volume admissibility;
3. a **globally optimized q=1 KL repair** on an actual target matrix where raw volume sampling fails the old `1/2` gate.

The full conjecture is still OPEN. The remaining step is structural, not a missing scalar Fourier estimate: prove a universal bound on the KL/scale cost of one of these aggregate exits, or classify the failure into a completed hub/grouped-coordinate branch.

## 8. Status and review boundary

- `QFORM-WEIGHTED-FRACTIONAL-VOLUME-SHARP-v1`: proved here by a direct modification of the displayed determinant step plus the source sharp-HY calculation; independent review pending.
- `QFORM-INTRINSIC-RIDGE-VOLUME-BRIDGE-v1`: elementary spectral inequality proved here; independent review pending.
- Exact `17x17` application: symbolic formulas plus deterministic finite checks saved with this report; finite checks are not independent proof review.
- Claude `e5f71...` Theorem D was applied at the determinant/entropy step, not merely cited.
- account03/B04 theorem was applied at equation (6.11).
- Full QFORM: OPEN / NOT PROVED / NOT DISPROVED.
- Continuity of the full target: OPEN. The weighted/ridge branches above individually give continuous densities in their stated scopes.
