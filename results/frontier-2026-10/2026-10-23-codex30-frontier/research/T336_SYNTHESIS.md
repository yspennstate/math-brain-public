# T336: constructive RBF posterior approximation and unconditional GP-prior ERM

## Status and exact scope

This package extends the internally completed scalar finite-rank target. It does **not** count that prior result as new. The combined result below treats a zero-mean RBF Gaussian process on a compact input ball, positive observation noise, a bounded number of context examples and query locations, and a specified signed, masked, unnormalized ReLU-attention architecture with local linear mixing. It gives explicit approximation sizes and a finite-class **ERM** sample bound. No claim is made that gradient descent finds the ERM, that the same circuit is a standard softmax transformer, or that the unrestricted original catalog row is fully solved.

The proof is distributed across A21–A24, A28, the encoder-grid addendum, and the unconditional-ERM addendum. A29 independently reviews these steps. The constructions use exact real constants. Quantization applies to the learned encoder parameters; the attention solver is a fixed, unquantized part of the hypothesis class.

## 1. Conservative joint posterior inference

For a PSD feature kernel, write the train, train-query and query Gram blocks as G,H,J. The joint noisy predictive law at m queries is Gaussian with

\[
A=G+sI,\qquad \mu=H^TA^{-1}y,\qquad C=J+sI_m-H^TA^{-1}H,\quad s>0.
\]

Suppose the spectrum of A lies in [a,b], 0<a<b. Put c=(a+b)/2, d_0=(b-a)/2, and let T_L be the degree-L Chebyshev polynomial. Define

\[
r_L(x)=\frac{T_L((c-x)/d_0)+1}{T_L(c/d_0)+1},\qquad
P_L(x)=\frac{1-r_L(x)}x.
\]

P_L is a polynomial of degree L-1. On [a,b],

\[
0\le r_L(x)\le e_L=\frac{2}{T_L(c/d_0)+1}
=\frac{4q^L}{(1+q^L)^2},\qquad q=\frac{\sqrt{b/a}-1}{\sqrt{b/a}+1}.
\]

Consequently 0≼P_L(A)≼A^{-1}. The emitted joint covariance

\[
\widehat C=J+sI_m-H^TP_L(A)H
\]

satisfies **\(\widehat C\succeq C\succeq sI_m\)** at every L≥1. This is a conservative covariance statement, stronger than a noise-floor guarantee. The degree-L residual r_L is minimax among polynomials r with r(0)=1 and r≥0 on [a,b], in the supremum norm on that interval. This follows directly from the classical Chebyshev extremal inequality and is not claimed as a new extremal theorem.

If each feature has norm at most R_f, n≤N, and |y_i|≤B, the exact forward KL obeys

\[
\operatorname{KL}\bigl(N(\mu,C)\Vert N(\widehat\mu,\widehat C)\bigr)
\le \frac{e_L^2}{4s^2}\left(2NB^2mR_f^2+m^2R_f^4\right).
\]

Here \(\widehat\mu=H^TP_L(A)y\). The proof uses a Schur-complement bound, the Gaussian KL formula and an error bound on covariance, without a KL triangle inequality. In the exact finite-feature architecture, each signed dot product is two ReLU heads. A21 gives L+1 attention layers, two heads per layer, and residual width p+4m+3 for p feature coordinates (or the stated padding for equally sized heads). It includes the actual query covariance-row readout and a fixed-coefficient recurrence.

The rational example in A27 uses a PSD train/query Gram of all ones and s=1/10. The ordinary degree-one data-space approximation gives variance −17/30. The one-sided correction gives 21/110. This example concerns the data-space Schur-complement formula, not the prior feature-space formula whose positive noise floor was already established in Brain.

## 2. Explicit infinite-rank RBF approximation from raw inputs

For \(k(x,z)=\exp(-\|x-z\|^2/(2\ell^2))\), \(\|x\|,\|z\|\le R\), truncate the feature expansion at total degree k:

\[
\phi_\beta(x)=e^{-\|x\|^2/(2\ell^2)}\frac{x^\beta}{\ell^{|\beta|}\sqrt{\beta!}},\quad |\beta|\le k,
\qquad p=\binom{d+k}{k}.
\]

With a_0=R²/ℓ², the omitted feature kernel is PSD and

\[
\sup_{x,z}|k(x,z)-\langle\phi(x),\phi(z)\rangle|
\le\frac{a_0^{k+1}}{(k+1)!}.
\]

A28 builds an explicit raw-input ReLU encoder using piecewise-linear square/exponential approximations and clipped multiplication. Its depth, width, weight bound and interpolation count are given as formulas in d,R,ℓ,k and a target feature error ζ. Shared approximate features preserve PSD exactly. Their kernel error is at most the truncation error plus 2ζ+ζ². A23/A28 propagate this error directly through the posterior mean, covariance and forward KL. Thus the RBF result does not assume that an exact exponential feature map was given in the input.

The encoder-grid addendum makes the learning class concrete. Only encoder weights are gridded; every output feature coordinate is clipped to [-2,2]. All grid members therefore have feature norm at most 2√p and share the same fixed attention interval [s,s+4Np]. Every candidate emits a covariance in [sI,(s+4pm)I] and, after clipping context labels at B, a mean with norm at most

\[
M_B=4pN\sqrt m\,B/s.
\]

The addendum supplies a grid spacing δ_w, encoder parameter count P_enc and weight bound Q such that the grid contains an actual comparator with uniform forward KL at most ε_app on |y_i|≤B. Its cardinality is at most (4Q/δ_w)^{P_enc}. This closes the gap between a continuous-weight construction and a finite learnable class. The fixed attention constants are not learned or rounded.

## 3. Unconditional Gaussian-prior pretraining bound

Now draw independent whole GP tasks with exogenous input locations. Context labels are **not** conditioned to be bounded. Query labels are jointly Gaussian with the context, and the candidate can depend on those correlated context labels. A pathwise Gaussian-NLL envelope uses the unconditional query marginal, so this dependence causes no concentration gap.

For a finite candidate class of size J with global mean norm at most M and covariance between (s/2)I and VI, let

\[
V_0=s+mk_{\rm diag},\quad
\Lambda=4\left[\frac m2\log(2V/s)+\frac{2M^2}s+\frac{2mV_0}s\right],\quad
u=\log(2J/\delta).
\]

With probability at least 1−δ, an exact empirical NLL minimizer satisfies

\[
\mathcal K(\widehat f)-\inf_{f\in\mathcal F}\mathcal K(f)
\le 8\sqrt2\,\Lambda\sqrt{u/T}+4\Lambda u/T,
\quad \mathcal K(f)=\mathbb E_D\operatorname{KL}(p_D\Vert q_f).
\]

An empirical optimization error is added if only an approximate ERM is obtained. For excess at most ξ, the explicit sufficient sample count is

\[
T\ge\max\{512\Lambda^2u/\xi^2,\;8\Lambda u/\xi\}.
\]

The bounded-context comparator transfers to the original GP prior. Set

\[
\rho_B=\min\{1,2N e^{-B^2/[2(k_{\rm diag}+s)]}\},\quad
C_{M,V}=\frac{mV_0}s+\frac m2\log^+(V/s)+\frac{2M^2}s.
\]

Then its unconditional expected KL is at most

\[
\varepsilon_{\rm app}+C_{M,V}\rho_B
+\frac{2\sqrt3\,mk_{\rm diag}}s\sqrt{\rho_B}.
\]

Combine these formulas with the explicit encoder grid. For RBF, k_diag=1, M=M_B, V=s+4pm and log J≤P_enc log(4Q/δ_w). Every quantity is specified. The guarantee is **prior-averaged expected forward KL**, not a uniform guarantee on the trained predictor over all label values.

The unconditional addendum gives a concrete consistency sequence: B_j=j, ε_app,j=1/j, δ_j=j^{-2}, and sufficiently many pretraining tasks \(T_j\ge j^2\Lambda_j^2\log(2J_j/\delta_j)\). For fixed input dimension, p_j=O((log j)^d), so the Gaussian clipping-tail error vanishes. Borel–Cantelli gives almost-sure convergence of the expected-KL risks of the sequence of exact ERMs. A fixed global mean cap would generally prevent this convergence; U12 proves that obstruction explicitly.

## 4. Hierarchical-GP extension and remaining limits

A26 gives deterministic errors for approximate log evidence, including both log determinant and likelihood quadratic form. A30 constructs a finite-feature, finite-mixture circuit with a padding-safe deterministic trace recurrence, signed attention aggregation, and a simplex-preserving piecewise-affine ReLU readout. The readout may be very large. The latent component-label KL identity combines evidence-weight error and component predictive error into a mixture KL bound.

This is a separate finite-feature expressivity result. It does not automatically inherit the RBF or pretraining theorem above: the evidence perturbation, mixture learning class and sample analysis must be carried through separately. Independent review of A30 is recorded in A29.

Overall, the combined RBF construction plus unconditional finite-class ERM theorem supplies a scoped quantitative answer to the approximation/statistics part of T336. Efficient optimization, unrestricted labels in a uniform guarantee, a standard softmax architecture, and broad external novelty remain open. The full original row is not retired by this package.
