SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B06, 2026-09-24T04:51:24Z.
attacking: `QFORM-MIXED-LAYER-NORMAL-INNOVATION-RECEIVER-v1`; integrate a genuinely shared normal statistic by the complete three-frame product Fourier volume, and aggregate the whole mixed 3x3-minor bank before any scalar-pivot reciprocal is taken.

# account03/B06 r53 — same-bank normal curved sections and mixed-minor pivot aggregation

Programme: `QFORM-DENSITY-3EIG-20260922`  
Assignment: curved fiber integration / quantitative inequalities and rigorous computations  
Status: **TWO NEW SUPPORTING THEOREMS + TARGET-LEVEL PAID BRANCH + DESIGNATED PARTNER APPLIED / FULL QFORM OPEN**  
Execution: **WITHOUT_VERIFIED_BRAIN**

The unrestricted conjecture remains OPEN / NOT PROVED / NOT DISPROVED. No Gaussian, log-concavity, moment, compact-support, connected-support, iid, diagonal-basis, post-rotation independence, arbitrary-joint coarea cap, unrestricted fiber supremum, or law-uniform pointwise quadratic van-der-Corput estimate is used. Continuity is stated only where an `L^1` Fourier estimate is proved.

The immediate predecessor is account03/B06 r52,

`yspennstate/math-open-problems@87d28c657b28f8f816f4b72e6b92af8dd52398c0`

at

`proofnet24/QFORM-density/fleet-2026-09-22/account03/B06/20260924T042233Z-account03-B06-qform-r52/REPORT.md`.

Its low-Pluecker-disjoint branch puts the rank-three core into the literal three-hub form

`A_0=[I_3,Z]^T B [I_3,Z]`,                                      (1.1)

with `B=B^T` invertible, while the full matrix retains an arbitrary physical diagonal perturbation `D`. Writing `G=ZZ^T`, `beta=det B`, and

`P_0=|beta|`, `P_1=|beta| e_1(G)`, `P_2=|beta| e_2(G)`, `P_3=|beta| det G`,

r52 proves that its low-disjoint branch satisfies

`max(P_0,P_1,P_2)>5P/16`,                                       (1.2)

where `P=P_0+P_1+P_2+P_3` is the complete rank-three volume. It also isolates a true same-bank normal statistic after one literal hub pivot. The first unpaid analytic interface was precisely a nonzero normal innovation sharing its product bank with the curved two-plane.

The present run attacks that interface first rather than treating the normal statistic as independent or replacing the curved fiber by a supremum.

## 2. Same-bank normal curved-section theorem

Let `X=(X_i)_(i in S)` be independent original coordinates with probability densities at most one. Let

`w,v,n in R^S`

be orthonormal and assume the **three-frame diffuse gate**

`w_i^2+v_i^2+n_i^2 <= 1/2` for every `i in S`.                   (2.1)

Put

`L=<w,X>`, `V=<v,X>`, `N=<n,X>`.                                (2.2)

Let `R` be a disjoint original-coordinate bank and let `B_R` be any measurable random variable determined by `X_R`, so `B_R` is genuinely independent of `(L,V,N)`. No density assumption on `B_R` is made.

### Theorem 2.1 — `QFORM-SAMEBANK-NORMAL-CURVED-SECTION-v1`

For arbitrary real `alpha,gamma,c,v_0`, nonzero `lambda`, and nonzero `beta`, define

`Y=lambda(V-v_0)^2 + alpha L + gamma V + beta N + B_R + c`.       (2.3)

Then the two-dimensional law of `(L,Y)` has a continuous `C_0` density `g` satisfying

`boxed: ||g||_infinity <= 16 / sqrt(|lambda beta|).`              (2.4)

The result is uniform in the input laws, in `alpha,gamma,c,v_0`, and in the law and size of the fresh-bank term `B_R`. The same product bank is allowed to generate `L,V,N`; no independence among those three projections is asserted.

### Proof

A determinant-one output shear removes `alpha L` from the second output. Completing the square in `V` absorbs `gamma V` into a new center `v_*`; constants are irrelevant. Adding the independent variable `B_R` is convolution in the second output coordinate and cannot increase an `L^infinity` norm. It therefore suffices to treat

`(L, lambda(V-v_*)^2 + beta N)`.                                 (2.5)

For the original one-dimensional densities write

`psi_i(u)=int exp(iux) f_i(x) dx`.                               (2.6)

Two completed product-Fourier inputs are source-pinned in the designated-partner line:

1. for every Parseval two-frame whose row leverage is at most `1/2`, uniformly under coordinatewise translations,

`int_(R^2) prod_i |psi_i(sw_i+xi v_i+c_i)| ds dxi <= (4pi)^2`;    (2.7)

2. for every Parseval three-frame whose row leverage is at most `1/2`, again translation-uniformly,

`int_(R^3) prod_i |psi_i(sw_i+xi v_i+r n_i+c_i)| ds dxi dr <= (4pi)^3`.   (2.8)

Equation (2.7) is written explicitly in account04/B06 r2, commit
`769800c0ab0851828772adabfb6874aa813e423d`; equation (2.8) is written explicitly in account04/B06 r1, commit
`f24c8db8946d54f4da2d11898697913af766ad32`. Both ultimately use the sharp one-dimensional estimate

`int |psi_i(u)|^p du <= 4pi/sqrt(p), p>=2`,                      (2.9)

and geometric Brascamp--Lieb. The full gate (2.1) implies the needed two-frame gate for `(w,v)` as well.

Let `Phi(s,t)` be the joint characteristic function of (2.5). Use the same damped Fresnel linearization as account04/B06 r1, then remove the damping by dominated/Fatou passage. For `t!=0`, after translating the Fresnel variable to absorb `v_*`,

`|Phi(s,t)|
 <= [4pi |lambda t|]^(-1/2)
    int_R prod_i |psi_i(s w_i + xi v_i + t beta n_i)| dxi.       (2.10)

Integrate (2.10) in `(s,t)` and set `r=beta t`. Define

`A(r)=int_(R^2) prod_i |psi_i(s w_i+xi v_i+r n_i)| ds dxi`.       (2.11)

Then

`int_(R^2)|Phi(s,t)| ds dt
 <= [4pi |lambda beta|]^(-1/2)
    int_R |r|^(-1/2) A(r) dr.                                    (2.12)

The point is to spend the **whole product Fourier volume before the singular weight**. By (2.7), uniformly in `r`,

`A(r)<=(4pi)^2`,                                                 (2.13)

while (2.8) gives

`int_R A(r) dr <=(4pi)^3`.                                       (2.14)

For any `R_0>0`, split the weighted integral at `|r|=R_0`:

`int |r|^(-1/2)A(r)dr
 <=4(4pi)^2 sqrt(R_0)+(4pi)^3/sqrt(R_0).`                         (2.15)

The two terms balance at `R_0=pi`, giving

`int |r|^(-1/2)A(r)dr <=4(4pi)^(5/2).`                           (2.16)

Substitution into (2.12) yields

`int_(R^2)|Phi| <= 4(4pi)^2 / sqrt(|lambda beta|).`               (2.17)

Two-dimensional Fourier inversion divides by `(2pi)^2`, so

`||g||_infinity <= 16 / sqrt(|lambda beta|)`.                    (2.18)

Since `Phi in L^1(R^2)`, the density is continuous and vanishes at infinity. This proves the theorem. QED.

### What this theorem changes

The previous partner theorem paid **exactly tangential** shared leakage, but left a positive normal innovation as the first obstruction. Theorem 2.1 pays every nonzero normal coefficient on a diffuse three-frame by integrating the product Fourier volume jointly. It does not claim a bound uniform as `beta ->0`; the exact zero endpoint is handled separately below by the designated partner.

If a normalized three-frame fails (2.1), its leverage scores sum to three, so there are at most five literal original coordinates with leverage `>1/2`. Thus failure of the analytic gate produces a finite heavy-coordinate certificate rather than a dimension-dependent fiber supremum.

## 3. Actual designated-partner application

The freshest completed designated account04/B06 result available in the run is

`QFORM-TANGENTIAL-SHARED-LEAKAGE-ABSORPTION-v1`,

`yspennstate/math-open-problems@a09353b7b4cc9b1b812b1d1f2f319f5dcef5e10b`,

`proofnet24/QFORM-density/fleet-2026-09-22/account04/B06/20260924T001014Z-account04-B06-QFORM-r3/REPORT.md`.

At the **actual normal-zero inequality** `beta=0`, (2.3) reduces to its exact tangential shared-bank form after fold recentering and the determinant-one output shear. Therefore on

`|V-v_*|>r`

that theorem gives

`boxed: ||g_r||_infinity <=4/(|lambda| r).`                      (3.1)

At the live off-fold scale `r=1/64`,

`boxed: ||g_(1/64)||_infinity <=256/|lambda|`,                   (3.2)

and in particular `<=256` when `|lambda|>=1`. This is a real application at the exact endpoint `beta=0`; it is not extrapolated to nonzero same-bank normal leakage. For `beta!=0`, Theorem 2.1 supplies instead the global two-output estimate (2.4), under the stronger three-frame diffuse gate.

Thus the two analytic mechanisms meet correctly at the structural split: designated-partner tangential absorption at exact normal zero, and complete product-Fourier integration for every nonzero normal coefficient. No false convolution of a shared normal statistic is used.

## 4. Exact complete mixed-minor identity for the r52 three-hub normal form

I now return to the full scalar quadratic form and prove an aggregate identity that directly spends the r52 `P_2` layer whenever the hub diagonal perturbation does not collapse the corresponding finite-dimensional currency.

Let

`F=[I_3,Z]`, `A=F^T B F + D`,                                   (4.1)

where `B=B^T` is invertible, `Z in R^(3xm)`, and `D` is an **arbitrary diagonal matrix in the original coordinates**. Let

`beta=det B`, `G=ZZ^T`, `D_H=diag(d_1,d_2,d_3)`,
`K=B+D_H`, `a_h=K_hh`.                                          (4.2)

Only the three hub diagonal entries occur in the mixed-minor identity; all tail diagonal entries remain present in the full quadratic form but disappear from the cross minors below.

For a tail pair `p<q`, define the oriented two-form vector

`U(p,q)=z_p x z_q in R^3`,                                      (4.3)

where `z_p` is the `p`th column of `Z`. Its `h`th component is exactly

`U_h(p,q)=det[e_h,z_p,z_q]`.                                    (4.4)

For each hub `h` define the complete mixed 3x3-minor vector

`L_h(p,q)=det A[H,{h,p,q}]`, `H={1,2,3}`.                       (4.5)

### Theorem 4.1 — `QFORM-MIXED-CROSSMINOR-AGGREGATE-v1`

Put

`M=K B^(-1)=I_3+D_H B^(-1)`.                                   (4.6)

Then the complete mixed-minor bank satisfies the exact vector identity

`L = beta M U`,                                                  (4.7)

and hence

`boxed:
 sum_h ||L_h||_2^2
 = beta^2 tr[ M adj(G) M^T ].`                                  (4.8)

If `D_a=diag(a_1,a_2,a_3)`, the weighted identity is

`boxed:
 Gamma := sum_h a_h^2 ||L_h||_2^2
 = beta^2 tr[ D_a^2 M adj(G) M^T ].`                             (4.9)

Both identities remain polynomially meaningful when `G` is singular; `adj(G)` is the ordinary adjugate.

#### Proof

The hub-to-tail core columns are `Bz_p`. In the mixed determinant (4.5), the only diagonal perturbation that can occur is the one at the shared hub coordinate `h`. Multilinearity therefore gives

`L_h(p,q)
 = det[B e_h+d_h e_h, Bz_p,Bz_q]
 = beta det[e_h,z_p,z_q]
   +d_h det[e_h,Bz_p,Bz_q].`                                    (4.10)

For any vectors `u,v in R^3`,

`Bu x Bv = beta B^(-T)(u x v)`.                                 (4.11)

Since `B` is symmetric,

`det[e_h,Bu,Bv]
 = beta sum_l (B^(-1))_(hl) det[e_l,u,v].`                       (4.12)

Equations (4.10)-(4.12) are exactly (4.7).

The exterior Cauchy--Binet identity gives

`sum_(p<q) U(p,q) U(p,q)^T = adj(ZZ^T)=adj(G).`                  (4.13)

Taking Hilbert--Schmidt norms in (4.7) proves (4.8), and multiplying row `h` by `a_h` before taking the norm proves (4.9). QED.

This is the requested **weighted replacement for selecting a favorable fiber maximum**: every physical tail pair is summed before any reciprocal quantity is taken.

## 5. Schur interpretation and a full scalar density payment

For a hub `h` with `a_h!=0`, let `J=H\{h}` and complete that literal original-coordinate square. Its Schur cross block between the two remaining hubs and the complete tail bank is

`N_h=A[J,T]-A[J,h] A[h,T]/a_h`.                                (5.1)

Let `Delta_h` be the product of the two singular values of this `2xm` block, with `Delta_h=0` if its rank is less than two.

For every tail pair `p<q`, the block determinant identity gives

`det A[H,{h,p,q}] = a_h det N_h[:,{p,q}].`                       (5.2)

Cauchy--Binet therefore yields

`boxed: ||L_h||_2=|a_h| Delta_h.`                                (5.3)

Consequently (4.9) is equivalently

`boxed:
 Gamma=sum_h (|a_h|^2 Delta_h)^2,`                               (5.4)

where the term is interpreted as zero at `a_h=0`.

Now use the completed rank-two-cross scalar-pivot theorem
`QFORM-RANK2-CROSS-SCALAR-PIVOT-v1`, source

`yspennstate/math-open-problems@38724ac681c4d046c3c843145121528135d3846b`

at

`proofnet24/QFORM-density/fleet-2026-09-22/account03/B18/20260923T102742Z-account03-B18-QFORM-r26/REPORT.md`.

It retains arbitrary same-side Schur curvature and proves

`||p_Q||_infinity <=8 (|a_h|^2 Delta_h)^(-1/4)`                  (5.5)

whenever that currency is nonzero. Since one of the three terms in (5.4) is at least `sqrt(Gamma/3)`, we obtain the target-level branch

### Corollary 5.1 — `QFORM-MIXED-CROSSMINOR-SCALARPIVOT-PAYMENT-v1`

If `Gamma>0`, the **complete ambient scalar quadratic form** (4.1), with every tail diagonal term and all same-side Schur curvature retained, has an essentially bounded density satisfying

`boxed:
 ||p_Q||_infinity <=8 (Gamma/3)^(-1/8).`                         (5.6)

No continuity assertion is made for this scalar-pivot wrapper.

The proof conditions only on disjoint ORIGINAL-coordinate banks and never declares spectral coordinates independent.

## 6. Quantitative connection to the r52 `P_2` mixed layer

Recall

`P_2=|beta| e_2(G)=|beta| tr(adj G).`                            (6.1)

Set

`tau=min_h |a_h|`,
`mu=sigma_min(KB^(-1)).`                                        (6.2)

From (4.9), positivity of `adj(G)` gives

`Gamma >= beta^2 tau^2 mu^2 tr(adj G)
       = tau^2 mu^2 |beta| P_2.`                                (6.3)

Hence on the actual r52 branch

`P_2>5P/16`,                                                     (6.4)

if `tau>0` and `mu>0`, Corollary 5.1 gives the explicit full-scalar estimate

`boxed:
 ||p_Q||_infinity
 < 8 [48/(5 tau^2 mu^2 |beta| P)]^(1/8).`                        (6.5)

This is not yet a universal numerical constant because `tau` and `mu` can collapse. What matters structurally is that **the entire P2 mixed layer is now paid unless a finite three-hub degeneration occurs**:

- `tau` small means an actual literal hub diagonal `a_h` is small;
- `mu` small means the actual hub block `K=B+D_H` is nearly singular relative to the core metric `B`.

No high-dimensional fiber supremum remains in this branch. Those are finite-dimensional hub degeneracies that can be handed to physical-pair/zero-pivot receivers.

The unweighted identity (4.8) is also informative: without hub diagonal perturbation, `K=B`, so

`sum_h ||L_h||^2=beta^2 e_2(G)=|beta|P_2`.                       (6.6)

Thus the `P_2` layer is literally the complete mixed 3x3-cross-minor energy before diagonal cancellation.

## 7. Connection back to the r52 normal statistic

In the r52 near-null-row decomposition, for a chosen hub row `h` one has a two-row matrix `Z_J`, Gram `G_2=Z_JZ_J^T`, and a true normal residual

`n_h=P_(ker Z_J) z_h`, `||n_h||^2<1/5`.                          (7.1)

When `n_h!=0`, define the normalized three-frame on the **same original tail bank** by

`(w^T;v^T)=G_2^(-1/2) Z_J`,
`n=n_h/||n_h||`.                                                 (7.2)

The three rows are orthonormal. If every physical leverage

`ell_i=w_i^2+v_i^2+n_i^2 <=1/2`,                                (7.3)

Theorem 2.1 is available for the canonical curved-section interface carrying a nonzero scalar normal coefficient. If (7.3) fails, because `sum_i ell_i=3`, at most five literal tail coordinates can be heavy. Thus positive normal innovation is no longer analytically blocked by same-bank dependence in the diffuse case; the remaining work is a **deterministic compiler** from r52's two-component normal coefficient vector into a scalar curved-section channel with quantitative `lambda beta`, or a routing of the at-most-five heavy coordinates.

Separately, Theorem 4.1/Corollary 5.1 already gives a full scalar payment whenever the aggregate mixed-pivot currency `Gamma` is quantitative, without passing through that compiler.

## 8. Deterministic checks

A fixed-seed checker tests 5,000 random symmetric invertible `B`, random `Z`, and random hub diagonal perturbations. It verifies:

1. `||L_h||=|a_h| Delta_h` from (5.2)-(5.3);
2. the unweighted trace identity (4.8);
3. the weighted trace identity (4.9).

The largest normalized discrepancies were respectively about

`2.03e-13`, `1.29e-15`, and `1.87e-15`.

The same checker independently evaluates the two-/three-frame split in (2.15): at the optimizer `R_0=pi` the near and far contributions are equal and Fourier inversion gives exactly the constant `16` in (2.4). These finite-precision computations are sanity checks only; Sections 2 and 4-6 contain the proofs.

## 9. Scope, corrections, and exact next debt

The full QFORM conjecture remains **OPEN / NOT PROVED / NOT DISPROVED**. Global continuity remains **OPEN**.

New continuous branch: Theorem 2.1 gives a `C_0` two-output density for nonzero same-bank normal coefficient on a diffuse three-frame. Designated partner r3 gives a `C_0` off-fold two-output density at exact normal zero. New scalar branch: Corollary 5.1 gives absolute continuity and essential boundedness, but continuity is not claimed.

The next exact B06 debt is

`QFORM-P1-OR-HUBDEGENERATE-MIXED-LAYER-COMPILER-v1`:

> In the r52 low-disjoint packet, consume either the remaining `P_1>5P/16` layer or the finite three-hub degenerations `tau ->0` / `sigma_min(KB^(-1))->0` left by the P2 payment. Use the new same-bank normal receiver when a scalar normal curved channel is exposed; otherwise route the at-most-five three-frame-heavy tail coordinates and the literal hub degeneracy through a source-valid physical-pair/one-hub receiver. Retain the complete diagonal tail and every nonzero spectral term.

Binding corrections retained: bounded density alone does not imply law-uniform pointwise quadratic phase decay; arbitrary projected joint density does not imply an indefinite quadratic pushforward cap; worst conditional projection caps may diverge; small random quadratic terms cannot be deleted for unbounded fragmented laws; rotations do not preserve coordinate independence; repeated eigenvalues are not Hessian degeneracy; no Monte Carlo histogram is evidence of a universal theorem.

No scheduler, task identity, email, notification, permission, public-release, cross-account-authentication, paid API/model, or remote-workflow state is changed by this report.
