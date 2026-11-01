Model actually running: **GPT-5.6 Sol. Reasoning level: UNVERIFIED** — this is **not GPT-6 at maximum**; no authenticated runtime model/effort telemetry or binding selector is exposed.

# I0006: uniform Bellman concentration and annealed removal of the continuation cap

Status: **proved restricted theorem / PARTIAL relative to canonical I0006**.  
Owner: `R7-06`, native ID `6aabe827777c8191a43330b4a87d481d`.  
Canonical target: `I0006`.  
Run-start master snapshot: `da2867d4a2146ea733a79613f37dd491d54f82cf`.  
Pre-artifact fresh master snapshot: `353570ff4401ace24aafcb790128ef811adfed5b`.  
Previous report: `research7_2026-09-17/R7-06/runs/2026-09-18/2026-09-18T154000Z__report.md` @ `2269749fb58b9466add4f44013db8fd5e3797132`.

This note executes the precommitted post-STUCK1 triple **B4 / B20 / B27** in the source-valid recovery law

\[
\nu(dx)=Z^{-1}e^{-|x|^{5/2}}\,dx
\tag{1.1}
\]

on `Z^5`.  The preceding run proved that a critical inverse-square negative core kills every Bellman continuation capped at height `B`, and reduced the uncapped case to the boundary excess

\[
\mathbb E_0[(H_{T_R}(X_{T_R})-B)_+;T_R\le n].
\tag{1.2}
\]

The new result is that, for the actual Bellman continuation, this excess is uniformly tiny once the cap exceeds the mean by a growing amount.  Thus the *uncapped-continuation gap itself* is closed in an annealed sense for the smooth critical Weibull law.  A different bridge is still missing before this can decide the source asymptotic.

## 2. Setup

For a deterministic scenery `z` and simple random walk `(X_j)` on `Z^5`, let

\[
u_n^z(x)
=
\sup_{\tau\le n}
\mathbb E_x\sum_{j=0}^{\tau-1}z(X_j),
\tag{2.1}
\]

where stopping immediately is allowed.  Equivalently,

\[
u_0^z\equiv0,
\qquad
u_{k+1}^z=(z+P\nu_k^z)_+.
\tag{2.2}
\]

When `z=\zeta` has law (1.1), write

\[
a_n=\mathbb E\,\nu_n^\zeta(0).
\tag{2.3}
\]

For the finite Green kernel put

\[
g_n(x,y)=\sum_{j=0}^{n-1}p_j(x,y),
\qquad
G_{2,5}:=\sum_{k=0}^\infty (k+1)p_k(0,0).
\tag{2.4}
\]

The local central limit bound `p_k(0,0)\le C(k+1)^{-5/2}` implies

\[
G_{2,5}<\infty.
\tag{2.5}
\]

The main mechanism below is specific to dimensions `d>4`: the entire finite-horizon Bellman functional has a horizon-independent Euclidean Lipschitz constant because the Green kernel is uniformly square summable.

## 3. B4 — prove something weaker completely: uniform concentration of the full Bellman value

### Lemma 3.1 (uniform `l^2` Green bound)

For every `n>=1`,

\[
\boxed{
\sum_{y\in\mathbb Z^5} g_n(0,y)^2\le G_{2,5}<\infty.
}
\tag{3.1}
\]

#### Proof

By symmetry and Chapman--Kolmogorov,

\[
\sum_y p_i(0,y)p_j(0,y)
=
\sum_y p_i(0,y)p_j(y,0)
=p_{i+j}(0,0).
\]

Hence

\[
\sum_y g_n(0,y)^2
=
\sum_{i,j=0}^{n-1}p_{i+j}(0,0).
\]

For fixed `k=i+j`, the number of pairs `(i,j)` is at most `k+1`, so

\[
\sum_y g_n(0,y)^2
\le
\sum_{k=0}^{\infty}(k+1)p_k(0,0)
=G_{2,5}.
\]

The series converges by (2.5). ∎

### Lemma 3.2 (Bellman value is uniformly Euclidean-Lipschitz)

Regard `\nu_n^z(0)` as a function of the finitely many scenery coordinates reachable in fewer than `n` steps.  Then

\[
\boxed{
|\nu_n^z(0)-\nu_n^{z'}(0)|
\le
\left(\sum_y g_n(0,y)^2\right)^{1/2}
\left(\sum_y|z(y)-z'(y)|^2\right)^{1/2}.
}
\tag{3.2}
\]

In particular its Euclidean Lipschitz constant is at most `G_{2,5}^{1/2}`, uniformly in `n`.

#### Proof

For a fixed stopping time `\tau<=n`, define its occupation coefficients

\[
\mu_\tau(y)=
\mathbb E_0\sum_{j<\tau}\mathbf1_{\{X_j=y\}}.
\tag{3.3}
\]

Every coefficient is nonnegative and

\[
0\le\mu_\tau(y)\le g_n(0,y).
\tag{3.4}
\]

The payoff for this fixed rule is the linear functional

\[
L_\tau(z)=\sum_y\mu_\tau(y)z(y).
\]

Therefore

\[
|L_\tau(z)-L_\tau(z')|
\le
\|\mu_\tau\|_2\,\|z-z'\|_2
\le
\|g_n(0,\cdot)\|_2\,\|z-z'\|_2.
\]

Taking the supremum over all stopping times on each side preserves the same Lipschitz constant, proving (3.2). ∎

### Lemma 3.3 (the one-site critical Weibull law has a finite log-Sobolev constant)

There exists `C_LS<\infty` such that the law (1.1) satisfies

\[
\operatorname{Ent}_\nu(f^2)
\le
2C_{LS}\int |f'|^2\,d\nu
\tag{3.5}
\]

for smooth `f`.

#### Proof

Let `V(x)=|x|^{5/2}`.  Outside `[-1,1]`,

\[
V''(x)=\frac{15}{4}|x|^{1/2}\ge\frac{15}{4}.
\]

On `[-1,1]`, replace `V` by the quadratic

\[
W_0(x)=\frac54x^2-\frac14.
\]

At `x=\pm1`, `W_0` and its first derivative match `V`; moreover `W_0''=5/2`.  Smoothing in arbitrarily small neighborhoods of `\pm1` gives a `C^2` potential `W` with

\[
W''\ge c_0>0
\]

and with `V-W` bounded and compactly supported.  The Bakry--Emery criterion gives a finite log-Sobolev constant for the probability measure proportional to `e^{-W(x)}dx`.  The Holley--Stroock bounded-perturbation lemma transfers the log-Sobolev inequality to `e^{-V(x)}dx`; normalization does not affect the conclusion. ∎

Only these two standard functional-inequality implications are imported here; all problem-specific estimates are proved in this note.

### Theorem 3.4 (dimension-free Bellman concentration in `d=5`)

There is a constant `c_*>0`, depending only on the one-site law and dimension, such that for every horizon `n`, every starting point `x`, and every `r>=0`,

\[
\boxed{
\mathbb P\left(\nu_n^\zeta(x)-\mathbb E\nu_n^\zeta(x)\ge r\right)
\le e^{-c_*r^2}.
}
\tag{3.6}
\]

Consequently, for `r>0`,

\[
\boxed{
\mathbb E\left(\nu_n^\zeta(x)-\mathbb E\nu_n^\zeta(x)-r\right)_+
\le
\Psi(r):=
\frac{e^{-c_*r^2}}{2c_*r}.
}
\tag{3.7}
\]

Both estimates are uniform in `n` and `x`.

#### Proof

For each finite horizon the relevant scenery is a finite product of copies of `\nu`.  By tensorization, (3.5) holds on that product with the same constant `C_LS`.  Lemma 3.2 gives Euclidean Lipschitz constant at most `G_{2,5}^{1/2}`.  The standard Herbst argument applied to the product log-Sobolev inequality therefore yields

\[
\mathbb P(F-\mathbb EF\ge r)
\le
\exp\left(-\frac{r^2}{2C_{LS}G_{2,5}}\right).
\]

Thus (3.6) holds with

\[
c_*=(2C_{LS}G_{2,5})^{-1}.
\]

Integrating the tail,

\[
\mathbb E(F-\mathbb EF-r)_+
=
\int_r^\infty\mathbb P(F-\mathbb EF\ge t)\,dt
\le
\int_r^\infty e^{-c_*t^2}dt
\le
\frac{e^{-c_*r^2}}{2c_*r}.
\]

Translation invariance gives the same constants for every `x`. ∎

### Corollary 3.5 (uniform excess above the largest smaller-horizon mean)

Since `a_k<=a_n` for `k<=n`, for every `k<=n`, `x`, and `r>0`,

\[
\boxed{
\mathbb E\bigl(\nu_k^\zeta(x)-a_n-r\bigr)_+
\le \Psi(r).
}
\tag{3.8}
\]

Indeed `a_n+r-a_k>=r`, so (3.8) follows directly from (3.7).

This is already stronger than the previous run needed: the continuation overshoot has a horizon-independent Gaussian tail around its own mean, even though the mean itself diverges.

## 4. B20 — find why the previous lower-increment algorithm fails

The preceding run suggested that once the inverse-square core is opaque, one should control (1.2) and then feed the core into a matching lower-increment argument.  The first half of that plan is now possible, but there is a structural sign issue in the second half.

The event

\[
\mathcal O=
\{\zeta(y)\le h_y\text{ for all }y\in B_R\}
\tag{4.1}
\]

with negative thresholds `h_y` is coordinatewise **decreasing**.  The Bellman value `\nu_n^\zeta(x)` is coordinatewise **increasing** in the scenery, because it is a supremum of linear functionals with nonnegative occupation coefficients.  Thus an opaque negative core suppresses the Bellman value; by itself it cannot be a direct favorable event proving a lower bound on `a_n`.

This is not merely a wording problem.  Harris association for a product measure gives, for every nonnegative increasing functional `F`,

\[
\boxed{
\mathbb E[F\mid\mathcal O]\le\mathbb EF.
}
\tag{4.2}
\]

To see this, `1_{\mathcal O^c}` is increasing, so

\[
\mathbb E[F1_{\mathcal O^c}]
\ge \mathbb EF\,\mathbb P(\mathcal O^c),
\]

which rearranges to (4.2).

Therefore the architecture now separates cleanly:

1. opacity can prove that an unfavorable core remains unfavorable even with an unbounded continuation;
2. but a further comparison identity is required to turn such suppression into information about the *growth* of `a_n`.

The existing susceptibility identity for a **uniform** downward mean shift does not yet provide this reverse bridge for a localized rare core.  Any future lower-growth argument must contain an additional ingredient of the following type: an influence/change-of-measure identity that converts the loss under a localized decreasing event into a positive contribution to a source quantity whose expectation is `a_n`, without reversing monotonicity.

That missing comparison, rather than the continuation overshoot, becomes the new logical bottleneck after Section 5 below.

## 5. B27 — swap the quantifiers: an annealed uncapped-opacity theorem

We now weaken the pathwise cap to exactly the average excess estimate needed after conditioning on a core.

Let `T_R` be the first exit from `B_R`.  At exit time `t`, take the **actual Bellman continuation**

\[
H_t(x)=\nu_{n-t}^\zeta(x),
\qquad 0\le t\le n.
\tag{5.1}
\]

The previous opacity theorem states that if the interior rewards satisfy

\[
\zeta(y)\le-\frac{A}{1+|y|^2},
\qquad |y|<R,
\tag{5.2}
\]

and

\[
A\log(1+R^2)\ge2C_5B,
\tag{5.3}
\]

then the crossing value with arbitrary nonnegative continuation is bounded by

\[
V_n(0)
\le
\mathbb E_0[(H_{T_R}(X_{T_R})-B)_+;T_R\le n].
\tag{5.4}
\]

### Theorem 5.1 (conditional annealed uncapped opacity)

Let `\mathcal O` be any decreasing event which implies (5.2), and suppose (5.3) holds.  For every `r>0`, choose

\[
B=a_n+r.
\tag{5.5}
\]

Then

\[
\boxed{
\mathbb E\bigl[V_n(0)\mid\mathcal O\bigr]
\le\Psi(r)
=
\frac{e^{-c_*r^2}}{2c_*r}.
}
\tag{5.6}
\]

Equivalently,

\[
\boxed{
\mathbb E[1_{\mathcal O}V_n(0)]
\le
\mathbb P(\mathcal O)\Psi(r).
}
\tag{5.7}
\]

#### Proof

Fix `t<=n` and `x`.  The functional

\[
F_{t,x}(\zeta)=
(\nu_{n-t}^\zeta(x)-B)_+
\]

is nonnegative and coordinatewise increasing.  By (4.2),

\[
\mathbb E[F_{t,x}\mid\mathcal O]
\le
\mathbb E F_{t,x}.
\tag{5.8}
\]

Since `B=a_n+r` and `a_{n-t}<=a_n`, Corollary 3.5 gives

\[
\mathbb E F_{t,x}\le\Psi(r).
\tag{5.9}
\]

Now condition on the random-walk exit pair `(T_R,X_{T_R})`.  Its law is independent of the scenery.  Averaging (5.8)--(5.9) over that exit law and using (5.4) yields

\[
\mathbb E[V_n(0)\mid\mathcal O]
\le
\Psi(r)\,\mathbb P_0(T_R\le n)
\le\Psi(r).
\]

Multiplying by `P(\mathcal O)` gives (5.7). ∎

### 5.2 Critical inverse-square core at the moving mean scale

Put, for large `b`,

\[
L_b=\log(e+b),
\qquad
R_b=\left\lfloor\rho\sqrt{b/L_b}\right\rfloor,
\qquad
A_b=K\frac b{L_b},
\tag{5.10}
\]

and define

\[
\mathcal O_b=
\left\{
\zeta(y)\le-\frac{A_b}{1+|y|^2}
\text{ for all }|y|<R_b
\right\}.
\tag{5.11}
\]

For fixed `rho`, choose `K` so that

\[
A_b\log(1+R_b^2)\ge2C_5b
\tag{5.12}
\]

for all sufficiently large `b`.  The previous critical-core computation gives constants `c,C>0` such that

\[
\boxed{
\mathbb P(\mathcal O_b)
\ge
\exp\{-C\Phi_5(b)\},
\qquad
\Phi_5(b)=\frac{b^{5/2}}{(\log(e+b))^{3/2}}.
}
\tag{5.13}
\]

Now set

\[
b=a_n+r.
\tag{5.14}
\]

Then (5.12) is precisely the opacity requirement for the cap in Theorem 5.1, and therefore

\[
\boxed{
\mathbb E[V_n(0)\mid\mathcal O_{a_n+r}]
\le
\frac{e^{-c_*r^2}}{2c_*r}.
}
\tag{5.15}
\]

In particular, if `r=\eta a_n` for any fixed `\eta>0`, then the source lower bound `a_n\to\infty` implies

\[
\mathbb E[V_n(0)\mid\mathcal O_{(1+\eta)a_n}]
\le
\exp\{-c_\eta a_n^2\}
\tag{5.16}
\]

up to a harmless polynomial prefactor.  Thus the unbounded continuation is asymptotically invisible on such a core in conditional expectation.

The key point is that this estimate already includes arbitrary excursions after the first exit; there is no remaining pathwise cap assumption.

## 6. What this proves, and what it does not

The previous run ended with the explicit obstruction

\[
\mathbb E_0[(H_{T_R}(X_{T_R})-B)_+;T_R\le n].
\]

For the smooth critical Weibull law, Theorem 5.1 controls exactly that quantity after conditioning on any decreasing opaque core.  In this restricted recovery case, **boundary-continuation overshoot is no longer the blocker**.

However, the source milestone is still not solved.  The new B20 diagnosis shows why: the core is a decreasing event and suppresses the Bellman value.  What is now missing is a source-faithful comparison principle that turns the amount of suppression created by localized inverse-square cores into a quantitative statement about the growth of the unconditioned mean `a_n` (or another source quantity already known to be equivalent to it).  No such reverse influence identity is proved here.

This distinction is important.  We have removed the technical cap from the obstacle theorem, but we have **not** proved that the current `(log log n)^{3/5}` correction is genuine, nor that it is absent.

## 7. Metric and method outcome

Frozen source metric:

`M_crit(5)` = width of the proved interval containing all subsequential values of `log a_t / log log t` under the admitted critical endpoint hypotheses.

Before this run: `M_crit(5)=0`.  
After this run: `M_crit(5)=0`.  
Movement: **NO MOVEMENT**.

Method outcomes:

- **B4:** proved the full finite-horizon Bellman functional has a horizon-independent `l^2` Lipschitz constant in `d=5`, and hence a horizon-independent Gaussian concentration inequality under the smooth critical Weibull product law.
- **B20:** identified the precise architectural failure of the previous intended lower-increment route: an opaque inverse-square core is decreasing and suppresses the Bellman value, so overshoot control alone cannot imply a lower bound for `a_n`.
- **B27:** replaced the quenched pathwise cap by a conditional annealed excess estimate and proved that the actual unbounded Bellman continuation contributes at most `Psi(r)` when the opacity cap is `a_n+r`.

This is the second ordinary post-STUCK1 no-movement run.  If the next ordinary run also leaves `M_crit(5)` unchanged, the following run must be the second Section-I thinking-only diagnosis for this HARD target.

## 8. Next mathematical attack

Do **not** return to the continuation overshoot; in the smooth recovery law it is now controlled.

The next nonrepeating triple is:

1. **B5 — add a parameter and differentiate:** introduce the amplitude `lambda` of a localized inverse-square penalty and differentiate `E u_n` in `lambda`; seek an exact local-core influence formula analogous to the uniform-shift susceptibility identity.
2. **B18 — say it in another language:** rewrite that derivative as a capacity/occupation functional of the optimal stopped path and identify whether the critical `log R` survives after averaging over the active set.
3. **B25 — count the same thing twice:** express the integrated local susceptibility both as a scenery interpolation loss and as expected occupation of the core, aiming for a noncircular bridge between local suppression and the unconditioned mean.

A successful next step would be an identity or one-sided inequality of the schematic form

\[
\mathbb E u_n(0)-\mathbb E u_n^{(\lambda w_R)}(0)
=
\int_0^\lambda
\mathbb E\,\mathcal L_{n,R}(s)\,ds,
\tag{8.1}
\]

with a lower bound on the integrated local occupation `\mathcal L_{n,R}` strong enough to interact with the critical inverse-square profile.  Without such a bridge, the opacity machinery remains a sharp but one-sided obstacle theorem rather than a determination of the source asymptotic.
