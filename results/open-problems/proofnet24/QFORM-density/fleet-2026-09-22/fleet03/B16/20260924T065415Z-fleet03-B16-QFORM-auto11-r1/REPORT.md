SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet03, slot B16, 2026-09-24T06:54:15Z.
attacking: QFORM-RANK2-SCHUR-INTEGRATED-FIBER-L2-v1 by testing the proposed mixed norm on a strict target before trying to prove it; after it fails, replace that absoluteized interface by a coupled pre-absolute third-resource mechanism.

# fleet03/B16 r43 — the r42 fiber-L2 mixed norm is not a universal closure criterion

Programme: `QFORM-DENSITY-3EIG-20260922`  
Run: `20260924T065415Z-fleet03-B16-QFORM-auto11-r1`  
Role: Projection-product interaction  
Execution: `WITHOUT_VERIFIED_BRAIN`  
Status: `REFUTED_INTERMEDIATE_MECHANISM + SOURCE-VALID REPAIR ON THE WITNESS / FULL QFORM OPEN`  
Global continuity: `OPEN`.

## 1. Scope and source boundary

The owner target remains the unrestricted statement for independent ORIGINAL-coordinate inputs with scalar probability densities at most one and an arbitrary real symmetric matrix having at least three eigenvalues of modulus at least one. No Gaussian, log-concave, moment, compact-support, connected-support, iid, diagonal-basis, or post-rotation-independence assumption is introduced.


The immediate predecessor is fleet03/B16 r42:

`yspennstate/math-open-problems@a7172687ed5ae3bc9154a1cf792c9afa21f2119f`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B16/20260924T055252Z-fleet03-B16-QFORM-r42/REPORT.md`.

It proved the exact hub-star Plancherel identity. For

`Q=aH^2+2H B+R`, `B=b dot X`,

with the literal physical hub `H` independent of the residual product bank, defining

`F_t(z)=int f_H(h) exp(i t(a h^2+2zh)) dh`

and

`G_t(z) dz = E[exp(i t R(X)); B in dz]`,

one has

`int |F_t(z)|^2 dz=(pi/|t|) int f_H^2 <= pi/|t|`,

`phi_Q(t)=int F_t(z)G_t(z) dz`,

and therefore

`|phi_Q(t)| <= sqrt(pi/|t|) ||G_t||_2`.                         (1.1)

r42 then isolated the sufficient proposed closure

`int_{|t|>=1} |t|^(-1/2) ||G_t||_2 dt <= C`.                   (1.2)

The first essential task this run is to test (1.2) before investing in a proof.

## 2. Strict-target counterexample to the proposed mixed norm

Fix `0<epsilon<=1/64` and let `H,X,Y` be mutually independent `Uniform[-1/2,1/2]` variables. Their densities equal one on their supports. Consider

`Q_epsilon = epsilon H^2 + 2 H X - epsilon X^2 + Y^2`.          (2.1)

Its coefficient matrix in the original independent coordinates is

`A_epsilon = [[epsilon,1,0],[1,-epsilon,0],[0,0,1]]`.            (2.2)

The first `2x2` block has characteristic polynomial

`lambda^2-(1+epsilon^2)`,

so

`spec(A_epsilon)={-sqrt(1+epsilon^2), 1, +sqrt(1+epsilon^2)}`.   (2.3)

Thus (2.1) is a strict instance of the FULL owner target for every allowed `epsilon`: all three eigenvalues have modulus at least one.

Take `H` as the r42 physical hub. Then

`a=epsilon`, `b=(1,0)`, `B=X`, `C=diag(-epsilon,1)`,

and the scalar Schur complement is

`S=C-bb^T/a=diag(-epsilon-epsilon^(-1),1)`.                      (2.4)

In the r41 notation, because `A_epsilon` is invertible,

`q_h=1`, `rho=1`, `tau=0`.                                      (2.5)

At normalized spectral scale `s=1`, (2.5) lies in the hard collar

`q_h>=63/64`, `0<|a|<=1/64`,

and satisfies the r41 conclusions `rho^2>=62/63`, `tau<=|a|/sqrt(63)`.

Hence this example tests the exact state for which (1.2) was proposed, rather than an unrelated rank-two control.

## 3. Exact complex fiber and logarithmic divergence

For (2.1), the residual term is

`R(X,Y)=-epsilon X^2+Y^2`,

and `B=X`. Since `X` is uniform on an interval of length one, the complex fiber density from r42 is exactly

`G_t(z)=1_{[-1/2,1/2]}(z) exp(-i epsilon t z^2) g(t)`,           (3.1)

where

`g(t)=int_{-1/2}^{1/2} exp(i t y^2) dy`.                         (3.2)

Therefore

`boxed: ||G_t||_2=|g(t)|.`                                      (3.3)

For `t>0`, set `R_t=sqrt(t)/2`. Scaling gives

`g(t)=t^(-1/2) [2 int_0^{R_t} exp(iu^2) du]`.                   (3.4)

The classical Fresnel value is

`2 int_0^infinity exp(iu^2) du = sqrt(pi) exp(i pi/4)`.          (3.5)

A one-line integration by parts gives the rigorous tail estimate

`|int_R^infinity exp(iu^2)du| <= 1/R` for every `R>0`.           (3.6)

Indeed, use `exp(iu^2)=(2iu)^(-1) d/du exp(iu^2)` and let the upper endpoint tend to infinity; the boundary term and the integral of `1/(2u^2)` together contribute at most `1/R`.

Combining (3.5)-(3.6),

`|2 int_0^R exp(iu^2)du| >= sqrt(pi)-2/R`.                       (3.7)

If `R>=4/sqrt(pi)`, the right side is at least `sqrt(pi)/2`. Since `R=R_t=sqrt(t)/2`, this occurs for

`t>=64/pi`.                                                      (3.8)

Thus

`boxed: |g(t)| >= (sqrt(pi)/2) t^(-1/2),  t>=64/pi.`             (3.9)

Equations (3.3) and (3.9) imply

`int_1^infinity t^(-1/2)||G_t||_2 dt`
` >= (sqrt(pi)/2) int_{64/pi}^infinity dt/t`
` = infinity.`                                                   (3.10)

The same is true for the two-sided integral in (1.2).

### New correction

`QFORM-HUBSTAR-FIBERL2-MIXEDNORM-UNIVERSAL-FALSE-v1`:

> The proposed universal r42 obligation
> `int |t|^(-1/2)||G_t||_2 dt < C`
> is false even in the normalized small-pivot hard collar and even for a strict three-large-eigenvalue target matrix with three compact cap-one independent inputs.

This refutes only the INTERMEDIATE absoluteized mixed-norm mechanism. It is not a counterexample to QFORM.

The structural reason is visible in (3.1): taking the `L2` norm in the star-frequency fiber before integrating in time preserves only the separate Fresnel factor from `Y^2`, whose magnitude is asymptotically `t^(-1/2)`. The outer hub Plancherel contributes another `t^(-1/2)` only after Cauchy-Schwarz, leaving the logarithmic endpoint `t^(-1)`. The missing gain must come from cancellation/curvature of the coupled `(H,X)` pair before this absoluteization, or from another source-separated third smoother.

## 4. The witness itself is paid: source-valid rank-two half-Riesz plus the disjoint third square

The failure of (1.2) is strictly a proof-interface failure. Rewrite

`Q_epsilon=Z_epsilon+Y^2`,                                      (4.1)

where

`Z_epsilon=epsilon H^2+2HX-epsilon X^2`.                         (4.2)

The completed orientation-free rank-two theorem

`QFORM-RANK2-AFFINE-HALF-RIESZ-v1`

is source-pinned at

`yspennstate/math-open-problems@e542b1a6ef471b329e4e88a6553e1aacb45acc1a`

`proofnet24/QFORM-density/interactive/20260922T161801Z-rank-two-fusion/REPORT.md`.

Applied to the `2x2` matrix

`Lambda_epsilon=[[epsilon,1],[1,-epsilon]]`,

whose determinant has magnitude `1+epsilon^2`, it gives

`sup_s E |Z_epsilon-s|^(-1/2)
 <=128(1+epsilon^2)^(-1/4).`                                    (4.3)

The square `Y^2` is independent of `Z_epsilon` and has density exactly

`p_{Y^2}(u)=u^(-1/2) 1_{0<u<1/4}`.                              (4.4)

Hence for almost every `t`, by convolution,

`p_{Q_epsilon}(t)
 =E p_{Y^2}(t-Z_epsilon)
 <=E |t-Z_epsilon|^(-1/2)
 <=128(1+epsilon^2)^(-1/4)
 <=128.`                                                        (4.5)

Thus

`boxed: ||p_{Q_epsilon}||_infinity <=128.`                       (4.6)

This is also a direct specialization of the already-completed fleet02/B20 theorem `QFORM-HALFRIESZ-PLUS-DISJOINT-SQUARE-v1`, source

`yspennstate/math-open-problems@20ec5f8f3ed2028edf27894cd3956d13e4662a9a`,

`proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B20/20260923T155833Z-fleet02-B20-QFORM-auto11c/REPORT.md`.

Therefore this exact repair scope is already published; this run does not duplicate it as a new theorem. What is new is that the r42 fiber-L2 route is now ruled out even though the output remains uniformly bounded by the pre-fiber nonlinear mechanism.

No new continuity claim is needed for this correction. Global QFORM continuity remains open.

## 5. Designated fleet04/B16 result applied to an actual inequality

The newest completed designated partner report consumed is fleet04/B16 r4, canonical source

`yspennstate/math-open-problems@7f2bb2d330022b09a6af6e39ab09d054caeaa346`,

`proofnet24/QFORM-density/fleet-2026-09-22/fleet04/B16/20260924T041516Z-fleet04-B16-QFORM-r4/REPORT.md`.

Its source-preserving phase-aligned theorem gives, for mutually independent `X,Y,W`, cap-one `X,Y`, and `W` with density cap `K`,

`F_{lambda,nu}=lambda(X+Y)^2+2nu W(X-Y)`,

`kappa_K=(sqrt(lambda^2+4nu^2/K^2)-|lambda|)/2`,

and

`||p_F||_infinity
 <=8 [K^2/(2|lambda|nu^2 kappa_K)]^(1/4).`                      (5.1)

Apply it with `lambda=nu=K=1` to the partner's strict-target carrier

`R_theta=theta H^2+(X+Y)^2+2(H+Z)(X-Y)`,                        (5.2)

where `Z` is the sum of two disjoint cap-one original coordinates, so Young's inequality gives `||p_{H+Z | H=h}||_infinity<=1` after conditioning on the physical hub in the source-valid construction. The partner calculation yields

`boxed: ||p_{R_theta}||_infinity
 <=8 (sqrt(5)-1)^(-1/4)
 =7.587162715951975... <7.588.`                                 (5.3)

Now let `T(W_0)` be ANY real random variable measurable with respect to a further disjoint original-coordinate product bank `W_0`; in particular it may be an arbitrary quadratic-plus-linear form on that bank. Since `T(W_0)` is independent of `R_theta`, convolution with its probability law cannot increase an `L-infinity` density. Therefore

`boxed: ||p_{R_theta+T(W_0)}||_infinity <7.588.`                 (5.4)

The carrier (5.2) already has at least three eigenvalues of modulus at least two by the partner's exact spectral calculation, and adding a block-diagonal disjoint `T(W_0)` preserves those carrier eigenvalues. Thus (5.4) is an actual strict owner-target inequality with arbitrary independent outside quadratic baggage, not a two-eigenvalue surrogate.

## 6. What changes in the B16 proof map

The r42 hub-star identity itself remains correct and useful:

`int |F_t|^2 = pi|t|^(-1) int f_H^2`.

What fails is the next Cauchy-Schwarz/fiber-L2 absoluteization as a UNIVERSAL time-integrable closure. The strict target (2.1) reaches the exact logarithmic endpoint.

Accordingly, B16 should not spend another run trying to prove (1.2). The replacement obligation is:

`QFORM-HUBSTAR-PAIR-PREABSOLUTE-THIRDRESOURCE-v1`:

> In the genuine shared-bank small-pivot collar where no already-paid disjoint-square, definite-plane, phase-aligned-pair, or source-separated fresh-hub exit applies, combine the literal hub-star oscillation with at least one rank-two Schur direction BEFORE taking a fiber norm/absolute value, so that the third smoothing resource is spent jointly rather than as `||G_t||_2`.

Equivalent direct small-ball/coarea formulations are acceptable only if they retain the original product provenance. The correction-safe exits already available should be used first:

1. a genuinely disjoint third square: rank-two half-Riesz + square convolution;
2. a definite projected two-plane: fleet04/B16 r4;
3. a source-preserving phase-aligned pair: fleet04/B16/fleet01/B16 pair-log route;
4. the exact density-preserving shear/Fresnel branch where its hypotheses hold.

The remaining work is the complementary shared-bank state, not another attempt to prove the false mixed norm.

## 7. Finite check and status

The deterministic checker in this run directory verifies:

- strict-target eigenvalues `{-sqrt(1+epsilon^2),1,+sqrt(1+epsilon^2)}` at `epsilon=1/64`;
- the hard-collar inequalities `q_h=1`, `rho=1`, `tau=0`;
- the exact Fresnel lower-bound threshold `t_0=64/pi=20.371832715762604...`;
- the repaired half-Riesz/square constant `<128`;
- the designated fleet04/B16 constant `7.587162715951975...<7.588`.

It ends `STATUS=PASS`. The checker is arithmetic/regression evidence; the logarithmic divergence is proved analytically in Section 3.

### Final status

- `QFORM-HUBSTAR-FIBERL2-MIXEDNORM-UNIVERSAL-FALSE-v1`: **PROVED correction to an intermediate mechanism**.
- Strict target witness `Q_epsilon`: **uniformly bounded by 128 via an already source-valid nonlinear route**; therefore **not a QFORM counterexample**.
- Designated partner theorem: **applied to the actual strict-target inequality (5.4)**.
- Full QFORM: **OPEN / NOT PROVED / NOT DISPROVED**.
- Full-target continuous density: **OPEN**.
- Execution: **WITHOUT_VERIFIED_BRAIN**; repository access and native brain ingestion remain distinct.
