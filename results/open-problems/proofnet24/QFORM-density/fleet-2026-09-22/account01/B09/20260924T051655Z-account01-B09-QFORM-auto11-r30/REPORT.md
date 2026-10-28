SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B09, 2026-09-24T05:16:55Z.
attacking: singular-pair diffuse-star nonprincipal volume by a quantitative disjoint edge-frame gap, with a bilinear-or-diagonal-plus-low-rank dichotomy that retains the residual exactly.

# account01/B09 r30 — disjoint edge-frame gap in the diffuse singular-pair collar

Programme: `QFORM-DENSITY-3EIG-20260922`  
Status: **NEW SUPPORTING THEOREM / ESSENTIAL STEP APPLIED / FULL QFORM OPEN**  
Execution label: `WITHOUT_VERIFIED_BRAIN`.

The unrestricted conjecture remains OPEN / not proved / not disproved. Full-target continuity remains OPEN separately. No random-variable rotation, law-uniform pointwise quadratic-phase decay, moment/support/log-concavity assumption, worst fiber supremum, or deletion of a small random quadratic term is used below.


## 1. Starting point from the preceding B09 singular-pair reduction

Fix a literal physical pair `H={a,b}` and its leaf bank `L=H^c`. In the exact singular-core / rank-one-cross chamber, use an orthonormal basis `(ell,k)` only inside the two-dimensional coefficient algebra:

`B=A[H,H]=tau ell ell^T`,
`A[H,L]=g r^T`,
`u=r/||r||_2`,
`P=I-u u^T`,
`E=P A[L,L] P`,
`s=|k^T g| ||r||_2`.

The preceding B09 run proved the exact grouped-hub mixed-minor identity. For every two leaf pairs `I,J`, define

`v_{ij}=u_j e_i-u_i e_j` for `I={i,j}`.

Then

`det A[{k} union I,{k} union J] = -s^2 v_I^T E v_J`.          (1.1)

Here `{k}` is multilinear coefficient notation in the two-dimensional hub row/column slot only. It is not a new random coordinate and no independence after the `(ell,k)` change is asserted.

The same preceding run isolated the still-unpaid macroscopic singular-pair collar

`Omega_(2,H)>=1/4`, `q:=max_i u_i^2<1/16`, `|tau|<1/8`, `s_3(A)>=1`,

for which necessarily

`s>2`, `||E||_F>7/8`.                                         (1.2)

The missing question was whether the transverse curvature `E` must create genuinely disjoint physical bilinear currency, or whether it can hide entirely in overlapping leaf pairs.

## 2. New theorem: quantitative disjoint edge-frame gap

Let `u` be any unit vector in `R^m`, `P=I-u u^T`, and let `E=PEP` be symmetric. For two-subsets `I={i,j}` use `v_I=u_j e_i-u_i e_j`. The edge vectors form a Parseval frame on `u^perp`:

`sum_I v_I v_I^T=P`.                                          (2.1)

Let

`K_u={P diag(d) P : d in R^m}`                                (2.2)

be the compressed coordinate-diagonal subspace, and define the ordered disjoint mixed currency

`D_u(E)=sum_(I,J: I cap J=empty) |v_I^T E v_J|^2`.             (2.3)

### Theorem `QFORM-DIFFUSESTAR-DISJOINT-EDGEFRAME-GAP-v1`

Put `q=max_i u_i^2`. Then

`boxed:
 D_u(E) >= (1-3q) dist_F(E,K_u)^2.`                            (2.4)

In particular, if `q<1/3`, then `D_u(E)=0` if and only if

`E=P diag(d) P`                                                (2.5)

for some physical-coordinate diagonal matrix `diag(d)`.

A sharper exact identity is available. Let `E_K` be the Frobenius-orthogonal projection of `E` onto `K_u` and put

`F=E-E_K`.

Then `F=PFP`, `diag(F)=0`, `D_u(E)=D_u(F)`, and

`boxed:
 D_u(F)
 =(1-sum_i u_i^4)||F||_F^2
  -2 sum_i u_i^2 ||F e_i||_2^2
  +4 sum_(i<j) u_i^2 u_j^2 F_ij^2.`                            (2.6)

Equation (2.4) follows immediately from (2.6).

### Proof

For `p_i=P e_i`, the compressed-diagonal space is the span of `p_i p_i^T`. Since `F` is orthogonal to this span,

`0=<F,p_i p_i^T>=p_i^T F p_i=F_ii`,                           (2.7)

where `Fu=0` was used in the last equality. A compressed diagonal has zero matrix element between disjoint edge vectors, because for `I cap J=empty`,

`v_I^T P diag(d) P v_J=v_I^T diag(d)v_J=0`.                   (2.8)

Hence `D_u(E)=D_u(F)`.

By the Parseval identity (2.1),

`sum_(I,J)|v_I^T F v_J|^2=||F||_F^2`.                         (2.9)

For a coordinate `i`, define the star-frame operator

`M_i=sum_(I contains i) v_I v_I^T`.

On `u^perp` one has the exact identity

`M_i=u_i^2 P+p_i p_i^T`.                                      (2.10)

Indeed, for `x perp u`,

`sum_(j!=i)(u_j x_i-u_i x_j)^2=x_i^2+u_i^2||x||_2^2`.

Therefore

`sum_(I,J both contain i)|v_I^T F v_J|^2
 =tr(F M_i F M_i)
 =u_i^4||F||_F^2+2u_i^2||F e_i||_2^2`,                        (2.11)

because `p_i^T F p_i=F_ii=0`.

Let `A0` be the sum in (2.9) over `I=J`, and `A1` the sum over distinct pairs sharing exactly one coordinate. Summing (2.11) over `i` counts `A0` twice and `A1` once:

`2A0+A1=(sum_i u_i^4)||F||_F^2+2 sum_i u_i^2||F e_i||_2^2`.   (2.12)

Also, since `diag F=0`,

`A0=4 sum_(i<j) u_i^2u_j^2 F_ij^2`.                           (2.13)

Now `||F||_F^2=A0+A1+D_u(F)`. Combining (2.12)-(2.13) proves (2.6). Finally

`sum_i u_i^4<=q`,
`sum_i u_i^2||F e_i||^2<=q||F||_F^2`,

and the last term in (2.6) is nonnegative, proving (2.4). QED.

## 3. Physical-minor consequence: disjoint leaf curvature enters only Omega_0 and two fixed Omega_1 hubs

For disjoint leaf pairs `I,J`, form the literal physical `2 x 2` determinant matrix

`M_(I,J)[p,q]=det A[{h_p} union I,{h_q} union J]`,

where `(h_1,h_2)=(a,b)`. The orthogonal coefficient change from `(a,b)` to `(ell,k)` conjugates this determinant matrix. Thus its Frobenius norm is invariant, while its `(k,k)` entry is the left side of (1.1). Consequently

`||M_(I,J)||_F^2 >= s^4 |v_I^T E v_J|^2`.                     (3.1)

When `I cap J=empty`, the diagonal entries `p=q` are physical third minors with exactly one shared coordinate `h_p`, hence belong to `Omega_(1,h_p)`, while the off-diagonal entries `p!=q` have disjoint row/column triples and belong to `Omega_0`. Summing (3.1) gives the localized source-coordinate inequality

`boxed:
 Omega_0+Omega_(1,a)+Omega_(1,b)
 >= s^4 D_u(E)
 >=(1-3q)s^4 dist_F(E,K_u)^2.`                                (3.2)

This is stronger than the preceding coarse `Omega_0+Omega_1+Omega_2` transverse-curvature bound: the genuinely disjoint edge-frame component cannot return to `Omega_2` at all, and any one-overlap remainder is localized to the two original hubs already in the singular pair.

## 4. Bilinear-or-diagonal-plus-rank-four compiler in the unpaid singular-pair collar

Let

`rho=dist_F(E,K_u)`.

Under the unpaid conditions (1.2), `1-3q>13/16` and `s^4>16`, so (3.2) yields

`boxed:
 Omega_0+Omega_(1,a)+Omega_(1,b) >13 rho^2.`                   (4.1)

In particular, if

`rho>=1/4`,                                                     (4.2)

then

`boxed:
 Omega_0+Omega_(1,a)+Omega_(1,b)>13/16,`                       (4.3)

and one of the three literal currencies is at least `13/48`.

If the winning currency is `Omega_0`, the completed no-marginal physical-third-volume receiver immediately gives a continuous `C_0` density with

`||p_Q||_infinity
 <=2 C3 (13/48)^(-1/6)
 <26.233`,                                                      (4.4)

where `C3=3*2^(4/3)e^(1/3)`. The identical coefficient multiplies interval length. If instead one of `Omega_(1,a),Omega_(1,b)` is large, the remaining overlap-one debt has now been localized to one of **two fixed original physical hubs**, rather than being spread over `n` possible pivots.

The complementary case has an exact normal form and no random error is discarded.

### Corollary `QFORM-SINGULARPAIR-BILINEAR-OR-DIAGLOWRANK-v1`

If `rho<1/4`, then there exist

- a literal physical-coordinate diagonal matrix `Lambda`,
- a symmetric matrix `R` of rank at most four,
- a symmetric leaf-supported residual `F`,

such that

`boxed: A=Lambda+R+F,  rank(R)<=4,  ||F||_op<=||F||_F=rho<1/4.`  (4.5)

Moreover, under `s_3(A)>=1`,

`boxed: s_3(Lambda+R)>3/4.`                                    (4.6)

### Proof

Choose `d` so that the orthogonal projection `E_K=P diag(d)P`, and put `F=E-E_K`. Since

`P(A[L,L]-diag(d)-F)P=0`,                                     (4.7)

any symmetric matrix in (4.7) has the form

`u c^T+c u^T`                                                   (4.8)

for some leaf vector `c`. Thus, after subtracting the literal leaf diagonal `diag(d)` and the retained residual `F`, every remaining leaf non-diagonal direction lies in `span{u,c}`. The singular pair core and the rank-one pair-to-leaf cross have range inside

`H direct_sum span{u,c}`,                                      (4.9)

which has dimension at most four. This proves (4.5). Weyl singular-value stability gives (4.6) without treating `F` as a probabilistically negligible quadratic perturbation. QED.

At `rho=0`, the leaf block has the exact form

`A[L,L]=diag(d)+u c^T+c u^T`.                                  (4.10)

Thus the remaining nonseparable leaf term is exactly a product of two linear forms, one being the star direction `u^T X_L`. This is the same structural obstruction as the current `(SP)` hub-that-sees-`P` continuation at `c4c23...`; that continuation explicitly leaves the corresponding adapted-hub maximal functional OPEN, so it is not silently assumed here.

The new reduction therefore identifies a sharp quantitative fork inside the previously opaque singular-pair/large-curvature collar:

1. a genuine disjoint bilinear component forces macroscopic `Omega_0` or a one-overlap packet localized to one of the two existing physical hubs;
2. otherwise the matrix is within operator norm `<1/4` of a diagonal-plus-rank-four matrix with three singular values `>3/4`, with the residual retained explicitly.

## 5. Designated account02/B09 result applied to an actual target inequality

Latest completed designated partner result available at the start of this run:

`QFORM-ROUGH-STAR-UNIFORM-SQRT-SMALLBALL-v1` and its pair-log splice,
`yspennstate/math-open-problems@9ccee3f9a64a934c026786b63baca551ef0ba743`,
`proofnet24/QFORM-density/fleet-2026-09-22/account02/B09/20260924T042556Z-account02-B09-QFORM-auto11-r17/REPORT.md`.

For an invertible indefinite literal physical pair `B`, with

`D_B=|det B|`, `kappa=sigma_min(B)`,

and Schur remainder

`R=sX^2+2X<m,Z>+bX+G(Z)+c`, `m!=0`,

the partner proves, uniformly in the scalar curvature `s` and arbitrary same-bank phase `G`,

`||p_Q||_infinity
 <= C_RS [D_B kappa ||m||_2]^(-1/4)`,                          (5.1)

`C_RS=4 sqrt(2)e^(1/4)Gamma(1/4)^(1/2)=13.8305403219...`,

with the same coefficient times interval length. Continuity is not claimed by that pair-log splice.

Apply it to independent cap-one inputs in

`Q_*=4UV+3X^2+2X Z_1+Z_2^2`.                                  (5.2)

The literal pair `(U,V)` has

`B=[[0,2],[2,0]]`, `D_B=4`, `kappa=2`,                         (5.3)

while the Schur remainder has `m=e_1`, `||m||=1`, scalar curvature `s=3`, and arbitrary-phase slot `G(Z)=Z_2^2`. Hence

`boxed:
 ||p_(Q_*)||_infinity
 <= C_RS 8^(-1/4)
 =8.2236884776... <8.224,`                                    (5.4)

and

`boxed: P{Q_* in I}<8.224 |I|.`                               (5.5)

The coefficient matrix has spectrum

`{-2,(3-sqrt(13))/2,1,2,(3+sqrt(13))/2}`,                     (5.6)

so it satisfies the owner's three-large-eigenvalue hypothesis. This is an actual target inequality and keeps the nonzero scalar curvature and same-bank square exactly.

## 6. Deterministic verification

Two independent regressions were run only as checks, not as proof premises.

- For flat `u` in dimension 17 (`q=1/17`) and a random symmetric `F=PFP` with `diag F=0`, the ordered disjoint edge currency divided by `||F||_F^2` was `0.830449826989622`, exceeding the theorem lower bound `1-3q=0.823529411764706`. Parseval held to floating error.
- On a random ten-leaf exact singular-pair instance, the grouped determinant identity (1.1) agreed with direct physical determinants to `4.44e-16`; the quantity `s^4 D_u(E)` was `52.5964484946`, while the corresponding physical `Omega_0+Omega_(1,a)+Omega_(1,b)` subset was `88.0484527075`, confirming (3.2) numerically.
- The partner example (5.2) has eigenvalues `-2,-0.3027756377,1,2,3.3027756377` and bound `8.2236884776`.

## 7. Remaining implication

The sharpened B09 frontier is

`QFORM-SINGULARPAIR-FIXEDHUB-OMEGA1-OR-DIAGLOWRANK-SP-v1`:

> In the diffuse exact singular-pair collar, use (4.1) to pay a macroscopic one-overlap packet localized to one of the two literal pair hubs without dividing by its possibly vanishing scalar pivot; on the complementary `rho<1/4` branch, splice the retained diagonal-plus-rank-four normal form (4.5) into the existing low-rank/separable or adapted-hub machinery without deleting `F`.

The exact zero-distance face is now identified with the currently open `(SP)`-type product-of-linear-forms obstruction rather than an unstructured arbitrary leaf-curvature problem. Full QFORM remains OPEN.
