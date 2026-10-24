# Rigor check — account03/B15 20260924T102515Z

This file checks the quantitative steps in `REPORT.md`.

## A. Concavity calculation

For `a=L/2` and `g(u)=2 Phi(a u)-1`,

`g'(u)=2 a phi(a u)=L phi(Lu/2)`.

Since `phi'(x)=-x phi(x)`,

`g''(u)=L * [-(L/2)^2 u phi(Lu/2)] = -(L^3/4)u phi(Lu/2)<=0` for `u>=0`.

Thus Jensen applies in the correct direction:

`E g(T^{-1/2}) <= g(E T^{-1/2})`.

The Gaussian interval bound is also in the correct direction because for a fixed variance a symmetric unimodal density maximizes the mass of a fixed-length interval when the interval is centered at the mean.

## B. Sharp cap-one constant

At `kappa=sqrt(2 pi)` and `L=1`,

`kappa/2=sqrt(pi/2)`.

Using the standard normal CDF,

`q_*=2 Phi(sqrt(pi/2))-1 = 0.7899085945560627...`,

so

`1-q_*=0.2100914054439373...`.

A single Gaussian with variance `T=1/(2 pi)` has peak

`(2 pi T)^(-1/2)=1`

and attains the interval concentration bound when centered at the interval midpoint. Hence the one-dimensional concentration theorem is sharp within the mixture class.

## C. Weak-closure direction

If `nu_n => mu` and `J` is open, Portmanteau gives

`mu(J) <= liminf_n nu_n(J)`.

Since each `nu_n(J)<=q_kappa(|J|)`, the liminf is also at most that same constant, so

`mu(J)<=q_kappa(|J|)`.

For compact support `[a,b]`, `J=(a-eps,b+eps)` has `mu(J)=1`, while `q_kappa(b-a+2eps)<1` for every finite `kappa`; contradiction. No reversal of Portmanteau is used.

## D. Product-TV amplification

For product measures and the cube event,

`nu_1 x ... x nu_n([0,1]^n)=product_i nu_i([0,1])<=q_*^n`.

Since the uniform cube law gives that event probability one,

`d_TV>=1-q_*^n`.

Numerical checks:

- `1-q_*^3 = 0.5071321183877962...`
- `1-q_*^10 = 0.9054267330355084...`
- `1-q_*^20 = 0.9910558971756630...`
- `1-q_*^40 = 0.9999200030246677...`

## E. Relaxed inverse-scale parameter in the determinant theorem

The source Gaussian-mixture proof has

`W_k >= Z_k product_i T_i^{alpha_i}`

with `0<=alpha_i<=2` and `sum_i alpha_i=2k`. Therefore

`W_k^{-1/(2k)} <= Z_k^{-1/(2k)} product_i (T_i^{-1/2})^{alpha_i/k}`.

Since `alpha_i/k<=2/k<1` for `k>=3`, Jensen for the concave power gives

`E (T_i^{-1/2})^{alpha_i/k} <= (E T_i^{-1/2})^{alpha_i/k}`.

If every inverse-scale moment is at most `kappa`, independence across coordinates gives

`E W_k^{-1/(2k)} <= Z_k^{-1/(2k)} kappa^{sum_i alpha_i/k} = Z_k^{-1/(2k)} kappa^2`.

The conditional Fourier inversion constant in the source theorem is `I_k/(2 pi)`, hence

`||p_Q||_infinity <= (I_k/(2 pi)) kappa^2 Z_k^{-1/(2k)}`.

At `kappa=sqrt(2 pi)` the factor `kappa^2/(2 pi)` equals one, recovering the source theorem exactly.

## F. TV-accuracy forces inverse-scale blow-up

If `d_TV(nu,Unif[0,1])<=eps`, then

`nu([0,1])>=1-eps`.

The concentration theorem gives

`1-eps <= 2 Phi(kappa/2)-1`,

hence

`kappa>=2 Phi^{-1}(1-eps/2)`.

For `k=3`, `Z_3>=1`, the present determinant certificate is therefore at least parametrically evaluated at

`(2 I_3/pi) [Phi^{-1}(1-eps/2)]^2`.

This is a statement about the size of the certificate produced by this mechanism, not a lower bound on the true density height.

With `I_3=2.942468198169458...`:

- `eps=.1`: required `kappa>=3.2897072539`, certificate `5.0681144568...`;
- `eps=.01`: required `kappa>=5.1516586071`, certificate `12.4287101476...`;
- `eps=.001`: required `kappa>=6.5810534630`, certificate `20.2825589653...`;
- `eps=1e-6`: required `kappa>=9.7832769514`, certificate `44.8229674789...`.

The normal-quantile asymptotic gives logarithmic divergence in `1/eps`.

## G. Logical-scope check

The argument does not use or imply:

- post-rotation independence;
- pointwise van-der-Corput decay;
- compact support of target inputs except when selecting `Uniform[0,1]` as an explicit admissible obstruction to approximation;
- any moment of the target rough law;
- a counterexample to the QFORM density conjecture.

It only blocks the proposed dense-subclass closure under the current Gaussian-mixture inverse-scale hypothesis and quantifies the loss under its direct relaxation.
