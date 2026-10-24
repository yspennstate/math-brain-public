# FOREST account04/B03 — second independent end-to-end review of `FOREST-KN-HERMITE-REDUCTION-v1`

Run: `20260922T014020Z-B03-r43`  
Outcome: **FULL_PROOF_CANDIDATE_REVIEW_2_PASS**  
Parent target: **OPERATIONALLY OPEN — NO AUTOMATIC TRUTH PROMOTION**  
Context: **WITHOUT_VERIFIED_BRAIN**

## 1. Exact target and control

The target is the source-exact Grimmett–Winkler forest conjecture: for every finite simple graph `G`, choose uniformly from **all** acyclic edge subsets, including the empty forest, disconnected forests, and every size. For every pair of distinct present edges `e,f`, prove

\[
\Pr(e,f\in F)\le \Pr(e\in F)\Pr(f\in F),
\]

equivalently

\[
\Delta_G(e,f):=Z_eZ_f-ZZ_{ef}\ge 0.
\]

Fresh owner control revision `2026-09-22.2` assigns account04/B03 to FOREST and explicitly supersedes the old installation/benchmark role. No installation work was performed in this run.

This report independently reviews the current team-lead candidate rather than rebuilding older local routes. The reviewed lead is account01/B01 `FOREST-KN-HERMITE-REDUCTION-v1`, shared handoff blob `cad5f1b8546f44f200d441b71095a9fde4a20d4b`, scientific report commit `77e2822624d2ea3881807aa7bfa56174563728c6`, report blob `e11be369a70e59449ea744da6f1e32040889c216`.

A named OTHER-account result was consumed and applied: account02/B03 `FOREST-2SEP-WEIGHTED-TRANSFER-v1`, shared handoff blob `5001e9cc0fb18f77c85ad0bb99d100da5937a1c0`, and its corrected one-boundary-edge follow-up `FOREST-BOUNDARY-DISCRIMINANT-v2`, shared handoff blob `abf745feb0430529ebc4ce68458ea99c6d8c4f3f`. Those results show that proper two-separators naturally induce arbitrary positive virtual-edge weights and that unit-edge simplification is not exact. This makes the lead's fixed-graph all-positive-weight upgrade the decisive all-graphs bridge rather than a cosmetic strengthening.

Before this review, account02/B02 independently reviewed the same lead candidate and recorded `PASS_SOURCE_BOUND_REVIEW_1` in `FOREST-SPECTRAL-CAP-REVIEW-v1`, blob `285be564e24a483d12d7dcb96dd3c422afc33403`. This report is an independent second end-to-end review.

## 2. External theorem bridge — independently source-checked

The published Semple–Welsh paper *Negative Correlation in Graphs and Matroids* gives exactly the two theorem facts needed by the lead.

First, on its p. 4 definition, a matroid is **independence correlated** when, for every distinct `e,f` and every positive real weighting `y`,

\[
I_e(M;y)I_f(M;y)-I_{ef}(M;y)I(M;y)\ge0.
\]

Second, Proposition 3.5 states that independence-correlated matroids are closed under minors.

Third, the final note on p. 13 explicitly records Cocks's fixed-graph result: if Conjecture 1.1 holds for a graph `G`, then `M(G)` is independence correlated.

Source checked in this run:
Charles Semple and Dominic Welsh, *Negative Correlation in Graphs and Matroids*,
https://www.math.canterbury.ac.nz/~c.semple/papers/SW07.pdf
(definition p. 4, Proposition 3.5 pp. 6–7, final note p. 13).

Therefore the following reduction is valid, graph by graph.

**Complete-graph reduction.** If the unit forest inequality holds for `K_n` for every `n`, then it holds for every finite simple graph. Indeed, fixed-graph Cocks upgrades unit Conjecture 1.1 on `K_n` to all-positive-weight independence correlation of `M(K_n)`. Proposition 3.5 passes this property to every deletion minor. Any simple graph on at most `n` vertices is obtained from `K_n` by deleting absent edges (isolated vertices do not change the graphic matroid or forest edge counts). Setting all surviving weights to one gives the source inequality.

I found no scope mismatch here. In particular, the Cocks statement is not merely a class-level implication, and the minor step is applied only after obtaining the stronger matroid property.

## 3. Independent derivation of the complete-graph formulas

Let

\[
R(z)=\sum_{m\ge1}m^{m-1}\frac{z^m}{m!},\qquad R=ze^R,
\]
\[
T(z)=R-\frac{R^2}{2},\qquad F(z)=e^{T(z)},\qquad A(z)=T'(z)=e^R.
\]

Here `F` is the labelled-forest EGF and `A` is the EGF for a labelled tree with one prescribed distinguished vertex.

For `K_n`, write `Z_n` for total forests, `E_n` for forests containing one fixed edge, and `J_adj,n`, `J_dis,n` for forests containing a fixed adjacent or disjoint pair.

The decompositions are:

\[
Z_n=n![z^n]F.
\]

For a fixed edge, deleting that edge from a forest that contains it creates two rooted tree components, hence

\[
E_n=(n-2)![z^{n-2}]FA^2.
\]

For two adjacent fixed edges, deleting both creates three rooted tree components, hence

\[
J_{\rm adj,n}=(n-3)![z^{n-3}]FA^3.
\]

For two disjoint fixed edges there are two cases. If the two marked edges belong to different tree components, deleting them gives four rooted components, contribution `FA^4`. If they belong to the same tree, deleting them gives three components; the middle component contains one endpoint of each marked edge, with four choices for that endpoint pair. A tree with two prescribed distinguished vertices has EGF

\[
T''(z)=A'(z)=\frac{A^2}{1-R}.
\]

Thus

\[
J_{\rm dis,n}
=(n-4)![z^{n-4}]FA^4\left(1+\frac4{1-R}\right).
\]

This rederivation confirms the lead's nontrivial disjoint-pair factor; no missing component case was found.

## 4. Independent Hermite coefficient derivation

Let `He_m(x)` be the probabilists' Hermite polynomial,

\[
e^{xu-u^2/2}=\sum_{m\ge0}He_m(x)\frac{u^m}{m!}.
\]

For

\[
C_m(a)=m![z^m]\exp(aR-R^2/2),
\]

Lagrange inversion with `R=ze^R` gives

\[
C_m(a)=He_m(m+a)-m\,He_{m-1}(m+a).
\]

Independently, the Cauchy change of variable `z=u e^{-u}` gives

\[
m![z^m]\frac{\exp(aR-R^2/2)}{1-R}=He_m(m+a).
\]

All four complete-graph coefficients therefore have the same Hermite argument `x=n+1`. Put

\[
H_j=He_j(n+1),\qquad D_j=H_j-jH_{j-1}.
\]

Then

\[
Z_n=D_n,\qquad E_n=D_{n-2},\qquad J_{\rm adj,n}=D_{n-3}.
\]

With `k=n-4`,

\[
J_{\rm dis,n}=D_k+4H_k=5H_k-kH_{k-1}.
\]

The Hermite recurrence `H_{j+1}=xH_j-jH_{j-1}` also gives

\[
J_{\rm adj,n}=4H_k-kH_{k-1},
\]

so

\[
J_{\rm dis,n}=J_{\rm adj,n}+H_k.
\]

Since `H_k(n+1)>0`, the disjoint orbit is strictly harder whenever both orbits exist.

## 5. One-variable gap and root estimate

Set

\[
a=H_k,\qquad s=\frac{kH_{k-1}}{H_k}.
\]

Repeated use of the Hermite recurrence yields

\[
J_{\rm dis,n}=a(5-s),\quad
J_{\rm adj,n}=a(4-s),
\]
\[
E_n=a(2n+6-3s),
\]
\[
Z_n=a(n^2+3n+10-(n+4)s).
\]

Hence

\[
E_n^2-Z_nJ_{\rm dis,n}=a^2G_n(s),
\]

where

\[
G_n(s)=(5-n)s^2+(n^2-4n-6)s-n^2+9n-14.
\]

This identity was independently checked symbolically by recurrence and exactly by code.

It remains to prove `G_n(s)>0`. The zeros `lambda_i` of `He_k` are the eigenvalues of the standard real symmetric Jacobi matrix with off-diagonal entries `sqrt(1),...,sqrt(k-1)`. Thus they are real and symmetric, and a row-sum/Gershgorin bound gives `|lambda_i|<2sqrt(k)<x=n+1`. Consequently

\[
s=\frac{H_k'(x)}{H_k(x)}
 =\sum_i\frac1{x-\lambda_i}.
\]

Pairing roots `+lambda,-lambda`,

\[
\frac1{x-\lambda}+\frac1{x+\lambda}
=\frac{2x}{x^2-\lambda^2}
\ge \frac2x+\frac{2\lambda^2}{x^3}.
\]

Using `sum_i lambda_i^2=k(k-1)`,

\[
s\ge \frac{k}{x}+\frac{k(k-1)}{x^3}
=\frac{(n-4)(n-1)(n+4)}{(n+1)^3}
=:L_n.
\]

Also

\[
D_k=H_k-kH_{k-1}=H_k(1-s)>0
\]

because `D_k=k![z^k]FA^4` is a positive forest coefficient. Therefore `0<=s<1`.

For `n>=6`,

\[
G'_n(s)=2(5-n)s+n^2-4n-6.
\]

This is decreasing in `s`, and at `s=1` it equals `n^2-6n+4>0`; hence `G_n` is increasing throughout `[0,1]`. Therefore

\[
G_n(s)\ge G_n(L_n)=\frac{P(n)}{(n+1)^6},
\]

where

\[
P(n)=2n^6+70n^5-33n^4+185n^3+1369n^2-3147n+1170.
\]

Writing `n=t+6`,

\[
P(t+6)=2t^6+142t^5+3147t^4+33233t^3+187651t^2+551661t+666396>0
\]

for every `t>=0`. Thus the disjoint-pair gap is positive for all `n>=6`, and the adjacent-pair gap is larger.

The remaining complete graphs are exact:
`K_2` has no distinct pair;
`K_3`: `(Z,E,J_adj)=(7,3,1)`, gap `2`;
`K_4`: `(38,14,4,5)`, disjoint gap `6`;
`K_5`: `(291,93,23,29)`, disjoint gap `210`.

Hence the unit forest pairwise inequality holds on every `K_n`.

## 6. Independent exact regression

A separate standard-library checker, written for this review rather than copied from the lead, brute-enumerates every edge subset of `K_2,...,K_6`, tests acyclicity by union-find, and compares the direct counts with the Hermite formulas. It then verifies the recurrence reductions, exact rational lower bound, gap identity, shifted polynomial identity, and positive gaps for every `3<=n<=1000`.

Checker SHA-256:
`d5a5bbf76a3a8dcf97291b239b5fb2243d29f09780454689d28d7415427a68b9`

Checker byte count: `2808`.

Captured output SHA-256:
`73adc7e4201349357902f85d0f31363526a53abb104697bebfabbdfa64965f90`

Captured output byte count: `473`.

Captured output:

```text
INDEPENDENT_FOREST_KN_REVIEW
K 2 brute (2, 1, None, None) formula (2, 1, None, None)
K 3 brute (7, 3, 1, None) formula (7, 3, 1, None)
K 4 brute (38, 14, 4, 5) formula (38, 14, 4, 5)
K 5 brute (291, 93, 23, 29) formula (291, 93, 23, 29)
K 6 brute (2932, 822, 178, 226) formula (2932, 822, 178, 226)
range_3_1000_exact_identities=PASS
small_bruteforce=PASS
hermite_gap_formula=PASS
root_bound_numeric_regression=PASS
shift_polynomial=PASS
ALL_INDEPENDENT_REVIEW_CHECKS_PASS
```

The computation is regression evidence only; the all-`n` proof is the symbolic argument above.

## 7. End-to-end conclusion and review gate

Combining Sections 2–5 gives a complete candidate chain:

1. exact Hermite argument proves source unit pairwise negative correlation for every complete graph `K_n`;
2. Cocks's fixed-graph theorem upgrades each `M(K_n)` to independence correlation for all positive weights;
3. Semple–Welsh Proposition 3.5 passes independence correlation to every deletion minor;
4. every finite simple graph is a deletion subgraph of a suitable `K_n`;
5. setting surviving weights to one yields the source inequality for every finite simple graph.

This review found no unhandled graph order, marked-edge orbit, singular/zero-weight step, or theorem-scope mismatch. The reduction uses strictly positive weights only where the external theorem does; deletion itself is obtained by minor closure, not by setting a positive weight equal to zero inside the definition.

Account02/B02 already supplied one independent positive end-to-end review. This account04/B03 report supplies a second independent positive end-to-end review, including a fresh source check, a fresh derivation of all nontrivial coefficient identities, and an independently written exact regression.

Accordingly the lead construction now satisfies the collective protocol's **two-independent-review prerequisite for a FULL_PROOF_CANDIDATE**. Per the same protocol, this does **not** automatically promote the open problem to externally established truth, publication novelty, or owner-approved solved status. The operational parent label remains `OPEN` until the team lead/owner performs the explicit truth-promotion step and any desired external novelty/source review.

No counterexample to the candidate was found.

## 8. Handoff

Status label: **FULL_PROOF_CANDIDATE_REVIEW_2_PASS**.

Essential step applied: the first all-graphs coverage implication is independently proved and source-bound: complete-graph unit pNC plus fixed-graph Cocks plus minor closure covers every finite simple graph.

Candidate refuted: **no**.

Auxiliary only: **no**; this is an end-to-end target-level review.

Novelty: **UNVERIFIED**. This report verifies mathematical correctness of the current candidate chain against the checked sources; it does not claim that the Hermite proof is absent from the literature.

Brain status: **WITHOUT_VERIFIED_BRAIN**. Repository retrieval is not native brain retrieval/context activation.
