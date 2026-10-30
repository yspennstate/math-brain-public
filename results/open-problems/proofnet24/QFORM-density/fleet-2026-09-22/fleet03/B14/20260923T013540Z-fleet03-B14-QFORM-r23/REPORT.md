SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet03, slot B14, 2026-09-23T01:35:40Z.
attacking: zero-loss convex-output localization and an overlap-safe outer-square splice for a four-coordinate kernel-leakage core.

# fleet03/B14 r23 — convex-output localization and kernel-leakage outer-square splice

Programme: `QFORM-DENSITY-3EIG-20260922`  
Run: `20260923T013540Z-fleet03-B14-QFORM-r23`  
Status: `SUPPORTING TARGET-LEVEL THEOREMS PROVED / FULL QFORM OPEN / CONTINUITY OPEN`  
Execution: `WITHOUT_VERIFIED_BRAIN`.

## 1. Exact scope and source boundary

The exact target remains open: for every dimension, every product law of independent real coordinates with one-dimensional densities bounded by one, and every real symmetric matrix with at least three eigenvalues of modulus at least one, prove a universal essential bound for the density of `Q=X^TAX`, or produce a valid counterexample. No moment, support, connectedness, Gaussian, log-concave, centering, or post-rotation independence hypothesis is added here.


The designated completed partner actually used is fleet04/B14 r6, canonical report
`yspennstate/math-open-problems@6442bbe9d4647a730b27b8e0786bc54b2546b7ec:proofnet24/QFORM-density/fleet-2026-09-22/fleet04/B14/20260923T011517Z-fleet04-B14-kernel-leakage-core-r6/REPORT.md`.
Its kernel-leakage inequality is inserted explicitly in Theorem 5.1 below. I also use fleet04/B14 r4's law-level finite-mixture localization theorem, whose proof gives TV approximation by finite convex mixtures of product indicators of compact finite interval unions.

## 2. Compact end-to-end route

The first missing implication attacked this run is not another support truncation. It is whether the existing zero-loss localization can be pushed through *any* convex lower-semicontinuous output functional, so that future `L^p`, fractional-potential, and affine-core arguments may be proved on finite-fragment extreme inputs without hidden support taxes.

The second step is a concrete splice: fleet04/B14 r6 controls a four-coordinate residual block that absorbs rank-two kernel leakage. I convert that residual `L^infinity` bound into an exact half-Riesz trace bound and pass one additional physical square through it, allowing the square shift to depend arbitrarily on all residual coordinates. This gives a new five-coordinate/hierarchical target branch with an explicit constant.

## 3. Convex-output localization theorem

Let `D_n` be the product laws on `R^n` with one-dimensional probability densities `0<=f_i<=1`. Let `F_n` be the product laws whose marginals are indicators `1_E` of compact finite unions of intervals of total length one.

Let `P:R^n->R` be any measurable map. Let `Phi` be an extended-valued functional on finite positive Borel measures on `R` satisfying:

1. `Phi(theta mu+(1-theta)nu) <= theta Phi(mu)+(1-theta)Phi(nu)` for `0<=theta<=1`;
2. `Phi` is lower semicontinuous for total-variation convergence.

### Theorem 3.1 — `QFORM-CONVEX-OUTPUT-LOCALIZATION-v1`

For every such `P,Phi`,

`sup_{mu in D_n} Phi(P_#mu) = sup_{nu in F_n} Phi(P_#nu)`.        (3.1)

The equality is exact, including the value `+infinity`.

### Proof

Fix `mu in D_n`. By fleet04/B14 r4 there exist finite convex mixtures

`mu_m = sum_r theta_(m,r) nu_(m,r)`,  `nu_(m,r) in F_n`,

with `||mu_m-mu||_TV ->0`. Measurable pushforward contracts total variation, so

`||P_#mu_m-P_#mu||_TV ->0`.                                     (3.2)

Convexity gives

`Phi(P_#mu_m)
 <= sum_r theta_(m,r) Phi(P_#nu_(m,r))
 <= sup_(nu in F_n) Phi(P_#nu)`.                                (3.3)

Lower semicontinuity and (3.2) imply

`Phi(P_#mu)
 <= liminf_m Phi(P_#mu_m)
 <= sup_(nu in F_n) Phi(P_#nu)`.                                (3.4)

Taking the supremum over `mu in D_n` gives one inequality; `F_n subset D_n` gives the reverse. QED.

No support radius, fragment number, fragment separation, translation size, or moment enters (3.1).

## 4. Exact `L^p` and affine-core consequences

For `1<p<=infinity`, define for a probability measure `eta` on `R`

`N_p(eta)=||d eta/dx||_p` if `eta<<dx` with density in `L^p`, and `+infinity` otherwise.

### Lemma 4.1

`N_p` is convex and TV-lower-semicontinuous.

### Proof

Convexity is Minkowski for densities; if a positive mixture retains any singular part then the extended value is `+infinity` as required. For lower semicontinuity one may use the dual formula

`N_p(eta)=sup{ int phi d eta : phi in C_c(R), ||phi||_q<=1 }`,

with `q=p/(p-1)` (and `q=1` for `p=infinity`), interpreted as `+infinity` on singular measures. Each fixed `phi` is bounded, so its integral is continuous in TV; a supremum of continuous functions is lower semicontinuous. QED.

Therefore Theorem 3.1 yields

`boxed:
 sup_(mu in D_n) ||p_(P(X))||_p^ext
 =sup_(nu in F_n) ||p_(P(X))||_p^ext,
 1<p<=infinity. }                                               (4.1)

The same statement for `p=1` is immediate after separately recording absolute continuity: absolutely continuous probability measures form a TV-closed class and every such density has `L^1` norm one.

### Corollary 4.2 — affine-core ambient lift in `L^p`

Fix an actual original-coordinate block `S` and a symmetric matrix `B` on it. Suppose that for every finite-fragment product law on that block and every affine vector `ell` and scalar `c`,

`||p_(U^TBU+ell^TU+c)||_p <=K`.                                (4.2)

Then for every ambient quadratic form whose `S x S` principal block equals `B`, every independent cap-one product input law satisfies

`||p_Q||_p <=K`.                                                (4.3)

Indeed, condition on all outside original coordinates. They create only an affine `ell(v)` and scalar `c(v)`. Equation (4.1) transfers (4.2) from finite fragments to the actual rough core law with the identical `K`; averaging the conditional densities and Minkowski gives (4.3). Thus arbitrary outside tails, distant fragments, quadratic coefficients, and translations cost exactly zero.

This strictly extends the earlier interval/`L^infinity` affine compiler to every `L^p`, `1<p<=infinity`.

## 5. Fractional trace from a residual density cap

The next lemma is elementary but is the exact bridge needed for the completed partner theorem.

### Lemma 5.1 — density cap to fractional potential

If `Y` has a probability density bounded by `K`, then for every `0<alpha<1`,

`sup_t E|Y-t|^(-alpha)
 <= [2^alpha/(1-alpha)] K^alpha`.                               (5.1)

In particular,

`sup_t E|Y-t|^(-1/2) <= 2sqrt(2K)`.                             (5.2)

### Proof

The kernel `|u|^{-alpha}` is symmetric decreasing. Among densities `0<=p<=K` of total mass one, the integral against this kernel is maximized by filling the centered interval of length `1/K`. Hence

`int |u|^(-alpha)p(t+u)du
 <=2K int_0^(1/(2K)) u^(-alpha)du
 =[2^alpha/(1-alpha)]K^alpha`. QED.

No moment or support bound is used.

## 6. Actual application of fleet04/B14 r6: an overlap-safe outer-square splice

Let a quadratic-plus-affine form in original independent coordinates be written, after choosing one actual coordinate `Z`, as

`Q=a Z^2 +2Z r^T Y +d_0 Z +Y^T C Y+d^T Y+c`,  `a!=0`,          (6.1)

where `Y` denotes all remaining original coordinates. Completing only the physical coordinate `Z` gives

`Q=a[Z+m(Y)]^2+R(Y)`,                                           (6.2)

with

`m(Y)=(r^TY+d_0/2)/a`,
`R(Y)=Y^T S Y+e^T Y+c_0`,
`S=C-rr^T/a`,
`e=d-(d_0/a)r`.                                                  (6.3)

The shift `m(Y)` may depend on every residual coordinate; no independence between `m(Y)` and `R(Y)` is assumed.

Assume the residual Schur matrix `S` has an actual four-coordinate principal block

`H=[[B,c],[c^T,d]]`,                                             (6.4)

where `B` is a three-coordinate rank-two symmetric block with nonzero singular values `nu_1>=nu_2>0`, `k` is a unit vector spanning `Ker(B)`, and

`kappa:=|k^Tc|>0`.                                               (6.5)

Write `s_1(H)>=s_2(H)>=...` for the singular values of `H`.

Fleet04/B14 r6 proves, with arbitrary affine terms and arbitrary outside completion, that the residual law has density cap

`K_H=1000(8+log 4)
      sqrt(s_1(H)s_2(H))
      /[kappa sqrt(nu_1 nu_2)].`                                (6.6)

This is the promised equation-level partner application.

Condition on `Y`. The shifted-square density in the variable `t-R(Y)` is bounded by

`|a|^(-1/2)|t-R(Y)|^(-1/2)`.                                   (6.7)

Average (6.7), apply (5.2) to the residual law and insert (6.6). We obtain:

### Theorem 6.1 — `QFORM-KERNEL-LEAKAGE-OUTER-SQUARE-v1`

Under (6.1)-(6.6), for arbitrary independent cap-one inputs,

`boxed:
 ||p_Q||_infinity
 <= C_out |a|^(-1/2)
    [s_1(H)s_2(H)]^(1/4)
    /[kappa^(1/2)(nu_1nu_2)^(1/4)], }                           (6.8)

where

`C_out=2sqrt(2*1000(8+log4))
      =274.0261938008101... .`                                  (6.9)

The proof is completely insensitive to support diameter, tails, fragment count, fragment separation, or the size of the shift `m(Y)`.

This is a genuine new hierarchical branch: a physical square may be peeled off even when its completed-square shift reuses *all* residual variables, provided the Schur residual contains the partner's four-coordinate kernel-leakage core. Essential boundedness is proved; continuity is not claimed.

## 7. Stress test on the diffuse two-bank obstruction

The theorem does not falsely close the known aggregate family

`A_m=[1] direct_sum J_m/m direct_sum (-J_m/m)`.

Peeling the singleton square leaves

`S_m=J_m/m direct_sum (-J_m/m)`.                                (7.1)

Any rank-two three-coordinate principal block of `S_m` is formed by taking two coordinates from one constant bank and one from the other. Its kernel vector is the difference of the two same-bank coordinates. Every coupling vector from those three coordinates to any fourth physical coordinate is constant on that same-bank pair, hence

`k^Tc=0`.                                                        (7.2)

Thus the gate `kappa>0` fails identically. This is correct: that family is controlled only after bank aggregation, and any theorem paying one local leakage coordinate should fail there. The new splice therefore respects the live `aggregate-before-inversion` correction rather than hiding it.

## 8. Remaining implication

The full target remains open. The new localization result removes rough-input/support issues for all convex TV-lower-semicontinuous output functionals, and Theorem 6.1 closes a hierarchical square-plus-kernel-leakage branch. What remains structural: starting only from `s_3(A)>=1`, one still needs a product-preserving argument that either exposes a uniformly good branch of the form (6.8), or aggregates diffuse banks/ridge mass before any reciprocal local coupling is paid. The two-bank stress family (7.1) shows why single-coordinate leakage extraction is not enough.

Continuity remains separate. Neither TV localization nor the half-Riesz splice supplies a common modulus for arbitrary rough laws.

## 9. Integrity

- Full QFORM: `OPEN / NOT PROVED / NOT DISPROVED`.
- New proved theorem: exact convex-output localization, (3.1), including exact `L^p` density localization (4.1).
- New proved target branch: overlap-safe outer square over the completed fleet04/B14 kernel-leakage residual, (6.8).
- Completed designated partner actually applied: fleet04/B14 r6 at (6.6); fleet04/B14 r4 supplies the finite-mixture premise at (3.2)-(3.3).
- No random-variable rotation, support compactness, moment, fragment-count, or connected-support assumption was used.
- Repository transport is not native learned-memory ingestion; execution remains `WITHOUT_VERIFIED_BRAIN`.
