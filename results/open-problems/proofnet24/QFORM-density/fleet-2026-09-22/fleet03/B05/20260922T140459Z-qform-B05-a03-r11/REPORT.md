# fleet03/B05 — hidden-bank coarea and a determinant-safe pure-transverse subbank

**Programme:** `QFORM-DENSITY-3EIG-20260922`, owner revision `2026-09-22.5`  
**Run:** `20260922T140459Z-qform-B05-a03-r11`  
**Assignment:** Quadratic coarea bound  
**Classification:** `ESSENTIAL_STEP_APPLIED / SUPPORTING THEOREM PROVED / FULL TARGET OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`; `full_brain_connected=false`.

## 1. Exact scope and correction-aware starting point

The owner target is the full arbitrary-product-law statement: for every dimension, every independent real coordinate family with probability densities `0<=f_i<=1`, and every real symmetric matrix `A` having at least three eigenvalues of modulus at least one, prove a dimension-, law-, sign-, and matrix-independent essential density bound for `Q=X^T A X`, or give a valid counterexample. Continuity is a separate stronger request.

This report does **not** use law-uniform pointwise Fresnel decay, independence after spectral rotation, a fiber supremum, a single good cross minor, a single Schur rank-two extraction, or a bounded conditional density as a substitute for genuine independence. In particular it respects `QFORM-CONDITIONAL-CAP-NOT-INDEPENDENCE-v1`: arbitrary correlation can align `2SY+Z^2` into the logarithmically singular product `2YU`.

The immediately preceding B05 theorem, source

`yspennstate/math-open-problems@bf7bff5c9b11cf495ccbcb09ef48549fd9c0d409:proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B05/fleet03-B05-20260922T133738Z-qform-r12/REPORT.md`,

proved a universal determinant-scale half-Riesz estimate for every rank-two product quadratic form and reduced the exact-rank-three coarea obstruction to the **first** leverage-heavy, near-isotropic physical pivot. This run changes mechanism: instead of another Schur/half-Riesz cascade, it uses a direct near/far coarea split in the hyperbolic variable while preserving one genuinely independent square-producing original-coordinate bank.

The assigned partner is `fleet04/B05`. A fresh check of both its canonical QFORM proof root and its shared QFORM handoff root found no completed current-programme artifact, so no assigned-partner theorem is fabricated. The closest completed compatible fleet04 result actually applied below is

`fleet04/B20`, `QFORM-AGGREGATE-HYPERBOLIC-SQUARE-v1`, source-read at

`yspennstate/math-open-problems@c233995d6abf7574b8b1a876cac244b1b91e3c38:proofnet24/QFORM-density/fleet-2026-09-22/fleet04/B20/20260922T132134Z-fleet04-B20-QFORM-r1/REPORT.md`.

It gives, for three independent scalar banks of density caps `M_U,M_V,M_Z`,

`||p||_infinity <= 4 M_Z sqrt(M_U M_V)/sqrt(|ab|)`

for a hyperbolic term `2aUV` plus an arbitrary `V`-dependent term and a shifted square `b(Z+theta(V))^2`, uniformly after conditioning on independent outside coordinates.

Two further completed sources are used:

- `fleet02/B04`, `QFORM-LINEAR-FORM-L2-CAP-v1`, source
  `yspennstate/math-open-problems@f1c1b2dd3a0b2ca4c821505d6ae9100f30383906:proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B04/fleet02-B04-20260922T125623Z-r11-product-fourier/REPORT.md`, proving
  `M(sum c_j X_j)<=sqrt(2)/||c||_2` for arbitrary independent density-cap-one coordinates;
- `fleet02/B10`, source
  `yspennstate/math-open-problems@11c9ae19edfd07e3a0bd4053a910667c20e721ab:proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B10/20260922T130225Z-b10-qform-r11/REPORT.md`, proving the heavy-isotropic independent-leakage branch and the exact counterexample showing that conditional caps do not replace independence.

## 2. Applying the fleet04 aggregate-bank theorem exposes the remaining anisotropy tax

Consider the heavy-isotropic rank-three normalization developed in the completed B10 work. Let

`A=U Lambda U^T`, `U^T U=I_3`, `|lambda_k(Lambda)|>=1`,

and let a leverage-heavy physical row be

`u_i=sqrt(c)e`, `c>1/2`, `e^T Lambda e=0`.

Set `beta=P_(e^perp)Lambda e`, `B=||beta||>0`, choose `f=beta/B` and a unit `g perpendicular e,f`. In the spectral basis `(e,f,g)`,

`Lambda=[[0,B,0],[B,r,s],[0,s,tau]]`,

hence

`det Lambda=-B^2 tau`, so `tau!=0` and

`B^2 |tau|=|det Lambda|>=1`.                                      (2.1)

Write the residual physical rows as

`u_j=s_j e+y_j f+z_j g`, `j!=i`,

and put

`T=sum s_j X_j`, `Y=sum y_j X_j`, `Z=sum z_j X_j`.

Parseval gives

`sum s_j^2=1-c`, `sum y_j^2=sum z_j^2=1`,
`sum s_j y_j=sum s_j z_j=sum y_j z_j=0`.                            (2.2)

The quadratic form is exactly

`Q=2B(sqrt(c)X_i+T)Y +(r-s^2/tau)Y^2
    +tau(Z+(s/tau)Y)^2`.                                            (2.3)

In the stronger old subcase where the leakage bank `T`, the `Y` bank, and an independent square-producing `Z` bank are supported on disjoint original-coordinate sets, the fleet04/B20 theorem applies directly. If the usable `Z` bank has coefficient norm `rho`, the source-valid linear-form theorem gives

`M(sqrt(c)X_i)<=c^(-1/2)`, `M(Y)<=sqrt(2)`, `M(Z)<=sqrt(2)/rho`.

Thus the fleet04 theorem gives the actual inequality

`||p_Q||_infinity
 <= 4*2^(3/4)c^(-1/4) rho^(-1) / sqrt(B|tau|)`.                      (2.4)

This is useful but is **not determinant-safe** under only (2.1): substituting `D=B^2|tau|` turns its spectral factor into `B^(1/2)D^(-1/2)`, which can grow with `B` even though `D>=1`. This identifies a precise obstruction in the partner inequality: the symmetric `|ab|^-1/2` payment spends too much of the square coefficient and too little of the hyperbolic coefficient for the isotropic determinant identity `B^2|tau|`.

The theorem below changes the split so that the exponents become exactly `|a|^-2/3|b|^-1/3`, matching `B^2|tau|`.

## 3. Main new theorem: a hidden correlated bank is harmless if the square bank remains independent

### Theorem 3.1 — `QFORM-HIDDEN-BANK-HYPERBOLIC-SQUARE-v1`

Let `U,Z` be independent real random variables, and let `(V,S)` be an arbitrary random pair/vector, such that the pair `(U,Z)` is independent of `(V,S)`. No independence between `V` and `S` is assumed. Suppose `U,V,Z` have probability densities satisfying

`M(U)<=M_U`, `M(V)<=M_V`, `M(Z)<=M_Z`.

Let `a,b!=0`, and let `H(v,s), theta(v,s)` be arbitrary measurable real functions. Define

`W=2aUV+H(V,S)+b(Z+theta(V,S))^2`.                                  (3.1)

Then `W` is absolutely continuous and

`boxed{ ||p_W||_infinity
 <= 3*2^(2/3) (M_U M_V M_Z)^(2/3)
       |a|^(-2/3)|b|^(-1/3). }`                                     (3.2)

Equivalently, every interval `I` satisfies the coarea/small-ball estimate

`P(W in I)<=3*2^(2/3)(M_U M_V M_Z)^(2/3)
 |a|^(-2/3)|b|^(-1/3)|I|`.                                          (3.3)

The hidden variable `S` may contain arbitrarily many original coordinates and may determine `V`; only the two scalar sources `U,Z` must remain genuine independent banks.

### Proof

Let `m(v)` be the density of `V`; `m(v)<=M_V`. Since `V` is absolutely continuous, `P(V=0)=0`. Fix `(v,s)` with `v!=0`.

There are two conditional density bounds, and the proof deliberately uses a different one on small and large `|v|`.

**Near bound.** First condition on `U=u`. Translation does not affect density caps. The pushforward of `Z` by `z -> b(z+theta)^2` has density bounded by

`M_Z |b|^(-1/2) [sigma w]_+^(-1/2)`, `sigma=sign(b)`.                 (3.4)

For a probability density `f<=M_U`, the one-sided bathtub inequality gives, for every real `q` and every nonzero `d`,

`int f(u)[q-du]_+^(-1/2)du <= 2 sqrt(M_U/|d|)`.                       (3.5)

With `d=2av`, (3.5) becomes

`int f_U(u)[q-2avu]_+^(-1/2)du
 <= sqrt(2M_U)|a v|^(-1/2)`.                                         (3.6)

Hence, uniformly in `s` and the values of `H,theta`,

`p_(W|V=v,S=s)(t)
 <= K |v|^(-1/2)`,                                                    (3.7)

where

`K=sqrt(2M_U) M_Z /sqrt(|ab|)`.                                      (3.8)

**Far bound.** Instead condition on `Z`. For fixed `z,v,s`, (3.1) is affine in `U` with slope `2av`, so

`p_(W|V=v,S=s)(t)<=M_U/(2|a v|)`.                                    (3.9)

Now split at an arbitrary `R>0`. Mixing the conditional laws and using only the **marginal** density of `V`, not a conditional cap, gives

`p_W(t)
 <= K int_(|v|<=R) m(v)|v|^(-1/2)dv
    + M_U/(2|a|R)`

` <= 4 K M_V sqrt(R)+M_U/(2|a|R)`.                                  (3.10)

Write

`A0=4 sqrt(2M_U) M_Z M_V /sqrt(|ab|)`,
`D0=M_U/(2|a|)`.

The minimum of `A0 R^(1/2)+D0 R^(-1)` occurs at

`R=(2D0/A0)^(2/3)`

and equals

`3*2^(-2/3) A0^(2/3)D0^(1/3)`

`=3*2^(2/3)(M_U M_V M_Z)^(2/3)|a|^(-2/3)|b|^(-1/3)`.                 (3.11)

This proves (3.2). For almost every `(v,s)` the conditional law has a density; the uniform integrable mixture bound above supplies an unconditional density. Integrating that density over an interval proves (3.3). QED.

### Why this does not violate the live conditional-cap correction

The fleet02/B10 falsifier has a correlated variable `S=-Z^2/(2Y)+U` designed so that the same `Z` responsible for square smoothing is absorbed into the hidden hyperbolic variable. Theorem 3.1 explicitly forbids that collapse: its square supplier `Z` is an independent bank, while the hidden variable may correlate arbitrarily only with `V`. Thus (3.2) uses genuine original-coordinate independence, not a conditional-density surrogate.

## 4. Heavy-isotropic corollary with a partially pure transverse bank

The theorem applies to (2.3) under a strictly weaker condition than full separation of all three residual banks.

Let `K` be **any** set of residual original-coordinate indices such that

`s_k=0` and `y_k=0` for every `k in K`,                               (4.1)

and define its transverse mass

`rho=(sum_(k in K) z_k^2)^(1/2)`.                                    (4.2)

Assume `rho>0`. Split

`Z=Z_K+Z_J`,
`Z_K=sum_(k in K) z_kX_k`, `J=({j!=i}\K)`.

Then `T` and `Y` depend only on `J`, while `Z_K` uses only `K`; hence `sqrt(c)X_i`, `Z_K`, and the whole hidden `J`-bank have the exact independence structure of Theorem 3.1. The remaining overlapping transverse part `Z_J` is harmless because it can be absorbed into the arbitrary square shift.

Specifically put

`U=sqrt(c)X_i`, `V=Y`, `S=(X_j)_(j in J)`,

`H(V,S)=2BTY+(r-s^2/tau)Y^2`,

`theta(V,S)=Z_J+(s/tau)Y`.

Then (2.3) has exactly the form (3.1) with `a=B`, `b=tau` and independent square bank `Z_K`.

The source-valid linear-form cap gives

`M_U<=c^(-1/2)`,
`M_V<=sqrt(2)` because `sum y_j^2=1`,
`M_(Z_K)<=sqrt(2)/rho`.                                                (4.3)

Applying (3.2) and the determinant identity (2.1) yields

`||p_Q||_infinity
 <=3*2^(4/3)c^(-1/3)rho^(-2/3)|det Lambda|^(-1/3)`.                   (4.4)

Under the target normalization `c>1/2`, `|det Lambda|>=1`,

`boxed{ ||p_Q||_infinity < 3*2^(5/3) rho^(-2/3)
       =9.5244063118... rho^(-2/3). }`                                (4.5)

Thus any heavy-isotropic exact-rank-three branch with a dimension-free amount `rho>=rho_0>0` of **pure transverse square-bank mass** is uniformly closed, even if the leakage `T` and hyperbolic variable `Y` are maximally dependent through the same original-coordinate bank.

The extreme `rho=1` case has the same `<9.525` cap as the previously completed independent-leakage theorem, but the hypotheses are different: here `T` may overlap arbitrarily with `Y`.

This is a genuine coarea result, not an easy diagonal subclass: the form is indefinite, spectrally rotated, and the hidden bank may be arbitrarily high-dimensional with arbitrary bounded-density product laws.

## 5. Precise remaining geometric factor

Define the maximal pure-transverse mass in the normalized heavy-isotropic state by

`rho_pure^2 = sum_{j: s_j=0 and y_j=0} z_j^2`.                         (5.1)

The present theorem pays exactly `rho_pure^(-2/3)`. It therefore isolates the first still-unpaid branch of this coarea mechanism:

**`QFORM-ISOTROPIC-MIXED-TRANSVERSE-BANK-v1` — OPEN.** Handle heavy `c in (1/2,1)`, `e^T Lambda e=0`, when `rho_pure` is arbitrarily small or zero, so essentially every coordinate carrying transverse `z`-mass also carries leakage `s`-mass or hyperbolic `y`-mass. One must aggregate this mixed bank before conditioning; replacing it by a conditional cap is refuted, and averaging inverse local minors loses dimension.

A useful next attack is a two-bank version of Theorem 3.1 in which the square supplier shares coordinates with `V,S` but the coefficient triples obey the exact Parseval orthogonality in (2.2). The missing factor is no longer a second Schur pivot or a rank-two half-Riesz potential; it is quantitatively the loss of a genuinely independent transverse component.

This branch is separate from the arbitrary-additional-spectrum interaction debt in the full target. The theorem here is exact-rank-three supporting mathematics and must not be promoted to a full solution.

## 6. Status and integrity

**Proved:**

- `QFORM-HIDDEN-BANK-HYPERBOLIC-SQUARE-v1`, the direct small-ball/coarea inequality (3.2)--(3.3);
- `QFORM-PURE-TRANSVERSE-SUBBANK-COAREA-v1`, bound (4.4), including arbitrary signs and arbitrary dependence inside the hidden residual bank;
- the precise `rho_pure^(-2/3)` price of this mechanism.

**Actually applied peer mathematics:**

- fleet04/B20's aggregate hyperbolic-square theorem was applied in (2.4), exposing its anisotropy tax and motivating the determinant-compatible exponent repair;
- fleet02/B04's linear-form cap was applied in (4.3);
- fleet02/B10's correction is used to delimit the independence hypothesis rather than being ignored.

**Not proved:**

- the mixed-transverse branch `rho_pure ->0`;
- a complete exact-rank-three theorem;
- arbitrary additional nonseparable spectral directions;
- the full owner QFORM conjecture;
- continuity of the density in the new branch. The theorem proves absolute continuity and an essential `L^infinity` bound only.

No assigned `fleet04/B05` current-QFORM artifact was available at the final prepublication source check. No native mathematical-memory receiver was used; repository reads/writes are not native ingestion. Execution therefore remains `WITHOUT_VERIFIED_BRAIN`.
