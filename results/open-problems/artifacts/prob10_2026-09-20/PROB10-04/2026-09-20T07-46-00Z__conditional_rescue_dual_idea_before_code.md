# PROB10-04 idea before code — condition on six rescue aggregates and dualize the remaining Díaz entropy program

Runtime model: **GPT-5.6 Sol; reasoning level UNVERIFIED — not GPT-6 maximum.**

## New idea

Do **not** continue tuning the rounded Díaz saddle.  Replace the previous planned outer interval optimization by an entropy-dual certificate.

The naive version would try to claim that Díaz et al.'s critical-point expression (their equation (25)) upper-bounds `F(x)` for arbitrary positive multipliers.  Before using that, attack its negation.  The copy-count factor has the wrong curvature: for one positive-copy simplex with total mass `lambda=1` and multiplier product `r=nu_ps*mu_ps=2`, the relevant term is

\[
H(x)=x\log x+(1-x)\log(1-x)-x\log 2.
\]

At the stationary split `x=2/3`, `H=-\log 3`, while at the boundary `x=0`, `H=0`.  Hence `0\le -\log 3` is false.  So equation (25), although correct at a critical point, is **not** a free global Gibbs upper bound.  This kills the all-at-once dual route.

The repair is to condition on the three copy masses

\[
(\ell_{ps},\ell_{ns1},\ell_{ns2}),
\]

for which the positive-curvature copy term is constant, and then dualize every remaining negative-entropy block by the log-sum inequality.  For the rescue refinement, also condition on only three normalized aggregate coordinates

\[
q=Q_{safe}/\ell_{ps},\qquad
\beta=B_{can}/\ell_{nu},\qquad
e=E_1/\ell_{ns1},
\]

with the zero-denominator boundary convention `q=0`, `beta=0`, or `e=0` as appropriate.  Every feasible configuration maps into the compact relaxed six-scalar domain

\[
0\le \ell_{ps}\le\lambda_p,
\quad \ell_{ns1},\ell_{ns2}\ge0,
\quad \ell_{ns1}+\ell_{ns2}\le\lambda_n,
\quad (q,\beta,e)\in[0,1]^3.
\]

The iid-priority rescue factor from the preceding run becomes

\[
s_i(q,\beta,e)=1-\frac12\beta q^i e\in[1/2,1].
\]

For each degree `(i,1)`, replace the source variable partition `nu_ps^i+nu_ns1` by

\[
\Psi^{R}_{i,1}=\nu_{ps}^i s_i+z\nu_{ns1},
\]

where `z>0` is the dual variable for the aggregate constraint `E_1=e ell_ns1`.

For clause types, introduce two real tilts `eta,zeta`.  If

- `r_Q(alpha)=ps(alpha) 1{ps(alpha)+ns(alpha)>=2}` is the number of safe positive slots contributed by clause type `alpha`, and
- `r_B(alpha)=1` for the two blocking types `((0,1),(1,1))`, `((0,1),(0,2))` and zero otherwise,

use the tilted clause partition

\[
\Psi_k^{Q,B}(\mu;\eta,\zeta)
=\sum_{\alpha:p(\alpha)=k}\frac{2}{w(\alpha)!}
\mu_{ps}^{ps(\alpha)}\mu_{ns1}^{ns1(\alpha)}\mu_{ns2}^{ns2(\alpha)}
\exp\{\eta r_Q(\alpha)+\zeta r_B(\alpha)\}.
\]

The exact missing lemma to prove in this run is:

> **Six-scalar conditional dual lemma.**  Conditional on the six outer coordinates above, the rescue-corrected high-dimensional Díaz entropy maximum equals, on every relative-interior feasible fiber, the infimum of an explicit finite-dimensional dual over `(nu_ps,nu_ns1,nu_ns2,mu_ps,mu_ns1,mu_ns2,z,eta,zeta)`, and is always bounded by that dual on boundary fibers.  Consequently the adversarial primal maximization can be relaxed from the source ambient `K=7223` variables at `M=23` to a compact six-scalar outer supremum.

This would remove the need for a 7,223-variable interval cover and, unlike the false all-at-once dual, would remain valid on boundary faces.  It would **not** by itself move the source threshold endpoint; the next obligation would be a rigorous interval certificate for the six-scalar outer supremum at some `alpha<4.4898`.

## Three approaches to compare in the report

1. **All-at-once Gibbs dual:** try and refute it with the exact two-state copy-simplex obstruction above.
2. **Conditional six-scalar dual:** prove it by blockwise log-sum / relative-entropy inequalities; this is the main route.
3. **Eliminate `(q,beta,e)` by a linearized rescue penalty:** test whether `-log(1-x)>=x` plus Fenchel/Young can yield a separable global lower bound on the rescue product.  The expected obstruction is that on a domain touching `q=0`, `beta=0`, or `e=0`, no strictly positive affine lower bound on the product can hold; Young gives the wrong inequality direction for an upper count.

No code should be written unless this mathematical reduction produces a finite claim worth checking.
