Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. NO FIXED-METRIC MOVEMENT on H0008: `I_mf: >= phi'(1+eta)-phi'(1-eta)>0 -> same`; this is the second consecutive unchanged H0008 run after the preceding movement. Methods actually used: #6 DEFORM TO A POINT YOU CAN SOLVE, #18 SAY IT IN ANOTHER LANGUAGE, #23 DO WHAT THE PROPOSER DID NOT EXPECT.**

# R14 HARD OUTSIDE — H0008: full finite-tilt multifractal phase

## 0. Continuity and ownership

This run preserves all mandatory R14 handoffs. I do **not** reopen the original negative-margin spherical-perceptron target, H0017, D0036, D0039, or D0034. The active exclusive R14 HARD OUTSIDE claim remains

`operations/claims/H0008.md`,

for Achyut Kumar, *Threshold cascades of interacting diffusions on unimodular random trees: a conditional branching-process universality theorem, the annealed pressure, and the dimension of the failed boundary*, arXiv:2608.15987v1 (17 Aug 2026), Section 12.3, open problem (6), “Boundary fluctuations.”

The verified intake identifies the target as the multifractal spectrum of transmission-weighted flows (the Legendre transform associated with the pressure of Definition 5.2), together with the harmonic-measure question for the failed cluster. The first clause is the object below. The harmonic-measure clause is not claimed solved.

Before research I recovered the current campaign `INDEX.md` and `RANKING.md`, root `POSTED.md`, root `RESULTS.md`, `QUEUE.md`, the latest owner directive, the H-intake verification, the canonical H0008 claim, the two preceding R14 H0008 reports, and neighboring admission/ownership reports. The current canonical claim is still R14/HARD OUTSIDE; no release, reassignment, POSTED exclusion, or source-resolution record was found.

## 1. Current primary/later-source check — 19 Sep 2026

The current primary arXiv record for 2608.15987 is still the August 2026 manuscript. It states the finite-type Galton–Watson reduction, the tilted-matrix pressure

\[
\phi(\beta)=\log\rho(M(\beta)),
\]

and the already-proved failed-boundary dimension `log rho(M)` conditional on the reduction. The paper itself explicitly places boundary fluctuations beyond its proved dimension theorem. A bounded current search on 19 Sep 2026 found no later primary paper explicitly claiming a resolution of H0008. This is bounded negative evidence, not a novelty certificate.

The relevant classical machinery is substantial and must be credited rather than rediscovered:

- Biggins–Kyprianou, *Measure change in multitype branching*, Adv. Appl. Probab. 36 (2004), 544–581: general-type martingale change of measure and Kesten–Stigum / `X log X` criteria, developed in particular for branching-random-walk martingales.
- Biggins–Rahimzadeh Sani, *Convergence results on multitype, multivariate branching random walks*, Adv. Appl. Probab. 37 (2005), 681–705: uniform transform convergence, smooth Perron–Frobenius theory, and particle-count large deviations for multitype BRW.
- Barral, *Generalized vector multiplicative cascades*, Adv. Appl. Probab. 33 (2001), 874–895: simultaneous convergence of uncountable families of cascade martingales and dimensions of the associated boundary measures.
- Attia–Barral, *Hausdorff and Packing Spectra, Large Deviations, and Free Energy for Branching Random Walks in R^d*, CMP 331 (2014), 139–187, plus the 2017 erratum: the one-type theory computes the whole spectrum, including non-gradient/phase-transition levels. I do **not** silently import this one-type theorem into the multitype source model; it is used only as a guide to what the finite-tilt theorem should look like.

Thus no claim below is a novelty claim for generic BRW technology. The source-specific work is the exact failed-tree normalization and the verification that the source finite-type pressure enters the multitype BRW theorem with the `beta=1` shift.

## 2. Frozen metric and previous state

The canonical metric remains

`I_mf` = length of a closed nonzero interval of local transmission exponents on which a complete source-normalized pressure-spectrum equality has been proved.

The first H0008 run proved, under the stated nondegenerate finite-type BRW hypotheses, that for **some** `eta>0`,

\[
\dim_H E(-\phi'(\beta))
=
\phi(\beta)-(\beta-1)\phi'(\beta),
\qquad |\beta-1|\le \eta,
\]

and hence

\[
I_{mf}\ge \phi'(1+\eta)-\phi'(1-\eta)>0.
\]

The second H0008 run did not move this fixed quantity. It instead isolated the harmonic-conductance recursion and proved that the entire pressure curve cannot determine harmonic measure.

This run globalizes the multifractal theorem from a neighborhood of `beta=1` to the **entire finite-tilt positive free-energy phase**, but because the frozen metric was recorded only through an existential, unspecified `eta`, and because zero-temperature `|beta|=infinity` endpoints can still matter when the positive phase is unbounded, I do **not** manufacture a strict numerical/symbolic interval-length improvement. The fixed metric honestly remains at its previous certified lower bound.

## 3. Source normalization recovered exactly

Work under the source finite-type branching reduction. Let the finite type set be `D`. Write

\[
B_{ij}=m_*q(j),
\qquad
M(\beta)_{ij}=B_{ij}p_{ij}^{\beta},
\qquad p_{ij}\in(0,1]
\]

on allowed type transitions. Thus the actual failed-child mean matrix is `M(1)`.

For an actual failed edge of type `i->j`, define the displacement

\[
x_{ij}=-\log p_{ij}\ge0.
\]

For a failed descendant `u` at generation `n`, let

\[
S(u)=\sum_{e\in[o,u]}x_e,
\qquad
W(u)=e^{-S(u)}=\prod_{e\in[o,u]}p_e.
\]

The actual failed genealogy is a finite-type BRW whose mean Laplace matrix at BRW tilt `q` is

\[
\widehat M(q)_{ij}
=M(1)_{ij}e^{-q x_{ij}}
=B_{ij}p_{ij}^{1+q}
=M(1+q)_{ij}.
\]

Therefore its BRW pressure is

\[
\boxed{\psi(q)=\log\rho(\widehat M(q))=\phi(1+q).}
\tag{3.1}
\]

This is the same normalization correction proved and exactly sanity-checked in the first H0008 run. In particular, the failed-tree Legendre expression is

\[
\boxed{
D(a)=\inf_{q\in\mathbb R}\{\psi(q)+qa\}
=\inf_{\beta\in\mathbb R}\{\phi(\beta)+(\beta-1)a\}.
}
\tag{3.2}
\]

The unshifted `phi(beta)+beta a` would count the potential tree rather than the already-failed genealogy in the constant-transmission test.

## 4. Method #6 — deform all the way to the exact martingale failure boundary

The previous proof stopped in a small neighborhood of `q=0`. There is no intrinsic reason to stop there.

Let

\[
\lambda(q)=e^{\psi(q)}=\rho(\widehat M(q))
\]

and choose positive right/left Perron vectors `r(q), ell(q)`, normalized by `ell(q)^T r(q)=1`. Define the tilted type kernel

\[
Q_q(i,j)
=\frac{\widehat M(q)_{ij}r_j(q)}{\lambda(q)r_i(q)}.
\tag{4.1}
\]

Its invariant law is `pi_q(i)=ell_i(q)r_i(q)` after normalization. Perron differentiation gives

\[
\psi'(q)
=-\sum_{i,j}\pi_q(i)Q_q(i,j)x_{ij}.
\tag{4.2}
\]

Hence the local exponent selected by tilt `q` is

\[
\boxed{a(q)=-\psi'(q)=-\phi'(1+q).}
\tag{4.3}
\]

Define the tilted free-energy / dimension function

\[
\boxed{
F(q)=\psi(q)-q\psi'(q)
=\phi(1+q)-q\phi'(1+q).
}
\tag{4.4}
\]

At `q=0`,

\[
F(0)=\psi(0)=\phi(1)=\log\rho(M(1))>0
\]

in the supercritical source regime.

The exact derivative is

\[
F'(q)=-q\psi''(q).
\tag{4.5}
\]

When the transmission cocycle is non-coboundary, the Green–Kubo/Perron variance satisfies `psi''(q)>0` for every finite `q` on the fixed strongly connected support. Then `F` increases on `(-infinity,0]`, decreases on `[0,infinity)`, and the finite-tilt nondegenerate phase is the interval

\[
\mathcal J=\{q\in\mathbb R:F(q)>0\}
\tag{4.6}
\]

containing `0`.

The point of the deformation is that the proof mechanism has an exact failure criterion: **it works for every finite `q` with `F(q)>0`, and the additive martingale becomes critical when `F(q)=0`.** There is no separate small-`eta` obstruction.

## 5. Method #18 — say it in the additive-martingale / spine language

### Theorem R14-H0008-03 (entire finite-tilt positive phase)

Assume:

1. the source finite-type front-decoupled Galton–Watson reduction;
2. `M(1)` is irreducible and supercritical;
3. the allowed type-transition support is strongly connected and every allowed `p_ij` is strictly positive;
4. the failed offspring vectors have a uniform finite `(1+delta)` moment for some `delta>0`;
5. the finite-type transmission cocycle is non-coboundary when a nontrivial interval of exponents is desired.

Let `psi`, `F`, `a(q)` be (3.1), (4.4), (4.3). Then on survival:

**(i)** for every finite `q` with `F(q)>0`,

\[
\boxed{
\dim_H E(a(q))
=F(q)
=\phi(1+q)-q\phi'(1+q).
}
\tag{5.1}
\]

Equivalently, writing `beta=1+q`,

\[
\boxed{
\dim_H E(-\phi'(\beta))
=\phi(\beta)-(\beta-1)\phi'(\beta).
}
\tag{5.2}
\]

**(ii)** the conclusion can be made simultaneous for all `q` in any compact `K subset mathcal J`; hence the previous local theorem extends to every compact part of the whole finite-tilt positive phase.

**(iii)** if `q_*` is finite and `F(q_*)=0`, then

\[
\dim_H E(a(q_*))=0.
\tag{5.3}
\]

No non-emptiness assertion is needed for (5.3); under the standard convention `dim_H emptyset=0`, the upper bound is already sharp as a dimension statement.

**(iv)** if `F(q)<0`, then almost surely

\[
E(a(q))=\varnothing.
\tag{5.4}
\]

Thus finite `q` is completely classified. The only spectrum pieces not covered by this theorem are possible **zero-temperature endpoints** arising as `q -> +/- infinity` when `mathcal J` is unbounded, plus the separate harmonic-measure clause of H0008.

### Proof

#### Step 1. First-moment upper bound for every finite tilt

For generation `n`, set

\[
Z_n(t)=\sum_{|u|=n}e^{-tS(u)}.
\]

For fixed finite `t`, finite-dimensional Perron–Frobenius theory gives `C_t<infinity` such that

\[
\mathbb E_i Z_n(t)
=e_i^T\widehat M(t)^n\mathbf 1
\le C_t e^{n\psi(t)}.
\tag{5.5}
\]

Let `N_n(a,epsilon)` count generation-`n` failed vertices satisfying

\[
|S(u)/n-a|\le\epsilon.
\]

For either sign of `t`,

\[
N_n(a,\epsilon)
\le e^{n(ta+|t|\epsilon)}Z_n(t).
\tag{5.6}
\]

Indeed, on the indicated window `e^{-tS(u)}` is bounded below by `exp[-n(ta+|t|epsilon)]`.

Combining (5.5), Markov's inequality and Borel–Cantelli yields, almost surely,

\[
\limsup_{n\to\infty}\frac1n\log N_n(a,\epsilon)
\le \psi(t)+ta+|t|\epsilon.
\tag{5.7}
\]

The generation metric on the boundary has cylinders of diameter `e^{-n}`, so letting `epsilon downarrow0` and optimizing over `t` gives

\[
\dim_H E(a)
\le \inf_t\{\psi(t)+ta\}.
\tag{5.8}
\]

At `a=a(q)=-psi'(q)`, convexity makes `t=q` the minimizer and therefore

\[
\dim_H E(a(q))\le F(q).
\tag{5.9}
\]

If `F(q)<0`, choose `epsilon` small enough that the right side of (5.7) is negative at `t=q`. Then `N_n(a(q),epsilon)=0` for all sufficiently large `n`; an infinite ray with limiting exponent `a(q)` would supply one such vertex at every large generation, contradiction. This proves (iv). If `F(q)=0`, (5.9) gives (iii).

#### Step 2. The Perron additive martingale

For a root of type `i`, define

\[
\mathcal W_n^{(i)}(q)
=\frac{e^{-n\psi(q)}}{r_i(q)}
\sum_{|u|=n}e^{-qS(u)}r_{\tau(u)}(q).
\tag{5.10}
\]

The Perron equation for `widehat M(q)` gives

\[
\mathbb E_i\mathcal W_n^{(i)}(q)=1,
\]

and the branching property gives the martingale property.

Under the `q`-spine change of measure, a type transition `i->j` has law (4.1). The logarithm of the one-step normalized multiplicative factor is

\[
\log A_q(i,j)
=-q x_{ij}-\psi(q)+\log r_j(q)-\log r_i(q).
\]

Taking its stationary `pi_q Q_q` mean and using (4.2), the Perron-vector coboundary averages to zero and

\[
\mathbb E_{\mathrm{sp},q}[\log A_q]
=q\psi'(q)-\psi(q)
=-F(q).
\tag{5.11}
\]

Hence `F(q)>0` is exactly negative logarithmic drift of the normalized factor along the size-biased spine.

Because the edge displacements take only finitely many values and the failed offspring vector has a `(1+delta)` moment, the one-generation martingale family satisfies the corresponding `X log X` domination. Biggins–Kyprianou's multitype measure-change criterion therefore yields uniform integrability at every finite `q` with `F(q)>0`, and

\[
\mathcal W_n^{(i)}(q)\to\mathcal W_\infty^{(i)}(q),
\qquad
\mathcal W_\infty^{(i)}(q)>0
\]

on survival.

On a compact `K subset mathcal J`, continuity of the Perron data, boundedness of the finite displacement alphabet and the same `(1+delta)` domination are uniform. The uniform multitype BRW transform theorem of Biggins–Rahimzadeh Sani, equivalently the simultaneous cascade machinery of Barral in this finite-state setting, gives a version with simultaneous convergence throughout `K`.

#### Step 3. The tilted boundary measure

For a vertex `u` at generation `n`, let `W_infty^{(u)}(q)` be the martingale limit in the descendant subtree rooted at `u`. Define the cylinder measure

\[
\mu_q([u])
=
\frac{e^{-qS(u)-n\psi(q)}r_{\tau(u)}(q)
      \mathcal W_\infty^{(u)}(q)}
     {r_i(q)\mathcal W_\infty^{(i)}(q)}.
\tag{5.12}
\]

The martingale branching identity makes these cylinder masses consistent and their total mass one.

Under the associated spine law, the type chain has kernel `Q_q`; therefore the finite-state ergodic theorem and (4.2) give

\[
\frac{S(\xi|n)}n\longrightarrow
-\psi'(q)=a(q)
\qquad \mu_q\text{-a.s.}
\tag{5.13}
\]

The remaining subtree-martingale factor is subexponential along the spine. One convenient proof uses a slightly smaller positive moment supplied by the `(1+delta)` assumption and compact containment in `mathcal J`: the upper tail is summable by Markov, while under the size-biased spine law the lower tail satisfies the elementary size-bias bound `E[W 1_{W<e^{-cn}}] <= e^{-cn}`. Borel–Cantelli therefore gives

\[
\frac1n\log\mathcal W_\infty^{(\xi|n)}(q)\to0.
\tag{5.14}
\]

Since the Perron vector ranges over finitely many types,

\[
\frac1n\log r_{\tau(\xi|n)}(q)\to0.
\]

Taking logarithms in (5.12), using (5.13)–(5.14), gives

\[
\lim_{n\to\infty}
-\frac1n\log\mu_q([\xi|n])
=\psi(q)+q a(q)
=F(q)
\qquad \mu_q\text{-a.s.}
\tag{5.15}
\]

Thus `mu_q` is exact-dimensional with dimension `F(q)` and is supported on `E(a(q))`. The mass-distribution principle yields

\[
\dim_H E(a(q))\ge F(q),
\]

which together with (5.9) proves (i). Uniform convergence on compact `K` yields (ii).

This completes the theorem.

## 6. What this says in the source `beta` coordinate

Put `beta=1+q` and define

\[
G(\beta)
=\phi(\beta)-(\beta-1)\phi'(\beta).
\tag{6.1}
\]

Then

\[
G'(\beta)=-(\beta-1)\phi''(\beta).
\tag{6.2}
\]

In the non-coboundary case, `phi''(beta)>0` for finite `beta`, so the positive phase

\[
\mathcal B=\{\beta:G(\beta)>0\}
\]

is an interval containing `1`, and the source-normalized spectrum is proved at **every finite point** of `mathcal B`:

\[
\boxed{
D(-\phi'(\beta))
=G(\beta).
}
\tag{6.3}
\]

If a finite endpoint `beta_*` satisfies `G(beta_*)=0`, its corresponding level has Hausdorff dimension zero by the same first-moment bound. If `G(beta)<0`, the corresponding exponent does not occur on any infinite failed ray almost surely.

Therefore, when both ends of `mathcal B` are finite, the multifractal spectrum is completely determined on the full closed exponent interval

\[
[-\phi'(\beta_+),-\phi'(\beta_-)]
\]

including its zero-dimensional endpoints. In that subclass there is no remaining finite-tilt gap.

When one end of `mathcal B` is infinite, a residual `beta -> +/- infinity` zero-temperature problem remains. It is a finite-state tropical/max-plus problem: the limiting slopes are extremal cycle means of `log p_ij`, and a positive-dimensional endpoint can survive if the branching restricted to the corresponding max-plus critical graph remains supercritical. I do **not** promote that endpoint classification without writing its full proof.

## 7. Method #23 — the source's first clause is much closer to classical than the operator wording suggests

The source motivates an infinite-dimensional boundary operator for fluctuations. For the **transmission-weight multifractal clause**, the finite-type reduction already contains enough structure to bypass that operator at every finite tilt. Once one conditions on the actual failed genealogy and applies the mandatory `beta=1` pressure shift, the problem is a standard finite-type BRW cascade. Classical multitype martingale and uniform-transform theorems then push the previous local result all the way to the exact free-energy boundary `G=0`.

This is an important route correction:

- the obstruction is **not** loss of Perron analyticity away from `beta=1`;
- it is **not** lack of a small neighborhood in which the tilted spine exists;
- the exact finite-tilt obstruction is `G(beta)=0`, i.e. additive-martingale criticality;
- what remains beyond finite tilt is a zero-temperature/max-plus endpoint analysis, plus the separate harmonic-measure problem.

The Attia–Barral one-type theorem is a warning that the endpoint problem should not be dismissed: it explicitly handles levels outside the gradient range and first-order phase transitions, and its 2017 erratum repairs a uniform-nondegeneracy issue. Any attempt to claim complete H0008 closure must either port that endpoint technology rigorously to this multitype source model or solve the finite-state max-plus critical-graph endpoint directly.

## 8. Why the fixed metric does not move despite the stronger theorem

The theorem is strictly stronger as a **scope statement** than the previous local-`eta` result: it proves every finite tilt in the positive free-energy phase. But the frozen metric is a numerical/symbolic interval length. The previous value was recorded only as

\[
I_{mf}\ge\phi'(1+\eta)-\phi'(1-\eta)>0
\quad\text{for some unspecified }\eta>0.
\]

Without a previously frozen numerical `eta`, and without closing every possible unbounded zero-temperature endpoint, there is no honest strict inequality between the old lower bound and a newly named closed interval length. I therefore record **no movement** rather than redefining the metric after seeing the result.

This is the second consecutive H0008 run with unchanged `I_mf` after the first run's movement. The shared/global stagnation count remains UNKNOWN; the own-track H0008 sequence is: movement, unchanged, unchanged. A third consecutive unchanged H0008 run would trigger Section I on the next invocation.

## 9. Remaining obligation and next nonrepeating methods

The cleanest remaining mathematical obligation is now the zero-temperature endpoint statement:

\[
\boxed{
\text{classify }\lim_{\beta\to\pm\infty}
\bigl[\phi(\beta)-(\beta-1)\phi'(\beta)\bigr]
\text{ and the corresponding extremal-ray level sets.}
}
\]

The likely finite-state object is the max-plus critical graph of the edge potential `log p_ij`, with ordinary Perron growth of the failed-child mean matrix restricted to critical edges after max-plus conjugation. This is where an actual closed maximal exponent interval, rather than an arbitrary compact subinterval, should emerge.

The next nonrepeating Section-B moves are **#8 GO THE OTHER WAY AND DISCRETIZE, #12 FIND WHAT IS CONSERVED, #17 LOOK FOR YOUR NUMBERS SOMEWHERE ELSE**: discretize the endpoint as a finite critical-cycle problem, identify the max-plus potential/cycle-mean invariant, and compare the residual entropy constant with known zero-temperature thermodynamic/max-plus Perron asymptotics.

The harmonic-measure clause remains separate. The previous run's conductance recursion and pressure-insufficiency counterexample remain valid handoff material but are not used to inflate the fixed multifractal metric.

## 10. Artifacts / audit boundary

No new finite enumeration or finite certificate is claimed in this run, so no checker-only artifact was manufactured. The new claim is theorem-sized and its proof is on the page above, as required. Existing exact artifacts from the preceding H0008 runs are preserved unchanged.

This report is a **self-check**, not an independent audit. H0008 is **PARTIAL / SOURCE OPEN**. No closure is claimed. Closure would still require the source's full requested scope, prior-art resolution at theorem-level precision, and the two required independent audits.

## structured ledger_delta

```yaml
ledger_delta:
  worker: R14
  category: HARD_OUTSIDE
  target: H0008
  source: "Kumar 2026, arXiv:2608.15987v1, Section 12.3 open problem (6)"
  status_before: PARTIAL
  status_after: PARTIAL
  metric: I_mf
  metric_before: ">= phi'(1+eta)-phi'(1-eta)>0 for some certified eta>0"
  metric_after: ">= phi'(1+eta)-phi'(1-eta)>0 for the same frozen certificate"
  movement: false
  own_h0008_consecutive_unchanged_after_prior_movement: 2
  authoritative_shared_stagnation_count: UNKNOWN
  methods_used: [6, 18, 23]
  new_result: "full finite-tilt positive-free-energy spectrum theorem: every finite beta with G(beta)>0 has exact dimension G(beta); finite G=0 endpoints have dimension 0; G<0 levels are absent"
  source_closure: false
  remaining:
    - "zero-temperature beta -> +/-infinity endpoint classification when the positive phase is unbounded"
    - "harmonic-measure clause of H0008"
    - "front-decoupling reduction remains conditional outside source-proved regimes"
    - "two independent audits before closure"
  next_methods: [8, 12, 17]
```

No shared root, peer track, email, Drive item, public post, permission, workflow, or scheduler setting was changed in this run.