SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B11, 2026-09-23T00:41:54Z.
attacking: near-coloop overlap via two independent spectral-ray banks: prove a translation-stable half-potential compiler allowing arbitrary overlap in the remaining source bank.

# account03/B11 QFORM r20 — tangent-ray bank removes a near-coloop overlap obstruction

Programme: `QFORM-DENSITY-3EIG-20260922`  
Run: `20260923T004154Z-account03-B11-QFORM-r20`  
Status: **ESSENTIAL_STEP_APPLIED / PROVED_SUPPORTING_THEOREM / FULL_TARGET_OPEN**  
Execution: **WITHOUT_VERIFIED_BRAIN**

The unrestricted conjecture remains OPEN. This report proves a new correction-safe product-preserving overlap theorem for exact-rank-three indefinite forms. It uses two disjoint original-coordinate ray banks but allows all spectral quantities inside the remaining source bank to be arbitrarily dependent. It does not use post-rotation independence, arbitrary-joint rank-three coarea, conditional-density-as-independence, a fiber supremum, law-uniform pointwise oscillatory decay, moments, compact support, or deletion of small coefficients.

## 1. Completed inputs

Designated partner `account04/B11`: `yspennstate/math-open-problems@4110bbfd21beffa0260a017d468b0a486af56db1`, path `proofnet24/QFORM-density/fleet-2026-09-22/account04/B11/20260922T222040Z-account04-B11-cone-envelope-r3/REPORT.md`. It proves that if `Z` is independent of `(V,W)`, `||p_Z||_inf<=L`, `||(V,W)||_inf<=M_2`, and

`T=2 alpha ZW + beta V^2 + 2 gamma VW + delta W^2 + affine`,

then

`||p_T||_inf <=3*2^(2/3)*(L M_2)^(2/3)|alpha|^(-2/3)|beta|^(-1/3)`.  (1.1)

The standard scalar product-projection bound used in the fleet gives, for a coefficient vector `a` and independent cap-one source coordinates,

`||p_(a dot X)||_inf <=sqrt(2)/||a||_2`.                         (1.2)

A source pin is `yspennstate/math-open-problems@39b2d7a6fc503f2abbeee3b50c30ed64886de365`, path `proofnet24/QFORM-density/fleet-2026-09-22/account03/B19/20260922T223200Z-account03-B19-QFORM-r19/REPORT.md`.

## 2. New analytic compiler

### Lemma 2.1 — translation-stable hyperbolic half-potential

Let `Z` be independent of `(S,H)`, with `||p_Z||_inf<=L`, `||p_S||_inf<=K`, and `a!=0`. For

`R=2aZS+H`,                                                      (2.1)

where `H` may depend arbitrarily on `S`, both one-sided half-potentials satisfy

`sup_t E (t-R)_+^(-1/2) <=4 sqrt(LK/|a|)`,                      (2.2)

`sup_t E (R-t)_+^(-1/2) <=4 sqrt(LK/|a|)`.                      (2.3)

Proof. Condition on `S=s,H=h`. The density of `2asZ+h` is capped by `m=L/(2|as|)`. For any probability density `q<=m`, the bathtub principle gives

`sup_t integral_(y<t) (t-y)^(-1/2)q(y)dy <=2sqrt(m)`,           (2.4)

and likewise on the opposite half-line. Therefore the conditional half-potential is at most `sqrt(2L/(|a||s|))`. For any probability density capped by `K`, another centered bathtub argument gives

`E|S|^(-1/2)<=K integral_(-1/(2K))^(1/(2K)) |s|^(-1/2)ds
             =2sqrt(2K)`.                                      (2.5)

Multiplication proves (2.2)-(2.3). QED.

### Lemma 2.2 — independent square smoothing

Let `V` be independent of `(R,C)`, with `||p_V||_inf<=K_V`, and `b!=0`. Then

`T=R+b(V+C)^2`                                                   (2.6)

has

`||p_T||_inf <=(K_V/sqrt(|b|))
 max{sup_t E(t-R)_+^(-1/2), sup_t E(R-t)_+^(-1/2)}.`            (2.7)

Indeed the shifted-square density is at most `K_V/(sqrt(|b|)*sqrt(|y|))` on the appropriate half-line. QED.

Combining the lemmas: if `Z,V` are independent of one another and of a source `G`, while `S,H,C` are arbitrary functions of `G`, then

`T=b(V+C(G))^2+2aZS(G)+H(G)`                                   (2.8)

satisfies

`boxed: ||p_T||_inf <=4 K_V sqrt(LK)/sqrt(|ab|).`               (2.9)

This is the key overlap-safe interface: no independence is required among `S,H,C`.

## 3. New theorem — `QFORM-NULL-TANGENT-TWORAY-OVERLAP-v1`

Let

`A=RMR^T`, `R^TR=I_3`,                                         (3.1)

where `M` is real symmetric, invertible, and indefinite. Let unit vectors `r,v` obey

`r^TMr=0`, `r^TMv=0`, `beta=v^TMv!=0`.                          (3.2)

Suppose two disjoint nonempty original-coordinate banks `H,K` have collinear spectral rows

`r_i=c_i r` on `H`, with `lambda=sum_H c_i^2>0`,                (3.3)

`r_i=d_i v` on `K`, with `mu=sum_K d_i^2>0`.                    (3.4)

Then, for arbitrary independent cap-one source laws,

`boxed: ||p_(X^TAX)||_inf
 <=8 lambda^(-1/4) mu^(-1/2)/sqrt(|s beta|),`                   (3.5)

where `s=||Mr||_2`. This covers both signatures `(2,1)` and `(1,2)`.

Proof. Let `G` be the remaining original coordinates and define

`Z=sum_H c_iX_i`, `V=sum_K d_iX_i`, `Y=sum_G r_jX_j`.           (3.6)

These three source-bank objects are mutually independent. By (1.2),

`||p_Z||_inf<=sqrt(2)/sqrt(lambda)`,
`||p_V||_inf<=sqrt(2)/sqrt(mu)`.                                (3.7)

Put `e_1=Mr/s`. Since `r` is null, `e_1 perp r`; since `r^TMv=0`, also `e_1 perp v`. Parseval `sum_i r_ir_i^T=I_3` therefore implies

`sum_(j in G)<r_j,e_1>^2=1`.                                   (3.8)

Thus `W=<Y,e_1>` is a normalized linear form of the independent source coordinates in `G`, so

`||p_W||_inf<=sqrt(2)`.                                         (3.9)

Using `R^TX=Zr+Vv+Y`, expand and complete the square only in the independent scalar `V`:

`Q=beta[V+C(Y)]^2+2sZW+H_0(Y)`,                                (3.10)

with

`C(Y)=(v^TMY)/beta`,
`H_0(Y)=Y^TMY-(v^TMY)^2/beta`.                                 (3.11)

The quantities `W,C(Y),H_0(Y)` may be arbitrarily dependent. Apply (2.9) with

`a=s`, `b=beta`, `L=sqrt(2)/sqrt(lambda)`, `K=sqrt(2)`,
`K_V=sqrt(2)/sqrt(mu)`.                                         (3.12)

The coefficient simplifies exactly to `8 lambda^(-1/4)mu^(-1/2)`, proving (3.5). QED.

## 4. Spectral payment

Choose `e_2` so `(r,e_1,e_2)` is orthonormal. In this basis

`M=[[0,s,0],[s,d,g],[0,g,f]]`,                                  (4.1)

hence

`det M=-s^2f`, `(M^(-1))_33=1/f`.                              (4.2)

If `sigma_min(M)>=sigma>0`, then `s=||Mr||>=sigma` and `||M^-1||_op<=1/sigma`, so `|f|>=sigma`.

Every unit `v` satisfying `r^TMv=0` is orthogonal to `e_1`, hence can be written

`v=a r+b e_2`, `a^2+b^2=1`.                                    (4.3)

Put `eta=|b|=dist(v,span(r))`. Equation (4.1) gives

`beta=b^2f`, so `|beta|>=eta^2 sigma`.                           (4.4)

Therefore (3.5) implies

`boxed: ||p_Q||_inf
 <=8 lambda^(-1/4)mu^(-1/2)eta^(-1)sigma^(-1).`                (4.5)

Concrete thresholds:

- `lambda>=1/2`, `mu>=1/4`, `eta=1` gives
  `||p_Q||_inf<=16*2^(1/4)/sigma=19.027313840043536.../sigma`;
- `lambda>=1/2`, `mu>=1/4`, `eta>=1/2` gives
  `||p_Q||_inf<=32*2^(1/4)/sigma=38.05462768008707.../sigma`.

Thus this is a genuine target-homogeneous bound on a rotated indefinite near-coloop branch, without selecting a reciprocal physical minor.

## 5. Designated partner applied to an actual inequality

At the exact full-null-bank endpoint `lambda=1`, the completed designated partner theorem applies with null-bank scalar density cap `sqrt(2)` and two-dimensional residual product-projection cap `e`. It gives

`||p_Q||_inf<=6e^(2/3)|det M|^(-1/3).`                          (5.1)

Hence, when `sigma_min(M)>=sigma`,

`boxed: ||p_Q||_inf<=6e^(2/3)/sigma
                     =11.686404246328054.../sigma.`             (5.2)

This pays the exact boundary. Theorem 3 is complementary: it moves into `lambda<1` when a quantitative tangent-curvature ray bank exists, and it tolerates arbitrary overlap inside the residual source where the partner's independent two-dimensional pair need not exist.

## 6. Why the third direction removes the rank-two logarithm

For independent `X,Y~Uniform[-1/2,1/2]`,

`p_(2XY)(t)=log(1/(2|t|)), 0<|t|<1/2`.                          (6.1)

The logarithmic rank-two singularity is therefore real. In the new proof the independent null-bank product `2sZW` initially carries the hyperbolic `1/|W|` Jacobian. Lemma 2.1 does not try to bound that density; it pays a half-order potential instead, lowering the singularity to `|W|^-1/2`, which is uniformly integrable because `W` is a normalized product projection. The independent tangent-curvature bank `V` then contributes the square kernel in Lemma 2.2. Every other residual quadratic term only translates that half-potential through `H_0(Y)` and cannot restore the logarithm. This identifies the third direction explicitly rather than hiding it inside an arbitrary projected-density cap.

## 7. Scope and next implication

The full conjecture is still OPEN. The new theorem requires a second disjoint rank-one source bank in the `M`-orthogonal tangent plane of the null ray, with quantitative `mu` and `eta`. The bare three-large-eigenvalue hypothesis has not yet been shown to force such a bank.

First remaining B11 implication:

`QFORM-NEAR-COLOOP-NO-TANGENT-RAY-AGGREGATION-v1` — starting from a near-unit null bank with leverage `<1`, prove either that a quantitative tangent-curvature ray bank exists and the theorem above applies, or aggregate a genuinely rank-two/three residual original-coordinate bank into an already-paid pair/ridge/grouped certificate, without deleting small coefficients or replacing product independence by a conditional density cap.

Arbitrary additional spectrum beyond the exact-rank-three core remains a separate full-target debt. This report proves **essential boundedness only in the stated branch**; continuity for this new branch is **not proved**.

## 8. Exact check

The accompanying `VERIFY.py` symbolically verifies `det M=-s^2f`, `(M^-1)_33=1/f`, the coefficient simplification in (3.12), and the numerical constants. Its recorded terminal line is

`QFORM_B11_TANGENT_RAY_OVERLAP_CHECK_PASS`.
