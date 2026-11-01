Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum.**

# NM13-04 / T07 — split-5 activity-2 atom, transparent theta neutralizers, and recursively decorated bicliques

Status: **PARTIAL on the parent Grimmett–Winkler problem / CANDIDATE_FULL for the restricted theorems below, pending later independent review.** The arbitrary-finite-graph uniform-forest pairwise negative-correlation conjecture remains OPEN.

Repository / branch: private `yspennstate/math-open-problems` / `master`  
Assigned root: `proofnet24/NM13-04/progress-forest/`  
Companion: NM13-08, `proofnet24/NM13-08/progress-forest-structure/`

## 0. Short handoff and why this run changes method

The three preceding NM13-04 substantive runs all left the parent source metric unchanged while proving, successively:

1. strict unit p-NC for `K_3 join I_n`;
2. strict unit p-NC for `K_4 join I_n`;
3. the stronger one-port-field PF-Rayleigh theorem for `Q_n=(K_5 join I_n)-01`, hence strict unit p-NC for `K_5 join I_n`.

The third run already warned not to make the next run merely a `B_6=203`-state `K_6 join I_n` repetition. The owner’s current PROGRESS20 rule also requires a materially different method after three unchanged substantive runs.

This run therefore leaves the terminal-partition transfer route and uses **deletion/contraction substitution and terminal activity balancing**. It consumes two fresh neighboring advances rather than duplicating them:

* NM13-08 proved PF series/parallel closure and, in its newest report, arbitrary-internal-edge insertion of transparent PF gadgets, together with the earlier unit-core transparent substitution theorem.
* PROB10-07 has now proved unit p-NC for every complete bipartite graph `K_{a,b}` with `min(a,b)<=30`.

The new work here is to extract an exact activity-2 PF atom from NM13-04’s own split-5 theorem, neutralize it by an explicit **infinite theta family of activity 3**, and then combine the exact substitution identities with PROB10-07 to obtain a genuinely new recursively decorated all-parameter graph class.

`POSTED.md` was checked. This T07 parent and the restricted constructions below are not treated as posted source-level closure.

## 1. Parent problem before/after, separately from mechanism gain

For a finite simple graph `G=(V,E)`, let

\[
I_G(\mathbf y)=\sum_{F\subseteq E:\,F\text{ acyclic}}\prod_{e\in F}y_e,
\qquad
\Delta_G(e,f)=I_eI_f-I_GI_{ef}.
\]

At unit weights, `Delta_G(e,f)>=0` is exactly pairwise negative edge correlation for the uniform measure on **all** forests.

**Parent source status:** `OPEN -> OPEN`.  
**Largest completely certified all-graph vertex order in repository continuity:** `9 -> 9`.  
**Equivalent lower bound on a source-valid counterexample order:** `>=10 -> >=10`.

The finite brute-force checks in this run certify terminal counts for one 7-vertex atom and one 11-vertex compensator only. They are **not** finite all-graph coverage and do not move the parent metric.

**Mechanism before this run:** split-5 PF atoms `Q_n`; NM13-08 transparent/PF substitution calculus; PROB10-07 biclique p-NC through width 30.

**Mechanism after this run:** an explicit infinite family `A_ell` (`ell>=2`) of **transparent, PF-Rayleigh, non-series-parallel** two-terminal gadgets built from the split-5 atom `Q_2`, plus the theorem that arbitrary finite recursive replacement of edges of any unit-p-NC core by these `A_ell` preserves unit p-NC. Applying this to the newly certified `K_{a,b}` cores gives a new all-parameter decorated-biclique class.

## 2. Essential recovered P14 and literature scope

Only dependencies needed here were reread.

### P14 continuity and failed routes

Preserved P14 facts:

* all source-scope simple graphs through nine vertices are unit-p-NC;
* block factorization reduces a vertex-minimal counterexample to 2-connected;
* the two-separator transfer plus the fixed-graph unit-to-positive-weight implication reduces it further to 3-connected;
* one-edge-field Rayleigh quadratics are exact and useful.

Preserved failures that matter for this run:

* the generic degree-three star/mesh route leaves a mixed three-terminal polarization;
* that mixed term is not universally nonnegative;
* the proposed reverse-Cauchy inequality was exactly refuted by a physical six-vertex example even though the physical Rayleigh gap stayed positive;
* Lorentzian/stability/Gårding shortcuts still lack the missing source-matching hypothesis.

Therefore this run does **not** claim a universal deletion/contraction discriminant theorem. The new theorem is a controlled substitution theorem with an exact transparent gadget.

### Fresh bounded public-source check on 20 September 2026

* Grimmett–Winkler, `math/0302185`, first published 29 April 2004 in *Random Structures & Algorithms* 24, study the uniform measure on **all forests**. Their published numerical verification is all graphs through eight vertices and nine-vertex graphs with at most 18 edges. Spanning trees are explicitly a different already-known law.
* Erickson, `arXiv:1008.3660`, proves the stronger all-positive-weight independent-set-Rayleigh statement for **series-parallel** graphs by a sum-of-squares formula.
* Huang, `arXiv:2311.00965`, treats arboreal-gas negative correlation on restricted graph families and still describes the general negative-correlation problem as open.
* Bado, DOI `10.1016/j.spl.2026.110960`, proves strict uniform-forest p-NC for every wheel, an infinite 3-connected non-series-parallel family.
* Tang–Zhang, `arXiv:2603.10738`, submitted 11 March 2026, prove p-NC for specified complete-graph spanning-subgraph ensembles including forests with a **fixed** component count (for fixed `k` and sufficiently large `n`), not the all-component uniform-forest law on arbitrary graphs.

A bounded search did not surface either the split-5 activity-2 neutralizer below or the recursively decorated biclique class. That is negative evidence only. **Novelty/priority remains UNVERIFIED.**

## 3. Two-terminal notation and the exact split-5 activity-2 atom

For a two-terminal graph `A` with terminals `u,v`, all real edges at unit weight, write

\[
I_A=D_A+C_A,
\]

where `D_A` counts forests in which `u,v` are disconnected and `C_A` counts forests in which they are connected. Define the terminal activity

\[
t_A=\frac{C_A}{D_A}.
\]

The empty forest gives `D_A>0`. Call `A` **transparent** if `t_A=1`.

Let

\[
Q_2=(K_5\vee\overline{K_2})-01,
\]

with terminals `0,1`. The preceding split-5 PF theorem proves that `Q_2` is PF-Rayleigh, i.e. after adjoining the virtual port edge `01` at arbitrary weight `s>=0`, every Rayleigh difference is nonnegative.

That report’s independent brute-force identity was

\[
I_{Q_2+ s\,01}=20826+6942s.
\]

For a virtual terminal edge, the coefficient of `s` is exactly `D_{Q_2}` while the constant term is `D_{Q_2}+C_{Q_2}`. Hence

\[
D_Q=6942,
\qquad
C_Q=20826-6942=13884=2D_Q,
\]

so

\[
\boxed{t_Q=2.}
\tag{3.1}
\]

The new checker independently re-enumerates every one of the `2^19` edge subsets of `Q_2` and recovers exactly these two terminal counts.

## 4. An explicit all-parameter activity-3 PF compensator

Fix an integer `ell>=2` and put

\[
q_\ell=2^\ell-1,
\qquad
r_\ell=3q_\ell.
\]

Let `B_ell` be the two-terminal theta graph consisting of `r_ell` internally disjoint paths of length `ell` in parallel, with fresh interiors.

For one length-`ell` path, every edge subset is a forest. The terminals are connected only when all `ell` edges are present, so

\[
D_{P_\ell}=2^\ell-1=q_\ell,
\qquad
C_{P_\ell}=1.
\]

In a parallel union of such paths, a forest may have **at most one** fully connected branch, since two connected branches would form a cycle. Therefore

\[
D_{B_\ell}=q_\ell^{r_\ell},
\qquad
C_{B_\ell}=r_\ell q_\ell^{r_\ell-1}
=3q_\ell^{r_\ell},
\]

and thus

\[
\boxed{t_{B_\ell}=3.}
\tag{4.1}
\]

Every `B_ell` is series-parallel, hence I-Rayleigh by Erickson and therefore PF-Rayleigh.

For `ell=2`, `B_2=K_{2,9}` with the two degree-9 vertices as terminals. The checker independently enumerates all `2^18` edge subsets and obtains

\[
D_{B_2}=19683=3^9,
\qquad
C_{B_2}=59049=3^{10}.
\]

## 5. New transparent non-series-parallel PF gadget family

Form `A_ell` by putting `Q_2` and `B_ell` **in series**, identifying terminal `1` of `Q_2` with one terminal of `B_ell`; the remaining terminal of `Q_2` and the far terminal of `B_ell` are the external terminals of `A_ell`.

For arbitrary two-terminal graphs `X,Y` composed in series, the outer terminals connect iff both pieces connect. Hence

\[
C_{X\circ Y}=C_XC_Y,
\]

while every other combination disconnects the outer terminals:

\[
D_{X\circ Y}=D_XD_Y+D_XC_Y+C_XD_Y.
\]

Equivalently,

\[
t_{X\circ Y}=\frac{t_Xt_Y}{1+t_X+t_Y}.
\tag{5.1}
\]

Using (3.1) and (4.1),

\[
t_{A_\ell}
=\frac{2\cdot3}{1+2+3}
=1.
\]

More exactly,

\[
D_{A_\ell}
=6D_QD_{B_\ell}
=C_{A_\ell}
=41652\,(2^\ell-1)^{3(2^\ell-1)}.
\tag{5.2}
\]

NM13-08’s PF series-composition theorem applies because both factors are PF-Rayleigh. Therefore:

### Theorem `T07-SPLIT5-Q2-THETA-NEUTRALIZER-04`

For every integer `ell>=2`, `A_ell` is **PF-Rayleigh and transparent**.

It is also genuinely outside Erickson’s series-parallel graph class: `Q_2` contains the `K_4` subgraph on clique vertices `{0,2,3,4}`, and `Q_2` is a subgraph of `A_ell`. Hence `A_ell` has a `K_4` minor and is not series-parallel.

The exact size is

\[
|V(A_\ell)|
=8+3(2^\ell-1)(\ell-1),
\]

\[
|E(A_\ell)|
=19+3\ell(2^\ell-1).
\tag{5.3}
\]

For `ell=2`, this gives a 17-vertex, 37-edge transparent PF gadget with

\[
D=C=819836316.
\]

This is a different neutralizer from NM13-08’s split-4 `Q_7` activity-`25/7` construction: here the non-series-parallel atom is NM13-04’s own split-5 `Q_2`, its activity is exactly `2`, and the compensator has the simple constant activity `3` for every `ell>=2`.

## 6. Self-contained unit-core substitution sign theorem

The following is the exact deletion/contraction mechanism used to turn `A_ell` into a graph-class theorem.

Let `H` be a unit-p-NC graph and let `g=uv` be any edge. Let `A` be a transparent PF-Rayleigh two-terminal graph with fresh interior and `D_A=C_A=d`. Replace `g` by `A`, identifying its terminals with `u,v`; call the result `H[g<-A]`.

Put `B=H-g`, regarded as a two-terminal graph at `u,v`. Write `D_B,C_B` for its unit terminal-conditioned forest sums.

For two surviving core edges `r,k`, transparency gives polynomially in all surviving core variables

\[
I_{H[g<-A]}=d\,I_H\big|_{y_g=1},
\]

hence

\[
\boxed{
\Delta_{H[g<-A]}(r,k)=d^2\Delta_H(r,k)\ge0.
}
\tag{6.1}
\]

For two gadget edges `p,q`, the environment presents `A` with the effective nonnegative port activity

\[
t_B=C_B/D_B\ge0.
\]

Direct differentiation of

\[
I_{H[g<-A]}=D_B(I_A+t_BD_A)
\]

gives

\[
\boxed{
\Delta_{H[g<-A]}(p,q)
=D_B^2\Delta_{\widehat A(t_B)}(p,q)\ge0,
}
\tag{6.2}
\]

because `A` is PF-Rayleigh.

For a mixed gadget/core pair, define

\[
J_A(p)=D_AC_{A,p}-C_AD_{A,p}.
\]

The same deletion/contraction expansion gives the exact cancellation

\[
\boxed{
\Delta_{H[g<-A]}(p,r)
=J_A(p)\,\Delta_H(g,r)\ge0.
}
\tag{6.3}
\]

Here `J_A(p)>=0` is exactly the Rayleigh difference between `p` and the virtual port edge of `A`, and `Delta_H(g,r)>=0` is supplied by unit p-NC of the core.

Equations (6.1)–(6.3) cover every edge pair. Therefore one replacement preserves unit p-NC. Since the resulting graph is again unit p-NC, the same argument iterates.

### Theorem `T07-RECURSIVE-TRANSPARENT-SUBSTITUTION-04`

If `H` is any finite simple unit-p-NC graph, then **every graph obtained by any finite sequence of edge replacements by fresh copies of `A_ell`, with an arbitrary choice `ell>=2` at each step, is unit-p-NC.**

Because `A_ell` has no edge joining its two external terminals directly, replacing an edge of a simple graph by a fresh `A_ell` preserves simplicity.

This theorem is source-valid for the resulting graphs: it concerns the uniform measure on all forests and does not change to spanning trees, fixed-component forests, or another ensemble.

## 7. New all-parameter graph class from the 02:55 PROB10 biclique theorem

The newest PROB10-07 report proves

\[
\boxed{
K_{a,b}\text{ is unit-p-NC whenever }\min(a,b)\le30.
}
\]

Apply Theorem `T07-RECURSIVE-TRANSPARENT-SUBSTITUTION-04` to these cores.

### Corollary `T07-DECORATED-BICLIQUES-04`

Fix arbitrary integers `a,b>=1` with `min(a,b)<=30`. Starting from `K_{a,b}`, perform any finite sequence of edge replacements by fresh gadgets `A_{ell_1},A_{ell_2},...`, where every `ell_i>=2`; replacements may be made on original edges or on edges created by earlier replacements. Then the resulting finite simple graph satisfies pairwise negative edge correlation under the uniform measure on all forests.

This is an infinite recursive class with unbounded graph size and arbitrarily many non-series-parallel blocks.

For the nonrecursive one-round case, replacing `k` distinct original biclique edges with `A_{ell_1},...,A_{ell_k}` gives

\[
|V|
=a+b+\sum_{i=1}^k\left[6+3(2^{\ell_i}-1)(\ell_i-1)\right],
\]

\[
|E|
=ab+\sum_{i=1}^k\left[18+3\ell_i(2^{\ell_i}-1)\right].
\tag{7.1}
\]

As soon as `k>=1`, the graph contains a `K_4` minor inside the inserted `Q_2` block, so this theorem is not an Erickson series-parallel corollary. The base biclique theorem itself is a separate exact repository result; this run does not relabel it as literature.

The same substitution corollary also applies to every other certified unit-p-NC core, including all source-scope graphs through nine vertices, wheels, and NM13-04’s split families. The biclique application is singled out because it is the newest genuinely all-parameter core theorem and had not yet been combined with NM13-08’s transparent calculus.

## 8. Exact computation and what it does / does not prove

Checker:

`proofnet24/NM13-04/progress-forest/runs/2026-09-20/2026-09-20T03-18-30Z__q2_theta_neutralizer_checker.py`

creation commit `9a30052e5a7fc90aac008dd0014830f3aa83d242`.

Archived output:

`proofnet24/NM13-04/progress-forest/runs/2026-09-20/2026-09-20T03-18-30Z__q2_theta_neutralizer_checker.out`

creation commit `553b6fa222f769c9a6ec472f3052cb9831332d79`.

The checker:

1. independently enumerates all `2^19` edge subsets of `Q_2` and verifies `D_Q=6942`, `C_Q=13884`;
2. independently enumerates all `2^18` edge subsets of `B_2=K_{2,9}` and verifies `D=19683`, `C=59049`;
3. verifies the exact series formulas and `D_{A_ell}=C_{A_ell}` for `ell=2,...,8` using integer arithmetic;
4. ends `ALL_EXACT_CHECKS_PASS`.

The all-`ell` theorem does **not** rest on checking `ell<=8`: equations (4.1), (5.1), and (5.2) are closed exact formulas valid for every integer `ell>=2`. The finite computations are independent regressions of the terminal counts used in the proof.

## 9. Failed/rejected routes this run

1. **Generic deletion/contraction discriminant closure:** not revived. P14 already has an exact physical counterexample to the proposed universal reverse-Cauchy sufficient inequality. Any universal statement here would be false without a new hypothesis.
2. **`K_6 join I_n` 203-state transfer:** deliberately not attempted. It would be a fourth consecutive fixed-split transfer run with the parent metric unchanged, contrary to the progress-first instruction.
3. **Activity balancing by numerical search:** unnecessary. The exact split-5 atom `Q_2` has activity `2`, so the required series compensator activity is exactly `3`; the theta family `B_ell` realizes this algebraically for every `ell>=2`.

The successful route is therefore a genuine method change: exact activity extraction + PF series balancing + deletion/contraction substitution.

## 10. Residual obstruction and next attack

The parent conjecture is still blocked at arbitrary 3-connected graphs. Transparent substitution creates broad new p-NC families but introduces 2-separators, so it does not by itself eliminate the minimal 3-connected obstruction isolated by P14.

The next useful attack should keep the new deletion/contraction viewpoint but target a **3-connected operation** rather than another separator decoration. A concrete candidate is an edge-addition criterion: for `G=H+g`, express the full one-edge-field Rayleigh quadratic for an old-edge pair in terms of the deletion law `H`, the contraction law `H/g`, and the two conditional marginal responses, then identify a structural hypothesis strictly weaker than the already-refuted universal reverse-Cauchy bound and verify it on a new 3-connected family. If no such hypothesis survives exact small examples, return to counterexample search rather than forcing a false general inequality.

## 11. ledger_delta

```yaml
ledger_delta:
  track: NM13-04
  parent: T07
  source_target: "Grimmett-Winkler uniform-all-forests pairwise edge negative correlation on every finite graph"
  parent_status_before: OPEN
  parent_status_after: OPEN
  source_metric: "largest completely certified all-graph vertex order"
  source_metric_before: 9
  source_metric_after: 9
  source_counterexample_lower_bound_before: ">=10"
  source_counterexample_lower_bound_after: ">=10"
  substantive_run_streak_before_method_change: 3
  method_change_executed: "terminal activity balancing + PF series composition + deletion/contraction transparent substitution"
  predecessor_preserved:
    - "NM13-04 split-5 one-port PF theorem for Q_n=(K5 join I_n)-01"
    - "P14 3-connected minimal-counterexample reduction and failed generic mixed-polarization routes"
    - "NM13-08 PF series/parallel and transparent substitution calculus"
    - "PROB10-07 K_{a,b} p-NC for min(a,b)<=30"
  new_theorems:
    - id: T07-SPLIT5-Q2-THETA-NEUTRALIZER-04
      verdict: CANDIDATE_FULL
      statement: "for every ell>=2, A_ell = Q_2 series B_ell is transparent PF-Rayleigh and non-series-parallel"
    - id: T07-RECURSIVE-TRANSPARENT-SUBSTITUTION-04
      verdict: CANDIDATE_FULL
      statement: "finite recursive replacement of edges of a unit-p-NC core by fresh A_ell gadgets preserves unit p-NC"
    - id: T07-DECORATED-BICLIQUES-04
      verdict: CANDIDATE_FULL
      statement: "all recursively A_ell-decorated K_{a,b}, min(a,b)<=30, are uniform-forest p-NC"
  exact_counts:
    Q2_D: 6942
    Q2_C: 13884
    Q2_activity: 2
    B2_D: 19683
    B2_C: 59049
    B2_activity: 3
    A2_D_equals_C: 819836316
  exact_checker: "2026-09-20T03-18-30Z__q2_theta_neutralizer_checker.py"
  exact_output: "2026-09-20T03-18-30Z__q2_theta_neutralizer_checker.out"
  exact_output_terminal: ALL_EXACT_CHECKS_PASS
  novelty_status: UNVERIFIED
  residual_obstruction: "arbitrary 3-connected graphs; separator-based transparent substitution does not close the parent"
  next_attack: "derive and stress-test a genuinely 3-connected edge-addition/deletion-contraction sign criterion weaker than P14's refuted universal reverse-Cauchy condition"
```

`END OF REPORT`
