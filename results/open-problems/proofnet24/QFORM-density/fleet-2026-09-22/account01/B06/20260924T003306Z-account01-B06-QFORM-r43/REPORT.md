SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B06, 2026-09-24T00:33:06Z.
attacking: the near-collinear twisted-flat survivor — derive a quantitative weighted stability theorem for the additive off-diagonal normal form, then exploit the exact flat core by an indefinite physical-pair Schur collapse and product-weighted curved receivers.

# account01/B06 r43 — weighted twist stability and exact flat-core Schur collapse

Programme: `QFORM-DENSITY-3EIG-20260922`  
Run: `20260924T003306Z-account01-B06-QFORM-r43`  
Role: curved fiber integration / analytic derivation and exact structural identities  
Status: **NEW SUPPORTING STRUCTURAL THEOREMS + NEW PRODUCT-WEIGHTED DENSITY ENDPOINT / DESIGNATED PARTNER APPLIED / FULL TARGET OPEN**  
Execution: `WITHOUT_VERIFIED_BRAIN`.

The unrestricted QFORM conjecture remains OPEN. This report advances the exact collinear-flat survivor from r42 in two ways.

1. It proves a quantitative dimension-free stability identity: in the diffuse-star regime, aggregate twisted-wedge energy controls Frobenius distance to `diagonal + rank <=2`. The proof averages the complete four-index packet before any minor selection or reciprocal payment.
2. Inside the exact flat core `C=D+a v^T+v a^T`, eliminating one literal indefinite physical pair kills the vector `v` exactly and leaves `diagonal + rank one`. This gives several curved-fiber receivers. In particular the formerly awkward endpoint `a_j=0` is paid by a square peel plus the designated account02/B06 product-projection theorem, with an explicit density bound.

No Gaussianity, log-concavity, moment, compact-support, connected-support, iid, diagonal-basis, or post-rotation independence is introduced. Coefficient-basis rotations below are deterministic algebra only. Every probabilistic conditioning uses disjoint groups of original independent coordinates.

## 1. Fresh source boundary and premises

Fresh `math-research-brain/main` was reread before publication. OWNER CONTROL remains revision `2026-09-22.15`, QFORM-only, with no account01/B06 pause/stop. `CURRENT_RESEARCH.md` and `CLAIMS.json` still mark the full theorem and global continuity as OPEN. The live correction inbox was refreshed. In particular this report does not use law-uniform pointwise quadratic-phase decay, arbitrary-joint 3D coarea, positive moments of worst conditional projection caps, post-rotation independence, unrestricted fiber suprema, single-minor inversion from aggregate mass, or any abstract `H_(1/2) -> L^infinity` upgrade.

The current UTC hour already contained this slot's canonical login from r42, so it was not overwritten; the protocol explicitly requires noting the existing same-hour login rather than fabricating a second one. A unique r43 start record was created separately.

### Designated partner result actually applied

The account02/B06 theorem used below is `QFORM-WEIGHTED-AFFINE-FIBER-BL-v1`, source-pinned in its B06 line and used in prior B06 work. In the one-dimensional form needed here:

> If `Z=(Z_k)` is a bank of independent real variables with densities at most one and `u` is a unit vector, then the scalar projection `u dot Z` has density at most `sqrt(e)`.

Thus for any nonzero coefficient vector `a`,

`||p_(a dot Z)||_infinity <= sqrt(e)/||a||_2`.                     (1.1)

This partner statement is applied at equation (6.7), not merely cited.

A newer account02/B06 supporting theorem, `QFORM-E2-HALFRIESZ-ROW-GATE-FREE-v1`, is also retained as context: for a literal physical cross block `M`, `H_(1/2) <= 8 e^(1/4) e_2(M^T M)^(-1/8)`. Its own handoff correctly warns that finite half-Riesz credit alone does not imply bounded density. The present run therefore does not use such an upgrade.

The fractional-potential and square-peel lemmas used below are from the checked Fourier-route report `yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`, `proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/FOURIER_ROUTE_REPORT.md`. In particular:

`D(a(X+shift)^2+S) <= |a|^(-1/2) H_(1/2)(S)`,                     (1.2)

and, for every physical cap-one scalar pivot `gamma != 0`,

`H_(1/4)(gamma(X+shift)^2+R) <= 4 |gamma|^(-1/4)`                (1.3)

with arbitrary remainder `R` measurable in the other original coordinates.

Own r41 proved the literal rank-one crossing quarter-Riesz receiver: if `X` is one original cap-one scalar, `Z` a disjoint product bank and

`S=F(X)+2 X(r dot Z)+G(Z)`,

then

`H_(1/4)(S) <= 3.60302972 ||r||_2^(-1/4)`.                       (1.4)

## 2. Exact collinear-star setting inherited from r42

Consider the zero-anchor two-star coefficient matrix

`A = [[0,0,a^T],
      [0,0,b^T],
      [a,b,C]]`.                                                   (2.1)

The first two variables `X,Y` and all background variables `Z_i` are literal original independent coordinates. In the exactly collinear chamber write

`b=lambda a`.                                                      (2.2)

The r42 twisted quantity for four distinct active background indices is

`T_(ij;kl)
 =a_k(b_i C_jl-b_j C_il)-a_l(b_i C_jk-b_j C_ik)`.                 (2.3)

When `lambda !=0` and all active `a_i` are nonzero, put

`R_ij=C_ij/(a_i a_j), i!=j`.                                      (2.4)

Then

`T_(ij;kl)
 =lambda a_i a_j a_k a_l
  (R_jl-R_il-R_jk+R_ik)`.                                         (2.5)

r42 proved that exact vanishing of all such twists forces

`C=D+a v^T+v a^T`                                                  (2.6)

on the active bank. We now quantify this statement without paying any individual small minor.

## 3. Weighted Hodge/ANOVA stability for the complete twisted packet

Let the active set be `S`, assume every `a_i !=0`, and write

`A2=||a||_2^2`, `p_i=a_i^2/A2`, `delta=max_i p_i`.                (3.1)

Choose `u=(u_i)` to minimize the weighted off-diagonal least-squares error

`N(u)=sum_(i!=j) p_i p_j (R_ij-u_i-u_j)^2`.                       (3.2)

Let `e_ij=R_ij-u_i-u_j` for `i!=j` and set `e_ii=0`. Denote the minimum simply by

`N=sum_(i!=j) p_i p_j e_ij^2`.                                   (3.3)

### Lemma 3.1 — weighted row cancellation

At a minimizer,

`sum_j p_j e_ij=0` for every `i`.                                 (3.4)

#### Proof

Differentiate (3.2) with respect to `u_i`. Symmetry of `R` gives

`0 = -4 p_i sum_(j!=i) p_j e_ij`.

Since `p_i>0` and `e_ii=0`, this is exactly (3.4). QED.

Let `I,J,K,L` be iid with law `p` and define the four-cycle second difference

`Delta=e_(J,L)-e_(I,L)-e_(J,K)+e_(I,K)`.                          (3.5)

### Lemma 3.2 — exact four-cycle energy

`E Delta^2 = 4N`.                                                  (3.6)

#### Proof

Each of the four square terms has expectation `N`. Every mixed term vanishes by conditioning on a shared index and using (3.4); terms on disjoint pairs factor through `E e_(I,J)=0`, again a consequence of (3.4). QED.

The same-side collisions `I=J` or `K=L` give `Delta=0`. A cross collision such as `I=K` has

`Delta=e_(J,L)-e_(I,L)-e_(J,I)`.

Because `p_i^2<=delta p_i` and `(x+y+z)^2<=3(x^2+y^2+z^2)`,

`E[Delta^2 1_(I=K)] <= 9 delta N`.                                (3.7)

The same estimate holds for `I=L`, `J=K`, `J=L`. The union bound therefore gives the dimension-free estimate

`E[Delta^2 1_(I,J,K,L all distinct)] >= (4-36 delta)N`.           (3.8)

### Theorem 3.3 — `QFORM-COLLINEAR-TWIST-WEIGHTED-STABILITY-v1`

Define the aggregate r42 twisted energy

`S_tw = sum_(i<j) sum_(k<l, {k,l} disjoint {i,j}) T_(ij;kl)^2`.   (3.9)

If `delta<1/9`, then there exist a diagonal matrix `D` and vector `v` such that

`boxed:
 ||C-(D+a v^T+v a^T)||_F^2
 <= S_tw / [lambda^2 ||a||_2^4 (1-9 delta)].`                     (3.10)

In particular, if `delta<=1/18`,

`boxed:
 ||C-(D+a v^T+v a^T)||_F
 <= sqrt(2 S_tw)/( |lambda| ||a||_2^2 ).`                         (3.11)

#### Proof

Set `v_i=a_i u_i` and choose the diagonal entries of `D` so that `D+a v^T+v a^T` matches `C` on the diagonal. The residual `E=C-(D+a v^T+v a^T)` then has

`E_ii=0`, `E_ij=a_i a_j e_ij`,                                   (3.12)

and hence

`||E||_F^2=A2^2 N`.                                               (3.13)

By (2.5), summing over all ordered distinct quadruples gives

`sum_(ordered distinct i,j,k,l) T_(ij;kl)^2
 =lambda^2 A2^4 E[Delta^2 1_distinct].`                           (3.14)

Each term in (3.9) has four orientation copies in the ordered sum (the apparent pair swap is already represented twice in (3.9)), so the left side of (3.14) equals `4 S_tw`. Combining (3.8), (3.13), and (3.14),

`4 S_tw >= lambda^2 A2^4 (4-36delta) N
          =4 lambda^2 A2^2 (1-9delta)||E||_F^2`,                  (3.15)

which proves (3.10)-(3.11). QED.

### Why this is useful

This is the quantitative version of r42's exact flatness theorem in the genuinely diffuse collinear-star chamber. It does not choose one `T_(ij;kl)` and invert it. A small *aggregate* four-index twisted packet implies a dimension-free Frobenius approximation to `diagonal + rank two`. Conversely, a large aggregate packet is precisely the resource r42's three-hub crossing receiver is designed to spend.

This theorem is still exact-collinearity stability: it does not by itself control the error caused by `b-lambda a !=0`. That near-collinear perturbation remains part of the full glue problem.

## 4. Exact pair-Schur collapse inside the flat core

Now assume the exact flat form (2.6), allowing `lambda` to be any real number. Put

`kappa=sqrt(1+lambda^2)`,
`H=(X+lambda Y)/kappa`.                                            (4.1)

`H` is independent of the entire background bank `Z`. Its density satisfies

`M_H:=||p_H||_infinity
 <= kappa/max(1,|lambda|)
 <= sqrt(2)`.                                                       (4.2)

The orthogonal hub combination perpendicular to `H` is null in the form. Thus the nontrivial coefficient matrix on `(H,Z)` is

`A_red = [[0, kappa a^T],
          [kappa a, D+a v^T+v a^T]]`.                              (4.3)

Fix a background coordinate `j` with `a_j !=0`; let `R=S\{j}` and

`c_j=d_j+2a_j v_j`.                                                (4.4)

The literal pair `(H,Z_j)` has block

`B_j=[[0,kappa a_j],[kappa a_j,c_j]]`,
`det B_j=-kappa^2 a_j^2<0`.                                       (4.5)

Its cross rows to the remaining background are

`E_j=[[kappa a_R^T],
      [a_j v_R^T+v_j a_R^T]]`.                                    (4.6)

### Theorem 4.1 — `QFORM-FLATCORE-PAIR-SCHUR-COLLAPSE-v1`

The exact Schur complement after eliminating `(H,Z_j)` is

`boxed:
 Schur_j
 =D_R+(d_j/a_j^2) a_R a_R^T.`                                   (4.7)

In particular every dependence on `v_R` cancels.

For every `k in R`, the extending physical principal triple obeys

`boxed:
 det A_red[{H,j,k}]
 =-kappa^2(a_j^2 d_k+a_k^2 d_j)
 =det(B_j) [d_k+(d_j/a_j^2)a_k^2].`                               (4.8)

#### Proof

For `s=kappa a_j`,

`B_j^(-1)=[[-c_j/s^2,1/s],[1/s,0]]`.                              (4.9)

Direct multiplication gives

`E_j^T B_j^(-1) E_j
 =a_R v_R^T+v_R a_R^T-(d_j/a_j^2)a_R a_R^T`.                     (4.10)

Subtracting (4.10) from the `R x R` block of (4.3) gives (4.7). Equation (4.8) is the determinant identity `det(B_j)` times the corresponding scalar Schur pivot. QED.

This cancellation is the main algebraic payoff of the exact flat normal form: the post-pair remainder is not arbitrary same-bank curvature but `diagonal + rank one`.

## 5. Curved receiver menu when `a_j !=0`

The general indefinite-pair quarter-Riesz kernel proved earlier in B06 applies to two independent scalar inputs with cap one. Here the first pair variable `H` has cap `M_H`, while `Z_j` has cap one. Rescale `H` by `M_H`; the determinant scales by `M_H^(-2)`. Using (4.2), the cap penalty `M_H^(3/4)` cancels the potentially favorable `kappa^(-3/4)` from `|det B_j|^(-3/8)`. Hence the safe product-preserving bound is

`D(Q) <= 2 sqrt(3) |a_j|^(-3/4) H_(1/4)(Schur_j)`.                (5.1)

No independence is asserted after rotating `(X,Y)`; only the scalar law of `H`, independent of `Z`, is used.

### 5.1 A physical Schur diagonal

For `k in R` put

`gamma_jk=d_k+(d_j/a_j^2)a_k^2`.                                  (5.2)

If `gamma_jk !=0`, apply (1.3) to the original scalar `Z_k` inside (4.7):

`H_(1/4)(Schur_j) <=4 |gamma_jk|^(-1/4)`.                         (5.3)

Thus

`boxed:
 D(Q) <=8 sqrt(3)
 |a_j|^(-3/4)|gamma_jk|^(-1/4).`                                  (5.4)

This is exactly the physical-triple determinant currency (4.8), expressed in curved-pair/fractional-potential form.

### 5.2 A rank-one crossing inside the Schur remainder

Take `k in R`, `L=R\{k}`. The literal cross vector from `Z_k` to the bank `Z_L` in (4.7) is

`r=(d_j/a_j^2)a_k a_L`,
`||r||=|d_j| |a_k| ||a_L||/a_j^2`.                               (5.5)

If this vector is nonzero, apply own r41 theorem (1.4) and then (5.1):

`boxed:
 D(Q)
 <=12.481262
 [ |a_j d_j a_k| ||a_L|| ]^(-1/4).`                              (5.6)

This branch spends an aggregate star norm `||a_L||` rather than a single background minor.

### 5.3 Diffuse rank-one Schur direction: fully aggregate receiver

Let `q=||a_R||>0` and suppose

`max_(k in R) a_k^2/q^2 <=1/2`, `d_j !=0`.                        (5.7)

Then (4.7) is `D_R+Lambda u u^T`, with `u=a_R/q` and

`Lambda=(d_j/a_j^2)q^2`.                                         (5.8)

The checked rank-one Fresnel theorem gives

`|phi_(Schur_j)(t)|
 <= min(1, 2 sqrt(pi) |Lambda|^(-1/2)|t|^(-1/2))`.                (5.9)

Applying the quarter-Riesz potential lemma to (5.9),

`H_(1/4)(Schur_j)
 <=16 c_(1/4) sqrt(2) pi^(1/4)
    |d_j|^(-1/4)|a_j|^(1/2)q^(-1/2)`,                            (5.10)

where

`c_(1/4)=2^(3/4) Gamma(3/8)/(2 sqrt(pi) Gamma(1/8))
         =0.1492703610...`.                                       (5.11)

Combining with (5.1):

`boxed:
 D(Q)
 <=32 sqrt(6) c_(1/4) pi^(1/4)
    |a_j|^(-1/4)|d_j|^(-1/4)||a_R||^(-1/2)`                      (5.12)

and the numerical front constant is

`32 sqrt(6)c_(1/4)pi^(1/4)=15.577102...`.                         (5.13)

This is the most assignment-aligned branch: the complete diffuse star is integrated before any physical-coordinate maximum or reciprocal minor is introduced.

## 6. New exact endpoint `a_j=0`: square peel + weighted product projection

The previous pair mechanism needs `a_j !=0`. The flat core also has a clean complementary endpoint.

Fix `j` with

`a_j=0`, `d_j !=0`.                                                (6.1)

Let `R=S\{j}`, set

`Astar=a_R dot Z_R`, `q=||a_R||_2>0`.                             (6.2)

Since `C_(jR)=v_j a_R`, the quadratic form can be completed in the *original* scalar `Z_j` as

`Q=d_j (Z_j+(v_j/d_j)Astar)^2 + S`,                               (6.3)

where

`S=2 kappa H Astar + G(Z_R)`                                      (6.4)

for a measurable quadratic `G` on the remaining original bank. By the physical square peel (1.2),

`D(Q) <= |d_j|^(-1/2) H_(1/2)(S)`.                               (6.5)

For fixed `Z_R`, hence fixed `Astar` and `G`, the density cap (4.2) and the bathtub inequality give

`E_H |2 kappa Astar H+G-t|^(-1/2)
 <=2 sqrt(M_H/kappa) |Astar|^(-1/2)
 <=2 |Astar|^(-1/2)`.                                             (6.6)

Now apply the designated account02/B06 theorem at the actual normalized projection `u=a_R/q`:

`||p_(u dot Z_R)||_infinity <=sqrt(e)`,

hence

`boxed:
 ||p_Astar||_infinity <=sqrt(e)/q.`                               (6.7)

For a scalar probability density bounded by `L`, the bathtub principle gives

`sup_c E|W-c|^(-1/2) <=2 sqrt(2L)`.                               (6.8)

Applying (6.8) to `Astar`, then averaging (6.6), yields

`H_(1/2)(S)
 <=4 sqrt(2) e^(1/4) q^(-1/2)`.                                  (6.9)

Therefore:

### Theorem 6.1 — `QFORM-FLATCORE-ZEROSTAR-DIAGONAL-ENDPOINT-v1`

Under (6.1)-(6.2), the full ambient flat-core form has an essentially bounded density satisfying

`boxed:
 ||p_Q||_infinity
 <=4 sqrt(2)e^(1/4)
    |d_j|^(-1/2)||a_R||_2^(-1/2).`                               (6.10)

The front constant is

`4 sqrt(2)e^(1/4)=7.263544635...`.                                (6.11)

The order of operations is essential: the reciprocal half-power is averaged against the *true product-derived projection law* (6.7) before the outer square is paid. There is no unrestricted fiber supremum.

This theorem proves essential boundedness in its stated branch. It does not claim continuity.

## 7. Consequences and exact remaining gap

The exact collinear/twisted-flat survivor is now substantially more rigid.

* If aggregate twisted energy is not small, r42 supplies the three-hub crossing currency.
* If the star is diffuse (`delta<1/9`) and aggregate twisted energy is small, Theorem 3.3 gives dimension-free Frobenius proximity to `diagonal + rank <=2`.
* At exact flatness, Theorem 4.1 turns every nonzero star coordinate into an indefinite physical pair whose Schur complement is exactly `diagonal + rank one`; (5.4), (5.6), or the aggregate diffuse receiver (5.12) can then fire.
* If a chosen background coordinate has zero star coefficient but nonzero diagonal, Theorem 6.1 fires directly, with the partner projection theorem used before the outer square.

There is also a qualitative exact-flat completeness observation. For `a_j !=0`, if the Schur matrix (4.7) is nonzero then either one physical diagonal `gamma_jk` is nonzero, or some off-diagonal rank-one crossing is nonzero; hence one of (5.4) or (5.6) gives a finite density bound. If (4.7) vanishes identically, the whole reduced matrix has rank at most two because the eliminated pair has rank two. Therefore an exact-flat target with a genuine third nonzero spectral direction cannot have every local receiver identically zero. This is **not** a universal quantitative bound: the usable local currency may still be arbitrarily small.

The first unpaid implication is now

`QFORM-NEARCOLLINEAR-STABILITY-TO-UNIFORM-FLATCORE-RECEIVER-v1`:

> Combine the near-collinearity error `b-lambda a` with Theorem 3.3 and the three-large-eigenvalue hypothesis to force, at universal scale, one of: a three-hub twisted volume; the aggregate diffuse Schur currency in (5.12); the zero-star diagonal endpoint (6.10); or another already checked grouped/ridge receiver. The bridge must not delete a coefficient-small quadratic perturbation on unbounded inputs and must not infer a large individual minor from aggregate mass.

The current report does not prove that quantitative spectral bridge. Sparse active support, highly concentrated star leverage `delta>=1/9`, and the general non-collinear chamber must be routed separately. Thus the full arbitrary-dimensional QFORM conjecture remains OPEN and no target counterexample is produced.

## 8. Exact/numerical checks

A deterministic checker accompanies this report. It verifies:

1. the weighted least-squares normal equations and exact identity `E Delta^2=4N` on random symmetric data;
2. the lower bound (3.8) in diffuse random instances;
3. the Schur identity (4.7) by direct matrix inversion on random inputs;
4. the triple determinant identity (4.8);
5. the numerical constants in (5.13) and (6.11).

The checks are diagnostics for the displayed identities, not evidence for the full conjecture.

## 9. Continuity status

Global continuity remains OPEN. r42's nonzero rank-three crossing branch has a continuous `C_0` density. The new r43 results (5.4), (5.6), (5.12), and (6.10) are recorded only as essential `L^infinity` bounds; no continuity upgrade is claimed here.
