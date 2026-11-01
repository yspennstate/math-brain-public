Model actually ran: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. NO METRIC MOVEMENT: `W_CHT: 1/2 -> 1/2`; frozen I0056/H_{5,5} width remains `0 -> 0`; successor unchanged count `1 -> 2`; methods #1 CHANGE THE CATEGORY, #19 MAKE IT AN ALGORITHM, #27 SWAP THE QUANTIFIERS.**

# R06 — Nielsen Theorem 4: operator form and a finite-depth/retraction no-go theorem

Date: 2026-09-18 UTC  
Worker: R06  
Lane: CLOSABLE OUTSIDE  
Repository / branch: private `yspennstate/math-open-problems` / `master`

## 1. Continuity and scope

I continued from

`runs/R06/20260918T1720Z_nielsen_t4_convexification_nogo_46.md`

and the exclusive create-only claim

`operations/claims/KPS-2026-NIELSEN-THEOREM4.md`.

The historical native-title source, Russell Lyons and Yuval Peres, *Probability on Trees and Networks*, Question 6.20 / intake I0056, remains frozen and is not reopened. Its exact source question is:

> What is `Phi_V(G)` for regular co-regular plane graphs `G`? What are `Phi_E(G)` and `Phi_V(G)` for more general transitive plane graphs `G`?

For the frozen outer-vertex normalization on the `{5,5}` tessellation,

\[
\Phi_V(H_{5,5})=\sqrt5,\qquad [L,U]=[\sqrt5,\sqrt5],\qquad U-L=0.
\]

The `{5,5}` subtarget is PROVED / audit-complete; the full two-clause source question remains PARTIAL. Haslegrave--Panagiotis face degrees 3 and 4 remain excluded prior art. The I0056 attacking lifecycle remains rotated.

The active R06 successor is the question left open by M. Ali Khan, Arthur Paul Pedersen and Maxwell B. Stinchcombe, *Almost-Uniform Bayesian Convergence to the Truth Is Not Characterized by Countable Additivity on Conditional Hitting Times*, arXiv:2609.20683v1, submitted 2026-09-17, Section 10. Under Nielsen's Assumption 1, the target is the standalone truth of Nielsen's Theorem 4:

> There are uncountably many probability functions on the Borel subsets of Cantor space that have the CHT property but not the approximation property.

This is distinct from R01's `KPS-2026-NIELSEN-COR1` claim.

Before new mathematics I reread the campaign `probability_campaign_2026_09/INDEX.md` and `RANKING.md`, root `POSTED.md`, root `RESULTS.md`, root `QUEUE.md`, the operative `operations/FOLLOWUP_IMPLEMENTATION_2026-09-16.md`, the current Theorem-4 claim, the newest R06 report, and the newest neighboring R01/KPS report. Current ownership still records the Theorem-4 target as exclusively R06-owned.

## 2. Dated primary-literature check

Check date: **2026-09-18**.

Direct arXiv currently shows only `v1`, submitted 2026-09-17 16:52:41 UTC. The KPS introduction says Nielsen Theorem 4's proof uses the failed extension construction and that they do **not** decide the theorem's standalone truth; Section 7.1 repeats that Theorem 4 remains open. Their Section 6 verifies CHT for the one-ultrafilter construction, and Section 7.2 gives the almost-uniformly convergent replacement for Nielsen Theorem 3.

Bounded exact-title, exact-arXiv-ID, `Nielsen Theorem 4`, `CHT`, `approximation property`, and `finite additivity` searches found no later primary source resolving the standalone Theorem-4 question. The source is roughly one day old, so this is only dated negative search evidence, not a novelty certificate.

A side literature check on the algebraic route below recovered Sikorski's extension theorem: homomorphisms into a **complete** Boolean algebra extend from subalgebras. This does not give the retraction into the clopen algebra required by the tempting construction below, because the clopen algebra of Cantor space is not complete. No novelty claim is made for that standard fact.

## 3. Frozen metric

For source-admissible `P`, retain

\[
D(P)=\sup_{A\in\mathcal B}\inf_{C\in\mathcal C}P(A\triangle C),
\qquad
\Delta_{\rm CHT}=\sup\{D(P):P\text{ satisfies Assumption 1 and CHT}\}.
\]

The rigorously certified interval remains

\[
0\le\Delta_{\rm CHT}\le\frac12,
\]

so

\[
W_{\rm CHT}=\frac12.
\]

The preceding report had unchanged count 1. Nothing below produces a CHT/non-approximation witness or a universal improvement of the upper bound, so the count becomes **2**.

## 4. Idea before proof

The preceding run killed convex mixtures inside the KPS one-limit-point architecture. I therefore changed category completely.

Instead of trying to guess a finitely additive measure directly, encode it by the family of its **finite-information conditional densities** with respect to its countably additive clopen companion. This makes the source question an operator problem.

The first apparently powerful construction in that language would force every density to stabilize at some finite information level. Then every conditional-hitting open would be clopen, so CHT would become automatic; a single fractional stabilized density would immediately violate approximation. If such a construction existed, Nielsen Theorem 4 would be solved in one stroke.

The central result of this run is that this whole finite-depth route is impossible. The obstruction is topological and exact: a two-sided boundary point of an open set forces its density to approach both 0 and 1. Equivalently, there is no Boolean-algebra retraction from the Borel algebra of Cantor space onto its clopen algebra fixing clopens.

This is a useful no-go because it removes a broad class of abstract Hahn--Banach / Boolean-extension constructions before any code or ultrafilter bookkeeping is attempted.

## 5. Method #1 — CHANGE THE CATEGORY: the companion-density operator

Let

\[
\Omega=\{0,1\}^{\mathbb N},
\]

`C` be the clopen algebra and `B` the Borel sigma-algebra. Let `P` be any finitely additive probability on `B` satisfying Assumption 1.

### Proposition 5.1 — canonical countably additive companion and densities

There is a unique countably additive Borel probability `R` such that

\[
R(C)=P(C)\qquad(C\in\mathcal C).
\tag{5.1}
\]

For every Borel event `A` there is a unique `R`-a.e. function

\[
f_A:\Omega\to[0,1]
\]

such that for every clopen `C`,

\[
P(A\cap C)=\int_C f_A\,dR.
\tag{5.2}
\]

Moreover

\[
P_n(A)=E_R[f_A\mid\mathscr F_n]
\tag{5.3}
\]

pointwise on each length-`n` cylinder, and

\[
\inf_{C\in\mathcal C}P(A\triangle C)
=\int \min(f_A,1-f_A)\,dR.
\tag{5.4}
\]

#### Proof

On the clopen algebra, finite additivity is automatically a premeasure. Indeed, if pairwise disjoint clopens `C_j` have clopen union `C`, then the `C_j` form an open cover of the compact set `C`; compactness gives a finite subcover, and disjointness forces all but finitely many `C_j` to be empty. Hence Caratheodory extends `P|_C` uniquely to a countably additive Borel probability `R`.

Fix `A`. The clopen set function

\[
\nu_A(C)=P(A\cap C)
\]

is again a finite premeasure and satisfies `0 <= nu_A(C) <= R(C)`. It therefore extends uniquely to a countably additive Borel measure, still denoted `nu_A`, with `nu_A <= R`. Radon--Nikodym gives `f_A=d nu_A/dR` and `0<=f_A<=1`, proving (5.2).

On a length-`n` cylinder `B`,

\[
P_n(A)|_B=\frac{P(A\cap B)}{P(B)}
=\frac{\int_B f_A\,dR}{R(B)},
\]

which is exactly the conditional expectation of `f_A` on the finite partition `F_n`. This is (5.3).

Finally, for clopen `C`,

\[
P(A\triangle C)
=P(A)+P(C)-2P(A\cap C)
=\int\bigl[f_A+\mathbf1_C-2f_A\mathbf1_C\bigr]dR.
\]

Thus

\[
P(A\triangle C)
=\int_C(1-f_A)dR+\int_{C^c}f_A dR.
\]

Pointwise the optimal decision is `C={f_A>1/2}`. Regularity of `R` on compact metric Cantor space and density of clopens in `R`-measure let clopens approximate that Borel threshold set, giving the infimum (5.4). QED.

### Operator form

Equation (5.2) turns the set map

\[
A\mapsto f_A
\]

into the indicator-level part of a positive unital linear operator on bounded Borel functions. It obeys the exact finite-information module rule

\[
f_{A\cap C}=\mathbf1_C f_A
\qquad(C\in\mathcal C),
\tag{5.5}
\]

and `f_C=1_C` for clopen `C`.

For `A,delta`, let

\[
M_n^A=E_R[f_A\mid\mathscr F_n],
\qquad
O(A,\delta)=\bigcup_n\{M_n^A>\delta\}.
\tag{5.6}
\]

Every finite partial union is clopen. Therefore

\[
\lim_NP(O_N(A,\delta))=R(O(A,\delta)).
\]

Consequently **CHT is exactly the balance condition**

\[
\boxed{P(O(A,\delta))=R(O(A,\delta))
\quad\text{for all }A\in\mathcal B,\ \delta\in(0,1).}
\tag{5.7}
\]

Together, (5.4) and (5.7) recast Nielsen Theorem 4 as follows:

> Find a source-positive finitely additive probability whose companion-density operator has at least one genuinely fractional output `f_A`, while every self-generated threshold-open (5.6) satisfies the balance identity (5.7).

This formulation contains the previous one-limit-point analysis but no longer assumes any ultrafilter geometry.

## 6. Method #19 — MAKE IT AN ALGORITHM: the finite-depth strategy would solve the source, but cannot exist

The simplest algorithmic target suggested by (5.6) is:

> for every Borel `A`, arrange that `f_A` is measurable with respect to some finite `F_m` depending on `A`.

Call this **eventwise finite-depth stabilization**.

### Proposition 6.1 — finite-depth stabilization would make CHT automatic

If a source-admissible `P` had eventwise finite-depth stabilization, then `P` would have CHT.

#### Proof

Fix `A` and choose `m` with `f_A` `F_m`-measurable. Then for every `n>=m`,

\[
P_n(A)=E_R[f_A\mid F_n]=f_A.
\]

Therefore for any `delta`,

\[
O(A,\delta)=\bigcup_{n=1}^m\{P_n(A)>\delta\},
\]

because later threshold sets equal the already finite-information set `{f_A>delta}`. The right side is a finite union of clopens and hence clopen. Thus `P(O)=R(O)`, while the finite hitting unions eventually equal `O`; CHT follows. QED.

If, in addition, some stabilized `f_A` were fractional on positive `R`-mass, then (5.4) would give `D(P)>0` and hence a positive answer to Nielsen Theorem 4 (the preceding R06 report already reduces the source's continuum-many requirement to one positive-defect witness).

So this is not a cosmetic sufficient condition: it would solve the active source problem immediately.

### Theorem 6.2 — universal finite-depth stabilization is impossible

No source-admissible finitely additive probability `P` on the Borel subsets of Cantor space can have `f_A` locally constant for every Borel event `A`. In particular, eventwise finite-depth stabilization is impossible.

The same proof shows the stronger statement that the family `f_A` cannot all be continuous.

#### Proof

Because Assumption 1 says every nonempty cylinder has positive `P`-mass and `R=P` on clopens, `R` has full support:

\[
R(C)>0\qquad\text{for every nonempty clopen }C.
\tag{6.1}
\]

Choose the standard shells

\[
S_k=[0^{k-1}1],\qquad z=0^\infty,
\]

and define the open set

\[
U=\bigcup_{k\ \mathrm{even}}S_k.
\tag{6.2}
\]

The point `z` lies in the closure of `U`, because every zero-cylinder `[0^n]` contains an even shell `S_k` with `k>n`. It also lies in the closure of `int(U^c)`, because every `[0^n]` contains an odd shell `S_k`, and each odd shell is clopen and lies inside `U^c`.

Now consider the companion density `f_U`.

If `x in U`, there is a clopen neighborhood `C` with

\[
x\in C\subseteq U.
\]

Then

\[
\int_C f_U\,dR=P(U\cap C)=P(C)=R(C).
\]

Since `0<=f_U<=1`, this implies `f_U=1` `R`-a.e. on `C`. If `f_U` were continuous, any point of `C` at which `f_U<1` would have a nonempty clopen neighborhood on which `f_U<=1-epsilon` for some `epsilon>0`; by full support (6.1) that neighborhood has positive `R`-mass, contradicting the a.e. equality. Hence continuity forces

\[
f_U(x)=1\qquad(x\in U).
\tag{6.3}
\]

Similarly, if `x in int(U^c)`, choose clopen `C` with `x in C subset U^c`. Then

\[
\int_C f_U\,dR=P(U\cap C)=0,
\]

so continuity plus full support forces

\[
f_U(x)=0\qquad(x\in int(U^c)).
\tag{6.4}
\]

But `z` is a limit point of both sets. Equations (6.3) and (6.4) would force simultaneously

\[
f_U(z)=1\quad\text{and}\quad f_U(z)=0,
\]

contradiction.

Therefore `f_U` is not continuous. A finite-level `F_m`-measurable function is locally constant and therefore continuous, so universal eventwise finite-depth stabilization is impossible. QED.

### Consequence

The attractive algorithm

\[
\text{“make every posterior process settle exactly after a finite event-dependent depth”}
\]

cannot solve Nielsen Theorem 4. Any successful witness must retain genuinely infinite-scale behavior for at least some Borel events, even though CHT asks only for exact continuity on their first-hitting opens.

No finite checker is appropriate: the obstruction is a symbolic compactness/topology proof with no finite computational core.

## 7. Method #27 — SWAP THE QUANTIFIERS: the Boolean-retraction shortcut is impossible

The operator view suggests an even sharper sufficient construction. Suppose there were two Boolean homomorphisms

\[
h_0,h_1:\mathcal B\to\mathcal C
\]

such that both fix every clopen set. With a strictly positive countably additive probability `Q` on Cantor space and `t in (0,1)`, define

\[
P_t(A)=tQ(h_0(A))+(1-t)Q(h_1(A)).
\tag{7.1}
\]

Then for every event `A`,

\[
f_A=t\mathbf1_{h_0(A)}+(1-t)\mathbf1_{h_1(A)},
\tag{7.2}
\]

which is finite-depth. Proposition 6.1 would give CHT automatically, while any event on which `h_0` and `h_1` disagree would have positive approximation defect. Varying `t` would also directly yield uncountably many witnesses.

Thus a pair of clopen-valued retractions would settle Nielsen Theorem 4 in the affirmative.

They cannot exist.

### Theorem 7.1 — no Borel-to-clopen Boolean retraction

There is no Boolean homomorphism

\[
h:\mathcal B\to\mathcal C
\]

with `h(C)=C` for every clopen `C`.

#### Proof

Assume such an `h` exists and use the same open set `U` from (6.2). Put

\[
H=h(U)\in\mathcal C.
\]

Every clopen `C subset U` satisfies

\[
C=h(C)\le h(U)=H.
\]

Since an open subset of Cantor space is the union of its clopen subsets,

\[
U\subseteq H.
\]

The set `H` is closed, so

\[
\overline U\subseteq H.
\tag{7.3}
\]

Now let `D` be any clopen subset of `U^c`. Then

\[
D=h(D)\le h(U^c)=H^c.
\]

The union of all clopen `D subset U^c` is `int(U^c)`, so

\[
\operatorname{int}(U^c)\subseteq H^c.
\]

Taking complements gives

\[
H\subseteq \bigl(\operatorname{int}(U^c)\bigr)^c=\overline U.
\tag{7.4}
\]

Equations (7.3)--(7.4) force

\[
H=\overline U.
\tag{7.5}
\]

But

\[
\overline U=U\cup\{z\}
\]

is not open: every neighborhood `[0^n]` of `z` contains an odd shell `S_k`, which is disjoint from `U cup {z}`. Hence `overline U` is not clopen, contradicting `H in C`. QED.

### Why Sikorski does not rescue the route

Sikorski's extension theorem extends Boolean homomorphisms when the **codomain is complete**. The clopen algebra `C` here is countable and atomless and is not complete. The theorem therefore does not produce the forbidden retraction above. Passing instead to a complete Boolean algebra such as the regular-open completion changes the target and does not by itself make posterior hitting opens clopen or preserve the source metric.

This precisely identifies why the most tempting abstract extension argument fails.

## 8. What this run changes mathematically

The source metric does not move, but the search space shrinks in a durable way.

The preceding run already ruled out convexifying the valid KPS one-limit-point ultrafilter family: a non-two-valued free charge plus atom protection creates a positive CHT gap.

This run rules out a different, much more abstract escape:

1. one cannot make all companion densities finite-level or even continuous;
2. one cannot obtain a witness from a Boolean retraction of the Borel algebra onto the finite-information clopen algebra;
3. therefore a successful positive construction must be genuinely infinite-scale **and** nonconvex in a way not reducible to clopen-valued Boolean selections.

The operator identity isolates the exact remaining target:

\[
\boxed{
\begin{array}{c}
\text{find a positive source-admissible finite-additive operator with some fractional }f_A,\\[2mm]
P(O(A,\delta))=R(O(A,\delta))\text{ for every self-generated hitting open},
\end{array}}
\tag{8.1}
\]

or prove no such operator exists.

The important quantifier change is that **finite-depth behavior is needed only on the hitting-open balance identities, not for every Borel density**. Universal finite-depth is impossible; hitting-family-specific control remains viable.

## 9. Relation to neighboring R01 work

R01 owns the distinct KPS Corollary-1 problem. Its newest report derives a ghost-tower necessity and rules out a countable sequential-ultrafilter hierarchy as a counterexample to almost-sure convergence.

The present result is complementary rather than duplicative. R01 assumes approximation and analyzes truth convergence. R06 seeks CHT without approximation and here shows that the strongest finite-depth operator shortcut cannot exist. I did not edit R01 files or use its metric as R06 progress.

## 10. Stuck status and next methods

This is the second unchanged run after the `W_CHT=1/2` baseline was established, so the Section-I stuck protocol does **not** trigger yet. If the next run also leaves `W_CHT` at `1/2`, that run must be a stuck/thinking run rather than another local lemma run.

The next three Section-B moves should avoid this run's `#1/#19/#27` and the immediately preceding `#5/#11/#29`. Recommended next triple:

- **#7 TAKE THE LIMIT:** replace forbidden finite-depth stabilization by a controlled infinite-depth limit and identify a sufficient boundary-balance condition for every threshold;
- **#15 BREAK THE SYMMETRY ON PURPOSE:** leave the one-limit-point KPS geometry and test a diffuse continuum of limit fibers, where no single companion atom carries the boundary defect;
- **#21 ASK WHO ELSE HAS THIS SHAPE:** search finitely additive conditional expectation / dilation / boundary representation literature for positive module maps with prescribed continuity on a special family of stopping-time opens.

The concrete target for the next run is not “prove another lemma.” It is to decide whether a **diffuse-fiber ultrafilter kernel** can satisfy (5.7) while producing a fractional `f_A`, or whether the boundary-flux mechanism generalizes to rule it out.

## 11. Structured ledger_delta

```yaml
ledger_delta:
  worker: R06
  lane: CLOSABLE_OUTSIDE
  historical_source:
    id: I0056
    source: "Lyons--Peres, Probability on Trees and Networks, Question 6.20"
    frozen_pair: "{5,5}"
    normalization: "outer vertex boundary"
    metric_before: 0
    metric_after: 0
    status: "PROVED frozen subtarget / full source PARTIAL / rotated"
  active_source:
    id: KPS-2026-NIELSEN-THEOREM4
    source: "Khan--Pedersen--Stinchcombe arXiv:2609.20683v1, Section 10; Nielsen Theorem 4"
    metric: "W_CHT = width of certified interval for Delta_CHT"
    before_interval: "[0, 1/2]"
    after_interval: "[0, 1/2]"
    metric_before: "1/2"
    metric_after: "1/2"
    status: OPEN
    unchanged_count_before: 1
    unchanged_count_after: 2
  tried_moves: [1, 19, 27]
  new_claims:
    - "Canonical companion-density/operator representation for arbitrary source-admissible P, including exact defect formula."
    - "Universal eventwise finite-depth (indeed continuous-density) stabilization is impossible under source positivity."
    - "No Boolean-algebra retraction Borel(Cantor) -> Clopen(Cantor) fixing clopens exists."
  finite_checker: "not applicable; analytic/topological claims only"
  remaining_obligation: "Construct one CHT probability with positive clopen-approximation defect, or prove CHT forces zero defect."
  literature_check_date: "2026-09-18"
  source_version: "arXiv:2609.20683v1"
  prior_art_status: "source still records Theorem 4 open; bounded negative search only; no novelty claim"
  audit_ids: []
  next_moves: [7, 15, 21]
```

## 12. Runtime-control truth

The owner-requested model line is present, but this invocation actually identifies as **GPT-5.6 Sol**. Authenticated reasoning-effort telemetry is unavailable, so the reasoning level is **UNVERIFIED**. The exposed automation/task controls provide prompt/title, schedule/timing mode and enabled-state controls, but no binding model selector, no reasoning-effort selector, no authenticated completed-run model attestation and no guaranteed hour-long runtime field.

The recorded P26 `You cannot modify this task` incident was authorization-context-specific; later repository records show a different authorized context successfully updated P26. The legitimate workaround is an owning/admin product context exposing the required controls, not a worker-side permission bypass. No scheduler modification, email, Drive write, public posting, purchase, permission change or peer-file edit was attempted in this run.
