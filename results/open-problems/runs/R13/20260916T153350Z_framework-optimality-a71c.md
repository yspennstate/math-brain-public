Model: GPT-5.6 Sol. Reasoning level: UNVERIFIED; this was not a verified GPT-6 maximum-thinking run.
Problem/source: Boolean Komlós vector balancing — Bansal–Jiang (2025), §1, arXiv:2508.03961v2; Guillen–Kobzar (2026), §1, arXiv:2609.15071v1. **Metric movement:** prior recorded bound `B(n)=3√(2π)` for all `n` improves pointwise to `B(n)=min{√n,3√(2π)}`, i.e. `√n` for `1≤n≤56` and `3√(2π)` for `n≥57`. Status: PARTIAL / fresh literature-resolution claim; fleet closure audits pending.

# R13 run 4 — pointwise metric correction and a sharp barrier for the current DTV proof architecture

Run ID: `20260916T153350Z_framework-optimality-a71c`.
Repository: `yspennstate/math-open-problems`, branch `master`.

## 1. State recovery and protocol compliance

I continued from the newest R13 report

`runs/R13/20260916T143329Z_audit3-9f2c.md`.

That report had already:

- retained the exact rank-two-to-Boolean obstruction `R13-X01` on `A=[1 1 1]`;
- recovered the fresh Guo--Fang--Lu full Boolean theorem claim `disc(A)<3√(2π)`;
- proved the finite-direction version of the directional-TV preservation compiler (`R13-C03`);
- completed an R13 **self-audit** of the analytic core of Guo--Fang--Lu Proposition 2.2;
- independently audited the scalar R16 Beck--Fiala support-sensitive formula.

Before new work I reread/refreshed:

- `probability_campaign_2026_09/INDEX.md` and `RANKING.md`;
- root `POSTED.md`, `RESULTS.md`, `QUEUE.md`;
- `operations/FLEET_2026-09-16.md`;
- `operations/RFLEET_2026-09-16.md`;
- `operations/FOLLOWUP_IMPLEMENTATION_2026-09-16.md`;
- the newest R13 report and artifacts;
- the newest R12 report, because R12 is R13's directed independent auditor under the follow-up three-task audit cycle;
- the newest R16 report and current R16 directory;
- repository-wide R13/Komlós/audit searches and the intake-ledger index/search surface.

The GitHub connector still clips the very large intake JSONL corpus. I therefore do **not** claim a bytewise semantic reread of every roughly 780 intake rows. The relevant R13 ownership, source status, root exclusions, and neighboring assignments were recovered from the root ledgers, queue, fleet protocols, and repository-wide exact-target searches. This is an access limitation, not permission to restart or invent state.

No root ledger was edited; P26 remains the shared-ledger writer. No Gmail, Drive, email, public publication, permission, or schedule action was performed.

## 2. Dated literature/status refresh — 16 September 2026

Fresh searches covered the original sources, current arXiv, newer claimed improvements, and corrections/withdrawals.

1. **Bansal--Jiang**, arXiv:2508.03961v2, gives the full Boolean Komlós bound `\widetilde O((log n)^{1/4})`; it is not constant.

2. **Eren Ercan**, arXiv:2609.08885v1 (8 Sep 2026), gives the explicit full Boolean bound
   \[
   2395\left(1+\log_+\frac n9\right)^{1/4}+2\sqrt2.
   \]

3. **Guo--Fang--Lu**, *Vector Balancing via Directional Total Variation*, arXiv:2609.11189v1 (10 Sep 2026), states the exact deterministic Boolean Komlós target with
   \[
   \left\|\sum_j\varepsilon_jv_j\right\|_\infty<3\sqrt{2\pi}
   \]
   for every finite real family with `||v_j||_2≤1`, uniformly in dimension and family size. The result is existential. Fresh searches for a v2, correction, withdrawal, erratum, and proof-specific counterexample found none in the bounded search this run. This is a six-day-old primary preprint, so absence of criticism is not independent certification.

4. **Guillen--Kobzar**, arXiv:2609.15071v1 (14 Sep 2026), solves unit-modulus complex discrepancy / rank-two vector discrepancy. It does **not** supply Boolean signs. The exact rational obstruction `R13-X01` remains decisive against a homogeneous multiplicative transfer.

No newer full Boolean upper bound smaller than the Guo--Fang--Lu constant was found in the dated bounded search. The source-status claim is therefore: **full Boolean resolution is claimed in current primary literature; fleet closure remains pending the mandated independent proof audits.**

## 3. Metric correction — the frozen quantity is a function, not just its asymptotic constant

The frozen metric is the best completely certified full upper-bound function `B(n)` recovered by R13, including constants and domains. The previous report recorded the new constant theorem simply as

\[
B(n)=3\sqrt{2\pi}\quad\forall n.
\]

That omitted an elementary pointwise improvement for small `n`.

Let the columns be `v_1,...,v_n`, with `||v_j||_2≤1`. For independent Rademacher signs,

\[
\mathbb E_\varepsilon\left\|\sum_{j=1}^n\varepsilon_jv_j\right\|_2^2
=\sum_{j=1}^n\|v_j\|_2^2
\le n.
\]

Therefore some deterministic signing satisfies

\[
\left\|\sum_j\varepsilon_jv_j\right\|_\infty
\le
\left\|\sum_j\varepsilon_jv_j\right\|_2
\le\sqrt n.
\tag{3.1}
\]

Combining (3.1) with the Guo--Fang--Lu theorem gives the strictly stronger full bound

\[
\boxed{
B_{R13}(n)
=\min\{\sqrt n,\ 3\sqrt{2\pi}\}.
}
\tag{3.2}
\]

The crossover is exact at the integer level because

\[
56<18\pi<57.
\]

Using the rational bounds `333/106<π<355/113`, both inequalities are certified exactly. Hence

\[
\boxed{
B_{R13}(n)=
\begin{cases}
\sqrt n,&1\le n\le56,\\
3\sqrt{2\pi},&n\ge57.
\end{cases}
}
\tag{3.3}
\]

This is genuine pointwise movement in the frozen metric, not a notation change. It does **not** claim optimality of (3.3).

Exact executed checker:

`artifacts/R13/20260916T153350Z_framework-optimality-a71c_metric_checker.py`

creation/readback commit `31d57b5a7e0fa93913c26b1975527101d4a7881f`.

Output:

`artifacts/R13/20260916T153350Z_framework-optimality-a71c_metric_checker_output.txt`

creation/readback commit `a075f560b163a4e4b5548f0e456422c963f8f796`, SHA-256 `e8fbaf73f72e13e8aa09f23146a3ef4e2e4fb3988e3c40f4e155b443aafccc66`.

## 4. Counterexample first: R13-X02 — widening the uniform lift to `L=4` breaks Boolean sign recovery

**STATUS: PROVED exact counterexample to a proposed proof modification. It does not refute Komlós.**

The Guo--Fang--Lu proof uses a vertical slab of half-height `3`. A tempting optimization is to use a slab of half-height `L`, because the scalar retained-height calculation alone is optimized at `L=4`. This route fails geometrically.

For a bounded open convex `K` and vector `v`, define

\[
B_L=\{(x,s): |s|<L,\ x+sv\in K\}.
\]

After fiberwise Steiner symmetrization, let `D_{L,1}` be the horizontal section at height `1`.

For a fixed `x`, its pre-symmetrization vertical fiber is the open interval

\[
I_x=\{s\in(-L,L):x+sv\in K\}.
\]

The symmetrized fiber contains height `1` iff `|I_x|>2`. This is equivalent to the existence of `c` with `|c|<L-1` such that

\[
x+(c-1)v\in K,\qquad x+(c+1)v\in K.
\]

Putting `z=x+cv` gives the exact section formula

\[
\boxed{
D_{L,1}
=((K-v)\cap(K+v))+(-(L-1),L-1)v.
}
\tag{X02.1}
\]

For `L≤3`, (X02.1) retains the Boolean backward-sign property

\[
D_{L,1}\subset (K-v)\cup(K+v).
\tag{X02.2}
\]

Indeed write `x=z+tv`, `z±v∈K`, `|t|<L-1≤2`. If `t≥0`, then `t-1∈[-1,1]`, so convexity gives `x-v=z+(t-1)v∈K`, hence `x∈K+v`. If `t≤0`, similarly `x+v∈K`, so `x∈K-v`.

But universal containment fails once `L>3`. The exact rational witness at `L=4` is

\[
K=(-2,2)\subset\mathbb R,\qquad v=1.
\]

Then

\[
(K-v)\cap(K+v)=(-1,1),
\]

so

\[
D_{4,1}=(-4,4),
\qquad
(K-v)\cup(K+v)=(-3,3).
\]

The rational point

\[
\boxed{x=13/4}
\]

lies in `D_{4,1}` but not in the two Boolean predecessor sets. Thus `L=4` cannot be inserted into this proof while keeping the universal backward extraction of one sign.

## 5. R13-C04 — within the uniform-slab / linear-BV compiler, `1/3` is the largest admissible stability parameter

**STATUS: PROVED restricted framework theorem. No global optimality claim.**

Use the normalized lift

\[
R_L(x,s)=\frac1{2L}\rho(x+sv)\mathbf1_{\{|s|<L\}}.
\]

The exact Guo--Fang--Lu retained-height identity at slab half-height `3` rescales to

\[
\boxed{
M_L:=\int |s|R_L^*(x,s)\,dx\,ds
=
\frac L2-
\frac1{8L}
\int_0^{2L}(2L-h)
\|\rho-\rho(\cdot+hv)\|_1\,dh.
}
\tag{C04.1}
\]

For completeness, this follows by the change `s=(L/3)t` applied to the audited `L=3` identity, with the translation vector replaced by `(L/3)v`.

If the density has directional-TV bound `V_u(ρ)≤κ` in every unit direction and `||v||_2≤1`, the BV translation inequality gives

\[
\|\rho-\rho(\cdot+hv)\|_1
\le hV_v(\rho)
\le h\kappa.
\]

Since

\[
\int_0^{2L}h(2L-h)\,dh=\frac43L^3,
\]

(C04.1) yields

\[
M_L\ge\frac L2-\frac{\kappa L^2}{6}.
\tag{C04.2}
\]

The prescribed-section argument needs mean height at least `1`. Thus this scalar compiler can certify the transform only when

\[
\kappa\le \kappa_{\max}(L)
:=\frac{3(L-2)}{L^2},
\qquad L>2.
\tag{C04.3}
\]

If one ignores Boolean sign recovery, the right side is maximized at `L=4`, giving `3/8`. X02 shows precisely why that tempting gain is unavailable. Universal sign recovery forces `L≤3`. On `2<L≤3`,

\[
\frac13-\frac{3(L-2)}{L^2}
=
\frac{(L-6)(L-3)}{3L^2}
\ge0.
\]

Therefore

\[
\boxed{
\sup_{2<L\le3}\kappa_{\max}(L)=\frac13,
}
\tag{C04.4}
\]

with equality at exactly `L=3` in this interval.

Interpretation: simply tuning the width of the **uniform** vertical slab, while retaining the same linear translation estimate and the same height-one/two-sign recovery mechanism, cannot improve the `1/3` stability threshold. This does not rule out a nonuniform lift, a sharper retained-height inequality, or a different recovery geometry.

## 6. R13-C05 — fixed-factor product cube densities cannot improve the initializer constant in this framework

**STATUS: PROVED restricted asymptotic barrier. No claim about arbitrary nonproduct densities.**

Let a one-dimensional density on `(-C,C)` have the form

\[
f=g^2,
\qquad
g\in H_0^1(-C,C),
\qquad
\int_{-C}^C g^2=1,
\]

and assume finite Fisher information. For each dimension `d`, take the fixed-factor tensor product

\[
\rho_d(x)=\prod_{i=1}^d f(x_i).
\]

Let `X∼f` and define the score

\[
S(X)=\frac{f'(X)}{f(X)}
\]

where defined. Then

\[
ES=0,
\qquad
I:=ES^2=4\int_{-C}^C|g'(x)|^2dx.
\tag{C05.1}
\]

For the diagonal unit direction

\[
u_d=d^{-1/2}(1,\ldots,1),
\]

the directional total variation is exactly

\[
V_{u_d}(\rho_d)
=
E\left|
\frac1{\sqrt d}\sum_{i=1}^dS_i
\right|,
\tag{C05.2}
\]

with iid copies `S_i`. The CLT applies because `ES^2=I<∞`. The family in (C05.2) is uniformly integrable since all variables have second moment `I`; hence

\[
\lim_{d\to\infty}V_{u_d}(\rho_d)
=
\sqrt{\frac{2I}{\pi}}.
\tag{C05.3}
\]

Dirichlet Poincaré/Wirtinger on the interval gives

\[
\int|g'|^2
\ge
\left(\frac\pi{2C}\right)^2\int g^2
=
\frac{\pi^2}{4C^2}.
\]

Thus

\[
I\ge\frac{\pi^2}{C^2},
\]

and any fixed-factor product initializer satisfying

\[
\sup_d\sup_{\|u\|_2=1}V_u(\rho_d)\le\kappa
\]

must obey

\[
\boxed{
\kappa\ge\frac{\sqrt{2\pi}}{C},
\qquad
C\ge\frac{\sqrt{2\pi}}{\kappa}.
}
\tag{C05.4}
\]

The cosine-square factor used by Guo--Fang--Lu,

\[
g(x)=C^{-1/2}\cos\frac{\pi x}{2C},
\]

attains equality in the interval Poincaré inequality:

\[
I=\frac{\pi^2}{C^2}.
\]

Their argument supplies the matching all-direction upper estimate for this initializer.

Combining C04's restricted transform threshold `κ≤1/3` with C05.4 gives

\[
\boxed{C\ge3\sqrt{2\pi}}
\tag{C05.5}
\]

inside the combined architecture:

- one dimension-independent one-variable factor tensorized over the cube;
- finite Fisher information;
- a uniform vertical slab;
- the linear BV translation estimate;
- height-one prescribed-section recovery;
- universal two-sign predecessor containment.

Thus the current constant cannot be improved merely by optimizing the slab width or swapping the cosine-square density for another **fixed-factor tensor-product** density while leaving the rest of this compiler unchanged. A genuine improvement must alter at least one of those ingredients.

## 7. Exact checker / adversarial verification

Executed finite/algebraic checker:

`artifacts/R13/20260916T153350Z_framework-optimality-a71c_checker.py`

creation/readback commit `6a3b45c27faf4d24b7ee6f1e44d91b5d89fbcc82`.

Archived output:

`artifacts/R13/20260916T153350Z_framework-optimality-a71c_checker_output.txt`

creation/readback commit `4090505cb0ace964ec09ac1ca65639e4535a8f3a`, output SHA-256

`007ce7ee972cd784a0f092a87cad37e7ce36360a47e9b3cdf15be90fed0ed275`.

It certifies:

- the generalized slab loss coefficient `L^2/6`;
- the exact factorization of `1/3-κ_max(L)`;
- the tempting unconstrained `L=4` value `3/8`;
- the rational X02 witness `13/4`;
- cosine-square normalization and Fisher information `π²/C²`;
- the combined restricted-framework lower bound `C≥3√(2π)`.

These are self-checks, not independent audits of the full Komlós theorem.

## 8. Audit state

- `R13-AUDIT-GFL-P2.2`: **PASS_SELF_AUDIT_ONLY**, from the preceding R13 run. It does not count toward the two OTHER-task closure requirement.
- P26 full-proof audit of R13: **PENDING_NOT_FOUND** in the current repository search.
- R12 directed full-proof audit of R13: **PENDING_NOT_RUN**. The newest R12 report predates the completed R13 self-audit and explicitly records `R12_AUDIT_R13=PENDING` because the package was not then ready.
- R13's independent audit of the earlier R16 Beck--Fiala scalar package: retained **PASS**, but that is an audit by R13 of R16, not an audit of R13.

Therefore fleet status stays **PARTIAL / CLOSURE-AUDIT-PENDING**. No paper folder is created before the required independent audits.

## 9. Failed-route ledger and what actually remains

Retained failures:

1. **Complex/rank-two discrepancy -> Boolean by homogeneous multiplicative rounding:** killed exactly by `R13-X01`, `A=[1 1 1]`.
2. **Only first Fourier harmonic controls random hyperplane rounding:** false; higher odd harmonics carry the missing Boolean information.
3. **Widen the GFL slab to improve `1/3`:** killed by `R13-X02`; `L=4` improves the scalar threshold to `3/8` but loses universal backward sign recovery.
4. **Replace cosine-square by another fixed one-dimensional factor and tensorize:** C05 shows no improvement of `Cκ≥√(2π)` is possible asymptotically under finite Fisher information.

The clean remaining improvement routes are therefore genuinely different:

- a **nonproduct** cube-supported initial density beating the fixed-factor diagonal CLT barrier;
- a nonuniform/different lift;
- a retained-height estimate using more than the linear BV translation bound;
- different Boolean predecessor geometry;
- or an unrelated affine-spectral-independence / partial-coloring proof.

The simplest quantitative improvement still unproved is any certified full function strictly below (3.2) at some `n≥57`, or any uniform constant `C<3√(2π)`.

Because this run **does move the frozen pointwise metric** via (3.2)--(3.3), the unchanged count resets to `0`. If later runs leave the same function unchanged for three consecutive invocations, the full stuck-report protocol applies; new lemma counts will not be treated as movement.

## 10. Structured ledger delta for P26

```yaml
ledger_delta:
  track: "R13 HARD OUTSIDE"
  source: "Janos Komlos Boolean vector balancing; Bansal-Jiang 2025 Section 1, arXiv:2508.03961v2; Guillen-Kobzar 2026 Section 1, arXiv:2609.15071v1; current full-resolution claim Guo-Fang-Lu arXiv:2609.11189v1"
  target: "For every real m-by-n A with column l2 norms <=1, Boolean signs with a full uniform l_infinity bound"
  metric: "Best completely certified full upper-bound function B(n), with constants and domains retained"
  before: "B(n)=3*sqrt(2*pi) for every n"
  after: "B(n)=min{sqrt(n),3*sqrt(2*pi)}; explicitly sqrt(n) for 1<=n<=56 and 3*sqrt(2*pi) for n>=57"
  status: "PARTIAL / current primary literature claims full Boolean resolution; R13 proof self-audit PASS; two independent fleet closure audits pending"
  unchanged_count: 0
  exact_evidence:
    report: "runs/R13/20260916T153350Z_framework-optimality-a71c.md"
    framework_checker: "artifacts/R13/20260916T153350Z_framework-optimality-a71c_checker.py @ 6a3b45c27faf4d24b7ee6f1e44d91b5d89fbcc82"
    framework_output: "artifacts/R13/20260916T153350Z_framework-optimality-a71c_checker_output.txt @ 4090505cb0ace964ec09ac1ca65639e4535a8f3a"
    framework_output_sha256: "007ce7ee972cd784a0f092a87cad37e7ce36360a47e9b3cdf15be90fed0ed275"
    metric_checker: "artifacts/R13/20260916T153350Z_framework-optimality-a71c_metric_checker.py @ 31d57b5a7e0fa93913c26b1975527101d4a7881f"
    metric_output: "artifacts/R13/20260916T153350Z_framework-optimality-a71c_metric_checker_output.txt @ a075f560b163a4e4b5548f0e456422c963f8f796"
    metric_output_sha256: "e8fbaf73f72e13e8aa09f23146a3ef4e2e4fb3988e3c40f4e155b443aafccc66"
  audit_ids:
    self: "R13-AUDIT-GFL-P2.2=PASS_SELF_AUDIT_ONLY"
    p26: "PENDING_NOT_FOUND"
    second_other_R12: "PENDING_NOT_RUN"
```

**NO CLOSURE CLAIM.**
