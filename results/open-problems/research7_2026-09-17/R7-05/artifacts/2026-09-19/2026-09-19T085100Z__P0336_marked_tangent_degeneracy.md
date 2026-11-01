# P0336 — full marked tangent degeneracy at second variation

Worker: `R7-05`  
Canonical target: `P0336`  
Source: Eustasio del Barrio, Alberto González-Sanz, Jean-Michel Loubes, David Rodríguez-Vítores, *Distributional Limit Theory for Optimal Transport*, arXiv:2505.19104v2, Problem 4.  
Status after this artifact: **OPEN / PARTIAL**.  
Frozen metric: `SEL_ID = 0` throughout this artifact.

## 1. Why this attack was needed

The preceding R7-05 run proved two exact facts.

1. If a matched source-target pair is written as
   \[
   X=(A,S),\qquad Y=(B,T),\qquad D=B-A\in[1,3],\qquad H=T-S,
   \]
   then the empirical objective differs from the permutation-independent horizontal baseline by
   \[
   e(D,H)=\sqrt{D^2+H^2}-D.
   \]
2. For a prescribed scaled vertical mean displacement, the quadratic cell problem has the equality condition
   \[
   Z=\frac m2 D,
   \]
   and *every* horizontal coupling of the uniform horizontal marginals can lie on that equality manifold.

That left a natural possible escape: perhaps the full two-dimensional empirical fluctuations in the horizontal marks force a particular horizontal coupling when one imposes source and target compatibility, even though the scalar vertical cell problem does not.

This artifact shows that this escape also fails at the full marked tangent level. The failure is pathwise, not only after averaging over Gaussian fluctuations.

The central theorem below says that every sufficiently interior bistochastic horizontal kernel has exactly the same second-order tangent energy for every smooth marked perturbation of the two marginals. The only first-order quantity seen by the energy is the **scalar vertical flux** obtained after integrating out the horizontal marks.

---

## 2. Tangent model

Let
\[
A=[0,1],\qquad B=[2,3],\qquad I=[0,1].
\]
We use `a` for the source horizontal coordinate, `b` for the target horizontal coordinate and `s` for the limiting common vertical coordinate.

A population-optimal plan supported on equal vertical coordinates can be written
\[
\pi_0^k(da\,ds\,db\,dt)
 = k(a,b,s)\,da\,db\,ds\,\delta_s(dt),
\]
where for almost every `s`, `k(\cdot,\cdot,s)` is bistochastic:
\[
\int_B k(a,b,s)\,db=1\quad\text{for a.e. }a,
\]
\[
\int_A k(a,b,s)\,da=1\quad\text{for a.e. }b.
\]
Consequently,
\[
\iint_{A\times B} k(a,b,s)(b-a)\,da\,db
=\int_B b\,db-\int_A a\,da
=\frac52-\frac12=2.
\tag{2.1}
\]
This identity is independent of `k` and holds separately at every vertical level `s`.

For the robust realizability statement below assume in addition that
\[
k\in C^1,\qquad k(a,b,s)\ge \kappa>0.
\tag{2.2}
\]
The lower bound is not needed for the energy inequality itself; it only guarantees that an arbitrary bounded signed tangent correction can be embedded into a genuinely nonnegative nearby density for sufficiently small perturbation size.

Let the source and target marginals be perturbed smoothly as
\[
d\mu_\varepsilon=(1+\varepsilon f(a,s))\,da\,ds,
\]
\[
d\nu_\varepsilon=(1+\varepsilon g(b,s))\,db\,ds,
\]
with bounded smooth `f,g` and equal total mass. Write the vertical marginal perturbations
\[
F(s)=\int_A f(a,s)\,da,
\qquad
G(s)=\int_B g(b,s)\,db.
\tag{2.3}
\]
Define the unique zero-boundary scalar flux
\[
m(s)=\int_0^s (F(r)-G(r))\,dr.
\tag{2.4}
\]
Equal total masses imply `m(1)=0`, while by definition `m(0)=0`.

A first-order marked transport perturbation consists of:

- an edge-density correction `q(a,b,s)`, and
- a scaled vertical displacement `u(a,b,s)`, so that the target height is
  \[
  t=s+\varepsilon u(a,b,s).
  \]

The tangent source and target constraints are
\[
\int_B q(a,b,s)\,db=f(a,s),
\tag{2.5}
\]
\[
\int_A q(a,b,s)\,da
-
\partial_s\!\left(\int_A k(a,b,s)u(a,b,s)\,da\right)
=g(b,s).
\tag{2.6}
\]
Equation (2.6) follows by testing the pushed-forward target marginal against a smooth function `phi(b,t)`, expanding
\[
\phi(b,s+\varepsilon u)
=
\phi(b,s)+\varepsilon u\,\partial_s\phi(b,s)+O(\varepsilon^2),
\]
and integrating by parts in `s`. The boundary term vanishes because the total vertical flux below will vanish at `s=0,1`.

The second-order excess Euclidean energy above the fixed horizontal baseline is
\[
\mathcal E_k(u)
=
\int_0^1\iint_{A\times B}
\frac{k(a,b,s)u(a,b,s)^2}{2(b-a)}\,da\,db\,ds.
\tag{2.7}
\]
Indeed, uniformly because `1<=b-a<=3`,
\[
\sqrt{(b-a)^2+\varepsilon^2u^2}-(b-a)
=
\varepsilon^2\frac{u^2}{2(b-a)}+O(\varepsilon^4).
\tag{2.8}
\]

---

## 3. B18 — the full marked compatibility collapses to one scalar flux

Integrate (2.6) over `b` and use (2.5). Define
\[
M_u(s)
=
\iint_{A\times B}k(a,b,s)u(a,b,s)\,da\,db.
\tag{3.1}
\]
Then
\[
G(s)=F(s)-M_u'(s).
\]
Hence every tangent-feasible perturbation necessarily satisfies
\[
M_u'(s)=F(s)-G(s).
\tag{3.2}
\]
With zero boundary flux, (3.2) forces
\[
\boxed{M_u(s)=m(s).}
\tag{3.3}
\]

This is the marked flux equation. All horizontal-mark information in `f(a,s)` and `g(b,s)` disappears from the *necessary energy-bearing constraint* after one integrates the horizontal coordinates. The remaining marked mismatch may still constrain `q`, but `q` has no contribution to the second-order energy (2.7).

This is already a substantial obstruction to the previous route: the two-dimensional empirical field can affect the cost-bearing vertical motion only through the one-dimensional cumulative discrepancy `m` at tangent order.

---

## 4. B6 — exact minimization of the marked tangent energy

### Theorem 4.1 (pathwise marked tangent degeneracy)

Let `k` be any bistochastic kernel as above. Among all tangent-feasible pairs `(q,u)` satisfying (2.5)-(2.6), the vertical energy obeys
\[
\boxed{
\mathcal E_k(u)\ge \frac14\int_0^1m(s)^2\,ds.
}
\tag{4.1}
\]
Whenever the tangent constraints are realizable, equality in (4.1) requires and is attained by
\[
\boxed{
u_*(a,b,s)=\frac{m(s)}2\,(b-a).}
\tag{4.2}
\]
The minimum value is independent of the horizontal kernel `k`, even when `k=k_s` varies with the vertical level.

#### Proof

Fix `s` and abbreviate `D=b-a`. By (3.3),
\[
m(s)=\iint k u.
\]
Cauchy-Schwarz with the factors `sqrt(kD)` and `sqrt(k)u/sqrt(D)` gives
\[
\begin{aligned}
m(s)^2
&=\left(\iint \sqrt{kD}\,\frac{\sqrt{k}u}{\sqrt D}\right)^2\\
&\le
\left(\iint kD\right)
\left(\iint k\frac{u^2}{D}\right).
\end{aligned}
\]
By bistochasticity, (2.1) gives `\iint kD=2`. Therefore
\[
m(s)^2
\le
2\iint k\frac{u^2}{D}
=4\iint k\frac{u^2}{2D}.
\]
Thus the energy at level `s` is at least `m(s)^2/4`; integrating in `s` proves (4.1).

Equality in Cauchy-Schwarz holds exactly when, on the support of `k`,
\[
\frac{u}{D}=\lambda(s).
\]
The flux condition `\iint ku=m` and `\iint kD=2` then give
\[
2\lambda(s)=m(s),
\]
so
\[
u_*(a,b,s)=\frac{m(s)}2D.
\]
Substitution gives
\[
\iint k\frac{u_*^2}{2D}
=
\frac{m(s)^2}{8}\iint kD
=
\frac{m(s)^2}{4}.
\]
This proves the variational statement. ∎

The common-slope condition from the preceding run therefore survives the *full* marked perturbation problem. The point is stronger than the previous fiber calculation: it is not an ansatz after ignoring horizontal fluctuation constraints; it is the exact minimizer of the complete tangent energy subject to those constraints, provided the remaining edge-density correction can be supplied.

---

## 5. B27 — swap the quantifiers: every interior horizontal kernel works for every smooth marked perturbation

The key remaining issue is whether the horizontal perturbations `f` and `g` can actually be accommodated at the equality field (4.2). They can, for every sufficiently interior kernel, and there is an explicit formula.

### Theorem 5.1 (explicit tangent realization for arbitrary interior `k`)

Assume (2.2). Let
\[
u_*(a,b,s)=\frac{m(s)}2(b-a).
\]
Define the target-mark vertical flux density
\[
J_*(b,s)
=
\int_A k(a,b,s)u_*(a,b,s)\,da
=
\frac{m(s)}2\int_A k(a,b,s)(b-a)\,da.
\tag{5.1}
\]
Set
\[
C(b,s)=g(b,s)+\partial_sJ_*(b,s).
\tag{5.2}
\]
Then
\[
\int_B C(b,s)\,db=F(s).
\tag{5.3}
\]
Consequently the explicit signed edge correction
\[
\boxed{
q_*(a,b,s)=f(a,s)+C(b,s)-F(s)
}
\tag{5.4}
\]
satisfies both tangent marginal equations (2.5)-(2.6).

Moreover, because `q_*` is bounded and `k>=kappa>0`, for sufficiently small `|epsilon|` one has
\[
k+\varepsilon q_*\ge0.
\tag{5.5}
\]
Thus `(q_*,u_*)` is not merely a formal signed solution: it is the tangent of a genuinely nonnegative nearby edge-density family, whose target marginal agrees with `nu_epsilon` to first order.

#### Proof

First integrate (5.1) over `b`. Using the equality field and (2.1),
\[
\int_BJ_*(b,s)\,db
=
\iint ku_*
=
m(s).
\tag{5.6}
\]
Therefore, from (5.2) and (3.2),
\[
\int_BC(b,s)\,db
=
G(s)+m'(s)
=
G(s)+F(s)-G(s)
=
F(s),
\]
which is (5.3).

Now integrate (5.4) over `b`:
\[
\int_Bq_*\,db
=f(a,s)+\int_BC\,db-F(s)=f(a,s).
\]
So the source tangent marginal is correct.

Integrating (5.4) over `a` instead gives
\[
\int_Aq_*\,da
=F(s)+C(b,s)-F(s)=C(b,s).
\]
Hence, by (5.2),
\[
\int_Aq_*\,da-\partial_sJ_*(b,s)=g(b,s),
\]
which is exactly (2.6).

Finally, boundedness of the smooth data and of `k, partial_s k` makes `q_*` bounded. If `||q_*||_infty=Q`, then `k+epsilon q_*>=0` whenever `|epsilon|<=kappa/Q` (with the claim trivial if `Q=0`). The first-order pushforward expansion used to derive (2.6) then shows that the target marginal is `nu_epsilon+O(epsilon^2)` in the weak `C^2` test-function sense. ∎

### Quantifier-strengthened corollary

The order of the quantifiers is the important point:

\[
\boxed{
\textbf{For every }k\ge\kappa\text{ bistochastic, and for every smooth marked perturbation }(f,g),
\text{ the same minimum }\frac14\int m^2\text{ is attained.}
}
\tag{5.7}
\]

Thus product coupling is not distinguished from any other strictly positive bistochastic horizontal kernel by the complete first-order marked compatibility problem.

This is pathwise. One does **not** need to average over the Gaussian empirical field. Therefore taking expectation, conditioning on the vertical empirical bridge, or invoking horizontal self-averaging at this order cannot create a selector that is absent before averaging.

---

## 6. Interpretation as a marked `H^{-1}` energy

Equation (3.2) is a one-dimensional continuity equation. The scalar flux is fixed by
\[
m'(s)=F(s)-G(s),\qquad m(0)=m(1)=0.
\]
The horizontal marks contribute an effective mobility
\[
\iint k(a,b,s)(b-a)\,da\,db=2.
\]
The minimum energy is therefore
\[
\frac1{2\times 2}\int_0^1m(s)^2\,ds
=
\frac14\int_0^1m(s)^2\,ds.
\tag{6.1}
\]
This is exactly the linearized one-dimensional quadratic transport energy with mobility `2`.

For the empirical model, the vertical marginal empirical processes suggest
\[
m_n(s)
\approx
B_X(s)-B_Y(s),
\]
where `B_X,B_Y` are independent Brownian bridges after the usual `sqrt(n)` scaling. If the tangent Gamma-limit can be justified for the discrete assignment problem, then the leading excess-cost prediction is
\[
 n\left[
 \frac1n\sum_i\|X_i-Y_{\sigma_n(i)}\|
 -\left(\bar B_n-\bar A_n\right)
 \right]
\Longrightarrow
\frac14\int_0^1(B_X-B_Y)^2\,ds.
\tag{6.2}
\]
Since `B_X-B_Y` has the law of `sqrt(2)B` for a standard Brownian bridge `B`, the predicted law is
\[
\frac12\int_0^1B(s)^2\,ds
=
\frac12\sum_{r\ge1}\frac{Z_r^2}{\pi^2r^2},
\tag{6.3}
\]
with mean
\[
\frac12\sum_{r\ge1}\frac1{\pi^2r^2}=\frac1{12}.
\tag{6.4}
\]

**Important:** (6.2)-(6.4) are a prediction of the tangent theory, not a proved statement about P0336 in this artifact. Proving the discrete liminf/recovery sequence would be a separate theorem. These formulas are recorded because they give a sharp quantitative target for the next scale and a potential falsification test.

---

## 7. What this rules out

This run rules out a stronger family of potential selectors than the preceding run.

1. **Not only the vertical marginal:** adding the complete horizontal-mark fluctuation constraints at first order does not select a horizontal kernel.
2. **Not product self-averaging at Gaussian/tangent order:** product `k=1` is one member of an entire pathwise equality family.
3. **Not a fixed `s`-independent degeneracy only:** `k(a,b,s)` may vary with `s`; the minimum remains the same because the bistochastic identity (2.1) holds level by level.
4. **Not an expectation-level accident:** the degeneracy occurs before taking expectation over empirical fluctuations.

The previous run's tentative blocker "marked cross-fiber compatibility with the full two-dimensional empirical fluctuations" is therefore refined. At first tangent order, marked compatibility is *not* the selector.

---

## 8. Exact remaining gap

The source-level limit is still unidentified. The theorem above leaves three genuinely different places where selection can hide:

1. **Discrete/permutation scale:** the empirical plan is a permutation matrix, while the tangent construction uses a continuum edge-density correction. Integrality and local matching geometry may select a horizontal kernel below the smooth tangent scale.
2. **Higher asymptotic order:** after the order-`epsilon^2` tangent energy ties all kernels, the first nonvanishing next-order functional may depend on the horizontal kernel.
3. **Boundary of the bistochastic polytope:** Theorem 5.1 gives robust realizability for `k>=kappa`; singular kernels such as deterministic horizontal maps require a separate tangent-cone analysis.

The simplest mathematically sharp next question is:

> In a finite horizontal-bin approximation, what is the first asymptotic order at which two distinct bistochastic horizontal kernels have different optimal costs after the common order-`epsilon^2` term is removed?

That is now a cleaner target than trying to infer the full source limit directly from the Brownian vertical bridge.

---

## 9. Relation to current source status

The current source version, arXiv:2505.19104v2 (13 July 2026), still poses Problem 4: identify the limit of the empirical Euclidean OT plan for independent uniform samples on `[0,1]^2` and `[2,3]x[0,1]`.

A bounded 2026-09-19 follow-up search of the exact source title/problem geometry and recent source-author work did not recover a later theorem resolving this unregularized selection problem. Search failure is negative evidence only.

Nothing in this artifact identifies the literal limiting plan. The correct source status remains **OPEN / PARTIAL**, and `SEL_ID` remains `0`.

---

## 10. Next nonrepeating methods

The next ordinary P0336 run should not repeat B6/B18/B27. The most useful next triple is:

- **B8 — discretize:** replace the horizontal coordinates by two or three mark bins while retaining continuous vertical positions, and derive the exact tangent cone around both interior and singular bistochastic kernels.
- **B16 — compute every small case:** solve exact small finite-bin assignment instances symbolically/rationally where possible and identify the first order at which the horizontal coupling affects optimal cost.
- **B24 — find the extremal object:** once the first kernel-dependent correction is isolated, determine which bistochastic kernels extremize it; product, monotone/translation, and anti-monotone kernels are the first candidates.

These attacks target the now-isolated sub-tangent/discrete selector rather than redoing the already-degenerate Gaussian cell problem.
