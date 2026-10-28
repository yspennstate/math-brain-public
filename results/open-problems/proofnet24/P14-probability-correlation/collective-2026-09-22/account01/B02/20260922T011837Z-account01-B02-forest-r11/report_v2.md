# FOREST / account01-B02 — exact degree-three star identity and sharp degree-four obstruction

Run: `20260922T011837Z-account01-B02-forest-r11`  
Authoritative report revision: **v2**, incorporating the later-retrieved assigned-partner handoff; the earlier `report.md` is preserved as immutable run history.  
Candidate: `FOREST-DEG3-STAR-ID-v1`  
Outcome: **ESSENTIAL_STEP_APPLIED**  
Parent target: **OPEN**  
Execution context: **WITHOUT_VERIFIED_BRAIN**

## 1. Source target and current collective state

For a finite simple graph `G`, let `F` be uniform over **all** acyclic edge subsets, including the empty forest and disconnected forests. For distinct edges `e,f`, write

\[
\Delta_G(e,f)=Z_e Z_f-Z Z_{ef}.
\]

The target is `Delta_G(e,f) >= 0` for every marked pair.

This run consumed the latest complete lead snapshot

`account01/B01/20260922T000824Z-account01-B01-forest-11/report.md`
(blob `367d85a8c6ac4ef3f00e1686a28eac60642274e0`).

In a lexicographically minimal source counterexample that snapshot proves the universal Simpson inequality

\[
\rho_{eg}\rho_{fg}\ge \rho_{ef}>0
\]

for every third edge `g` when `(e,f)` violates the target. It follows there that violating pairs form a matching in the edge-correlation graph, every third edge is strictly negatively correlated with both members of a violating pair, and a preserved minimal 3-connected candidate satisfies `rho_ef <= 1/13`.

The named OTHER-account result applied here is account04/B02

`20260922T000916Z-account04-B02-r46/report.md`
(blob `47f7f2ae8703696df361ce78033b50c51212fa23`).

For an adjacent marked pair `e=ab,f=ac`, that report proves the exact triangle-completion identity and hence: in a lexicographically minimal simple counterexample, a violating adjacent pair must be an **induced open wedge**, so `bc` is absent.

I also used account03/B03 `20260922T005605Z-b03-forest-r11b` (blob `0246ec8c670c47ed632dfc2de0b7a6fdb3f8443f`) as a method constraint: its exact activity residual inequality is asymptotically saturated on complete graphs, so a constant-factor-loss switch is not an acceptable universal mechanism.

The assigned partner account02/B03 **did** deliver the later source-bound handoff
`FOREST-BOUNDARY-DISCRIMINANT-v2`,
(blob `abf745feb0430529ebc4ce68458ea99c6d8c4f3f`). It proves the exact one-boundary-edge Rayleigh quadratic
`Q(w)=D0+M w+D1 w^2` and the corrected response-weight criterion
\[
Q(w)\ge0
\iff
P_eP_f\le \frac{A+wB}{w}(BD_0+AwD_1).
\]
It also gives a genuine overlapping-cycle witness with negative mixed coefficient `M=-2` while `Q(w)>0` for every positive `w`, so coefficientwise positivity of the boundary quadratic is not a valid proof principle.

## 2. Compact conditional end-to-end route

The lead and peer reductions imply that a minimal counterexample can be sought among 3-connected graphs. If a violating pair is adjacent, account04/B02 reduces it to an induced open wedge `b-a-c`. The first local question is then whether a low-degree center can support the required Simpson reversal.

This run closes that question exactly at degree three:

> **Theorem (`FOREST-DEG3-STAR-ID-v1`).**  
> Let `G` be any finite simple graph and let `a` have degree three with
> `N_G(a)={b,c,d}`. Put `e=ab` and `f=ac`. Under the uniform law on all
> unrooted forests of `G`,
> \[
> \Delta_G(e,f)\ge0.
> \]
> More strongly, the Rayleigh gap has an exact positive-coefficient
> decomposition in five connectivity-state counts of `G-a`.

Consequently, in a lexicographically minimal 3-connected counterexample, **every violating adjacent pair is an induced open wedge whose center has degree at least four**.

This does not settle disjoint marked pairs, nor adjacent pairs centered at degree at least four, so the parent conjecture remains open.

## 3. Exact star-extension partition

Assume `deg_G(a)=3`, with star edges

\[
e=ab,\qquad f=ac,\qquad g=ad,
\]

and put `K=G-a`.

For every forest `H` of `K`, classify the connectivity partition induced by `H` on `{b,c,d}`. Let

- `s0`: `b|c|d` (all three separate);
- `sbc`: `bc|d`;
- `sbd`: `bd|c`;
- `scd`: `cd|b`;
- `sbcd`: `bcd` (all three connected).

All other vertices and components are unrestricted. Let

\[
N=s_0+s_{bc}+s_{bd}+s_{cd}+s_{bcd},
\]

the total number of forests of `K`.

For a fixed `H`, an incident-edge set `S subseteq {e,f,g}` extends `H` to a forest of `G` **iff no two selected star edges end in the same component of `H`**.

Proof: if two selected star edges have endpoints in one `H`-component, the two star edges together with the unique `H`-path between their non-`a` endpoints create a cycle. Conversely, if every selected star edge goes to a different `H`-component, contracting the components of `H` turns the selected star edges into an ordinary star, hence no cycle is created. This is exact and includes disconnected `H`.

Therefore the extension multiplicities are:

| state of `{b,c,d}` in `H` | all extensions | containing `e` | containing `f` | containing both `e,f` |
|---|---:|---:|---:|---:|
| `b|c|d` | 8 | 4 | 4 | 2 |
| `bc|d` | 6 | 2 | 2 | 0 |
| `bd|c` | 6 | 2 | 3 | 1 |
| `cd|b` | 6 | 3 | 2 | 1 |
| `bcd` | 4 | 1 | 1 | 0 |

No local swap or injectivity assumption appears in this table: these are exhaustive quotient-component counts.

Thus

\[
\begin{aligned}
Z&=8s_0+6(s_{bc}+s_{bd}+s_{cd})+4s_{bcd},\\
Z_e&=4s_0+2s_{bc}+2s_{bd}+3s_{cd}+s_{bcd},\\
Z_f&=4s_0+2s_{bc}+3s_{bd}+2s_{cd}+s_{bcd},\\
Z_{ef}&=2s_0+s_{bd}+s_{cd}.
\end{aligned}
\tag{3.1}
\]

## 4. Positive signed identity

Expanding `Z_e Z_f-Z Z_ef` in (3.1) and collecting the five disjoint state products gives

\[
\boxed{
\Delta_G(e,f)
=
4s_{bc}N
+s_{bd}s_{cd}
+s_{bcd}(s_{bd}+s_{cd}+s_{bcd}).
}
\tag{4.1}
\]

Every term is nonnegative, proving the theorem.

### 4.1 Application of the assigned partner's exact boundary-weight criterion

Keep `e,f` at unit source weight and give the third star edge `g=ad` a variable weight `w>=0`. The same five-state extension count gives the exact quadratic

\[
\begin{aligned}
\Delta(w)
={}&(1+w)^2 s_{bc}(s_0+s_{bc}+s_{bd}+s_{cd})
+2(1+w)s_{bc}s_{bcd}\\
&+s_{bcd}(s_{bcd}+s_{bd}+s_{cd})
+w^2s_{bd}s_{cd}
+(1-w^2)s_0s_{bcd}.
\end{aligned}
\tag{4.2}
\]

Hence

\[
\boxed{\Delta(w)\ge0\quad\text{for every }0\le w\le1.}
\tag{4.3}
\]

At the actual source value `w=1`, the last term cancels and (4.2) becomes exactly (4.1).

This directly applies account02/B03's `FOREST-BOUNDARY-DISCRIMINANT-v2`: in this degree-three star geometry the partner's exact induced-response threshold is satisfied throughout the full interval from deletion (`w=0`) to the unit source edge (`w=1`). The term `(1-w^2)s_0s_{bcd}` also explains why one must **not** infer an all-positive-coefficient quadratic or arbitrary-`w` closure from the unit theorem. This agrees with the partner's separate `M=-2` adversary: the correct object is the whole response quadratic at the actual response, not the sign of its mixed coefficient.

This is also an exact multiplicity certificate in the requested forest-pair language. The signed difference between the positive product `Z_e Z_f` and negative product `Z Z_ef` is the cardinality of the following disjoint **decorated** pair reservoir:

- four labelled copies of `S_bc x F(K)`;
- one copy of `S_bd x S_cd`;
- one copy of `S_bcd x (S_bd union S_cd union S_bcd)`.

Here each `S_pi` is the actual set of forests of `K` realizing terminal partition `pi`. Hence the coefficients `4,1,1` are proved extension multiplicities, not guessed fibre bounds.

The argument also survives arbitrary positive weights on edges of `K`, replacing each `s_pi` by the corresponding weighted forest sum, while the three incident star edges retain unit weight. Only the unit-weight source theorem is needed here.

### Degree-two boundary

If `deg(a)=2`, with only `e=ab,f=ac`, let `s` count forests of `G-a` in which `b,c` are separate and `t` those in which they are connected. Then directly

\[
Z=4s+3t,\quad Z_e=Z_f=2s+t,\quad Z_{ef}=s,
\]

and

\[
\Delta=t(s+t)\ge0.
\]

Thus degree at most three is completely settled for adjacent marked pairs.

## 5. Application to the named OTHER-account theorem

Account04/B02 proves that an adjacent violating pair in a lexicographically minimal source counterexample must be an induced open wedge `b-a-c`, i.e. `bc` is absent.

The present identity adds an independent local restriction. A preserved minimal source counterexample is 3-connected, hence `deg(a)>=3`. If `deg(a)=3`, (4.1) gives `Delta_G(ab,ac)>=0`, contradicting violation. Therefore

\[
\boxed{
\text{adjacent violation in a minimal counterexample}
\Longrightarrow
bc\notin E(G)\ \text{and}\ \deg_G(a)\ge4.
}
\tag{5.1}
\]

Combining with the lead snapshot, such a pair must simultaneously be the unique positive-correlation partner of each marked edge, every third edge must have strictly negative covariance with both marked edges, and the marked Pearson correlation is at most the lead's bound.

A useful immediate corollary is that **no adjacent edge pair can be a violating pair in a cubic minimal counterexample**. This does not rule out disjoint violating pairs.

## 6. Sharp obstruction to blindly extending the same mechanism to degree four

The coefficientwise positivity in (4.1) is special. It already fails for the analogous star-conditioned pair expansion at degree four.

Let `a` have four neighbours. For a base forest `H` of `G-a`, let

\[
W(H)=\prod_C (1+k_C),
\]

where `k_C` is the number of neighbours of `a` in component `C`. If `b,c` are the endpoints of the marked star edges, define

\[
\alpha_H=\frac1{1+k_{C_b}},\qquad
\beta_H=\frac1{1+k_{C_c}},\qquad
r_H=\mathbf1_{\{C_b\ne C_c\}}.
\]

The exact symmetrized contribution of a pair of base forests `H,J` to `Delta` is proportional to

\[
K(H,J)=
\alpha_H\beta_J+\alpha_J\beta_H
-r_H\alpha_H\beta_H-r_J\alpha_J\beta_J.
\tag{6.1}
\]

Take one base state with all four neighbours separate and another with all four joined. Then

\[
(W,\alpha,\beta,r)=(16,\tfrac12,\tfrac12,1)
\quad\text{and}\quad
(5,\tfrac15,\tfrac15,0),
\]

so

\[
K=-\frac1{20},
\qquad
W(H)W(J)K=-4.
\tag{6.2}
\]

Thus a degree-four proof cannot simply assert nonnegativity of every star-conditioned base-pair term. Genuine switching/cancellation between different base pairs is required.

This negative local term is source-realizable. For example, take the four star edges from `a` and let `G-a` contain a path through all four neighbours. The empty outside forest and the full outside path give exactly the two states in (6.2). Direct source counts for one labelled realization are

\[
Z=82,\quad Z_e=Z_f=34,\quad Z_{ef}=14,\quad \Delta=8>0.
\]

So (6.2) refutes only the stronger **termwise-positive degree-four mechanism**, not the FOREST conjecture.

## 7. Exact regression

The archived checker exhausts every outside simple graph for `n=4,5,6` with a fixed degree-three center `a` and neighbours `b,c,d`, independently enumerates all forests of the full graph, and verifies both (3.1) and (4.1).

Executed output:

```text
FOREST_DEG3_STAR_ID_PASS
outside_graphs_exhausted_n4_to_n6=1096
zero_gap_instances=169
direct_forest_count_identity_failures=0
positive_coefficient_identity_failures=0
degree4_sep_join_cross_coefficient=-4
DEGREE4_COEFFICIENTWISE_EXTENSION_REJECTED
```

Checker SHA-256: `d504b254a9530664e0f30a2064a9f9aeb71fb7c8637dbe293229b568c507230d`.  
Output SHA-256: `f10e8bfc0d2bad8d5e628c710d194215cb03f99f6259670906a9a781cfe156e8`.

The finite computation is regression evidence only; the universal degree-three proof is the quotient-component calculation above.

## 8. First essential remaining implication

The surviving adjacent obstruction is now source-exact:

> In a lexicographically minimal 3-connected counterexample, can an induced open wedge `b-a-c` with `deg(a)>=4` satisfy the lead's simultaneous Simpson constraints for **every** third edge?

The degree-four calculation shows that a proof by coefficientwise positivity of independent star states is impossible. The next switching must couple *different* base forests and use either:
1. a multiplicity-controlled exchange between their neighbour-component partitions, or
2. the lead's global sign requirement to show the negative base-pair terms in (6.2) force a forbidden positive covariance with one of the other star edges.

That is a genuinely smaller unpaid implication than before this run. It preserves the full source target and does not replace it by a fixed-size, rooted, or weighted-parent problem.

## 9. Status

- Parent Grimmett-Winkler FOREST conjecture: **OPEN**.
- `FOREST-DEG3-STAR-ID-v1`: **proved** as an exact all-graphs local theorem; the partner boundary-weight formulation is verified here for the entire literal third-star-edge interval `0<=w<=1`.
- Minimal-counterexample consequence: adjacent violations must be induced open wedges centered at degree at least four.
- Naive coefficientwise degree-four extension: **CANDIDATE_REFUTED** by an exact source-realizable negative base-pair term.
- Overall run label: **ESSENTIAL_STEP_APPLIED**.
- Novelty/priority of the degree-three identity: **UNVERIFIED**; no publication-priority claim is made.
- Brain status: **WITHOUT_VERIFIED_BRAIN**.
