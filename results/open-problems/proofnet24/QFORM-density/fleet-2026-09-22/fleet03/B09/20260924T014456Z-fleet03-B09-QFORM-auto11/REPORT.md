SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet03, slot B09, 2026-09-24T01:44:56Z.
attacking: the exact rank-one physical-pair / rank-one-star collar, by Schur-completing one physical hub square and proving that the arbitrary leaf-curvature defect survives as aggregate rank-two cross volume which can be spent at linear interval scale.

# fleet03/B09 — Schur-pivoted curvature defect to aggregate E2 + physical-square receiver

Programme: `QFORM-DENSITY-3EIG-20260922`  
Role: B09 bilinear block mechanism / quantitative inequalities  
Run: `20260924T014456Z-fleet03-B09-QFORM-auto11`  
Status: **NEW SUPPORTING THEOREM / LINEAR SMALL-BALL SUBBRANCH / FULL QFORM OPEN / FULL-TARGET CONTINUITY OPEN**  
Execution: `WITHOUT_VERIFIED_BRAIN`.

## 1. Source boundary


The immediate same-slot predecessor is

`yspennstate/math-open-problems@99841dc027d136e588e06850b969efbd5bce3c32`,
`proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B09/20260924T011706Z-fleet03-B09-QFORM-r43/REPORT.md`.

It proved the rank-one-star local identity, the dimension-free distance to the aligned model `lambda rr^T + diagonal`, and the Bernoulli disjoint-cross compiler. The analytic receiver used here is the row-marginal-free critical two-volume theorem

`yspennstate/math-open-problems@588fa418bc29d4b889fcbbee2b61370234ceef37`,
`proofnet24/QFORM-density/fleet-2026-09-22/fleet01/B03/20260923T175336Z-fleet01-B03-QFORM-r30/REPORT.md`.

For a residual two-bank form with physical source-coordinate cross matrix `C` and `Z2=e2(CC^T)>0`, that theorem proves

`sup_s E|R-s|^(-1/2) <= 8(2e)^(1/4) Z2^(-1/8)`,                 (1.1)

with no row-marginal hypothesis. If one further genuine original coordinate completes as

`Q=a[X+h]^2+R`,                                                   (1.2)

then

`||p_Q||_infinity <= 8(2e)^(1/4)|a|^(-1/2)Z2^(-1/8)`,           (1.3)

and therefore every interval `J` satisfies the identical coefficient times `|J|`. The source proves essential boundedness for this random-center square receiver; it does not separately claim continuity.

## 2. Exact singular-pair / rank-one-star setup

Fix a literal physical pair `H={h,j}` and a disjoint original-coordinate leaf bank `I`. Condition on every original coordinate outside `H union I`; this only creates affine terms, and all bounds below are uniform in the conditioning.

Assume the physical pair core is nonzero rank one:

`B=A[H,H]=[[a,b],[b,c0]]`, `rank B=1`,                          (2.1)

and choose the label `h` so that `a=A_hh !=0`. Thus

`c0=b^2/a`.                                                       (2.2)

Assume the pair-to-leaf block has rank one:

`A[H,I]=g r^T`, `g=(g_h,g_j)^T`, `r!=0`.                         (2.3)

Let

`D=A[I,I]`                                                        (2.4)

be completely arbitrary symmetric. Put

`R2=||r||_2^2`, `q=max_k r_k^2/R2`.                              (2.5)

For each leaf `k`, define the physical rowwise transverse defect

`delta_k = dist(D[k,I\{k}], span(r_{I\{k}}))`.                   (2.6)

Also define the exact aligned-model distance

`d_* = inf_{lambda in R, Lambda diagonal}
       ||D-lambda rr^T-Lambda||_F`.                              (2.7)

The same-slot predecessor proved, for `q<1`,

`d_* <= sqrt(2) (sum_k delta_k^2)^(1/2)`.                        (2.8)

No norm, sign, rank, or support assumption is imposed on `D`.

## 3. First essential implication: physical Schur completion preserves the transverse defect exactly

Complete the square in the genuine original coordinate `X_h`. Writing `x=X_h`, `y=X_j`, `z=X_I` and suppressing arbitrary affine terms for one line,

`Q = a x^2+2bxy+c0 y^2
     +2 g_h x (r^Tz)+2 g_j y(r^Tz)+z^T D z + affine`.            (3.1)

Because `c0=b^2/a`, exact completion gives

`Q = a[x + (b y+g_h r^Tz+affine)/(a)]^2 + R_h(y,z)`,             (3.2)

where the residual quadratic coefficients are

`A_h^Schur[{j},I] = gamma_h r^T`,
`gamma_h := g_j-(b/a)g_h`,                                      (3.3)

and

`D_h := D-(g_h^2/a) rr^T`.                                      (3.4)

The remaining physical hub square is exactly zero:

`A_h^Schur[j,j]=c0-b^2/a=0`.                                    (3.5)

Two exact invariances are immediate.

### Lemma 3.1 — transverse-defect invariance

For every `k`,

`dist(D_h[k,-k], span(r_-k)) = delta_k`,                         (3.6)

and

`inf_{lambda,Lambda diagonal}||D_h-lambda rr^T-Lambda||_F=d_*`. (3.7)

Proof: `(g_h^2/a)r_k r_-k` is itself in `span(r_-k)`, so subtracting it does not change the orthogonal residual in (2.6). Equation (3.7) follows because subtracting a scalar multiple of `rr^T` only translates the optimization variable `lambda`. QED.

### Lemma 3.2 — pair/star Schur invariant

Let

`kappa := g^T adj(B) g`.                                         (3.8)

Then

`boxed: a gamma_h^2 = kappa`.                                    (3.9)

Indeed, using `c0=b^2/a`,

`g^T adj(B)g
 = c0 g_h^2-2b g_hg_j+a g_j^2
 = a(g_j-(b/a)g_h)^2`.                                          (3.10)

Thus `|a| gamma_h^2=|kappa|`. In particular, `gamma_h=0` is precisely the branch in which the leaf star lies in the range direction of the rank-one pair and the kernel-star Schur coupling vanishes.

These identities use coefficient algebra only; no random variables are rotated.

## 4. Compile the preserved defect into one residual original-coordinate two-volume

For the Schur residual `R_h`, define

`Xi_h := gamma_h^2 sum_k (R2-r_k^2) delta_k^2`.                  (4.1)

For a leaf partition `I=S disjoint union T`, consider the literal residual source-coordinate cross matrix

`C_h(S,T)=A_h^Schur[{j} union S,T]`.                             (4.2)

For fixed `k` and two distinct opposite leaves `u,v`,

`det C_h[{j,k},{u,v}]
 = gamma_h (r_u D_h[k,v]-r_v D_h[k,u])`.                         (4.3)

Cauchy-Binet on the two-row matrix formed by `gamma_h r_-k` and `D_h[k,-k]`, together with Lemma 3.1, gives

`sum_{u<v; u,v !=k} det C_h[{j,k},{u,v}]^2
 = gamma_h^2 (R2-r_k^2) delta_k^2`.                              (4.4)

Summing over `k` yields exactly `Xi_h`.

Now color each leaf independently into `S` with probability `1/3`, otherwise into `T`. A summand in (4.4) indexed by three distinct leaves `(k,u,v)` survives in the selected disjoint cross block exactly when `k in S` and `u,v in T`, with probability

`(1/3)(2/3)^2 = 4/27`.                                           (4.5)

Therefore some literal original-coordinate partition satisfies

`boxed:
 Z2_h(S,T):=e2(C_h C_h^T) >= (4/27) Xi_h.
}`                                                                  (4.6)

No individual physical `2x2` minor is selected or inverted.

Using `R2-r_k^2 >=(1-q)R2` and (2.8),

`Xi_h
 >= gamma_h^2(1-q)R2 sum_k delta_k^2
 >= [(1-q)/2] gamma_h^2 R2 d_*^2`.                              (4.7)

Hence for `q<1`, some residual cut obeys

`boxed:
 Z2_h(S,T)
 >= [2(1-q)/27] gamma_h^2 R2 d_*^2.
}`                                                                  (4.8)

This is the required aggregate-before-reciprocal step.

## 5. New payment theorem — `QFORM-RANKONE-PAIR-SCHUR-E2-SQUARE-RECEIVER-v1`

Assume the setup of Sections 2-4 and `Xi_h>0`. Then the law of the full conditional quadratic form has an essentially bounded density and

`boxed:
 ||p_Q||_infinity
 <= 8(2e)^(1/4)(27/4)^(1/8)
    (|a|^4 Xi_h)^(-1/8)
 < 15.510 (|a|^4 Xi_h)^(-1/8).
}`                                                                  (5.1)

Consequently every interval `J` satisfies

`boxed:
 P{Q in J}
 <=15.510 (|a|^4 Xi_h)^(-1/8)|J|.
}`                                                                  (5.2)

### Proof

Equation (3.2) is an exact completion of one genuine original-coordinate square. Conditional on all residual variables, `X_h` still has its original density cap one; the center in (3.2) may depend arbitrarily on those variables. By (4.6), the residual `R_h` has an original-coordinate two-bank cut of total squared two-volume `Z2_h >=(4/27)Xi_h`. Apply the row-marginal-free theorem (1.1) to `R_h`, then its completed-square receiver (1.3):

`||p_Q||_infinity
 <=8(2e)^(1/4)|a|^(-1/2) Z2_h^(-1/8)
 <=8(2e)^(1/4)(27/4)^(1/8)|a|^(-1/2)Xi_h^(-1/8)`.                (5.3)

Since `|a|^(-1/2)=(|a|^4)^(-1/8)`, this is (5.1). Integrating the density over an interval gives (5.2). QED.

This proof never takes a square root of an interval probability. The critical rank-two packet is first converted to a whole-copy half-Riesz bound and then spent by the exact physical square, so the final estimate is genuinely `O(|J|)`.

The source square receiver proves essential boundedness here. This report does **not** promote (5.1) to continuity.

## 6. Dimension-free aligned-model corollary

Combining (4.8) directly with (1.3) gives, for `q<1`,

`boxed:
 ||p_Q||_infinity
 <=8(2e)^(1/4)[27/(2(1-q))]^(1/8)
   (|a|^4 gamma_h^2 R2 d_*^2)^(-1/8).
}`                                                                  (6.1)

By Lemma 3.2,

`|a|^4 gamma_h^2 = |a|^3 |kappa|`,                               (6.2)

so equivalently

`boxed:
 ||p_Q||_infinity
 <=8(2e)^(1/4)[27/(2(1-q))]^(1/8)
   (|a|^3 |kappa| R2 d_*^2)^(-1/8).
}`                                                                  (6.3)

In the source diffuse chamber `q<1/16`, the numerical coefficient is

`8(2e)^(1/4)[27/(2*(15/16))]^(1/8)
 =17.0496872873... <17.050`.                                      (6.4)

Let `tau` be the nonzero eigenvalue of the rank-one pair core `B`. Since `B=tau uu^T`, one of its two physical diagonals satisfies

`|a| >= |tau|/2`.                                                 (6.5)

Choosing that pivot in (6.3), still for `q<1/16`, gives the physical-pair invariant form

`boxed:
 ||p_Q||_infinity
 <22.111 (|tau|^3 |kappa| R2 d_*^2)^(-1/8).
}`                                                                  (6.6)

The exact singular-pair anchored overlap-two currency from fleet01/B09 is

`Omega_(2,H)=kappa^2(R2^2-sum_i r_i^4)`.                         (6.7)

Since `sqrt(Omega_(2,H)) <= |kappa|R2`, (6.6) implies

`||p_Q||_infinity
 <22.111 (|tau|^3 sqrt(Omega_(2,H)) d_*^2)^(-1/8).`              (6.8)

In particular, in the macroscopic collar `Omega_(2,H)>=1/4`,

`boxed:
 ||p_Q||_infinity
 <24.112 |tau|^(-3/8)d_*^(-1/4).
}`                                                                  (6.9)

Thus the genuinely nonaligned-curvature portion of the exact singular-pair collar is paid whenever the pair scale and leaf-model defect are not simultaneously collapsing. The remaining issue is now explicitly a near-stratum problem, not a missing arbitrary-curvature compiler.

## 7. Target-valid diffuse stress family

Take even `m`,

`B=diag(1,0)`, `g=e2`,
`r=(1,...,1)/sqrt(m)`,                                            (7.1)

and let `v` be a flat Walsh vector with entries `+/-1/sqrt(m)` and `v perpendicular r`. Put

`D=t vv^T`.                                                       (7.2)

This is the same source family used to show that the anchored singular-pair overlap-two ledger is blind to arbitrary dense leaf curvature. Its nonzero spectrum is `{1,+1,-1,t}` (with the obvious merging when values coincide), so at `t=1` it satisfies the owner target.

Here the pivot `h` is the first hub: `a=1`, `gamma_h=1`, `R2=1`, and

`Xi_h=t^2(m-2)/m`.                                                (7.3)

Therefore (5.1) gives

`boxed:
 ||p_Q||_infinity
 <=15.5090100709 [t^2(m-2)/m]^(-1/8).
}`                                                                  (7.4)

At `m=64`, `t=1`,

`Xi_h=62/64=0.96875`,
`boxed: ||p_Q||_infinity <=15.5706812238`.                        (7.5)

This is a genuine linear interval bound with arbitrary dense same-leaf curvature retained. It is intentionally not claimed uniform as `t->0`; the exact `t=0` collinear-star endpoint is paid by fleet02/B09 r15, while the robust near-zero interpolation remains open.

## 8. Designated fleet04/B09 theorem applied to an actual inequality

The completed fleet04/B09 theorem is

`yspennstate/math-open-problems@c0d3f34e557a374f41b2639994c43af4f950b682`,
`proofnet24/QFORM-density/fleet-2026-09-22/fleet04/B09/20260923T101659Z-fleet04-B09-dense-self-cross-fourier-r1/REPORT.md`.

For any literal invertible physical `3x3` cross block `K`, retaining arbitrary dense same-side curvature, it proves

`||p_Q||_infinity <=3|det K|^(-1/3)`,                            (8.1)

with a continuous density and the same coefficient times interval length.

Apply it to the six-coordinate target-valid regression from r43:

`B=[[1,1],[1,1]]`, `g=(1,-1)`, `r=(1,1,1,1)`,                   (8.2)

`D=[[0,0,1,0],
    [0,0,0,1],
    [1,0,0,0],
    [0,1,0,0]].`                                                  (8.3)

The full symmetric matrix has eigenvalues

`{-2.372281323269,-1,-1,1,2,3.372281323269}`,                    (8.4)

so it satisfies the owner's spectral target. The literal disjoint physical triple

rows `{h1, leaf1, leaf2}`, columns `{h2, leaf3, leaf4}`

has cross matrix

`K=[[1,1,1],
    [-1,1,0],
    [-1,0,1]]`,                                                   (8.5)

and

`det K=3`.                                                        (8.6)

Therefore the designated partner theorem gives the actual inequality

`boxed:
 ||p_Q||_infinity <=3*3^(-1/3)=3^(2/3)=2.080083823052...,
}`                                                                  (8.7)

and

`P{Q in J}<=3^(2/3)|J|`,                                         (8.8)

with a continuous density. This partner payment is stronger on this finite regression; the new theorem above addresses the complementary diffuse setting where selecting one physical determinant can deteriorate or vanish.

## 9. What is closed and what remains open

This run closes the following scoped implication:

**exact nonzero rank-one physical pair + rank-one pair-to-leaf star + arbitrary leaf curvature + positive Schur-pivoted curvature defect -> one aggregate residual original-coordinate two-volume -> dependence-safe critical half-Riesz estimate -> the original physical square -> `O(|J|)` interval bound.**

The central exact facts are that Schur completion subtracts only an aligned `rr^T` leaf term, so every transverse defect survives unchanged, and that `a gamma_h^2=kappa`.

It does **not** solve the full QFORM conjecture. The remaining B09 debt is now sharpened to

`QFORM-SINGULARPAIR-NEARALIGNED-OR-TINYCORE-INTERPOLATION-v1`:

in the diffuse exact singular-pair collar, handle the regime where `|tau|^3 |kappa| R2 d_*^2` is small while the target spectral resource remains macroscopic. The exact aligned endpoint `d_*=0`, the exact zero-core/collinear-star endpoint, and the nonzero-defect receiver are separately understood; what is missing is a source-preserving robust interpolation/routing that does not delete a small quadratic remainder on unbounded inputs.

Full unrestricted QFORM remains **OPEN**. Full-target continuity remains **OPEN**. The new branch proves essential boundedness and linear interval scaling; continuity is not claimed for it.
