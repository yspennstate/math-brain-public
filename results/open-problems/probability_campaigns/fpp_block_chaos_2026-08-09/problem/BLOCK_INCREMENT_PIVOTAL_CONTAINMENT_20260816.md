# A tie-safe pivotal window for positive block increments

Date: 2026-08-16  
Status: deterministic containment and influence ledger proved; the required
point-to-point geometry and integrated rate remain open

Companions:

* `BLOCK_INCREMENT_NOISE_SPLIT_20260816.md`, SHA-256
  `c106b719e76e584157c36a840a55fbb3c68571e0b4386ff509bec699366f0de0`;
  `1d912a8123f49b831d91bd83b85d1514707e75be2053e82926c9a4108d44e293`.

The second companion identifies the missing Boolean observables

`g_(L,s)=1_{(X^L-X)^+>s}`.

This note proves the first deterministic step in a Dembin--Elboim-style
influence argument for those observables.  It is deliberately formulated at
the level of one scalar edge copy.  A paired block contains both the original
and replacement copies, while the available FPP pivotal argument changes one
two-point edge weight at a time.

## 1. Abstract two-functional lemma

Fix all coordinates except one scalar coordinate `e`, whose two values are
`a<b`, and put `d=b-a`.  Let `T_0,T_1` be minima of path costs in which this
coordinate occurs with coefficient either zero or one.  This includes the case
where the same original edge occurs in both functionals, and the case where one
functional ignores the coordinate.

Write `omega^-` and `omega^+` for the configurations with the coordinate fixed
to `a` and `b`, respectively, and set

`T_r^-=T_r(omega^-),   T_r^+=T_r(omega^+),
 delta_r=T_r^+-T_r^-`                                             (1)

for `r=0,1`.  Monotonicity and the one-edge Lipschitz bound give

`0<=delta_r<=d`.                                                   (2)

Let `Pi_r^-` be the event that every minimizing path for `T_r^-` uses the
scalar coordinate `e`.  Ties are allowed.  If `delta_r>0`, then `Pi_r^-`
holds: an avoiding minimizer would have unchanged cost after the increase and
would force `delta_r=0`.

Put

`Delta^pm=T_1^pm-T_0^pm,   z^pm=(Delta^pm)^+,
 g_s^pm=1_{z^pm>s}`.                                            (3)

Then the following directional containments are exact:

`{g_s^-=0, g_s^+=1}
 subset {s-d<z^-<=s} intersect Pi_1^-`,                         (4)

`{g_s^-=1, g_s^+=0}
 subset {s<z^-<=s+d} intersect Pi_0^-`.                         (5)

In particular,

`{g_s^-!=g_s^+}
 subset {|z^--s|<=d} intersect (Pi_0^- union Pi_1^-).`           (6)

### Proof

From (1),

`Delta^+-Delta^-=delta_1-delta_0`,                              (7)

so `|Delta^+-Delta^-|<=d`; the positive-part map is one-Lipschitz,
and hence `|z^+-z^-|<=d`.

On the event in the left side of (4), `z^+>z^-`.  Therefore
`Delta^+>Delta^-`, including the case in which `Delta^-<=0`, and (7) gives
`delta_1>delta_0`.  In particular `delta_1>0`, so every lower-configuration
minimizer for `T_1` uses `e`.  The threshold crossing and the Lipschitz bound
also give `s-d<z^-<=s`.  This proves (4).  Interchanging the roles of zero and
one gives `delta_0>delta_1`, the `T_0` use event, and the window in (5).
Their union proves (6).  No canonical tie rule or uniqueness assumption was
used.

## 2. Exact influence consequence for a two-point law

Now let the scalar coordinates be independent with

`P(omega_e=a)=p,   P(omega_e=b)=1-p`,                          (8)

where `0<p<1`, and let `sigma_e` toggle the value of coordinate `e`.  The event
that `e` is pivotal for `g_s` depends only on the other coordinates.  Therefore

`Inf_e(g_s)=p^(-1) P(e pivotal, omega_e=a).`                    (9)

In the actual environment on `{omega_e=a}`, let `Pi_r(e)` denote the
intersection of all minimizing paths for `T_r`.  Define

`h_e^1(s)=P(omega_e=a, s-d<z<=s, e in Pi_1(e)),`               (10)

`h_e^0(s)=P(omega_e=a, s<z<=s+d, e in Pi_0(e)),`               (11)

and `h_e(s)=h_e^0(s)+h_e^1(s)`.  Equations (4)--(5) imply

`Inf_e(g_s)<=p^(-1) h_e(s).`                                  (12)

Consequently, with

`H(s)=max_e h_e(s),   B(s)=sum_e h_e(s)`,                     (13)

one has the exact ledger

`sum_e Inf_e(g_s)^2 <= p^(-2) H(s) B(s).`                     (14)

This uses only `h_e^2<=H h_e`; there is no hidden independence or
left--right multiplication.

Suppose all path weights lie in `[a,b]`, the endpoints have graph distance
`ell`, and an admissible path of `ell` edges is available.  Every geodesic then
has at most `(b/a)ell` edges.  Summing (10)--(11) pointwise over the scalar copies
therefore gives

`B(s)<= (b/a)ell P(s-d<z<=s+d).`                              (15)

Thus

`sum_e Inf_e(g_s)^2
 <= p^(-2)(b/a)ell H(s) P(s-d<z<=s+d).`                       (16)

The two half-windows in (10)--(11) are disjoint, which is why (15) has only
one length factor.  Dropping the condition `omega_e=a` or replacing the
intersection of all geodesics by a chosen geodesic only weakens the bound.

## 3. Specialization to the campaign increment

Take `T_0=X` and `T_1=X^L` on the enlarged product space containing every
original edge weight and every independent replacement copy in block `L`.
Then `z=(X^L-X)^+`.

* An original edge outside `L` occurs in both passage times.
* An original edge in `L` occurs only in `X`.
* A replacement edge in `L` occurs only in `X^L`.
* A replacement edge outside `L` is ignored and has zero influence.

All four cases satisfy the abstract lemma.  Hence (4)--(16) give the exact
individual original or replacement edge weights.

There is a small but important granularity distinction.  If a macroscopic
block contains at most `m` physical edges, its paired original--replacement
version contains at most `2m` scalar coordinates.  Comparing fixed block
retention `t` with independent scalar-copy retention therefore uses

`q=t^(1/(2m))`,                                                (17)

and gives `1-q=Theta(1/m)` for fixed `t<1`.  If each four-state
original--replacement pair is packaged as one coordinate, the exponent is
`1/m`, but then a pair-coordinate pivotal theorem, rather than the existing
one-edge theorem, is required.  Equation (17) is the direct scalar route.

## 4. Quantitative BKS bridge and its block-size cost

There is a dimension-free quantitative theorem that converts (14) into a
noise-covariance bound.  Keller and Kindler's Theorem 7
([arXiv:1003.1839](https://arxiv.org/abs/1003.1839)) applies to arbitrary,
not necessarily monotone, Boolean functions under the biased product measure.
If scalar coordinates are resampled with probability `epsilon`, put

`W(g)=p(1-p) sum_e Inf_e(g)^2`.

Their result gives

`Cov(g(omega),g(omega^epsilon))
 <= (6e+1) W(g)^theta_p(epsilon)`,                           (18)

where

`theta_p(epsilon)
 =epsilon/(epsilon+log(2B(p)e)+3log log(2B(p)e))`             (19)

and `B(p)` is their biased hypercontractivity constant.  Here the second copy
retains a scalar coordinate with probability `1-epsilon`, matching the noise
operator convention in the companion notes.

For a paired block containing at most `m` physical edges, set

`q=t^(1/(2m)),   epsilon=1-q`.

refined scalar-copy product, gives for every layer

`nu_(L,s)^blk(t)<=nu_(L,s)^scalar(q).`                        (20)

Combining (16), (18), and (20) therefore yields

`nu_(L,s)^blk(t)
 <=(6e+1)[((1-p)/p)(b/a)ell H_L(s)
             P(s-d<z_L<=s+d)]^theta_p(1-t^(1/(2m))).`        (21)

If the bracket is at least one, the bound is merely vacuous, as it should be.
For fixed `p` and fixed `0<t<1`,

`1-t^(1/(2m))=(-log t)/(2m)+O(m^(-2)),
 theta_p(1-t^(1/(2m)))=Theta_(p,t)(1/m).`                    (22)

This is a sharp accounting warning.  Through generic quantitative BKS, making
the block-layer covariance tend to zero requires the logarithm of the
reciprocal influence bound in (21) to dominate `m`.  A polynomially small
squared-influence sum gives no decay when `m` grows faster than `log ell`.  This
does not prove that the FPP observable is stable; it proves only that the
block-noise parameter.

There is also a universal lower bound showing that this is not repaired by a
better squared-influence estimate for a nondegenerate layer.  If `N_sc` scalar
coordinates are active, product Poincare and Cauchy--Schwarz give

`Var(g)<=p(1-p) sum_e Inf_e(g)`,                              (23)

`W(g)>=Var(g)^2/(p(1-p)N_sc).`                               (24)

Thus, if `Var(g)>=v_0>0` and `N_sc` is polynomial in the passage scale, then
even the smallest possible right side furnished by (18) has

`W(g)^theta_p(1-t^(1/(2m)))
 >=exp(-O_(p,t,v_0)(log N_sc/m)).`                            (25)

It cannot tend to zero when `m` dominates `log N_sc`.  This is a limitation of
the universal influence theorem, not a lower bound on the true block-noise
covariance.

The campaign's intended tiling is far inside this mismatch.  CRUX 9.7
(`CRUX_iteration_arithmetic.md`, SHA-256
`58593b9aaf82676e746933bf6ec4aed36529bec217d1ed60627e8acd051e98aa`)
uses longitudinal size `n` and transversal width `W_blk=sqrt(nQ)`.  A block
therefore contains `m=Theta(n W_blk)` physical edges.  At the conjectural
choice `Q=n^(1/3)`, this is `Theta(n^(5/3))`; at the Kesten-scale choice
`Q=n^(1/2)`, it is `Theta(n^(7/4))`.  Any polynomial-size finite localization
has `log N_sc=O(log n)`.  Hence the scalar-edge BKS route cannot certify fixed
whole-block noise sensitivity for a nondegenerate layer at either campaign
scale, even with optimally spread individual influences.

## 5. What is still missing

Dembin and Elboim obtain their crossing influence bound by combining the
analogue of (12) with vertical translation symmetry, a bound on the number of
unavoidable geodesic edges in a column, and a one-step small-ball estimate;
see equations (4.4)--(4.9) of
[arXiv:2505.03211v1](https://arxiv.org/abs/2505.03211v1).

For the fixed-endpoint pair increment, (15) supplies the global `B(s)` bound,
but no existing result supplies the required per-edge spreading bound on
`H(s)`.  The point-to-point small-ball theorem controls one passage time, not
the difference window in (10)--(11), and the fixed-endpoint geometry lacks the
vertical symmetry used for a crossing.

A sufficient next input would be a rate-bearing estimate of the form

`H_L(s)<=kappa_L(s) P(s-d<z_L<=s+d)`                          (26)

with `ell kappa_L(s)` small enough that the logarithm of the reciprocal of
`ell kappa_L(s) P(s-d<z_L<=s+d)^2` dominates the paired block size `m`, uniformly
and integrably in `s`.  Equations (23)--(25) show, however, that combining such
an estimate only through generic scalar-edge BKS still cannot close the
campaign's growing blocks on nondegenerate layers.  A successful proof needs a
direct paired-block covariance estimate, a genuinely block-adapted theorem
using more than scalar influences, or a redesigned engine with much smaller
independent blocks.  None of these conclusions is proved here.

## 6. Negative controls

* The lemma is tie-safe because positive passage-time change forces use by
  every lower-configuration minimizer.  Merely saying that a canonical
  geodesic uses the edge would not prove the converse and is not used.
* The window has total width `2(b-a)`, not `b-a`: the increment may cross the
  threshold in either direction when a common edge is raised.
* The scalar-copy refinement doubles the maximum coordinate count per paired
  block.  Using `t^(1/m)` together with an individual-edge theorem would mix
  two different noise granularities.
* A straight-path environment saturates the use event and has no spatial
  spreading.  It is a necessary negative control for any proposed (26).

An independent proof audit is required before this note is used as a campaign
dependency.
