# fleet02/B18 auto11 — early substantive checkpoint

Programme `QFORM-DENSITY-3EIG-20260922`; full conjecture remains OPEN.

I am working in the exact-rank-three null-hub normal form already proved in the B18 chain:

\[
Q=2(X_0+\ell\cdot X_L)(g\cdot X_L)+d(\beta\cdot X_L)^2,
\qquad \|\beta\|_2=1,\quad \beta\cdot g=0,\quad \gamma=\|g\|_2>0.
\]
In the target-normalized moderate/high-shear compiler, `|d| gamma^2=hD`, `h>=1/5`, `D>=1`. For leaf `i`, `q_i=beta_i^2+g_i^2/gamma^2`.

## First new implication: the exact zero-edge heavy endpoint is paid

Assume a heavy witness satisfies `g_i=0`, hence `q_i=beta_i^2>1/2`. Put `T=g_- dot X_-`; then `||g_-||=gamma`. Conditioning on all `X_-`, the only random variables left are the two genuinely independent original coordinates `X_0,X_i`, and

\[
Q=d\beta_i^2X_i^2+2\ell_iT X_i+2T X_0+C(X_-).
\]
Thus for fixed `T=t`, completing the `X_i` square reduces to a translated square of coefficient `a=d beta_i^2`, convolved with `2tX_0`. If `U,V` are independent cap-one scalars, the density of

\[
aU^2+bU+2tV
\]
has the uniform envelope

\[
H_a(t)\le \min\left\{\frac1{2|t|},\sqrt{\frac{2}{|a||t|}}\right\}.
\]
The second term is the bathtub convolution of the square kernel `(|a||x|)^(-1/2)` against a probability density capped by `(2|t|)^(-1)`.

By Livshyts--Paouris--Pivovarov Theorem 1.1, the normalized original-source projection `T/gamma` has density cap at most `sqrt(2)`, hence `p_T<=sqrt(2)/gamma` (the one-coordinate endpoint is even stronger). Bathtub rearrangement against the even decreasing envelope above gives, with `H=|a|gamma^2`,

\[
\mathbb E H_a(T)\le 6e^{-1/3}H^{-1/3}.
\]
The exact computation splits at `R=gamma/(2sqrt(2))` versus `|a|/8`: the first case is at most `4H^(-1/3)`; in the second, putting `x=2sqrt(2)gamma^3/H>1` gives

\[
2H^{-1/3}x^{-1/3}(2+\log x)\le 6e^{-1/3}H^{-1/3},
\]
with equality of this majorant at `x=e`.

Therefore

\[
\boxed{\ \|p_Q\|_\infty\le 6e^{-1/3}(|d|\gamma^2q_i)^{-1/3}.\ }
\]
For the target-normalized B18 compiler, `|d|gamma^2=hD>=1/5` and `q_i>1/2`, so

\[
\boxed{\ \|p_Q\|_\infty<6e^{-1/3}10^{1/3}=9.262319472.\ }
\]
This uses no support/moment assumption and is insensitive to the arbitrary dense twist `ell_-`; after conditioning it only changes the critical-value shift. It closes the literal `g_i=0` endpoint left open by fleet04/B18 r4 and by the newest partner checkpoint.

## Second implication: source-separated/aligned twist is also paid

If the leaf set splits `L=J disjoint_union K` with `g_K=beta_K=0` and `ell_J=a g+b beta`, put

`S=X_0+ell_K dot X_K`, `C=g dot X_J`, `D0=beta dot X_J`.

Then `S` is genuinely independent of `(C,D0)` and `||p_S||_infinity<=1` by convolution with the original `X_0`. The normalized pair `(C/gamma,D0)` is a two-dimensional orthogonal projection of an ORIGINAL product block, so LPP gives pair-density cap at most 2 and hence `||(C,D0)||_infinity<=2/gamma`. The completed fleet02/B18 theorem `QFORM-CAPPED-SCALAR-DEPENDENT-PAIR-v1` applies exactly to

`Q=2SC+2aC^2+2bCD0+dD0^2`

and yields

\[
\boxed{\ \|p_Q\|_\infty\le 3\,4^{2/3}(|d|\gamma^2)^{-1/3}.\ }
\]
At `hD=|d|gamma^2>=1/5` this is at most `12.926608141`. Exact coefficient alignment is the special case `K=empty`.

The first still-unpaid local state is therefore genuinely punctured and source-entangled: a heavy witness with `0<|g_i|<1/64`, no applicable diffuse exit, and a twist component that cannot be peeled onto coordinates disjoint from both `g` and `beta`. Small nonzero `g_i` cannot be replaced by zero under arbitrary unbounded cap-one inputs.
