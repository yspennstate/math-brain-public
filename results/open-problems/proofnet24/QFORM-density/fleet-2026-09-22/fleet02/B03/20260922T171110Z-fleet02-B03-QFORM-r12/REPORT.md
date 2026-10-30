# Pair-collision cross-block smoothing and the sharp k=2 square-pivot interface

Programme: `QFORM-DENSITY-3EIG-20260922`. Worker: `fleet02/B03`. Run: `20260922T171110Z-fleet02-B03-QFORM-r12`.

**Status:** `PROVED_SUPPORTING_THEOREM + STRUCTURAL_OBSTRUCTION / FULL_TARGET_OPEN / WITHOUT_VERIFIED_BRAIN`.

The full target remains the universal essential-density bound for `X^T A X` when the original coordinates are independent with densities at most one and `A` has at least three eigenvalues of magnitude at least one. This report proves a dependence-safe independent-copy theorem that closes the `one square pivot + two-by-two disjoint cross block` branch with an explicit universal bound. It also gives an exact target family showing that this branch is not forced quantitatively by the bare spectral hypothesis.

## 1. Sources and corrections consumed

Fresh brain controls were read from current `main`; the latest owner control observed before publication was revision `2026-09-22.8`, programme `QFORM-DENSITY-3EIG-20260922`, with no later stop. The assignment is `Decoupled time integral`: use the independent-copy identity for `|phi|^2` while retaining the dependence between each coordinate sum and difference.

The designated partner result actually applied is fleet03/B03, run `20260922T155848Z-fleet03-B03-QFORM-r15`, brain handoff blob `0013af393d82b9ddd034f61e5560018d2be9a530`, canonical mathematics `yspennstate/math-open-problems@57e920edebdcf1da2a046bcf4152dd459925bb8c`. Its theorem says that for

    Q = d (Z+h(W))^2 + R(W),  d != 0,

with `Z` independent of `W` and density cap one, writing `eta(t)=E exp(itR)` and `psi(t)=|eta(t)|^2`, every `1/2 <= alpha < 1` with

    S_alpha = integral_R psi(t)^alpha dt < infinity

implies

    ||p_Q||_infinity <= 2/[sqrt(pi(1-alpha))] |d|^(-1/2) S_alpha^(1/2).   (1.1)

The live correction `QFORM-UV-CONDITIONAL-CAP-FALSE` is enforced throughout: no conditional or marginal independence of `X_i+X_i'` and `X_i-X_i'` is asserted. The live local-cross-rank and one-triple aggregate falsifiers are also retained; no fixed-minor exhaustion claim is made.

## 2. Exact independent-copy pair law

Let `X_i'` be an independent copy of `X_i`, and define

    u_i = X_i-X_i',   v_i = X_i+X_i'.

The pair `(u_i,v_i)` has joint density

    g_i(u,v) = (1/2) f_i((v+u)/2) f_i((v-u)/2).              (2.1)

Thus

    0 <= g_i <= 1/2,       integral g_i = 1,                (2.2)

and, since `f_i <= 1` and `integral f_i=1`,

    ||g_i||_2^2
      = (1/2) (integral f_i(x)^2 dx)^2
      <= 1/2.                                                  (2.3)

The coordinates `i` remain independent as *pairs* `(u_i,v_i)`, but `u_i` and `v_i` inside one pair need not be independent. This is the only product structure used below.

For a real symmetric matrix `S`, vector `b`, and

    R(X) = X^T S X + b^T X + c,

we have the exact collision identity

    |E exp(itR(X))|^2
       = E exp(it[R(X)-R(X')])
       = E exp(it[u^T S v + b^T u]).                          (2.4)

No moment, support, centering, or regularity assumption is used.

## 3. Pair-collision cross-block lemma

Let `I,J` be disjoint original-coordinate sets with `|I|=|J|=k`, and assume the physical cross block

    C = S[I,J]

is invertible. Put `D=|det C|`. Then, for `eta(t)=E exp(itR)`,

    psi(t):=|eta(t)|^2 <= min(1, pi^k D^(-1) |t|^(-k)).       (3.1)

### Proof

Condition on all pair variables `(u_l,v_l)` with `l` outside `I union J`. The terms involving only `I`, only `J`, the linear term, and all couplings to the conditioned outside pairs contribute only unit-modulus factors to the two block amplitudes. The sole `I-J` interaction is

    u_I^T C v_J + u_J^T C^T v_I.

Writing

    z=(u_I,v_I),  w=(u_J,v_J),

this is `z^T M w` with

    M = [[0,C],[C,0]],     |det M| = D^2.                    (3.2)

Let `F_I(z)` and `F_J(w)` denote the corresponding block pair densities multiplied by those unit-modulus phases. From (2.3),

    ||F_I||_2 <= 2^(-k/2),   ||F_J||_2 <= 2^(-k/2).          (3.3)

For the Fourier convention `hat F(xi)=integral exp(i xi dot z)F(z)dz`, Plancherel in dimension `2k` gives

    ||hat F||_2=(2pi)^k ||F||_2.

Integrating first in `z`, applying Cauchy--Schwarz in `w`, and changing variables `xi=tMw` gives

    |integral F_I(z)F_J(w) exp(it z^T M w) dz dw|
      <= (2pi)^k |t|^(-k) |det M|^(-1/2)
             ||F_I||_2 ||F_J||_2
      <= pi^k D^(-1)|t|^(-k).                               (3.4)

The bound is uniform in the conditioned outside pairs, so averaging preserves it. The trivial bound `psi<=1` completes (3.1). QED.

This proof is exactly dependence-safe: it treats every `(u_i,v_i)` jointly and never conditions one member of a conjugate pair on the other.

## 4. Threshold k=3: direct density recovery

For `k>=3`, (3.1) gives

    |eta(t)| <= min(1, pi^(k/2)D^(-1/2)|t|^(-k/2)).          (4.1)

With `t_0=pi D^(-1/k)`, direct integration yields

    integral_R |eta(t)| dt
       <= 2 pi [k/(k-2)] D^(-1/k).                           (4.2)

Hence Fourier inversion gives the supporting theorem

    ||p_R||_infinity <= [k/(k-2)] D^(-1/k),   k>=3.          (4.3)

For `k=3`,

    ||p_R||_infinity <= 3 |det S[I,J]|^(-1/3).               (4.4)

This reproduces the known disjoint three-by-three cross-block constant and is a consistency check on the collision argument, not a novelty claim.

## 5. New threshold k=2: combine with the partner square theorem

The collision estimate is more useful at `k=2` than direct Fourier inversion. Here

    psi(t) <= min(1, K |t|^(-2)),
    K = pi^2 D^(-1).                                         (5.1)

For every `alpha in (1/2,1)`, splitting at `sqrt(K)` gives exactly

    S_alpha = integral psi(t)^alpha dt
       <= [4 alpha/(2alpha-1)] pi D^(-1/2).                  (5.2)

Insert (5.2) into the designated partner inequality (1.1). For

    Q = d(Z+h(W))^2 + R(W),                                  (5.3)

where the physical residual `R` has a disjoint invertible two-by-two cross block `C`,

    ||p_Q||_infinity
      <= 4 sqrt{ alpha/[(1-alpha)(2alpha-1)] }
             |d|^(-1/2) D^(-1/4).                           (5.4)

The scalar factor is minimized at

    alpha = 1/sqrt(2),

where

    alpha/[(1-alpha)(2alpha-1)] = (1+sqrt(2))^2.

Therefore

    ||p_Q||_infinity
       <= 4(1+sqrt(2)) |d|^(-1/2)|det C|^(-1/4).             (5.5)

This is a genuine linear-small-ball estimate obtained from the independent-copy time integral while retaining the exact sum/difference dependence.

## 6. Matrix corollary: one physical pivot plus one cross-2 Schur certificate

Let `A` be any real symmetric matrix, choose an original coordinate `i` with

    d=A_ii != 0,

and condition on no active variables. Completing the square in the physical coordinate `X_i` gives

    X^T A X = d(X_i+h(X_-i))^2 + R(X_-i),                    (6.1)

where the residual quadratic matrix is the exact Schur complement

    S = A_-i,-i - A_-i,i A_i,-i/d.                           (6.2)

All remaining quadratic coefficients stay inside `R`; no spectral summand is deleted. If `S` contains disjoint two-sets `I,J` with invertible `C=S[I,J]`, then (5.5) applies directly:

    ||p_{X^TAX}||_infinity
       <=4(1+sqrt(2)) |A_ii|^(-1/2)|det S[I,J]|^(-1/4).      (6.3)

Equivalently, the block determinant identity

    det A[{i} union I, {i} union J]
       = A_ii det S[I,J]                                     (6.4)

gives the source-coordinate form

    ||p_{X^TAX}||_infinity
       <=4(1+sqrt(2))
          ( |A_ii| |det A[{i} union I,{i} union J]| )^(-1/4). (6.5)

The two row/column triples in (6.5) overlap exactly at the pivot `i`; `I` and `J` themselves are disjoint. There is no leverage hypothesis and no restriction on any additional eigendirections.

## 7. Exact target adversary to an exhaustive pivot+cross2 reduction

The new theorem is not forced with a dimension-free determinant resource by the bare three-large-eigenvalue hypothesis. Consider, for `m>=2`,

    A_m = [1] direct_sum (J_m/m) direct_sum (-J_m/m).         (7.1)

Its nonzero eigenvalues are exactly `{1,1,-1}`. Thus every `A_m` satisfies the full target's spectral hypothesis.

There are two pivot types.

**Singleton pivot.** Taking the first coordinate gives `d=1` and

    S = J_m/m direct_sum (-J_m/m).                            (7.2)

Any invertible disjoint `2 x 2` cross block must use one coordinate from each bank on each side. Its determinant magnitude is exactly

    |det C| = 1/m^2.                                         (7.3)

Thus (6.3) pays the diverging factor `|det C|^(-1/4)=sqrt(m)`.

**Bank pivot.** Pivoting any positive-bank coordinate (`d=1/m`) annihilates the rest of that rank-one positive bank in the Schur complement; the result is

    [1] direct_sum 0_(m-1) direct_sum (-J_m/m),               (7.4)

up to permutation. The negative-bank case is analogous. Every disjoint `2 x 2` cross block of (7.4) has determinant zero, because the singleton has no cross coupling and only one rank-one bank remains.

Hence there is no pivot for which this `k=2` certificate supplies a uniform bound on the family. This is a source-valid obstruction to the proposed exhaustive mechanism

    `three large eigenvalues => one physical pivot + uniformly quantitative disjoint cross2 Schur block`.

It is NOT a counterexample to QFORM: the same family is already controlled by completed grouped-bank aggregation. It says that the full proof must combine the present collision branch with an overlap/grouped-coordinate branch rather than try to force a single local certificate.

## 8. First unpaid implication

A conditional end-to-end proof can now close every matrix admitting either an already-completed diffuse/ridge/bank branch or the certificate (6.3). The first unpaid implication is a genuinely exhaustive **product-preserving structural reduction** from the bare three-large-eigenvalue condition to one of those branches, with the `A_m` family assigned to the bank side rather than a local-minor side.

For this B03 pathway, the next Fourier question is whether the pair-collision argument can be aggregated over many overlapping rank-one cross banks before taking a reciprocal determinant, producing a dimension-free collision functional that remains strong on (7.1). The exact pair law (2.1), rather than false `U/V` conditional independence, is the correct starting object.

## 9. Verification scope

A companion exact checker verifies the optimizing exponent, the mixed-minor/Schur identity on exact rational matrices, and the target family for `m=2,...,8`: singleton-pivot best disjoint cross-2 determinant `1/m^2`, every bank-pivot best determinant zero. These finite checks are regression evidence only; Sections 2--7 contain the all-parameter proofs.
