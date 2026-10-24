Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. NO SOURCE-METRIC MOVEMENT: G0004 `U_F: 1 -> 1`; STUCK RECOVERY 2/2 EXECUTED SUCCESSFULLY on the selected `K_{3,n}` target, in fact on a larger bipartite class; post-recovery-2 substantive unchanged count `0 -> 1`; methods #6 DEFORM TO A POINT YOU CAN SOLVE / #8 GO THE OTHER WAY AND DISCRETIZE / #29 ADD THE POINTS AT INFINITY.**

# R17 C077 — G0004 recovery 2/2: full Flammant quantifiers on `K_{3,n}` and a larger bipartite class

Repository / branch: private `yspennstate/math-open-problems` / `master`.  
Worker: R17, HARD OUTSIDE.  
Status: **OPEN / PARTIAL. Recovery 2/2 produced a source-valid nonplanar theorem, but the fixed source-wide metric is unchanged.**

## 0. Continuity, ownership, required reading, and current-source check

The canonical claim `operations/claims/G0004.md` still names **R17** as exclusive owner of Lucas Flammant's finite-graph percolation Conjecture 2.2. The original Chvátal--Sankoff binary-LCS target remains terminally handed off at

\[
0.792665992\le \gamma_2\le0.826275942762282626,
\qquad U-L=0.033609950762282626,
\]

and the later Rhodes--Vargas `D0064` target remains terminal at `R_class=0/3`. Neither predecessor is reopened.

At run start I reread or rechecked the required current surfaces:

- `probability_campaign_2026_09/INDEX.md` and `RANKING.md`;
- root `POSTED.md`, `RESULTS.md`, and `QUEUE.md`;
- `operations/NEW_METHODS_2026-09-16.md` and `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md`;
- canonical claim `operations/claims/G0004.md`;
- newest own report C076 and the preceding G0004 reports C069--C075;
- repository search for canonical intake identity `flammant_finite_graph_2026::conjecture_2.2`, including `probability_1000_intake_G_20260910/problems.jsonl` and neighboring admission screens.

No root exclusion or newer claim supersedes R17 ownership.

Fresh primary-source search on 2026-09-19 again found Lucas Flammant, arXiv:2609.03492, as the current source. The public abstract still says that the unrestricted arbitrary-finite-graph statement is a conjecture and that the proved case is the outer-face planar case with explicit success lower bound `1-2 sqrt(epsilon)`. Searches by exact title/arXiv id together with `K_{3,n}` / bipartite terminology found no later source-matching solution. This is bounded negative evidence, not a worldwide novelty certificate.

The fixed source-wide metric remains

\[
U_F:=\inf\Bigl\{u:\limsup_{\varepsilon\downarrow0}R_*(\varepsilon)\le u
\text{ is rigorously certified under all source quantifiers}\Bigr\}.
\]

Before: `U_F=1`. After: `U_F=1`.

C076 selected recovery 2/2: prove the full source event/kernel statement on `K_{3,n}`, uniformly in `n,p`. This run executes that recovery. The selected family is settled positively, and the same proof gives a larger class, but because the result is restricted it does not move `U_F`. This is the first substantive unchanged run after recovery 2/2. Two further unchanged substantive runs would trigger the third stuck episode, at which point HARD policy requires a handoff and rotation rather than a third recovery.

## 1. Source-normalized failure functional

Let `G` be a finite graph with iid Bernoulli bond percolation of parameter `p`, origin `o`, boundary `B`, and source events `(E_b)_{b\in B}`. Write

\[
q_b(\omega):=1-\Pr(E_b\mid \pi=\omega).
\]

The source hypotheses imply that every `q_b` is decreasing and

\[
\mathbb E q_b\le \varepsilon.
\]

Let

\[
C_b:=\{o\leftrightarrow b\},\qquad
C:=\bigcup_{b\in B}C_b,
\qquad
S(\omega):=\{b\in B:C_b(\omega)\},
\qquad N:=|S|.
\]

On `C`, define

\[
m(\omega):=\min_{b\in S(\omega)}q_b(\omega).
\]

Conditionally on the percolation configuration, the probability that **all** connected boundary labels fail is at most `m`, regardless of dependence among the auxiliary events. Hence it is enough to bound

\[
R:=\frac{\mathbb E[m;C]}{\Pr(C)}.
\tag{1.1}
\]

This is the same source-valid reduction already recovered in the canonical G0004 history; I use it rather than rederive the older exact variational formulation.

## 2. A general contact-moment inequality

The `k=1` member of C074's factorial Harris hierarchy has an especially useful form here.

For every connected label `b` we have `m\le q_b`, so pointwise

\[
Nm=\sum_{b\in B}{\bf1}_{C_b}m
\le
\sum_{b\in B}{\bf1}_{C_b}q_b.
\]

Each `C_b` is increasing and each `q_b` is decreasing. Harris--FKG therefore gives

\[
\mathbb E[{f1}_{C_b}q_b]
\le
\Pr(C_b)\,\mathbb E q_b
\le
\varepsilon\Pr(C_b).
\]

Summing,

\[
\boxed{\mathbb E[Nm]\le \varepsilon\,\mathbb EN.}
\tag{2.1}
\]

Let

\[
M:=\mathbb E[N\mid C].
\]

For every `a>0`, splitting according to `N\le aM` and using (2.1) on the complement yields

\[
\boxed{
R\le
\Pr(N\le aM\mid C)+\frac{\varepsilon}{a}.
}
\tag{2.2}
\]

Indeed, on `N>aM`, `m\le Nm/(aM)`, and `\mathbb EN=M\Pr(C)`.

Thus the recovery problem reduces to a lower-tail estimate for the number of connected boundary vertices.

## 3. Method #6 — DEFORM TO A POINT YOU CAN SOLVE

The C076 plan proposed tracking the full eight column types of `K_{3,n}`. The useful deformation is simpler: retain only the **direct origin-to-boundary row** and treat every other open edge as possible extra mass.

This reveals a larger solvable class.

Let

\[
G=(L\sqcup B,E)
\]

be any finite **simple bipartite graph**, take the boundary to be the entire `B` side, and take `o\in L` with degree

\[
d:=\deg(o)\ge1.
\]

Set

\[
\rho:=\frac{|E|}{d}\ge1.
\tag{3.1}
\]

Because every path from `o` begins with an edge from `o` directly into the boundary side `B`,

\[
C=\{o\leftrightarrow B\}
\quad\Longleftrightarrow\quad
D>0,
\]

where `D` is the number of open edges incident to `o`. Thus

\[
D\sim\operatorname{Bin}(d,p).
\tag{3.2}
\]

Let `T` be the total number of open edges of `G`. Every connected boundary vertex is incident to at least one open edge, and different boundary vertices require distinct incident edges, so

\[
N\le T.
\tag{3.3}
\]

Write

\[
\lambda:=dp,
\qquad
s:=\Pr(D>0)=1-(1-p)^d,
\qquad
\mu:=\mathbb E[D\mid D>0]=\frac{\lambda}{s}.
\tag{3.4}
\]

The event `C={D>0}` depends only on the `d` origin edges. All other edges remain independent Bernoulli(`p`) after conditioning on `C`. Therefore

\[
\mathbb E[T\mid C]
=
\mu+p(|E|-d)
=
\mu+(\rho-1)\lambda
\le
\rho\mu,
\tag{3.5}
\]

because `\lambda=s\mu\le\mu`. Combining (3.3)--(3.5),

\[
\boxed{M\le \rho\mu.}
\tag{3.6}
\]

For `K_{r,n}` with `o` on the side of size `r` and `B` the side of size `n`, one has `d=n`, `|E|=rn`, hence simply

\[
\rho=r.
\tag{3.7}
\]

So the selected `K_{3,n}` recovery has `\rho=3`.

## 4. Method #8 — DISCRETIZE: an exact one-dimensional binomial lemma

No eight-state transfer matrix is needed. The direct-edge count `D` is the correct finite statistic.

Define the universal constant

\[
c_0:=1-e^{-1}.
\]

### Lemma 4.1 (uniform conditional lower tail)

Let `D\sim Bin(d,p)`, with `\lambda=dp`, `s=\Pr(D>0)`, and `\mu=\lambda/s`. For every

\[
0<t\le \frac{c_0}{2},
\]

one has

\[
\boxed{
\Pr(D\le t\mu\mid D>0)
\le
\frac1{c_0}\exp\!\left(-\frac{c_0}{8t}\right).
}
\tag{4.1}
\]

#### Proof

We split into three exhaustive regimes.

**Regime A: `0<\lambda<1`.** Using

\[
(1-p)^d\le \frac1{1+dp}=\frac1{1+\lambda},
\]

we get

\[
s\ge\frac{\lambda}{1+\lambda},
\qquad
\mu=\frac\lambda s\le1+\lambda<2.
\]

Hence `t\mu<2t\le c_0<1`. On `D>0` one has `D\ge1`, so the event in (4.1) is empty.

**Regime B: `1\le\lambda<c_0/t`.** Since

\[
s=1-(1-p)^d\ge1-e^{-\lambda}\ge c_0,
\]

we have `\mu\le\lambda/c_0`, and therefore

\[
t\mu<\frac{t\lambda}{c_0}<1.
\]

Again the event is empty on `D>0`.

**Regime C: `\lambda\ge c_0/t`.** We still have `s\ge c_0`, so

\[
t\mu\le \frac{t\lambda}{c_0}\le\frac\lambda2,
\]

where the last inequality uses `t\le c_0/2`. The standard multiplicative Chernoff bound for a binomial variable gives

\[
\Pr(D\le\lambda/2)\le e^{-\lambda/8}.
\]

Conditioning on `D>0` and using `s\ge c_0` and `\lambda\ge c_0/t`,

\[
\Pr(D\le t\mu\mid D>0)
\le
\frac{e^{-\lambda/8}}{c_0}
\le
\frac1{c_0}\exp\!\left(-\frac{c_0}{8t}\right).
\]

This proves (4.1). `\square`

The inequality `(1-p)^d\le(1+dp)^{-1}` used in Regime A follows from

\[
(1-p)^{-d}\ge 1+\frac{dp}{1-p}\ge1+dp.
\]

Thus no asymptotic approximation is hidden in the lemma.

## 5. Main recovery theorem

### Theorem 5.1 (full Flammant event quantifiers on a bipartite boundary-side class)

Let `G=(L\sqcup B,E)` be a finite simple bipartite graph, let the Flammant boundary be the entire `B` side, let `o\in L` have degree `d\ge1`, and let

\[
\rho=|E|/d.
\]

For iid Bernoulli bond percolation of arbitrary parameter `p`, and for **arbitrary source-admissible event families `(E_b)_{b\in B}`** with increasing conditional success probabilities and `\Pr(E_b)\ge1-\varepsilon`, define `R` by (1.1). Then, for

\[
0<\varepsilon\le e^{-1},
\]

\[
\boxed{
R
\le
\frac{\varepsilon}{c_0}
\left(
1+8\rho\log\frac1\varepsilon
\right),
\qquad c_0=1-e^{-1}.
}
\tag{5.1}
\]

Consequently the source conclusion holds uniformly on every family satisfying

\[
\rho(\varepsilon)\,\varepsilon\log(1/\varepsilon)\to0.
\tag{5.2}
\]

In particular, for every fixed `r`, the entire family `K_{r,n}` obeys the full source event/kernel statement uniformly in `n` and `p`, with

\[
\boxed{
R_{K_{r,n}}(\varepsilon)
\le
\frac{\varepsilon}{1-e^{-1}}
\left(1+8r\log\frac1\varepsilon\right).
}
\tag{5.3}
\]

For the recovery target `K_{3,n}` this becomes

\[
\boxed{
R_{K_{3,n}}(\varepsilon)
\le
\frac{\varepsilon}{1-e^{-1}}
\left(1+24\log\frac1\varepsilon\right)
\longrightarrow0.
}
\tag{5.4}
\]

#### Proof

From (3.6), `M\le\rho\mu`. Therefore, for every `a>0`,

\[
\{N\le aM\}\cap C
\subseteq
\{D\le a\rho\mu\}\cap\{D>0\},
\]

because `D\le N` whenever `D>0` (each open origin edge lands at a distinct connected boundary vertex).

Apply Lemma 4.1 with

\[
t=a\rho.
\]

As long as `a\rho\le c_0/2`, (2.2) gives

\[
R
\le
\frac1{c_0}\exp\!\left(-\frac{c_0}{8a\rho}\right)
+\frac\varepsilon a.
\tag{5.5}
\]

Let

\[
L:=\log(1/\varepsilon)\ge1,
\qquad
 a:=\frac{c_0}{8\rho L}.
\]

Then `a\rho=c_0/(8L)\le c_0/2`, and

\[
\exp\!\left(-\frac{c_0}{8a\rho}\right)=e^{-L}=\varepsilon.
\]

Substituting in (5.5) gives exactly (5.1). Equation (5.3) follows from `\rho=r` for `K_{r,n}`, and (5.4) is `r=3`. `\square`

### Scope check

This theorem uses the **full original source quantifiers on the auxiliary events**. It does **not** assume cluster measurability, independence between the `E_b`, symmetry of the kernels, bounded boundary size, or a special form of the decreasing failure kernels. The restriction is solely on the graph/boundary geometry: bipartite, boundary equal to one color class, with the quantitative parameter `\rho=|E|/deg(o)`.

This is therefore a genuine nonplanar source-valid theorem. It is still only **PARTIAL** relative to arbitrary finite graphs.

## 6. Method #29 — ADD THE POINTS AT INFINITY

The point of Lemma 4.1 is that it closes every scaling boundary that the C076 `np^2` plan would otherwise have had to analyze separately.

The single parameter

\[
\lambda=dp
\]

covers:

1. `\lambda<1`: conditioned on connection, the direct-contact count has conditional mean below `2`, so a sufficiently small fractional lower-tail threshold is literally impossible;
2. `1\le\lambda<c_0/t`: the conditional mean is at most `\lambda/c_0`, and the threshold is still below one;
3. `\lambda\ge c_0/t`: the ordinary binomial Chernoff lower tail is exponentially small.

Thus `p\downarrow0`, `d\to\infty`, finite-`\lambda`, and dense regimes are all handled without a missing boundary case. In particular, the earlier finite-core parameter `np^2` is unnecessary for this recovery theorem: direct contact from the origin plus the total-open-edge domination already gives a stronger route.

## 7. What this teaches about the full conjecture

The theorem isolates a new quantitative obstruction parameter:

\[
\rho=\frac{|E|}{\deg(o)}.
\]

When the origin sees a non-negligible fraction of all graph edges, adaptive boundary-label failure is harmless up to an explicit `\rho\varepsilon\log(1/\varepsilon)` cost. Therefore any counterexample sequence built within this bipartite geometry must force

\[
\rho\gtrsim\frac1{\varepsilon\log(1/\varepsilon)}.
\]

This is consistent with the previous lesson that multiplicity/fanout, not merely nonplanarity, is the central difficulty. The remaining unrestricted problem is precisely the regime where a small origin interface controls a graph with much larger total edge mass and where later shared-component mergers can expose many new boundary labels.

This observation does **not** prove a lower bound on `R_*` and does not move the source-wide metric.

## 8. Why no checker was manufactured

The new claim is theorem-sized and has a complete symbolic proof above. Its only numerical constant is `c_0=1-e^{-1}`, and there is no finite enumeration or computer-dependent core. Under the 90/10 policy, creating a small-case checker here would only certify examples of a proof that is already exact; I therefore did not spend the run manufacturing a checker-only artifact.

If this restricted theorem later becomes part of a paper package, an independent audit or formalization can check the three deterministic inequalities `(2.1)`, `(3.6)`, and Lemma 4.1. Such a future check would be validation, not today's research contribution.

## 9. Prior-art note

The fresh 2026-09-19 bounded search used the exact Flammant title/arXiv id, `Conjecture 2.2`, and combinations with `K_{3,n}`, `complete bipartite`, `bipartite`, and `boundary`. I found the current Flammant preprint and no later primary item claiming either the unrestricted conjecture or the bipartite theorem above. The source abstract itself advertises only the outer-face planar theorem with `1-2 sqrt(epsilon)`.

This negative search is not a novelty certificate. The ingredients Harris--FKG and binomial Chernoff bounds are standard/folklore tools; the claim here is the source-specific combination and scope reduction, not novelty of those inequalities.

## 10. Next route and HARD lifecycle

Recovery 2/2 has now been **executed**, not merely selected. It succeeded on `K_{3,n}` and the larger class above, but strict metric `U_F` remains `1`. Under the fixed-metric rule this begins a new post-recovery-2 unchanged streak at `1`.

The next substantive G0004 run, if no source closure or literature resolution intervenes, must use a fresh triple:

- **#9 RANDOMIZE:** search for a randomized exploration/ownership rule whose expected multiplicity is controlled by an interface quantity smaller than `|E|/deg(o)`;
- **#23 DO WHAT THE PROPOSER DID NOT EXPECT:** assume the conjecture is false and deliberately amplify the high-`\rho` regime by attaching a huge hidden edge reservoir behind a tiny origin cut, while enforcing the decreasing-kernel budgets exactly;
- **#26 HUNT THE SPORADIC CASE:** identify the smallest non-bipartite/shared-core graph where the bound through `\rho` is useless and solve its exact failure LP symbolically before generalizing.

If two more substantive runs leave `U_F` unchanged, that is the **third stuck episode** after the two allowed recoveries, and R17 must write the handoff and rotate to a newly admitted outside target. There will be no third G0004 recovery.

## 11. Model / scheduler control status

The exposed scheduler surface still provides title, prompt, schedule / relative start, timing mode, enablement, and list/update controls. It exposes **no bindable model-family selector, no reasoning-effort selector, and no authenticated runtime-model telemetry**. Therefore the requested `GPT-6 / maximum` setting remains prompt text only and cannot be honestly asserted as runtime configuration from this surface.

Changing that requires an authorized product/API/admin scheduler surface that actually exposes model and reasoning fields together with execution telemetry. The historical P26 `"You cannot modify this task"` failure is documented in the owner policy as an authorization-context issue; root `RESULTS.md` also records that P26 later accepted its full update from another authorized context. The legitimate workaround is therefore the owning/admin-authorized scheduler context or platform support, not a duplicate task, repository edit, or permission bypass.

No scheduler change was attempted in this run.

## 12. Structured ledger delta

```yaml
ledger_delta:
  track: R17
  lane: HARD_OUTSIDE
  canonical_target: G0004
  source: "Lucas Flammant, arXiv:2609.03492, Conjecture 2.2"
  status: PARTIAL
  fixed_metric:
    name: U_F
    before: 1
    after: 1
    movement: false
  hard_lifecycle:
    recovery_selected_before_run: "2/2"
    recovery_executed_this_run: "2/2"
    post_recovery_2_substantive_unchanged_count_before: 0
    post_recovery_2_substantive_unchanged_count_after: 1
    third_stuck_handoff_due_after_additional_unchanged_substantive_runs: 2
  new_result:
    theorem: "Full source event/kernel quantifiers hold on finite bipartite graphs when the boundary is one color class, with R <= eps/(1-e^-1) * (1 + 8 rho log(1/eps)), rho=|E|/deg(o)."
    selected_recovery_corollary: "For K_{3,n}, R <= eps/(1-e^-1) * (1 + 24 log(1/eps)) -> 0 uniformly in n,p."
    broader_corollary: "For K_{r,n}, fixed r, R = O(r eps log(1/eps)) uniformly in n,p."
    source_scope: "restricted graph class; auxiliary-event quantifiers unchanged"
  methods_this_run: [6, 8, 29]
  next_methods_reserved: [9, 23, 26]
  predecessor_targets:
    binary_lcs: "terminal; width 0.033609950762282626; not reopened"
    D0064: "terminal; R_class=0/3; not reopened"
  source_current_check: "2026-09-19 bounded search; current public source still states unrestricted conjecture; no later source-matching solution found"
  artifacts_created: []
  shared_roots_modified: false
  peer_files_modified: false
  scheduler_modified: false
  email_or_drive: false
```

No shared root, peer file, canonical claim, scheduler, workflow, email, Drive item, permission, purchase, or public posting was modified.
