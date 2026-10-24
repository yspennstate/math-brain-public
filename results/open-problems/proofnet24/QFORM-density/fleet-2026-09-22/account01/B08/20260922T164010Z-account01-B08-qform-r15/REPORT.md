# account01/B08 — large-defect stable-rank trichotomy for a diffuse selected eigenspace

**Run:** `20260922T164010Z-account01-B08-qform-r15`  
**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Fresh owner control at start:** revision `2026-09-22.7`  
**Assignment:** diffuse eigenvector case  
**Classification:** `ESSENTIAL_STEP_APPLIED / PROVED_SUPPORTING_THEOREM / FULL_TARGET_OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`; repository retrieval is not native learned-memory ingestion.

## 1. Exact target and conditional end-to-end position

The full target remains open: for every dimension, every product law of independent real coordinates with densities bounded by one, and every real symmetric matrix `A` with at least three eigenvalues of modulus at least one, prove one universal density bound for `X^T A X`, ideally with a continuous density, or give a valid counterexample.

This run attacks the first unpaid implication from the preceding B08 result: a selected three-dimensional large-eigenspace may be diffuse while the remaining spectral part is a large, dense, nonseparable operator. The preceding perturbative theorem paid a small operator-norm defect. The new point is that a **large defect of sufficiently high stable rank cannot remain an unstructured obstruction**: after an original-coordinate cut it either gives an immediately ridge-certifiable cross block or creates a quantitatively localized physical cross row. Thus the only still-unpaid large-defect diffuse branch has low stable rank or a localized certificate.

A compact conditional end-to-end route is therefore:

1. choose any three genuine eigenvectors with `|lambda_j|>=1` and test their original-coordinate row leverage;
2. localized selected rows go to the existing localized-coordinate machinery;
3. if the selected frame is diffuse, split the complementary spectral part into its original-coordinate diagonal plus off-diagonal defect `E`;
4. if `||E||` is small, the designated partner theorem below closes the density problem continuously;
5. if `||E||` is large and `sr(E)` is high, the theorem proved in this report either closes continuously by the ridge theorem or produces a universal localized cross-row resource;
6. hence the remaining diffuse debt is reduced to low-stable-rank off-diagonal remainders plus the explicit localized-cross-row branch, where grouped-coordinate / pivot / quarter-moment mechanisms can be applied.

Steps 2 and 6 are not yet an exhaustive proof of the full conjecture, so no full-solution status is claimed.

## 2. Exact source dependencies actually applied

### Assigned partner account02/B08

The named partner result actually used is account02/B08 `QFORM-DIFFUSE-APPROX-BLOCK-STABILITY-v1`, canonical source

`yspennstate/math-open-problems@c1c6ffe8c742cbba7611b5a3f1d73cf71019f47b`

at

`proofnet24/QFORM-density/fleet-2026-09-22/account02/B08/B08-20260922T153820Z-r12/REPORT.md`.

Specialized to no conditioning and singleton blocks, it says the following. Write

`A=R Lambda R^T+C`, `R^T R=I_3`, `s_min(Lambda)>=1`,

let `delta=max_i ||r_i||^2` for the rows `r_i` of `R`, write

`C=D+E`,

where `D=diag(C)` and `E=C-D`, and put `tau=||E||`. If

`delta<=1/48`, `tau<=1/40`,

then the theorem's hypotheses hold and `X^T A X` has a continuous `C_0` density with

`||p_Q||_infinity <= (720/41)sqrt(3e) < 51`.                    (2.1)

This exact inequality is the small-defect branch below. It retains the full arbitrary diagonal `D`, all signs, all additional spectral directions, and arbitrary input densities bounded by one.

### Ridge endpoint

The large-defect branch uses `QFORM-RIDGE-DENSITY-v1`, canonical source

`yspennstate/math-open-problems@9c1167db05c7b0f520f060796fde921ed769a4e7`

at

`proofnet24/QFORM-density/interactive/20260922T151048Z-ridge-window/REPORT.md`.

For an original-coordinate cross block `B=A[I,J]`, define

`K_gamma=BB^T(gamma^2 I+BB^T)^(-1)`, `theta_gamma=tr K_gamma`.

Its `q=1` case states that if

`max_i (K_gamma)_ii <=1/2`, `theta_gamma>2`,

then the full quadratic form, with arbitrary self blocks, outside coordinates and outside couplings, has a continuous `C_0` density and

`||p_Q||_infinity <= sqrt(e)/(sqrt(2) gamma) * theta_gamma/(theta_gamma-2)`.    (2.2)

No post-rotation independence is used.

### Optional downstream localized resource

For interpretation of the localized alternative, account01/B19 `QFORM-SAME-BANK-CONTAMINATION-SPLICE-v1`, canonical source `yspennstate/math-open-problems@2e5d5cdc3bb7121673bc920497fb11cac9eceb46`, proves a quarter-negative-moment estimate from one nontrivial original-coordinate cross singular direction. It is not needed to prove the trichotomy itself, but it makes the localized output directly consumable by existing proof branches.

## 3. New theorem — `QFORM-DIFFUSE-LARGE-DEFECT-STABLE-RANK-v1`

Let

`A=R Lambda R^T+C`

with `R` an `n x 3` real matrix with orthonormal columns and `Lambda` real symmetric with `s_min(Lambda)>=1`. In the target application the columns of `R` are three genuine large eigenvectors, so `C` is the remaining spectral part; the proof below only uses the displayed decomposition and rank at most three of `R Lambda R^T`.

Assume the selected frame is diffuse:

`delta := max_i ||r_i||^2 <= 1/48`.                              (3.1)

Split the residual in the **original independent coordinates** as

`D=diag(C)`, `E=C-D`, `tau=||E||_op`.                             (3.2)

Thus `E` is symmetric with zero diagonal. If `tau>0`, define its stable rank

`sr(E)=||E||_F^2/tau^2`.

Then one of the following holds.

### (A) Small defect — already closed

If `tau<=1/40`, then by the assigned partner theorem

`||p_Q||_infinity <51`,

and the density is continuous and vanishes at infinity.

### (B) Large high-stable-rank defect — ridge closure or a localized physical row

Suppose

`tau>1/40`, `sr(E)>=30`.                                         (3.3)

Then there exists an original-coordinate cut `I sqcup J=[n]`. Put

`F=E[I,J]`, `B=A[I,J]`, `gamma=tau/2`,
`K_gamma=BB^T(gamma^2 I+BB^T)^(-1)`.

For this cut,

`theta_gamma(B):=tr K_gamma >=3`.                               (3.4)

Consequently exactly one of the following two source-valid conclusions is available:

1. if `max_i (K_gamma)_ii<=1/2`, then the full quadratic form has a continuous `C_0` density and

   `||p_Q||_infinity <= 3 sqrt(2e)/tau < 120 sqrt(2e) <280`;       (3.5)

2. otherwise there is a genuine original coordinate `i in I` whose physical cross row satisfies

   `||B[i,J]||_2 > gamma/sqrt(2)=tau/(2sqrt(2)) > 1/(80sqrt(2))`.  (3.6)

Thus a high-stable-rank large defect cannot evade both diffuse ridge smoothing and a universal localized physical cross resource.

### (C) Remaining large-defect diffuse obstruction

If neither (A) nor (B) applies, then necessarily

`tau>1/40`, `sr(E)<30`,                                           (3.7)

or the high-stable-rank branch has produced the explicit localized row (3.6). Hence an unresolved counterexample inside (3.1) must have a **low-stable-rank off-diagonal residual** or expose a fixed-scale localized cross coordinate.

## 4. Proof of the new theorem

Only branch (B) is new; branch (A) is exactly the designated partner inequality (2.1).

### 4.1 Random physical cut captures one quarter of off-diagonal Frobenius energy

Give each original coordinate an independent sign `epsilon_i in {+1,-1}` and let `I={i:epsilon_i=+1}`, `J=I^c`. For the rectangular cross block `F=E[I,J]`, every unordered off-diagonal pair `{i,j}` is separated with probability `1/2`; when it is separated, exactly one copy of `E_ij^2=E_ji^2` appears in `||F||_F^2`. Since `E` has zero diagonal,

`E_cut ||F||_F^2 = (1/4)||E||_F^2`.                              (4.1)

Therefore some deterministic cut satisfies

`||F||_F^2 >= (1/4)||E||_F^2 = (sr(E)/4) tau^2`.                 (4.2)

Also, because `F` is a compression of `E`,

`||F||_op<=tau`.                                                  (4.3)

Fix such a cut for the rest of the proof.

### 4.2 The residual cross block already has ridge effective dimension at least six

At `gamma=tau/2`, write the singular values of `F` as `s_j(F)`. From (4.3), `s_j(F)^2<=tau^2`, so termwise

`s_j(F)^2/(gamma^2+s_j(F)^2)
 >= s_j(F)^2/(tau^2/4+tau^2)
 = (4/5) s_j(F)^2/tau^2`.

Summing and using (4.2),

`theta_gamma(F)
 :=sum_j s_j(F)^2/(gamma^2+s_j(F)^2)
 >= (4/5)||F||_F^2/tau^2
 >= sr(E)/5
 >=6`.                                                          (4.4)

This is the key aggregation step: it converts failure of a small operator-norm residual approximation into a scale-sensitive effective-dimension resource without taking any fiber supremum and without rotating the product law.

### 4.3 The selected three-eigenvector core can destroy at most three ridge directions

Across the same physical cut,

`B=A[I,J]=F+G`,

where

`G=(R Lambda R^T)[I,J]`.

Independently of the size or signs of the three selected eigenvalues,

`rank(G)<=3`.                                                     (4.5)

The standard singular-value rank-perturbation inequality gives

`s_j(B)>=s_(j+3)(F)`                                              (4.6)

for every admissible `j`: indeed Weyl's inequality applied to `F=B-G` has `s_4(G)=0`.

The function

`h_gamma(s)=s^2/(gamma^2+s^2)`

is increasing on `[0,infinity)`. Hence (4.6) implies

`theta_gamma(B)
 >= sum_j h_gamma(s_(j+3)(F))
 >= theta_gamma(F)-3
 >=3`.                                                           (4.7)

The loss of three is exact at the level needed here: a rank-three selected spectral core may cancel three residual singular directions, but not a stable-rank bank of six ridge units.

### 4.4 Low ridge leverage closes the entire quadratic form

If

`max_i (K_gamma)_ii<=1/2`,

then (4.7) and the ridge theorem (2.2) apply with `q=1`. Since `x/(x-2)` decreases for `x>2`, (4.7) gives

`||p_Q||_infinity
 <= sqrt(e)/(sqrt(2)gamma) * 3
 = 3sqrt(2e)/tau`.                                               (4.8)

Under `tau>1/40`,

`3sqrt(2e)/tau <120sqrt(2e)=279.7972777916...<280`.              (4.9)

The cited ridge theorem supplies an integrable characteristic-function envelope, hence the density is continuous and vanishes at infinity. All diagonal/self terms, signs, outside couplings and additional eigenvalues are already included in that theorem.

### 4.5 High ridge leverage gives a fixed original-coordinate resource

If instead some coordinate `i in I` has

`(K_gamma)_ii>1/2`,

then functional calculus gives the positive-semidefinite inequality

`K_gamma <= gamma^(-2) BB^T`,

because `x/(gamma^2+x)<=x/gamma^2` for `x>=0`. Taking the `i`-th diagonal entry,

`||B[i,J]||_2^2=(BB^T)_ii > gamma^2/2`.

Thus

`||B[i,J]||_2 > gamma/sqrt(2)=tau/(2sqrt(2))>1/(80sqrt(2))`       (4.10)

as claimed. This is a statement in the original physical coordinates, so it may be used by localized-coordinate conditioning and cross-bank lemmas without asserting independence after a spectral rotation.

This proves the theorem. QED.

## 5. A downstream quantitative consequence of the localized alternative

For completeness, (4.10) implies

`s_1(B)>1/(80sqrt(2))`.

The completed one-cross-singular-direction lemma in the account01/B19 source cited above therefore yields, after conditioning any outside original coordinates, the uniform quarter-negative-moment certificate

`sup_t E |K-t|^(-1/4)
 <= (2+sqrt(pi)) [320 sqrt(2) e]^(1/4)`                          (5.1)

for the corresponding two-bank conditional quadratic expression `K=F(X_I)+2X_I^T B X_J+G(X_J)`. This is not itself a density bound, but it shows that the localized output is already in the quantitative format consumed by existing Schur/pivot smoothing branches rather than being a merely qualitative statement.

## 6. What changed relative to the preceding B08 run

The prior B08 theorem treated `C=D+E` only while `||E||` stayed inside an operator-norm perturbation budget. This report handles the opposite regime by **not** trying to regard the large defect as an adversarial error. Instead it aggregates its Frobenius energy over a random original-coordinate cut, turns high stable rank into ridge effective dimension, and uses the fact that the selected large-eigenvector core has rank only three across every cut.

The resulting source-valid trichotomy is:

- small off-diagonal residual norm -> partner theorem closes continuously;
- large off-diagonal residual with `sr(E)>=30` -> ridge theorem closes continuously unless a physical cross row has universal size;
- the only nonlocalized large-defect remainder left is `sr(E)<30`.

This is a materially different mechanism from the preceding small-perturbation run and directly advances `QFORM-DIFFUSE-LARGE-DEFECT-AGGREGATION-v1`.

## 7. First remaining implication

The next B08 debt is now

### `QFORM-DIFFUSE-LOW-STABLE-RANK-OR-LOCALIZED-CLOSURE-v1`

Under the diffuse selected-frame condition (3.1), close the two outputs not already paid above:

1. `tau>1/40` and `sr(E)<30`: exploit the constant effective-rank structure of the off-diagonal residual by a product-preserving grouped-coordinate decomposition, without replacing stable rank by a false fixed-local-minor dichotomy;
2. the localized alternative (4.10): combine the universal cross-row scale with a selected-spectrum or physical-pivot resource to upgrade the existing quarter-negative-moment certificate to a uniform density bound.

The known singleton-plus-two-banks example prevents claiming that every remaining matrix must have a rank-three cross cut or a uniformly good small principal minor. Any closure must aggregate coordinate banks or use a source-valid pivot/ridge splice.

## 8. Correction compatibility and status

This proof does **not** use any of the live-refuted mechanisms: no law-uniform pointwise van-der-Corput decay, no post-rotation independence, no unrestricted fiber supremum, no fabricated conditional density cap, no fixed good principal minor, and no universal rank-three-cross-cut dichotomy. The only averaging is over physical coordinate cuts and is converted into a deterministic existence statement before the product-law ridge theorem is applied.

The full QFORM conjecture remains **OPEN**. Continuity is proved only on the closed branches (A) and (B1); it is not yet established on the unresolved alternatives (B2)/(C).

The companion `checks.py` / `check_results.json` verify only the threshold arithmetic `sr>=30 => theta_F>=6 => theta_B>=3`, the `<280` constant, and the localized-row floor. They do not replace the analytic proof above.
