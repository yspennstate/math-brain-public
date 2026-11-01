# Supplemental audit of `GLOBAL_REFLECTION.md`

The stated double-cone Poisson masses and their Laplace coefficient are correct. The prior marked process has intensity `alpha*c_alpha*|z|^{-1-alpha} dz P_U(du)` on both signs. The selector for positive `z` is the event `(Xu)_2>0`, and for negative `z` it is `(Xu)_1>0`. Each projected stable coordinate is continuous and symmetric, so each mark event has probability `1/2`, irrespective of the other coordinate. Positive and negative `z` restrictions of a Poisson process are independent, hence `P_2` and `P_1` are independent; the initialization theorem also makes their entire process `N` independent of `(F,C)`.

For `p=alpha/2` and `lambda>=0`, a direct one-sided intensity calculation is

\[
\int_0^\infty \alpha c_\alpha z^{-1-\alpha}(1-e^{-\lambda z^2})\,dz
=c_\alpha\Gamma(1-p)\lambda^p.
\]

Thinning by the independent support mark multiplies this exponent by `1/2`. Thus each claimed Laplace transform is exactly `exp[-(c_alpha/2)Gamma(1-alpha/2)lambda^(alpha/2)]`. There is no second factor of `1/2` for choosing a sign: the positive-side tail intensity already has coefficient `c_alpha`, while the displayed PPP density covers both signs.

I also checked the reflected endpoint signs. Positive `z` gives endpoint output `+z²(u,v)`; negative `z` gives `-z²(v_minus,u_minus)`. These produce equation (V). On a released normal, the endpoint action is `G r`; on a reflected zero set it is the corresponding Schur diagonal action. All have nonnegative off-diagonal entries for `rho>0`, so the mixed-sign invariance calculation is consistent. The independent sign-invariance and finite-cutoff quantifier repairs in `reviews/h03_global_review.md` are still needed to justify the full network transfer.

The simple stable masses hold because the **initial double cone** makes the terminal selector a single initial-mark sign event. The broader all-mixed finite classifier in `ALL_MIXED_ENTRANCE.md` can depend on `gamma`, `R`, and the full original mark; replacing its masses by these stable half-thinnings would be unjustified. This audit does not add a proof of the proposed all-mixed residual-coupled law.
