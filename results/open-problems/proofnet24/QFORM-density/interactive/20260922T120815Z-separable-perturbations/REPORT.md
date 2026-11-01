# Diffuse quadratic components with arbitrary separable perturbations

Programme: QFORM-DENSITY-3EIG-20260922. Interactive derivation, 22 September 2026. Claim ID: QFORM-DIFFUSE-SEPARABLE-PHASE-v1.

**Status:** complete analytic argument for the theorem below, pending independent end-to-end review. The full arbitrary-matrix three-large-eigenvalue conjecture remains OPEN. No literature-wide novelty claim or native learned-memory ingestion claim is made.

## 1. Source and exact advance

This extends the existing fleet02/B08 argument at `yspennstate/math-open-problems@0b5925a458d36c1ec1cf8ab344c9676260a97c8a:proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B08/B08-20260922T113624Z-qform11/REPORT.md`, blob `212febc02c4c1f3a8e6c073d0a8ed5d2d6b4ea0a`. The full report was read, including its geometric Brascamp-Lieb and sharp Hausdorff-Young proof. Its unperturbed diffuse-rank theorem is the dependency, not a newly discovered result here.

The new step retains an arbitrary coordinate-separable phase as a complex product amplitude. Sharp Hausdorff-Young applies to complex functions without changing its constant. Consequently the density estimate survives arbitrary separable perturbations, including diagonal quadratic perturbations. A physical-principal-block version also permits every outside coupling. No independent-noise assertion is used.

## 2. Theorem

Let X_1,...,X_n be independent real random variables with probability densities 0<=f_i<=1. Let U be an n-by-r real matrix with U^T U=I_r, r>=3, and rows u_i^T. Assume

`c_i=||u_i||_2^2 <= 1/2` for every i.

Let Lambda be any invertible real symmetric r-by-r matrix and V_i arbitrary real-valued measurable functions, finite almost surely. Define

`T=(U^T X)^T Lambda (U^T X)+sum_i V_i(X_i)`,

`B(U)=prod_{c_i>0} (1-c_i)^(-(1-c_i)/2)`, and `Delta=|det Lambda|`.

Then T has a bounded continuous density vanishing at infinity, and

`||p_T||_infinity <= [r/(r-2)] B(U)^(2/r) Delta^(-1/r) <= [e r/(r-2)] Delta^(-1/r)`.

In particular r=3 and Delta>=1 give the bound 3e. The V_i need not be bounded, smooth, polynomial, integrable, or independent of U^T X. No moments, centering, identical laws, log-concavity, compact support, connected support, or sign assumptions are imposed. The leverage condition is an additional geometric hypothesis, not a consequence of the original conjecture's spectral hypothesis.

## 3. Classical inputs

Use the convention `hat h(xi)=integral exp(-i xi x) h(x) dx`.

Geometric rank-one Brascamp-Lieb: if v_i are unit vectors and positive c_i satisfy `sum c_i v_i v_i^T=I_r`, then

`integral_R^r prod H_i(v_i dot xi)^(c_i) dxi <= prod (integral_R H_i)^(c_i)`

for nonnegative integrable H_i. The exact normalized statement is Theorem 3.3 in Livshyts-Paouris-Pivovarov, arXiv:1507.07949, https://arxiv.org/pdf/1507.07949 .

Sharp Hausdorff-Young, for COMPLEX h and 1<=p<=2, q=p/(p-1):

`||hat h||_q <= (2 pi)^(1/q) p^(1/(2p)) q^(-1/(2q)) ||h||_p`.

Source: W. Beckner, Inequalities in Fourier analysis, Annals of Mathematics 102 (1975), 159-182, DOI 10.2307/1970980; publisher record https://annals.math.princeton.edu/1975/102-1/p11 .

## 4. Full proof

### Step 1: retain the perturbations exactly

For each fixed real t put

`h_{i,t}(x)=f_i(x) exp(i t V_i(x))`.

Then `||h_{i,t}||_p=||f_i||_p<=1` for every p>=1. Push the complex product measure with density `prod h_{i,t}` forward by x -> U^T x. It has an L^1 density g_t with `||g_t||_1<=1`: complete U to an orthogonal matrix (U,W), evaluate the original product at Uy+Wz, and integrate in z. Fubini gives both existence and the norm bound. Its Fourier transform is

`hat g_t(xi)=prod_i hat h_{i,t}(u_i dot xi)`.

Zero rows contribute scalar factors of modulus <=1 and may be omitted from estimates. No conditional independence after spectral rotation is asserted.

### Step 2: uniform L^1 Fourier estimate for the complex projection

For nonzero rows put `v_i=u_i/sqrt(c_i)`. Then `sum c_i v_i v_i^T=I_r` and `sum c_i=r`. Apply geometric Brascamp-Lieb with

`H_i(s)=|hat h_{i,t}(sqrt(c_i) s)|^(1/c_i)`.

It gives

`||hat g_t||_1 <= prod_i c_i^(-c_i/2) ||hat h_{i,t}||_(1/c_i)`.

Set `q_i=1/c_i>=2` and `p_i=1/(1-c_i)<=2`. Sharp Hausdorff-Young yields

`||hat h_{i,t}||_(1/c_i) <= (2 pi)^(c_i) (1-c_i)^(-(1-c_i)/2) c_i^(c_i/2)`.

The c_i powers cancel, hence

`||hat g_t||_1 <= (2 pi)^r B(U)`.

This bound is independent of t and the functions V_i. The elementary inequality `-(1-c) log(1-c)<=c`, for 0<=c<1, gives `B(U)<=exp(r/2)`. To check its sign, `c+(1-c)log(1-c)` is zero at 0 and has derivative `-log(1-c)>=0`.

### Step 3: justified quadratic inversion with a Gaussian cutoff

The characteristic function of T is exactly

`phi_T(t)=integral_R^r exp(i t y^T Lambda y) g_t(y) dy`.

For t nonzero and epsilon>0, insert exp(-epsilon |y|^2). Fourier inversion for g_t and Fubini are valid because hat g_t is integrable and the Gaussian cutoff is integrable. Thus

`I_epsilon(t)=(2 pi)^(-r) integral hat g_t(xi) K_{epsilon,t}(xi) dxi`,

where

`K_{epsilon,t}(xi)=integral exp(-epsilon |y|^2+i t y^T Lambda y+i xi dot y) dy`.

Diagonalize Lambda orthogonally inside this Gaussian integral. Its scalar factor for eigenvalue lambda_j and rotated frequency eta_j is

`sqrt(pi) (epsilon-i t lambda_j)^(-1/2) exp[-eta_j^2/(4(epsilon-i t lambda_j))]`.

The exponential has modulus at most 1 because `Re (epsilon-i t lambda_j)^(-1)=epsilon/(epsilon^2+t^2 lambda_j^2)>0`. Consequently

`|K_{epsilon,t}(xi)| <= pi^(r/2) prod_j (epsilon^2+t^2 lambda_j^2)^(-1/4) <= pi^(r/2) |t|^(-r/2) Delta^(-1/2)`.

Together with Step 2 this gives

`|I_epsilon(t)| <= B(U) pi^(r/2) |t|^(-r/2) Delta^(-1/2)`.

For each fixed t the density g_t is integrable, so dominated convergence as epsilon decreases to zero yields

`|phi_T(t)| <= min(1, K |t|^(-r/2))`, where `K=B(U) pi^(r/2) Delta^(-1/2)`.

The bound 1 follows from the actual probability law of T, not from positivity of the auxiliary complex g_t. The argument does not invoke the false arbitrary-density one-dimensional stationary-phase estimate.

### Step 4: integrate and recover the density

Put `t_0=K^(2/r)`. Since r>2,

`integral_R |phi_T(t)| dt <= 2 [t_0+K integral_{t_0}^infinity t^(-r/2)dt] = 2 [r/(r-2)] K^(2/r)`.

The characteristic function is integrable. Fourier inversion gives a bounded continuous density vanishing at infinity, and

`||p_T||_infinity <= (2 pi)^(-1)||phi_T||_1 <= [r/(r-2)] B(U)^(2/r) Delta^(-1/r)`.

Using B(U)<=exp(r/2) proves the stated simpler estimate. QED.

## 5. Matrix consequences

**Diagonal perturbations.** Every matrix `A=D+U Lambda U^T`, with D an arbitrary real diagonal matrix and U,Lambda as above, has the stated bound. Arbitrary linear terms can also be absorbed in the V_i. The full A can have many additional small nonzero eigenvalues. Delta refers to Lambda, not to the full matrix A.

**Physical principal block.** Suppose only `A_II=D+U Lambda U^T` on a subset I of ORIGINAL coordinate indices has the above representation. All other entries of A may be arbitrary. Conditional on `X_{I^c}=z`, the form is

`X_I^T A_II X_I+2 X_I^T A_{I,I^c} z+z^T A_{I^c,I^c} z`.

The conditional X_I keep their original independent laws. Incorporate the linear terms into V_i and ignore the modulus-one constant phase. The same characteristic-function bound is uniform in z; averaging preserves it. Step 4 then proves the same bounded-continuous-density conclusion for the entire quadratic form. No conditional normalization loss or independence of quadratic summands occurs. QED.

**Nonunit density bounds.** For `f_i<=M_i`, replace B(U) by `B(U) prod_i M_i^(c_i)`. A common bound M introduces exactly an M^2 factor in the final density bound.

## 6. Explicit target-matching example

Let n=6, r=3, `U=(I_3;I_3)/sqrt(2)`, `Lambda=diag(2,2,-2)`, and `D=I_6/10`. Every leverage equals 1/2. The full matrix has eigenvalues

`21/10, 21/10, -19/10, 1/10, 1/10, 1/10`.

Thus it is genuinely coupled in the independent coordinates, indefinite, has three large absolute eigenvalues, and has three additional small nonzero eigenvalues. Here `B(U)=2^(3/2)` and `Delta=8`, so the sharper bound is exactly `||p_Q||_infinity<=3`.

Finite exact symbolic checks of this example and of scalar prefactors have passed. Their scope is only algebraic sanity checking; they do not verify the full conjecture or substitute for review of this analytic proof.

## 7. Full-target obstruction and review request

The spectral hypothesis alone has not been shown to force a suitable diagonally perturbed diffuse component or a suitable physical principal block with determinant uniformly bounded below. Nor does the proof handle an arbitrary nonseparable remainder by merely multiplying its phase into the amplitude. For leverage >1/2 the displayed route would request Fourier L^q control for q<2, outside the available Hausdorff-Young range.

Accordingly the full conjecture remains OPEN. Please have existing fleet02/B08 and fleet04/B12 independently check the complex-amplitude and uniform-in-conditioning steps. Existing proof-assembly workers can then use the exact supported scope. This is a request for review, not a claim that either review has occurred.

## 8. Operational provenance

Current control was reread before publication; the owner check-in request remains active. This is an interactive mathematical output, not a scheduled-worker login or an independent peer review. Repository access is not verified native brain ingestion. Only mathematics and source pins are included. A narrow local credential/signed-link pattern scan and human scope review were performed; the full repository privacy scanner was not available in the working container. No credential, native scheduler ID, email, public release, paid call, remote workflow, new account, or unrelated material is included.
