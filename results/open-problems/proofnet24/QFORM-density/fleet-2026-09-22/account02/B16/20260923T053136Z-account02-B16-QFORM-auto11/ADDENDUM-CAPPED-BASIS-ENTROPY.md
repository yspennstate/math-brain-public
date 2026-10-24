# Addendum — near-coloop entropy barrier for capped-basis Fresnel and a five-bank target-valid stress family

Programme: `QFORM-DENSITY-3EIG-20260922`  
Worker: account02/B16, Projection-product interaction  
Run: `20260923T053136Z-account02-B16-QFORM-auto11`  
Status: supporting theorem + exact mechanism obstruction; full QFORM remains open.  
Execution: `WITHOUT_VERIFIED_BRAIN`.

This addendum is to be read after `REPORT.md` together with `CORRECTION.md`. It records mathematics obtained after the report snapshot and does not rewrite either immutable file.

## Source pins actually used

1. Fresh owner-controlled brain state was read from `yspennstate/math-research-brain` main, OWNER CONTROL revision `2026-09-22.15`; live corrections did not stop account02/B16 or invalidate the premises below.
2. Designated partner: account03/B16 r26, `yspennstate/math-open-problems@d6730c301e46e6337bc3b32e30eb3d04f07dc90b`, path `proofnet24/QFORM-density/fleet-2026-09-22/account03/B16/20260923T045948Z-account03-B16-QFORM-r26/REPORT.md`. In particular, its capped-basis Fresnel interface uses a probability law `w` on nonsingular physical 3-bases with every coordinate marginal at most `1/2` and the score

`Z_w = exp(H(w)+sum_S w_S log(det(R_S)^2))`,

and yields the density certificate `3e (D Z_w)^(-1/3)` with `D=|det Lambda|`.
3. Required pinned Claude package: `yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`, especially `RESULTS.md`, `FOURIER_ROUTE_REPORT.md`, and `COUNTEREXAMPLE_SEARCH.md`. Its ruled one-sheet theorem gives the majority-sign density bound `pi sqrt(2)` for exact-rank-three indefinite forms while using two-dimensional product projections without asserting projected independence.
4. Previously completed account02/B16 theorem `QFORM-FINITE-LINE-BANK-COMPRESSION-v1`, canonical source `yspennstate/math-open-problems@b9e19e2c19ecd6f6ede282cd3c73ad014c449e9f`, proves for an exact-rank-three target whose nonzero spectral rows occupy `K` one-dimensional directions that

`||p_Q||_infinity <= 2 C_3 binom(K,3)^(1/3)`,

where `C_3=16 sqrt(30) 2^(1/4)=104.21688998922089...`.

## 1. First unpaid implication and the candidate proof engine

The partner r26 reduction leaves, after its paid exits, a true near-coloop collar with one physical row of leverage

`c>63/64`, `a:=1-c<1/64`.

A natural hope is that the capped-basis Fresnel theorem can be optimized over the basis law `w` so that `Z_w` stays bounded below as `a -> 0`. The next theorem shows that this is impossible for structural information alone: the marginal cap on the hub forces the entropy score to vanish at least as `sqrt(a)`.

## 2. `QFORM-NEAR-COLOOP-CAPPED-BASIS-ENTROPY-BARRIER-v1`

Let `R` be any `n x 3` Parseval frame, `R^T R=I_3`. For every physical triple `S` put

`v_S := det(R_S)^2`.

By Cauchy--Binet, `v=(v_S)` is a probability distribution on 3-subsets. Fix a physical coordinate `i`, write its leverage as

`c := ||r_i||^2`, `a:=1-c`.

The standard volume-sampling marginal identity gives

`sum_{S: i in S} v_S = c`, `sum_{S: i notin S} v_S = a`.          (2.1)

Let `w` be any probability distribution on nonsingular physical triples satisfying the capped-basis condition

`alpha_k := P_w(k in S) <= 1/2` for every coordinate `k`.           (2.2)

Define

`Z_w := exp(H(w)+sum_S w_S log v_S)`.                              (2.3)

If `w` puts positive mass on a triple with `v_S=0`, then `Z_w=0` and the conclusion below is immediate. Otherwise

`log Z_w
 = -sum_S w_S log(w_S/v_S)
 = -D_KL(w || v)`,                                                 (2.4)

so

`Z_w = exp(-D_KL(w||v))`.                                         (2.5)

Let

`q := P_w(i notin S) = 1-alpha_i >= 1/2`.                         (2.6)

Apply data processing for relative entropy under the binary map `S -> 1_{i notin S}`. By (2.1), the corresponding Bernoulli parameter under `v` is `a`, hence

`D_KL(w||v)
 >= q log(q/a)+(1-q)log((1-q)/c).`                                (2.7)

When `c>1/2`, equivalently `a<1/2`, the Bernoulli divergence in (2.7) is increasing for `q>=1/2`, because its unconstrained minimum is at `q=a<1/2`. Therefore

`D_KL(w||v)
 >= (1/2)log((1/2)/a)+(1/2)log((1/2)/c)
 = -log(2 sqrt(ac)).`                                              (2.8)

Combining (2.5) and (2.8),

`boxed: Z_w <= 2 sqrt(c(1-c)).`                                    (2.9)

This is a universal obstruction for every capped-basis law `w` in the near-coloop regime.

### Consequence for the partner Fresnel certificate

The partner certificate is

`||p_Q||_infinity <= 3e (D Z_w)^(-1/3)`.                          (2.10)

On any target-valid family with fixed `D`, (2.9) means this proof engine cannot produce a uniform constant as `a -> 0`: even the best admissible score can be at most order `sqrt(a)`, so the resulting certificate necessarily deteriorates at least on the `a^(-1/6)` scale. This is a statement about the certificate, not a lower bound on the true density.

## 3. Sharp target-valid stress family

The score loss in (2.9) is not merely an artifact of the data-processing proof. It is attained on an explicit exact-rank-three family whose true density remains uniformly bounded.

Let `m` be divisible by four and `m>128`. Choose signs `(sigma_j,tau_j)` so that each of the four pairs in `{+/-1}^2` occurs exactly `m/4` times, and put

`eta_j := sigma_j tau_j`.

Fix `a in (0,1/64)`, `c=1-a`. In coefficient coordinates define the Parseval-frame rows

`r_0 = sqrt(c) e_1`,

`r_j = (sqrt(a) eta_j, sigma_j, tau_j)/sqrt(m)`, `1<=j<=m`.         (3.1)

The balanced-sign identities give

`sum eta_j = sum sigma_j = sum tau_j = 0`,
`sum eta_j sigma_j = sum tau_j =0`,
`sum eta_j tau_j = sum sigma_j =0`,
`sum sigma_j tau_j = sum eta_j =0`.                               (3.2)

Hence

`sum_{j=1}^m r_j r_j^T = diag(a,1,1)`,

and after adding `r_0 r_0^T=diag(c,0,0)`,

`R^T R=I_3`.                                                       (3.3)

Take the coefficient-space quadratic matrix

`B = [[0,1,0],[1,0,0],[0,0,1]]`.                                  (3.4)

Its eigenvalues are exactly `{1,-1,1}` and `|det B|=1`. Therefore

`A=R B R^T`                                                        (3.5)

has exact rank three and nonzero spectrum `{1,-1,1}`. Every member of the family is inside the exact target class.

The hub leverage is `c>63/64`; the family is a genuine near-coloop family. The nonzero spectral rows occupy only five one-dimensional directions: the hub direction plus one direction for each of the four sign pairs `(sigma,tau)`. Orthogonal diagonalization of `B` preserves this number of row lines. Therefore `QFORM-FINITE-LINE-BANK-COMPRESSION-v1` applies after grouping the original coordinates by these five directions. It gives

`||p_Q||_infinity
 <= 2 C_3 binom(5,3)^(1/3)
 = 449.0569661600281... < 450`,                                    (3.6)

uniformly in `a`, `m`, and in all independent original-coordinate input laws with density caps one. The grouping occurs before the curved pushforward and uses only independence of disjoint original-coordinate banks.

Thus the family is harmless for the actual QFORM target despite the capped-basis score degeneration proved below.

## 4. Exact attainment of the entropy barrier

For the natural Pluecker law `v_S=det(R_S)^2`, (2.1) says

`P_v(0 in S)=c`, `P_v(0 notin S)=a`.                               (4.1)

Define

`w_* := (1/2) v(. | 0 in S) + (1/2) v(. | 0 notin S)`.             (4.2)

Then the hub marginal under `w_*` is exactly `1/2`.

Conditional on `0 in S`, a basis consists of the hub plus two leaves. The transverse leaf vectors

`u_j=(sigma_j,tau_j)/sqrt(m)`                                      (4.3)

form a two-dimensional Parseval frame. The conditional Pluecker law is its two-volume sampling law, so each leaf inclusion marginal equals

`||u_j||^2=2/m`.                                                    (4.4)

Conditional on `0 notin S`, normalize the first leaf coordinate by `sqrt(a)` and write

`u~_j=(eta_j,sigma_j,tau_j)/sqrt(m)`.                              (4.5)

The balanced-sign identities make `(u~_j)` a three-dimensional Parseval frame. The factor `sqrt(a)` in every three-leaf determinant is common and cancels under conditioning, so the conditional law is the three-volume sampling law of `(u~_j)`. Hence every leaf inclusion marginal is

`||u~_j||^2=3/m`.                                                   (4.6)

Therefore under `w_*`, every leaf marginal is

`(1/2)(2/m)+(1/2)(3/m)=5/(2m)<1/2`,                               (4.7)

while the hub marginal is exactly `1/2`. Thus `w_*` satisfies all capped-basis hypotheses.

The likelihood ratio is constant on the two binary classes:

`w_*(S)/v_S = 1/(2c)` if `0 in S`,
`w_*(S)/v_S = 1/(2a)` if `0 notin S`.                              (4.8)

Hence

`D_KL(w_*||v)
 = (1/2)log(1/(2c))+(1/2)log(1/(2a))
 = -log(2 sqrt(ac))`,                                              (4.9)

and therefore

`boxed: Z_{w_*}=2 sqrt(ac).`                                       (4.10)

So (2.9) is sharp on a genuine target-valid family. With `D=1`, the best capped-basis Fresnel certificate on this family is forced to scale like `a^(-1/6)` even though the true density is `<450` by (3.6).

This explains the `a^(-1/6)` degradation at the near-coloop boundary as an information-theoretic consequence of simultaneously demanding a half-marginal cap on the almost-mandatory hub and comparing to the natural Pluecker law.

## 5. Applying the pinned Claude theorem to a real target-level side inequality

The same family has exact-rank-three indefinite signature `(2,1)`. The completed ruled one-sheet theorem in the required pinned Claude source applies to its majority-sign side and gives

`boxed: ess sup_{majority-sign levels} p_Q <= pi sqrt(2).`          (5.1)

The theorem reaches (5.1) through a two-dimensional product-projection estimate and does not assert that the projected pair is independent. Thus the source is used at an actual curved-pushforward inequality, not just as background.

Combined with (3.6)--(4.10), this localizes the remaining near-coloop difficulty: the majority-sign/one-sheet side is already uniformly paid, while any general proof of the minority-sign/two-sheet side cannot rely solely on capped-basis reweighting with all coordinate marginals at most `1/2`.

## 6. What this changes and what it does not

`QFORM-NEAR-COLOOP-CAPPED-BASIS-ENTROPY-BARRIER-v1`: PROVED.  
`QFORM-FOUR-SIGN-NEAR-COLOOP-STRESS-v1`: PROVED target-valid supporting construction.  
Full QFORM: OPEN.

The obstruction is to a proof engine, not to the conjecture. It does not rule out phase-sensitive Fresnel, mixed-hub, grouped-bank, or real-space source-provenance arguments. In fact the same family is paid by grouped-bank compression.

The first unpaid B16 implication is now:

`QFORM-NEAR-COLOOP-SOURCE-PROVENANCE-TRANSITION-v1`.

In the partner collar `c>63/64`, bridge the exact-coloop endpoint to small positive `a=1-c` while retaining the original hub source factor and the common-source longitudinal/transverse modulation before any completion or absolute-value step. On indefinite exact-rank-three forms, the pinned Claude result already pays the majority-sign side, so the remaining curved debt is the minority/two-sheet side. The addendum proves that forcing every basis marginal below `1/2` cannot be the uniform bridge. Arbitrary additional spectrum remains a separate global debt.
