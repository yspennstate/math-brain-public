Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum.**

# PROB10-04 idea before code — transport Gibbs covariance in outer mean space

Status: **research idea / source OPEN**. Model is the owner-frozen classical iid proper random 3-SAT model. The published explicit-decimal source bracket remains `[3.52,4.4898]`; no endpoint movement is claimed here.

## Why change method now

The preceding PROB10-04 run proved an inverse-free parallel-sum certificate for strict negativity of the remaining Díaz outer Hessian:

\[
D(y)-T^T\Sigma_V(y)T-(I-T)^T\Sigma_C(y)(I-T)\succ0.
\]

At the inherited finite-decimal saddle surrogate, a fixed rational split `T_6` has a substantial pointwise minimum eigenvalue about `0.0720`, but that is only a point certificate. The exact remaining local obligation is to control how the two finite-state Gibbs covariance matrices move when the **mean parameter** `y=(u,v,w)` moves. Re-solving the six natural multipliers on every outer box would largely recreate the old grid problem.

The new idea is to prove a finite-support covariance-transport inequality directly in exponential-family geometry, then convert a mean-space ball around the saddle into a multiplicative covariance enclosure. This should turn one certified center into a certified neighborhood without covariance inversion or repeated multiplier solving.

## Exact missing lemma before any code

Consider a finite block exponential family

\[
A(\theta)=\sum_b m_b\log\sum_{s\in S_b}g_{b,s}e^{\theta\cdot s},
\qquad \Sigma(\theta)=\nabla^2A(\theta),
\]

with `m_b>0`, `g_{b,s}>0`, finite supports `S_b`, and positive-definite covariance at a reference point `theta_0`.

For a direction `delta`, define the largest within-block directional range

\[
R(\delta)=\max_b\max_{s,t\in S_b}|\delta\cdot(s-t)|.
\]

The exact lemma to prove is

\[
\boxed{e^{-R(\delta)}\Sigma(\theta_0)\preceq
\Sigma(\theta_0+\delta)\preceq e^{R(\delta)}\Sigma(\theta_0).}
\tag{I.1}
\]

The intended proof differentiates every directional variance along `theta_t=theta_0+t delta`. For each test vector `x`,

\[
{d\over dt}\,x^T\Sigma(\theta_t)x
=\sum_bm_b\,\mathbb E_t[(X_b-\mathbb EX_b)^2(Y_b-\mathbb EY_b)],
\]

where `X_b=x·S_b`, `Y_b=delta·S_b`; hence the derivative in absolute value is at most `R(delta)` times the variance itself. Grönwall then gives (I.1).

The second missing step is to invert the mean map without solving for `theta`. If

\[
y=\nabla A(\theta),\qquad \lambda_0=\lambda_{\min}(\Sigma(\theta_0)),
\]

and every within-block support diameter is at most `L` in Euclidean norm, then for `rho=||y-y_0||_2<lambda_0/L` the desired consequence is

\[
\boxed{(1-s)\Sigma_0\preceq\Sigma(y)\preceq(1-s)^{-1}\Sigma_0,
\qquad s={L\rho\over\lambda_0}.}
\tag{I.2}
\]

A sharper anisotropic form should replace `L/lambda_0` by a finite Mahalanobis support constant

\[
L_*:=\max_{b,s,t}\sqrt{(s-t)^T\Sigma_0^{-1}(s-t)}
\]

and the mean norm `||z||_{Sigma_0^{-1}}`. This is the preferred compiler if it survives the proof.

## Three routes to try in this run

1. **Isotropic mean-ball transport.** Prove (I.1)-(I.2) exactly and combine them with the fixed `T_6` inverse-free LMI. This is deliberately conservative but requires only support diameters and the center covariance.

2. **Mahalanobis support transport.** Prove the covariance-adapted version using `L_*`; because the Díaz variable support is highly anisotropic, this may enlarge the certified neighborhood materially. The finite support maximization is exact and small enough to enumerate after the proof.

3. **Single-center globalization test.** Ask whether either transport inequality can cover the whole feasible outer polytope from one center. If not, quantify the obstruction rather than hiding it. A failure would force the next method change to a recentered/support-oracle cover or a value-gap argument, not another local rescue motif.

## How this would plug into the Díaz outer Hessian

Let

\[
M_0=D(y_0)-T^T\Sigma_{V,0}T-(I-T)^T\Sigma_{C,0}(I-T)\succeq\eta_0I.
\]

For an outer mean ball, if the two covariance transport factors are `1/(1-s_V)` and `1/(1-s_C)`, while

\[
||D(y)-D(y_0)||_{op}\le L_D\rho,
\]

then the sufficient robust certificate is

\[
\eta_0-L_D\rho
-{s_V\over1-s_V}\|T^T\Sigma_{V,0}T\|_{op}
-{s_C\over1-s_C}\|(I-T)^T\Sigma_{C,0}(I-T)\|_{op}>0.
\tag{I.3}
\]

For the copy covariance in the Díaz coordinates, I expect the elementary bound `L_D=sqrt(6)` on the copy simplex. Proving (I.3) with exact finite-support constants would be a real local certification theorem, but **not** by itself an improved random-3-SAT threshold endpoint. The global outer separation and rescue penalty still have to be paid, and the center data must ultimately be outward-certified rather than treated as rounded decimals.