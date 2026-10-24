SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B08, 2026-09-23T05:21:44Z.
attacking: extend the self-matched mixed-minor Fourier branch from the 1/2 occupancy threshold to a Jensen-tunable threshold below 5/8, then sharpen the nested-packet router without selecting a physical row/minor.

# account03/B08 r28 — Jensen-tunable mixed-order compiler and 3/5 nested-volume router

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Owner control:** revision `2026-09-22.15`  
**Assignment:** diffuse eigenvector case  
**Classification:** `NEW CONTINUOUS SUPPORTING THEOREM + SHARPER DIFFUSE ROUTER / FULL TARGET OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`.

## 1. Target, source discipline, and corrections

The unrestricted target remains open: for independent ORIGINAL real coordinates with one-dimensional densities bounded by one and arbitrary real symmetric `A` with at least three eigenvalues of modulus at least one, prove a universal finite density bound for `Q=X^T A X`, or produce a valid counterexample. No Gaussian, moment, compact-support, connected-support, log-concavity, iid, or diagonal-basis hypothesis is added. Independence is never transferred through a general rotation.

Fresh control was read from `yspennstate/math-research-brain` main at `7d2e7c8ec01c8843fd226292ab75bdb17385abae`; the later OWNER CONTROL is revision `2026-09-22.15` and keeps QFORM as the sole target.

The live corrections used here include the failure of law-uniform pointwise quadratic Fresnel decay, the failure of arbitrary-joint rank-three coarea, the failure of positive conditional projection-density moments, dimension loss from naive fiber suprema, and the fresh `QFORM-COHEAVY-SINGLE-ROW-EXTRACTION-FALSE-v1`. The last correction is especially relevant: fixed aggregate determinant mass need not contain one physical row/minor of universal size. Every argument below keeps determinant currency aggregated before inversion.

The immediate predecessor is

`yspennstate/math-open-problems@e76d2e984f81a058590bb143ff21e387fbbeab09`,
`proofnet24/QFORM-density/fleet-2026-09-22/account03/B08/20260923T042303Z-account03-B08-qform-diffuse-r27/REPORT.md`.

It constructed, from an anchored third-volume law, a self-matched half-half mixture of physical order-three and order-two minors. The present run removes its artificial residual-row threshold `1/2` by combining that mixture with the completed Jensen/sharp-Hausdorff--Young compiler.

Two completed analytic sources are used at proof level:

1. **Mixed-order physical-minor BL/Fourier theorem:**
   `yspennstate/math-open-problems@86f318f0826325e6df3504e1e8ec15f4316cc861`,
   `proofnet24/QFORM-density/fleet-2026-09-22/account01/B01/20260923T001242Z-b01-qform-auto11/REPORT.md`.
   It proves the varying-order determinant expansion and entropy currency at the `q=1` Fourier exponent.

2. **Sharp-HY volume/Jensen compiler:**
   `yspennstate/math-open-problems@49c80441f24d6c697350119fac09426077b7e313`,
   `proofnet24/QFORM-density/fleet-2026-09-22/account02/B02/20260922T231047Z-account02-B02-qform-r16-6c4f9a1e/REPORT.md`.
   It proves the Jensen step and the exact scalar sharp-Hausdorff--Young factor `H_q(c)` for fixed-order volume laws.

The new point is that the determinant/BL argument in source 1 and the Jensen/HY argument in source 2 combine without requiring fixed minor order.

## 2. New theorem: mixed-order Jensen compiler

Let `I,J` be disjoint sets of ORIGINAL coordinates, condition every coordinate outside `I union J`, and let `M=A[I,J]` be the resulting physical cross block. The same-bank quadratic blocks, all outside couplings and all induced affine terms remain arbitrary.

Let `Omega` be any probability law on nonzero square physical minors `(S,T)` of `M`, of possibly varying orders

`k(S,T)=|S|=|T|>=1`.

Define

`alpha_i=P_Omega(i in S)`,
`beta_j=P_Omega(j in T)`,
`kbar=E_Omega k(S,T)=sum_i alpha_i=sum_j beta_j`,

and

`K(Omega)=exp(E_Omega log det(M_ST)^2 + H(Omega)).`                 (2.1)

For `q>=1`, put

`H_q(c)=q^(q/2-c)(q-c)^(-(q-c)/2)`, `H_q(0)=1`,                   (2.2)

and

`B_beta=prod_j (1-beta_j)^(-(1-beta_j)/2)`,                       (2.3)

with the continuous endpoint value one at `beta_j=1`.

### Theorem 2.1 — `QFORM-MIXED-ORDER-JENSEN-COMPILER-v1`

Assume

`alpha_i<=q/2` for every row `i`,                                        (2.4)

and

`kbar>2q`.                                                              (2.5)

Then the full ambient quadratic form has a continuous density vanishing at infinity and

`boxed:
 ||p_Q||_infinity
 <= [kbar/(kbar-2q)]
    [B_beta prod_i H_q(alpha_i)]^(1/kbar)
    K(Omega)^(-1/(2kbar)).
`                                                                        (2.6)

In particular,

`boxed:
 ||p_Q||_infinity
 <= e q^(-1/2) [kbar/(kbar-2q)] K(Omega)^(-1/(2kbar)).
`                                                                        (2.7)

This is an aggregate theorem: no individual determinant is selected or inverted.

### Proof

The completed decoupling step underlying both sources gives, after conditioning outside `I union J`,

`|phi_Q(t)|^2 <= E_W F_t(W)`,                                          (2.8)

where `W` has a product density with one-dimensional caps at most one and

`F_t(w)=prod_(i in I) |psi_i(2t(Mw)_i)|`, `0<=F_t<=1`.                  (2.9)

For `q>=1`, Jensen gives

`E F_t <= (E F_t^q)^(1/q)`.                                            (2.10)

Use the Brascamp--Lieb exponents

`c_i=alpha_i`, `d_j=1-beta_j`.

Their scaling is exact because

`sum_i c_i+sum_j d_j=kbar+|J|-kbar=|J|`.                               (2.11)

For positive Gaussian parameters the diagonal-plus-PSD determinant expansion is

`det(D+M^T D_I M)`
`=sum_T sum_(|S|=|T|) det(M_ST)^2 prod_(i in S)(alpha_i u_i)
                                    prod_(j notin T)((1-beta_j)v_j).`    (2.12)

Every support point of `Omega`, regardless of its order, is one positive term in (2.12). Weighted AM--GM with weights `Omega(S,T)` therefore gives

`det(D+M^T D_I M)`
`>=K(Omega) prod_i(alpha_i u_i)^alpha_i
             prod_j((1-beta_j)v_j)^(1-beta_j).`                         (2.13)

Hence Lieb's Gaussian formula yields

`C_BL<=K(Omega)^(-1/2)
       prod_i alpha_i^(-alpha_i/2)
       prod_j(1-beta_j)^(-(1-beta_j)/2).`                               (2.14)

Now apply the sharp scalar Hausdorff--Young calculation from the fixed-order Jensen source to the row function `|psi_i|^q`. Assumption (2.4) is exactly the condition `q/alpha_i>=2`. After the scale change `s=2t x`, the `i`th row contribution is bounded by

`(2|t|)^(-alpha_i)(2pi)^alpha_i
 alpha_i^(alpha_i/2) H_q(alpha_i).`                                    (2.15)

The powers of `alpha_i` cancel (2.14). Multiplying (2.15) over rows, using `sum alpha_i=kbar`, and retaining the coordinate factors gives

`E F_t^q
 <=K(Omega)^(-1/2)(pi/|t|)^kbar
    B_beta prod_i H_q(alpha_i).`                                       (2.16)

Combining (2.8), (2.10), and (2.16),

`|phi_Q(t)|
 <=min(1,(T/|t|)^a),`                                                  (2.17)

where

`a=kbar/(2q)>1`,
`T=pi [B_beta prod_i H_q(alpha_i)]^(1/kbar)
       K(Omega)^(-1/(2kbar)).`                                         (2.18)

Thus

`int_R |phi_Q(t)|dt
 <=2T a/(a-1)
 =2T kbar/(kbar-2q).`                                                   (2.19)

Fourier inversion gives a continuous `C0` density and, after division by `2pi`, exactly (2.6).

For the coarse form, the same concavity inequalities from the fixed-order source depend only on the marginal sums, not on fixed order:

`B_beta<=exp(kbar/2)`,                                                  (2.20)

and, because `log H_q` is concave with `log H_q(0)=0` and derivative `(1-log q)/2` at zero,

`prod_i H_q(alpha_i)<=exp(kbar/2)q^(-kbar/2).`                          (2.21)

Therefore

`[B_beta prod_i H_q(alpha_i)]^(1/kbar)<=e q^(-1/2)`,                   (2.22)

which gives (2.7). QED.

No scalar law-uniform Fresnel estimate is asserted: the integrable decay is obtained only after original-coordinate decoupling, the mixed physical-minor determinant expansion, Brascamp--Lieb, Jensen, and Hausdorff--Young are combined.

## 3. Application to the r27 self-matched anchored third-volume law

Use the exact setup of r27. For a physical cross block `B`, fix anchor row `i` and anchor column `a`, and define the double-incident third-volume

`Z=sum_(R,C) det B[{i} union R,{a} union C]^2>0`,                       (3.1)

where `R,C` are residual physical pairs. Let `w3` be the normalized determinant-squared law and let

`alpha_k=P_w3(k in R)`, `k!=i`, `sum_(k!=i)alpha_k=2`.                  (3.2)

Let

`R_i=||r_i||_2`.                                                       (3.3)

The predecessor constructs an order-two physical-minor law `v2*` with exactly the same residual-row marginals and

`K(v2*)>=Z/R_i^2`.                                                     (3.4)

For the half-half law

`Omega=(w3+v2*)/2`,                                                    (3.5)

one has

`kbar=5/2`,
`K(Omega)>=2Z/R_i`,                                                    (3.6)

anchor-row marginal `1/2`, and residual-row marginal exactly `alpha_k`.

Put

`h=max_(k!=i) alpha_k`.                                                (3.7)

### Corollary 3.1 — `QFORM-ANCHORED-THREEVOLUME-JENSEN-EXTENSION-v1`

If

`h<5/8`,                                                               (3.8)

set

`q=max(1,2h)<5/4`.                                                     (3.9)

Then Theorem 2.1 applies and gives a continuous `C0` density with

`boxed:
 ||p_Q||_infinity
 <= [5e/(sqrt(q)(5-4q))] (2Z/R_i)^(-1/5).
`                                                                        (3.10)

Indeed every row marginal is at most `q/2`, while

`kbar=5/2>2q`.

For `h<=1/2`, `q=1`, and (3.10) becomes

`||p_Q||_infinity <=5e(2Z/R_i)^(-1/5)`,                                (3.11)

which improves r27's coefficient `10sqrt(e)` on the same branch.

The identical statement holds for columns after transposing the physical cross block.

## 4. Explicit diffuse q=0 consequences

The preceding B08 q=0 route supplies either the already-paid continuous branch

`||p_Q||_infinity<77/L`,                                               (4.1)

or physical anchors with

`Z>L^6/6912`.                                                          (4.2)

Assume (4.2) and `R_i<=L`. Then

`(2Z/R_i)^(-1/5)<3456^(1/5)/L`.                                       (4.3)

### 4.1 Improved half-occupancy branch

If `h<=1/2`, (3.11) and (4.3) give

`boxed:
 ||p_Q||_infinity
 <5e 3456^(1/5)/L
 =69.3392648725.../L
 <70/L.
`                                                                        (4.4)

This strictly improves the predecessor's `<85/L` bound, and continuity holds.

### 4.2 Stronger 3/5 router

More importantly, if

`h<=3/5`,                                                               (4.5)

choose `q=6/5`. Since `6/5<5/4`, (3.10) gives

`||p_Q||_infinity
 <25e sqrt(5/6) 3456^(1/5)/L
 =316.488995762.../L
 <317/L.`                                                               (4.6)

Therefore if this `<317/L` row-oriented continuous branch fails while `R_i<=L`, then some residual physical row `k` has

`alpha_k>3/5`,                                                          (4.7)

and the same fixed anchored third-volume packet carried by triples containing `k` is

`alpha_k Z>(3/5)Z>L^6/11520.`                                         (4.8)

Transposing gives the identical column conclusion.

Thus, after the initial `<77/L` exit, every remaining diffuse q=0 state obeys the sharper two-sided router:

**row side:** either

- `R_i>L`, or
- a continuous `<317/L` density branch, or
- a nested anchored third-volume packet `>L^6/11520` on one residual physical row;

and independently the same trichotomy holds on the column side.

This improves r27's nested threshold `L^6/13824` and, more importantly, proves the parameterized fact that every occupancy strictly below `5/8` is analytically payable with a finite universal constant. The `5/8` boundary is the exact integrability threshold of this `3/2` mixed-order law: `kbar=5/2` and Theorem 2.1 requires `2q<5/2`, while paying a row of occupancy `h` requires `q>=2h`.

## 5. Why the new result survives the co-heavy single-row correction

The fresh target-class correction `QFORM-COHEAVY-SINGLE-ROW-EXTRACTION-FALSE-v1` shows that a fixed aggregate determinant budget can be spread over arbitrarily many tiny physical row atoms. No step above contradicts or bypasses that correction.

The proof uses the complete probability law `Omega` and the entropy-determinant currency `K(Omega)`. In the paid branches, no physical row, edge, or local determinant is selected and inverted. In the failure branch, (4.8) records only a **nested aggregate mass** carried by the event `k in R`; it does not claim that one local minor inside that event is large.

The next mechanism must therefore consume the `>L^6/11520` nested packet at bank level. The exact co-heavy identity from neighboring work,

`p_ik Z = ||r_i wedge r_k||^2 R_ik`,                                   (5.1)

and the completed aggregate-`e2` Fourier/square-lift theorem are natural receivers when a nonzero physical pivot is available; the zero/near-zero-pivot sibling still requires a product-preserving pair/ridge/grouped-bank smoother.

## 6. Completed account04 result applied to an actual inequality

A fresh current-QFORM search found no completed artifact for the designated `account04/B08` path, so no designated-partner result is fabricated.

The compatible completed account04/B18 maximum-density transfer is source-pinned at

`yspennstate/math-open-problems@ce50e74f705c49f66524aa6565d4aa4a9be88061`,
`proofnet24/QFORM-density/fleet-2026-09-22/account04/B18/20260922T182500Z-account04-B18-QFORM-r2/REPORT.md`.

Its product-projection consequence is

`||p_(u^T X)||_infinity<=sqrt(2)/||u||_2`                               (6.1)

for every nonzero coefficient vector on an ORIGINAL-coordinate independent bank.

Apply (6.1) to the actual large-star alternative in the new router. If

`R_i=||r_i||_2>L`,                                                     (6.2)

then

`boxed: ||p_(r_i^T X_J)||_infinity<sqrt(2)/L.`                         (6.3)

If the transposed router simultaneously has a column star `C_a>L`, the two projections use the disjoint original-coordinate banks `J` and `I`, so they are genuinely independent and

`boxed: ||p_(r_i^T X_J, c_a^T X_I)||_infinity<2/L^2.`                  (6.4)

Equations (6.3)-(6.4) are retained as product-linear currency for the remaining curved receiver. They are not promoted to a generic indefinite quadratic pushforward bound.

## 7. Continuity and remaining implication

Theorem 2.1, Corollary 3.1, and the `<70/L` / `<317/L` branches prove a continuous density vanishing at infinity. The large-star account04 application proves only a bounded linear projection density. The full target's continuity remains open.

The unrestricted QFORM conjecture remains **OPEN / not proved / not disproved**.

The first B08 debt is now

`QFORM-THREEANCHOR-3/5-AGGREGATE-RECEIVER-v1`:

> starting with an anchored third-volume packet `Z>L^6/6912` whose non-large-star side has a residual row (or column) carrying more than `3/5` of `Z`, consume that nested aggregate before selecting a physical minor. Use the co-heavy identity / aggregate `e2` compiler when a nonzero physical square is available, and a zero-pivot product-bank mechanism otherwise.

The parameterized theorem shows that no occupancy `<5/8` needs separate geometry in this `3/2` mixed-minor interface.

## 8. Arithmetic checks

The companion checker verifies

- `3456^(1/5)=5.101698002503164...`;
- the `q=1` diffuse constant `5e*3456^(1/5)=69.33926487245078...`;
- the `q=6/5` diffuse constant `25e sqrt(5/6)*3456^(1/5)=316.4889957622237...`;
- `(3/5)/6912=1/11520`;
- the integrability gap at `q=6/5`: `5/2-2q=1/10>0`.

These finite computations check arithmetic only; the theorem above is analytic.
