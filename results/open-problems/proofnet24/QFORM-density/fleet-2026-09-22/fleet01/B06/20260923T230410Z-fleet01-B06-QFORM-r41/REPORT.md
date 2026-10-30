SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet01, slot B06, 2026-09-23T23:04:10Z.
attacking: the r38 small-pivot transverse-star branch — replace the fragile outer scalar square by an indefinite original physical pair, then spend the exact rank-one Schur crossing through a quarter-Riesz product receiver.

# fleet01/B06 r41 — indefinite physical pair plus rank-one crossing quarter-Riesz receiver

Programme: `QFORM-DENSITY-3EIG-20260922`  
Run: `20260923T230410Z-fleet01-B06-QFORM-r41`  
Role: curved fiber integration / analytic derivation and exact structural identities  
Status: **SUPPORTING ANALYTIC THEOREM PROVED / DESIGNATED PARTNER APPLIED / SMALL-PIVOT TRANSVERSE-STAR SUBBRANCH CLOSED / FULL TARGET OPEN**  
Execution: `WITHOUT_VERIFIED_BRAIN`.

The unrestricted QFORM conjecture remains OPEN. The new argument proves a product-preserving density receiver for an indefinite physical pair followed by a rank-one physical crossing. It is then applied to the small-background-diagonal part of r38's transverse-star packet, removing the division by that small diagonal. No Gaussianity, moment, compact-support, connected-support, log-concavity, iid, diagonal-basis, or post-rotation-independence assumption is introduced. Continuity is not claimed for the new branch.

## 1. Fresh source boundary and dependencies


Corrections retained include: no law-uniform pointwise quadratic-phase decay; no unrestricted fiber supremum; no arbitrary-joint coarea cap; no positive moment of worst conditional projection-density caps; no independence after rotation; no uniformly good single-minor inference; and the recent `QFORM-RANK1-SAMEBANK-HALFRIESZ-FALSE-v1`. The theorem below is not a same-bank argument: the scalar crossing hub and the bank are disjoint original-coordinate product groups.

Inputs actually used:

1. Own `QFORM-INDEFINITE-PHYSICAL-PAIR-QUARTER-RIESZ-v1`, `yspennstate/math-open-problems@ababe93762d210413fe9f19389e3b45f5dd150ba`, `proofnet24/QFORM-density/fleet-2026-09-22/fleet01/B06/20260923T130129Z-fleet01-B06-QFORM/REPORT.md`. For two original independent cap-one coordinates with invertible indefinite symmetric physical pair `B`, `D=|det B|`, and arbitrary affine terms,

   `p_F(t) <= 2 sqrt(3) D^(-3/8) |t-t0|^(-1/4)`.                 (1.1)

2. Independently checked exact-rank crossing theorem, `yspennstate/math-open-problems@829192412f2a2d84e72b4bed91115fc5fab68401`, `proofnet24/QFORM-density/interactive/20260923T164118Z-full-proof-paper/NEW_PROJECTED_CROSSING.md`. For rank `r`, arbitrary internal functions on the two independent banks are retained.

3. Designated partner fleet02/B06 `QFORM-WEIGHTED-AFFINE-FIBER-BL-v1`, canonical source `yspennstate/math-open-problems@8dd33c1abd4fd64140f59032feda2b13d4351da5`. At the actual equation below it gives, for every unit original-coordinate coefficient vector `v`,

   `||p_(v dot Z)||_infinity <= sqrt(e)`.                          (1.2)

The latest partner theorem `QFORM-E2-HALFRIESZ-ROW-GATE-FREE-v1` remains compatible background but is not needed for the new rank-one quarter-potential estimate.

## 2. Rank-one physical crossing controls a quarter-Riesz potential

Let `H` be one original scalar coordinate with density at most one. Let `Z=(Z_j)` be a disjoint original product bank, independent of `H`, with each scalar density at most one. Let `r` be a nonzero real coefficient vector, and allow arbitrary measurable real internal functions `F,G`. Set

`S = F(H) + 2 H (r dot Z) + G(Z)`.                                 (2.1)

Define

`H_(1/4)(S) = sup_a E |S-a|^(-1/4)`.                              (2.2)

### Theorem 2.1 — `QFORM-RANK1-CROSS-QUARTERRIESZ-v1`

Under (2.1),

`boxed:
 H_(1/4)(S) <= C_1 ||r||_2^(-1/4),`                               (2.3)

where

`C_1 = 8 pi^(1/4) e^(1/8) /
       [Gamma(1/4) cos(pi/8)]
     = 3.603029719786... .`                                        (2.4)

### Proof

Normalize `v=r/||r||`. The designated fleet02/B06 theorem (1.2), applied here to the genuine original product bank, gives

`||p_(v dot Z)||_infinity <= sqrt(e)`.                              (2.5)

Use the exact-rank crossing theorem with rank one, left projection density cap `M_H<=1`, right projection cap `M_Z<=sqrt(e)`, and singular value `||r||`. Arbitrary `F` and `G` are permitted. Thus

`|phi_S(t)|
 <= min(1, K |t|^(-1/2)),
 K = sqrt(pi) e^(1/4) ||r||^(-1/2).`                               (2.6)

For `0<alpha<1`,

`|x|^(-alpha)
 = [Gamma(alpha) cos(pi alpha/2)]^(-1)
   int_0^infinity cos(tx) t^(alpha-1) dt`                           (2.7)

in the standard regularized sense. Multiplying the Fourier side by a Gaussian cutoff and using the positive heat regularization of `|x|^-alpha`, followed by Fatou, gives for `alpha=1/4`

`E|S-a|^(-1/4)
 <= [Gamma(1/4)cos(pi/8)]^(-1)
    int_0^infinity t^(-3/4)|phi_S(t)|dt`.                          (2.8)

The crossover in (2.6) is `t=K^2`, and exactly

`int_0^infinity t^(-3/4) min(1,Kt^(-1/2)) dt
 = int_0^(K^2)t^(-3/4)dt
   +K int_(K^2)^infinity t^(-5/4)dt
 =8 sqrt(K).`                                                       (2.9)

Since `sqrt(K)=pi^(1/4)e^(1/8)||r||^-1/4`, (2.3)-(2.4) follow. QED.

This is the desired aggregate-before-supremum mechanism: the full original product bank is compressed only through its one-dimensional projection-density theorem, then the rank-one crossing Fourier envelope is integrated against the quarter-Riesz weight. No fiber maximum or individual coefficient reciprocal is used.

## 3. An indefinite physical pair supplies the other three quarters

Let `X_1,X_2,H,Z` be mutually disjoint original-coordinate product groups, with `X_1,X_2,H` scalar. Suppose the quadratic matrix on `(X_1,X_2)` is an invertible indefinite symmetric `2x2` matrix `B`, `D=|det B|`. After exact Schur completion of this physical pair, suppose its critical-value remainder has the form (2.1), with arbitrary same-bank curvature inside `G`.

### Theorem 3.1 — `QFORM-INDEFINITE-PAIR-PLUS-RANK1-CROSS-v1`

The full quadratic form has an essentially bounded density satisfying

`boxed:
 ||p_Q||_infinity
 <= C_* D^(-3/8)||r||^(-1/4),`                                    (3.1)

with

`C_* = 2sqrt(3) C_1
     = 12.481261071701... .`                                       (3.2)

### Proof

Condition on `(H,Z)`. The affine terms induced in `(X_1,X_2)` are arbitrary, so (1.1) applies uniformly and its critical value is exactly the Schur remainder `S(H,Z)`:

`p_(Q|H,Z)(q)
 <=2sqrt(3)D^(-3/8)|q-S(H,Z)|^(-1/4).`                             (3.3)

Average (3.3), take the supremum in `q`, and apply Theorem 2.1. QED.

The two original variables in the indefinite pair remain independent because no probabilistic rotation is performed. The scalar hub `H` and bank `Z` are also genuine disjoint original-coordinate groups.

## 4. Exact zero-anchor Schur identity: the crossing is a star wedge

Return to the live zero-anchor chamber

`A = [[0,0,a^T],
      [0,0,b^T],
      [a,b,C]]`,                                                    (4.1)

with original hub coordinates `X,Y` and original background coordinates `Z_1,...,Z_m`.

Fix a background index `i` with `a_i !=0`. Use the **physical pair** `(X,Z_i)`, whose matrix is

`B_i = [[0,a_i],[a_i,c]],   c=C_ii`,                               (4.2)

so

`det B_i=-a_i^2`,                                                   (4.3)

hence it is invertible indefinite for every real `c`, including arbitrarily small or zero `c`. Its exact inverse is

`B_i^(-1) = [[-c/a_i^2,1/a_i],[1/a_i,0]].`                         (4.4)

The pair cross-column to `Y` is `(0,b_i)^T`, while the pair cross-column to `Z_j`, `j!=i`, is `(a_j,C_ij)^T`. Therefore the Schur remainder has

`(Y,Y) coefficient =0`,                                            (4.5)

and

`(Y,Z_j) coefficient
 = b_j - (b_i/a_i)a_j`.                                            (4.6)

All arbitrary background curvature from `C` remains inside the internal `Z_-i` function and is allowed by Theorem 3.1.

Define the physical wedge-anchor vector

`w^(i)=a_i b-b_i a`,
 L_i=||w^(i)||_2.                                                   (4.7)

Its `i`-th component is zero, and (4.6) says the rank-one Schur crossing vector has norm

`||r||=L_i/|a_i|`.                                                  (4.8)

Theorem 3.1 with `D=a_i^2` therefore gives the c-free bound

`boxed:
 ||p_Q||_infinity
 <= C_* |a_i|^(-1/2)L_i^(-1/4),`                                  (4.9)

whenever `a_i!=0` and `L_i>0`. The symmetric statement with the physical pair `(Y,Z_i)` is

`||p_Q||_infinity
 <= C_* |b_i|^(-1/2)L_i^(-1/4)`.                                  (4.10)

Consequently, with

`alpha_i=max(|a_i|,|b_i|)`,                                        (4.11)

we have the concise physical-coordinate receiver

`boxed:
 ||p_Q||_infinity
 <= C_* alpha_i^(-1/2)L_i^(-1/4)`                                 (4.12)

for every index with `alpha_i L_i>0`.

This is a genuine small-pivot repair: the background diagonal `c=C_ii` has disappeared completely from the analytic denominator.

## 5. Exact coefficient-plane geometry

Let

`G = [[||a||^2,a dot b],[a dot b,||b||^2]],
 Delta^2=det G.`                                                    (5.1)

For `v_i=(a_i,b_i)^T`, direct expansion gives

`boxed:
 L_i^2 = v_i^T adj(G) v_i.`                                        (5.2)

When `Delta>0`, if

`ell_i=v_i^T G^(-1)v_i`                                            (5.3)

is the normalized physical leverage of the coefficient plane, then

`boxed: L_i=Delta sqrt(ell_i),    sum_i ell_i=2.`                   (5.4)

Thus (4.12) pays a physical anchor by the product of its literal star magnitude and its coefficient-plane wedge leverage; it does not select a background diagonal.

For the near-collinear parameterization

`b=lambda a+epsilon`, `epsilon perpendicular a`,                    (5.5)

there is also the exact identity

`boxed:
 L_i^2=a_i^2||epsilon||^2+epsilon_i^2||a||^2.`                     (5.6)

Hence failure of (4.12) at a star-heavy coordinate can occur only through genuine global near-collinearity of the two star rows, not through a small `C_ii`.

## 6. Apply to r38's small-pivot transverse-fourth-power currency

Use r38 notation at a nonzero pivot `c=C_ii`. Let

`p=(a_i,b_i)`, `P=||p||`,                                          (6.1)

and rotate the two-dimensional hub coefficient plane only to evaluate the deterministic Schur identity, aligning `p` with the first axis. The transverse hub-to-bank coefficient from r38 is then, up to sign,

`n_j=(a_i b_j-b_i a_j)/P`.                                         (6.2)

Therefore

`L_i=P||n||`.                                                       (6.3)

Choose the physical hub `h` with coefficient

`p_h=max(|a_i|,|b_i|)>=P/sqrt(2)`.                                 (6.4)

Applying (4.12) and (6.3),

`||p_Q||_infinity
 <= C_* p_h^(-1/2)(P||n||)^(-1/4)
 <= C_* 2^(1/4) P^(-3/4)||n||^(-1/4).`                            (6.5)

R38's transverse-fourth-power alternative is

`sum_j n_j^4 >= D0/2`,                                             (6.6)

where for `c!=0`

`D0=sum_j delta_j^2=D_i^diag/c^2`.                                 (6.7)

Since `||n||_2^4 >= sum_j n_j^4`, (6.5)-(6.7) yield

`boxed:
 ||p_Q||_infinity
 <= C_* 2^(5/16)
    P^(-3/4)|c|^(1/8)(D_i^diag)^(-1/16).`                          (6.8)

The numerical front constant in (6.8) is

`C_*2^(5/16)=15.499951566421... .`                                 (6.9)

### Target-scale small-pivot corollary

Let `s=s_3(A)>0`. In the live r38 transverse-packet branch, assume

`P>=s/16`,
`0<|c|<=s/16`,
`D_i^diag>=81 s^6/2^24`,                                           (6.10)

and (6.6). Then (6.8) gives

`boxed: ||p_Q||_infinity <188.439/s.`                              (6.11)

The scaling is exact:

`P^(-3/4)|c|^(1/8)(D_i^diag)^(-1/16)`

has total quadratic scale `s^-1` under (6.10).

R39 already paid the same transverse-fourth-power currency when `|c|>=s/16` (under its target-scale packet gates) with `<246.116/s`. Thus the former dependence on a **large** background scalar pivot is removed throughout the subbranch (6.10): the small-pivot side is paid by an indefinite pair that remains nondegenerate because its determinant is `-p_h^2`, not by dividing by `c`.

The exact `c=0` case is already covered by the general c-free receiver (4.12) whenever `L_i>0`; equation (6.8) itself should not be used at `c=0` because r38's normalization `D0=D_i^diag/c^2` is then undefined.

## 7. Finite exact/algebraic checks

A direct numerical Schur-complement check over dimensions `m=2,3,7,12`, ten random trials each, verified (4.5)-(4.6) with maximum absolute discrepancy `1.78e-15`.

The constants were independently recomputed from the closed forms:

`C_1=3.6030297197863614`,
`C_*=12.481261071701265`,
`C_*2^(5/16)=15.499951566420881`,
small-pivot target constant `188.43866121660622`.

These checks are verification aids, not the proof.

## 8. What remains open

The new theorem closes the **small-background-pivot / transverse-fourth-power** subbranch whenever the star anchor `P` is target-scale, and more generally supplies the c-free receiver (4.12). It does not by itself pay:

- the simultaneous small-star state `P<s/16` at the distinguished collision coordinate;
- r38's longitudinal currency `sum_j(rho d_j+m_j^2)^2`;
- r40's genuinely near-collinear mixed-currency residue when the physical wedge `L_i` is too small;
- arbitrary higher-rank global configurations not reduced to this zero-anchor chamber.

The next local implication is therefore

`QFORM-SMALL-STAR-OR-LONGITUDINAL-BANK-AFTER-PAIR-PEEL-v1`:

> after the c-free physical-pair receiver, route simultaneous small star/wedge leverage to the existing aggregate crossing/volume branches, or spend the longitudinal same-sign diagonal bank jointly with the near-collinear hub while retaining arbitrary same-bank curvature.

The full arbitrary-dimensional QFORM conjecture remains **OPEN**. No target counterexample was found. Global continuity remains **OPEN**; this run proves essential boundedness only in the stated branches. Independent end-to-end review of the new r41 theorem is pending.
