# FOREST / fleet02 B01 — separator-sector shortcut refuted; full induced weighting retained

Run: `B01-20260922T0004Z-forest-r11`  
Campaign: `COLLECTIVE-OPEN-PROBLEMS-20260921T234023Z`  
Outcome: **CANDIDATE_REFUTED** for the separator-sector lemma below; finite weighted regression is **AUXILIARY_ONLY**.  
Parent target: **OPEN**.

## 1. Exact target and continuity

The target remains the Grimmett--Winkler/Grimmett uniform-forest pairwise inequality: for every finite simple graph \(G\), with \(F\) uniform over **all** acyclic edge subsets (all sizes, disconnected forests included, unit edge weights), prove for every pair of distinct edges
\[
\Pr(e,f\in F)\le \Pr(e\in F)\Pr(f\in F).
\]
Equivalently, with
\[
\Delta_G(e,f)=Z_eZ_f-ZZ_{ef},
\]
prove \(\Delta_G(e,f)\ge0\).

The current collective lead directory `fleet01/B01` was not yet present at the last pre-write master snapshot used in this run, so there was no complete current lead report to consume. Under the campaign's missing-peer rule I did not wait. I read the exact source/history dependencies needed for this assigned separator/deletion-contraction route.

The main inherited separator facts used here are:

1. The existing P14 two-separator transfer (`proofnet24/P14-probability-correlation/runs/2026-09-16/2026-09-16T16-20-50Z__report.md`) already proves the exact same-side marginal formula. If \(G=A\cup B\) with \(V(A)\cap V(B)=\{u,v\}\), the \(B\)-side does **not** induce a uniform conditional law on \(A\). It induces one virtual \(uv\)-edge of activity \(C_B/D_B\) (or \(1+C_B/D_B\) when the physical separator edge is separately present), and the Rayleigh numerator on \(A\) is multiplied by \(D_B^2\). I therefore do **not** claim that transfer as new work here.
2. The existing P14 three-terminal work (`.../2026-09-16T19-18-17Z__report.md` and `.../2026-09-17T04-40-00Z__report.md`) shows why the first unresolved separator mechanism is genuinely three-terminal: the exact five-state boundary distribution leaves a mixed polarization term which endpoint Rayleigh signs alone do not control.
3. I consumed the current **OTHER-account** result `fleet03/B02`, commit `e5ada175cb0383d4b87fc8243e76790dbc9abb8c`, path
   `proofnet24/P14-probability-correlation/collective-2026-09-22/fleet03/B02/20260921T235733Z-b02-forest-r11/report.md`.
   That result proves the exact deletion--contraction identity
   \[
   AB\,\Delta_G(e,f)=BZ D_0+AZ D_1-\Delta_G(g,e)\Delta_G(g,f)
   \tag{1.1}
   \]
   and hence, in a lexicographically minimal counterexample with violating pair \(e,f\), every third edge \(g\) satisfies
   \[
   \Delta_G(g,e)\Delta_G(g,f)>0.
   \tag{1.2}
   \]
   It also shows that violating pairs form equivalence classes ("bad-pair clusters"), with strict opposite sign from a nontrivial cluster to every external edge.

A useful fleet01/B03 current collective report was also read:
`proofnet24/P14-probability-correlation/collective-2026-09-22/fleet01/B03/20260921T234923Z-b03-poprestore-r11/overlap_reconnection_report.md`.
It gives the exact base-forest identity
\[
\Delta_G(e,f)=n_{10}n_{01}-n_{00}n_{11}+Nq,
\tag{1.3}
\]
where \(q\) is the overlap/reconnection count, equivalently
\[
\Delta_G(e,f)=N^2[\Pr(Q)-\operatorname{Cov}(X,Y)].
\tag{1.4}
\]
Thus the target is exactly the reconnection estimate \(\operatorname{Cov}(X,Y)\le\Pr(Q)\), not the false stronger demand \(\operatorname{Cov}(X,Y)\le0\).

These two other-worker results are compatible: (1.3) identifies the exact slack a universal switching proof may spend, while (1.1)--(1.2) constrain the sign pattern of any genuinely minimal violating graph.

## 2. Compact conditional end-to-end separator route

A separator/deletion--contraction proof would close the target if the following chain could be completed.

1. Blocks and exact two-separator transfer remove 1- and 2-separations while retaining the induced boundary law/weights. This part is already available.
2. In a minimal surviving 3-connected counterexample, apply the fleet03/B02 identity (1.1) to every third edge. Any violating pair must satisfy the global sign-coherence condition (1.2), and the bad pairs must form the reported equivalence classes.
3. At the first genuine 3-terminal interface (notably a degree-three apex / Delta--Y geometry), retain the full five-state boundary-connectivity distribution and prove that its mixed response term is incompatible with that global sign-coherence pattern.
4. The contradiction rules out a minimal counterexample, closing the source target.

The **first tempting implication** in Step 3 is to split a two-terminal or three-terminal boundary distribution into connectivity sectors and ask for Rayleigh nonnegativity inside each sector before mixing. That would make the mixed response term disappear sector-by-sector. This run directly tests and **refutes** that implication in the smallest relevant two-terminal model.

## 3. Exact two-terminal cell formula with the true induced weight

Let \(A\) be a simple graph with two distinguished vertices \(u,v\), with the virtual edge \(h=uv\) absent. Fix two distinct physical edges \(e,f\in E(A)\).

For each occupancy cell \(ij\in\{00,01,10,11\}\), let

- \(d_{ij}\) be the number of forests in that cell in which \(u,v\) are disconnected;
- \(c_{ij}\) be the number of forests in that cell in which \(u,v\) are connected.

If the outside separator network induces virtual-edge activity \(\lambda\ge0\), put
\[
r=1+\lambda\ge1.
\]
After summing the virtual edge, every disconnected forest receives the factor \(r\), while every connected forest receives factor \(1\). Therefore the exact same-side Rayleigh numerator, up to the already-known positive outside factor, is
\[
P(r)=(r d_{10}+c_{10})(r d_{01}+c_{01})
 -(r d_{00}+c_{00})(r d_{11}+c_{11}).
\tag{3.1}
\]
Thus
\[
P(r)=Ar^2+Br+C
\tag{3.2}
\]
with
\[
\begin{aligned}
A&=d_{10}d_{01}-d_{00}d_{11},\\
B&=d_{10}c_{01}+c_{10}d_{01}-d_{00}c_{11}-c_{00}d_{11},\\
C&=c_{10}c_{01}-c_{00}c_{11}.
\end{aligned}
\tag{3.3}
\]

The coefficient \(C\) is exactly the Rayleigh numerator of the **connected-boundary sector alone**. There is no source theorem saying \(C\ge0\), and the next section shows that it can be strictly negative even though the correctly weighted mixture \(P(r)\) is positive throughout the source-realizable range \(r\ge1\).

## 4. Source-valid counterexample to sectorwise conditioning

Take the simple graph
\[
A=K_{2,2}
\]
on vertices \(0,1,2,3\), with terminal pair \(u=0,v=1\) and physical edges
\[
02,\ 03,\ 12,\ 13.
\]
Take
\[
e=02,\qquad f=12.
\]

Exact forest counting, in cell order \(00,01,10,11\), gives
\[
(d_{00},d_{01},d_{10},d_{11})=(3,3,3,0)
\tag{4.1}
\]
and
\[
(c_{00},c_{01},c_{10},c_{11})=(1,1,1,3).
\tag{4.2}
\]
Consequently the connected-boundary sector has
\[
C=c_{10}c_{01}-c_{00}c_{11}=1\cdot1-1\cdot3=-2<0.
\tag{4.3}
\]

So the candidate separator lemma

> "condition on the two boundary vertices being connected; the remaining physical edge indicators are still pairwise negatively correlated"

is **false** already on this four-vertex simple network.

This is **not** a counterexample to the uniform-forest conjecture. The correct induced separator law uses the full mixture (3.1). For this same example,
\[
(A,B,C)=(9,-3,-2),
\]
hence
\[
P(r)=9r^2-3r-2=(3r+1)(3r-2).
\tag{4.4}
\]
On the entire physically relevant range \(r\ge1\),
\[
P(r)\ge P(1)=4>0.
\tag{4.5}
\]
The positive disconnected-sector and mixed contributions are therefore essential. Throwing away the actual boundary distribution destroys the sign even when the true weighted transfer is healthy.

The exhaustive checker described below found no connected-sector failure for graph orders \(n\le3\); the displayed \(K_{2,2}\) instance is the first failure under the checker's deterministic order at \(n=4\). I make no literature-priority claim from that fact.

## 5. Application of the named fleet03/B02 result

The fleet03/B02 sign-cluster theorem might superficially suggest conditioning more finely until every piece has a fixed sign. The \(K_{2,2}\) calculation shows why that is invalid.

In a hypothetical minimal source counterexample, (1.2) constrains the **full** deletion/contraction responses:
\[
\Delta_G(g,e)\Delta_G(g,f)>0
\quad\text{for every third edge }g.
\]
But a separator connectivity sector is not itself the original forest measure of a smaller simple graph, and its internal pair gap can have the wrong sign, as (4.3) proves. Therefore B02's sign coherence cannot be pushed inside the `connected`/`disconnected` sectors separately.

The correct use of B02 in the separator programme is consequently:

> retain the entire induced weighted transfer, then impose the B02 sign-coherence inequalities on the **full response vector** of that transfer.

For a 2-separator this is exactly what the old virtual-edge activity \(C_B/D_B\) achieves and the theorem-dependent all-positive-weight smaller-graph result closes the case. For a 3-terminal interface, the existing five-state transfer and mixed-polarization formula must be handled as a whole. The live missing implication is therefore not "sectorwise Rayleigh"; it is a full three-terminal response-cone inequality strong enough to contradict the B02 bad-cluster sign pattern.

This is a genuine narrowing: one natural separator induction is now conclusively unavailable, while the exact replacement obligation is source-compatible and preserves the boundary weights the assignment requires.

## 6. Exact finite regression

Artifact: `forest_separator_check.py`.

SHA-256:
`0f61286ed1342ee7abca90d6c9ef0b62d46472bd26fc0f2ca92d50b9f3a6f8f0`.

The program exhaustively enumerates every labelled simple \(A\) on at most five vertices, every absent terminal edge \(uv\), and every pair of distinct physical edges \(e,f\). It computes the exact integer cells \(d_{ij},c_{ij}\), forms (3.2), and minimizes the quadratic exactly over \(r\ge1\) using rational arithmetic.

Executed stdout SHA-256:
`219bf77d854a9649a5c627002b26bb247a646ad9e105bef4b82da8ef773461f0`.

Exact output:
```text
FOREST_TWO_SEPARATOR_EXACT_REGRESSION
weighted_instances_checked=46563
instances_by_n={2: 0, 3: 3, 4: 480, 5: 46080}
weighted_failures_r_ge_1=0
first_weighted_failure=None
first_connected_sector_failure=(4, [(0, 2), (0, 3), (1, 2), (1, 3)], (0, 1), (0, 2), (1, 2), [3, 3, 3, 0], [1, 1, 1, 3], (9, -3, -2), -2, (Fraction(4, 1), Fraction(1, 1)))
K22_regression=PASS
all_exact_assertions=PASS
```

The `46563` finite instances and absence of a weighted failure are **AUXILIARY_ONLY**. They neither prove the universal conjecture nor enlarge a certified graph-order baseline. Their role is regression/adversarial checking of the exact transfer formula and the sector counterexample.

## 7. Result status and next mathematical action

**CANDIDATE_REFUTED:** sectorwise boundary conditioning does not preserve pairwise forest negative correlation; the four-vertex \(K_{2,2}\) example gives the exact failure \(C=-2\).

**ESSENTIAL consequence for the assigned proof route:** any valid separator/deletion--contraction argument must retain the actual boundary-connectivity distribution and induced weights. In particular, no proof may replace the full three-terminal mixed response by separate Rayleigh assertions on terminal partition sectors.

**Parent target:** OPEN. No full proof candidate is claimed and no target-level counterexample is claimed.

**Next same-target action:** work directly in the existing five-state three-terminal transfer / degree-three-apex response cone and combine it with fleet03/B02's quantitative identity
\[
\Delta_G(g,e)\Delta_G(g,f)
>
Z(BD_0+AD_1)
\]
for every third edge of a minimal counterexample. The desired next implication is a contradiction between this simultaneous strict sign-coherence and the exact three-terminal mixed response. That is materially different from sectorwise conditioning and preserves all induced weights.

## 8. Scope / provenance / runtime truth

Work was performed `WITHOUT_VERIFIED_BRAIN`: no authenticated native brain retrieval/receiver-context use occurred, and installation is not a prerequisite under the current collective-research control.

Model self-report: `GPT-5.6 Sol`.  
Requested effort: maximum actually supported.  
Configured/known reasoning effort: `UNKNOWN / not exposed`.  
Provider reasoning-token usage: `null / not exposed`.  
Provider thinking-time usage: `null / not exposed`.

Scoped review of the new artifacts found only mathematical definitions, public/repository-relative source references, small graph data, and exact checker output. No credentials, scheduler identifiers, machine paths, unrelated private data/transcripts, benchmark answer material, email/Drive content, public-posting actions, paid API/model calls, remote workflows, or permission changes are included.
