# FOREST / fleet01-B20 — exact path/contraction resolution of the overlap reservoir

Run: `B20-20260922T001739Z-t11`  
Directive: `COLLECTIVE-OPEN-PROBLEMS-20260921T234023Z`  
Outcome: **ESSENTIAL_STEP_APPLIED** (exact structural reduction only; parent conjecture remains **OPEN**)  
Brain status: **WITHOUT_VERIFIED_BRAIN**

## 1. Exact target and consumed cross-account versions

The active source target is the Grimmett--Winkler uniform-unrooted-forest pairwise inequality. For every finite simple graph `G`, if `F` is uniform over all acyclic edge subsets, prove for every distinct pair `e,f`

\[
\Pr(e,f\in F)\le \Pr(e\in F)\Pr(f\in F).
\]

With `Z,Z_e,Z_f,Z_ef` the corresponding forest counts, this is

\[
\Delta_G(e,f):=Z_eZ_f-ZZ_{ef}\ge0.
\]

I substantively consumed the following exact current collective results.

1. `fleet04/B02`, run `20260922T000916Z-fleet04-B02-r46`, report blob `47f7f2ae8703696df361ce78033b50c51212fa23`.  For an adjacent pair `e=ab,f=ac` it proves the exact five-state formula and the **triangle-completion theorem**: in a lexicographically minimal simple counterexample a violating adjacent pair must be an induced open wedge, so `bc` is absent.  It identifies the next unpaid step as using reconnection paths in the 3-connected obstruction rather than another small-graph census.
2. `fleet03/B02`, run `20260921T235733Z-b02-forest-r11`, report blob `c492ca3b040b5d185e0c825ef1c63d3759a3d8f8`.  It proves the deletion/contraction sign-coherence identity for a lexicographically minimal counterexample and the resulting bad-pair equivalence classes.
3. The compatible fleet01/B03 exact overlap reduction, run `20260921T234923Z-b03-poprestore-r11`, report blob `4dbaa2d764eddbc02026736e5b1fe265ba14f24d`, supplies the exact overlap correction and is used below as the common algebraic interface.

No peer PASS label is treated as target closure.  The parent problem remains open.

## 2. Starting point: the exact adjacent five-state gap

Fix adjacent distinguished edges

\[
e=ab,\qquad f=ac,
\]

and put

\[
K=G-\{e,f\}.
\]

For a forest of `K`, retain only the terminal partition of `{a,b,c}` and let

- `A=w_{abc}`;
- `B=w_{ac|b}`;
- `C=w_{ab|c}`;
- `Q=w_{a|bc}`;
- `D=w_{a|b|c}`.

The consumed exact reduction is

\[
\boxed{
\Delta_G(e,f)=BC-AD+Q(B+C+D+Q).
}
\tag{2.1}
\]

Here `Q` is exactly the overlap reservoir: the base forest connects `b` to `c` while keeping `a` in another component.  The current collective bottleneck is to exploit that reservoir with controlled multiplicity rather than discard it.

The new result below resolves `Q`, and in fact every nontrivial three-terminal state, into exact path/contraction channels.

## 3. Path-contraction lemma for a pair-connected terminal state

Let `K` be any finite graph (parallel edges are allowed in contractions below), let `x,y,z` be three distinct terminals, and use arbitrary positive edge weights `y_h` if desired.  Write

\[
W_{xy|z}(K)
\]

for the weighted forest sum in which `x,y` lie in one component and `z` lies in a different component.

For a simple `x-y` path `P` contained in `K-z`, contract every edge of `P` to one vertex `s_P`.  Let

\[
D_{z,s_P}(K/P)
\]

be the weighted forest sum in the contracted graphic multigraph for forests in which `z` and `s_P` are disconnected.  Loops created by contraction are unavailable to a forest and parallel edges retain their ordinary graphic-matroid meaning.

### Lemma `FOREST-PATH-CONTRACTION-20260922`

\[
\boxed{
W_{xy|z}(K)
=
\sum_{P\in\mathcal P_{xy}(K-z)}
\left(\prod_{h\in P}y_h\right)
D_{z,s_P}(K/P).
}
\tag{3.1}
\]

At unit weights the path factor is one.

### Proof

Every forest counted by `W_{xy|z}` has a **unique** simple `x-y` path `P`; because `z` is in a different component, `P` avoids `z`.  Contracting `P` sends the remaining chosen edges to a forest of `K/P` in which `z` is disconnected from `s_P`.  Conversely, any such contracted forest lifts, together with the fixed path `P`, to a forest of `K` having terminal partition `xy|z`.  Graphic contraction gives a bijection, including the cases in which parallel classes or loops are created.  The weight factors into the path weight times the remaining forest weight.  Distinct paths are disjoint channels because a forest has only one `x-y` path.  Summing gives (3.1).  QED.

Applied cyclically,

\[
\begin{aligned}
B&=\sum_{P\in\mathcal P_{ac}(K-b)} y(P)D_{b,s_P}(K/P),\\
C&=\sum_{P\in\mathcal P_{ab}(K-c)} y(P)D_{c,s_P}(K/P),\\
Q&=\sum_{P\in\mathcal P_{bc}(K-a)} y(P)D_{a,s_P}(K/P).
\end{aligned}
\tag{3.2}
\]

Thus the formerly opaque overlap count `Q` is an exact **disjoint sum of two-terminal disconnection partition functions on contracted minors**.

## 4. Exact resolution of the all-connected state by the same `b-c` paths

The all-connected state `A` admits a sharper decomposition using the same path index.

For a simple `b-c` path `P`, put `Z_P=I(K/P)`, the weighted sum of all forests of the contracted multigraph.  If `P` avoids `a`, split

\[
Z_P=C_P+D_P,
\]

where `D_P=D_{a,s_P}(K/P)` and `C_P` is the weighted forest sum with `a` connected to `s_P`.

Define

\[
A_{\rm off}:=\#\{H\in A:\ a\notin P_{bc}(H)\},
\qquad
A_{\rm mid}:=\#\{H\in A:\ a\in P_{bc}(H)\},
\]

with the evident weighted interpretation.  Here `P_{bc}(H)` is the unique `b-c` path in the forest `H`.

Then

\[
\boxed{
Q=\sum_{P\in\mathcal P_{bc}(K-a)} y(P)D_P,
\qquad
A_{\rm off}=\sum_{P\in\mathcal P_{bc}(K-a)} y(P)C_P,
}
\tag{4.1}
\]

and

\[
\boxed{
A_{\rm mid}
=
\sum_{\substack{P\in\mathcal P_{bc}(K)\\ a\in V(P)}} y(P)I(K/P),
\qquad
A=A_{\rm off}+A_{\rm mid}.
}
\tag{4.2}
\]

### Proof

If an all-connected forest has a `b-c` path avoiding `a`, contraction of that unique path leaves `a` connected to the contracted path vertex.  This is exactly the `C_P` channel and is reversible.  If the unique `b-c` path contains `a`, then the fixed path itself already connects all three terminals, so after contraction **any** forest of `K/P` lifts to an all-connected forest with that unique `b-c` path.  Conversely every all-connected forest falls in exactly one of these two cases.  QED.

A more symmetric equivalent form is obtained by summing over minimal terminal Steiner trees `T`:

\[
\boxed{
A=\sum_{T\in\mathcal T_{abc}(K)}y(T)I(K/T).
}
\tag{4.3}
\]

Each all-connected forest has one unique minimal terminal subtree, so (4.3) is again a disjoint contraction decomposition.

## 5. New exact form of the adjacent Rayleigh gap

Substitute (4.1)--(4.2) into (2.1).  Since

\[
Q-A_{\rm off}
=
\sum_{P\in\mathcal P_{bc}(K-a)}y(P)(D_P-C_P),
\]

we obtain

\[
\boxed{
\Delta_G(e,f)
=
BC-D A_{\rm mid}
+Q(B+C+Q)
+D\!\sum_{P\in\mathcal P_{bc}(K-a)}y(P)(D_P-C_P).
}
\tag{5.1}
\]

This is an exact source-scope identity, not a sufficient condition and not a finite-size approximation.

It separates the old single negative term `-AD` into two precise mechanisms:

1. **through-`a` path mass** `A_mid`, which has to be paid primarily by the ordinary `BC` switching channel;
2. **pathwise two-terminal odds** `C_P-D_P` on contracted minors, which is paired path-by-path with the overlap reservoir `Q`.

That is substantially narrower than the undifferentiated obligation `AD <= BC+Q(B+C+D+Q)`.  A future switching map can now carry the unique path label `P` as part of its reversible data; landing in `Q` no longer has an uncontrolled path multiplicity.

## 6. Consequence for the current minimal-counterexample branch

By the consumed fleet04/B02 result, if a lexicographically minimal simple counterexample has a violating adjacent pair `ab,ac`, then `bc` is absent.  By the inherited 3-connectivity reduction, `G-a` is 2-connected.  Therefore there are at least two internally vertex-disjoint `b-c` paths in `G-a`.

But `K-a=G-a`, because only `ab,ac` were deleted.  Hence (4.1) gives the exact lower bound

\[
\boxed{
Q
=\sum_{P\in\mathcal P_{bc}(G-a)}D_{a,s_P}(K/P)
\ge \#\mathcal P_{bc}(G-a)
\ge2
}
\tag{6.1}
\]

at unit weights.  The first inequality uses only the empty forest in each contracted disconnection count.  More importantly than the numerical `2`, every path term in (6.1) is a two-terminal partition function on a **strict contracted minor**; because `bc` is absent, each avoiding path has at least two edges.

Thus the 3-connected open-wedge branch really does possess the overlap mass suggested by fleet04/B02, and (5.1) identifies exactly what remains to control.  The existence of two paths alone is not enough: the signs of `D_P-C_P` are not fixed, and `A_mid` remains an independent negative channel.  No unsupported inequality such as `Q>=A` or `D_P>=C_P` is asserted.

## 7. First still-unpaid implication

The parent conjecture would follow for the adjacent branch from a multiplicity-controlled path-labelled charge proving the right side of (5.1) nonnegative.  The next exact obligation is therefore:

> **PATHWISE-CHARGE.**  For every 3-connected open-wedge candidate, use the contracted path channels to charge (i) the through-`a` path mass `D A_mid` into `BC`, and (ii) every negative two-terminal imbalance `D(C_P-D_P)` into the positive `Q(B+C+Q)` reservoir, without counting one base forest in two different path channels.

The decomposition proves that the overlap side of this prospective map has no hidden path multiplicity: every `Q` forest has exactly one `b-c` path.  What is still missing is the cross-forest switching that pays the two displayed negative mechanisms.  This is the first unpaid universal implication after the consumed open-wedge result.

## 8. Exact independent computation

Two stdlib-only exact checkers are archived in this run.

`path_contraction_checker.py` verifies on **all 1,096 labelled simple graphs on 3,4,5 vertices** that

- all three pair-connected identities (3.1) hold; and
- the Steiner-tree contraction identity (4.3) holds.

That is `4,384` exact identities with zero failures.

`adjacent_path_resolution_checker.py` independently verifies on the same 1,096 graphs that

- the `Q` path decomposition in (4.1) is exact; and
- the split `A=A_off+A_mid` in (4.1)--(4.2) is exact.

That is another `2,192` exact identities with zero failures.  The finite checks audit the bijections; they are not evidence of universal target closure.

## 9. Status and integrity

Classification: **ESSENTIAL_STEP_APPLIED**.

The full Grimmett--Winkler forest conjecture remains **OPEN**.  This run neither claims a full adjacent-pair proof nor a novelty/priority certificate.  It converts the overlap reservoir and the all-connected obstruction into exact path-labelled contracted-minor sums and exposes a concrete switching obligation that directly continues the newest cross-account open-wedge candidate.

No new brain-installation or benchmark work was performed after the live owner reallocation was read.  No benchmark gold, credentials, scheduler identifiers, machine paths, unrelated private transcripts, email, Drive, paid/remote compute, workflow or permission change appears in these scientific artifacts.
