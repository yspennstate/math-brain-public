# FOREST B02 r12 — authoritative source correction and end-to-end candidate

Status: **FULL_PROOF_CANDIDATE / SOURCE_GATE_RESOLVED** for the team candidate. This is an internal mathematical-candidate status, not a public solved-problem or novelty claim. Context: **WITHOUT_VERIFIED_BRAIN**.

This file is a later immutable correction to `report.md` in the same run. It **supersedes only** that report's statements that the fixed-graph Cocks bridge is invalid and that a contraction/cross-term gate remains necessary for the lead chain. The new spectral-mixture theorem (equations (1)–(12) of `report.md`) remains valid and useful, but it is no longer an essential missing gate for the shortest end-to-end proof.

## 1. Why the source-scope correction is necessary

After the initial report was archived, a fresh peer handoff became visible:

- account03/B01 `FOREST-KN-HERMITE-REDUCTION-v1` second independent review, blob `ebc7fb763974ac1d5afea8e4f4c2fc2dc1e403bc`.

It pointed to the **final published Semple–Welsh source**, not the earlier working-paper mechanism. I checked that source directly.

Semple–Welsh, *Negative Correlation in Graphs and Matroids*, final published version, Section 5 Note (printed p. 13), explicitly records that Cocks proved the fixed-graph implication: if Conjecture 1.1 holds for a graph `G`, then `M(G)` is independence correlated. In the same paper, Proposition 3.5 proves that independence-correlated matroids are closed under minors. Their definition of independence correlation quantifies over **all positive real edge weights**.

This is exactly the bridge needed by the lead. The earlier team objection correctly refuted an obsolete/class-level parallel-copy proof mechanism, but it did not refute the later fixed-graph theorem explicitly recorded in the final peer-reviewed source.

Published-source coordinates:
- C. Semple, D. Welsh, *Negative Correlation in Graphs and Matroids*, Combin. Probab. Comput. 17 (2008), 423–435, Proposition 3.5 and Section 5 Note.
- C. Cocks, *Correlated Matroids*, Combin. Probab. Comput. 17 (2008), 511–518, DOI 10.1017/S0963548308009152. Its published abstract says it proves the graphic-matroid equivalences and answers the Semple–Welsh open questions.

## 2. Review gate now satisfied internally

The exact current lead is account01/B01 `FOREST-KN-HERMITE-REDUCTION-v1`, blob `cad5f1b8546f44f200d441b71095a9fde4a20d4b`, with the source chronology reconciliation in blob `032497949594326305913cb8871c00ab7d0dc528`.

Two independent existing-worker end-to-end reviews are now present:

1. account03/B02 `FOREST-KN-COCKS-REDUCTION-v2` review PASS 1, blob `b0a0f97426634919131e37b5a7bad4c4b7f8bb1e`;
2. account03/B01 second independent end-to-end review PASS 2, blob `ebc7fb763974ac1d5afea8e4f4c2fc2dc1e403bc`.

Both review the complete-graph Hermite calculation and the fixed-graph Cocks/minor-closure transfer. My own prior B02 audit had already independently checked the `K_n` formulas/small cases; this invocation independently rechecked the source bridge against the final Semple–Welsh paper and rederived the all-`n` Hermite inequality below.

## 3. Compact end-to-end proof candidate

### Step A: exact reduction from all simple graphs to complete graphs

For any graph `G`, its cycle matroid `M(G)` has independent sets exactly the acyclic edge sets, so Conjecture 1.1 is exactly the user's uniform law on all unrooted forests.

The final Semple–Welsh Note records Cocks's fixed-graph theorem:
\[
\text{unit forest pNC on }G
\quad\Longrightarrow\quad
M(G)\text{ is independence correlated for all positive weights}. \tag{A1}
\]
Semple–Welsh Proposition 3.5 gives
\[
M\text{ independence correlated}\Longrightarrow
\text{every minor of }M\text{ independence correlated}. \tag{A2}
\]
Every finite simple graph `G` on `n` vertices is obtained from `K_n` by deleting nonedges. Hence once the unit forest inequality is proved for every `K_n`, (A1) applied to `K_n`, then (A2), proves it for every simple `G`; setting surviving weights to 1 gives exactly the source law. No contraction/minimal-counterexample gate is needed in this chain.

### Step B: exact complete-graph enumeration

Let `R=R(z)` solve
\[
R=z e^R,
\]
the EGF of rooted labelled trees. Put
\[
T=R-\frac{R^2}{2},\qquad F=e^T,\qquad A=T'=e^R.
\]
Thus `F` is the EGF of labelled forests.

For a fixed edge and the two edge-pair orbits of `K_n`, let:
- `Z_n` = all forests,
- `E_n` = forests containing a fixed edge,
- `J_adj` = forests containing a fixed adjacent edge pair,
- `J_dis` = forests containing a fixed disjoint edge pair.

Deleting the marked edge(s) gives the exact labelled decompositions
\[
Z_n=n![z^n]F, \tag{B1}
\]
\[
E_n=(n-2)![z^{n-2}]FA^2, \tag{B2}
\]
\[
J_{\rm adj}=(n-3)![z^{n-3}]FA^3, \tag{B3}
\]
\[
J_{\rm dis}=(n-4)![z^{n-4}]FA^4
\left(1+\frac4{1-R}\right). \tag{B4}
\]
For (B4), if the two disjoint marked edges lie in different tree components, deletion gives four singly rooted tree components, the `1` term. If they lie in one tree, deleting both edges gives three components; one of the four endpoint pairings is the middle doubly rooted tree. Since
\[
T''=\frac{A^2}{1-R},
\]
summing those four choices gives the extra `4/(1-R)` term.

### Step C: Hermite coefficient extraction

Use the Cauchy substitution `z=u e^{-u}` (`R=u`, `dz=(1-u)e^{-u}du`). For probabilists' Hermite polynomials
\[
e^{xu-u^2/2}=\sum_{j\ge0}He_j(x)\frac{u^j}{j!},
\]
set, at the common point `x=n+1`,
\[
H_j=He_j(n+1),\qquad D_j=H_j-jH_{j-1}.
\]
Then (B1)–(B4) become
\[
Z_n=D_n,\qquad E_n=D_{n-2},\qquad
J_{\rm adj}=D_{n-3}, \tag{C1}
\]
\[
J_{\rm dis}=D_{n-4}+4H_{n-4}
           =J_{\rm adj}+H_{n-4}. \tag{C2}
\]
Therefore the disjoint pair is the harder orbit.

### Step D: all-`n` disjoint inequality

Take `n>=6`, put `k=n-4`, `x=n+1=k+5`, and
\[
s=\frac{kH_{k-1}}{H_k}=\frac{H_k'(x)}{H_k(x)}.
\]
Using the Hermite recurrence `H_{j+1}=xH_j-jH_{j-1}`, direct simplification gives
\[
E_n^2-Z_nJ_{\rm dis}=H_k^2\,G_n(s), \tag{D1}
\]
where
\[
G_n(s)=(5-n)s^2+(n^2-4n-6)s-n^2+9n-14. \tag{D2}
\]

The roots `lambda_i` of `He_k` are the eigenvalues of the standard symmetric Jacobi matrix with off-diagonal entries `sqrt(1),...,sqrt(k-1)`. Its spectrum is symmetric, and
\[
\sum_i\lambda_i^2=\operatorname{tr}(J^2)=k(k-1). \tag{D3}
\]
A direct quadratic-form bound gives `|lambda_i|<=2sqrt(k-1)<x`, so `H_k(x)>0`. Pairing roots `±lambda` and using
\[
\frac1{x-\lambda}+\frac1{x+\lambda}
=\frac{2x}{x^2-\lambda^2}
\ge \frac2x+\frac{2\lambda^2}{x^3}
\]
gives
\[
s=\sum_i\frac1{x-\lambda_i}
\ge \frac{k}{x}+\frac{k(k-1)}{x^3}
=\frac{(n-4)(n-1)(n+4)}{(n+1)^3}
=:L_n. \tag{D4}
\]
Also `D_k=H_k(1-s)>0` because it is the positive forest coefficient `(n-4)![z^{n-4}]FA^4`, so
\[
0<s<1. \tag{D5}
\]

For `n>=6`,
\[
G_n'(s)=2(5-n)s+n^2-4n-6
\ge n^2-6n+4>0
\]
on `[0,1]`, so `G_n(s)>=G_n(L_n)`. Exact simplification yields
\[
(n+1)^6G_n(L_n)
=2n^6+70n^5-33n^4+185n^3+1369n^2-3147n+1170.
\]
Writing `n=t+6`, this is
\[
2t^6+142t^5+3147t^4+33233t^3+
187651t^2+551661t+666396>0. \tag{D6}
\]
Thus `E_n^2-Z_nJ_dis>0` for every `n>=6`; (C2) gives the adjacent inequality as well.

The remaining cases are exact:
- `K_3`: adjacent gap `2`;
- `K_4`: disjoint gap `6` (adjacent gap `44`);
- `K_5`: disjoint gap `210` (adjacent gap `1956`).
Graphs with fewer than two edges are vacuous.

Hence the unit uniform-forest pair inequality holds for every `K_n`.

### Step E: transfer back to every finite simple graph

Combine Step D with Cocks's fixed-graph upgrade (A1) for each `K_n`. Then `M(K_n)` is independence correlated for every positive weighting. By minor closure (A2), deletion of the nonedges preserves independence correlation, so `M(G)` is independence correlated for every finite simple `G`. At unit weights its independent-set measure is exactly the uniform law on all acyclic edge subsets.

Therefore, for every finite simple `G` and every distinct edges `e,f`,
\[
\Pr(e,f\in F)\le\Pr(e\in F)\Pr(f\in F).
\]

## 4. Relation to this run's new spectral theorem

The source-valid ALOV/log-concavity derivation in the original `report.md` is unaffected by the source correction. In particular, for any hypothetical violation whose two `g`-conditioned endpoint laws already have nonpositive marked covariance,
\[
\rho_{ef}\le
\frac{q_g}{q_g+2}\sqrt{q_eq_f},
\]
and at unit weights `rho_ef<=1/3`. Applied to account03/B03's `FOREST-THETA-WEIGHTED-GATE-v1`, it gives the weighted bound `rho_ef(w)<=w/(w+2)`. This remains a reusable quantitative comparison, but it is auxiliary once the fixed-graph Cocks theorem is admitted.

## 5. Scientific authority

Internal campaign status is now **FULL_PROOF_CANDIDATE** because the chain is complete and the required two independent end-to-end review passes are present. This does **not** establish novelty, priority, journal correctness, or permission for public solved-problem claims. The next appropriate action is campaign-lead integration and ordinary expert/source scrutiny, not further unsupported promotion.

No benchmark/installation work was performed. Scheduler inventory note remains unchanged: no account02 managed-slot deficit observed; zero scheduler mutations.
