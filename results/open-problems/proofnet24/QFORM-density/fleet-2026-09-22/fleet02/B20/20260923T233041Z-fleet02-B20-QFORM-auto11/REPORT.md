SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet02, slot B20, 2026-09-23T23:30:41Z.

# fleet02/B20 — aggregate third-volume closure of the diffuse physical-pair branch

Programme: `QFORM-DENSITY-3EIG-20260922`  
Role: Proof closure and keeper / SYNTHESIS  
Status: **ESSENTIAL STEP APPLIED / DIFFUSE D2 AGGREGATE E3 PAID OR ALIGNED DIAGONAL+RANK8 RETAINED-TAIL STATE / FULL QFORM OPEN**  
Execution: `WITHOUT_VERIFIED_BRAIN`  
Continuity: **OPEN**.

The owner target remains the unrestricted one: independent original real coordinates with densities at most one, arbitrary real symmetric `A` with at least three eigenvalues of modulus at least one, and one universal finite essential-supremum bound for the density of `X^T A X`. No moment, Gaussian, log-concavity, support, diagonal-basis, or post-rotation-independence hypothesis is added. Nonzero coefficient tails are retained throughout.

## 1. Fresh source boundary and corrections


The corrections used below are the current ones: no law-uniform pointwise quadratic-phase decay, no worst-fibre supremum, no arbitrary-joint coarea replacement, no conditional-cap-as-independence, no independence after rotating the source variables, no deletion of a nonzero small matrix tail on unbounded inputs, and no inference of one uniformly good physical minor from aggregate volume without proof.

The required pinned source was read at

`math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`

under `proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/`, including `RESULTS.md`, `FOURIER_ROUTE_REPORT.md`, and `COUNTEREXAMPLE_SEARCH.md`.

Two proved pieces from that source are used at equations below.

1. In the diffuse physical two-volume branch, its `D_2`/fractional-potential estimate gives the already source-complete full-law inequality

`H_(1/2)(Q):=sup_t E|Q-t|^(-1/2)
 <265.625`.                                                         (1.1)

2. Its Theorem H will be applied to a target-valid exact obstruction family in Section 8, giving the actual bound `||p_Q||_infinity<=4` there.

The pinned fifth-volume exit also remains available on every literal physical cut:

`e_5(N^T N)>=1/1024  =>  ||p_Q||_infinity<=10 sqrt(2e)<23.317`.       (1.2)

No counterexample is reported by the pinned search; that observation is not used as proof.

## 2. Newest completed designated partner, used exactly

The newest compatible completed fleet03/B20 result at final partner discovery is r39:

`math-open-problems@5d9892edb6f33beda5ce5e10c4482fcc5fe994a8`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B20/20260923T214857Z-fleet03-B20-QFORM-r39/REPORT.md`.

Its exact finite-core constants are

`kappa=2^-20`, `tau=2^-60`,                                      (2.1)

and, on every unpaid pair/triple branch,

`epsilon_H=(3+122 sqrt(10))2^-20
           =0.0003707865472226546`,                               (2.2)

with the global representation

`A=diag(0_H,A[L,L])+K_6+E_39`,
`rank K_6<=6`,
`||E_39||op<epsilon_H+1/64
             =0.015995786547222654`.                              (2.3)

The physical-triple gate in that same result pays

`102 tau^(-1/3)=106954752`.                                       (2.4)

These expressions are retained literally. Since `sqrt(10)<4`,

`epsilon_H<(3+488)2^-20<512*2^-20=1/2048`,                       (2.5)

so r39 in particular gives

`||E_39||op<33/2048`.                                             (2.6)

The inherited physical provenance that must accompany (2.3) is the original-coordinate partition `H disjoint_union L`, `|H|<=124`, and

`s_1(A[H,L])s_2(A[H,L])>1/480`.                                  (2.7)

As proved in the immediately preceding B20 run, Cauchy--Binet therefore supplies a literal physical row pair `T={t1,t2} subset H` for which, with

`M=A[T,L]`, `G=MM^T`, `S^2=det G`,                               (2.8)

one has

`S>S_0:=1/(480 sqrt(7626))
      =2.3856699607287348e-5`.                                    (2.9)

The rank-six shorthand alone is not used without this source currency.

## 3. Diffuse two-volume notation

This run attacks the diffuse branch of the preceding dichotomy:

`ell_j:=m_j^T G^(-1)m_j<=3/4` for every physical `j in L`,          (3.1)

where `m_j` is column `j` of `M`. Since `G` is positive definite,

`sum_j ell_j=2`.                                                   (3.2)

For each `j`, put `I_j=L\{j}`, let

`P_j=M[:,I_j]^T`,
`c_j=A[I_j,j]`,
`d_j=dist(c_j,col(P_j))`,                                         (3.3)

and define the aggregate third-direction defect

`Z_agg:=sum_(j in L) S^2(1-ell_j)d_j^2`.                          (3.4)

All sets here are sets of literal source coordinates.

### Lemma 3.1 — exact local third-volume identity

For every `j`,

`e_3([P_j,c_j]^T[P_j,c_j])
 =S^2(1-ell_j)d_j^2`.                                             (3.5)

Equivalently, the left side is the third Cauchy--Binet volume of the actual physical cross block

`A[I_j,T union {j}]`.                                             (3.6)

#### Proof

The matrix determinant lemma gives

`det(P_j^T P_j)
 =det(G-m_jm_j^T)
 =S^2(1-m_j^TG^(-1)m_j)
 =S^2(1-ell_j)`.                                                   (3.7)

For any full-column-rank `P`, the Gram determinant of `[P,c]` factors as

`det([P,c]^T[P,c])=det(P^TP) dist(c,col(P))^2`.                    (3.8)

The same identity extends to the rank-deficient endpoint by continuity, with both sides zero. Combining (3.7)-(3.8) gives (3.5). QED.

## 4. New theorem: aggregate local defects force one global physical E3 cut

### Theorem 4.1 — `QFORM-R39-DIFFUSE-AGGREGATE-E3-v1`

There is a literal partition `L=I disjoint_union J` such that, for

`N=A[I,T union J]`,                                               (4.1)

one has

`Z_3(N):=e_3(NN^T)>= (27/256) Z_agg`.                             (4.2)

The constant `27/256` is the optimal value obtainable from the independent one-parameter split used in this proof.

#### Proof

Assign each light coordinate independently to `I` with probability `p` and to `J` with probability `1-p`. Expand `Z_3(N)` by Cauchy--Binet and retain only column triples of the form `T union {j}`, `j in J`.

For fixed `j`, every squared `3x3` minor contributing to (3.5) survives precisely when `j in J` and its three row coordinates all lie in `I`. This has probability

`(1-p)p^3`.                                                       (4.3)

Therefore

`E Z_3(N) >= (1-p)p^3 Z_agg`.                                    (4.4)

The right side is maximized at `p=3/4`, with value `27/256`. Hence at least one deterministic physical split realizes (4.2). No random-source independence is asserted after any rotation; the randomness here is only the probabilistic method applied to coordinate labels. QED.

## 5. The large-defect branch is completely paid

Use the completed marginal-free physical-third-volume theorem

`QFORM-Z3-CROSSING-MARGINAL-FREE-v1`

from fleet02/B03, canonical source

`math-open-problems@df738b7f0821d9af56dfd992cab10ecc6704e3fb`.

For every literal cross cut `N` with `Z_3(N)>0`, arbitrary same-side quadratic blocks, arbitrary affine terms, and arbitrary additional spectrum are retained, and

`||p_Q||_infinity <= C_3 Z_3(N)^(-1/6)`,
`C_3=3*2^(4/3)e^(1/3)=10.5501688311648...`.                       (5.1)

Assume

`Z_agg>=2^-50`.                                                   (5.2)

By Theorem 4.1,

`Z_3(N)>= (27/256)2^-50=27*2^-58`.                               (5.3)

Thus the entire ambient law is paid by

`||p_Q||_infinity
 <=3*2^(4/3)e^(1/3)(27*2^-58)^(-1/6)
 =2048 sqrt(3)e^(1/3)
 =4950.57229398737...<4950.573`.                                  (5.4)

Conditioning the coordinates outside the cut only generates affine terms, and (5.1) is uniform in those terms, so (5.4) is a full-law bound, not a frozen-slice statement.

On the same selected cut, if the stronger pinned condition `e_5(N^TN)>=1/1024` happens to hold, (1.2) improves (5.4) to `<23.317`; otherwise the cut carries the explicit obstruction `e_5(N^TN)<1/1024`. This is the required pinned fifth-volume result applied at its exact physical scope.

## 6. Small aggregate defect forces common-plane rigidity, with an improved constant

Assume from now on

`Z_agg<2^-50`.                                                    (6.1)

Normalize

`V=G^(-1/2)M`,                                                    (6.2)

where `G^(-1/2)` is the symmetric positive square root. Write `v_j` for the columns of `V`. Then

`sum_j v_jv_j^T=I_2`, `||v_j||^2=ell_j<=3/4`.                    (6.3)

For each `j`, choose a least-squares vector `y_j in R^2` for the off-diagonal column `A[L\{j},j]` against the frame rows `v_i`, and put

`r_ij=A_ij-v_i^T y_j`, `i!=j`.                                   (6.4)

Because multiplication of the two frame coordinates by an invertible matrix does not change their column space,

`sum_(i!=j) r_ij^2=d_j^2`.                                       (6.5)

Set

`D^2:=sum_j d_j^2=sum_(j)sum_(i!=j)r_ij^2`.                       (6.6)

### Lemma 6.1 — tight-frame symmetrization

There are a physical diagonal matrix `Delta`, a symmetric `2x2` matrix `K`, and a symmetric zero-diagonal matrix `E` such that

`A[L,L]=Delta+V^T K V+E`,                                        (6.7)

and

`||E||op<=||E||F<=sqrt(22) D`.                                   (6.8)

#### Proof

Let

`B:=sum_i v_i y_i^T`,
`e_ij:=v_i^T y_j-v_j^T y_i`.                                     (6.9)

Symmetry of `A` gives

`e_ij=r_ji-r_ij`.                                                 (6.10)

Since the frame is tight,

`u_j:=y_j-Bv_j=sum_i v_i e_ij`.                                  (6.11)

The synthesis map with columns `v_i` has operator norm one, so

`sum_j ||u_j||^2
 <=sum_(i,j)e_ij^2
 <=4D^2`.                                                         (6.12)

Let `U` have columns `u_j`. From `y_j=Bv_j+u_j` and `VV^T=I_2`,

`B-B^T=-UV^T`.                                                    (6.13)

Hence, with `H=(B-B^T)/2`,

`||H||F<=||U||F/2<=D`.                                           (6.14)

Put `K=(B+B^T)/2`. Then

`q_j:=y_j-Kv_j=u_j+Hv_j`,                                        (6.15)

and therefore

`sum_j||q_j||^2
 <=2sum_j||u_j||^2+2sum_j||Hv_j||^2
 <=8D^2+2||H||F^2
 <=10D^2`.                                                        (6.16)

For `i!=j`, define

`E_ij:=A_ij-v_i^T K v_j
      =r_ij+v_i^Tq_j`.                                            (6.17)

Set the diagonal `Delta` so that `E_jj=0`. Since `A` and `K` are symmetric, `E` is symmetric. Finally,

`||E||F^2
 =sum_(i!=j)E_ij^2
 <=2D^2+2sum_j sum_(i!=j)(v_i^Tq_j)^2
 <=2D^2+2sum_j||q_j||^2
 <=22D^2`.                                                        (6.18)

This proves (6.7)-(6.8). QED.

Because `ell_j<=3/4`, (3.4) gives

`Z_agg>= (S^2/4) D^2`.                                           (6.19)

Combining (2.9), (6.1), (6.8), and (6.19),

`||E||op
 <2 sqrt(22) 2^-25/S_0
 =960 sqrt(22*7626)/2^25
 =0.0117187444120632...`.                                        (6.20)

The near equality is useful: `22*7626=167772<(2048/5)^2=167772.16`, so exactly

`boxed: ||E||op<3/256.`                                          (6.21)

The tail `E` is retained; it is never treated as a uniformly small random quadratic perturbation.

## 7. Two simultaneous low-rank consequences of the small-defect branch

### 7.1 After conditioning the unused finite-core coordinates

Condition the original coordinates in `H\T`. The remaining quadratic matrix on `T union L` is

`A[T union L,T union L]
 =diag(0_T,Delta)+K_4+diag(0_T,E)`,                               (7.1)

where

`K_4=[[A[T,T], M],[M^T,V^TKV]]`.                                 (7.2)

The range of `K_4` is contained in the four-dimensional subspace consisting of the two physical `T` coordinates plus the two-dimensional row space of `V` inside `L`; hence

`rank K_4<=4`.                                                     (7.3)

The error still satisfies `<3/256`. The conditioning changes only affine terms beyond this quadratic block.

Thus the diffuse survivor is not merely a half-potential state: conditionally it is an exact **physical diagonal + rank-at-most-four carrier + retained operator tail below `3/256`**, while still enjoying the full-law half-potential currency (1.1).

### 7.2 Combine with the newest partner r39 globally

Substitute (6.7) into the partner identity (2.3):

`A=diag(0_H,Delta)+K_8+E_*`,                                     (7.4)

where

`K_8:=K_6+diag(0_H,V^TKV)`, `rank K_8<=8`,                       (7.5)

and

`E_*:=E_39+diag(0_H,E)`.                                         (7.6)

Using (2.6) and (6.21),

`||E_*||op<33/2048+24/2048=57/2048<1/32`.                        (7.7)

Since the owner target has `s_3(A)>=1`, Weyl gives the clean retained-core certificate

`boxed:
 s_3(diag(0_H,Delta)+K_8)>31/32.`                                (7.8)

This is the exact expression-level application of the newest designated partner. It does not delete `E_*`; it identifies the coefficient geometry that any next analytic receiver must absorb.

## 8. Target-valid stress family: `Z_agg=0` is real, but is not a counterexample

The new E3 gate cannot be strengthened to say that every target matrix in this diffuse physical-pair state has `Z_agg>0`.

Let `m>=4` and choose two orthonormal flat Walsh rows `V in R^(2xm)`, so

`VV^T=I_2`, `||v_j||^2=2/m<=1/2`.                                (8.1)

Take two original hub coordinates `T` and `m` original light coordinates `L`, and define

`A=[[0,V],[V^T,0]]`.                                              (8.2)

Its nonzero eigenvalues are exactly

`{1,1,-1,-1}`,                                                    (8.3)

so it is fully target-valid. Here `S=1`, all `ell_j=2/m`, `A[L,L]=0`, hence every `d_j=0` and

`Z_agg=0`.                                                        (8.4)

Thus aggregate third-volume cannot be forced purely from the three-large-eigenvalue hypothesis plus diffuse pair area.

This family is nevertheless uniformly paid by the **pinned Theorem H**. Use the literal two physical coordinates `T` as the hub set, the literal light bank as `I`, and `r=0`. The hub-to-light frame Gram matrix is `VV^T=I_2`, and every normalized physical row leverage is `2/m<=1/2`. Theorem H gives

`|phi_Q(t)|<=min(1,4 pi^2 |t|^-2)`.                              (8.5)

Therefore

`||p_Q||infinity
 <=(2pi)^(-1) int_R min(1,4pi^2/t^2)dt
 =4`.                                                             (8.6)

No rotated components are declared independent. The theorem works directly with the original product coordinates. This is a target-valid obstruction to a stronger `Z_agg`-positivity claim and an exact pinned-source payment, not a QFORM counterexample.

## 9. First unpaid implication after this run

The large diffuse-defect branch is now completely paid. Every surviving r39 finite-core state is reduced to the following source-preserving disjunction.

**Concentrated pair-volume branch:** some literal `j in L` has `ell_j>3/4`, so more than `3/4` of the fixed physical pair area is incident to one original coordinate, exactly as in the preceding run.

**Aligned diffuse branch:** all `ell_j<=3/4`,

`Z_agg<2^-50`,                                                    (9.1)

and simultaneously:

- the full ambient law has `H_(1/2)(Q)<265.625`;
- `A[L,L]=Delta+V^TKV+E` with `rank(V^TKV)<=2` and `||E||op<3/256`;
- after conditioning `H\T`, the quadratic matrix is physical diagonal + rank at most four + retained error `<3/256`;
- globally `A=diag(0_H,Delta)+K_8+E_*`, `rank K_8<=8`, `||E_*||op<1/32`, and the retained carrier core has third singular value `>31/32`.

The first source-complete unpaid implication is therefore

`QFORM-R39-COLOOP-OR-ALIGNED-RANK8-RETAINEDTAIL-PAYMENT-v1`:

> Under the full original independent cap-one target hypotheses and the complete r39 finite-core provenance, pay either the physical `>3/4` pair-volume coloop, or the aligned diffuse state (9.1) with the simultaneous half-potential, diagonal+rank-four conditional structure, global diagonal+rank-eight structure, and every nonzero tail retained; or route it source-preservingly to a completed physical pair/triple, three-hub/grouped-square, projected-crossing, ridge, E3, E5, or exact low-rank receiver.

The stress family in Section 8 shows that another attempt to force a positive aggregate E3 defect is the wrong next mechanism. The useful next step is instead an affine-uniform **diagonal-plus-bounded-rank receiver stable under a retained coefficient tail**, or a direct conversion of the physical pair-volume coloop into a two/three-hub receiver. A small operator tail must be spent inside such a receiver, not erased probabilistically.

## 10. Numerical/algebraic regressions

Independent deterministic checks performed in this run:

- 500 random full-rank `2xm` matrices verified the local Gram identity (3.5), maximum normalized error `<6.6e-15`.
- Random constructions of the matrix in (7.2) returned rank at most four throughout.
- The constants evaluate to
  `S0=2.3856699607287348e-5`,
  `C3=10.550168831164775`,
  large-defect payment `2048 sqrt(3)e^(1/3)=4950.57229398737`,
  small-defect L-tail `0.01171874441206322<3/256`,
  and combined r39 tail `0.027714530959285874<1/32`.

These checks support the algebra; the proofs above are exact and do not depend on the numerics.

## 11. Status

- Full unrestricted QFORM: **OPEN / NOT PROVED / NOT DISPROVED**.
- New theorem: `QFORM-R39-DIFFUSE-AGGREGATE-E3-v1`.
- New structural compiler: diffuse branch is either paid by `<4950.573` or is diagonal + rank at most eight modulo a retained operator error `<1/32`, with third singular value of the retained core `>31/32`; a sharper conditional rank-four description also holds.
- Required pinned result: applied at actual equations (1.1), (1.2), and the target-valid Theorem-H payment (8.5)-(8.6).
- Newest designated partner: fleet03/B20 r39 consumed at exact expressions (2.1)-(2.6), and used in (7.4)-(7.8).
- Pointwise-decay, fibre-sup, arbitrary-joint coarea, conditional-cap, post-rotation-independence, and small-random-tail corrections remain enforced.
- Continuity remains separate and OPEN.
- Repository retrieval is authenticated, but no actual learned-memory receiver ingestion was exposed; execution remains `WITHOUT_VERIFIED_BRAIN`.
