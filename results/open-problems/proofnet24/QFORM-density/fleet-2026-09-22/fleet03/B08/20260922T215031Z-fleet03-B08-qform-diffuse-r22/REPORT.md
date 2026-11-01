SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), slot B08, 2026-09-22T21:50:31Z.
attacking: convert the surviving near-rank-two bicolop state from a normalized ridge determinant bank into a dimension-free, two-sided grouped 2x2 determinant core for the ACTUAL physical cross block H, while paying the genuine-third-curvature alternative.

# fleet03/B08 — actual-H grouped determinant core after the near-rank-two reduction

**Run:** `20260922T215031Z-fleet03-B08-qform-diffuse-r22`  
**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Owner control:** revision `2026-09-22.15` at the initial fresh read (later than the prompt's historical `2026-09-22.5`)  
**Assignment:** Diffuse eigenvector case  
**Classification:** `PROVED SUPPORTING STRUCTURAL THEOREM / THIRD-CURVATURE BRANCH PAID / FULL TARGET OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`

## 1. Exact target and correction discipline

The full target remains open: for every finite `n`, every vector of independent real coordinates with probability densities bounded by one, and every real symmetric matrix with at least three eigenvalues of modulus at least one, prove one universal finite essential bound for the density of `X^T A X`, or produce a target-valid counterexample. No moment, Gaussian, log-concave, compact-support, connected-support, or independence-after-spectral-rotation hypothesis is added. Continuity is tracked separately.

This run does not use the refuted law-uniform pointwise quadratic-phase decay, unrestricted fiber suprema, the false arbitrary-joint rank-three coarea bound, the false positive conditional projection-density moment, a fixed-good-minor extraction, or the newly recorded false claim that a singular indefinite Schur-lightcone core by itself has a bounded density. The latter correction is `QFORM-INDEFINITE-SCHUR-LIGHTCONE-CORE-UNBOUNDED-v1`; it says an external third smoother must be retained in that geometry.

## 2. Source-pinned inputs actually consumed

### 2.1 fleet03/B08 r20 near-rank-two state

Canonical source:

`yspennstate/math-open-problems@d5547a484fcc9b62341d80e9ba902cbe2e484284`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B08/20260922T201956Z-fleet03-B08-qform-diffuse-r20/REPORT.md`.

In the only unpaid nonzero-pivot strict-higher-rank branch there are a genuine original-coordinate scalar pivot `a!=0`, an actual original-coordinate cross block `H`, a scale `gamma>0`, singular values

`h_1>=h_2>=h_3>=...>0`,

and top singular vectors `u_1,u_2` on the left and `v_1,v_2` on the right. For physical indices `j,r`, r20 proves

`L_j:=u_1(j)^2+u_2(j)^2 > 6221/6450`,                         (2.1)

`R_r:=v_1(r)^2+v_2(r)^2 > 6221/6450`,                         (2.2)

and

`h_3/h_2 < sqrt(329/1609088) < 3/200`.                        (2.3)

The same run preserves the full original-coordinate product structure and proves that this branch is within `0.010111 gamma` in Hilbert--Schmidt norm of rank two. Its exact-rank-two endpoint is already paid.

### 2.2 fleet02/B08 grouped-bank refinement

Immutable snapshot used:

`yspennstate/math-open-problems@55b475aece02e3bd181935ff66a26b8988100a0c`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B08/B08-20260922T204103Z-1dd824/REPORT.md`.

That report consumes r20 and proves in the strict-higher-rank survivor

`x_1 x_2 > 41413921384333/62139940601856 > 16/25`,             (2.4)

where `x_nu=min(1,h_nu^2/gamma^2)`. Hence

`h_1 h_2 >= gamma^2 sqrt(x_1x_2) > (4/5) gamma^2`.             (2.5)

It also proves the exact-rank-two double-incident grouped `L^3` theorem. I do not silently extend that theorem to higher rank; the whole point of the present run is to isolate what survives before such a stability extension is proved.

### 2.3 newest fleet03/B06 third-curvature dichotomy

Immutable snapshot used:

`yspennstate/math-open-problems@eac866b378f5c54411a55f7eb49f89336a4701ae`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B06/20260922T212328Z-fleet03-B06-qform-r19/REPORT.md`.

For the normalized cross matrix `Z=H(g^2I+H^T H)^(-1/2)`, `g=gamma/16`, this report forms the physical double-incident minor matrix

`M_Z(k,s)=det Z[{j,k},{r,s}]`,

proves `||M_Z||_F^2>1067/2000`, and proves a dichotomy. If `E_2(M_Z)>=1/4096`, genuine third exterior curvature is available and the branch is analytically payable. If `E_2(M_Z)<1/4096`, then `M_Z` lies within relative Frobenius error `<0.041455` of rank one.

### 2.4 compatible completed fleet04 theorem actually applied

The designated `fleet04/B08` current-QFORM handoff/report is still absent at the fresh repository check, so no designated-partner theorem is fabricated. The compatible completed fleet04 theorem actually applied here is fleet04/B18:

`yspennstate/math-open-problems@441e5c1ae4b8aa71ba1bb68aa07d26d83afafcd3`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet04/B18/20260922T113729Z-fleet04-B18-qform-r1/REPORT.md`.

Its proof supplies the dependence-safe physical-square kernel

`p_Q(t) <= |a|^(-1/2) int_0^infinity p_R(t-sgn(a)u) u^(-1/2) du`,       (2.6)

because after completing the genuine original coordinate, the square variable has a conditional density cap one even though it is dependent on the residual value. Section 6 below applies (2.6) to the newest third-curvature branch.

### 2.5 one-dimensional product projection cap

I also use fleet02/B06 `QFORM-WEIGHTED-AFFINE-FIBER-BL-v1`, source snapshot

`yspennstate/math-open-problems@8dd33c1abd4fd64140f59032feda2b13d4351da5`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B06/b06-20260922T155426Z-9fd56fa68a65/REPORT.md`.

Its `k=1` case says that every unit linear projection of independent cap-one coordinates has density at most `sqrt(e)`.

## 3. Exterior-square representation of the ACTUAL cross block

Let `I,J` be the two disjoint original-coordinate banks of `H`. The second exterior power

`W:=wedge^2 H`

is the matrix indexed by physical row pairs and physical column pairs whose entries are the `2 x 2` minors of `H`. With a thin SVD

`H=sum_nu h_nu u_nu v_nu^T`,

we have the exact singular expansion

`W=sum_(alpha<beta) h_alpha h_beta
       (u_alpha wedge u_beta)(v_alpha wedge v_beta)^T`.         (3.1)

The leading term is

`W_12=h_1 h_2 (u_1 wedge u_2)(v_1 wedge v_2)^T`,              (3.2)

and the remainder satisfies

`||W-W_12||_op = h_1 h_3`.                                     (3.3)

Indeed the singular values of `wedge^2 H` are exactly the pairwise products `h_alpha h_beta`; after removing `(1,2)`, the largest remaining product is `h_1h_3`.

Let `P_j` select left exterior coordinates `{j,k}`, `k!=j`, and let `Q_r` select right exterior coordinates `{r,s}`, `s!=r`. Define the ACTUAL physical double-incident minor matrix

`M_H:=P_j W Q_r^T`,

so

`(M_H)_(k,s)=det H[{j,k},{r,s}]`.                               (3.4)

For two orthonormal vectors `u_1,u_2`, the elementary identity

`sum_(k!=j) (u_1(j)u_2(k)-u_2(j)u_1(k))^2
 =u_1(j)^2+u_2(j)^2`                                           (3.5)

shows

`||P_j(u_1 wedge u_2)||_2=sqrt(L_j)`,

and similarly `||Q_r(v_1 wedge v_2)||_2=sqrt(R_r)`. Therefore

`||P_j W_12 Q_r^T||_op=h_1h_2 sqrt(L_j R_r)`.                  (3.6)

Compression cannot increase operator norm, so by (3.3),

`||P_j(W-W_12)Q_r^T||_op <=h_1h_3`.                            (3.7)

## 4. New theorem: a dimension-free actual-H grouped determinant core

### Theorem 4.1 — `QFORM-ACTUAL-BICOLOOP-GROUPED-MINOR-v1`

In the strict-higher-rank fleet03/B08 r20 survivor, the ACTUAL physical double-incident minor matrix satisfies

`boxed( ||M_H||_op > (3/4) gamma^2. )`                         (4.1)

Consequently

`boxed(
 sum_(k!=j)sum_(s!=r)
 det H[{j,k},{r,s}]^2 > (9/16) gamma^4.
)`                                                              (4.2)

Equivalently, there exist unit coefficient vectors

`alpha in R^(I\{j})`, `beta in R^(J\{r})`

such that, after extending them by zero at `j` and `r`,

`boxed(
 |det [[e_j^T H e_r,       e_j^T H beta],
        [alpha^T H e_r,    alpha^T H beta]]|
 > (3/4) gamma^2.
)`                                                              (4.3)

Thus the entire spread-out determinant bank can be compressed BEFORE inversion into a uniformly invertible grouped `2 x 2` core of the actual Schur cross block. No individual physical minor is selected.

#### Proof

By reverse triangle inequality for operator norm and (3.6)-(3.7),

`||M_H||_op
 >= h_1h_2 sqrt(L_jR_r)-h_1h_3`
` = h_1h_2 [sqrt(L_jR_r)-h_3/h_2].`                            (4.4)

Because both `L_j,R_r>6221/6450`,

`sqrt(L_jR_r)>6221/6450`.                                      (4.5)

By (2.3),

`h_3/h_2 <3/200`.                                              (4.6)

By (2.4)-(2.5),

`h_1h_2>(4/5)gamma^2`.                                         (4.7)

Therefore

`||M_H||_op
 >(4/5) gamma^2 (6221/6450-3/200)`
` =(24497/32250) gamma^2`
` >(3/4) gamma^2`,                                             (4.8)

since `24497/32250-3/4=619/64500>0`. This proves (4.1).

Since Frobenius norm dominates operator norm,

`||M_H||_F^2 >9 gamma^4/16`,

which is exactly (4.2) by the definition of `M_H`.

Finally choose unit left/right singular vectors `alpha,beta` realizing `||M_H||_op`. Multilinearity of the determinant gives

`alpha^T M_H beta`
`=sum_(k!=j,s!=r) alpha_k beta_s
  [H_jr H_ks-H_js H_kr]`
`=H_jr (alpha^T H beta)
 -(e_j^T H beta)(alpha^T H e_r)`,                              (4.9)

which is exactly the determinant displayed in (4.3). QED.

### 4.2 The grouped variables remain source-valid product objects

Let `U=X_I`, `V=X_J`. Define

`Y_alpha=sum_(k!=j) alpha_k U_k`,
`Y_beta =sum_(s!=r) beta_s V_s`.                               (4.10)

Because `alpha,beta` are unit vectors and the original coordinates are independent with density caps one, the one-dimensional affine-fiber theorem gives

`||p_(Y_alpha)||_infinity <=sqrt(e)`,
`||p_(Y_beta)||_infinity <=sqrt(e)`.                           (4.11)

Moreover `U_j` is genuinely independent of `Y_alpha`, and `V_r` is genuinely independent of `Y_beta`, because the grouped variables use disjoint ORIGINAL coordinates from their anchors. Hence

`||p_(U_j,Y_alpha)||_infinity <=sqrt(e)`,
`||p_(V_r,Y_beta)||_infinity <=sqrt(e)`.                       (4.12)

The left grouped pair and right grouped pair are also independent across the original cut before any conditioning. Thus (4.3) is not merely a spectral compression: it is backed by two original-coordinate grouped pairs with dimension-free joint density caps.

This statement deliberately stops short of conditioning on complementary grouped fibers. Such a conditioning can destroy density caps and is one of the live corrected interfaces. The remaining analytic transducer must retain those fiber variables inside an integrated product-law argument.

### 4.3 Two-sided physical shear invariance

The matrix `M_H` is invariant under arbitrary row shears

`row_k -> row_k+c_k row_j` for `k!=j`,

and arbitrary column shears

`col_s -> col_s+d_s col_r` for `s!=r`,                                 (4.13)

because every entry of `M_H` is a determinant using the anchor row `j` and anchor column `r`. Thus the currency (4.1)-(4.3) survives subsequent Schur-style eliminations through the same physical anchors. This is useful for a future grouped-core payment theorem.

## 5. Why this is stronger than the preceding normalized determinant bank

The r20/r19 results controlled the normalized matrix

`Z=H(g^2I+H^T H)^(-1/2)`.

A large determinant bank for `Z` does not automatically yield a physical grouped variable for `H`, because the right regularizer mixes physical columns. Theorem 4.1 removes that problem: its determinant is built directly from **the actual physical cross block `H`**, and its grouping coefficients act on original coordinates themselves.

The lower bound is dimension-free and aggregate-before-inversion. In particular, the bank may consist of arbitrarily many individually tiny physical minors; their coherent operator norm still yields the grouped determinant in (4.3).

## 6. Applying completed fleet04 mathematics to the paid third-curvature branch

For completeness, combine the newest B06 branch with fleet04/B18 at an actual inequality rather than only citing it.

If the normalized incident-minor matrix `M_Z` satisfies

`E_2(M_Z)>=1/4096`,                                              (6.1)

fleet03/B06 r19 proves

`E_3(H)>=g^6/4096`, `g=gamma/16`,                              (6.2)

and the unconditional regularized determinant gives an `L^3` residual density with

`||p_R||_3 <=(9e/2)^(2/3) E_3(H)^(-1/9).`                      (6.3)

Starting from the fleet04/B18 kernel (2.6), Holder on `[0,U]` and total mass on `[U,infinity)` give, after optimizing,

`sup_t int_0^infinity p_R(t-u)u^(-1/2)du
 <= C_A ||p_R||_3^(3/4),`

`C_A=8/3^(3/4)`.                                               (6.4)

Therefore

`||p_Q||_infinity
 <= C_A |a|^(-1/2)(9e/2)^(1/2) E_3(H)^(-1/12)`
` <= [192/3^(3/4)] sqrt(e/2)
      /sqrt(|a|gamma)`
` =98.19571365.../sqrt(|a|gamma)`
` <99/sqrt(|a|gamma).`                                        (6.5)

This is an actual application of the completed fleet04 dependence-safe square mechanism. It proves absolute continuity and essential boundedness in Branch (6.1). Continuity is not claimed from this final square step.

## 7. Updated strict-higher-rank B08 proof tree

The nonzero-pivot bicolop survivor is now reduced as follows.

1. **Exact rank two:** paid by fleet02/B08's grouped theorem, with the source-recorded bound `<7.712/sqrt(|a|gamma)`.
2. **Strict higher rank with normalized third curvature `E_2(M_Z)>=1/4096`:** paid by (6.5), `<99/sqrt(|a|gamma)`.
3. **Strict higher rank with `E_2(M_Z)<1/4096`:** B06 r19 forces the normalized incident bank within `4.15%` relative Frobenius distance of rank one, while Theorem 4.1 here simultaneously gives an ACTUAL-H grouped `2 x 2` determinant `>3gamma^2/4` backed by two independent original-coordinate grouped pairs of joint density cap at most `sqrt(e)`.

The first remaining implication is therefore sharply isolated:

> **`QFORM-GROUPED-CORE-WITH-FIBER-TAIL-v1` (OPEN).** Given the two anchored grouped pairs in (4.10)-(4.12), a uniformly invertible actual cross coefficient matrix (4.3), the two-sided Schur-shear invariance, and the small/factorized normalized higher-rank tail from B06 r19, prove an integrated product-law estimate that keeps the complementary fiber variables inside the oscillatory/half-Riesz calculation. Do not condition on those fibers and assert a cap, and do not discard the higher-rank tail by moments.

This is narrower than generic near-rank-two stability: the hard state now contains a concrete dimension-free grouped core in original coordinates.

The separate structural scale `|a|gamma` is still visible in all paid nonzero-pivot branches; this run does not claim the bare three-large-eigenvalue hypothesis has yet provided a universal lower bound for that product. The zero/near-zero outer pivot sibling also remains to be integrated with the completed null-coloop mechanisms.

## 8. Status

**Proved here:**

- `QFORM-ACTUAL-BICOLOOP-GROUPED-MINOR-v1`, equations (4.1)-(4.3).
- A dimension-free actual physical double-incident minor-bank lower bound `>9gamma^4/16` in the strict-higher-rank survivor.
- Source-valid grouped-pair density caps (4.11)-(4.12) without rotating independence away.
- Two-sided anchor-shear invariance of this actual determinant currency.
- Re-application of fleet04/B18 to the genuine-third-curvature branch, yielding (6.5).

**Not proved:** the unrestricted universal QFORM theorem; a universal bound independent of the structural scale `|a|gamma`; continuity in the new square-smoothed branch; or the grouped-core-with-fiber-tail transducer. No counterexample to the full conjecture is claimed.
