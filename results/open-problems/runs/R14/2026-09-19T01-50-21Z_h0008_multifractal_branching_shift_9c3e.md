Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. PARTIAL METRIC MOVEMENT on newly admitted H0008: `I_mf: 0 -> >= phi'(1+eta)-phi'(1-eta) > 0` on the explicitly stated nondegenerate finite-type source slice, for some certified `eta>0`; full H0008 remains OPEN/PARTIAL. Methods actually used: #1 CHANGE THE CATEGORY, #5 ADD A PARAMETER AND DIFFERENTIATE, #25 COUNT THE SAME THING TWICE.**

# R14 HARD OUTSIDE — H0008 boundary multifractal spectrum

## 0. Continuity, mandatory handoffs, and successor admission

The previous R14 target D0034 / Bradley Question 6 exhausted both permitted HARD stuck-recovery cycles and was terminally handed off in

`runs/R14/2026-09-19T00-53-53Z_d0034_terminal_handoff_successor_gate_a4c7.md`.

I do **not** reopen D0034, D0039, D0036, H0017, or the original negative-margin spherical-perceptron track. H0021 is still a released HARD source with a canonical handoff file naming `UNASSIGNED AFTER R16 HANDOFF`; under the create-only ownership rule I did not overwrite that canonical transfer gate or create a shadow H0021 claim.

I therefore continued the outside-source admission scan. H0008 passed the source/current-literature/ownership gate and was claimed create-only for R14 at

`operations/claims/H0008.md`

creation commit

`86b31650d55fa126f2a0cfe1fa780d8f6142b1c6`.

The claim was read back at that exact commit before research. No competing H0008 claim or prior H0008 mathematical run was recovered before creation.

The exact outside source is Achyut Kumar, *Threshold cascades of interacting diffusions on unimodular random trees: a conditional branching-process universality theorem, the annealed pressure, and the dimension of the failed boundary*, arXiv:2608.15987v1 (17 Aug 2026), Section 12.3, open problem (6), **Boundary fluctuations**. The verified intake quotation asks for

> the multifractal spectrum of transmission-weighted flows (the Legendre transform associated with the pressure of Definition 5.2), and the harmonic measure of the cluster itself.

The first clause is the target of this run. The harmonic-measure clause is **not** claimed solved here.

## 1. Required whole-repository/current-neighbor read

Before successor research I recovered the current campaign `INDEX.md` and `RANKING.md`, root `POSTED.md`, `RESULTS.md`, `QUEUE.md`, the new-methods owner directive and deployment policy, the newest R14 report, the verified H intake, and current neighboring source histories. In particular:

- H0003 is separately owned by NM13-11; its recent work is on front-decoupling/echo control and does not own H0008.
- H0006 was separately owned by R12 and terminally handed off after reaching `FSS_layers=2/3`; it does not own H0008.
- H0011 has a separate canonical owner and concerns the continuous-type CRT limit.
- H0008 had no canonical claim and no prior mathematical report in the bounded repository search before the create-only claim above.

The H intake itself was source-checked on 14 Sep 2026 and records H0008 verbatim as an open problem. No stale `PENDING` row was treated as automatic dispatch authority; the claim was created only after the exact source and ownership checks above.

## 2. Dated primary/later literature check — 19 Sep 2026

The current arXiv record for 2608.15987 remains the August 2026 paper. Its abstract states the finite-type Galton-Watson reduction, the real-analytic pressure

\[
\phi(\beta)=\log \rho(M(\beta)),
\]

and the already-proved failed-boundary dimension

\[
\dim_H \partial S=\log \rho(M)=\phi(1).
\]

The later Kumar--Duddala companion arXiv:2608.21125 (21 Aug 2026) addresses front propagation/Bramson delay and the continuous-type/CRT programme; it does not advertise a theorem closing H0008's transmission-weighted boundary multifractal spectrum or harmonic-measure clause.

The relevant classical machinery is **not new**:

1. J. D. Biggins and A. E. Kyprianou, *Measure change in multitype branching*, Adv. Appl. Probab. 36 (2004), 544--581, develops the multitype change-of-measure/spine martingale theory used below.
2. J. D. Biggins and A. Rahimzadeh Sani, *Convergence results on multitype, multivariate branching random walks*, Adv. Appl. Probab. 37 (2005), 681--705, proves uniform transform convergence and particle-count limit theorems using smooth Perron--Frobenius matrices and saddlepoint large deviations.
3. Julien Barral, *Generalized vector multiplicative cascades*, Adv. Appl. Probab. 33 (2001), 874--895, gives simultaneous convergence of branching-random-walk cascades and evaluates dimensions of the associated boundary measures.

Thus I make **no novelty claim** for multitype BRW multifractal technology itself. The useful contribution here is the exact identification of the source object with the correctly normalized BRW pressure, including a necessary `beta=1` shift that is easy to miss.

A bounded current search found no later paper explicitly claiming to resolve Kumar's H0008 source problem. That is negative bounded evidence only, not a worldwide novelty certificate.

## 3. Fixed metric and a normalization correction

The create-only H0008 claim freezes

`I_mf` = length of a nonzero closed interval of local transmission-weight exponents on which a complete pressure-spectrum equality has been proved.

The *length metric itself* is unchanged. However, the formula written in the admission file used the unshifted expression

\[
\inf_\beta\{\phi(\beta)+\beta a\}.
\]

That formula is not correctly anchored for level sets **inside the already-failed tree** if the source convention satisfies `M(1)=M`, as the source abstract does. The correction is mathematical, not a policy reset: the failed-tree BRW pressure is

\[
\boxed{\psi(q)=\phi(1+q)},
\]

so its level-set Legendre expression is

\[
\boxed{
D(a)=\inf_{q}\{\psi(q)+qa\}
=\inf_{\beta}\{\phi(\beta)+(\beta-1)a\}.
}
\tag{3.1}
\]

If the source's notation `\phi^*` already incorporates this `beta=1` anchoring, then (3.1) is simply that convention written explicitly. If `\phi^*` is defined as the ordinary unshifted Legendre transform of `phi`, an affine normalization correction is required before interpreting it as a spectrum on `\partial S`.

Because claim files are create-only ownership records, I do not rewrite the claim file. This immutable report records the correction and all subsequent use of `I_mf` refers to the same interval-length metric with the source-correct anchor (3.1).

## 4. Method #1 — change category: the failed boundary is a finite-type branching random walk

Work under the source's finite-type front-decoupled Galton--Watson reduction. Let `D` be the finite type set. Write

\[
B_{ij}=m_*q(j)
\]

for the potential child intensity before transmission and let `p_{ij}\in(0,1]` be the source transmission probability along a type `i->j` edge. Then the actual failed-child mean matrix is

\[
M(1)_{ij}=B_{ij}p_{ij},
\]

and the source tilt has the form

\[
M(\beta)_{ij}=B_{ij}p_{ij}^{\beta}.
\tag{4.1}
\]

For a failed edge `i->j`, put

\[
x_{ij}:=-\log p_{ij}\ge0.
\]

For a failed descendant `u` at generation `n`, let

\[
S(u)=\sum_{e\in[o,u]}x_e,
\qquad
W(u)=e^{-S(u)}=\prod_{e\in[o,u]}p_e.
\]

The *actual failed genealogy* is therefore a finite-type branching random walk with mean Laplace matrix

\[
\widehat M(q)_{ij}
:=M(1)_{ij}e^{-q x_{ij}}
=B_{ij}p_{ij}^{1+q}
=M(1+q)_{ij}.
\tag{4.2}
\]

Consequently its log-Laplace/Perron pressure is exactly

\[
\boxed{\psi(q)=\log\rho(\widehat M(q))=\phi(1+q).}
\tag{4.3}
\]

This is the category change that makes the first H0008 clause a standard multitype BRW/multiplicative-cascade problem rather than an infinite-dimensional boundary-operator problem.

## 5. Method #25 — count the same boundary twice: the `beta=1` shift is forced

There is a one-line exact sanity test that any proposed spectrum must survive.

Take the one-type constant-transmission case. Let the potential branching factor be `m_*` and every transmission probability be the same `p\in(0,1)`. Write

\[
A=\log m_*,\qquad L=\log p<0.
\]

Then

\[
\phi(\beta)=A+\beta L,
\qquad
a=-\phi'(\beta)=-L.
\]

The already-proved failed-boundary dimension is

\[
\phi(1)=A+L=\log(m_*p).
\]

The shifted spectrum gives

\[
\phi(\beta)+(\beta-1)a=A+L=\phi(1),
\]

exactly the dimension of the failed boundary. The unshifted expression gives

\[
\phi(\beta)+\beta a=A=\log m_*,
\]

which is the ambient potential-tree growth and is wrong for `\partial S` whenever `p\ne1`.

This exact calculation was checked symbolically with no floating point. Artifact:

`artifacts/R14/2026-09-19T01-50-21Z_h0008_pressure_shift_checker.py`

with archived output

`artifacts/R14/2026-09-19T01-50-21Z_h0008_pressure_shift_checker.out`

ending `ALL_EXACT_CHECKS_PASS`.

This is a certified obstruction to any proof route that applies the source tilt around `beta=0` without first changing measure to the actual failed genealogy.

## 6. Method #5 — add the tilt parameter and differentiate

Let

\[
\lambda(q):=\rho(\widehat M(q)),
\qquad
\psi(q)=\log\lambda(q)=\phi(1+q).
\]

For `q` in a real neighborhood of `0`, let `r(q),\ell(q)>0` be right/left Perron vectors normalized by

\[
\ell(q)^Tr(q)=1.
\]

Define the Markov kernel

\[
Q_q(i,j)
=
\frac{\widehat M(q)_{ij}r_j(q)}{\lambda(q)r_i(q)}.
\tag{6.1}
\]

Its invariant distribution is proportional to `\ell_i(q)r_i(q)`. Differentiating the Perron eigenvalue gives

\[
\psi'(q)
=
-\sum_{i,j}\pi_q(i)Q_q(i,j)x_{ij}.
\tag{6.2}
\]

Hence the tilted-spine typical local exponent is

\[
\boxed{a(q)=-\psi'(q)=-\phi'(1+q).}
\tag{6.3}
\]

and the candidate dimension is

\[
\boxed{
F(q)=\psi(q)-q\psi'(q)
=\phi(1+q)-q\phi'(1+q).
}
\tag{6.4}
\]

Equivalently, with `beta=1+q`,

\[
\boxed{
F(\beta)=\phi(\beta)-(\beta-1)\phi'(\beta)
=\phi(\beta)+(\beta-1)a_\beta,
\quad a_\beta=-\phi'(\beta).
}
\tag{6.5}
\]

At the un-tilted failed-tree point `q=0`,

\[
F(0)=\psi(0)=\phi(1)=\dim_H\partial S,
\]

so the formula is anchored to the source's already-proved dimension theorem.

## 7. Theorem proved this run — interior finite-type failed-boundary spectrum

### Theorem R14-H0008-01

Assume the source finite-type branching reduction, and in addition:

1. `M(1)` is irreducible and supercritical: `rho(M(1))>1`;
2. every allowed transmission satisfies `p_{ij}>0`;
3. the failed offspring vectors have a uniform finite `(1+delta_0)` moment for some `delta_0>0` (the source's exponential-moment regimes are more than sufficient);
4. the pressure `phi(beta)=log rho(M(beta))` is evaluated on a real neighborhood of `beta=1` via (4.1);
5. the transmission displacement is nondegenerate at `beta=1`, equivalently
   \[
   \phi''(1)>0.
   \tag{7.1}
   \]

Then there exists `eta>0` such that, on survival of the failed Galton--Watson tree, for every

\[
\beta\in[1-\eta,1+\eta],
\qquad
a_\beta=-\phi'(\beta),
\]

the level set

\[
E(a_\beta)
:=
\left\{\xi\in\partial S:
\lim_{n\to\infty}-\frac1n\log W(\xi|n)=a_\beta
\right\}
\]

has almost surely

\[
\boxed{
\dim_H E(a_\beta)
=
\phi(\beta)-(\beta-1)\phi'(\beta).
}
\tag{7.2}
\]

Equivalently, on the closed exponent interval

\[
A_\eta
=
[a_{1+\eta},a_{1-\eta}],
\]

\[
\boxed{
\dim_H E(a)
=
\inf_{\gamma}
\{\phi(\gamma)+(\gamma-1)a\}
}
\tag{7.3}
\]

whenever the minimizer lies in `[1-eta,1+eta]`. Moreover

\[
|A_\eta|
=\phi'(1+\eta)-\phi'(1-\eta)>0.
\tag{7.4}
\]

Thus the H0008 interval metric moves from `0` to at least the strictly positive exact symbolic quantity in (7.4) on this source-valid nondegenerate finite-type slice. No numerical estimate is promoted to a rigorous endpoint.

### Proof

Put `q=beta-1` and use the branching-random-walk representation (4.2)--(4.3).

#### Step 1: first-moment upper bound

For generation `n`,

\[
Z_n(q):=\sum_{|u|=n}e^{-qS(u)}.
\]

Perron--Frobenius theory on a compact `q`-interval gives a constant `C_q<infty` with

\[
\mathbb E_i Z_n(q)
=e_i^T\widehat M(q)^n\mathbf1
\le C_q e^{n\psi(q)}.
\tag{7.5}
\]

Let `N_n(a,delta)` count generation-`n` failed vertices with

\[
|S(u)/n-a|\le\delta.
\]

For either sign of `q`,

\[
N_n(a,\delta)
\le
\exp\{n(qa+|q|\delta)\}Z_n(q).
\tag{7.6}
\]

By (7.5), Markov's inequality, and Borel--Cantelli, for every `epsilon>0`, almost surely for all large `n`,

\[
Z_n(q)\le e^{n(\psi(q)+\epsilon)}.
\]

Therefore

\[
\limsup_{n\to\infty}\frac1n\log N_n(a,\delta)
\le
\psi(q)+qa+|q|\delta+\epsilon.
\]

Cover `E(a)` by its generation-`n` cylinders, whose diameters are `e^{-n}` in the source tree-boundary metric. Letting `epsilon,delta downarrow0` and then infimizing in `q` yields

\[
\dim_H E(a)
\le
\inf_q\{\psi(q)+qa\}.
\tag{7.7}
\]

This part uses no second moment.

#### Step 2: multitype additive martingale

Let `r(q)` be the positive right Perron vector of `widehat M(q)`. Normalize, for a root of type `i`,

\[
\mathcal W_n(q)
:=
\frac{e^{-n\psi(q)}}{r_i(q)}
\sum_{|u|=n}e^{-qS(u)}r_{\tau(u)}(q).
\tag{7.8}
\]

By the branching property and the Perron equation, `(mathcal W_n(q))` is a mean-one nonnegative martingale.

At `q=0`, its interior/nonboundary condition is

\[
\psi(0)-0\psi'(0)=\phi(1)>0.
\]

The finite `(1+delta_0)` offspring moment and bounded finite-type displacements imply the standard Biggins--Kyprianou `L log L` condition at `q=0`; by continuity, after shrinking `eta`, the additive martingales are uniformly integrable, indeed `L^{1+delta}`-bounded for some `delta>0`, throughout `|q|<=eta`. Hence

\[
\mathcal W_n(q)\to\mathcal W_\infty(q)
\]

in `L^1` and almost surely, with `mathcal W_infty(q)>0` on survival. This is exactly the multitype measure-change regime of Biggins--Kyprianou (2004); the stronger simultaneous convergence used here is also covered by Biggins--Rahimzadeh Sani (2005)/Barral (2001).

#### Step 3: boundary Gibbs measure and spine

For a vertex `u` at depth `n`, write `mathcal W_infty^{(u)}(q)` for the corresponding normalized limit in its descendant subtree. Define on cylinders

\[
\mu_q([u])
=
\frac{
 e^{-n\psi(q)-qS(u)}
 r_{\tau(u)}(q)
 \mathcal W_\infty^{(u)}(q)
}{
 r_i(q)\mathcal W_\infty(q)
}.
\tag{7.9}
\]

The martingale recursion makes these cylinder masses consistent, so `mu_q` is a probability measure on `partial S` on survival.

Under the associated Peyriere/spine law, the type process is the finite-state irreducible Markov chain (6.1). Perron differentiation gives (6.2), and the Markov ergodic theorem therefore gives, for `mu_q`-almost every ray, almost surely,

\[
\frac{S(\xi|n)}n\longrightarrow -\psi'(q)=a(q).
\tag{7.10}
\]

Thus `mu_q(E(a(q)))=1`.

#### Step 4: exact dimension of the tilted measure

Taking logarithms in (7.9),

\[
-\frac1n\log\mu_q([\xi|n])
=
\psi(q)+q\frac{S(\xi|n)}n
-\frac1n\log\mathcal W_\infty^{(\xi|n)}(q)
+o(1),
\tag{7.11}
\]

since the finite-type Perron-vector factors are uniformly bounded above and below.

The remaining subtree-martingale term is subexponential along the spine. For the lower tail, size bias gives

\[
\mathbb P_q\{\mathcal W_\infty^{(\xi|n)}<e^{-\varepsilon n}\}
\le e^{-\varepsilon n},
\]

up to a type-dependent bounded normalization. For the upper tail, the `L^{1+delta}` bound gives

\[
\mathbb P_q\{\mathcal W_\infty^{(\xi|n)}>e^{\varepsilon n}\}
\le C e^{-\delta\varepsilon n}.
\]

Both are summable, so Borel--Cantelli gives

\[
\frac1n\log\mathcal W_\infty^{(\xi|n)}(q)\to0
\quad \mu_q\text{-a.e.}
\tag{7.12}
\]

Combining (7.10)--(7.12),

\[
\lim_{n\to\infty}
-\frac1n\log\mu_q([\xi|n])
=
\psi(q)-q\psi'(q).
\tag{7.13}
\]

By the mass-distribution/Frostman principle,

\[
\dim_H E(a(q))
\ge
\psi(q)-q\psi'(q).
\tag{7.14}
\]

The upper bound (7.7), evaluated at the same `q`, gives the reverse inequality. Hence equality holds and, after substituting `beta=1+q`, gives (7.2)--(7.3).

#### Step 5: a genuine interval

The source pressure is real analytic. Assumption `phi''(1)>0` and continuity give `phi''>0` on a sufficiently small symmetric interval `[1-eta,1+eta]`. Therefore

\[
a_\beta=-\phi'(\beta)
\]

is strictly monotone there, and its image is the nonzero closed interval `A_eta`. At the same time

\[
F(1)=\phi(1)>0,
\]

so shrinking `eta` again keeps the martingale strictly inside the nondegenerate Biggins region and preserves the `L^{1+delta}` bounds used above. This proves (7.4) and completes the theorem. QED.

## 8. What `phi''(1)>0` means — and why the homogeneous case is not a counterexample

For the finite-state tilted chain, `phi''(1)` is the asymptotic variance of the additive edge observable `x_{ij}=-log p_{ij}` under the `beta=1` Perron/spine chain. It vanishes exactly in the coboundary/zero-variance case

\[
x_{ij}=c+h_i-h_j
\]

on the recurrent allowed edge graph. Then every long ray has the same asymptotic transmission exponent `c`, so a nonzero-width multifractal spectrum is not expected. The one-type constant-`p` sanity check is exactly this degenerate case.

Thus the theorem does not hide the exceptional case: H0008 has a genuine spectrum whenever the source pressure has nonzero local curvature; if the pressure is affine, the level-set spectrum collapses to the single deterministic exponent, as it should.

## 9. Status relative to the source

Honest label: **PARTIAL**.

What is now proved in this R14 package:

- the correct failed-tree BRW pressure is `psi(q)=phi(1+q)`;
- the pressure spectrum on a nondegenerate finite-type source slice is rigorously
  \[
  \dim_H E(a_\beta)
  =\phi(\beta)-(\beta-1)\phi'(\beta);
  \]
- a nonzero exponent interval is certified whenever `phi''(1)>0` and the source offspring moment assumptions put the additive martingales in the standard interior `L^{1+delta}` regime.

What is **not** proved:

1. the harmonic-measure/dimension-drop clause of H0008;
2. a boundary spectrum beyond the finite-type front-decoupled reduction in source regimes where that reduction itself remains conjectural;
3. any claim that the multitype BRW/cascade theorem is new rather than an application of classical Biggins/Barral machinery;
4. an explicit numerical value of `eta` or the interval width for a particular source parameter instance.

No numerical estimate is a rigorous metric endpoint.

## 10. Metric ledger

```yaml
ledger_delta:
  worker: R14
  category: HARD_OUTSIDE
  source_id: H0008
  source_target: "Kumar 2026, arXiv:2608.15987, Section 12.3 open problem (6), Boundary fluctuations"
  status: OPEN_PARTIAL
  claim:
    path: operations/claims/H0008.md
    creation_commit: 86b31650d55fa126f2a0cfe1fa780d8f6142b1c6
    readback_at_creation_commit: true
  metric:
    name: I_mf
    meaning: "proved nonzero interval length for transmission-weight local-exponent spectrum"
    before: 0
    after: ">= phi'(1+eta)-phi'(1-eta) > 0 on the stated nondegenerate finite-type slice"
    numerical_value: UNMEASURED
    movement: true
  theorem_claims:
    - R14-H0008-01
  methods_tried: [1, 5, 25]
  exact_checker:
    script: artifacts/R14/2026-09-19T01-50-21Z_h0008_pressure_shift_checker.py
    output: artifacts/R14/2026-09-19T01-50-21Z_h0008_pressure_shift_checker.out
    result: ALL_EXACT_CHECKS_PASS
  source_closure: false
  audits_completed: []
  audits_required_if_full_closure: [P26, OTHER_DISTINCT_TRACK]
  prior_handoffs_reopened: false
```

Because this run moves the H0008 metric, the H0008 unchanged-run/stuck-recovery count starts at zero after movement; no Section-I recovery is triggered.

## 11. Next genuinely different methods

Do not repeat #1/#5/#25 next run. The next H0008 attack should use:

- **#11 DUALIZE:** express the harmonic measure through conductance/flow duality on the failed tree and identify the correct transfer operator;
- **#21 ASK WHO ELSE HAS THIS SHAPE:** compare with Lyons--Pemantle--Peres / Avez entropy, branching harmonic measure dimension drop, and random-conductance trees rather than continuing BRW cylinder counting;
- **#29 ADD THE POINTS AT INFINITY:** treat the end boundary plus Martin boundary as the natural compactification and test whether the source `K_infty` essential spectrum controls the harmonic-measure local dimensions.

The next metric-moving result should address the *second* H0008 clause or extend the first clause beyond the front-decoupled finite-type reduction. Another restatement of the BRW Legendre transform is not enough.

## 12. Model/scheduler control-plane truth

The prompt requests GPT-6 with maximum reasoning. The actually exposed model for this invocation is GPT-5.6 Sol, and authenticated reasoning-effort telemetry is unavailable, so the reasoning level is UNVERIFIED. I do not claim GPT-6 or verified maximum reasoning.

The exposed task-control surface still does not provide a binding model-family selector, a binding reasoning-effort selector, guaranteed hour-long execution, or authenticated completed-run model telemetry. Enforcing GPT-6/maximum would require an owner-authorized product/workspace/API/admin surface that exposes persistent model/reasoning controls plus runtime attestation.

The historical P26 response `You cannot modify this task` is an authorization-context boundary. The lawful workaround is the owning/otherwise authorized task context or authorized platform/admin support; it is not to duplicate the task, bypass permissions, or edit repository state and call that a scheduler repair.

No email, Drive, public posting, purchase, permission change, workflow execution, or scheduler change was made in this run.
