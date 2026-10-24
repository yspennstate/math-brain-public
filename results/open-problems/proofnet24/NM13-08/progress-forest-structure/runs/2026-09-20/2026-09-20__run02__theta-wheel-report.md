Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum.**

# NM13-08 / T07 — series/parallel terminal-activity calculus and transparent theta expansions of every wheel

Status: **PARTIAL on the parent problem / CANDIDATE_FULL for the restricted closure theorem below, pending later independent review.** The arbitrary-finite-graph uniform-forest conjecture remains OPEN.

Repository / branch: private `yspennstate/math-open-problems` / `master`  
Assigned root: `proofnet24/NM13-08/progress-forest-structure/`  
Companion: NM13-04, `proofnet24/NM13-04/progress-forest/`

## 0. Compact handoff and what changed this run

The preceding NM13-08 substantive report proved an exact two-terminal substitution identity. If an edge `g=xy` of a core `H` is replaced by a two-terminal graph `A`, with `D_A,C_A` the forest generating polynomials for terminal-disconnected and terminal-connected forests, then with `t_A=C_A/D_A`:

- core-core Rayleigh differences are `D_A^2` times the corresponding core Rayleigh difference evaluated at virtual port weight `y_g=t_A`;
- gadget-gadget Rayleigh differences reduce to the completed gadget `A+g` at a positive virtual port weight;
- cross-edge Rayleigh differences factor into two port-interface determinants `J_A(p)J_B(e)`, where `J_Q(p)=D_Q C_{Q,p}-C_Q D_{Q,p}`;
- consequently, if `t_A=1` at unit weights and `A+g` is I-Rayleigh, replacing an edge of a merely unit-p-NC core preserves unit p-NC.

That report supplied one fixed transparent gadget, `O_6-g`, with `D_A=C_A=361`, and used it to make arbitrarily large expansions of certified finite cores.

The current companion NM13-04 has now proved strict unit p-NC for every complete split graph `K_3 ∨ \overline{K_n}` by a five-state transfer matrix, and combined that with the octahedral gadget. I do **not** duplicate that split-graph theorem. This run instead develops the missing algebra of two-terminal **series and parallel composition**, uses it to manufacture infinitely many unit-transparent gadgets, and applies them to the independent all-parameter wheel theorem of Bado. The resulting family has three independent parameter layers: wheel size, number/location of substitutions, and a freely chosen theta length at every substitution.

`POSTED.md` was checked. The general T07 conjecture and the theorem below are not marked posted/settled there.

## 1. Exact parent problem and recovered scope

For a finite simple graph `G=(V,E)`, let

\[
I_G(\mathbf y)=\sum_{F\subseteq E:\,F\text{ acyclic}}\prod_{e\in F}y_e.
\]

For distinct edges `e,f`, write

\[
\Delta_G(e,f)=I_e I_f-I_G I_{ef}.
\]

At unit weights,

\[
\frac{\Delta_G(e,f)}{I_G^2}
=
\Pr(e\in F)\Pr(f\in F)-\Pr(e,f\in F),
\]

so `Delta_G(e,f)>=0` is exactly pairwise negative edge correlation for the uniform measure on **all** acyclic spanning edge subsets. Isolated vertices and all component counts are allowed. This is not the uniform spanning-tree measure.

Recovered exact scope:

1. **Grimmett--Winkler, `math/0302185`, RSA 24 (2004).** Their forest conjecture is the arbitrary-graph unit-weight pairwise statement above. Their computation proves it for every graph on at most 8 vertices and for every 9-vertex graph with at most 18 edges. They explicitly distinguish uniform forests from the already-known spanning-tree theorem.

2. **P14 repository continuation.** P14 exactly certified the complementary dense 9-vertex sector, so every simple graph on at most 9 vertices is covered at unit weights. Its complete-order source metric is `9`; therefore a counterexample, if one exists, has at least 10 vertices. No complete 10-vertex census is claimed.

3. **Erickson, `arXiv:1008.3660`.** Erickson defines the stronger I-Rayleigh property, `Delta>=0` at every positive edge-weight evaluation, and proves a sum-of-squares theorem for every series-parallel graph (Theorem 1.2). The paper also records prior two-sum closure of I-Rayleigh graphs and develops stronger SOS inheritance under minors/direct sums. This weighted theorem is stronger than the source's unit-only statement.

4. **Later work.** Huang (`arXiv:2311.00965`) studies arboreal-gas negative correlation in specific graph/parameter regimes and states the general problem remains open. Tang--Zhang (`arXiv:2603.10738`, 11 March 2026) prove p-NC for specified uniform spanning-subgraph families of the complete graph, including forests with a fixed number of components for fixed `k` and sufficiently large `n`; that is not the all-component-count arbitrary-graph measure here. Idriss Olivier Bado, *Negative edge correlation for uniform random forests on wheel graphs*, Statistics & Probability Letters 241, 110960, DOI `10.1016/j.spl.2026.110960`, proves strict pairwise negative edge correlation for every wheel `W_m=K_1+C_m`, `m>=3`, under the uniform measure on all forests.

Fresh bounded searches on 20 September 2026 for uniform-forest negative correlation combined with theta graphs / edge replacement / wheel expansion did not surface the closure class proved below. This is negative evidence only. **Novelty/priority is UNVERIFIED.**

## 2. New two-terminal series/parallel activity and sign calculus

Let `Q` be a two-terminal graph with terminals `x,y`. Split its forest polynomial into

\[
I_Q=D_Q+C_Q,
\]

where `D_Q` sums forests in which `x,y` are disconnected and `C_Q` sums forests in which `x,y` are connected. Define

\[
t_Q:=\frac{C_Q}{D_Q},
\qquad
q_Q:=\frac{C_Q}{C_Q+D_Q}=\frac{t_Q}{1+t_Q},
\]

and for an edge `p` of `Q` define the port-interface determinant

\[
J_Q(p):=D_Q C_{Q,p}-C_QD_{Q,p}.
\]

As in the previous report,

\[
J_Q(p)=\Delta_{Q+g}(p,g),
\]

where `g` is a new edge joining the terminals, and this expression is independent of the weight assigned to `g`.

### Theorem T07-SP-TERMINAL-CALCULUS-04

Let `Q_1,Q_2` be two-terminal graphs with disjoint interiors.

### (a) Parallel composition

Let `Q=Q_1\parallel Q_2`, obtained by identifying the two pairs of terminals. Then

\[
D_Q=D_1D_2,
\qquad
C_Q=C_1D_2+D_1C_2,
\tag{2.1}
\]

hence

\[
\boxed{t_Q=t_1+t_2.}
\tag{2.2}
\]

For `p in E(Q_1)`,

\[
\boxed{J_Q(p)=D_2^2J_{Q_1}(p),}
\tag{2.3}
\]

and symmetrically `J_Q(p)=D_1^2J_{Q_2}(p)` for `p in E(Q_2)`.

### (b) Series composition

Let `Q=Q_1\circ Q_2`, obtained by identifying the second terminal of `Q_1` with the first terminal of `Q_2` at a single articulation vertex. Then

\[
C_Q=C_1C_2,
\qquad
D_Q=D_1D_2+D_1C_2+C_1D_2,
\tag{2.4}
\]

hence

\[
\boxed{q_Q=q_1q_2}
\tag{2.5}
\]

and equivalently

\[
\boxed{t_Q=\frac{t_1t_2}{1+t_1+t_2}.}
\tag{2.6}
\]

For `p in E(Q_1)`,

\[
\boxed{
J_Q(p)=C_2(D_2+C_2)J_{Q_1}(p),
}
\tag{2.7}
\]

and symmetrically

\[
J_Q(p)=C_1(D_1+C_1)J_{Q_2}(p)
\]

for `p in E(Q_2)`.

### Proof

For parallel composition, a pair of forests `(F_1,F_2)` has acyclic union unless both `F_1` and `F_2` connect the terminals. If both connect, the unique terminal path in each forest forms a cycle in the union; conversely, a cycle using both sides would force a terminal path on each side. Thus the union is terminal-disconnected exactly when both sides are disconnected, giving `D_Q=D_1D_2`, while it is terminal-connected exactly when one side connects and the other disconnects, giving (2.1). Dividing by `D_1D_2` proves (2.2).

For `p in Q_1`,

\[
D_{Q,p}=D_{1,p}D_2,
\]

and

\[
C_{Q,p}=C_{1,p}D_2+D_{1,p}C_2.
\]

Therefore

\[
\begin{aligned}
J_Q(p)
&=D_1D_2(C_{1,p}D_2+D_{1,p}C_2)
 -(C_1D_2+D_1C_2)D_{1,p}D_2\\
&=D_2^2(D_1C_{1,p}-C_1D_{1,p}),
\end{aligned}
\]

which is (2.3).

For series composition, the two sides meet at only one vertex, so the union of any forest from `Q_1` and any forest from `Q_2` is automatically a forest. The outer terminals are connected iff both constituent forests connect their own terminals. Hence `C_Q=C_1C_2` and

\[
D_Q=(D_1+C_1)(D_2+C_2)-C_1C_2,
\]

which is (2.4). Equation (2.5) follows by dividing `C_Q` by the total polynomial `(D_1+C_1)(D_2+C_2)`; (2.6) is the same identity in odds coordinates.

For `p in Q_1`,

\[
D_{Q,p}=D_{1,p}(D_2+C_2)+C_{1,p}D_2,
\qquad
C_{Q,p}=C_{1,p}C_2.
\]

Substitution gives

\[
\begin{aligned}
J_Q(p)
&=[D_1(D_2+C_2)+C_1D_2]C_{1,p}C_2\\
&\qquad-C_1C_2[D_{1,p}(D_2+C_2)+C_{1,p}D_2]\\
&=C_2(D_2+C_2)(D_1C_{1,p}-C_1D_{1,p}),
\end{aligned}
\]

which is (2.7). QED.

### Sign consequence

At positive weights all prefactors in (2.3) and (2.7) are nonnegative. Therefore the port-interface sign condition

\[
J_Q(p)\ge0\quad\text{for every edge }p
\]

is closed under both series and parallel composition. This is stronger information than the scalar activity laws alone and is exactly the sign quantity occurring in the cross-edge factorization from `T07-PORT-SUBSTITUTION-01`.

## 3. An infinite factory of exact unit-transparent theta gadgets

For an integer `ell>=2`, let `P_ell` be a path of length `ell` between two terminals. Every edge subset of a path is a forest, and the terminals are connected iff all `ell` path edges are chosen. Therefore at unit weights

\[
D(P_\ell)=2^\ell-1,\qquad C(P_\ell)=1,
\tag{3.1}
\]

so

\[
t(P_\ell)=\frac1{2^\ell-1},\qquad q(P_\ell)=2^{-\ell}.
\tag{3.2}
\]

Let

\[
r_\ell:=2^\ell-1
\]

and let `A_ell` be the parallel union of `r_ell` internally vertex-disjoint copies of `P_ell`. By repeated use of (2.2),

\[
t(A_\ell)=r_\ell\,t(P_\ell)=1.
\tag{3.3}
\]

More explicitly, with `d=2^ell-1=r_ell`,

\[
D(A_\ell)=d^d,
\]

because every branch must be terminal-disconnected, while

\[
C(A_\ell)=d\cdot 1\cdot d^{d-1}=d^d.
\tag{3.4}
\]

Thus every `A_ell` is **exactly unit-transparent**:

\[
\boxed{D(A_\ell)=C(A_\ell).}
\]

Let `K_ell=A_ell+g`, where `g` is the direct terminal edge. `K_ell` is a two-terminal series-parallel graph: it is a parallel composition of one direct edge and `r_ell` length-`ell` paths. Erickson's Theorem 1.2 therefore makes `K_ell` I-Rayleigh at all positive weights.

For completeness, an individual edge `p` of `P_ell` has

\[
D_p=2^{\ell-1}-1,\qquad C_p=1,
\]

hence

\[
J_{P_\ell}(p)
=(2^\ell-1)-(2^{\ell-1}-1)
=2^{\ell-1}>0.
\]

The parallel sign law (2.3) therefore also gives strictly positive port-interface signs throughout `A_ell`.

### Corollary T07-THETA-TRANSPARENT-SUBSTITUTION-05

Let `H` be any graph satisfying unit-weight pairwise negative edge correlation for the uniform measure on all forests. Pick any edge `g=xy` and replace it by `A_ell` for an arbitrary `ell>=2`, using fresh internal vertices. Then the resulting graph `G` again satisfies unit-weight pairwise negative edge correlation.

### Proof

The previous NM13-08 substitution theorem applies with `A=A_ell`. Equation (3.4) gives `t_A=1`, so every core-core Rayleigh difference in `G` is exactly `D_A^2` times the corresponding **unit-weight** core Rayleigh difference in `H`. Thus no weighted hypothesis on the core is introduced.

For gadget-gadget pairs, the substitution theorem reduces the sign to a Rayleigh difference in `K_ell=A_ell+g` at a positive virtual port weight; this is nonnegative because `K_ell` is I-Rayleigh by Erickson's series-parallel theorem.

For a gadget edge `p` and core edge `e`, the substitution theorem gives

\[
\Delta_G(p,e)=J_{A_\ell}(p)J_{H-g}(e).
\]

The first factor is nonnegative because it equals a port-edge Rayleigh difference in the I-Rayleigh graph `K_ell`; the second equals the unit core difference `Delta_H(e,g)` and is nonnegative by hypothesis. These cases exhaust edge pairs. QED.

The important point is that the **core remains unit-only**. The stronger weighted theorem is used only on the fixed inserted series-parallel gadget.

## 4. New all-parameter application: theta-expanded wheels

Let

\[
W_m=K_1+C_m,\qquad m\ge3,
\]

with `m` rim vertices. Bado's theorem proves strict pairwise negative edge correlation for the uniform measure on all forests of every `W_m`.

Define `\mathcal W^\Theta` as follows.

1. Start from an arbitrary wheel `W_m`, `m>=3`.
2. Choose an arbitrary current edge.
3. Choose an arbitrary integer `ell>=2`.
4. Replace that edge by a fresh copy of `A_ell`, the parallel union of `2^ell-1` internally disjoint length-`ell` paths.
5. Repeat any finite number of times, with both the next edge and the next `ell` allowed to depend arbitrarily on the preceding construction.

### Theorem T07-WHEEL-THETA-CLOSURE-06

Every graph in `\mathcal W^\Theta` has pairwise negative edge correlation under the uniform measure on **all** forests.

### Proof

The starting wheel has unit p-NC by Bado. Each replacement preserves unit p-NC by Corollary `T07-THETA-TRANSPARENT-SUBSTITUTION-05`. Induction on the number of replacements proves the claim for every finite adaptive replacement sequence. QED.

This is genuinely all-parameter. If the replacement lengths are `ell_1,...,ell_k`, then

\[
|V|
=
m+1+\sum_{i=1}^k(2^{\ell_i}-1)(\ell_i-1),
\tag{4.1}
\]

and

\[
|E|
=
2m+\sum_{i=1}^k\bigl(\ell_i(2^{\ell_i}-1)-1\bigr).
\tag{4.2}
\]

There is no upper bound on `m`, `k`, or any `ell_i`.

### Why this is outside the recovered named theorem scopes

For `k>=1`, the resulting graph is not a wheel: every inserted theta gadget contributes fresh degree-2 internal vertices, whereas a wheel has rim degree 3.

It is not series-parallel. By deleting all but one branch inside every inserted gadget and contracting along that branch, the original wheel `W_m` is recovered as a minor. Every wheel `W_m`, `m>=3`, has a `K_4` minor (indeed `W_3=K_4`), so it is not series-parallel; series-parallel graphs are minor-closed.

The class is also not a complete-graph fixed-component family of Tang--Zhang. Its probability space is the uniform measure over forests of **all** component counts on sparse non-complete graphs.

Grimmett--Winkler's finite verification cannot cover the class because `m,k,ell_i` are unbounded. P14's all-graphs-through-9 certificate is likewise only the finite seed metric, not this transfer theorem.

The application is complementary to NM13-04: NM13-04's new source class is the complete split family `K_3∨\overline{K_n}` with a five-state terminal transfer. The present theorem starts from the independently known wheel family and enlarges it by an infinite factory of variable transparent theta substitutions.

## 5. Essential exact execution

Artifact `2026-09-20__run02__theta_checker.py` was executed locally with exact integer arithmetic; its preserved output is `2026-09-20__run02__theta_checker.out`.

The checker does four things.

1. Enumerates the smallest new gadget `A_2`, consisting of three internally disjoint 2-edge paths, and verifies `D=C=27`, `Z=54`.
2. Adds the direct port edge and checks all 21 unit Rayleigh numerators of the completed gadget: `Z=81`, `negative=0`, `min_delta=36`. The all-positive-weight theorem still comes from Erickson; this is only a finite sanity check.
3. Enumerates `W_4` and the graph obtained by replacing one spoke with `A_2`. It finds `Z(W_4)=134`, `Z(expanded)=3618=27*134`, all 78 edge-pair Rayleigh numerators nonnegative, and minimum numerator `13608`.
4. Verifies every surviving core-core pair scales by exactly `D_A^2=27^2=729`, and checks the closed transparent count identity for `ell=2,...,7`.

Terminal line:

`ALL_EXACT_CHECKS_PASS`.

This enumeration is **not** the all-parameter proof. It checks the algebra on the first nontrivial instance; the arbitrary-parameter result is the theorem above.

## 6. Parent scope vs demonstrated mechanism gain

### Parent theorem

Before: **OPEN** for arbitrary finite graphs under the uniform measure on all forests. Complete finite-order repository certificate through 9 vertices.

After: **OPEN**, with the same universal finite-order lower bound `counterexample order >=10`. This run does **not** claim a source-level finite-order improvement or a general proof.

### Demonstrated mechanism gain

Before this run, NM13-08 had one explicit unit-transparent I-Rayleigh port gadget, `O_6-g`, and arbitrary iteration of that single gadget over certified cores.

After this run:

- a complete series/parallel **terminal activity calculus** is proved;
- the port-interface sign `J` is shown to propagate by explicit nonnegative multiplicative factors under both series and parallel composition;
- an **infinite family** of simple unit-transparent gadgets `A_ell`, one for every `ell>=2`, is proved exactly;
- arbitrary **heterogeneous** sequences of these gadgets preserve unit p-NC;
- applying that closure to every wheel gives the new all-parameter class `\mathcal W^\Theta`, unbounded simultaneously in wheel size, substitution depth, and gadget length.

A compact metric for the demonstrated closure mechanism is therefore:

`number of explicit transparent gadget shapes available for substitution: 1 -> infinite (indexed by ell>=2)`,

while the parent source status remains `OPEN -> OPEN`.

## 7. Residual obstruction and next attack

The transparent substitution mechanism cannot by itself prove the general conjecture because it only enlarges graphs already known to satisfy unit p-NC. It does not yet show that an arbitrary 3-connected graph decomposes into a certified core plus transparent ports, nor does it control a generic two-terminal gadget with `t_A != 1` against a core known only at unit weight.

The most useful next attack is therefore not another gadget census. It is to seek a **multiport activity-balancing lemma**: given a nontransparent two-terminal side with activity `t!=1`, determine whether a finite series/parallel compensator can force total activity exactly 1 while preserving the relevant port-interface signs and without collapsing the graph back into an already known series-parallel scope. A successful balancing theorem would turn arbitrary local replacements into unit-preserving moves and could reach genuinely new 3-connected cores.

No historical/peer file, shared root, schedule, permission, workflow, public posting, email/Drive resource, or paid compute was modified.
