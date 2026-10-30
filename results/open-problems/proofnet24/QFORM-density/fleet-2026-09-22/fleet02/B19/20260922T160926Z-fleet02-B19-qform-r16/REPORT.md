# fleet02/B19 — wedge/star-to-ridge extraction in the surviving two-offdiagonal branch

**Programme:** `QFORM-DENSITY-3EIG-20260922`, owner revision `2026-09-22.5`  
**Run:** `20260922T160926Z-fleet02-B19-qform-r16`  
**Assignment:** Universal proof assembly / SYNTHESIS  
**Outcome:** `ESSENTIAL_STEP_APPLIED / FULL_TARGET_OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`

## 1. Exact target and source discipline

The target remains unrestricted: for arbitrary dimension, independent real coordinates with probability densities bounded by one, and every real symmetric `A` having at least three eigenvalues of modulus at least one, prove one universal finite essential-supremum bound for the density of `Q=X^T A X`, or give a target-valid counterexample. No moments, bounded support, log-concavity, diagonal-basis reduction, or independence after spectral rotation is assumed.

Fresh control was read from `yspennstate/math-research-brain` under owner revision `2026-09-22.5`; the live correction inbox was refreshed through commit `18e019124ff2bb35b24ab14f34fab8373eef1901` before this report was assembled. In particular I do not use a fixed good coordinate triple, a universal rank-three cross cut, a single Schur-rank-two extraction, post-rotation conditional caps, fiber suprema, or law-uniform pointwise Fresnel decay.

Source-pinned dependencies actually applied:

1. **Named partner fleet03/B19 r13**, `yspennstate/math-open-problems@0e6d1715955458010d43193cab3dafc293c0e28c`, proves the exact indefinite-pivot quarter-kernel / Schur-critical-value splice and completes the one-effective branch up to a physical Schur diagonal or a physical Schur cross bank.
2. **fleet01/B19 r11**, `yspennstate/math-open-problems@2e5d5cdc3bb7121673bc920497fb11cac9eceb46`, proves the original-coordinate one-cross-singular square-root-log estimate and closes the same-bank contaminated one-effective branch by supplying the needed negative quarter moment.
3. **fleet02/B04 r11b**, `yspennstate/math-open-problems@b129377880c18fe011dd4513282f2e0b60e412e0`, proves the square-assisted ridge theorem: with one untouched original-coordinate square, ridge trace `theta>4q/3` and ridge diagonal cap `q/2` suffice.
4. The ridge-window source is `yspennstate/math-open-problems@9c1167db05c7b0f520f060796fde921ed769a4e7`; I use only its stated structural/ridge notions and do not upgrade its review status.

Together with the earlier fleet03/B19 low-offdiagonal-rank reduction, the presently surviving structural branch is the product-preserving `s_2(H)>1/8` case for `H=A-diag(A)` inside `sr(H)<32`; the former `s_2(H)<=1/8` one-effective residue has been paid.

## 2. New wedge/star-to-ridge dichotomy

For a real matrix `B` with singular values `sigma_1>=sigma_2>=...`, define its tail square mass

`T(B)=sum_{j>=2} sigma_j(B)^2 = ||B||_F^2-sigma_1(B)^2.`

For a symmetric zero-diagonal matrix `H`, let `r=||H||op` and `sr(H)=||H||F^2/r^2`.

### Theorem 2.1 — `QFORM-WEDGE-STAR-RIDGE-DICHOTOMY-v1`

Let `H` be real symmetric with zero diagonal. Assume

` s_2(H) >= delta >0,     sr(H) <= R. `

Then at least one of the following holds.

**(A) Heavy physical row.** There is an original coordinate `i` with

` ||H[i,i^c]||_2 >= delta / sqrt(256 R). `

**(B) Low-leverage ridge-ready physical cut.** There is a bipartition of the original coordinates into `I disjoint_union J`, a cross block `B=H[I,J]`, and a scale

` gamma >= delta/sqrt(128 R) `

such that, with

`K_gamma = B B^T (gamma^2 I+B B^T)^(-1),  theta=tr K_gamma,`

one has

` theta >= 8/5,      max_i (K_gamma)_ii <= 1/2. `

Thus at `delta=1/8`, `R=32`, every matrix in the surviving branch has either

` ||H[i,i^c]||_2 >= 1/(512 sqrt(2)) `

for some physical coordinate, or a physical ridge-ready cross bank at scale

` gamma >= 1/512,   theta>=8/5,   max diag K_gamma<=1/2. `

The second alternative is already beyond the square-assisted threshold `4/3` for `q=1`; what remains unpaid is **resource disjointness/routing** to an untouched nontrivial scalar square, not effective ridge dimension.

### Proof

Let

`E = sum_{|P|=|Q|=2} det H[P,Q]^2 = sum_{a<b} s_a(H)^2 s_b(H)^2.`

The equality is Cauchy--Binet for the second exterior power. Hence

`E >= r^2 delta^2.`                                                   (2.1)

Split `E=D+O`, where `D` sums those `2x2` minors whose row and column index pairs are disjoint, and `O` sums the overlapping ones. Put

`d_i=sum_{j ne i} H_ij^2`, and `w_ij=H_ij^2`.

Because the diagonal of `H` is zero, an overlap in one index contributes exactly a product `w_ij w_ik`, while a coincident row/column pair contributes `w_ij^2`. Counting the two orientations of every one-index overlap gives

`O = sum_i d_i^2 - sum_{i<j} w_ij^2 <= sum_i d_i^2.`               (2.2)

If `O>=E/2`, then

`max_i d_i >= (sum_i d_i^2)/(sum_i d_i)
             >= (E/2)/||H||F^2
             >= delta^2/(2R).`

Thus `||H[i,i^c]||_2>=delta/sqrt(2R)`, which is stronger than (A).

Assume instead `D>=E/2`. Choose a uniformly random bipartition `I disjoint_union J`. Every ordered disjoint row-pair/column-pair minor survives as a `2x2` minor of `H[I,J]` with probability `1/16`. Therefore some cut `B=H[I,J]` satisfies

`e_2(B):=sum_{a<b} sigma_a(B)^2 sigma_b(B)^2
        >= D/16 >= E/32 >= r^2 delta^2/32.`                         (2.3)

Write `S=||B||F^2` and `T=T(B)`. Since

`e_2(B) <= S T`

and `S<=||H||F^2<=R r^2`, (2.3) gives

`T >= delta^2/(32R).`                                                 (2.4)

Set `gamma^2=T/4`. Then `gamma>=delta/sqrt(128R)`. Write `x_j=sigma_j(B)^2`, so `T=sum_{j>=2}x_j`.

If `x_1>=T`, concavity/subadditivity of `x/(gamma^2+x)` with value zero at zero gives

`sum_{j>=2} x_j/(gamma^2+x_j) >= T/(gamma^2+T)=4/5,`

while `x_1/(gamma^2+x_1)>=4/5`. Hence `theta>=8/5`.

If `x_1<T`, then every `x_j<=x_1`, and

`theta >= (x_1+T)/(gamma^2+x_1)
         = (x_1+T)/(T/4+x_1) > 8/5.`

So in all cases `theta>=8/5`. If `max diag K_gamma<=1/2`, alternative (B) holds.

Otherwise for some row `i`, `(K_gamma)_ii>1/2`. Functional calculus gives

`K_gamma <= gamma^(-2) B B^T`,

hence

`||B[i,*]||_2^2 > gamma^2/2 = T/8
                  >= delta^2/(256R).`

Since `B[i,*]` is a subrow of the physical offdiagonal row of `H`, alternative (A) follows. QED.

## 3. Exact numerical consequence in the live B19 residual

The named partner's reduction plus the completed contamination splice leave

` s_2(H)>1/8,   sr(H)<32 `

as the genuinely two-offdiagonal-resource branch. Applying Theorem 2.1 with `delta=1/8`, `R=32` yields the explicit structural fork

`heavy row >= 1/(512 sqrt(2))`

or

`gamma>=1/512, theta>=8/5, max diag K_gamma<=1/2.`

The latter is exactly a `q=1` ridge bank satisfying the analytic threshold of fleet02/B04 (`8/5>4/3`). If an untouched original coordinate with `|A_kk|>=a_0>0` can be reserved disjointly from that bank, fleet02/B04 immediately gives a universal density bound depending only on the numerical lower bounds `a_0` and `gamma>=1/512`. The current theorem does **not** claim that such a scalar can always be reserved: the random-cut extraction may use the coordinate carrying the scalar resource. That is now the first unpaid product-geometry routing issue.

## 4. A target-valid no-go: one cross singular direction cannot be upgraded to a half-moment

A tempting way to route a heavy physical square is to combine its `|s|^(-1/2)` square kernel with a residual carrying one physical cross singular direction, by strengthening fleet01/B19's negative quarter-moment bound to a negative half-moment. This is false even inside the exact target class.

Let `U,V,X,Y` be independent `Uniform[0,1]`, and set

`Q = U^2 + V^2 + (X-Y)^2.`

Its symmetric matrix is

`diag(1,1) direct_sum [[1,-1],[-1,1]],`

with eigenvalues `{2,1,1,0}`. Hence it satisfies the exact three-large-eigenvalue hypothesis. The residual

`K=(X-Y)^2 = X^2 - 2XY + Y^2`

has a nonzero physical cross singular coefficient (`|C|=1`) and arbitrary same-bank self terms of precisely the form allowed by the fleet01/B19 cross-bank lemma. Nevertheless

`E |K|^(-1/2) = integral_0^1 integral_0^1 |x-y|^(-1) dx dy = infinity.`

More generally, for `0<alpha<1/2`,

`E |K|^(-alpha)
 = integral_0^1 integral_0^1 |x-y|^(-2alpha) dx dy
 = 1 / [(1-2alpha)(1-alpha)],`                                  (4.1)

and the integral diverges for `alpha>=1/2`. In particular the quarter moment is finite (`8/3` at `alpha=1/4`) while the half moment is not. So the quarter exponent used by the named partner/fleet01 splice is qualitatively sharp against rank-one-square collapse.

This does not threaten QFORM: `U^2+V^2` already has density at most `pi`, and convolution with the independent nonnegative residual cannot increase `L^infinity`. It shows instead that a universal proof must **reroute the degeneracy** rather than demand a half-moment from a single contaminated cross direction.

## 5. Conditional end-to-end architecture and exact first unpaid implication

Current source-valid assembly:

1. low-leverage spectral-window/ridge branches are paid in their stated scopes;
2. partner fleet03/B19 plus fleet02/B19 r15 and fleet01/B19 pays the entire `s_2(H)<=1/8` one-effective contaminated branch;
3. therefore the residual is `s_2(H)>1/8`, `sr(H)<32`;
4. Theorem 2.1 now forces either a universal heavy physical offdiagonal row or a universal-scale `q=1`, `theta>=8/5` low-leverage ridge-ready physical cut;
5. the half-moment counterexample rules out closing the heavy-square/rank-one-cross endpoint by simply upgrading the one-cross quarter-moment lemma.

The first unpaid implication can therefore be stated precisely as:

### `QFORM-DISJOINT-SCALAR-OR-DEGENERACY-ROUTING-v1`

There should exist universal constants `a_0,c_0>0` such that every target matrix in the residual `H=A-diag(A)`, `s_2(H)>1/8`, `sr(H)<32` satisfies at least one of:

- a paid branch already in the source ledger; or
- a cross bank `B=A[I,J]` and an original coordinate `k notin I union J` with `|A_kk|>=a_0`, together with a ridge scale `gamma>=c_0`, `tr K_gamma>4/3`, `max diag K_gamma<=1/2`; or
- a product-preserving aggregate/hyperbolic packet that pays the heavy-row alternative; or
- a quantitative rank-one-square collapse which, by the global three-large-eigenvalue hypothesis, forces a **second independent curvature resource** and hence descends to a paid two-square / hyperbolic-square branch.

Theorem 2.1 supplies the ridge-effective-dimension part with explicit `c_0=1/512`; what is not yet proved is the disjoint scalar / heavy-row / degeneracy routing. This is structural, not another Fourier exponent estimate.

Full QFORM remains **OPEN**. No continuity claim is added for the new structural lemma, and no auxiliary result is promoted to a full solution.

## 6. Exact computation used

`CHECKER.py` verifies the exterior-square decomposition on deterministic zero-diagonal symmetric examples, exhaustively averages all bipartitions to check the `D/16` factor, checks the `theta>=8/5` ridge inequality on representative spectra, and checks the target example eigenvalues and exact negative-moment values.

Checker SHA-256: `b90f5fffcfb7810f16251524655d1dd9ad87b0d1ff2a6978b47d68c8b867ece0`.

Captured stdout SHA-256: `b8f911be1dad29966f9d856040e8f8312b158f3c1b26003be714d1c6a289dd48`.

Exact captured stdout:

```text
H1: wedge=411 disjoint=84 overlap=327 avg_cut=5.25
H2: wedge=745 disjoint=344 overlap=401 avg_cut=21.5
ridge: x=[1, 1] T=1 gamma=0.5 theta=1.6
ridge: x=[10, 1] T=1 gamma=0.5 theta=1.7756097561
ridge: x=[1, 0.4, 0.3, 0.3] T=1 gamma=0.5 theta=2.50629370629
ridge: x=[1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1] T=1 gamma=0.5 theta=3.65714285714
ridge: x=[0.7, 0.6, 0.5, 0.4] T=1.5 gamma=0.612372435696 theta=2.35410500977
target_eigenvalues= [np.float64(2.0), np.float64(1.0), np.float64(1.0), np.float64(0.0)]
alpha=1/8: exact_negative_moment=32/21
alpha=1/4: exact_negative_moment=8/3
alpha=3/8: exact_negative_moment=32/5
alpha=1/2: DIVERGES logarithmically because integral |x-y|^{-1} dxdy diverges
QFORM_WEDGE_STAR_RIDGE_CHECK_PASS
```

The finite checks support the algebra only; the theorem is proved symbolically above.
