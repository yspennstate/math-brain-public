SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account 03, slot B19, 2026-09-23T00:25:41Z.
attacking: the near-singular double-near-null O3 companion state: prove that an exactly rank-two internal bank is quantitatively robust, forcing a product-preserving 2+1 grouped-coordinate block.

# fleet03/B19 r20 — robust internal-bank theorem for the O3 near-singular survivor

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Assignment:** Universal proof assembly  
**Owner control consumed:** revision `2026-09-22.15`  
**Status:** `ESSENTIAL_STEP_APPLIED / PROVED SUPPORTING TARGET-LEVEL STRUCTURAL THEOREM / FULL TARGET OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN` (`full_brain_connected=false`).

## 1. Exact target and correction boundary

The unrestricted target remains open: for arbitrary independent real coordinates with marginal densities at most one and arbitrary real symmetric `A` having at least three eigenvalues of modulus at least one, prove a universal essential-density bound for `Q=X^TAX`, or give a valid counterexample. The full continuous-density conclusion is also open.

This run uses no post-rotation independence, arbitrary-joint rank-three coarea estimate, positive conditional projection-density moment, pointwise quadratic-phase decay, worst-fiber supremum, fixed-good-minor reduction, or perturbative deletion of small coefficients. The source state explicitly marks the first two of those gates false.

The immediate source is fleet03/B19 r19. In an exact-rank-three O3 packet, suppose exactly one of the three resource banks has internal spectral rank two and the other two are rank-one banks. r19 already pays the state unless the compressed two-companion matrix `B` simultaneously satisfies

`kappa(B)<1/64`,                                                   (1.1)

`theta_1<1/4096`, `theta_2<1/4096`,                               (1.2)

where `theta_a=|det M| lambda_a^2 |t_a|`, `t_a=v_a^T M v_a`, and the complete companion-pair determinant packet obeys

`mu=|det M| lambda_1 lambda_2 |v_1 cross v_2|^2 >=1/512`.          (1.3)

The purpose of this run is to resolve the first structural implication inside precisely this survivor.

## 2. Setup

Write the exact-rank-three core as

`A=R M R^T`, `R^T R=I_3`, `M=M^T`, `s_min(M)>=1`.                 (2.1)

Let `H_1,H_2,G` partition the original-coordinate spectral rows. Assume the two companion banks are rank one:

`sum_(i in H_a) u_i u_i^T = lambda_a v_a v_a^T`,                 (2.2)

where `0<lambda_a<=1`, `|v_a|=1`, and `v_1,v_2` are linearly independent. Put

`S_G=sum_(i in G)u_i u_i^T=I-lambda_1v_1v_1^T-lambda_2v_2v_2^T`. (2.3)

Assume the internal bank is genuinely rank two:

`rank(S_G)=2`.                                                    (2.4)

Set

`rho=v_1^T v_2`, `g^2=1-rho^2`,                                 (2.5)

and let

`T=[v_1 v_2]^T M [v_1 v_2]`,                                    (2.6)

`B=diag(sqrt(lambda_1),sqrt(lambda_2)) T diag(sqrt(lambda_1),sqrt(lambda_2)).` (2.7)

The packet identity proved in r19 is

`mu=|det M| lambda_1 lambda_2 g^2`.                              (2.8)

## 3. Exact rank-two frame identity

### Lemma 3.1 — internal-bank defect parameter

Define

`tau=2-lambda_1-lambda_2`.                                       (3.1)

Then

`0<=tau<=1`,                                                     (3.2)

`lambda_1 lambda_2 g^2 = 1-tau`,                                (3.3)

`rho^2<=tau`,                                                    (3.4)

`min(lambda_1,lambda_2)>=1-tau`,                                (3.5)

and the two nonzero eigenvalues of `S_G` are exactly

`1` and `tau`.                                                   (3.6)

#### Proof

Since `S_G` is positive semidefinite, each `lambda_a<=1`. The rank-two assumption gives `det S_G=0`. The two-rank-one determinant lemma gives

`det(I-lambda_1v_1v_1^T-lambda_2v_2v_2^T)`
` =1-lambda_1-lambda_2+lambda_1lambda_2(1-rho^2)=0`.

This is (3.3). Its right side is nonnegative, so `lambda_1+lambda_2>=1`, hence `tau<=1`; the upper bound `lambda_1+lambda_2<=2` gives `tau>=0`.

Because `lambda_1lambda_2<=1`, (3.3) gives `g^2>=(1-tau)`, so `rho^2=1-g^2<=tau`, proving (3.4). Since each `lambda_a<=1` and their sum is `2-tau`, each is at least `1-tau`, proving (3.5).

Let `w` be the unit normal to `span(v_1,v_2)`. Equation (2.3) gives `S_Gw=w`, so one nonzero eigenvalue is one. Also `tr S_G=3-lambda_1-lambda_2=1+tau`. Since `rank S_G=2`, the other nonzero eigenvalue is `tau`. QED.

Thus a rank-two internal bank is quantified by one number `tau`: small `tau` means that the two rank-one companion banks almost exhaust two orthogonal spectral directions.

## 4. A two-dimensional compression of a three-eigenvalue form cannot be small

### Lemma 4.1 — plane-compression lower bound

Let `P` be any two-dimensional subspace of `R^3`, let `U` have orthonormal columns spanning `P`, and let `M=M^T` satisfy `s_min(M)>=1`. Then

`||U^T M U||_op >=1`.                                           (4.1)

#### Proof

In the orthogonal decomposition `R^3=P direct_sum P^perp`, write

`M=[[C,q],[q^T,r]]`, `C=U^TMU`.

The linear functional `x -> q^T x` on the two-dimensional `P` has a nonzero kernel vector `x`. For that vector the normal component of `M(Ux)` vanishes, hence

`||C x||=||M(Ux)||>=||Ux||=||x||`,

where the inequality is `s_min(M)>=1`. Therefore `||C||_op>=1`. QED.

This elementary observation is the key new mechanism: the missing singular value cannot hide entirely in the one-dimensional normal coupling of a two-plane.

## 5. Lower bound for the compressed companion block

Let `V=[v_1 v_2]` and `G_2=V^TV`. Its eigenvalues are `1+|rho|` and `1-|rho|`. Choose an orthonormal `U` spanning the same plane and an invertible `L` with `V=UL`, so `L^TL=G_2`. If `C=U^TMU`, then

`T=L^T C L`.                                                     (5.1)

For every symmetric `C`, congruence and the Rayleigh characterization give

`||L^T C L||_op >= s_min(L)^2 ||C||_op`.                        (5.2)

Indeed, take a unit `x` attaining `|x^TCx|=||C||_op`, put `y=L^{-1}x/||L^{-1}x||`, and evaluate `y^TL^TCLy`. Since `s_min(L)^2=lambda_min(G_2)=1-|rho|`, Lemma 4.1 yields

`||T||_op >=1-|rho|`.                                           (5.3)

A second congruence with `D=diag(sqrt(lambda_1),sqrt(lambda_2))` gives

`||B||_op >= min(lambda_1,lambda_2) ||T||_op`.                  (5.4)

Using Lemma 3.1,

`boxed: ||B||_op >= (1-tau)(1-sqrt(tau)).`                       (5.5)

No sign assumption on `M`, `T`, or `B` was used.

## 6. The r19 near-singular survivor forces a robust rank-two internal bank

### Lemma 6.1 — r19 diagonal suppression

Under (1.2)-(1.3),

`|B_11|<1/8`, `|B_22|<1/8`.                                    (6.1)

#### Proof

Put `p=|det M|lambda_1lambda_2`. From (1.3), `p>=mu>=1/512`. Since `B_11=lambda_1t_1`,

`theta_1=|det M|lambda_1^2|t_1|=(p/lambda_2)|B_11|`.

Therefore

`|B_11|=theta_1 lambda_2/p <(1/4096)/(1/512)=1/8`.

The second diagonal is identical. QED.

### Lemma 6.2 — r19 spectral upper bound

Under (1.1) and (6.1),

`||B||_op<17/64`.                                                (6.2)

#### Proof

Because `B` is real symmetric, let its eigenvalues have absolute values `s_1=||B||_op` and `s_2=kappa(B)<1/64`. Also

`|tr B|<=|B_11|+|B_22|<1/4`.

If the eigenvalues have the same sign, `s_1+s_2=|tr B|<1/4`. If they have opposite signs, `s_1-s_2<=|tr B|<1/4`, hence `s_1<1/4+1/64=17/64`. QED.

### Theorem 6.3 — `QFORM-O3-RANK2-INTERNAL-ROBUSTNESS-v1`

In the exact-rank-three, exactly-one-internal-rank-two O3 survivor (1.1)-(1.3), the internal-bank defect satisfies

`boxed: tau>1/3.`                                                (6.3)

Consequently the two nonzero eigenvalues of `S_G` are `1` and a number strictly larger than `1/3`.

#### Proof

If `tau<=1/3`, (5.5) gives

`||B||_op >= (2/3)(1-1/sqrt(3)).`                               (6.4)

But

`(2/3)(1-1/sqrt(3)) >17/64`.                                   (6.5)

For an exact rational verification of (6.5), it is equivalent to `1/sqrt(3)<77/128`; squaring reduces this to `16384<17787`. This contradicts Lemma 6.2. Hence `tau>1/3`. QED.

Numerically the exact crossing of `(1-tau)(1-sqrt(tau))=17/64` is about `tau=0.3498223459`; the rational `1/3` threshold is deliberately conservative.

## 7. Forced product-preserving 2+1 grouped-coordinate volume

The robust rank-two conclusion has a second exact consequence that is directly useful for the next proof step.

Choose any `3x2` matrix `W` with

`W W^T=S_G`.                                                     (7.1)

For `a in {1,2}` and `b` the other index, define the grouped spectral map

`L_a=[sqrt(lambda_a)v_a, W]`.                                   (7.2)

Then

`L_a L_a^T=S_G+lambda_a v_av_a^T=I-lambda_b v_bv_b^T`,          (7.3)

so

`det(L_a)^2=1-lambda_b`.                                        (7.4)

But

`(1-lambda_1)+(1-lambda_2)=tau>1/3`.                            (7.5)

Therefore at least one choice of companion bank satisfies

`boxed: det(L_a)^2>1/6`, equivalently `|det L_a|>1/sqrt(6)`.     (7.6)

This is a genuine original-product decomposition: the scalar aggregate uses only coordinates in `H_a`, while the two-dimensional grouped projection uses only coordinates in `G`; those source banks are independent. No spectral rotation is declared to preserve coordinate independence.

Cauchy--Binet gives the equivalent physical principal-triple packet statement

`sum_(j in H_a, i<k in G) |det A[{j,i,k},{j,i,k}]|`
` =|det M| det(L_a)^2`
` >|det M|/6 >=1/6`.                                            (7.7)

Thus the r19 near-singular/double-near-null state cannot remain a weak `1/512` packet. If the internal bank is exactly rank two, it automatically upgrades to a constant `>1/6` one-companion/two-internal aggregate packet with a rank-two source bank whose frame eigenvalues are `1` and `>1/3`.

## 8. Designated-partner application to an actual inequality

The completed designated partner `fleet04/B19` proved `QFORM-NULL-COLOOP-ADAPTIVE-HY-STABILITY-v1` at canonical source

`yspennstate/math-open-problems@5b5cea245bb2f9f6e85e0efb7f9bc28183fc5f1a`,

`proofnet24/QFORM-density/fleet-2026-09-22/fleet04/B19/20260922T222052Z-fleet04-B19-QFORM-r2/REPORT.md`.

In its exact residual-diffuse null-coloop branch, when `0<D<=1` and `|det M|>=1`, it gives

`||p_Q||_infinity <34 sqrt(log(e/D))`.                           (8.1)

On the concrete range `D>=e^(-8)`,

`log(e/D)<=9`, hence

`boxed: ||p_Q||_infinity<102.`                                  (8.2)

This is a genuine target-level inequality for arbitrary independent cap-one input laws, not a statement about positivity or a numerical histogram. A newer fleet01/B19 result removes the exact-null essential-bound gap by a different direct smoothing theorem; (8.2) remains a valid completed partner inequality at the scope stated here and is retained in the assembly rather than silently enlarged.

## 9. Compact conditional proof map after r20

The proof tree currently has the following correction-safe form.

- Diagonal and localized physical-block branches are paid by completed direct small-ball results.
- Diffuse ridge/spectral-window branches are paid at their exact leverage hypotheses.
- Quantitative two-original-coordinate Schur pivots are paid without a `sigma_min(B)` loss by r18's sequential two-pivot/third-source theorem.
- Exact null-coloop essential boundedness is paid by the newer independent-linear-square smoothing result; the partner adaptive theorem additionally supplies continuous density away from its singular interface.
- Exact-rank-three aggregate O3 states with all three resource banks rank one were paid before r19.
- In the exactly-one-internal-rank-two O3 chamber, r19 pays every state except (1.1)-(1.3). Theorem 6.3 now proves that every remaining such state has a quantitatively robust rank-two internal bank, and (7.6)-(7.7) force a full-volume product-preserving `2+1` grouped source block.

Nothing here proves the unrestricted theorem or arbitrary-extra-spectrum descent.

## 10. First unpaid implication after the new theorem

The first missing implication in this branch is now

`QFORM-O3-ROBUST-2PLUS1-GROUPED-PAYMENT-v1`:

> Let an exact-rank-three target core be represented by two disjoint original-coordinate source banks: one rank-one aggregate scalar bank and one rank-two product-projection bank whose frame eigenvalues are at least `1` and `1/3` up to ordering, with combined grouped spectral map satisfying `det(L)^2>1/6`. Prove a universal linear small-ball/density bound while retaining the internal product-projection provenance of the rank-two bank; or split it into an already-paid heavy-coordinate or diffuse-ridge certificate.

A bound using only an arbitrary joint density cap for the rank-two grouped variable is **not** sufficient: the live arbitrary-joint coarea and fiber mechanisms are false. The next payment must exploit that the rank-two grouped law is a genuine projection of independent cap-one physical coordinates. This is precisely the product-preserving grouped-coordinate reduction requested by the current owner continuation.

Separate outstanding branches include the chamber with at least two internally rank-two O3 resource banks, the global no-pivot `N3` low-cross-rank/co-heavy hybrid, and descent in the presence of arbitrary additional spectrum.

**Full QFORM:** `OPEN / NOT PROVED / NOT DISPROVED`.  
**Full continuity:** `OPEN`.
