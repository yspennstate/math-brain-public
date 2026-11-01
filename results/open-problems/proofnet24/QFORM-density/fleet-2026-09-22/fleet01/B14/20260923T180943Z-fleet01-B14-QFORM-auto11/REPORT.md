# fleet01 / B14 — conditional L^p-budget extreme localization

Run: `20260923T180943Z-fleet01-B14-QFORM-auto11`

Status: **NEW SUPPORTING LOCALIZATION THEOREM + TARGET-VALID PARTNER APPLICATION. FULL QFORM REMAINS OPEN.**

## 1. Scope and source pins

Owner programme: `QFORM-DENSITY-3EIG-20260922`, programme revision `2026-09-22.5`. Fresh brain control was resolved before publication; the last observed control head before this report was `yspennstate/math-research-brain@8c00034eafd094929df68cbad69dea27f987db44`, whose `AGENTS.md` still keeps all slots on the unrestricted rough-law QFORM target and keeps the rough single-hub `(SP)` route OPEN rather than proved.

Designated partner result actually used below:

- `fleet02/B14`, r41 report at `yspennstate/math-open-problems@6bc5027a5df12a2cd28130ded9fb53711eb90e39`, path
  `proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B14/20260923T173217Z-fleet02-B14-QFORM-r41/REPORT.md`.

I use only its completed pre-Jensen receiver inequality and its subprobability mass-homogeneity/whole-score localization. I do **not** use uniform pointwise quadratic Fourier decay, post-rotation independence, arbitrary-joint coarea, a bounded-diameter localization, or any fixed fragment-count statement.

Execution is `WITHOUT_VERIFIED_BRAIN`: repository reads/writes occurred, but no genuine native receiver-use event was established.

---

## 2. New lemma: exact conditional L^p-budget localization

The previous whole-law extreme reduction is not by itself tailored to fleet02/B14 r41, because r41 consumes an *integrated conditional L^p density budget*. The point of this run is that this budget itself admits an exact zero-loss extreme reduction.

### Theorem 2.1 (`QFORM-CONDITIONAL-LP-BUDGET-EXTREME-LOCALIZATION-v1`)

Fix `p>1`. Let `(Omega,nu)` be any probability space and let

`F : Omega x R^m -> R`

be measurable. For each `i`, fix a mass `m_i in (0,1]`, and let

`F_{m_i}={f_i: 0<=f_i<=1, int_R f_i=m_i}`.

For `f=(f_1,...,f_m)`, define the finite measure `M_f` on `Omega x R` by pushing

`nu(dz) prod_i f_i(u_i) du_i`

through `(z,u)->(z,F(z,u))`. Put `rho=nu tensor Lebesgue` and define

`B_p(f)= ||dM_f/d rho||_p^p`

when `M_f<<rho` with an `L^p(rho)` density, and `B_p(f)=+infinity` otherwise.

Then

`sup_{f_i in F_{m_i}} B_p(f_1,...,f_m)`

is exactly equal to

`sup B_p(1_{E_1},...,1_{E_m})`,

where each `E_i` is a **bounded finite union of intervals** of Lebesgue measure `m_i`.

There is no support-radius, diameter, component-count, separation, translation, or moment parameter in the identity. In particular the result allows the finite-union extreme supports to have arbitrarily many components and arbitrarily large diameter.

### Proof

#### Step 1: compactify one marginal without renormalizing

Let `0<=f<=1`, `int f=m`. For `R>0`, let

`delta_R=int_{|x|>R} f(x) dx`.

Choose any bounded interval `I_R` outside `[-R,R]` with length `delta_R` and set

`g_R=f 1_{[-R,R]} + 1_{I_R}`.

Then `0<=g_R<=1`, `int g_R=m`, and `g_R` is compactly supported. Moreover

`||g_R-f||_1 <= 2 delta_R -> 0`.

Thus tails and unbounded support can be removed with no renormalization and vanishing `L^1` error. The filler interval may be arbitrarily remote; its location never enters the later estimate.

#### Step 2: every compact cap-one fixed-mass density is approximated by finite mixtures of extreme sets

Let `g` be compactly supported, `0<=g<=1`, `int g=m`. For an integer `K>=1`, partition the line into grid cells of length

`h=m/K`.

Only finitely many cells meet the support. On each such cell `C_j`, replace `g` by its cell average

`a_j = h^{-1} int_{C_j} g`.

Then `0<=a_j<=1` and, because `int g=m=Kh`,

`sum_j a_j=K`.

Hence `a=(a_j)` lies in the hypersimplex

`P={a in [0,1]^N: sum_j a_j=K}`.

Every extreme point of `P` is a `0/1` vector with exactly `K` ones: if two coordinates were strictly between zero and one one could perturb them by `(+eps,-eps)`; because the coordinate sum is the integer `K`, an extreme point cannot have exactly one fractional coordinate. Therefore `P` is the convex hull of those `0/1` vectors.

Consequently the grid average is an **exact finite convex mixture**

`g_K = sum_s theta_s 1_{E_s}`,

where each `E_s` is a union of exactly `K` grid cells and therefore `|E_s|=Kh=m`. Standard `L^1` approximation by fine cell averages gives `||g_K-g||_1->0` as `K->infinity`.

Combining this with Step 1: every fixed-mass cap-one density is an `L^1` limit of finite convex mixtures of indicators of bounded finite-union sets of exactly the same mass.

#### Step 3: tensor the mixtures

For each coordinate choose such an approximation

`g_i^{(n)}=sum_{s_i} theta_{i,s_i}^{(n)} 1_{E_{i,s_i}^{(n)}}`.

Then the product density is the finite convex mixture

`prod_i g_i^{(n)} = sum_{s_1,...,s_m} (prod_i theta_{i,s_i}^{(n)}) prod_i 1_{E_{i,s_i}^{(n)}}`.

Also

`||prod_i g_i^{(n)}-prod_i f_i||_1 <= sum_i (prod_{k<i} m_k)(prod_{k>i} m_k) ||g_i^{(n)}-f_i||_1`,

so the product source measures converge in total variation. Pushforward cannot increase total variation, hence `M_{g^{(n)}} -> M_f` in total variation.

#### Step 4: convexity and lower semicontinuity of the L^p density functional

For a finite positive measure `mu` define

`Phi_p(mu)=||dmu/d rho||_p^p`

if an `L^p(rho)` density exists, and `+infinity` otherwise. The map `Phi_p` is convex, since `x->x^p` is convex.

It is also lower semicontinuous under total-variation convergence. Indeed, if `mu_n->mu` in total variation and `liminf Phi_p(mu_n)<infinity`, pass to a subsequence with uniformly bounded `L^p` densities `q_n`. Since `p>1`, `L^p(rho)` is reflexive, so a further subsequence converges weakly to some `q in L^p(rho)`. Testing against bounded simple functions supported on finite-`rho` sets, total variation identifies `mu=q rho`; weak lower semicontinuity then gives

`Phi_p(mu)<=liminf Phi_p(mu_n)`.

#### Step 5: conclude the exact supremum identity

Let `S` be the supremum of `B_p` over the stated extreme product laws. If `S=+infinity` there is nothing to prove. Otherwise, by convexity of `Phi_p`, every finite product mixture from Step 3 obeys

`B_p(g_1^{(n)},...,g_m^{(n)}) <= S`.

Step 4 gives

`B_p(f_1,...,f_m)<=liminf_n B_p(g_1^{(n)},...,g_m^{(n)})<=S`.

The reverse inequality is immediate because the extreme laws are admissible. This proves the theorem. `□`

### What this does and does not say

It is crucial that an extreme support `E_i` is kept **whole**. It may be a very disconnected finite union. The theorem does not give a bounded diameter and does not permit one to normalize its interval components and sum an absolute-value certificate afterward. That forbidden proof order is exactly where the known fragment losses occur.

---

## 3. Direct composition with completed fleet02/B14 r41

Partner r41 proves the following completed receiver rule. Let

`4/3<r<2`, `p=r/(r-1)`, `alpha=r-1`,

and suppose, conditional on a product driver `Z=z`, a core variable `T_z` is independent of an independent cap-one scalar receiver `W`. For

`Q=T_Z+s(Z)+d W^2 + (2 b^T Z+e) W`,

write

`R0=sqrt(d^2+||b||_2^2)`.

If

`B_p = int ||p_{T_z}||_p^p dnu(z)<infinity`,

then r41 gives

`||p_Q||_infty`
` <= 2^{3 alpha/(2r)} (2-r)^(-1/r) R0^{-alpha/r} B_p^{1/p}`.      (3.1)

Therefore Theorem 2.1 has an immediate exact compiler consequence:

### Corollary 3.1 (`QFORM-RECEIVER-BUDGET-ZERO-LOSS-COMPILER-v1`)

If the conditional core budget satisfies

`B_p <= K^p`

for every bounded finite-union extreme product law of the core coordinates, then the **same** inequality holds for every arbitrary cap-one product core law, and (3.1) gives

`||p_Q||_infty`
` <= 2^{3 alpha/(2r)} (2-r)^(-1/r) R0^{-alpha/r} K`               (3.2)

with no additional localization factor.

Thus one may localize arbitrary rough core laws at the `L^p`-budget level *before* invoking the singular receiver estimate, while leaving the active score `2b^T Z+e` aggregated. Arbitrary core translations, disconnected supports, tail locations and missing moments do not change the constant.

Partner r41 also proves the subprobability score estimate

`||p_eta||_infty <= K 2^{2 alpha/r}(2-r)^(-1/r) m^{1/r} L^{alpha/r}`,      (3.3)

where a driver piece has mass `m` and its score pushforward has density cap `L`. Whenever the **unnormalized** score cap retains fragment mass, `L<=m L0`, the right side is exactly linear in `m`, because

`m^{1/r}(m L0)^{alpha/r}=m^{(1+alpha)/r}L0^{alpha/r}=m L0^{alpha/r}`.

Hence countably many remote driver pieces may be summed with zero tax. This is the precise mass-homogeneity interface needed to combine the present core localization with r41.

---

## 4. Actual target-valid inequality: diffuse receiver bank

Here is a pure quadratic-form family to which the completed partner result applies and for which the diffuse bank matters.

Let `X,Y,W,Z_1,...,Z_m` be mutually independent real random variables with densities at most one. Let `H` be any symmetric `m x m` matrix, `b in R^m`, and `c,d in R`. Consider

`Q = 2 c X Y + Z^T H Z + d W^2 + 2 (b^T Z) W`.                 (4.1)

No moments or support assumptions are imposed. The law of every coordinate may be arbitrarily fragmented or unbounded.

### 4.1 Core L^p budget

For arbitrary shifts `a,beta` and every `p>1`, independent cap-one `X,Y` satisfy

`||p_{2c(X-a)(Y-beta)}||_p <= p |c|^{-1+1/p}`.               (4.2)

Indeed, with `gamma=1-1/p`, conditional on `Y-beta=y`, the `L^p` norm of the scaled `X-a` density is at most

`(2|c||y|)^(-gamma)`.

Minkowski and the sharp cap-one bathtub bound

`E |Y-beta|^{-gamma} <= 2^gamma/(1-gamma)`

then give

`||p||_p <= (2|c|)^(-gamma) 2^gamma/(1-gamma)`
` = p |c|^{-gamma}`,

which is (4.2). This is uniform in the shifts and hence remains true after arbitrary outside original-coordinate variables are conditioned out.

Taking `T_z=2cXY`, `s(z)=z^T H z`, the conditional budget in (3.1) is therefore

`B_p^{1/p} <= p |c|^{-1+1/p}`.                              (4.3)

Theorem 2.1 shows that the identical budget is obtained if the rough `X,Y` laws are reached as limits of bounded finite-union extreme laws; no componentwise normalization is required.

### 4.2 Apply partner r41

Substitute (4.3) into (3.1). Since `1-1/p=1/r`,

`||p_Q||_infty <= [r/(r-1)] 2^{3(r-1)/(2r)} (2-r)^(-1/r)`
`                  * |c|^(-1/r) * (d^2+||b||_2^2)^(-(r-1)/(2r))`.      (4.4)

At `r=3/2`, `p=3`, this becomes the explicit inequality

`||p_Q||_infty <= 3*2^(7/6) |c|^(-2/3) (d^2+||b||_2^2)^(-1/6)`.        (4.5)

Numerically, `3*2^(7/6)=6.734772289856...`.

This is a genuine use of the completed fleet02/B14 r41 *global* receiver theorem: the third spectral direction may be spread diffusely over many coefficients of `b`; no single pair coefficient needs to be order one.

### 4.3 Verify the exact three-large-eigenvalue target

The coefficient matrix of (4.1) is the direct sum of

`B_hyp=[[0,c],[c,0]]`

and

`S=[[H,b],[b^T,d]]`.

The first block has eigenvalues `+|c|,-|c|`. Also, for the receiver basis vector `e_W`,

`||S e_W||_2 = sqrt(d^2+||b||_2^2)=R0`,

hence

`||S||_op >= R0`.

Because `S` is symmetric, it has an eigenvalue of modulus at least `R0`. Therefore, whenever

`|c|>=1` and `sqrt(d^2+||b||_2^2)>=1`,

the active matrix already has at least three eigenvalues of modulus at least one. Thus (4.5) yields the universal strict-target bound

`||p_Q||_infty <= 3*2^(7/6) < 6.735`.                        (4.6)

The useful point is the diffuse case, for example

`d=0`, `b=(1/sqrt(m),...,1/sqrt(m))`.

Then every physical receiver-driver entry tends to zero with `m`, but `||b||_2=1`, so (4.6) stays dimension-free. This is outside any argument requiring a single order-one receiver-driver coefficient.

### 4.4 Arbitrary outside translations cost zero

Add any further independent cap-one original-coordinate vector `R`, with an arbitrary symmetric outside block and arbitrary cross-couplings from `R` to `X,Y,Z,W`. Condition on `R=r`. Those couplings only create:

- arbitrary translations of the hyperbolic core `X,Y`;
- an arbitrary affine term in `Z`, absorbed into `s_r(Z)`;
- an arbitrary scalar shift of the receiver score;
- an additive constant.

Both (4.2) and partner r41 are uniform in those shifts. Hence the same constant (4.5) holds after averaging over `R`, with no support or moment assumption on `R`. The active principal block from (4.1) remains a principal block of the full matrix, so the three-large-eigenvalue count persists by interlacing.

### 4.5 Remote-fragment stress test

Suppose any active marginal is a cap-one density supported on many extremely remote pieces. Theorem 2.1 says to approximate it by convex mixtures of **whole** bounded finite-union extreme laws. For each normalized extreme component the same core/score estimates hold. If one instead records the mixture as unnormalized pieces, partner r41's (3.3) is linear in the mixture mass once the unnormalized score cap `L<=mL0` is retained. Thus the final constant is unchanged after summing.

This is categorically different from partitioning one certificate-active extreme set into its interval components and renormalizing those components first. Partner r41's own exact-target obstruction shows that this latter proof order can create a power loss even though the underlying law has not changed.

---

## 5. Why the theorem is useful for the full programme

The new lemma removes a specific analytic localization debt. Whenever a future full-QFORM branch can be organized as

`conditional core L^p budget -> completed receiver compiler`,

one does **not** need to prove that budget directly for every unbounded/fractured cap-one law. It is enough to prove it on bounded finite-union extreme product laws, with no bound on component count or diameter. Convexity plus total-variation lower semicontinuity restores the arbitrary laws with exactly the same constant.

The proof-order rule is now:

1. keep every certificate-active finite-union extreme support whole;
2. pay the conditional `L^p` budget or score estimate at probability/subprobability level;
3. only then average the extreme components or outside pieces.

This simultaneously handles arbitrary translations, distant fragments and unbounded supports without introducing moments.

The remaining full-QFORM obstruction is **not** support localization. Starting only from `s_3(A)>=1`, one still needs an exhaustive product-preserving structural reduction that forces either a receiver/core configuration with a quantitative whole-score parameter, or one of the completed ridge/volume/mixed-hub/grouped-bank exits. The diffuse/no-good-pivot geometries not covered by those alternatives remain unpaid. I do not claim the unrestricted theorem or a counterexample.

---

## 6. Audit notes

- No uniform pointwise quadratic Fourier decay was used.
- No independence after an orthogonal rotation was used.
- No arbitrary-joint coarea estimate was used.
- No bounded support diameter was claimed.
- No fixed number of support components was claimed.
- The `L^p` lower-semicontinuity argument is at the **joint `(z,t)` measure** level, so it does not assume pointwise convergence of conditional densities.
- The target check in Section 4 is a genuine principal-block/eigenvalue argument, not a projection-only surrogate.
- The result is a supporting theorem and has not yet received an independent end-to-end review.

Full unrestricted QFORM status: **OPEN**.
