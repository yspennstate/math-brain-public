# Threshold noise is not yet weighted block-increment chaos

literature comparison is a scope audit, not a new FPP theorem.  The geometric
estimate needed to apply the lemma to point-to-point FPP remains open.  An
independent referee should check the exact current bytes before this note is used
as a campaign dependency.

This note is read together with
`BLOCK_INCREMENT_NOISE_SPLIT_20260816.md` (SHA-256
`c106b719e76e584157c36a840a55fbb3c68571e0b4386ff509bec699366f0de0`).
That note replaces the Cauchy--Schwarz term
`sqrt(A4 Pbar)` by the exact weighted overlap

\[
 S_z(t)=\sum_L \mathbb E[z_L(Y)z_L(Y^{(t)})],\qquad
 z_L=(X^L-X)^+,\quad t=1-\kappa,
\]

on the product space carrying the original and replacement block variables.
Here `Y^(t)` is obtained by retaining each product coordinate with probability
`t` and otherwise resampling it independently.

Two recent results look close but do not supply this estimate:

* Elboim, *Small ball probabilities for the passage time in planar
  first-passage percolation*, arXiv:2406.10971v2, Theorem 1.1, proves for
  absolutely continuous weights on `(0,infinity)` that
  \[
  \sup_a \mathbb P\{T(0,x)\in[a,a+1]\}
      \leq C/\sqrt{\log\|x\|}.
  \]
* Dembin--Elboim, *Noise sensitivity and variance lower bound for minimal
  left-right crossing of a square in first-passage percolation*,
  arXiv:2505.03211v1, Theorem 1.2, proves noise sensitivity of a fixed-quantile
  event for a constrained left--right crossing time with two-point weights.
  The unconditional range is
  `k <= exp(-C sqrt(log n)) sqrt(n)`; a many-sided limit-shape hypothesis gives
  `k <= n^(1-epsilon)`; their stronger uniform-curvature hypothesis gives the
  full square crossing.  They explicitly note that this curvature hypothesis
  is not known for any ordinary lattice-FPP weight law.

The purpose here is to state exactly what a threshold-noise result would have
to control before it can close the weighted MG2B engine.


Let `(Omega,mu)` be a finite product probability space and let `T_t`,
`0 <= t <= 1`, be the usual resampling-noise operator.  Thus `T_t` is a
self-adjoint positive contraction, and on the Efron--Stein component indexed by
`S` it has eigenvalue `t^|S|`.

Let `z >= 0` lie in `L^2(mu)`, let `(Y,Y^(t))` be the corresponding noise
coupling, and put

\[
 \nu_z(t;s):=
 \operatorname{Cov}\big(\mathbf 1_{\{z(Y)>s\}},
                         \mathbf 1_{\{z(Y^{(t)})>s\}}\big).
 \tag{1}
\]

Positivity of `T_t` gives `nu_z(t;s) >= 0`.  For every cutoff `R >= 0`,

\[
 \operatorname{Cov}(z(Y),z(Y^{(t)}))^{1/2}
 \leq
 \int_0^R \sqrt{\nu_z(t;s)}\,ds
 +\Big(\mathbb E[(z-R)_+^2]\Big)^{1/2}.
 \tag{2}
\]

### Proof

Write `g_s=1_{z>s}-P(z>s)`.  In `L^2`,

\[
 z\wedge R-\mathbb E[z\wedge R]=\int_0^R g_s\,ds.
\]

Also

\[
 \nu_z(t;s)=\langle g_s,T_tg_s\rangle
            =\|T_t^{1/2}g_s\|_2^2.
\]

Apply Minkowski's integral inequality after `T_t^(1/2)`.  For the remainder,
use that `T_t^(1/2)` is a contraction and

\[
 \|(z-R)_+-\mathbb E[(z-R)_+]\|_2
 \leq \big(\mathbb E[(z-R)_+^2]\big)^{1/2}.
\]

The left side of (2) is exactly
`||T_t^(1/2)(z-Ez)||_2`.  This proves (2).  Truncation also proves the statement
when the displayed integral is infinite.  No monotonicity of `z` in the product
coordinates is used.

For a family `(z_L)`, define

\[
 C_z:=\sum_L(\mathbb Ez_L)^2,
 \quad
 A_L(R):=\int_0^R\sqrt{\nu_{z_L}(t;s)}\,ds,
 \quad
 \tau_L(R):=\big(\mathbb E[(z_L-R)_+^2]\big)^{1/2}.
\]

Then the exact mean--covariance split and (2) give

\[
 \boxed{
 S_z(t)\leq C_z+\sum_L\big(A_L(R_L)+\tau_L(R_L)\big)^2.}
 \tag{3}
\]

Consequently a sufficient replacement for block chaos is the quantitative,
summed condition

\[
 \frac{C_z}{M D_n}
 +\frac1{M D_n}\sum_L
       \big(A_L(R_L)+\tau_L(R_L)\big)^2
 \leq \eta.
 \tag{4}
\]

This exposes two obligations.  Noise sensitivity can address only the covariance
term.  It never removes the static floor `C_z`.  Moreover, convergence at one
threshold does not control the integral in (3).  Even pointwise convergence at
every fixed threshold is insufficient without an integrable uniform estimate and
tail control.  If `z_L <= B_L` and
`sup_{0<=s<=B_L} nu_{z_L}(t;s) <= eps_L`, for example, (3) yields only

\[
 S_z(t)\leq C_z+\sum_L B_L^2\epsilon_L.
 \tag{5}
\]

The factors `B_L^2` and the sum over blocks cannot be discarded.

Here is a finite-product sanity check showing why one quantile is logically too
weak.  Let `A_n` be the `{0,1}` version of the parity of `n` fair bits, let `B`
be one further fair bit, independent of them, and set
`z_n=A_n+B/4`.  At the median threshold `1/2`,
`1_{z_n>1/2}=A_n`, whose noise covariance is `t^n/4` and tends to zero for every
fixed `t<1`.  Nevertheless

\[
 \operatorname{Cov}(z_n(Y),z_n(Y^{(t)}))
 =\frac{t^n}{4}+\frac{t}{64}\longrightarrow\frac{t}{64}.
 \tag{6}
\]

The stable low-amplitude coordinate is invisible at that median threshold and is
visible to the weighted covariance.

Even convergence at every fixed layer is insufficient without tail uniformity.
For `p_n -> 0`, let `B_n` be a Bernoulli-`p_n` product coordinate and put
`w_n=B_n/sqrt(p_n)`.  For every fixed `s >= 0`, the threshold covariance is at
most `t p_n` and tends to zero, while
`Cov(w_n(Y),w_n(Y^(t)))=t(1-p_n) -> t`.  This is why (2) retains an explicit
tail term instead of invoking dominated convergence informally.

There is also an exact passage-time version of the layer cake.  Put

\[
 h_{L,u}:=\mathbf 1_{\{X\leq u<X^L\}}.
\]

Then, by Tonelli and the identity

\[
 z_L=(X^L-X)^+=\int_{\mathbb R}h_{L,u}\,du,
\]

\[
 \operatorname{Cov}_t(z_L,z_L)
 =\iint_{\mathbb R^2}
   \operatorname{Cov}_t(h_{L,u},h_{L,v})\,du\,dv.
 \tag{7}
\]

Thus the natural Boolean objects are *directed block-pivotal layer events* for
the pair `(X,X^L)`, not threshold events for `X` alone.

## 2. Exact boundary of the two literature results

### Elboim's point-to-point small ball theorem

The theorem is uniform in the interval location and has the useful explicit
`1/sqrt(log distance)` rate.  Its proof applies a continuous Mermin--Wagner
perturbation on endpoint-anchored dyadic annuli.  Every endpoint-to-endpoint path
crosses every annulus, so the accumulated drift pushes one passage time through a
unit interval.

That mechanism does not directly control (1).  In `z_L=X^L-X`, a common annular
perturbation moves both passage times and can cancel in their difference.  An
anti-symmetric perturbation of the original and replacement variables inside the
chosen block is a conceivable new argument, but it would need a fresh product-cost
and unavoidable-crossing calculation.  The campaign already recorded the related
anchored-versus-free-endpoint localization boundary in
`D_lowerbound_blocktime_attempt_20260812.md`; the present mismatch is different:
it is one passage time versus a coupled passage-time difference.

### Dembin--Elboim's crossing-threshold theorem

For their Boolean event `f=1_{tau >= q_alpha}`, equations (4.4) and (4.9) show the
key mechanism: pivotality forces both geodesic use and passage time in the one-step
window adjacent to the quantile, leading schematically to

\[
 \sum_e \operatorname{Inf}_e(f)^2
 \leq C K_n\,
 \mathbb P\{\widetilde\tau\in[q_\alpha-b+a,q_\alpha]\}^2.
 \tag{8}
\]

Their small-ball estimate and a vertically symmetric crossing geometry then make
the right side vanish.  This is a valuable template, but the theorem itself does
not instantiate (3):

1. `tau` is a minimal left--right crossing (with a constrained-width version),
   whereas the campaign variable is a fixed point-to-point passage time.
2. Their noise retains or resamples individual edges independently.  The MG2B
   filtration retains or resamples whole paired block coordinates.  The latter is
   much coarser noise.
3. Their observable lives on the original edge environment.  Here `z_L` is a
   function on the enlarged original-plus-replacement product space.
4. They control one fixed-quantile indicator.  Equation (3) needs an integrated,
   quantitative family of increment-tail indicators for every relevant `L`.
5. Even perfect decorrelation leaves `C_z=sum_L(Ez_L)^2`.
6. The proof uses vertical translation symmetry to spread crossing influences;
   the fixed-endpoint geometry has no such symmetry.
7. Their main noise theorem is for a two-point law.  Elboim's point-to-point
   small-ball theorem is for absolutely continuous laws.  Neither result alone
   covers the campaign's law-uniform bootstrap.

The noise-granularity issue is already decisive in an abstract test.  Put the
parity of `N` fair edge bits inside one block.  Under independent edge noise its
covariance is `t^N/4`, but under retain-or-refresh noise on the whole block it is
`t/4`.  Thus edge-noise sensitivity cannot simply be relabelled as the block-noise
estimate used in (3).

There is, however, an exact comparison at a much weaker edge-noise scale.  Suppose
the independent edge-pair coordinates are partitioned into blocks of size at most
`m`.  Let `T_t^blk` retain each whole block with probability `t`, and let
`T_q^edge` retain each edge-pair coordinate independently with probability

\[
 q=t^{1/m}.
\]

If `f=sum_S f_S` is the edge-coordinate ANOVA decomposition and `b(S)` is the
number of blocks met by `S`, then

\[
 \langle f,T_t^{\rm blk}f\rangle
 =\sum_S t^{b(S)}\|f_S\|_2^2
 \leq\sum_S q^{|S|}\|f_S\|_2^2
 =\langle f,T_q^{\rm edge}f\rangle. \tag{G}
\]

Indeed `|S| <= m b(S)`, hence `q^|S| >= t^{b(S)}`.  The parity example attains
equality when all `N=m` bits lie in one block.  For fixed block-noise parameter
`t<1`, the edge resampling rate required by (G) is
`1-q=Theta(1/m)`.  The qualitative theorem “noise sensitive for every fixed edge
version would need a quantitative pair-edge theorem down to `Theta(1/m)`.

So it would be incorrect to cite either paper as an existing proof of weighted
block chaos or of (4).


For each block `L` and layer `s`, set

\[
 g_{L,s}=\mathbf 1_{\{(X^L-X)^+>s\}}.
\]

The next useful theorem is not generic “noise sensitivity of FPP.”  It is an
integrated block-increment estimate of the form

\[
 C_z+\sum_L\left(
   \int_0^{R_L}
   \sqrt{\operatorname{Cov}_t(g_{L,s}(Y),g_{L,s}(Y^{(t)}))}\,ds
   +\tau_L(R_L)
 \right)^2
 \leq \eta M D_n,
 \tag{9}
\]

at the fixed `t=1-kappa` required by the MG2B constants.

A Dembin--Elboim-style route to (9) would require two new inputs:

* an edge-level pivotal-containment statement for `g_{L,s}`.  Changing a further
  edge must force a relevant geodesic-use event and place the *difference*
  `X^L-X` in a short window around `s`;
* a summed, rate-bearing small-ball/geometry bound for those difference windows,
  uniform enough in `L` and integrable in `s` to survive (9), together with an
  estimate for pair-edge noise at the vanishing rate required by (G), or a direct
  paired-block argument.

For two-point weights, changing one edge changes each passage time by at most one
weight gap, suggesting a constant-width difference window.  But whether the
relevant edge belongs to one of the old/new geodesics and whether the resulting
influence sum has the needed block normalization are exactly the missing geometric
steps.  Resampling an entire paired block can have block-size oscillation, and the
parity example shows why a same-parameter edge estimate cannot repair this.  The
only generic comparison (G) spends a factor of the block size in the noise rate.
These steps should be proved from FPP geometry, not inferred from (8).

## 4. Strongest case that this note is too pessimistic

The influence argument behind (8), rather than its stated theorem, may extend to
the pair observable `g_{L,s}`.  If one obtains a uniform squared-influence bound
whose integral in (9) is `o(MD_n)` and separately proves `C_z=o(MD_n)`, the recent
threshold-noise machinery could close the weighted engine.  The decisive check is
therefore concrete: derive the exact pivotal containment for `g_{L,s}` under one
outside-coordinate switch and run the squared-influence sum with the point-to-point
available lemma.

## 5. Disposition

  edge-to-block noise comparison (G).
* **Verified prior art:** the two cited theorem statements and the influence/small-
  ball mechanism (8).
* **Not proved:** (9), a point-to-point analogue of the crossing influence estimate,
  or any improvement of the FPP variance exponent.
* **Correction to the campaign map:** recent Boolean threshold-noise results are
  relevant ingredients, but they do not discharge weighted block chaos without the
  static-floor and integrated increment-layer estimates above.
