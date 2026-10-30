SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet03, slot B08, 2026-09-24T09:23:59Z.
attacking: the punctured double-alignment tube by transferring the two literal crossing singular planes back to the exact child two-frame, then decomposing global star misalignment into bankwise residual and a source-safe split-slope mismatch.

# fleet03/B08 — split-alignment Pythagoras and tunable collar sharpening

Programme: `QFORM-DENSITY-3EIG-20260922`  
Run: `20260924T092359Z-fleet03-B08-qform-diffuse-r51`  
Assignment: diffuse eigenvector case  
Status: **NEW SUPPORTING STRUCTURAL ROUTER + NEW TUNABLE CONTINUOUS PAYMENT + DESIGNATED PARTNER APPLIED / FULL QFORM OPEN**  
Execution: **WITHOUT_VERIFIED_BRAIN**

The unrestricted conjecture remains OPEN. The new crossing-payment branch below has a continuous `C_0` density. The split-alignment identities and the designated-partner small-ball estimate do not by themselves prove continuity or a density bound on the final collar. No Gaussian, log-concavity, moment, compact-support, connected-support, post-rotation-independence, arbitrary-joint coarea, fiber-supremum, or law-uniform pointwise quadratic-phase decay assumption is used.

## 1. Source-pinned state

The immediate same-slot input is

- `yspennstate/math-open-problems@19c12072f7e67266ce894042034bcabb9c376bea`,
- `proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B08/20260924T061920Z-fleet03-B08-qform-diffuse-r51/REPORT.md`.

It gives, after earlier payments, an original-coordinate hub/child decomposition

`A=[[a,b^T],[b,C]]`,

with the child written

`C=V Lambda V^T+E`,

where `V in R^(m x 2)` has orthonormal columns,

`m_2=s_2(C)>=m_0 L`, `m_0=sqrt(47/48)`,

`r=s_3(C)=||E||op<L/4096`,

and

`max_i ||V_{i,*}||^2<=1/16`.

A physical Bernoulli half-cut `J disjoint_union K` has already been selected so that

`G:=V_J^T V_J >= g I_2`,
`H:=V_K^T V_K=I_2-G >= g I_2`,

with

`g=1/2-1/(4 sqrt(2))=0.32322330470336313...`.

For the literal child crossing

`D=C[J,K]`

one has

`s_2(D)>=s_0 L`,
`s_3(D)<L/4096`,

where

`s_0=g sqrt(47/48)-1/4096`
`   =0.31959453358755213...`.

Let `R_2(D)` and `L_2(D)` be the top-two right and left singular spaces and put

`d_K=dist(b_K,R_2(D))`,
`d_J=dist(b_J,L_2(D))`.

The prior run used threshold `L/64`: if either distance is that large, the marginal-free third-compound theorem pays the form; otherwise both augmented literal crossings are close to rank two.

The third-compound receiver itself was reread at

- `proofnet24/QFORM-density/fleet-2026-09-22/fleet01/B04/20260923T194715Z-fleet01-B04-QFORM-auto11-r18/REPORT.md`.

For every literal original-coordinate crossing `B`,

`||p_Q||_infinity <= 6^(4/3) e_3(BB^T)^(-1/6)`,

with `p_Q in C_0`, while retaining arbitrary same-bank phases.

The designated fleet04/B08 source actually applied below is

- `yspennstate/math-open-problems@f324267086411b9725aa0733e108ab6efc2e760a`,
- `proofnet24/QFORM-density/fleet-2026-09-22/fleet04/B08/20260924T081435Z-fleet04-B08-QFORM-r3/REPORT.md`.

Its derivative-splitting theorem states that for cap-one `X` independent of `Y`, if `Gamma(Y)` has density cap `K`, then for arbitrary `R(Y)`,

`sup_t P(|a X^2+X Gamma(Y)+R(Y)-t|<eps) <= 4 sqrt(2 K eps)`.

The fresh correction `QFORM-NONZERO-PUNCTURE-FIBERWISE-TMINUS1-FALSE-v1` was also consumed before publication: no fiberwise `|t|^-1` continuation through a nonzero puncture is used here.

## 2. A tunable third-compound payment

The previous `L/64` alignment threshold is not intrinsic. Fix any `eta>0`. If

`d_K>=eta L`,

then the star-over-rank-two exterior-algebra inequality from the immediate predecessor gives

`e_3(B_K B_K^T) >= s_2(D)^4 d_K^2 >= s_0^4 eta^2 L^6`,

for the literal crossing `B_K=[b_K^T;D]`. Therefore

`boxed: ||p_Q||_infinity <= C_eta/L,`

`C_eta:=6^(4/3) s_0^(-2/3) eta^(-1/3)`,

and `p_Q in C_0(R)`. The transpose argument is identical if `d_J>=eta L`.

Hence for every fixed `eta`, an unpaid branch may assume simultaneously

`d_J<eta L`, `d_K<eta L`.

The value used below is

`eta=2^(-20)=9.5367431640625e-7`,

for which

`boxed: C_eta=2369.5656377954524.`

Thus shrinking the alignment tube by more than four orders of magnitude from the original `1/64` gate costs only a finite universal constant.

## 3. Transfer from the literal crossing planes to the exact child frame

The important point is to avoid a perturbative statement about the random quadratic form. Only deterministic coefficient subspaces are compared.

Write

`D_0=V_J Lambda V_K^T`, `F=E[J,K]`, so `D=D_0+F`, `||F||op<=r`.

Let `z_K` be the orthogonal projection of `b_K` onto `R_2(D)`. Because `z_K` lies in the top-two right singular subspace, there is `x` in the top-two left singular subspace such that

`D^T x=z_K`, `||x||<=||z_K||/s_2(D)`.

But `D_0^T x` lies in `range(V_K)`. Therefore

`dist(z_K,range(V_K)) <= ||F^T x||`
`                         <= [r/s_2(D)] ||z_K||`.

Consequently

`e_K:=dist(b_K,range(V_K))`
` <= d_K+[r/s_2(D)](||b_K||+d_K)`.

The same argument on the left gives

`e_J:=dist(b_J,range(V_J))`
` <= d_J+[r/s_2(D)](||b_J||+d_J)`.

On the live thin-puncture branch,

`q:=r/s_2(D) < q_*:=1/(4096 s_0)`
` =0.0007639073868361965...`.

Hence, writing `e=(e_J^2+e_K^2)^(1/2)`,

`boxed: e <= (1+q_*) (d_J^2+d_K^2)^(1/2)+q_* ||b||.`

In particular, under the tunable unpaid gate `d_J,d_K<eta L`,

`boxed: e < (1+q_*) sqrt(2) eta L+q_* ||b||.`

No Wedin/Davis-Kahan theorem is needed for this transfer; it is a direct singular-vector representation plus the deterministic coefficient error `F`.

## 4. Exact split-alignment Pythagoras identity

This is the main new structural identity.

Define the bankwise least-squares coefficients

`c_J=G^(-1) V_J^T b_J`,
`c_K=H^(-1) V_K^T b_K`,

and orthogonal residuals

`r_J=b_J-V_J c_J`,
`r_K=b_K-V_K c_K`.

Thus `||r_J||=e_J`, `||r_K||=e_K`. Put

`delta=c_J-c_K`,
`beta=dist(b,range(V))`.

### Lemma `QFORM-SPLIT-ALIGNMENT-PYTHAGORAS-v1`

One has the exact identity

`boxed: beta^2=e_J^2+e_K^2+delta^T G H delta.`

Proof. Any global vector in `range(V)` has the form `(V_J c,V_K c)`. Orthogonality of the bankwise least-squares residuals gives

`beta^2=e_J^2+e_K^2+min_c [(c_J-c)^T G(c_J-c)+(c_K-c)^T H(c_K-c)].`

Since `G+H=I`, the minimizer is

`c_*=G c_J+H c_K`.

Writing `delta=c_J-c_K`,

`c_J-c_*=H delta`, `c_K-c_*=-G delta`.

Because `H=I-G`, the matrices `G,H` commute, and the minimum equals

`delta^T(HGH+GHG)delta=delta^T GH delta`.

This proves the identity.

Since every eigenvalue of `G` lies in `[g,1-g]`,

`g(1-g) I <= GH <= (1/4) I`.

Therefore

`boxed: g(1-g)||delta||^2 <= beta^2-e^2 <= (1/4)||delta||^2.`

This is an exact quantitative description of the difference between *global* alignment and two independent bankwise alignments. The only additional degree of freedom is the coefficient mismatch `delta`.

## 5. Collapse of the double-alignment tube

Combine Sections 3 and 4. If

`beta > 2 e`,

then

`beta^2-e^2 > (3/4) beta^2`.

Using `beta^2-e^2 <= ||delta||^2/4`,

`boxed: ||delta||>sqrt(3) beta.`

Otherwise `beta<=2e`, and the transfer bound yields

`boxed:
 beta <= 2(1+q_*) sqrt(2) eta L+2q_* ||b||.
}`

Thus the entire thin double-alignment state obeys the following trichotomy for every fixed `eta>0`:

1. **continuous crossing payment:** `||p_Q||inf<=C_eta/L`, `p_Q in C_0`; or
2. **split-slope mismatch:** `||c_J-c_K||>sqrt(3) beta`; or
3. **ultra-common alignment:** `beta<=2(1+q_*)sqrt(2)eta L+2q_*||b||`.

For `eta=2^-20`,

`2(1+q_*)sqrt(2)eta=2.699458867187416e-6`,

`2q_*=0.001527814773672393`.

The inherited distributed-star gate is

`||b||>rho_*L`,
`rho_*=0.0006247538095703261`.

Therefore branch 3 sharpens to the relative statement

`boxed: beta/||b|| < 0.005848650958799406.`

So, after a `<2369.566/L` continuous payment, the prior `beta<||b||/4` collar collapses to either a genuine split-slope mismatch or a star aligned with the common child plane to better than `0.585%` in relative Euclidean norm.

If branch 2 occurs while branch 3 fails, then

`||delta||>sqrt(3) beta`
`          >0.010130160616376999 ||b||`
`          >6.328856436640812e-6 L`.

This is a fixed target-scale coefficient resource, not a vanishing qualitative mismatch.

There is also a source-safe interpretation. The scalar difference slope

`S_delta=delta^T V_J^T X_J-delta^T V_K^T X_K`

is an ORIGINAL-coordinate linear form with coefficient-vector norm exactly

`[(delta^T G delta)+(delta^T H delta)]^(1/2)=||delta||`.

Hence the standard one-dimensional product-projection theorem gives

`||p_(S_delta)||infinity <= sqrt(2)/||delta||`.

No independence between `S_delta` and the common longitudinal slope is asserted. This scalar is therefore a legitimate future receiver input, but this report does not incorrectly treat it as an independent convolution factor.

## 6. Designated fleet04/B08 theorem applied on the same survivor

The full hub polynomial is

`Q=a X_0^2+2X_0 <b,Y>+Y^T C Y`,

where the physical hub `X_0` is independent of the child product vector `Y`. The standard product-marginal bound gives

`||p_(2<b,Y>)||infinity <=1/(sqrt(2)||b||)`.

Apply `QFORM-DISTRIBUTED-STAR-DERIVATIVE-SPLIT-v1` from fleet04/B08 with

`Gamma=2<b,Y>`, `R(Y)=Y^T C Y`.

It retains all of `C`, all signs, and arbitrary dependence between `Gamma` and `R`. Thus

`boxed:
 sup_t P(|Q-t|<eps)
 <=4*2^(1/4) sqrt(eps/||b||).
}`

At the inherited `||b||>rho_*L` gate this is

`boxed:
 sup_t P(|Q-t|<eps)
 <190.311 sqrt(eps/L).
}`

This is an actual inequality on the same double-alignment survivor. It is deliberately recorded as a square-root small-ball bound, not misreported as a density bound. The partner's own pair-log transducer upgrades this to a density bound only when an eligible physical-pair completion with persistent effective star is available.

## 7. Regression checks

A deterministic seeded checker verified the split-alignment identity over 600 random orthonormal two-frames and balanced physical cuts. Maximum absolute Pythagoras error was `4.263256414560601e-14`.

The direct plane-transfer inequality of Section 3 was tested on the same 600 configurations with random small crossing perturbations; maximum observed violation was `0`.

The fixed constants were independently recomputed as

`g=0.32322330470336313`,
`m_0=0.9895285072531598`,
`s_0=0.31959453358755213`,
`q_*=0.0007639073868361965`,
`C_(2^-20)=2369.5656377954524`,
`relative ultra-alignment gate=0.005848650958799406`,
`fixed mismatch scale=6.328856436640812e-6 L`.

These computations are regression evidence only; Sections 2--6 are analytic.

## 8. What is actually left

This run does **not** solve the full conjecture. It removes a misleadingly broad description of the simultaneous rank-two tube. In the inherited B08 geometry, after a finite continuous payment the primitive obstruction is now one of two sharply quantified states:

- a **split-slope mismatch** `||delta||>sqrt(3) beta`, carrying a source-safe scalar linear-form resource; or
- an **ultra-common longitudinal collar** `beta/||b||<0.005849`.

The next B08 implication is

`QFORM-SPLIT-SLOPE-MISMATCH-OR-ULTRALONGITUDINAL-COMPILER-v1`:

use the mismatch scalar through a dependence-safe shared-slope / whole-copy receiver, or show that the ultra-common collar forces an existing exact-aligned, pair-log, ridge, volume, or higher-spectral exit. The fresh correction against nonzero-puncture fiberwise `|t|^-1` estimates rules out treating the latter by a worst-fiber continuity argument.

Full universal boundedness: **OPEN**. Global continuity: **OPEN**.
