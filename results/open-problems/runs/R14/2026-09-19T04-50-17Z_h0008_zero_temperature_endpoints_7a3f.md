Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. FIXED-METRIC CERTIFICATION MOVEMENT on H0008: `I_mf: only the certified lower bound >= phi'(1+eta)-phi'(1-eta)>0 -> exact full value a_hi-a_lo`; the multifractal clause is complete under the source finite-type branching reduction and hypotheses stated below, while the harmonic-measure clause remains OPEN. Methods actually used: #8 GO THE OTHER WAY AND DISCRETIZE, #12 FIND WHAT IS CONSERVED, #17 LOOK FOR YOUR NUMBERS SOMEWHERE ELSE.**

# R14 HARD OUTSIDE — H0008 zero-temperature endpoints and the full finite-type multifractal interval

## 0. Continuity, ownership, and scope

This run preserves all prior R14 hard-task handoffs. I do **not** reopen the original negative-margin spherical-perceptron target, H0017, D0036, D0039, or D0034. The active exclusive R14 HARD OUTSIDE claim remains `operations/claims/H0008.md`.

The exact outside source is Achyut Kumar (2026), *Threshold cascades of interacting diffusions on unimodular random trees: a conditional branching-process universality theorem, the annealed pressure, and the dimension of the failed boundary*, arXiv:2608.15987v1 (17 Aug 2026), Section 12.3, Open problem (6), **“Boundary fluctuations.”** The source asks for two things on the failed boundary: the multifractal spectrum of transmission-weighted flows (identified with the Legendre-transform problem for the pressure of Definition 5.2) and the harmonic measure of the failed cluster, where a dimension drop is expected.

The canonical H0008 claim freezes

`I_mf` = the length of the largest closed nonzero interval of local transmission exponents on which a complete source-normalized pressure-spectrum equality has been proved under the source finite-type supercritical branching hypotheses.

The first H0008 run moved the certification from `0` to the local lower bound

\[
I_{mf}\ge \phi'(1+\eta)-\phi'(1-\eta)>0
\]

for some proved but unspecified `eta>0`. The second run did not move this metric and instead isolated the harmonic-conductance recursion. The immediately preceding run proved the spectrum at **every finite tilt in the positive free-energy phase**, but correctly did not call that metric movement because the possible `|beta|=infinity` endpoints had not been identified and maximality of the exponent interval had not been proved.

This run closes exactly that zero-temperature gap. It therefore upgrades the fixed metric from a lower-bound-only certification to its **exact full value**. This is certification movement on the already frozen quantity, not a redefinition of the metric.

The source normalization correction from the first H0008 run is retained throughout: the actual failed genealogy has mean matrix `M(1)`, so its branching-random-walk pressure is `psi(q)=phi(1+q)`, and the source-normalized Legendre expression on the failed tree is

\[
D(a)=\inf_{q\in\mathbb R}\{\psi(q)+qa\}
     =\inf_{\beta\in\mathbb R}\{\phi(\beta)+(\beta-1)a\}.
\]

The earlier unshifted `phi(beta)+beta a` would count the potential tree rather than the already-failed genealogy in the constant-transmission sanity check.

## 1. Required repository and current-source read

Before research I reread or targeted-search recovered:

- `probability_campaign_2026_09/INDEX.md` and `RANKING.md`;
- root `POSTED.md`, `RESULTS.md`, and `QUEUE.md`;
- `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md`;
- `operations/claims/H0008.md`;
- the exact H0008 intake wording under `probability_1000_intake_H_20260914/`;
- all three previous H0008 R14 reports, newest first;
- current neighboring source-family history for H0003, H0005, H0006 and H0011.

The current canonical H0008 claim is still R14 / HARD OUTSIDE / SOURCE-OPEN. I found no release, reassignment, POSTED exclusion, or competing owner. Neighboring tracks do not license reopening their source clauses: H0003 is at an audit-pending handoff after a literal-source refutation; H0005 has its own endpoint counterexample history; H0006 was terminally handed off by R12; H0011 was retired after its unchanged-run limit.

Fresh primary-source checks dated 19 Sep 2026 recovered the same arXiv v1 source:

- https://arxiv.org/abs/2608.15987
- companion https://arxiv.org/abs/2608.21125

The companion studies front propagation/Bramson correction and the continuous-type limit theory. It does not claim to settle Open problem (6)'s finite-type boundary multifractal spectrum or harmonic measure. A bounded current search found no later primary paper explicitly resolving H0008. This is bounded negative evidence, not a novelty certificate.

## 2. Previous finite-tilt theorem, recovered exactly

Work under the source finite-type front-decoupled Galton--Watson reduction. Let `D` be the finite type set, let

\[
M(\beta)_{ij}=B_{ij}p_{ij}^{\beta},\qquad p_{ij}\in(0,1]
\]

on the fixed strongly connected allowed type graph, and let the actual failed-child mean matrix be `M(1)`. Put

\[
x_{ij}=-\log p_{ij}\ge0,
\qquad
A(q)_{ij}=M(1)_{ij}e^{-q x_{ij}}=M(1+q)_{ij}.
\]

Define

\[
\psi(q)=\log\rho(A(q))=\phi(1+q),
\qquad
a(q)=-\psi'(q),
\qquad
F(q)=\psi(q)-q\psi'(q)=\psi(q)+q a(q).
\tag{2.1}
\]

The preceding report proved, under irreducibility/supercriticality, a uniform finite `(1+delta)` offspring moment, and the usual nondegeneracy needed for a nontrivial spectrum, that for every finite `q`:

\[
F(q)>0\implies \dim_H E(a(q))=F(q),
\tag{2.2}
\]

\[
F(q)=0\implies \dim_H E(a(q))=0,
\tag{2.3}
\]

and

\[
F(q)<0\implies E(a(q))=\varnothing.
\tag{2.4}
\]

It also proved the all-exponent first-moment upper bound

\[
\dim_HE(a)\le \inf_{q\in\mathbb R}\{\psi(q)+qa\}.
\tag{2.5}
\]

The only multifractal pieces left were possible `q=+infinity` and `q=-infinity` endpoints when the positive phase does not terminate at a finite tilt.

## 3. Method #8 — discretize zero temperature to two finite cycle-mean problems

The source finite-type potential is a finite weighted directed graph. The zero-temperature slopes are therefore not mysterious analytic limits: they are the extremal directed-cycle means of the edge displacement `x`.

Define

\[
a_{\rm cyc}^{-}
 :=\min_C\frac1{|C|}\sum_{e\in C}x_e,
\qquad
 a_{\rm cyc}^{+}
 :=\max_C\frac1{|C|}\sum_{e\in C}x_e,
\tag{3.1}
\]

where the minimum/maximum is over directed cycles in the allowed type graph. Because the graph is finite and strongly connected, both extrema are attained by simple directed cycles. They are finite combinatorial objects (equivalently, minimum/maximum mean-cycle values, computable by standard finite graph algorithms such as Karp's).

The key conclusion proved below is

\[
\boxed{
\lim_{q\to+\infty}a(q)=a_{\rm cyc}^{-},
\qquad
\lim_{q\to-\infty}a(q)=a_{\rm cyc}^{+}.
}
\tag{3.2}
\]

Thus the two possible missing exponent endpoints reduce to two finite weighted-graph optimization problems.

## 4. Method #12 — the conserved coboundary and the critical-edge matrices

### 4.1 Minimum side

Set `a_-=a_cyc^-`. Give each allowed edge `i->j` the reduced raw weight

\[
w_{ij}=x_{ij}-a_-.
\]

Every directed cycle has nonnegative total `w`-weight by definition of `a_-`. Hence the finite system of difference constraints

\[
h_j-h_i\le w_{ij}
\tag{4.1}
\]

is feasible. Concretely, fix a root type and take `h_j` to be the shortest-path distance to `j` in the graph with weights `w`; absence of negative cycles gives (4.1).

Define the **reduced cost**

\[
c^-_{ij}=x_{ij}-a_-+h_i-h_j\ge0.
\tag{4.2}
\]

For every type path `i_0,...,i_n`, the coboundary terms telescope:

\[
\sum_{k=0}^{n-1}x_{i_ki_{k+1}}
=na_- -h_{i_0}+h_{i_n}
 +\sum_{k=0}^{n-1}c^-_{i_ki_{k+1}}.
\tag{4.3}
\]

This is the conserved quantity the previous finite-tilt argument did not need. Since the finite vector `h` is bounded and every reduced cost is nonnegative, (4.3) already implies that no infinite path can have asymptotic exponent below `a_-`.

Let the **minimum critical-edge mean matrix** be

\[
C^-_{ij}=M(1)_{ij}\,\mathbf 1_{\{c^-_{ij}=0\}}.
\tag{4.4}
\]

At least one minimum-mean directed cycle has every edge tight after choosing a shortest-path potential, so `rho(C^-)>0`.

Now let `D(q)=diag(e^{q h_i})`. Similarity preserves spectral radius, and direct substitution gives

\[
e^{qa_-}D(q)^{-1}A(q)D(q)
=
\big(M(1)_{ij}e^{-q c^-_{ij}}\big)_{ij}.
\tag{4.5}
\]

As `q->+infinity`, the right side converges entrywise to `C^-`. Spectral-radius continuity in finite dimension yields

\[
\boxed{
\psi(q)+qa_-\longrightarrow \log\rho(C^-).
}
\tag{4.6}
\]

Because the set of positive reduced costs is finite, either every reduced cost is zero or there is a gap

\[
\delta_-:=\min\{c^-_{ij}:c^-_{ij}>0\}>0.
\]

Thus the matrix in (4.5) is `C^-+O(e^{-q\delta_-})` entrywise. Finite-dimensional Perron root asymptotics (or a finite cycle expansion of powers) imply exponential convergence up to a finite root exponent; in particular

\[
q\big(a(q)-a_-\big)\to0.
\tag{4.7}
\]

Combining (4.6) and (4.7),

\[
\boxed{
F(q)\longrightarrow \log\rho(C^-)
\quad(q\to+\infty).
}
\tag{4.8}
\]

Even without (4.7), (3.2) follows directly from convexity: `g(q)=psi(q)+qa_-` is convex, nonincreasing, and has the finite limit (4.6), so `g'(q)=psi'(q)+a_- ->0`, i.e. `a(q)->a_-`.

### 4.2 Maximum side

Apply the same construction to `-x`. Equivalently choose a finite potential `k` such that

\[
c^+_{ij}=a_+-x_{ij}+k_i-k_j\ge0,
\qquad a_+=a_{\rm cyc}^{+},
\tag{4.9}
\]

and define

\[
C^+_{ij}=M(1)_{ij}\,\mathbf 1_{\{c^+_{ij}=0\}}.
\tag{4.10}
\]

Then

\[
\boxed{
\psi(q)+qa_+\to\log\rho(C^+),
\quad a(q)\to a_+,
\quad F(q)\to\log\rho(C^+)
\quad(q\to-\infty).
}
\tag{4.11}
\]

The path identity dual to (4.3) rules out asymptotic exponents above `a_+`.

## 5. Method #17 — identify the residual entropy and transfer it back to the branching boundary

The quantities `log rho(C^-)` and `log rho(C^+)` are the finite-state **zero-temperature residual entropies/growth rates** of the extremal edge subshifts. This mechanism is classical in thermodynamic formalism for locally constant potentials on subshifts of finite type. Relevant literature includes Chazottes--Gambaudo--Ugalde on zero-temperature limits of locally constant potentials, Wolf--Yang on classification via zero-temperature measures, and Burr--Wolf on zero-temperature thermodynamic invariants. I make **no novelty claim** for the generic finite-state zero-temperature/coboundary mechanism.

What is source-specific here is the shifted failed-tree pressure `psi(q)=phi(1+q)`, and the transfer from the critical-edge subshift to the actual failed **multitype Galton--Watson boundary**.

### Lemma 5.1 (minimum endpoint dimension)

Assume the source finite-type failed process is in the non-singular supercritical regime covered by its Galton--Watson boundary theorem. If the positive free-energy phase extends to `q=+infinity`, then on survival of the full failed process

\[
\boxed{
\dim_H E(a_-)=\log\rho(C^-).
}
\tag{5.1}
\]

Here, if `rho(C^-)=1`, both sides are zero; if `rho(C^-)>1`, the endpoint level set contains a surviving critical-edge multitype subtree of that dimension.

#### Proof

The universal upper bound (2.5), evaluated along `q->+infinity` and using (4.6), gives

\[
\dim_HE(a_-)\le\log\rho(C^-).
\tag{5.2}
\]

If the positive phase extends to every finite positive `q`, then `F(q)>0` for all finite `q`. By (4.8), necessarily `rho(C^-)>=1`.

If `rho(C^-)=1`, (5.2) gives dimension at most zero, hence equality under the standard convention `dim_H emptyset=0`.

Suppose `rho(C^-)>1`. Choose a strongly connected component `H` of the zero-reduced-cost graph whose Perron root realizes `rho(C^-)`. Retain from the failed Galton--Watson process only children corresponding to zero-reduced-cost edges inside `H`. This is a finite-type Galton--Watson process with mean matrix the corresponding irreducible block of `C^-`, hence it is supercritical. Its inherited offspring moment satisfies the same source hypothesis.

Every ray of this restricted subtree has all `c^-` terms in (4.3) equal to zero, so

\[
\frac{S_n}{n}=a_-+\frac{-h_{i_0}+h_{i_n}}n\longrightarrow a_-.
\]

Therefore its boundary is contained in `E(a_-)`. The standard multitype Galton--Watson boundary-dimension theorem used by the source gives its dimension `log rho(C^-)` on restricted-subtree survival.

It remains only to pass from restricted-subtree survival with positive probability to the almost-sure statement conditional on survival of the full irreducible failed process. In the non-singular irreducible supercritical finite-type process, on survival the population visits every communicating type infinitely often and the total population is unbounded. Strong connectivity supplies, in a bounded number of generations, a positive-probability route from any type to a type of `H`; branching independence then gives infinitely many disjoint trials, each with a uniformly positive probability of starting a surviving `H`-restricted subtree. The conditional probability that all trials fail is zero. Hence on full survival some surviving restricted subtree occurs almost surely, proving the lower bound matching (5.2). `square`

### Lemma 5.2 (maximum endpoint dimension)

If the positive phase extends to `q=-infinity`, then, by the same argument with `C^+`,

\[
\boxed{
\dim_HE(a_+)=\log\rho(C^+)
}
\tag{5.3}
\]

on survival, with the same zero-dimensional convention at `rho(C^+)=1`.

## 6. The exact full exponent interval

Assume now the non-coboundary case, so `psi` is strictly convex on finite `q`. Equivalently, its asymptotic variance is positive; then `a(q)=-psi'(q)` is strictly decreasing and continuous. Recall

\[
F'(q)=-q\psi''(q).
\tag{6.1}
\]

Hence `F` decreases on `(0,infinity)` and increases as `q` moves toward zero on `(-infinity,0)`, while `F(0)=psi(0)=log rho(M(1))>0`.

Define the two phase edges

\[
q_R=\sup\{q\ge0:F(q)>0\}\in(0,+\infty],
\tag{6.2}
\]

\[
q_L=\inf\{q\le0:F(q)>0\}\in[-\infty,0).
\tag{6.3}
\]

Define the **smallest admissible exponent**

\[
a_{\rm lo}=
\begin{cases}
 a(q_R),&q_R<+\infty,\\
 a_{\rm cyc}^{-},&q_R=+\infty,
\end{cases}
\tag{6.4}
\]

and the **largest admissible exponent**

\[
a_{\rm hi}=
\begin{cases}
 a(q_L),&q_L>-\infty,\\
 a_{\rm cyc}^{+},&q_L=-\infty.
\end{cases}
\tag{6.5}
\]

### Theorem R14-H0008-04 (complete finite-type transmission multifractal spectrum)

Under the source finite-type front-decoupled Galton--Watson reduction, assume:

1. `M(1)` is irreducible and supercritical;
2. the allowed finite type graph is strongly connected and every allowed `p_ij` is positive;
3. failed offspring vectors have a uniform finite `(1+delta)` moment for some `delta>0`;
4. the process is non-singular in the standard multitype Galton--Watson sense (singular deterministic cases reduce directly to their unique path exponent);
5. the displacement cocycle `x_ij=-log p_ij` is not cohomologous to a constant when a nonzero exponent interval is desired.

Then, conditional on survival, the complete local transmission-exponent spectrum is supported on the closed interval

\[
\boxed{[a_{\rm lo},a_{\rm hi}].}
\tag{6.6}
\]

For every `a` in its interior there is a unique finite `q` with `a=a(q)` and

\[
\boxed{
\dim_HE(a)=\inf_{t\in\mathbb R}\{\psi(t)+ta\}
=\inf_{\beta\in\mathbb R}\{\phi(\beta)+(\beta-1)a\}.
}
\tag{6.7}
\]

At a finite-tilt phase edge the right side is zero by `F(q_edge)=0`, matching (2.3). At an infinite-tilt edge, Lemma 5.1 or 5.2 gives the zero-temperature value

\[
\dim_HE(a_{\rm lo})=\log\rho(C^-)
\quad(q_R=+\infty),
\tag{6.8}
\]

\[
\dim_HE(a_{\rm hi})=\log\rho(C^+)
\quad(q_L=-\infty).
\tag{6.9}
\]

No ray has an exponent outside `[a_lo,a_hi]`. Consequently this is the **largest closed interval** on which the source-normalized spectrum equality is valid, and the frozen metric has the exact value

\[
\boxed{I_{mf}=a_{\rm hi}-a_{\rm lo}.}
\tag{6.10}
\]

#### Proof

For an interior `a`, strict monotonicity of `a(q)` gives a unique finite `q` with `a=a(q)`. Since `a` lies strictly between the phase-edge slopes, that `q` lies in the positive phase and `F(q)>0`; the preceding finite-tilt theorem (2.2) gives (6.7).

Suppose `q_R<infinity`. Then continuity and monotonicity give `F(q_R)=0`, so the finite-tilt endpoint theorem gives dimension zero at `a_lo=a(q_R)`. For any `a<a_lo`, evaluate the Legendre upper bound at `q_R>0`:

\[
\psi(q_R)+q_Ra
=\underbrace{\psi(q_R)+q_Ra_{lo}}_{F(q_R)=0}
 +q_R(a-a_{lo})<0.
\]

The same Borel--Cantelli argument used in the preceding report therefore shows `E(a)=emptyset`.

If instead `q_R=+infinity`, (4.3) shows directly that no path can have limiting exponent below `a_cyc^-=a_lo`, while Lemma 5.1 gives the endpoint dimension and the finite-tilt theorem gives every interior exponent.

The left phase edge is symmetric. If `q_L>-infinity`, then `q_L<0`, `F(q_L)=0`, and for `a>a_hi=a(q_L)`,

\[
\psi(q_L)+q_La
=0+q_L(a-a_{hi})<0,
\]

so `E(a)=emptyset`. If `q_L=-infinity`, the maximum-side telescoping identity rules out exponents above `a_cyc^+=a_hi`, while Lemma 5.2 gives the endpoint dimension.

Thus no exponent outside `[a_lo,a_hi]` occurs, all interior exponents obey the pressure formula, and both endpoints obey it in the appropriate finite- or zero-temperature sense. This proves maximality and (6.10). `square`

### Degenerate coboundary case

If `x_ij=a_0+h_j-h_i` on every allowed edge, then (4.3) has zero reduced cost on every path and every ray has the single exponent `a_0`; `psi(q)=psi(0)-qa_0`. The multifractal interval collapses to length zero. This is the expected degenerate exception and is why the claim's nonzero-interval movement is stated only in the non-coboundary source slice.

## 7. What moved, exactly

Before this run, the frozen quantity had only a proved lower bound:

\[
I_{mf}\ge \phi'(1+\eta)-\phi'(1-\eta)>0
\]

for some local `eta>0`.

The previous finite-tilt theorem proved much more pointwise but did **not** certify the maximal closed interval because its two possible zero-temperature endpoints were unresolved.

This run proves the endpoint slopes, endpoint dimensions, and emptiness outside the phase interval. Therefore the same frozen quantity is now known **exactly**:

\[
\boxed{I_{mf}=a_{hi}-a_{lo},}
\]

with `a_lo,a_hi` given by (6.4)--(6.5) and the infinite-tilt alternatives given by the finite cycle means (3.1). This is a certification improvement on the original metric, not a numerical estimate and not a changed denominator.

The source-level status is nevertheless **PARTIAL**, not PROVED, for two reasons:

1. the theorem is conditional on the source's finite-type branching reduction and the explicit moment/nondegeneracy hypotheses above; it is unconditional only where the source has already established that reduction (in particular its dissipative regime);
2. Open problem (6) also asks for the **harmonic measure of the cluster itself** and its expected dimension drop. That second clause remains open in the general multitype source model.

Thus this run closes the finite-type **multifractal-spectrum clause** under the source reduction, but does not close H0008 as a whole and does not trigger paper/audit closure protocol.

## 8. Prior art and novelty boundary

The following mechanisms are classical and are **not** claimed as new:

- Perron pressure for a finite locally constant potential;
- extremal cycle averages / ergodic optimization on a finite subshift;
- zero-temperature Gibbs states and residual entropy for locally constant potentials;
- multitype Galton--Watson boundary dimension;
- multitype branching-random-walk additive martingales and spine changes of measure used in the previous report.

Relevant literature checked this run includes:

- J.-R. Chazottes, J.-M. Gambaudo, E. Ugalde, *Zero-temperature limit of one-dimensional Gibbs states via renormalization: the case of locally constant potentials*, ETDS 2011;
- Christian Wolf, Yun Yang, *A topological classification of locally constant potentials via zero-temperature measures*, Trans. AMS 2019;
- Michael Burr, Christian Wolf, *Computability at zero temperature*, Nonlinearity 2020 / arXiv:1809.00147;
- the multitype branching-random-walk/martingale references already recorded in the previous H0008 reports.

The source-specific contribution claimed here is only the **application and exact normalization**: the failed genealogy shifts the source pressure by one, `psi(q)=phi(1+q)`, and the two zero-temperature residual-entropy matrices `C^-`,`C^+` supply the missing endpoint dimensions for the source finite-type transmission spectrum. A bounded negative search is not a novelty certificate.

## 9. No checker-only artifact

No new finite enumeration claim was introduced. The mean-cycle/coboundary statements are theorem-sized and proved on the page for an arbitrary finite weighted type graph; the source parameters need not be rational. In accordance with the 90/10 rule, I did not manufacture a checker merely to certify unchanged arithmetic.

## 10. Next research direction and fresh methods

The multifractal clause has reached its natural finite-type endpoint. The only source clause still materially open on this assignment is the multitype **harmonic-measure dimension drop**. The previous harmonic run already certified that the entire pressure curve is insufficient: conductance-normalized sibling weights depend on the full offspring/conductance law.

If H0008 continues, the next nonrepeating methods should be **#3 PROVE SOMETHING STRONGER, #14 FIND THE GROUP ACTING, #28 REPLACE FOR ALL WITH FOR TYPICAL**. A metric-worthy target would be an invariant environment law for the type/conductance state seen from the harmonic ray, yielding an entropy-rate formula and a strict Jensen/dimension-drop criterion in the genuinely multitype source model. Another finite-tilt pressure lemma would not count as progress.

Because this run moves the frozen multifractal metric certification, the H0008 unchanged-run streak resets to zero for the purpose of the Section-I stuck rule.

## 11. Runtime/model-control honesty

The prompt requests GPT-6 at maximum reasoning. That is **not** the runtime I can verify. The actual model exposed to this invocation is GPT-5.6 Sol; authenticated reasoning-effort telemetry is not exposed, so the reasoning level is UNVERIFIED.

The task-control surface available here exposes title/prompt, schedule/relative-start, timing mode, enabled state, and notification behavior. It still exposes **no binding model-family selector, no reasoning-effort selector, no guaranteed-duration control, and no authenticated completed-run model telemetry**. Therefore `GPT-6 / maximum` remains prompt text rather than an enforceable scheduler setting. Making it binding would require an owner/admin-authorized product, workspace, API, or scheduler surface that actually exposes model and reasoning fields and run attestation.

Repository history records an older P26-context response `You cannot modify this task` and a later successful P26 update from a different authorized context. That is an authorization/context boundary, not permission to duplicate a task or bypass controls. The lawful workaround is the owning/admin-authorized task surface or platform support. No scheduler or permission state was changed in this run.

## 12. Structured ledger_delta

```yaml
ledger_delta:
  worker: R14
  category: HARD_OUTSIDE
  source_id: H0008
  source: "Achyut Kumar, arXiv:2608.15987v1, Section 12.3 Open problem (6), Boundary fluctuations"
  ownership: "exclusive R14 claim preserved"
  source_status: PARTIAL_OPEN
  clause_progress:
    multifractal_finite_type_under_reduction: "COMPLETE in this report, including zero-temperature endpoints"
    harmonic_measure_general_multitype: OPEN
  fixed_metric: I_mf
  before: ">= phi'(1+eta)-phi'(1-eta)>0 for some proved local eta; exact maximal interval unknown"
  after: "= a_hi-a_lo exactly, with finite phase edges or extremal cycle-mean zero-temperature edges"
  movement: "lower-bound-only certification -> exact fixed-metric value"
  methods_used: [8, 12, 17]
  preceding_triple: [6, 18, 23]
  unchanged_streak_after: 0
  theorem: R14-H0008-04
  exact_finite_checker: "not applicable; theorem-sized arbitrary-real finite graph argument is on page"
  prior_art_status: "generic zero-temperature/cycle/coboundary and BRW machinery classical; no novelty claim"
  next_methods: [3, 14, 28]
  closure: false
  closure_reason: "harmonic-measure clause remains open; source reduction is conditional outside regimes already proved by source"
  shared_root_edits: false
  email_drive_public_post_scheduler_permission_workflow_changes: false
```
