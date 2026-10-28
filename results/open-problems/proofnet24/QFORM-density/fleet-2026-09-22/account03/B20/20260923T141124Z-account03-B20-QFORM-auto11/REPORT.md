SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B20, 2026-09-23T14:11:24Z.
attacking: close account04/B20's N3(1/192) threshold-transfer debt using the arbitrary-tau no-pivot reduction, then spend its STAR4 rank-two branch by selected physical third-volume smoothing and compile every selected-volume anchor into explicit second-compound products.

# account03/B20 auto11 — tiny-core partner splice and selected-volume anchor expansion

## Status

The unrestricted QFORM conjecture remains **OPEN / NOT PROVED / NOT DISPROVED**.

This run proves two supporting statements.

1. **`QFORM-TINYCORE-R9-STAR4-SELECTEDVOLUME-COMPILER-v1`.** The completed account04/B20 `N3(1/192)` one-window theorem can be inserted into a valid full-target reduction by choosing the already-proved no-pivot scale `tau0=2^-20`. On its remaining STAR4 branch, either a rank-one tube is obtained, or a selected physical third-volume theorem pays the full law with continuous density `<464.029`, or there is a literal selected-third-volume row anchor, or the cross block is quantitatively two-sided aligned and near rank two.

2. **`QFORM-SELECTED3-ANCHOR-EXPANSION-v1`.** A concentrated selected-third-volume row anchor admits an exact original-coordinate determinant expansion. Its incident mass is bounded by two explicit products: a physical hub edge times a second compound of the residual cross block, and a physical cross-row norm times a selected two-volume. Hence every row anchor produced by (1) forces one of two quantitative second-stage resources. This is the first new reduction beyond the already-known selected-volume/aligned-core split.

No rotation of the random variables, post-rotation independence, pointwise quadratic-phase decay, moment bound, log-concavity, support connectedness, compact support, Gaussian assumption on the original inputs, one-good-minor shortcut, or arbitrary-joint coarea estimate is used.

Continuity is proved only on the paid ridge/D5/selected-volume branches described below. The full-target continuity assertion remains open.

Execution status: `WITHOUT_VERIFIED_BRAIN`.

## 1. Source-pinned completed inputs

### 1.1 Full target may be reduced to an arbitrarily small strict no-pivot class

Use `yspennstate/math-open-problems@472b70df7d1edbb3afac23269bc2e4368ae0e371`,
`proofnet24/QFORM-density/interactive/20260922T225732Z-claude-synthesis/GEOMETRIC_SYNTHESIS.md`, Theorem 5.1.

For any fixed `tau in (0,1]`, it proves that a universal density theorem on the strict class

    N3(tau):
      |A_ii| < tau,
      |det A[{i,j},{i,j}]| < tau for every i != j,
      s_3(A) >= 1,

implies the full original QFORM theorem. Its proof pays a scalar pivot or a physical 2x2 pivot in the full ambient matrix and reduces only the remaining strict class. The Gaussian variables appearing in its padding lemma are auxiliary variables inside that reduction; they are not an assumption on the original input laws.

Fix from now on

    tau0 = 2^(-20).

Then proving the theorem on `N3(tau0)` is enough for the full bounded-density target.

### 1.2 Designated partner account04/B20

Use account04/B20 r9, `QFORM-N3-ONEWINDOW-RIDGE-OR-PHYSICALSTAR-v1`, canonical mathematics

`yspennstate/math-open-problems@e9b86c6b32c6209586e9f3bc040017300954c205`,
`proofnet24/QFORM-density/fleet-2026-09-22/account04/B20/20260923T132335Z-account04-B20-QFORM-r9/REPORT.md`.

Its hypotheses are the stricter-looking threshold class `N3(1/192)`. Its conclusion is exhaustive:

- a ridge-diffuse branch gives a continuous density `<239.109`;
- otherwise a physical high-leverage row is found;
- a concentrated star edge yields a physical principal pair with

      |det B| >= 1/61440;

- otherwise there are disjoint original-coordinate leaf banks `J,K` around a physical hub `h` such that, with

      u=A[J,h],  v=A[K,h],  N=A[J,K],  E=||N||_F^2,

  one has

      ||u||^2 > b,       ||v||^2 > b,       b=1/122880,
      E > E0,            E0=36481/147456.

  Its D5 receiver gives continuous density `<199.674` unless

      x1+x2+x3+x4 > (63/64) E,                       (1.1)

  where `x_r=s_r(N)^2` are the squared singular values in decreasing order.

### 1.3 Selected physical three-volume theorem

Use account03/B09 r32, `QFORM-FRACTIONAL-SUBVOLUME-BL-v1`, canonical mathematics

`yspennstate/math-open-problems@56d0211f2f04d74152032fd1914196673eb5c3e6`,
`proofnet24/QFORM-density/fleet-2026-09-22/account03/B09/20260923T124906Z-account03-B09-QFORM-r32/REPORT.md`.

For an actual original-coordinate cross matrix `M`, take any chosen family `Omega` of physical 3x3 minors with total squared determinant mass `Z_Omega>0`. If the normalized selected-minor row inclusion marginals are all at most `1/2`, then the **full** quadratic-plus-affine law, retaining arbitrary same-bank curvature and arbitrary conditioned outside variables, has a continuous density satisfying

    ||p_Q||_infinity <= 3 e Z_Omega^(-1/6).             (1.2)

Only original-coordinate banks are used.

## 2. Closing the partner's threshold-transfer gap

This is an actual equation-level application of the designated account04/B20 theorem.

Every member of `N3(tau0)` satisfies

    |A_ii| < 2^(-20) < 1/192,

and for every physical pair

    |det A[{i,j},{i,j}]| < 2^(-20) < 1/192.             (2.1)

Therefore every `N3(tau0)` matrix lies inside the exact matrix scope of account04/B20 r9. Thus the full-target reduction of Section 1.1 and the partner theorem really compose; no unproved transfer from `N3(1/64)` to `N3(1/192)` is needed.

Consequently every `N3(tau0)` member is already paid on the partner's ridge branch by

    ||p_Q||_infinity < 239.109                           (2.2)

with continuous density, or enters its physical-pair/STAR4 branch.

For completeness, the partner's physical pair is a full-ambient paid branch: the determinant-only pair theorem in the geometric synthesis applies when the pair is indefinite, and the elementary two-variable definite-pair bound applies when it is definite. At `D=1/61440`, the indefinite estimate is below `3197`, while the definite estimate is below `779`. This branch therefore has a universal bounded density. I do **not** promote continuity from this pair payment, because the cited determinant-only theorem records absolute continuity and an `L^infinity` bound but does not supply the full target's continuity statement.

It remains to refine the STAR4 branch satisfying (1.1).

## 3. Rank-one tube versus quantitative rank-two product

Let `x_r=s_r(N)^2`, `E=sum_r x_r`, and retain

    E>E0=36481/147456,
    x1+x2+x3+x4 > (63/64)E.                              (3.1)

### Case 3A: `s2 <= s1/16`

Then `x2,x3,x4 <= x1/256`, hence

    (63/64)E < x1+x2+x3+x4 <= (259/256)x1.

Therefore

    E < (259/252)x1,
    sum_{r>=2} x_r = E-x1 < x1/36.                      (3.2)

Equivalently,

    (sum_{r>=2}s_r(N)^2)^(1/2) < s1(N)/6.               (3.3)

This is a quantitative relative-rank-one tube in literal original-coordinate cross data.

### Case 3B: `s2 > s1/16`

Since the sum of four terms in (3.1) is at most `4x1`,

    x1 > (63/256)E > (63/256)E0.

Hence

    s1 s2 > x1/16 > rho0,
    rho0 := 63 E0 / 4096
            = 255367/67108864
            = 0.0038052648305892944... .               (3.4)

This is the branch where selected third-volume smoothing becomes effective.

## 4. Exact exterior identity for each physical star

Take a singular decomposition

    N = sum_r s_r p_r q_r^T,

where the `p_r` form an orthonormal left singular frame on the physical `J` row space. For the hub star `u=A[J,h]`, define `P2` as projection onto `span{p1,p2}` and

    d_J^2 = ||(I-P2)u||^2.

Let `Gamma_J` be the total squared determinant mass of all physical 3x3 minors of the actual cross matrix `[u,N]` that use the hub column and two leaf columns. Exterior algebra / Cauchy--Binet gives the exact identity

    Gamma_J
      = sum_{a<b} x_a x_b
          ( ||u||^2 - |<u,p_a>|^2 - |<u,p_b>|^2 ).     (4.1)

Indeed, `Gamma_J` is the squared Hilbert--Schmidt norm of `u wedge (wedge^2 N)`; expanding in the orthonormal exterior basis `p_a wedge p_b` gives (4.1).

In particular,

    Gamma_J >= x1 x2 d_J^2 + x2 x3 ||P2 u||^2.          (4.2)

The same formulas hold on the `K` side for `v` using the right singular frame. This identity was also used in the fresh account01/B19 selected-volume work; it is rederived here so the present splice is self-contained.

## 5. A universal selected-volume threshold for the partner STAR4 packet

Set

    b = 1/122880,
    G_perp = rho0^2 b/4
           = 65212304689/2213609288845146193920
           = 2.945971767358352e-11,

    G_3 = b E0^2/4096
        = 1330863361/10943747094510305280
        = 1.2160947703804292e-10.

Since

    G_3/G_perp = 16384/3969 > 1,

put

    G_* := G_perp.                                      (5.1)

There are two ways to force `Gamma_J>G_*`.

First, if

    x3 >= E/64,

then `x2>=x3`, and (4.1) gives

    Gamma_J >= x2 x3 ||u||^2
             > (E/64)^2 b
             > G_3
             > G_*.                                    (5.2)

Second, if

    d_J^2 >= b/4,

then (3.4) and (4.2) give

    Gamma_J >= x1x2 d_J^2
             = (s1s2)^2 d_J^2
             > rho0^2 b/4
             = G_*.                                    (5.3)

Identical statements hold for `Gamma_K` and the right-star transverse mass `d_K^2`.

## 6. Spend a large selected volume, or obtain a literal aggregate row anchor

Suppose `Gamma_J>G_*`. Normalize the selected physical 3x3 minors contributing to `Gamma_J` as in account03/B09 r32.

If every physical row inclusion marginal is at most `1/2`, (1.2) gives the full law a continuous density with

    ||p_Q||_infinity
      <= 3e G_*^(-1/6)
      = 464.028127525... < 464.029.                     (6.1)

If that marginal condition fails, some literal original-coordinate row `i in J` carries more than half of the selected third-volume mass. Thus its incident mass

    Z_i
      := sum_{a<b in J\{i}} sum_{c<d in K}
          det [u,N_c,N_d]_{ {i,a,b} }^2

obeys

    Z_i > Gamma_J/2 > G_*/2                             (6.2)

with

    G_*/2
      = 65212304689/4427218577690292387840
      = 1.472985883679176e-11.                          (6.3)

This is a **physical selected-third-volume anchor**, not a selected single minor. The same conclusion holds on the `K` side.

Therefore, if neither side is paid by (6.1) and neither side produces the anchor (6.2), we must have

    Gamma_J <= G_*,   Gamma_K <= G_*.

By (5.2)--(5.3), this forces simultaneously

    x3 < E/64,
    d_J^2 < b/4,
    d_K^2 < b/4.                                       (6.4)

Since `x4<=x3` and (3.1),

    x1+x2 > (61/64)E,
    sum_{r>=3}x_r < (3/64)E.                            (6.5)

Also

    ||P2 u||^2 > 3b/4 = 1/163840,
    ||Q2 v||^2 > 3b/4 = 1/163840.                      (6.6)

Thus the partner STAR4 remainder is now exhaustively reduced to:

- the relative-rank-one tube (3.3);
- a continuous selected-volume payment `<464.029`;
- a selected-third-volume physical row anchor (6.2); or
- a two-sided aligned near-rank-two core (6.5)--(6.6).

This is a source-valid full-ambient reduction: all same-side curvature and all extra spectrum remain present.

## 7. New anchor-expansion compiler

The selected-volume anchor (6.2) is the first remaining implication attacked further in this run.

Let `i in J` be the anchored physical row. Write `N_-i` for `N` with row `i` removed. For rows `a<b` different from `i` and leaf columns `c<d`, define

    M_{ab;cd} = det [[N_ac,N_ad],[N_bc,N_bd]],
    L_{ab;c}  = det [[u_a,N_ac],[u_b,N_bc]].

Expansion of the anchored 3x3 determinant along physical row `i` gives the exact identity

    D_{iab;cd}
      := det [u,N_c,N_d]_{ {i,a,b} }
       = u_i M_{ab;cd}
         - N_ic L_{ab;d}
         + N_id L_{ab;c}.                               (7.1)

Define two aggregate residual resources

    E2_i := sum_{a<b,c<d} M_{ab;cd}^2
          = e_2(N_-i^T N_-i),                           (7.2)

and

    H2_i := sum_{a<b,c} L_{ab;c}^2.                     (7.3)

`H2_i` is the selected two-volume of the actual physical matrix `[u_-i,N_-i]` formed by the hub column and one leaf column.

Using `(r+s+t)^2 <=3(r^2+s^2+t^2)` in (7.1) and summing,

    Z_i
      <= 3 u_i^2 E2_i
         + 3 sum_{a<b,c<d}
             (N_ic^2 L_{ab;d}^2 + N_id^2 L_{ab;c}^2).

For each fixed `a,b,d`, the coefficient sum over the other leaf column is at most `||N[i,*]||_2^2`. Therefore

    boxed:
    Z_i <= 3( u_i^2 E2_i + ||N[i,*]||_2^2 H2_i ).       (7.4)

This estimate is completely dimension free and uses only physical entries/minors.

Combining (6.2) with (7.4), at least one of the following must hold:

    boxed:
    u_i^2 E2_i > G_*/12,                                (7.5)

or

    boxed:
    ||N[i,*]||_2^2 H2_i > G_*/12,                       (7.6)

where

    G_*/12
      = 65212304689/26563311466141754327040
      = 2.4549764727986265e-12.                         (7.7)

Because we are inside `N3(tau0)`, every physical off-diagonal entry obeys the deterministic consequence of the no-pivot inequalities

    A_ij^2 < tau0 + tau0^2
           = 1048577/1099511627776.                     (7.8)

(Indeed `A_ij^2 = A_ii A_jj - det A[{i,j},{i,j}]` and take absolute values.) Hence the first product branch (7.5) already implies the fixed second-compound lower bound

    boxed:
    E2_i
      > 65212304689/25332772063150080
      > 2.574226954e-6.                                 (7.9)

The second branch (7.6) is a genuine physical cross-row times selected-two-volume resource. No reciprocal single edge or single minor has been selected.

This is the new closure interface:

**`QFORM-N3-SELECTEDANCHOR-SECONDSTAGE-PAYMENT-v1`** — pay either the physical-edge-times-second-compound resource (7.5)/(7.9) or the physical-cross-row-times-selected-two-volume resource (7.6), while retaining arbitrary same-side curvature and arbitrary extra spectrum.

The natural mechanisms are an aggregate rank-two bilinear/fractional-potential receiver for (7.5), and a second selected-family BL or grouped ridge argument for (7.6). Any successful payment must spend the aggregate product before taking reciprocals.

## 8. Regression checks

`CHECK_OUTPUT.txt` in this immutable run folder records exact rational arithmetic for all displayed constants and `100` exact `Fraction` test instances of (7.1) and (7.4). It ends with

    STATUS=QFORM_B20_AUTO11_CHECK_PASS.

These computations are regression evidence only. The proofs above are analytic.

## 9. Scope and remaining debt

What is now proved:

- the partner `N3(1/192)` theorem composes rigorously with a full-target reduction through `tau0=2^-20`;
- its STAR4 rank-two branch is reduced to the four explicit physical outcomes listed at the end of Section 6;
- its selected-third-volume anchor is further reduced to the two explicit second-stage aggregate products (7.5)--(7.6).

What is **not** proved:

- the relative-rank-one tube is not yet paid;
- the two-sided aligned near-rank-two core is not yet paid;
- the second-stage aggregate products (7.5)--(7.6) are not yet paid;
- therefore the strict `N3(tau0)` theorem is still open, hence the unrestricted conjecture is still open;
- full-target continuity is still open.

No full-solution status should be inferred from the reduction.

## 10. Exact source paths consumed

- arbitrary-tau full-target reduction: `yspennstate/math-open-problems@472b70df7d1edbb3afac23269bc2e4368ae0e371`, `proofnet24/QFORM-density/interactive/20260922T225732Z-claude-synthesis/GEOMETRIC_SYNTHESIS.md`;
- designated partner: `yspennstate/math-open-problems@e9b86c6b32c6209586e9f3bc040017300954c205`, `proofnet24/QFORM-density/fleet-2026-09-22/account04/B20/20260923T132335Z-account04-B20-QFORM-r9/REPORT.md`;
- selected-subvolume BL theorem: `yspennstate/math-open-problems@56d0211f2f04d74152032fd1914196673eb5c3e6`, `proofnet24/QFORM-density/fleet-2026-09-22/account03/B09/20260923T124906Z-account03-B09-QFORM-r32/REPORT.md`;
- fresh parallel exterior-volume comparison: `yspennstate/math-open-problems@f63decefb7148fe0640c66d014a49a4ef1f5621e`, `proofnet24/QFORM-density/fleet-2026-09-22/account01/B19/account01-B19-20260923T134858Z-auto11/REPORT.md`.

The last source confirms that the exterior-volume/rank-two split is consistent with the current fleet frontier; the anchor-expansion inequality in Section 7 is the new step of this run.
