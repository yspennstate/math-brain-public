SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B04, 2026-09-24T10:46:54Z.
attacking: exactly optimize the arbitrary-self random-slope pair compiler and remove the exact zero-Schur-diagonal restriction from the aggregate row certificate, retaining the full physical row before inversion.

# account01/B04 r35 — arbitrary-self exact optimizer and nonzero-self Schur-row certificate

Programme: `QFORM-DENSITY-3EIG-20260922`  
Role: Product Fourier rearrangement  
Status: **NEW SUPPORTING OPTIMIZATION + NEW ARBITRARY-SELF SCHUR-ROW COROLLARY / FULL QFORM OPEN**  
Regularity: essential boundedness in the new pair+row branch; continuity is **not** claimed.  
Execution: `WITHOUT_VERIFIED_BRAIN`.

## 1. Fresh source boundary


The key completed analytic dependency is account02/B14 r34:

- repository/commit: `yspennstate/math-open-problems@ee5472663f2f7934749ac90f2a0305a4cbda37b0`;
- path: `proofnet24/QFORM-density/fleet-2026-09-22/account02/B14/20260923T112750Z-account02-B14-QFORM-r34/REPORT.md`;
- theorem: `QFORM-ARBITRARY-SELF-RANDOM-SLOPE-MASS-v1`.

That theorem removes the exact-zero self restriction by copy-differencing one genuine original-coordinate hub. It keeps arbitrary self curvature and arbitrary correlation of the bank remainder with the random slope.

The designated account02/B04 partner result actually applied below is r22:

- repository/commit: `yspennstate/math-open-problems@2311fa678098f3ac7b96e5eb3795d9def07cc2fd`;
- path: `proofnet24/QFORM-density/fleet-2026-09-22/account02/B04/20260924T091038Z-account02-B04-QFORM-auto11-r22/REPORT.md`;
- theorem: `QFORM-ZEROPIVOT-J1-WEIGHTED-MIXED-HUB-v1`.

Its deterministic checker is committed at `a3c536edd7183f5078f5571c5a44d57761ee68ce` with output at `689fe56a9700330a4e242c3e2fe6b2cf4e045c6e`.

No law-uniform pointwise quadratic-phase decay, post-rotation independence, arbitrary-joint coarea, support radius, moments, compactness, connected support, Gaussianity, or perturbative deletion of a small random quadratic term is used.

## 2. Input compiler with arbitrary self curvature

Let an outer pair of **original independent coordinates** have invertible indefinite symmetric block `B`. Put

`D=|det B|`, `kappa=sigma_min(B)>0`.                               (2.1)

After exact pair completion, let the remaining active probability law have one original-coordinate hub `X` and an independent original-coordinate bank `V`, with

`Y=h X^2+X S(V)+R(V)`,                                             (2.2)

where `h` is arbitrary, `R` may be arbitrarily correlated with `S`, and the scalar slope `S(V)` has probability density cap `H`.

Account02/B14 r34 proves the exact one-parameter certificate

`||p_Q||_infinity`
` <= inf_(q>0) [ 8 q^(-1/2) sqrt(H/kappa) + D^(-1/2) J(q) ],`      (2.3)

where, writing

`eta=sqrt(2 pi e) erfc(1/sqrt(2))`,                               (2.4)

one has

`J(q)=log(2q)+2+eta`,                           `q>=1/2`,           (2.5)

and for `0<q<=1/2`, with `y=log(1/(2q))`,

`J(q)=sqrt(2q) int_0^infinity e^(-v/2)sqrt(1+y+v) dv.`            (2.6)

The source report used the convenient choice `q=1`. The first new step here is to solve (2.3) exactly.

## 3. Exact optimization

Define the dimensionless parameter

`rho=8 sqrt(DH/kappa)`                                             (3.1)

and

`Psi(rho)=inf_(q>0) [rho q^(-1/2)+J(q)].`                          (3.2)

Then (2.3) becomes

`||p_Q||_infinity <= D^(-1/2) Psi(rho).`                           (3.3)

### Theorem 3.1 — `QFORM-ARBITRARYSELF-RANDOM-SLOPE-EXACT-OPTIMIZER-v1`

Let

`eta=sqrt(2 pi e) erfc(1/sqrt(2))`
`   =1.3113590848375969... .`                                     (3.4)

For every `rho>0`, the infimum in (3.2) is attained uniquely and

`boxed:`
`Psi(rho)=4+eta+2 log(rho/sqrt(2)),                 rho>=sqrt(2),` (3.5)

while for `0<rho<=sqrt(2)`, let `w=w(rho)>=1` be the unique solution

`rho=e sqrt(2w) e^(-w)`.                                          (3.6)

Equivalently,

`w=-(1/2) W_(-1)(-rho^2/e^2).`                                   (3.7)

Then

`boxed:`
`Psi(rho)=4 e^(-(w-1)/2) sqrt(w)`
`         +sqrt(2 pi e) erfc(sqrt(w/2)).`                          (3.8)

At `rho=sqrt(2)`, the two branches agree and equal `4+eta`.

### Proof

For `q>=1/2`, (2.5) gives

`F(q)=rho q^(-1/2)+log(2q)+2+eta`.

Hence

`F'(q)=q^(-3/2)(sqrt(q)-rho/2).`                                  (3.9)

The critical point is `q=(rho/2)^2`, and it lies in this branch exactly when `rho>=sqrt(2)`. Substitution gives (3.5).

For `0<q<=1/2`, set

`q=(1/2)e^(-y)`, `y>=0`, `w=1+y`.                                 (3.10)

Define

`I(y)=int_0^infinity e^(-v/2)sqrt(1+y+v) dv`.                     (3.11)

Then `J=e^(-y/2)I`. Integration by parts gives

`I(y)=2sqrt(1+y)+K(y)`,                                           (3.12)

where

`K(y)=int_0^infinity e^(-v/2)/sqrt(1+y+v) dv`.                    (3.13)

Differentiating `J=e^(-y/2)I` and using (3.12) yields the exact cancellation

`dJ/dy=-e^(-y/2)sqrt(1+y).`                                      (3.14)

Therefore

`d/dy [rho sqrt(2)e^(y/2)+J]`
` =(rho/sqrt(2))e^(y/2)-e^(-y/2)sqrt(1+y).`                       (3.15)

The critical equation is

`rho=sqrt(2)e^(-y)sqrt(1+y)`,                                    (3.16)

which is strictly decreasing from `sqrt(2)` to zero, so the critical point is unique for `0<rho<=sqrt(2)`. Squaring (3.16), putting `w=1+y`, and rearranging gives

`-rho^2/e^2=(-2w)e^(-2w)`,                                       (3.17)

hence (3.7) on the lower real Lambert branch.

At the critical point, the first term is

`rho sqrt(2)e^(y/2)=2e^(-y/2)sqrt(1+y).`                          (3.18)

Also a change of variables in (3.13) gives

`K(y)=e^((1+y)/2)sqrt(2pi) erfc(sqrt((1+y)/2)).`                  (3.19)

Combining (3.12), (3.18), and `J=e^(-y/2)I` proves (3.8). The derivative signs at the branch boundary and the divergence as `q downarrow0` or `q to infinity` prove global minimality. QED.

This is an exact optimization of an already-proved arbitrary-self compiler; it does not alter its hypotheses.

## 4. Useful low-rho envelope

For the low branch, the standard Mills inequality

`erfc(x)<=e^(-x^2)/(x sqrt(pi))`, `x>0`,                           (4.1)

gives

`Psi(rho)<=e^(-(w-1)/2)[4sqrt(w)+2/sqrt(w)].`                     (4.2)

From (3.6),

`e^(-(w-1)/2)=2^(-1/4)rho^(1/2)w^(-1/4).`                        (4.3)

Thus

`Psi(rho)<=2^(-1/4)rho^(1/2)w^(1/4)(4+2/w).`                     (4.4)

This exposes the critical behavior: in the small-`rho` regime the optimized certificate has only a fourth-root logarithmic loss through `w~log(1/rho)`.

## 5. Arbitrary-self Schur-numerator row certificate

Start from an arbitrary real symmetric physical matrix and isolate an invertible indefinite pair `H` of original coordinates:

`A=[[B,C^T],[C,D_0]],`
`S=D_0-CB^(-1)C^T,`
`N_H=det(B) S.`                                                    (5.1)

Let

`D=|det B|`, `kappa=sigma_min(B)>0`.                              (5.2)

Choose any remaining **original coordinate** `i` for which

`R_i:=||(N_H)_(i,K\{i})||_2>0.`                                  (5.3)

There is deliberately **no condition** on `(N_H)_(ii)`.

Write `a=S_(i,K\{i})`. Then

`||a||_2=R_i/D`.                                                   (5.4)

After conditioning only on the already-completed pair and on any outside original coordinates, the residual is exactly

`S_ii X_i^2 + X_i[beta+2a^T V]+R_0(V)`.                           (5.5)

No term is dropped. The bank `V` still consists of independent original coordinates. The sharp product-projection estimate

`||p_(a^T V)||_infinity<=sqrt(2)/||a||_2`                         (5.6)

therefore gives the translated slope cap

`H_i<=1/(sqrt(2)||a||_2)=D/(sqrt(2)R_i).`                         (5.7)

Because `Psi` is increasing in `rho`, Theorem 3.1 immediately yields the following.

### Theorem 5.1 — `QFORM-SCHUR-NUMERATOR-ARBITRARYSELF-ROW-v1`

Under (5.1)-(5.3), define

`rho_i=2^(11/4) D/sqrt(kappa R_i).`                               (5.8)

Then the full ambient law satisfies

`boxed:`
`||p_Q||_infinity <= D^(-1/2) Psi(rho_i).`                        (5.9)

The result is uniform in the Schur self coefficient `S_ii`, including arbitrarily small, zero, and arbitrarily large values. It also allows arbitrary remaining same-bank curvature and affine terms. This removes the exact condition `(N_H)_ii=0` from account01/B04 r34 without a continuity or perturbation argument.

If `rho_i>=sqrt(2)`, (3.5) gives the explicit branch

`boxed:`
`||p_Q||_infinity`
` <=D^(-1/2)[4+eta+2log(2^(9/4)D/sqrt(kappa R_i))].`              (5.10)

If `rho_i<=sqrt(2)`, write

`w_i=-(1/2)W_(-1)(-rho_i^2/e^2)>=1`.                             (5.11)

Then (4.4) gives the determinant-cancelled form

`boxed:`
`||p_Q||_infinity`
` <=2^(9/8)(kappa R_i)^(-1/4) w_i^(1/4)(4+2/w_i)`                 (5.12)

and in particular

`<=6*2^(9/8)(kappa R_i)^(-1/4)w_i^(1/4).`                         (5.13)

This low branch is not a universal target closure by itself: `w_i` may grow if the selected pair degenerates. The full structural problem is to obtain a favorable pair+row scale or trigger another paid endpoint.

Continuity is not claimed in Theorem 5.1; its source compiler supplies essential boundedness in this scope.

## 6. Fully dense, genuinely rotated indefinite stress matrix with nonzero Schur self

The account02/B04 r22 report uses the explicit matrix

`A_*=`
`[[0,4,4,4,4,4],`
` [4,3,2,3,4,5],`
` [4,2,6,6,8,10],`
` [4,3,6,11,12,15],`
` [4,4,8,12,18,20],`
` [4,5,10,15,20,27]].`                                           (6.1)

Its characteristic polynomial is exactly

`(lambda-2)^3(lambda^3-59lambda^2+34lambda+960)`.                 (6.2)

Now perturb only the physical edge `(3,4)` by `+1/10`:

`A_tilde=`
`[[0,4,4,4,4,4],`
` [4,3,2,3,4,5],`
` [4,2,6,61/10,8,10],`
` [4,3,61/10,11,12,15],`
` [4,4,8,12,18,20],`
` [4,5,10,15,20,27]].`                                           (6.3)

Every off-diagonal physical coefficient is nonzero and the matrix is genuinely nonseparable in the independent coordinates. The perturbation has operator norm exactly `1/10`. Since `A_*` has three exact eigenvalues equal to `2`, Weyl puts three eigenvalues of `A_tilde` in `[1.9,2.1]`. Thus `A_tilde` satisfies the exact owner hypothesis rigorously.

Take physical pair `H={1,2}`. Then

`B=[[0,4],[4,3]],`
`D=16,`
`kappa=(sqrt(73)-3)/2.`                                           (6.4)

The exact Schur complement on coordinates `{3,4,5,6}` is

`S=`
`[[5,41/10,5,6],`
` [41/10,8,8,10],`
` [5,8,13,14],`
` [6,10,14,20]].`                                                 (6.5)

Use the last row. Its self coefficient is

`S_66=20 !=0`,                                                     (6.6)

so the preceding r34 exact-zero row theorem does **not** apply. Its Schur-numerator row energy is

`R_6=16 sqrt(6^2+10^2+14^2)=32sqrt(83).`                          (6.7)

Therefore

`rho_6=2^(11/4)*16/sqrt(((sqrt(73)-3)/2)*32sqrt(83))`
`     =3.786266673267286... >sqrt(2).`                            (6.8)

The high branch (5.10) gives

`boxed:`
`||p_(X^T A_tilde X)||_infinity`
` <=1.8202432195622835... .`                                      (6.9)

The source theorem's unoptimized `q=1` choice gives

`1.9476932346662073...`,                                          (6.10)

so exact optimization improves that same input certificate by about `7.0%`.

The perturbation also exits the particular rank-one-plus-diagonal residual hypothesis used by account02/B04 r22 on (6.1). A necessary off-diagonal rank-one identity fails:

`4*(61/10)=122/5 != 24=3*8.`                                     (6.11)

This is only a scope check for that displayed r22 decomposition; it is not a claim that no other partner mechanism can control `A_tilde`.

## 7. Designated account02/B04 theorem applied to an actual inequality

On the unperturbed matrix `A_*`, account02/B04 r22 takes the zero pivot `h=1`, residual rank-one vector

`v=(1,2,3,4,5)`,                                                   (7.1)

and anchor couplings `a_i=4`. Its pair weights are therefore

`c_{ij}=det((4,i),(4,j))^2=16(j-i)^2`.                            (7.2)

Exact enumeration over **ordered disjoint physical pair-pairs** gives

`J_h(I)=158720.`                                                    (7.3)

The completed r22 theorem therefore yields the concrete same-source inequality

`boxed:`
`||p_(X^T A_* X)||_infinity`
` <=3*2^(4/3)*158720^(-1/6)`
` =1.027359969793547... ,`                                        (7.4)

and that partner branch proves `p in C_0(R)`.

For comparison, Theorem 5.1 also applies to `A_*` via the pair `{1,2}` and the last Schur row and gives the same `1.820243...` bound as (6.9). Thus the designated partner theorem is sharper on its structured rank-one-plus-diagonal carrier; the new result's gain is **scope**: it handles arbitrary Schur self curvature and arbitrary residual curvature once one indefinite physical pair and one aggregate Schur row are available.

## 8. What remains

The exact-zero self obstruction from r34 is now removed analytically. The remaining structural debt is

`QFORM-INDEFINITE-PAIR-SCHURROW-SCALE-OR-PAID-EXIT-v1`:

starting only from the three-large-eigenvalue hypothesis, force an invertible indefinite physical pair `H` and a Schur-numerator row `i` for which the scale in (5.9) is universally controlled, **or** route failure to a completed projected-`E_2`, overlap-`J_1`, overlap-`J_2`, principal-curvature, ridge, grouped-hub, square-bank, or low-rank product-preserving endpoint. A collapsing pair determinant/smallest singular value can still make the present certificate grow; no claim of full closure is made.

The newest account03/B04 r55 theorem is compatible with this conclusion: its marginal-free one-hub projected-`E_2` receiver gives a continuous density whenever an inverse-free projected two-volume currency is positive at target scale. The present theorem covers a different pair+row currency and, unlike r34, does not require zero Schur self curvature.

## 9. Checks and scope

Deterministic checks are in `CHECKER.py` and `CHECKS.md` in this immutable run directory. No Monte Carlo result is used. The unrestricted conjecture is **OPEN**; this run supplies a supporting theorem with explicit constants and a target-valid rotated indefinite stress calculation. Independent end-to-end review has not yet been performed.
