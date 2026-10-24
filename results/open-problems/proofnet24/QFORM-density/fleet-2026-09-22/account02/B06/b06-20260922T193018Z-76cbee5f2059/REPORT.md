SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account02, slot B06, 2026-09-22T19:30:18Z.
attacking: the near-coloop ridge branch by integrating the hyperbolic two-bank singularity against the original product law, and testing whether near-coloop geometry forces one paid physical pair.

# account02/B06 — weighted hyperbolic two-bank smoothing and the near-coloop area budget

**Run:** `b06-20260922T193018Z-76cbee5f2059`  
**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Assignment:** `Curved fiber integration`  
**Classification:** `ESSENTIAL_STEP_APPLIED + CANDIDATE_REFUTED`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`  
**Full target:** OPEN / NOT PROVED / NOT DISPROVED.

## 0. Fresh scope and source pins

The sole target is the full arbitrary-dimensional statement: for independent real coordinates with densities at most one and a real symmetric `A` with at least three eigenvalues of modulus at least one, prove one universal density bound for `X^T A X`, or give a target-valid counterexample. No moment, support, sign, diagonal-basis, or post-rotation-independence hypothesis is added.

Fresh source control was read from `yspennstate/math-research-brain` under OWNER CONTROL revision `2026-09-22.13`. The proof-first continuation `QFORM-PROOF-FIRST-20260922T161801Z` explicitly prioritizes a product-preserving ridge-or-grouped-coordinate reduction and forbids the two corrected coarea interfaces. The live corrections used here include the failure of law-uniform pointwise quadratic-phase decay, unrestricted fiber suprema, arbitrary-joint rank-three coarea, conditional spectral-projection height moments, and fixed-good-minor reductions.

Latest complete own mathematical predecessor consumed: account02/B06 run `b06-20260922T182419Z-a73c8f1e`, canonical source `yspennstate/math-open-problems@1ce009d4eae2ef54915194828a32c99777f7cbf5`. It refuted a scalar conditional-supremum gate and replaced it by a probability-weighted curved-fiber envelope.

The product-projection input used below is `QFORM-WEIGHTED-AFFINE-FIBER-BL-v1`, account02/B06 `yspennstate/math-open-problems@8dd33c1abd4fd64140f59032feda2b13d4351da5`: if `R` has `k` orthonormal columns and the original coordinates are independent with density cap one, then `R^T X` has density cap at most `exp(k/2)`. In particular a unit linear form has density cap `sqrt(e)` and a two-dimensional orthogonal projection has density cap `e`.

The designated partner result actually consumed is account03/B06 run `20260922T181926Z-account03-B06-qform-r15`, canonical source `yspennstate/math-open-problems@e9064dc270a3f8b27be00279146080fdae0ec098`. Its `QFORM-TRANSVERSE-ARBITRARY-COLLAR-RIDGE-CLOSURE-v1` proves, in the stated O0/transverse/pivot setup, that for every fixed `epsilon`, at scale `g_epsilon=gamma sqrt(epsilon/(4+2sqrt(3)))`, `tr K_g(H)>=2-epsilon`; and if `max_i K_ii<=1-epsilon`, then the full ambient quadratic form is essentially bounded. At `epsilon=1/32` its explicit bound is `||p_Q||_infinity < 2101/sqrt(|a| gamma)`. Its remaining branch is a residual physical row with ridge leverage above `31/32`.

## 1. Conditional end-to-end route for this run

Apply the partner theorem first. If `max_i K_ii<=31/32` at the partner scale, the density is already bounded by the displayed partner inequality. Otherwise choose `i` with `K_ii>31/32`. The first new lemma below shows that this row carries a weighted two-row area budget `sum_(j!=i) det K[{i,j}] > (31/32)^2`, while deleting it leaves effective ridge dimension at least `31/32`.

A tempting next step would be to extract one uniformly conditioned original-coordinate pair. Section 4 gives an exact target matrix family showing that this is false: the entire area budget can be spread over arbitrarily many tiny physical pairs. The correct repair is to group the coordinate banks before taking the hyperbolic reciprocal. Section 3 proves a dimension-free two-bank density theorem. Its proof explicitly integrates a `1/|u-u0|` fiber singularity against a two-dimensional product-projection density cap; it never takes the false fiber supremum.

The remaining full-target debt is to force this grouped two-bank payment, or another completed payment, in the arbitrary near-coloop branch while retaining arbitrary same-side quadratic terms and extra spectrum.

## 2. Near-coloop ridge geometry: an exact weighted area budget

For a real `m x r` matrix `H` and `g>0`, write `K=K_g(H)=H(H^T H+g^2 I)^(-1)H^T`. Its eigenvalues lie in `[0,1)`, hence `0<=K<=I`.

### Lemma 2.1 — `QFORM-NEAR-COLOOP-RIDGE-AREA-BUDGET-v1`

For every row index `i`,

`sum_(j!=i) det K[{i,j}] = K_ii tr K - (K^2)_ii >= K_ii (tr K-1)`.   (2.1)

Therefore, if `tr K>=2-epsilon` and `K_ii>1-epsilon`, then

`sum_(j!=i) det K[{i,j}] > (1-epsilon)^2`.                            (2.2)

Expanding the two-by-two principal determinants gives
`sum_(j!=i) (K_ii K_jj-K_ij^2)=K_ii tr K-(K^2)_ii`. Since `0<=K<=I`, one has `K^2<=K`, hence `(K^2)_ii<=K_ii`. This proves the claim.

This is the right invariant for a near-coloop: not one large minor, but a normalized sum of squared two-row wedge areas.

### Lemma 2.2 — deletion cannot erase more than one ridge dimension

Let `H_-i` be `H` with row `i` deleted. Then

`tr K_g(H_-i) >= tr K_g(H)-K_ii >= tr K_g(H)-1`.              (2.3)

In particular, under the partner hypotheses `tr K>=2-epsilon`, deleting any near-coloop leaves `tr K_g(H_-i) >=1-epsilon`.

Proof: write `h` for row `i`, `M=H_-i^T H_-i+g^2 I`, and `t=h^T M^(-1)h`. Then `H^T H+g^2 I=M+hh^T`. Sherman--Morrison gives `K_ii=t/(1+t)`. Also the difference `tr K_g(H)-tr K_g(H_-i)` equals `g^2 h^T M^(-2)h/(1+t)`. Since `M>=g^2 I`, `g^2 M^(-2)<=M^(-1)`, so this difference is at most `t/(1+t)=K_ii`.

Applied to account03/B06 r15 at `epsilon=1/32`, the unpaid branch is therefore not “find some curvature”: it contains a row with leverage `>31/32`, total attached two-row area `>(31/32)^2`, and after deletion still at least `31/32` effective ridge dimension.

## 3. Weighted product replacement for the hyperbolic fiber supremum

### Theorem 3.1 — `QFORM-WEIGHTED-HYPERBOLIC-TWO-BANK-v1`

Let all coordinates of `X in R^m` and `Y in R^n` be mutually independent and have densities at most one. Let `R in R^(m x 2)` and `S in R^(n x 2)` have orthonormal columns. Put `U=R^T X`, `V=S^T Y`. Let `D` be invertible `2 x 2`, with `sigma=sigma_min(D)>0`, and let `alpha,beta in R^2`, `c in R`. Then

`T = 2 U^T D V + alpha^T U + beta^T V + c`

has an essentially bounded density satisfying

`||p_T||_infinity <= e sqrt(2 pi) / sigma`.                            (3.1)

The same bound holds after adding any random variable independent of all coordinates used in the two banks.

Proof: the weighted affine-fiber Brascamp--Lieb theorem gives `||p_U||_infinity<=e`. For fixed `U=u`, the `V`-dependent part is `w(u)^T V` with `w(u)=2D^T u+beta`. Because `S` has orthonormal columns, the `k=1` case of the same product-projection theorem gives `||p_(w^T V)||_infinity <= sqrt(e)/||w||` for `w!=0`. Let `u0=-(1/2)D^(-T) beta`. Then `||w(u)||>=2 sigma ||u-u0||`, so averaging conditional densities rather than taking their supremum yields

`||p_T||_infinity <= sqrt(e)/(2 sigma) E[1/||U-u0||]`.                 (3.2)

For every `rho>0`, the two-dimensional density cap gives

`E[1/||U-u0||] <= e int_(|z|<=rho)|z|^(-1)dz + rho^(-1)
                  =2 pi e rho+rho^(-1)`.                              (3.3)

Optimizing at `rho=(2 pi e)^(-1/2)` yields `E[1/||U-u0||]<=2sqrt(2 pi e)`, proving (3.1). An independent remainder only convolves the density and cannot increase the sup norm.

The conditional density in the first step has an infinite supremum over `u`: it blows up at `u0`. The original product law supplies a two-dimensional density cap for `U`, and the singularity is only `1/|u-u0|`, locally integrable in two dimensions. This is precisely a weighted product-structure replacement for the dimension-losing fiber supremum.

## 4. Exact target adversary: near-coloop does not force one paid physical pair

Fix `epsilon in (0,1/2]`, put `C0=4+2sqrt(3)`, `g=sqrt(epsilon/C0)`, and choose integers `N>=1`, even `M>=2`. Let `u,v in R^M` be orthonormal flat vectors: `u=(1,...,1)/sqrt(M)` and `v=(1,...,1,-1,...,-1)/sqrt(M)` with half plus and half minus signs. Define the `(N+1) x M` cross block `H` by `h_0=u`, `h_j=v/sqrt(N)` for `1<=j<=N`.

Then `H` has exactly two nonzero singular values, both one. Hence the symmetric target matrix `A_{N,M}=[[0,H],[H^T,0]]` has nonzero spectrum exactly `{1,1,-1,-1}` and lies inside the full QFORM hypothesis.

At the partner scale, with `s=1/(1+epsilon/C0)`, one has `K_g(H)=s H H^T`, so `tr K=2s>=2-epsilon`, `K_00=s>1-epsilon`, and

`det K[{0,j}]=s^2/N`, `sum_(j=1)^N det K[{0,j}]=s^2`.                 (4.1)

Thus the entire near-coloop area budget is present, but every individual attached ridge minor tends to zero as `N` grows. More strongly, every physical two-by-two principal block of `A_{N,M}` is either zero or has eigenvalues `+/-|H_ab|`, while `max |H_ab|=1/sqrt(M)`. Hence no dimension-free lower bound on a single conditioned physical pair follows from the partner near-coloop hypotheses. This is an exact target-matrix falsifier to that proposed reduction, not a counterexample to QFORM.

The same family is paid by grouping first. Define the two orthogonal product projections

`U=(X_0, N^(-1/2) sum_(j=1)^N X_j)`,
`V=(u^T Y, v^T Y)`.

Then exactly `X^T A_{N,M} X=2U^T V`. Theorem 3.1 with `D=I` gives, for every choice of independent cap-one input laws,

`||p_(X^T A_{N,M} X)||_infinity <= e sqrt(2 pi) <6.814`,              (4.2)

uniformly in `N,M`. Thus the false “near-coloop -> one good physical pair” step is repaired on its canonical diffuse adversary by aggregating each independent coordinate bank into its two-dimensional product projection before paying the hyperbolic reciprocal.

## 5. Partner result applied to a real branch inequality

Take `epsilon=1/32`. In the exact O0/transverse/pivot hypotheses of account03/B06 r15, with `g=gamma/sqrt(32(4+2sqrt(3)))`, there are now two rigorously separated cases. If `max_i K_ii<=31/32`, the completed partner theorem gives `||p_Q||_infinity <2101/sqrt(|a| gamma)`. If some `K_ii>31/32`, Lemmas 2.1-2.2 give

`sum_(j!=i) det K[{i,j}]>(31/32)^2`, `tr K_g(H_-i)>=31/32`.            (5.1)

This is the new exact output of applying the partner result: every survivor carries both a near-coloop and a quantitative aggregate second-direction certificate. Section 4 proves that (5.1) cannot be converted, using ridge geometry alone, into one uniformly conditioned physical pair. Theorem 3.1 supplies a complete payment whenever this certificate is realized as a disjoint two-bank bilinear block (affine perturbations allowed, plus an independent remainder).

## 6. First unpaid implication

`QFORM-NEAR-COLOOP-GROUPED-PAYMENT-v1`: starting from the r15 near-coloop alternative and the weighted area/deletion certificates (5.1), either extract an original-coordinate indefinite physical pair with dimension-free `D^2 kappa` and invoke the arbitrary-rank pair theorem, or build a disjoint grouped-coordinate hyperbolic smoother to which Theorem 3.1 applies, or obtain a second ridge payment after deletion. This reduction must retain arbitrary same-side quadratic terms and all extra spectral components.

The exact family above shows why the grouped option is indispensable: all local physical pairs can be arbitrarily weak while grouped product structure remains uniformly strong. No full-QFORM proof is claimed.

## 7. Decisive computation

`CHECK.py` is a finite sanity check of the exact family at `epsilon=1/32`, `N=M=64`. It verifies the two unit singular values of `H`, the four eigenvalues `+/-1` of `A`, the near-coloop and trace inequalities, the exact `s^2/N` pair-minor distribution and `s^2` total, the `1/sqrt(M)` physical-pair ceiling, and the constant `e sqrt(2 pi)`.

Executed-code SHA-256: `aedf7aa8cbf3db92f0a0e37d74a949d9b540d1da0bad121e3b8bff3199b7539f`.
Output SHA-256: `98bd91b18c6add08995ff671529f6c6080781c0f1d874ad63235765b52f94df6`.
The computation is not a proof certificate; the analytic identities above are the proof.
