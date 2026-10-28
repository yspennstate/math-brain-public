SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B12, 2026-09-23T13:47:01Z.
attacking: spectral-profile / participation-rank stability for adding arbitrary huge signed modes plus a dense spectral tail.

# account03/B12 — eroded spectral-profile stability for arbitrary added eigenvalues

Programme: `QFORM-DENSITY-3EIG-20260922`  
Run: `20260923T134701Z-qform-eigenvalue-r34`  
Assignment: Additional eigenvalue control  
Status: **PROVED SUPPORTING THEOREM / FULL QFORM OPEN**  
Continuity: **proved for the ridge branch below; not proved for the unrestricted target or the partner Schur fallback**  
Execution-memory status: `WITHOUT_VERIFIED_BRAIN`.

## 1. Exact contribution

Let `I,J` be disjoint sets of ORIGINAL independent coordinates. Write an actual final cross block as

`B = B0 + E`,

where `B0` is a reference cross block and `E` is the cross footprint of an arbitrary added symmetric spectral packet. Fix an integer `r>=0`, and put

`beta = s_{r+1}(E)`.

The first `r` singular directions of `E` are allowed to be completely arbitrary in magnitude and orientation. Define the **eroded baseline tail**

`u_j = ( s_{r+j}(B0) - beta )_+`,  `j=1,2,...`,

and its exact regularized profile

`Theta_u(gamma) = sum_j u_j^2/(gamma^2+u_j^2)`.

Then for every `gamma>0` with `Theta_u(gamma)>4`, the full ambient quadratic form has a continuous `C_0` density and

`||p_Q||_infinity <= [sqrt(e)/(2 gamma)] * Theta_u(gamma)/(Theta_u(gamma)-4)`.       (1.1)

Thus one may optimize the complete post-erosion singular profile rather than paying for only one hard threshold `s_{r+k}(B0)`. This is a genuine stability theorem for adding arbitrary smaller and larger eigenvalues: the first `r` added modes can be unbounded, and every remaining added mode is charged only through the single tail threshold `beta=s_{r+1}(E)`.

For a full symmetric update `R`, `E=R[I,J]` obeys

`s_{r+1}(E) <= s_{r+1}(R)`.                                    (1.2)

Hence (1.1) applies with any known upper bound `delta>=s_{r+1}(R)`, replacing `beta` by `delta` in the definition of `u_j`. The top `r` absolute eigenvalues of `R` may be arbitrarily large and of either sign.

No general rotation of the random variables is used. No quadratic remainder is treated as an independent convolution. The theorem acts on an actual original-coordinate cross block and inherits the arbitrary-self-block / arbitrary-outside-coupling scope of the ridge receiver.

## 2. Source pins and corrections

Fresh control before the derivation was read on `yspennstate/math-research-brain` main at observed commit

`987c70c9433591c2c1376a5db452d580aec9e78e`,


`f6b1c4c8517c1d59d13fc883ccc35012bae1fdd0`.

The analytic receiver is the completed one-scale ridge theorem:

`yspennstate/math-open-problems@9c1167db05c7b0f520f060796fde921ed769a4e7`

`proofnet24/QFORM-density/interactive/20260922T151048Z-ridge-window/REPORT.md`.

For an actual cross block `B=A[I,J]`,

`K_gamma = BB^T (gamma^2 I + BB^T)^(-1)`,  `theta_gamma=tr K_gamma`,

and if for some `1<=q<=2`

`max_i (K_gamma)_ii <= q/2`, `theta_gamma>2q`,

then the FULL ambient form has a continuous `C_0` density with

`||p_Q||_infinity <= sqrt(e)/(sqrt(2q) gamma) * theta_gamma/(theta_gamma-2q)`.     (2.1)

At `q=2`, the leverage condition is automatic because `0<=K_gamma<=I`.

The designated completed partner is account04/B12:

`yspennstate/math-open-problems@3948d77b0bde5af1bd37cd7c975d4f540eba901b`

`proofnet24/QFORM-density/fleet-2026-09-22/account04/B12/20260923T081758Z-account04-B12-complementary-schur-shield-r4/REPORT.md`.

Its actual equation-level use appears in Section 7.

Corrections respected: bounded density does not imply uniform pointwise quadratic-phase decay; rotations do not preserve independence; bounded projection density alone does not control an indefinite quadratic pushforward; naive fiber-sup integration can grow with dimension; the arbitrary-joint rank-three coarea and positive conditional-density-moment gates are false. None is used.

## 3. Deterministic profile erosion lemma

### Lemma 3.1

For real rectangular matrices `B0,E` of the same size, every `r>=0` and every `j>=1`,

`s_j(B0+E) >= (s_{j+r}(B0)-s_{r+1}(E))_+`.                 (3.1)

### Proof

Let `E_r` be the rank-`r` SVD truncation of `E`. Then

`rank(E_r)<=r`, `||E-E_r||_op=s_{r+1}(E)`.

A rank-`r` perturbation changes the singular-value counting function by at most `r`, so

`s_j(B0+E_r)>=s_{j+r}(B0)`.

One direct min-max proof intersects a `(j+r)`-dimensional lower-singular subspace for `B0` with `ker E_r`, losing at most `r` dimensions. Weyl's operator-norm perturbation inequality then gives

`s_j(B0+E) >= s_j(B0+E_r)-||E-E_r||_op
             >= s_{j+r}(B0)-s_{r+1}(E)`.

Taking the positive part gives (3.1). QED.

For a full symmetric update `R`, the cross compression is `E=P_I R P_J^T`. The ideal property gives

`s_j(E)<=||P_I|| s_j(R) ||P_J^T||=s_j(R)`,                 (3.2)

which proves (1.2).

## 4. Main exact-profile theorem

### Theorem 4.1 — `QFORM-ERODED-SPECTRAL-PROFILE-STABILITY-v1`

Under the setup of Section 1, for every `gamma>0` with `Theta_u(gamma)>4`,

`||p_Q||_infinity <= sqrt(e)/(2 gamma) * Theta_u(gamma)/(Theta_u(gamma)-4)`,       (4.1)

and `p_Q` has a continuous representative vanishing at infinity.

### Proof

Let the singular values of the final cross block `B` be `sigma_j`. Lemma 3.1 gives `sigma_j>=u_j`. Since

`x -> x^2/(gamma^2+x^2)`

is increasing on `[0,infinity)`,

`theta_gamma(B)
 = sum_j sigma_j^2/(gamma^2+sigma_j^2)
 >= sum_j u_j^2/(gamma^2+u_j^2)
 = Theta_u(gamma)`.                                         (4.2)

Apply the ridge theorem (2.1) with `q=2`. Its leverage hypothesis is automatic. The function `theta -> theta/(theta-4)` is decreasing on `(4,infinity)`, hence (4.2) gives (4.1). Continuity and the `C_0` conclusion are inherited from the source ridge theorem. QED.

This exact-profile compiler strictly contains the previous hard-threshold rank-budget theorem: if `u_1,...,u_k>=b>0`, then

`Theta_u(gamma)>=k b^2/(gamma^2+b^2)`

and optimizing recovers the earlier constant `3 k sqrt(3e)/(2(k-4)^(3/2)b)`.

## 5. Closed-form participation-rank corollary

The exact profile in Theorem 4.1 can be certified from only its second and fourth spectral moments. Put

`S = sum_j u_j^2`,
`T = sum_j u_j^4`.

Assume

`S^2 > 4T`.                                                  (5.1)

Equivalently, the participation ratio

`R_part = S^2/T`

is greater than four.

### Lemma 5.1 — Cauchy lower bound

For every `gamma>0`,

`Theta_u(gamma) >= S^2/(gamma^2 S + T)`.                    (5.2)

### Proof

On the positive `u_j`, apply Cauchy-Schwarz in Engel form:

`sum_j u_j^2/(gamma^2+u_j^2)
 = sum_j (u_j^2)^2/[u_j^2(gamma^2+u_j^2)]
 >= (sum_j u_j^2)^2 / sum_j u_j^2(gamma^2+u_j^2)
 = S^2/(gamma^2 S+T)`.

Zero terms contribute nothing. QED.

### Corollary 5.2 — `QFORM-ERODED-PARTICIPATION-RANK-STABILITY-v1`

If (5.1) holds, then with

`gamma_*^2 = (S^2-4T)/(12S)`                                (5.3)

one has a continuous `C_0` density satisfying

`||p_Q||_infinity
 <= [3 sqrt(3e)/2] * S^(5/2)/(S^2-4T)^(3/2)`.               (5.4)

### Proof

Let `D=S^2-4T>0`. By (5.2),

`Theta_u(gamma) >= L(gamma)=S^2/(gamma^2 S+T)`.

Whenever `D-4S gamma^2>0`, `L(gamma)>4`. Theorem 4.1 and monotonicity of `theta/(theta-4)` give

`||p_Q||_infinity
 <= sqrt(e)/(2gamma) * L/(L-4)
 = sqrt(e) S^2 / [2 gamma (D-4S gamma^2)]`.                 (5.5)

The denominator `gamma(D-4S gamma^2)` is maximized at `gamma^2=D/(12S)`, giving (5.4). QED.

This is more flexible than a flat singular threshold. It lets many unequal post-erosion directions cooperate through the participation ratio. The top `r` modes of the added spectrum remain completely free.

## 6. Concrete quantitative profile

Take `r=2`. Suppose the added symmetric update `R` has

`s_3(R)<=1/4`,

while the reference cross block has, beginning at singular index three,

`s_3,...,s_6 >= 5/4`,
`s_7,...,s_12 >= 21/20`.

The two largest absolute eigenvalues of `R` are unrestricted in magnitude, sign and orientation. After erosion by `delta=1/4`, the certified profile is

`u=(1,1,1,1,0.8,0.8,0.8,0.8,0.8,0.8)`.

Hence

`S=7.84`,
`T=6.4576`,
`S^2-4T=35.6352`,
`R_part=9.5183349851...`.

The closed-form scale is

`gamma_*=0.6154474065...`

and (5.4) gives

`||p_Q||_infinity <= 3.4655365469...`.                     (6.1)

Using the exact profile rather than the moment bound and minimizing (4.1) gives numerically

`gamma=0.6180940...`,
`Theta_u(gamma)=6.6514...`,
`||p_Q||_infinity <= 3.3457567531...`.                     (6.2)

For comparison, the previous flat-threshold theorem with `k=10`, `b=0.8` gives `3.6431937213...`. Thus the profile compiler obtains a real quantitative gain from the four stronger directions rather than discarding that information.

The numerical minimization is only evaluation of the already-proved deterministic formula (4.1), not empirical evidence for QFORM.

## 7. Required partner application at an actual inequality

Apply account04/B12's completed complementary-Schur shield to its five-coordinate physical core. In its notation the protected complementary block is

`D=diag(2,-2,2)`,

with `mu=2` and shear parameter `rho=1/2`, while an arbitrary symmetric `2x2` hostile packet `Theta` is allowed with no magnitude or sign restriction. The partner theorem gives

`ell(1/2)^2=(9-sqrt(17))/8`.

Now add a second, completely general dense symmetric local tail with

`||T||_op <= 1/3`.

The actual surviving physical singular gap is therefore

`g = 2 ell(1/2)^2 - 1/3
   = (9-sqrt(17))/4 - 1/3
   = 0.885890260262... >0`.                                (7.1)

For the five-coordinate physical receiver, the partner result gives

`||p_Q||_infinity
 <= 2 sqrt(30 pi)/g
 = 21.9172283481...`.                                      (7.2)

The hostile `2x2` spectral packet is arbitrarily large and signed; only the remaining dense tail is charged. This equation-level use is independent of the new ridge-profile branch. The partner branch proves essential boundedness in its stated scope; continuity is not claimed there.

## 8. Finite deterministic checks

A checker accompanies this report. It performs 10,000 randomized rectangular tests with

- `r=0,1,2,3`,
- an arbitrary large rank-`r` packet (singular magnitudes sampled up to order `10^3`),
- a full-rank residual tail with controlled operator norm,
- mixed rectangular dimensions.

It verifies (3.1) and the Cauchy profile bound (5.2). Recorded result: zero violations; the minimum numerical reserve margin was positive (`2.86e-4` in the seeded run). It also records the constants in Sections 6 and 7. These checks are sanity checks only; the proof is analytic.

## 9. Scope, what is new, and the next missing implication

The full QFORM conjecture remains **OPEN / NOT PROVED / NOT DISPROVED**.

The new result improves the additional-eigenvalue compiler in two ways:

1. it retains the entire eroded singular profile rather than collapsing it to the weakest of `k` reserve directions;
2. it gives a closed-form aggregate criterion `S^2>4T`, i.e. participation rank greater than four, after paying an arbitrary number `r` of completely uncontrolled added modes.

The obstruction is still structural. The bare target hypothesis supplies only three large global eigenvalues and does not force an original-coordinate cross footprint whose post-erosion participation ratio exceeds four. The next B12 implication is therefore a **three-global-modes to either participation-rank>4 cross footprint OR low-participation structured fallback** reduction. The low-participation side should be routed to physical-pivot / grouped-bank / hub / rank-two-half-Riesz mechanisms rather than paid by dimension-dependent fiber suprema.

Continuity is proved for Theorem 4.1 and Corollary 5.2 through the ridge receiver. Continuity is not established for the unrestricted target.

Repository transport and native brain ingestion remain separate; this run is `WITHOUT_VERIFIED_BRAIN`.
