SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B14, 2026-09-24T03:38:22Z.
attacking: overlap-through-the-square localization: keep a transverse original/product-bank hub inside the square vertex while averaging a source-disjoint random slope, with no support or moment assumptions.

# Early calculation

The existing interactive mixed-square receiver (`proofnet24/QFORM-density/interactive/20260923T211300Z-hub-square-receivers/REPORT.md`, Section 2) assumes the linear coefficient of the square hub depends only on the light bank. The calculation below tests whether that coefficient may depend arbitrarily on the transverse hub itself without losing the density bound.

Let `W,U,Z` be mutually independent, with one-dimensional density caps

`||p_W||_infinity <= K_W`, `||p_U||_infinity <= K_U`.

Let `D=D(Z)` have a Lebesgue density with `||p_D||_infinity <= M`, let `R=R(Z)` be arbitrary measurable, let `Phi=Phi(U,Z)` be arbitrary measurable, and let `a!=0`. Set

`Q = a (W + Phi(U,Z))^2 + D(Z) U + R(Z)`.

Conditional on `(U=u,Z=z)`, translation of `W` is free and the square pushforward density is bounded by

`K_W |a|^(-1/2) |v|^(-1/2) 1_{a v>0}`.

Fix `z` with `d=D(z)!=0`. The variable `dU` has density cap `m=K_U/|d|`. For every output target `s`, the conditional density therefore obeys

`p_{Q|Z=z}(s)
 <= K_W |a|^(-1/2) int_{a(s-R(z)-v)>0} |s-R(z)-v|^(-1/2) p_{dU}(v) dv`.

The one-sided bathtub inequality for a probability density `g<=m` is

`sup_t int_{v<t} (t-v)^(-1/2) g(v)dv <= 2 sqrt(m)`,

and the same bound holds on the other half-line. Hence

`||p_{Q|Z=z}||_infinity <= 2 K_W sqrt(K_U/(|a d|))`.

If a real random variable has density cap `M`, the symmetric half-Riesz bathtub estimate gives

`E |D|^(-1/2) <= 2 sqrt(2M)`.

Averaging in `Z`, with no need to separate `D` from `R`, yields

`||p_Q||_infinity <= 4 sqrt(2) K_W sqrt(K_U M/|a|)`.

Equivalently, writing the random slope as `D=2S` and assuming `||p_S||_infinity<=M_S`,

`||p_Q||_infinity <= 4 K_W sqrt(K_U M_S/|a|)`.

This is uniform in the arbitrary overlap `Phi(U,Z)` inside the square vertex. The restriction that the residual outside the square is `R(Z)` rather than arbitrary `R(U,Z)` is essential to this proof: an arbitrary U-dependent residual could cancel the affine slope before the one-sided Riesz integral is paid.

Next checks: (i) compile `W,U,S` from disjoint original-coordinate product banks using the source-valid one-dimensional projection cap; (ii) compare on the literal three-variable form `aW^2+cUZ` to account04/B14 r10; (iii) check whether the same conclusion is already contained in a more recent receiver before promoting the scoped theorem.

Status: early calculation only; full QFORM remains OPEN.
