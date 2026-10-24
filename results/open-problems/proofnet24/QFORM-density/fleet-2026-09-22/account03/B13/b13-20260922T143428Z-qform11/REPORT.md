# account03/B13 — nested-heavy rank-three dichotomy from local triple curvature and disjoint Pluecker mass

**Run:** `b13-20260922T143428Z-qform11`  
**Programme:** `QFORM-DENSITY-3EIG-20260922`, owner revision `2026-09-22.5`  
**Assignment:** Extremal product laws  
**Classification:** `ESSENTIAL_STEP_APPLIED / PROVED RANK-THREE STRUCTURAL THEOREM / FULL QFORM OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`; repository retrieval is not native receiver-memory ingestion.

The full owner conjecture remains **OPEN / NOT PROVED**. The theorem below is for rank exactly three; arbitrary additional spectrum is not removed.

## 1. Exact target and correction-aware route

The owner target is a dimension-free bound for the density of `X^T A X` for arbitrary independent real coordinates whose marginal densities are at most one, whenever real symmetric `A` has at least three eigenvalues of modulus at least one.

This run does not use law-uniform pointwise quadratic oscillatory decay, post-rotation independence, bounded support diameter, a single cross minor, or a fiberwise trace supremum. All are excluded by the live correction state.

The previous B13 run closed rank-exactly-three frames with any fixed finite number of projective spectral-row directions, but its constant grows with that number. A fresh peer theorem then paid a fixed positive **disjoint Pluecker-mass** channel. The first useful missing implication is therefore to understand the nested-heavy branch in a way that either produces a good physical triple or forces disjoint exterior mass.

## 2. Completed mathematics actually consumed

### 2.1 Account04 extremal-law reduction

The designated `account04/B13` artifact was not present in the fresh repository snapshot, so the asynchronous instruction forbids waiting or fabricating it. I instead applied the completed adjacent account04 structural result:

`yspennstate/math-open-problems@f57b07e7218b4318dd85bfef9ea247c7c647a716`

`proofnet24/QFORM-density/fleet-2026-09-22/account04/B14/20260922T114319Z-b14-qform-extreme-reduction-r1/REPORT.md`.

It proves, with no loss of constant, that for every interval `J` the supremum of

`P(X^T A X in J)`

over arbitrary independent densities `0<=f_i<=1`, `int f_i=1`, is attained in the supremum over product indicators `f_i=1_{E_i}`, `|E_i|=1`; compact finite unions of intervals suffice by total variation. I use this below as an actual inequality: after the geometric matrix estimate is established, it is enough to prove its slab bound on the indicator extreme class, and the account04 theorem lifts it to all admissible one-dimensional laws with exactly the same constant.

### 2.2 Three-original-coordinate affine theorem

Consumed source:

`yspennstate/math-open-problems@289810e1f075755898f573ee5b863ad3fa9af5b8`

`qform/fleet-2026-09-22/account02/B15/20260922T110507Z-account02-B15-qform-pivot-r1/REPORT.md`.

For three independent density-one coordinates and any real symmetric invertible `3 x 3` Hessian `B`, every affine tilt has density at most

`C3/sigma_min(B)`, where `C3=2*pi+3*sqrt(3)`.

### 2.3 Disjoint exterior-mass theorem

Consumed source-pinned peer snapshot:

`yspennstate/math-open-problems@d358b89ba78735cee238c01e83c2c3ca9ec66352`

`proofnet24/QFORM-density/fleet-2026-09-22/account01/B13/20260922T135910Z-account01-B13-qform-r13/REPORT.md`.

For rank exactly three, write `A=R Lambda R^T`, `R^T R=I_3`, and for each physical triple `I` put

`w_I=det(R_I)^2`, `sum_I w_I=1`.

If

`D0=sum_{I cap J=empty} w_I w_J`,

then, under `|lambda_j(Lambda)|>=1`,

`||p_{X^T A X}||_infinity <= 12 D0^(-1/6)` whenever `D0>0`.

This is the partner-style aggregate inequality used in Section 5 below.

## 3. Nested-heavy coordinates

Assume from now on that `A` has exact rank three and write

`A=R Lambda R^T`, `R^T R=I_3`, `sigma_min(Lambda)>=1`.

Let `r_k in R^3` be the physical spectral rows, so

`sum_k r_k r_k^T=I_3`.

Choose a leverage-heavy row `i` and set

`c=||r_i||^2>1/2`, `e1=r_i/sqrt(c)`.

Suppose the residual two-frame contains a second heavy row `j`: with `P1=I-e1 e1^T`, put

`w_j=P1 r_j`, `h=||w_j||^2>1/2`, `e2=w_j/sqrt(h)`.

Let `e3` complete `(e1,e2)` to an orthonormal basis and write

`r_j=rho e1+sqrt(h)e2`.

For `k` distinct from `i,j`, define

`d_k=<r_k,e3>^2`, `d_* = max_{k notin {i,j}} d_k`.

Parseval immediately gives

`sum_{k notin {i,j}} d_k=1`.                                      (3.1)

Also define the covariance left after removing the two heavy physical rows,

`S=sum_{k notin {i,j}} r_k r_k^T=I-r_i r_i^T-r_j r_j^T`.

In the basis `(e1,e2,e3)`,

`S=[[1-c-rho^2, -rho sqrt(h), 0],
    [-rho sqrt(h), 1-h, 0],
    [0,0,1]]`.

Hence

`Delta:=det S=(1-c)(1-h)-rho^2 >=0`.                              (3.2)

The nonnegativity is forced by `S>=0`.

## 4. First theorem: one final transverse atom gives a good physical triple

### Theorem 4.1 — `QFORM-RANK3-NESTED-HEAVY-TRIPLE-v1`

In the setup above,

`||p_{X^T A X}||_infinity <= C3/(c h d_*) <= 4 C3/d_*`.             (4.1)

In particular, if `d_*>=1/2`, then

`||p_{X^T A X}||_infinity < 8 C3 = 91.8347018391...`.              (4.2)

More generally, `d_*>=tau` gives the dimension-free bound `4C3/tau`.

### Proof

Choose `k` attaining `d_*` and form the `3 x 3` matrix `T` whose rows are `r_i,r_j,r_k`. In the orthonormal basis above it is lower triangular in its first two rows, so

`det(T)^2 = c h d_*`.                                               (4.3)

Because `T` is a row submatrix of a matrix with orthonormal columns,

`T^T T <= R^T R=I`, hence `||T||_op<=1`.                           (4.4)

The physical principal Hessian on coordinates `{i,j,k}` is

`B=T Lambda T^T`.

Let the singular values of `Lambda` be `mu1>=mu2>=mu3>=1`. The singular-value ideal inequality and (4.4) give

`s_1(B)<=mu1`, `s_2(B)<=mu2`.                                      (4.5)

On the other hand,

`|det B|=|det Lambda| det(T)^2=mu1 mu2 mu3 c h d_*`.               (4.6)

Therefore

`sigma_min(B)=|det B|/[s_1(B)s_2(B)] >= mu3 c h d_* >= c h d_*`.  (4.7)

Condition on every original coordinate outside `{i,j,k}`. The selected three coordinates remain independent with their original density caps, while the conditioned terms contribute only an affine tilt and scalar constant. The three-variable affine theorem gives conditional density at most `C3/(c h d_*)`; averaging preserves the bound.

Equivalently, on the account04/B14 extremal indicator class this proves the slab inequality

`P(Q in J)<= [C3/(c h d_*)]|J|`,

and the exact extreme-product reduction lifts that same inequality to all admissible marginal densities. QED.

## 5. Second theorem: if the final atom is diffuse, overlap forces disjoint exterior mass unless the two-row complement is singular

Assume `Delta>0`, so `S` is invertible. For each `k notin {i,j}` put

`q_k=r_k^T S^{-1}r_k`.

Since `S-r_k r_k^T` is positive semidefinite,

`0<=q_k<=1`.                                                        (5.1)

Moreover

`sum_k q_k = tr(S^{-1} sum_k r_k r_k^T)=tr(I_3)=3`,                (5.2)

where both sums in this section run over `k notin {i,j}`.

For the triple `I_k={i,j,k}`, (4.3) gives

`w_{I_k}=c h d_k`.                                                  (5.3)

By Cauchy--Binet on the rows excluding `i,j,k`,

`sum_{J: |J|=3, J cap {i,j,k}=empty} w_J`
`=det(S-r_k r_k^T)`
`=Delta(1-q_k)`.                                                    (5.4)

Every ordered pair counted in (5.3)-(5.4) is one of the disjoint pairs defining `D0`. Therefore

`D0 >= c h Delta sum_k d_k(1-q_k)`
`    = c h Delta [1-sum_k d_k q_k]`
`    >= c h Delta (1-3 d_*)`,                                     (5.5)

where the last inequality uses (5.2) and `d_k<=d_*`.

This proves:

### Theorem 5.1 — `QFORM-RANK3-NESTED-HEAVY-DISJOINT-v1`

If `d_*<1/3` and `Delta>0`, then

`D0 >= c h Delta (1-3d_*)>0`,                                     (5.6)

and consequently the completed disjoint-exterior theorem gives

`||p_{X^T A X}||_infinity`
` <= 12 [c h Delta (1-3d_*)]^(-1/6)`.                              (5.7)

No individual cross minor is selected or inverted in (5.7); the whole disjoint channel is paid before the density estimate.

## 6. Quantitative closure region and asymptotic residual

The two theorems combine into a concrete universal branch closure.

If

`d_* >= 1/6`,

then Theorem 4.1 gives

`||p_Q||_infinity <= 24 C3 = 275.5041055173...`.                   (6.1)

If instead

`d_* < 1/6` and `Delta >= 1/16`,

then, because `c h>1/4` and `1-3d_*>1/2`,

`D0>1/128`, and hence

`||p_Q||_infinity < 12*128^(1/6)=26.9390891595...`.                (6.2)

Thus the entire nested-heavy exact-rank-three branch is paid except for the sharper structural chamber

`d_*<1/6` and `Delta<1/16`,                                        (6.3)

if only these two mechanisms are used.

More importantly, the non-uniform parameters identify the only possible way an **unbounded-density sequence** could survive this branch. If a sequence of nested-heavy rank-three examples had `||p_Q||_infinity -> infinity`, then (4.1) forces

`d_* ->0`,                                                         (6.4)

and once (6.4) holds, (5.7) forces

`Delta ->0`.                                                       (6.5)

So the residual is not merely “second heavy.” It is simultaneously:

1. **final-direction diffuse:** every physical coefficient in the third transverse spectral direction vanishes (`d_*->0`), while their squares still sum to one;
2. **two-row nearly saturated:** the covariance left in the `(e1,e2)` plane has determinant `Delta->0`.

This is a substantially thinner rank-three obstruction than before this run.

## 7. Exact model check

A simple Parseval model shows the inequalities are nonvacuous. Take

`c=h=3/5`, `rho=0`,

one residual row of squared weight `2/5` in each of the `e1,e2` directions, and split the entire `e3` variance equally among four rows, each with `d_k=1/4`. Then

`d_*=1/4`, `Delta=4/25`, `c h=9/25`.

The lower bound (5.6) gives

`D0 >= (9/25)(4/25)(1/4)=9/625=0.0144`.

For this axis-banked model the exact disjoint-basis probability is

`D0=[2(3/5)(2/5)]^2 [1-4(1/4)^2]`
`   =(12/25)^2(3/4)=108/625=0.1728`,

which is safely above the theorem's lower bound. The accompanying checker records these exact rational values and the numerical constants in (6.1)-(6.2).

## 8. What is and is not proved

**Proved here:** a new dimension-free closure mechanism for a large part of the rank-three nested-heavy geometry, valid for arbitrary independent one-dimensional densities bounded by one; and a necessary two-parameter degeneration `(d_*,Delta)->(0,0)` for any putative unbounded-density sequence in that branch.

**Not proved:** arbitrary exact-rank-three orientation in the simultaneous final-diffuse/two-row-saturated limit; arbitrary additional spectrum; or the full owner conjecture. Continuity is not claimed from Theorem 4.1 alone. The disjoint-exterior branch inherits the completed peer theorem's bounded continuous density conclusion where its Fourier proof supplies it, but the present global status remains only a supporting rank-three theorem.

The next target-relevant attack should use the normalized diffuse final bank together with the nearly rank-one remaining `(e1,e2)` covariance **before conditioning destroys product provenance**. The natural canonical limit is two genuine heavy physical coordinates plus a high-cardinality diffuse transverse bank and a nearly one-dimensional shared leakage bank. This is materially different from another finite-projective-direction or single-minor selection argument.

**Full QFORM status: OPEN / NOT PROVED.**
