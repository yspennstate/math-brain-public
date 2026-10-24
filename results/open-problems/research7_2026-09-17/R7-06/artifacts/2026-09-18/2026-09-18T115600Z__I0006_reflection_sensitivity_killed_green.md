Model actually running: **GPT-5.6 Sol. Reasoning level: UNVERIFIED** — this is **not GPT-6 at maximum**; no authenticated runtime model/effort telemetry or binding model/effort selector is exposed.

# I0006: exact reflection-sensitivity identity and killed-Green critical energy

Status: **proved deterministic finite-horizon theorem / PARTIAL relative to canonical I0006**.  
Owner: `R7-06`, native ID `6aabe827777c8191a43330b4a87d481d`.  
Target: `I0006`, Bou-Rabee–Panagiotis high-dimensional unbounded-below odometer rate.  
Admission: `research7_2026-09-17/R7-06/admissions/2026-09-18T100120Z__I0006.md`.  
Previous critical endpoint theorem: `research7_2026-09-17/R7-06/artifacts/2026-09-18/2026-09-18T100358Z__I0006_critical_gamma_d_over_2_log_exponent.md`.  
Previous sharp standalone Green-tail theorem: `research7_2026-09-17/R7-06/artifacts/2026-09-18/2026-09-18T105100Z__I0006_critical_green_two_sided_tail.md`.

No source-level closure or publication-novelty claim is made here.

## 1. Why this object is the next one to study

The preceding run proved that at the untreated endpoint

\[
\gamma=\frac d2,\qquad d\ge5,
\]

the finite Green average really has the critical lower-tail cost

\[
\exp\!\left[-\Theta\!\left(
\frac{h^{d/2}}{(\log h)^{d/2-1}}
\right)\right].
\]

Therefore the logarithm in the current odometer upper bound cannot be removed by a stronger estimate on the **unreflected** scenery Green average alone. The only possible gain must come from the reflection/obstacle mechanism itself.

This note identifies the exact pathwise object that measures that gain. It is a Green kernel killed on the dynamic contact set of the reflected recursion. At the critical conjugate exponent its `q`-energy is bounded by the logarithm of its **effective lifetime**, not the logarithm of the full time horizon.

That reduction is deterministic and exact.

## 2. Reflected recursion and Bellman reformulation — method B1

Let `P` be the simple-random-walk averaging operator on `Z^d`. For a deterministic scenery `z:Z^d->R`, define the finite-horizon reflected recursion

\[
u_0^z\equiv0,\qquad
u_{n+1}^z=(z+P u_n^z)_+.
\tag{2.1}
\]

Write

\[
F_n^z=z+P u_n^z,
\tag{2.2}
\]

so that `u_{n+1}^z=(F_n^z)_+`.

This is the deterministic recursion underlying the source's finite-time odometer representation.

### Proposition 2.1 (finite-horizon optimal stopping)

Let `(X_j)` be simple random walk started at `x`. Then

\[
\boxed{
 u_n^z(x)
 =
 \sup_{\tau\le n}
 \mathbb E_x\!\left[\sum_{j=0}^{\tau-1}z(X_j)\right],
}
\tag{2.3}
\]

where the supremum is over stopping times with values in `{0,1,...,n}` and the empty sum at `tau=0` is zero.

#### Proof

For horizon zero the value is zero. If `V_n` denotes the right-hand side, the first decision is either to stop immediately, earning zero, or to take the present reward `z(x)`, move one random-walk step, and thereafter use an optimal rule for the remaining `n` steps. Thus

\[
V_{n+1}(x)=\max\{0,z(x)+PV_n(x)\}.
\]

This is exactly (2.1), with the same initial condition. Induction gives `V_n=u_n^z`. ∎

This changes the category of the problem: the nonlinear reflection is a finite-horizon parabolic obstacle / Snell-envelope problem.

## 3. Exact finite-amplitude reflection-loss conservation — method B12

Fix a nonnegative penalty `eta:Z^d->[0,infinity)` and set

\[
z^-=z-\eta.
\]

Monotonicity of the positive part and of `P` gives

\[
u_n^{z^-}\le u_n^z.
\]

Define

\[
\Delta_n=u_n^z-u_n^{z^-}\ge0,
\qquad
b_n=F_n^z-F_n^{z^-}=\eta+P\Delta_n\ge0.
\tag{3.1}
\]

The elementary identity

\[
a_+-(a-b)_+=\min\{b,a_+\},\qquad b\ge0,
\tag{3.2}
\]

gives an exact recursion.

### Proposition 3.1 (reflection-loss identity)

Pointwise,

\[
\boxed{
\Delta_{n+1}=\min\{b_n,u_{n+1}^z\}.
}
\tag{3.3}
\]

Define the nonnegative clipping/contact loss

\[
c_{n+1}=b_n-\Delta_{n+1}
=(b_n-u_{n+1}^z)_+.
\tag{3.4}
\]

Then

\[
\boxed{
\Delta_{n+1}=\eta+P\Delta_n-c_{n+1}.
}
\tag{3.5}
\]

Writing

\[
G_n=\sum_{j=0}^{n-1}P^j,
\]

one obtains for every `n>=1`

\[
\boxed{
\Delta_n
=G_n\eta-
\sum_{j=1}^{n}P^{n-j}c_j,
}
\tag{3.6}
\]

and hence

\[
\boxed{
 b_n
=G_{n+1}\eta-
\sum_{j=1}^{n}P^{n+1-j}c_j.
}
\tag{3.7}
\]

In particular,

\[
0\le b_n\le G_{n+1}\eta.
\tag{3.8}
\]

#### Proof

Equation (3.3) is (3.2) with `a=F_n^z` and `b=b_n`, because `F_n^{z^-}=F_n^z-b_n`. Equations (3.4)–(3.5) are immediate. Iterating (3.5) from `Delta_0=0` gives (3.6); applying `eta+P(·)` gives (3.7). ∎

Equation (3.7) is the conserved quantity sought in B12: **raw Green response = actual reflected response + propagated contact losses**. Reflection can only remove sensitivity, and it removes it exactly at contact with the obstacle.

## 4. One-sided derivative and the dynamically killed Green kernel

For the next result assume `eta` is bounded and nonnegative. Put

\[
z_s=z-s\eta,\qquad 0\le s\le1.
\]

For fixed finite horizon `n`, only finitely many scenery coordinates can influence `u_n(x)`, so `s\mapsto u_n^{z_s}(x)` is a Lipschitz piecewise-linear function.

Let

\[
A_j^z(x)=\mathbf 1_{\{F_j^z(x)>0\}}.
\tag{4.1}
\]

### Proposition 4.1 (directional derivative recursion)

The downward directional derivative

\[
d_n^{z,\eta}(x)
=
\lim_{\varepsilon\downarrow0}
\frac{u_n^z(x)-u_n^{z-\varepsilon\eta}(x)}{\varepsilon}
\tag{4.2}
\]

exists and satisfies

\[
d_0^{z,\eta}=0,
\qquad
\boxed{
 d_{n+1}^{z,\eta}(x)
 =A_n^z(x)\bigl(\eta(x)+P d_n^{z,\eta}(x)\bigr).
}
\tag{4.3}
\]

#### Proof

Assume the derivative exists through horizon `n`. If `F_n^z(x)>0`, then for all sufficiently small positive `epsilon` the perturbed pre-field remains positive, so differentiation passes through the positive part and gives `eta+Pd_n`. If `F_n^z(x)<0`, both positive parts are zero for small `epsilon`, giving derivative zero. If `F_n^z(x)=0`, lowering the scenery can only lower the pre-field, so the perturbed positive part is also zero and the downward derivative is again zero. This proves (4.3) inductively. ∎

Iterating (4.3) gives a positive kernel.

### Definition 4.2 (dynamic killed Green kernel)

For `n>=1`, set

\[
K_{n,z}(x,y)
=
\mathbb E_x\!\left[
\sum_{j=0}^{n-1}
\mathbf 1_{\{X_j=y\}}
\prod_{i=0}^{j}
A_{n-1-i}^z(X_i)
\right].
\tag{4.4}
\]

Then

\[
\boxed{
 d_n^{z,\eta}(x)=\sum_yK_{n,z}(x,y)\eta(y).
}
\tag{4.5}
\]

The product in (4.4) means that the random walk is killed when it first encounters the dynamic contact set in the backward Bellman time coordinate.

Since every factor is at most one,

\[
\boxed{
0\le K_{n,z}(x,y)\le g_n(x,y)
:=\sum_{j=0}^{n-1}P^j(x,y).
}
\tag{4.6}
\]

For the pre-reflection field define

\[
\widetilde K_{n,z}(x,y)
=\mathbf 1_{\{x=y\}}+
\sum_wP(x,w)K_{n,z}(w,y).
\tag{4.7}
\]

Then

\[
-\frac{d}{ds}F_n^{z_s}(x)
=
\sum_y\widetilde K_{n,z_s}(x,y)\eta(y)
\tag{4.8}
\]

for almost every `s`, and

\[
0\le\widetilde K_{n,z}(x,y)
\le g_{n+1}(x,y).
\tag{4.9}
\]

Consequently, the **finite-amplitude** field reduction has the exact integral representation

\[
\boxed{
F_n^z(x)-F_n^{z-\eta}(x)
=
\int_0^1
\sum_y\widetilde K_{n,z-s\eta}(x,y)\eta(y)\,ds.
}
\tag{4.10}
\]

Thus no linearization error is hidden in the final sensitivity formula: the active-set kernel simply changes along the deformation.

## 5. Critical q-energy is controlled by effective lifetime, not full horizon

Now specialize to the source regime `d>=5` and set

\[
\gamma=\frac d2,
\qquad
q=\frac{\gamma}{\gamma-1}=\frac d{d-2}.
\tag{5.1}
\]

The infinite-lattice Green function obeys

\[
G(x,y)\le C_d(1+|x-y|)^{2-d}.
\tag{5.2}
\]

The key critical identity is

\[
(d-2)(q-1)=2,
\qquad q(d-2)=d.
\tag{5.3}
\]

### Lemma 5.1 (energy compression by lifetime)

Let `k:Z^d->[0,infinity)` satisfy

\[
0\le k(y)\le G(0,y)
\]

and let

\[
L=\sum_y k(y)<\infty.
\]

Then

\[
\boxed{
\sum_y k(y)^q
\le C_d\bigl(1+\log(1+L)\bigr).
}
\tag{5.4}
\]

#### Proof

Take

\[
R=\max\{2,\sqrt{1+L}\}.
\]

For the inner region, using (5.2) and `q(d-2)=d`,

\[
\sum_{|y|\le R}k(y)^q
\le
C_d+C_d\sum_{1\le r\le R}r^{d-1-d}
\le C_d(1+\log R).
\tag{5.5}
\]

For `|y|>R`, because `(d-2)(q-1)=2`,

\[
k(y)^q
=k(y)k(y)^{q-1}
\le k(y)G(0,y)^{q-1}
\le C_dR^{-2}k(y).
\]

Hence

\[
\sum_{|y|>R}k(y)^q
\le C_dR^{-2}L\le C_d.
\tag{5.6}
\]

Since `log R <= C(1+log(1+L))`, (5.4) follows. ∎

Apply this to the dynamic kernel. Define the effective susceptibility/lifetime

\[
L_{n,z}(x)=\sum_y\widetilde K_{n,z}(x,y).
\tag{5.7}
\]

Because `widetilde K <= g_{n+1} <= G`, Lemma 5.1 gives

\[
\boxed{
Q_{n,z}(x):=
\sum_y\widetilde K_{n,z}(x,y)^q
\le
C_d\bigl(1+\log(1+L_{n,z}(x))\bigr).
}
\tag{5.8}
\]

The trivial lifetime bound is `L_{n,z}(x)<=n+1`, which recovers the old `O(log n)` critical energy. The point is that reflection replaces `n` by the **actual surviving Bellman lifetime**. If contact kills sensitivity much earlier, the logarithm shrinks automatically.

Two exact extremes confirm that this parameter is real rather than notation:

- if the scenery is uniformly very negative so every Bellman state is in contact, then `K=0`, `widetilde K=delta_x`, `L=1`, and `Q=1`;
- if the scenery is strictly positive everywhere, every state is active, `K=g_n`, `widetilde K=g_{n+1}`, `L=n+1`, and the critical `q`-energy grows on the familiar logarithmic scale.

The obstacle geometry can therefore interpolate between `O(1)` and the raw `Theta(log n)` critical energy.

## 6. Exact Weibull deformation cost through the killed kernel

The energy bound feeds directly into the critical stretched-exponential variational problem.

For any nonnegative kernel `k` with

\[
Q=\sum_y k(y)^q>0,
\]
Holder's inequality gives

\[
\sum_yk(y)\eta(y)
\le Q^{1/q}
\left(\sum_y\eta(y)^\gamma\right)^{1/\gamma}.
\tag{6.1}
\]

Thus the exact minimum cost of producing a linear deficit `h` is

\[
\boxed{
\inf_{\eta\ge0:\,\sum k\eta\ge h}
\sum_y\eta(y)^\gamma
=
\frac{h^\gamma}{Q^{\gamma-1}}.
}
\tag{6.2}
\]

Equality is attained by

\[
\eta(y)=\frac{h}{Q}k(y)^{q-1}.
\tag{6.3}
\]

Equation (4.10) upgrades this to finite amplitude.

### Theorem 6.1 (finite-amplitude reflected deformation lower bound)

Suppose a nonnegative perturbation `eta` lowers the pre-reflection field at `(n,x)` by at least `h>0`:

\[
F_n^z(x)-F_n^{z-\eta}(x)\ge h.
\tag{6.4}
\]

Let

\[
Q_*=
\sup_{0\le s\le1}
\sum_y\widetilde K_{n,z-s\eta}(x,y)^q,
\tag{6.5}
\]

and

\[
L_*=
\sup_{0\le s\le1}
L_{n,z-s\eta}(x).
\tag{6.6}
\]

Then

\[
\boxed{
\sum_y\eta(y)^\gamma
\ge
\frac{h^\gamma}{Q_*^{\gamma-1}}
\ge
c_d\,
\frac{h^\gamma}
{\bigl(1+\log(1+L_*)\bigr)^{\gamma-1}}.
}
\tag{6.7}
\]

#### Proof

By (4.10) and Holder,

\[
h
\le
\int_0^1
\sum_y\widetilde K_{n,z-s\eta}(x,y)\eta(y)\,ds
\le
Q_*^{1/q}
\left(\sum_y\eta(y)^\gamma\right)^{1/\gamma}.
\]

Raise to power `gamma` and use `gamma/q=gamma-1`. The second inequality follows from (5.8), uniformly in `s`. ∎

This theorem is the main output of the run. The denominator controlling critical negative-fluctuation cost is no longer forced to be `log n`; it is the logarithm of an **effective obstacle-limited susceptibility**.

It does **not** yet prove a sharper stochastic odometer tail, because one still must control `L_*` on the random environments and deformations relevant to the source lower-tail event.

## 7. Deliberately breaking radial symmetry — method B15

The preceding run identified the raw critical Green optimizer

\[
\eta(y)\propto g_n(0,y)^{q-1}.
\]

Could one simply break radial symmetry — for instance, put the deficit only in one angular sector — and obtain a cheaper way around the logarithmic cost?

No.

Let `A` be any subset and let

\[
Q_A=\sum_{y\in A}g_n(0,y)^q,
\qquad
Q=\sum_yg_n(0,y)^q.
\]

Restricting the perturbation to `A` changes the exact variational cost from

\[
\frac{h^\gamma}{Q^{\gamma-1}}
\]

to

\[
\boxed{
\frac{h^\gamma}{Q_A^{\gamma-1}}.
}
\tag{7.1}
\]

If `Q_A=rho Q`, the cost is multiplied by

\[
\boxed{\rho^{-(\gamma-1)}\ge1.}
\tag{7.2}
\]

Thus arbitrary angular asymmetry cannot improve on the raw Green optimizer. A fixed sector containing a fixed fraction of the critical `q`-energy only changes the constant; a thinner sector is strictly more expensive.

What **can** help is asymmetry aligned with the random contact geometry, because the correct kernel after reflection is not `g_n` but `widetilde K_{n,z}`. Its optimizer is

\[
\eta(y)\propto\widetilde K_{n,z}(x,y)^{q-1}.
\]

So B15 rules out the naive “choose a clever sector” route and isolates the only useful symmetry breaking: follow the surviving obstacle/optimal-stopping paths.

## 8. New exact blocking quantity

The previous logarithmic correction came from

\[
\sum_y g_n(0,y)^q\asymp\log n.
\]

The reflected problem replaces this by

\[
\boxed{
Q_{n,z}(x)=\sum_y\widetilde K_{n,z}(x,y)^q.
}
\tag{8.1}
\]

and, more coarsely, by

\[
\boxed{
L_{n,z}(x)=\sum_y\widetilde K_{n,z}(x,y).
}
\tag{8.2}
\]

The deterministic hierarchy is now explicit:

- if `L_eff=Theta(n)`, the old `O(log n)` critical energy remains possible;
- if `L_eff` is polynomial in `n`, the logarithm is still of order `log n` and this argument alone does not remove the log-log correction;
- if `L_eff` is polylogarithmic, then `Q_eff=O(log log n)`;
- if `L_eff=O(1)`, then `Q_eff=O(1)` and the critical deformation cost becomes pure `Theta(h^gamma)` at this deterministic level.

Therefore the slowly varying source question has been reduced to a concrete obstacle-susceptibility question:

> **How large can the dynamic killed-Green `q`-energy remain along the negative deformations that realize the critical odometer lower tail?**

That is strictly sharper than asking for a better standalone Green-function estimate, which the preceding run proved impossible in general.

## 9. What is proved and what remains open

### Proved here

1. the reflected recursion is exactly a finite-horizon optimal-stopping problem;
2. finite scenery lowering satisfies the exact Green-response-minus-contact-loss identity (3.7);
3. its one-sided sensitivity is a random-walk Green kernel killed on the dynamic contact set;
4. finite-amplitude sensitivity is the integral of these killed kernels along the deformation;
5. at `gamma=d/2`, the killed-kernel `q`-energy is at most `C[1+log(1+L_eff)]`;
6. any finite deformation lowering the pre-field by `h` pays at least the critical Weibull cost (6.7);
7. arbitrary spatial-sector symmetry breaking cannot beat the raw Green optimizer.

### Still open

1. obtain a useful probabilistic bound on `L_*` or `Q_*` under the source's random critical environment;
2. determine whether the source odometer actually carries the current `(log log t)^((d-2)/d)` upper correction or whether reflection removes it;
3. extend from the regular two-sided critical Weibull milestone to the full canonical I0006 tail-dependent classification;
4. complete independent audits and source-level packaging only if the full source is eventually resolved.

The frozen milestone metric remains `M_crit(d)=0`; this theorem is real structural progress but does not change that already-zero logarithmic-exponent width.
