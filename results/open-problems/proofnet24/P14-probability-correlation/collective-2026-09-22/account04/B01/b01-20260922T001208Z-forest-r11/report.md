# FOREST / account04 B01 — exact multi-bridge 2-separator gluing and weighted reconnection interface

Run: `b01-20260922T001208Z-forest-r11`  
Campaign: `COLLECTIVE-OPEN-PROBLEMS-20260921T234023Z` / FOREST  
Outcome: **ESSENTIAL_STEP_APPLIED (separator/gluing step only; parent conjecture remains OPEN)**  
Assignment: derive the all-parameter gluing/three-connected step connecting the current valid pieces, explicitly handling separator cases missing from known closure results.

## 1. Source-exact target and inherited facts

For a finite simple graph `G`, let

\[
I_G(\mathbf y)=\sum_{F\subseteq E(G):\,F\text{ acyclic}}\prod_{h\in F}y_h
\]

and

\[
\Delta_G(e,f)=I_e I_f-I_G I_{ef}.
\]

At unit weights, `Delta_G(e,f)>=0` is exactly the Grimmett--Winkler pairwise negative-correlation conjecture for the uniform law on all forests.

The exact inherited state used here is:

1. P14 has complete unit-weight coverage through nine vertices.
2. The fixed-graph Cocks/Semple--Welsh implication used by P14 upgrades a simple graph that satisfies the unit-weight source conjecture to the needed all-positive-weight independence-Rayleigh statement.
3. P14 previously stated that block factorization plus a binary two-separator transfer reduce a vertex-minimal counterexample to a 3-connected graph.
4. `account01/B03`, run `20260921T234923Z-b03-poprestore-r11`, derived the exact reconnection identity. For `K=G-{e,f}`, a forest `H` of `K`, addability indicators `X,Y`, four cell weights `n_ij`, total `N`, and overlap weight `q`,
   \[
   \Delta_G(e,f)=n_{10}n_{01}-n_{00}n_{11}+Nq
                =N^2(\Pr(Q)-\operatorname{Cov}(X,Y)).
   \]
   Thus the exact unpaid comparison is `Cov(X,Y)<=Pr(Q)`, not the false stronger assertion `Cov(X,Y)<=0`.
5. `account03/B02`, run `20260921T235733Z-b02-forest-r11`, derived the three-edge deletion/contraction identity and the sign-cluster restrictions that any lexicographically minimal counterexample must obey once the 3-connected reduction is justified.

The assigned partner is `account01/B02`. No completed current FOREST artifact for that slot was present in the latest account01 collective tree observed during this run, so the live missing-peer rule applies. The two named other-account results above are consumed directly below rather than waiting.

## 2. Multi-bridge separator model

Let `u,v` be two terminals. Let `B_1,...,B_m` be edge-disjoint subgraphs whose pairwise vertex intersections are exactly `{u,v}` and which otherwise have disjoint vertices. A possible original edge `uv` may be treated as its own one-edge bridge.

For each bridge `B_i`, split its forest polynomial into

\[
D_i=\sum_{\substack{F\text{ forest of }B_i\\u\not\leftrightarrow v\text{ in }F}}y^F,\qquad
C_i=\sum_{\substack{F\text{ forest of }B_i\\u\leftrightarrow v\text{ in }F}}y^F.
\]

The empty forest contributes to `D_i`, so `D_i>0` at every positive specialization.

A union of bridge forests is a forest of the glued graph `G` iff **at most one bridge connects `u` to `v`**. Therefore the full forest polynomial is exactly

\[
\boxed{
I_G=\prod_iD_i+\sum_i C_i\prod_{j\ne i}D_j
=\left(\prod_iD_i\right)\left(1+\sum_i\frac{C_i}{D_i}\right).
}
\tag{2.1}
\]

This already handles arbitrarily many `{u,v}`-bridges at once; no binary-associativity assumption is needed.

For a bridge `B_i`, let `g_i=uv` be a new virtual edge. Its completed forest polynomial is

\[
I_{B_i+g_i}=C_i+(1+y_{g_i})D_i,
\tag{2.2}
\]

because `g_i` may be selected exactly when the underlying bridge forest disconnects the terminals.

## 3. Same-bridge Rayleigh gaps: the outside world is one scalar fugacity

Fix distinct marked edges `e,f` in `B_i`. Put

\[
P_i=\prod_{j\ne i}D_j,\qquad
\Lambda_i=\sum_{j\ne i}\frac{C_j}{D_j}.
\tag{3.1}
\]

When differentiating with respect to `e,f`, both `P_i` and `Lambda_i` are constants. Equation (2.1) becomes

\[
I_G=P_i\bigl(C_i+(1+\Lambda_i)D_i\bigr).
\]

Hence, by direct differentiation,

\[
\boxed{
\Delta_G(e,f)=
P_i^2\,
\Delta_{B_i+g_i}(e,f)\big|_{y_{g_i}=\Lambda_i}.
}
\tag{3.2}
\]

This is the exact all-parameter same-side transfer. Every other `{u,v}`-bridge enters only through the **additive connection ratio**

\[
\Lambda_i=\sum_{j\ne i} C_j/D_j.
\]

Thus no separator proof may replace all external structure by an unweighted virtual edge unless it has proved that specialization. The physically induced virtual weight is generally nonunit and depends on the exact outside forest partition sums.

Boundary cases are automatic:

- a bridge that cannot connect `u,v` has `C_j=0` and contributes zero to `Lambda_i`;
- an original separator edge `uv` treated as a singleton bridge has `D=1,C=y_{uv}` and simply contributes its edge weight to `Lambda_i`;
- `Lambda_i=0` is covered directly by (3.2), or by continuity from positive values.

## 4. Cross-bridge Rayleigh gaps: complete cancellation of all other bridges

Let `e in B_i` and `f in B_j`, `i!=j`. Write derivatives with respect to the marked edge as `D_{i,e},C_{i,e}` and define the terminal response

\[
R_i(e)=D_iC_{i,e}-C_iD_{i,e}.
\tag{4.1}
\]

Let

\[
P_{ij}=\prod_{k\ne i,j}D_k.
\]

Expanding (2.1) and its three relevant derivatives gives the exact factorization

\[
\boxed{
\Delta_G(e,f)=P_{ij}^2\,R_i(e)\,R_j(f).
}
\tag{4.2}
\]

All ratios `C_k/D_k` from bridges other than `i,j` cancel identically.

Moreover, from (2.2),

\[
\Delta_{B_i+g_i}(e,g_i)
=
D_iC_{i,e}-C_iD_{i,e}
=
R_i(e),
\tag{4.3}
\]

and this quantity is independent of the virtual-edge weight `y_{g_i}`. Therefore

\[
\boxed{
\Delta_G(e,f)=
P_{ij}^2\,
\Delta_{B_i+g_i}(e,g_i)\,
\Delta_{B_j+g_j}(f,g_j).
}
\tag{4.4}
\]

This explicitly pays the cross-separator case that is easy to lose in a sequential gluing argument. It also shows why merely proving same-side inequalities in each bridge is insufficient: the internal-edge/virtual-edge Rayleigh signs are the exact cross-side interface.

### Algebra check for (4.2)

After factoring out `P_{ij}`, set

`a=D_i, b=C_i, x=D_{i,e}, y=C_{i,e}`,
`c=D_j, d=C_j, s=D_{j,f}, t=C_{j,f}`,

and let `r=sum_{k!=i,j} C_k/D_k`. Then

\[
\begin{aligned}
Z&=ac(1+r)+ad+bc,\\
Z_e&=xc(1+r)+xd+yc,\\
Z_f&=as(1+r)+at+bs,\\
Z_{ef}&=xs(1+r)+xt+ys.
\end{aligned}
\]

A direct expansion gives

\[
Z_eZ_f-ZZ_{ef}=(ay-bx)(ct-ds),
\]

which is exactly `R_i(e)R_j(f)`. In particular `r` cancels without any sign or approximation assumption.

## 5. Exact multi-bridge closure theorem

### Theorem (terminal-Rayleigh gluing)

Suppose for every `i` the completed bridge `B_i+g_i` is Rayleigh for every edge pair at every positive specialization required for its ordinary and virtual edge weights. Then the glued graph `G` is Rayleigh.

**Proof.** If both marked edges lie in one bridge, use (3.2). If they lie in different bridges, use (4.4). Both right sides are nonnegative. These exhaust all edge pairs. The singleton `uv` bridge is included by the boundary convention above. QED.

For the source unit-weight conjecture, the hypothesis can be weakened to the precise values actually generated by the other bridges: for same-bridge pairs one needs `B_i+g_i` at `y_g=Lambda_i`, and for cross-bridge pairs only the internal/virtual response (4.3).

## 6. Rigorous minimal-counterexample 3-connected reduction, including multi-component 2-cuts

Take a source counterexample `G` lexicographically minimal in `(|V|,|E|)`.

A one-vertex cut is eliminated by ordinary block factorization: same-block Rayleigh gaps reduce to a proper block, while cross-block edge indicators factor.

Now suppose `G` is 2-connected but has a 2-cut `{u,v}`. Let `K_1,...,K_m`, `m>=2`, be the components of `G-{u,v}`. For each `K_i`, form `B_i` from `K_i union {u,v}` and all incident edges, but place a possible original edge `uv` in its own singleton bridge. Because `G` is 2-connected, every nontrivial bridge attaches to both terminals. The completed graph `B_i+g_i` is simple and has strictly fewer vertices than `G`.

By minimality, every `B_i+g_i` satisfies the source unit-weight pairwise inequality. The fixed-graph Cocks/Semple--Welsh implication used in the preserved P14 state then supplies the positive-weight Rayleigh property needed at the induced virtual fugacity `Lambda_i`. Applying the theorem of §5 makes every pair in `G` Rayleigh, contradicting that `G` is a counterexample.

Hence

\[
\boxed{\text{every lexicographically minimal source counterexample is 3-connected.}}
\tag{6.1}
\]

This conclusion was already recorded in prior P14 work. The new contribution of this run is the explicit **multi-bridge, all-induced-parameter formula** (3.2)/(4.4), which removes the binary-gluing ambiguity and records exactly which weighted statement is used at a cut.

## 7. Direct application of account01/B03's reconnection identity

The same-side formula (3.2) gives a precise bridge from the current collective reconnection reduction to the old separator reduction.

Fix `e,f in B_i`. In the completed bridge `B_i+g_i`, set `y_{g_i}=Lambda_i`, delete `e,f`, and put on the remaining forests the resulting positive weighted law. The four-cell derivation of account01/B03 is purely algebraic, so with weighted cell sums it gives

\[
\Delta_{B_i+g_i}(e,f)
=
N_i(\Lambda_i)^2
\left[\Pr_{\Lambda_i}(Q)-\operatorname{Cov}_{\Lambda_i}(X,Y)\right].
\tag{7.1}
\]

Combining (3.2) and (7.1),

\[
\boxed{
\Delta_G(e,f)=
P_i^2N_i(\Lambda_i)^2
\left[\Pr_{\Lambda_i}(Q)-\operatorname{Cov}_{\Lambda_i}(X,Y)\right].
}
\tag{7.2}
\]

Therefore an arbitrary outside collection of separator bridges does **not** create a new kind of reconnection obstruction. It changes exactly one scalar parameter: the virtual-edge fugacity `Lambda_i`.

This also preserves the account01/B03 regression witness: one must not replace (7.2) by a proof of `Cov<=0`; the overlap reservoir `Q` remains essential.

## 8. Connection to account03/B02 and the remaining universal step

Account03/B02 proved that after reaching a lexicographically minimal 3-connected counterexample, any violating pair `e,f` must satisfy a quantitative three-edge sign-coherence identity for every third edge, and the violating pairs form strict sign clusters.

Sections 2--7 justify that this 3-connected stage can be reached without losing the exact current reconnection comparison or silently setting virtual separator weights to one. Thus the two current collective reductions are compatible:

1. all 1- and 2-separator structure is removed by exact gluing;
2. any surviving counterexample is a 3-connected simple graph;
3. for a violating pair, the reconnection inequality fails there:
   \[
   \operatorname{Cov}(X,Y)>\Pr(Q);
   \]
4. simultaneously, the account03/B02 deletion/contraction sign-cluster inequalities hold for every third edge.

The first genuinely unpaid universal implication is therefore now localized to:

> **3-connected weighted-reconnection/sign-cluster obstruction.** Rule out, in a 3-connected simple graph, a pair `e,f` for which the exact reconnection excess `Cov(X,Y)-Pr(Q)` is positive while the account03/B02 quantitative sign-coherence constraints hold for every third edge.

This is strictly narrower than “handle separators” or “prove negative covariance of addability”. The separator cases are paid by the identities above.

## 9. Status and handoff

**Target-level status:** OPEN.

**Run status:** `ESSENTIAL_STEP_APPLIED`.

What was proved here:

- exact forest-polynomial formula (2.1) for any number of `{u,v}`-bridges;
- exact same-bridge transfer (3.2) with the induced virtual fugacity `Lambda_i=sum C_j/D_j`;
- exact cross-bridge factorization (4.4), with complete cancellation of all other bridge ratios;
- a clean multi-bridge closure theorem;
- an explicit proof of the minimal-counterexample 3-connected reduction covering multi-component 2-cuts and a separator edge;
- exact compatibility formula (7.2) with account01/B03's current overlap-reconnection reduction.

What is **not** claimed:

- no full proof of Grimmett--Winkler;
- no improvement of the complete `n<=9` finite baseline;
- no claim that the 3-connected obstruction is solved;
- no claim that `Cov(X,Y)<=0`;
- no novelty/priority claim for the general 3-connected reduction already present in P14.

Suggested next use by the FOREST lead / partner workers:

1. adopt (3.2)/(4.4) as the separator interface rather than re-deriving binary gluing;
2. keep `Lambda_i` symbolic/nonnegative until a source theorem legitimately specializes it;
3. attack the localized 3-connected reconnection/sign-cluster obstruction, not separator bookkeeping;
4. test any stronger proposed reconnection inequality against account01/B03's `K_4-(2,3)` witness before using it universally.

## 10. Source/provenance and scope

Primary repository dependencies read in this run:

- `operations/claims/P0001.md`;
- `probability_campaign_2026_09/codex_20h_20260906/proofs/P0001_cactus_forests.md`;
- `proofnet24/P14-probability-correlation/runs/2026-09-17/2026-09-17T04-40-00Z__report.md`;
- `proofnet24/P14-probability-correlation/runs/2026-09-17/2026-09-17T05-19-47Z__mandatory-handoff-report.md`;
- `proofnet24/P14-probability-correlation/collective-2026-09-22/account01/B03/20260921T234923Z-b03-poprestore-r11/overlap_reconnection_report.md`;
- `proofnet24/P14-probability-correlation/collective-2026-09-22/account03/B02/20260921T235733Z-b02-forest-r11/report.md`.

Only source-matching mathematical material was read. No mixed-domain memory index, unrelated private corpus, email, Drive, benchmark answers, credentials, paid compute, remote workflow, or production population was used or modified.

`full_brain_connected=false`; this run is `WITHOUT_VERIFIED_BRAIN`.
