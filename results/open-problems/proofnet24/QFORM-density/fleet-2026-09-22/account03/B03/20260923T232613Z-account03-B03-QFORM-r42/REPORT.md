SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B03, 2026-09-23T23:26:13Z.
attacking: the exact mixed endpoint det(P_++P_-)=det(P_+-P_-)=0 by transverse-square slice Hausdorff-Young plus rank-one bilinear Plancherel, preserving sum/difference dependence.

# account03/B03 r42 — transverse-square closure of the singular/singular conjugate endpoint

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Assignment:** decoupled time integral  
**Classification:** `NEW SUPPORTING THEOREM / DESIGNATED PARTNER APPLIED / LINEAR SMALL-BALL RECEIVER / FULL TARGET OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`.

The unrestricted quadratic-form bounded-density conjecture remains **OPEN**. Full-target continuity remains **OPEN**. This report closes one exact two-dimensional endpoint left by B03 r41: both the same-bank curvature and the cross-difference curvature are singular, while the two original conjugate quadratic pieces remain nondegenerate. The proof keeps the true dependence between `U=X-X'` and `V=X+X'` and never conditions one conjugate variable on the other.

## 1. Fresh source state and correction boundary


The proof preserves the live corrections:

- no law-uniform pointwise van-der-Corput/Fresnel decay for arbitrary cap-one scalar laws;
- no independence after rotating the original input coordinates;
- no cap-one conditional law of `X-X'` given `X+X'`, or conversely;
- no arbitrary-joint coarea shortcut;
- no deletion of a small nonzero quadratic tail without moment/support assumptions.

A newer correction is especially relevant: `QFORM-RANK1-SAMEBANK-HALFRIESZ-FALSE-v1`, source

`yspennstate/math-open-problems@769800c0ab0851828772adabfb6874aa813e423d`

`proofnet24/QFORM-density/fleet-2026-09-22/account01/B01/20260923T220810Z-account01-B01-qform-auto11/REPORT.md`.

It gives the exact counterexample `-Y^2-Z^2+2YZ=-(Y-Z)^2`, showing that a rank-one bilinear crossing plus arbitrary same-bank phases need not have a finite critical half-Riesz potential. The theorem below does **not** contradict or use that false interface. Its essential extra resource is a square in a physical direction transverse to the rank-one bilinear direction on each independent bank.

The designated partner is account04/B03:

`yspennstate/math-open-problems@05ff82a8d052b024ae584e60dffb7b198fcd7db4`

`proofnet24/QFORM-density/fleet-2026-09-22/account04/B03/20260923T183012Z-account04-B03-dependent-riesz-r2/REPORT.md`.

Its dependence-safe fractional-budget theorem is applied quantitatively in Section 7.

## 2. The exact mixed endpoint

Let `X=(X_1,X_2)` have independent real coordinates with probability densities bounded by one, and let `X'` be an independent copy. Define

`U=X-X'`,  `V=X+X'`.

The vectors `U,V` are dependent. For real symmetric invertible `2 x 2` matrices `P_-`, `P_+`, and arbitrary affine data, put

`R_-(U)=U^T P_- U + ell_-^T U+d_-`,

`R_+(V)=V^T P_+ V + ell_+^T V+d_+`,

`S=R_-(U)+R_+(V)`.

Set

`H=P_-+P_+`,  `K=P_+-P_-`.

Expanding in the genuine independent original-copy pair `(X,X')` gives the exact identity

`S=X^T H X + X'^T H X' + 2X^T KX' + affine`.

B03 r41 paid the branch `det K !=0` by two-bank Plancherel while allowing arbitrary `H`. The exact remaining mixed endpoint considered here is

`det H=0`,  `det K=0`,  `det P_- det P_+ !=0`.                 (2.1)

Under (2.1), neither `H` nor `K` can vanish. Thus there are unit vectors `u,v` and nonzero scalars `a,b` such that

`H=a uu^T`,  `K=b vv^T`.                                       (2.2)

Moreover `u,v` are linearly independent; otherwise `H+K` and `H-K` would both have rank at most one, contradicting invertibility of `P_+` and `P_-`. Write

`Delta=|det(u,v)|>0`.                                            (2.3)

For the transformed banks

`Z=(Z_1,Z_2)=(u^T X,v^T X)`,
`W=(W_1,W_2)=(u^T X',v^T X')`,                                  (2.4)

`Z` and `W` are independent. Their coordinates inside a bank need not be independent. Since the original two-coordinate product density is at most one, the Jacobian gives

`||rho_Z||_infinity, ||rho_W||_infinity <= Delta^(-1)`.          (2.5)

After completing/translating the affine terms, which only translates these two planar densities and does not change their caps, `S` is reduced to

`T=a(Z_1^2+W_1^2)+2b Z_2W_2 + constant`.                        (2.6)

Thus the critical problem is a transverse square plus a rank-one bilinear crossing, not a rank-one crossing with arbitrary local phases.

## 3. Slice `L^3` lemma for the transverse square

We first prove a general statement. Let `Z=(Z_1,Z_2)` have any planar probability density `rho_Z<=M_Z`. For fixed `z_2`, write

`g(z_1)=rho_Z(z_1,z_2)`,  `m(z_2)=int_R g(z_1) dz_1`.

For fixed `t`, define

`A_t(z_2)=int_R g(z_1) exp(i t a z_1^2) dz_1`.                    (3.1)

Let `h` be the pushforward density of the finite slice measure `g(z_1)dz_1` by `z_1 -> z_1^2`. For `y>0`,

`h(y)=[g(sqrt y)+g(-sqrt y)]/(2sqrt y)`.                         (3.2)

A direct change of variables and `(r+s)^(3/2)<=sqrt(2)(r^(3/2)+s^(3/2))` give

`int_0^infinity h(y)^(3/2)dy
 <= int_R g(x)^(3/2)|x|^(-1/2)dx`.                               (3.3)

Since `g<=M_Z`, the right side is at most

`M_Z^(1/2) int_R g(x)|x|^(-1/2)dx`.                             (3.4)

Among functions `0<=g<=M_Z` of mass `m`, the last weighted integral is maximized by filling the centered interval of length `m/M_Z`; hence

`int_R g(x)|x|^(-1/2)dx <= 2sqrt(2 M_Z m)`.                     (3.5)

Combining (3.3)-(3.5),

`||h||_(3/2)^(3/2) <= 2sqrt(2) M_Z sqrt(m(z_2))`.                (3.6)

With Fourier convention `hat h(s)=int e^(isy)h(y)dy`, Hausdorff-Young gives

`||hat h||_3 <= (2pi)^(1/3)||h||_(3/2)`.                        (3.7)

Since `A_t(z_2)=hat h(at)`, cubing and scaling gives the exact useful slice estimate

`boxed:
 int_R |A_t(z_2)|^3 dt <= 16 pi M_Z^2 m(z_2)/|a|.
}`                                                                  (3.8)

No pointwise oscillatory estimate is used.

Define

`F_Z(t)=int_R |A_t(z_2)|^2 dz_2`.                                (3.9)

Because `|A_t(z_2)|<=m(z_2)` and `int m=1`,

`[F_Z(t)]^2 <= [int |A_t|][int |A_t|^3] <= int |A_t|^3`.       (3.10)

Integrating (3.10) in `t` and using (3.8) gives

`boxed:
 ||F_Z||_2 <= 4sqrt(pi) M_Z/sqrt(|a|).
}`                                                                  (3.11)

The identical estimate holds for the independent bank `W` with cap `M_W`.

## 4. Rank-one bilinear Plancherel glued to the square slices

For

`T=a(Z_1^2+W_1^2)+2b Z_2W_2`,                                   (4.1)

the characteristic function is

`phi_T(t)=int_R2 A_t(z_2) B_t(w_2) exp(i2bt z_2w_2) dz_2dw_2`.  (4.2)

For fixed nonzero `t`, the operator

`(L_t f)(z)=int_R exp(i2bt zw)f(w)dw`

has, by one-dimensional Plancherel,

`||L_t||_(2->2)=sqrt(pi/(|bt|))`.                                (4.3)

Therefore

`boxed:
 |phi_T(t)| <= min{1, sqrt(pi/(|bt|)) sqrt(F_Z(t)F_W(t))}.
}`                                                                  (4.4)

This is the key dependence-safe integrated estimate. It is not a uniform pointwise power law because `F_Z,F_W` may spike in `t`; their `L^2` norms, not pointwise values, are what the square slices control.

By Cauchy-Schwarz and (3.11),

`int_R F_Z(t)F_W(t)dt
 <=16 pi M_ZM_W/|a|`.                                            (4.5)

## 5. One-copy half-Riesz and the assigned whole-copy time integral

### Theorem 5.1 — transverse-square / rank-one-cross receiver

For independent planar banks with density caps `M_Z,M_W`, and `a,b!=0`, the variable (4.1) obeys

`boxed:
 int_R |t|^(-1/2)|phi_T(t)|dt
 <=2^(13/4)sqrt(pi)(M_ZM_W)^(1/4)|ab|^(-1/4).
}`                                                                  (5.1)

Indeed, split at `T_0>0`. The central interval contributes at most `4sqrt(T_0)`. On the tail, (4.4), Cauchy-Schwarz, and (4.5) give

`int_(|t|>T_0) |t|^(-1/2)|phi_T(t)|dt
 <=4pi sqrt(2)(M_ZM_W)^(1/2)|ab|^(-1/2) T_0^(-1/2)`.            (5.2)

Optimizing proves (5.1). Using the one-dimensional Riesz identity only after Gaussian regularization,

`int_R e^(itx)|t|^(-1/2)dt=sqrt(2pi)|x|^(-1/2)`,                (5.3)

we obtain

`boxed:
 sup_s E|T-s|^(-1/2)
 <=2^(11/4)(M_ZM_W)^(1/4)|ab|^(-1/4).
}`                                                                  (5.4)

For the assignment's exact whole-copy quantity, square (4.4), use (4.5), and again split at `T_0`:

`int_R |t|^(-1/2)|phi_T(t)|^2dt
 <=4sqrt(T_0)
   +16pi^2 M_ZM_W |ab|^(-1)T_0^(-3/2)`.                         (5.5)

Optimizing at the exact crossover gives

`boxed:
 int_R |t|^(-1/2)|phi_T(t)|^2dt
 <=16sqrt(2) 3^(-3/4)sqrt(pi)
    (M_ZM_W)^(1/4)|ab|^(-1/4).
}`                                                                  (5.6)

If `T'` is an independent copy of the **whole** variable `T`, then

`|phi_T(t)|^2=E exp(it(T-T'))`.                                  (5.7)

Thus (5.3), (5.6) imply

`E|T-T'|^(-1/2)
 <=16 3^(-3/4)(M_ZM_W)^(1/4)|ab|^(-1/4)`.                       (5.8)

Equation (5.7) is the only independent-copy identity used. At no stage is `X-X'` declared independent of `X+X'`.

## 6. Exact conjugate endpoint with determinant currency

Return to (2.1)-(2.6). Since `u,v` are unit vectors,

`det P_+ = ab Delta^2/4`,
`det P_- = -ab Delta^2/4`.                                       (6.1)

In particular

`D:=|det P_+|=|det P_-|=|ab|Delta^2/4`.                          (6.2)

Combining (2.5), (6.2) with Section 5 gives the new theorem.

### Theorem 6.1 — `QFORM-CONJUGATE-TRANSVERSE-RANK1-MIXED-HALFRIESZ-v1`

Under (2.1), for arbitrary affine terms,

`boxed:
 sup_s E|S-s|^(-1/2)
 <=2^(9/4) D^(-1/4)
 =4.756828460010884... D^(-1/4).
}`                                                                  (6.3)

Moreover the one-copy weighted Fourier integral is

`boxed:
 int_R |t|^(-1/2)|phi_S(t)|dt
 <=2^(11/4)sqrt(pi) D^(-1/4)
 =11.92360071543272... D^(-1/4),
}`                                                                  (6.4)

and the assigned decoupled whole-copy integral satisfies

`boxed:
 int_R |t|^(-1/2)|phi_S(t)|^2dt
 <=16 3^(-3/4)sqrt(pi) D^(-1/4)
 =12.440962412449712... D^(-1/4).
}`                                                                  (6.5)

Equivalently, for an independent whole copy `S'`,

`boxed:
 E|S-S'|^(-1/2)
 <=8sqrt(2)3^(-3/4)D^(-1/4)
 =4.963225915211198... D^(-1/4).
}`                                                                  (6.6)

The theorem is exactly at the singular/singular r41 endpoint: `H` and `K` are each rank one, but their rank-one directions must be transverse because both `P_+` and `P_-` are invertible. That transversality supplies the missing square resource.

### Linear small-ball receiver

Let `Y` be one genuinely independent original scalar coordinate with density at most one, independent of the entire bank producing `S`, and let `d!=0`. For

`Q=d(Y+h)^2+S+c`,                                                 (6.7)

the translated-square density envelope and (6.3) give

`boxed:
 ||p_Q||_(infinity,ess)
 <=2^(9/4)|d|^(-1/2)D^(-1/4).
}`                                                                  (6.8)

Hence every interval `I` satisfies

`boxed:
 P(Q in I)
 <=2^(9/4)|d|^(-1/2)D^(-1/4)|I|.
}`                                                                  (6.9)

This is genuine **linear output small-ball scaling**. The argument establishes an essentially bounded density on this branch. It does **not** establish continuity.

## 7. Designated account04/B03 result applied to this endpoint

The account04/B03 dependent fractional-budget theorem applies to the actual dependent pair `(U,V)`, because `P_-` and `P_+` are invertible. It gives

`E |R_-(U)-s|^(-1/4)|R_+(V)-t|^(-1/4)
 <=sqrt(B(P_-)B(P_+))`.                                         (7.1)

Using its universal `B(P)<=128|det P|^(-1/4)` and (6.2), we obtain the concrete new endpoint inequality

`boxed:
 E |R_-(U)-s|^(-1/4)|R_+(V)-t|^(-1/4)
 <=128 D^(-1/4).
}`                                                                  (7.2)

Consequently, for every `epsilon>0`,

`boxed:
 P(|R_-(U)-s|<=epsilon^2,
   |R_+(V)-t|<=epsilon^2)
 <=128 D^(-1/4) epsilon.
}`                                                                  (7.3)

This is an actual use of the designated partner theorem on the same endpoint. It retains the dependence between the conjugate sum and difference. The new Sections 3-6 supply the additional critical half-power that formal Holder cannot provide.

## 8. Relation to the newest four-coordinate determinant receiver

A concurrent account03/B06 supporting theorem, source

`yspennstate/math-open-problems@769800c0ab0851828772adabfb6874aa813e423d`

`proofnet24/QFORM-density/fleet-2026-09-22/account03/B06/20260923T222115Z-account03-B06-qform-r46/REPORT.md`,

proves for any invertible literal physical `4 x 4` block `M` the bound

`||p||_infinity <93 |det M|^(-1/4)`.

For the four genuine original coordinates `(X,X')`, the quadratic matrix of `S` is

`M=[[H,K],[K,H]]`,                                                (8.1)

and the block diagonalization into the sum/difference subspaces gives

`det M=det(H+K)det(H-K)=16 det(P_+)det(P_-)`.                    (8.2)

Thus that theorem, at its stated supporting scope, gives the fallback

`||p_S||_infinity <(93/2)|det(P_+)det(P_-)|^(-1/4)`.             (8.3)

This cross-check is useful because it pays every invertible two-sided physical conjugate pair without requiring `det H` or `det K` to be nonzero. The present theorem is still materially sharper at the exact singular/singular endpoint: when `|det P_+|=|det P_-|=D`, (8.3) is `<46.5 D^(-1/2)`, whereas (6.3) gives the scale-correct critical half-Riesz currency `4.757 D^(-1/4)` and then a separate genuine square gives (6.8). No claim is made that either local receiver is automatically extractable from every full target matrix.

## 9. What remains for the full target

The exact two-sided analytic endpoint `det H=det K=0` with invertible `P_+`, `P_-` is no longer an analytic gap: the transverse rank-one geometry forces the square-plus-cross structure and the assigned integrated estimate closes it.

The unrestricted conjecture is still **OPEN** because an arbitrary matrix with three eigenvalues of modulus at least one has not yet been shown, by a product-preserving structural reduction, to expose one of the already-paid local receivers at a universal scale. In particular, one cannot silently rotate to eigen-coordinates, and small physical minors cannot simply be inverted coordinate by coordinate.

For B03 the next useful implication is therefore structural rather than another formal exponent split: in whichever proof assembly produces a conjugate two-plane packet, quantify either (i) an invertible `K` (r41), (ii) this exact transverse rank-one mixed endpoint, (iii) the literal four-coordinate determinant receiver, or (iv) a source-disjoint third smoothing coordinate, with a dimension-free scale payment from the original three-large-eigenvalue hypothesis.

Full-target continuity remains **OPEN**. The branch (6.8) asserts essential boundedness only.
