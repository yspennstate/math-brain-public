Runtime model/effort: **UNVERIFIED**. GPT-6 maximum was requested, but this runtime exposes no authenticated model/effort telemetry or writable model/effort selector, so this report does not claim GPT-6 maximum. **Source status OPEN -> OPEN; source-level structural-family library moves by adding the complete tripartite family `K_{1,2,n}` for every `n>=1`; historical complete-all-graphs order metric remains `9 -> 9`.**

# PROB10-07 — exact Rayleigh theorem for the complete tripartite family `K_{1,2,n}`

Repository/branch: private `yspennstate/math-open-problems` / `master`  
Parent: Grimmett–Winkler pairwise negative edge correlation for the uniform measure on **all forests**  
Status: **PARTIAL / universal conjecture OPEN**  
Artifact stem: `20260920T0340Z_tripartite-k12n-transfer`

## 1. Continuity, scope and nonoverlap

Before committing to this scope I read the controlling owner file `operations/PROB10_2026-09-20.md`, current `POSTED.md`, the complete newest P14 handoff

`proofnet24/P14-probability-correlation/runs/2026-09-17/2026-09-17T05-19-47Z__mandatory-handoff-report.md`,

the complete newest HARD10-01 forest handoff

`proofnet24/HARD10-01/runs/2026-09-16/2026-09-16T21-16-42Z__report.md`,

the newest own PROB10-07 report

`runs/prob10_2026-09-20/PROB10-07/20260920T0255Z_integer-partition-quotient-k30-c3f8.md`,

and current same-parent follow-ups, including NM13-04's newest transparent-gadget / decorated-biclique report

`proofnet24/NM13-04/progress-forest/runs/2026-09-20/2026-09-20T03-18-30Z__split5-q2-transparent-neutralizer.md`.

P14/HARD10-01 retain the all-graphs order census through nine, the vertex-minimal 3-connected reduction, and the generic three-terminal obstruction. NM13-04/NM13-08 own split-join / port-field / transparent-substitution directions. The present result is a different fixed-core transfer family: complete tripartite `K_{1,2,n}`. It neither repeats graph-order enumeration nor uses the decorated-biclique substitution theorem.

Continuity pointers are preserved at

- `runs/R13/20260919T2345Z_handoff-to-PROB10-07-forest.md`;
- `artifacts/prob10_2026-09-20/PROB10-07/20260919T2347Z_forest-owner-handoff.md`.

This run also writes the non-mutating owner-chain delta

`artifacts/prob10_2026-09-20/PROB10-07/20260920T0340Z_tripartite-k12n-forest-owner-handoff.md`.

## 2. Exact source target and before/after metrics

For a finite graph `G=(V,E)`, let `F` be chosen uniformly from all acyclic subsets of `E`, retaining the full vertex set and allowing every component count. For distinct edges `e,f`, put

\[
Z=|\mathcal F(G)|,\qquad Z_e=|\{F:e\in F\}|,\qquad Z_{ef}=|\{F:e,f\in F\}|.
\]

Then

\[
\Pr(e)\Pr(f)-\Pr(e,f)=\frac{Z_eZ_f-ZZ_{ef}}{Z^2}.
\tag{2.1}
\]

Thus the source inequality is exactly the Rayleigh sign

\[
\Delta_G(e,f):=Z_eZ_f-ZZ_{ef}\ge0.
\tag{2.2}
\]

The preceding PROB10-07 report proved every complete bipartite `K_{a,b}` with `min(a,b)<=30`. That remains intact.

### New theorem `PROB10-07-K12N-TRIPARTITE`

For every integer `n>=1`, the uniform measure on all forests of the complete tripartite graph

\[
G_n=K_{1,2,n}
\]

satisfies

\[
\boxed{\Delta_{G_n}(e,f)>0\quad\text{for every distinct edge pair }e,f.}
\tag{2.3}
\]

Hence every distinct edge pair is **strictly negatively correlated**.

This is a genuinely non-series-parallel infinite family for `n>=2`. Write the parts as

\[
A=\{a\},\qquad B=\{b,c\},\qquad C=\{r_1,\ldots,r_n\}.
\]

For `n>=2`, the connected branch sets

\[
\{a\},\quad\{b\},\quad\{r_1\},\quad\{c,r_2\}
\]

are pairwise adjacent, giving a `K_4` minor. Therefore Erickson's series-parallel theorem does not subsume this family.

**Source status:** `OPEN -> OPEN`.  
**Complete-all-graphs order metric:** `9 -> 9`.  
**Structural family library:** adds all `K_{1,2,n}`, `n>=1`, on top of the preceding biclique range.  
**Novelty/priority:** **UNVERIFIED** after bounded repository and public-source searches; no priority claim is made.

## 3. Three materially different approaches compared

The mathematical idea was written before production code in

`artifacts/prob10_2026-09-20/PROB10-07/20260920T0340Z_tripartite-k12n-transfer-idea.md`,

creation commit `f96afd590089687e8dcde61dd738b7d030e28a3d`.

### A. General false-twin closure — not closed

Complete bipartite and complete multipartite families suggest cloning a vertex with the same neighborhood. A theorem saying unit forest-Rayleigh is preserved by arbitrary false-twin extension would be much stronger. However the forest decomposition after cloning depends on the full connectivity pattern induced on the old neighborhood, not on a scalar Rayleigh gap. I found no deletion-contraction identity that closes on the source invariant alone, so this route is not promoted.

### B. Component-species / Tutte expansion — exact but sign-hidden

A connected bipartite component with `s` left and `t` right vertices has `s^{t-1}t^{s-1}` spanning trees, so all forests of a complete bipartite graph admit an exact labelled-component exponential formula. Marked-edge forcing can likewise be decomposed according to whether the two marked edges lie in one or two tree components. The resulting coefficient identity is exact, but the Rayleigh sign becomes an alternating coefficient inequality with no current total-positivity theorem. This remains a possible all-width route, not a theorem of this run.

### C. Fixed-core partition transfer — succeeds

For `K_{1,2,n}`, the nontrivial fixed core consists of edges `ab,ac`, while every variable vertex `r_i` is an identical three-spoke star. The connectivity partition of the three fixed terminals is therefore a complete finite state. This yields the theorem below.

## 4. Five-state exact transfer

Process the fixed core first and then the `C` vertices one by one. At any stage the chosen edges form a forest, and their restriction induces one of the five labelled terminal partitions

\[
\pi_0=a|b|c,\quad
\pi_1=a|bc,\quad
\pi_2=ab|c,\quad
\pi_3=abc,\quad
\pi_4=ac|b.
\tag{4.1}
\]

For a new vertex `r`, choose a neighbor set `S subseteq {a,b,c}`. The new star is acyclic **iff** `S` meets each current connectivity block at most once.

Indeed, if two vertices of `S` already lie in one block, the old path between them together with the two new spokes through `r` makes a cycle. Conversely, if `S` meets distinct blocks, the new vertex joins distinct tree components by a star and cannot create a cycle.

Counting the legal neighbor sets from each state gives, in the order (4.1),

\[
M=
\begin{pmatrix}
4&1&1&1&1\\
0&4&0&2&0\\
0&0&4&2&0\\
0&0&0&4&0\\
0&0&0&2&4
\end{pmatrix}.
\tag{4.2}
\]

For example, from `a|b|c`, the empty set and three singleton stars preserve the state, the three two-spoke stars make the three pair partitions, and the three-spoke star makes `abc`. From `a|bc`, the four empty/singleton choices preserve the state, while `ab` or `ac` joins the two blocks and gives `abc`.

Write

\[
M=4I+N.
\]

Every nonzero transition of `N` strictly decreases the number of terminal blocks, so

\[
N^3=0.
\tag{4.3}
\]

Hence for every integer `x>=0`,

\[
\boxed{
M^x=4^x\left(I+\frac{x}{4}N+\frac{x(x-1)}{32}N^2\right).
}
\tag{4.4}
\]

Thus every aligned marked count is `4^x` times a quadratic polynomial in `x`.

## 5. Ten edge-pair orbits and exact marked vectors

There are three edge types under `S_2 x S_n`:

- `X`: core edge, represented by `ab`;
- `Y`: edge `a r_i`;
- `Z`: edge `b r_i` or `c r_i`.

Every distinct pair lies in exactly one of the following ten orbits:

`XX, YY, ZZ-B, ZZ-C, ZZ-D, XY, XZ-B, XZ-D, YZ-C, YZ-D`,

where `B` means a shared `B` endpoint, `C` a shared variable vertex, and `D` disjoint endpoints.

For an orbit, first process the minimum number `k=0,1,2` of distinguished variable vertices needed to realize it. Let

\[
v_0,v_e,v_f,v_{ef}
\]

be the row vectors counting legal choices of the two core edges and those `k` distinguished stars, respectively with no forced edge, only `e`, only `f`, or both forced. In the state order (4.1), direct finite enumeration gives:

| orbit | `k` | `v0` | `ve` | `vf` | `vef` |
|---|---:|---|---|---|---|
| XX | 0 | (1,0,1,1,1) | (0,0,1,1,0) | (0,0,0,1,1) | (0,0,0,1,0) |
| YY | 2 | (16,8,24,62,24) | (4,1,9,25,9) | (4,1,9,25,9) | (1,0,3,9,3) |
| ZZ-B | 2 | (16,8,24,62,24) | (4,5,9,29,5) | (4,5,9,29,5) | (1,2,3,11,1) |
| ZZ-C | 1 | (4,1,5,9,5) | (1,1,2,5,1) | (1,1,1,5,2) | (0,1,0,3,0) |
| ZZ-D | 2 | (16,8,24,62,24) | (4,5,9,29,5) | (4,5,5,29,9) | (1,2,2,12,2) |
| XY | 1 | (4,1,5,9,5) | (0,0,4,6,0) | (1,0,2,4,2) | (0,0,1,2,0) |
| XZ-B | 1 | (4,1,5,9,5) | (0,0,4,6,0) | (1,1,2,5,1) | (0,0,1,2,0) |
| XZ-D | 1 | (4,1,5,9,5) | (0,0,4,6,0) | (1,1,1,5,2) | (0,0,1,3,0) |
| YZ-C | 1 | (4,1,5,9,5) | (1,0,2,4,2) | (1,1,2,5,1) | (0,0,1,2,0) |
| YZ-D | 2 | (16,8,24,62,24) | (4,1,9,25,9) | (4,5,9,29,5) | (1,1,3,11,2) |

These vectors are not a numerical fit: each is obtained by enumerating only the four core subsets and at most `8^2` distinguished-star subsets under the legality criterion of §4. The checker reconstructs them from first principles rather than hard-coding them as assumptions.

Put

\[
x=n-k.
\]

For the physical pair orbit, `x>=0`; for `XX`, `k=0` and `n>=1`, so `x>=1`. The four exact forest counts are

\[
Z=v_0M^x\mathbf1,\quad
Z_e=v_eM^x\mathbf1,\quad
Z_f=v_fM^x\mathbf1,\quad
Z_{ef}=v_{ef}M^x\mathbf1.
\tag{5.1}
\]

## 6. Manifestly positive Rayleigh polynomials

Using (4.4) in (5.1), define

\[
P_Q(x)=16^{-x}\Delta_Q.
\]

Exact rational expansion gives:

\[
P_{XX}(x)=\frac{x(x+3)}{16}.
\tag{6.1}
\]

For the remaining nine orbits:

\[
P_{YY}(x)=\frac{1280+457x+41x^2}{8},
\]

\[
P_{ZZ-B}(x)=\frac{2336+617x+41x^2}{8},
\]

\[
P_{ZZ-C}(x)=\frac{1024+2368x+1097x^2+174x^3+9x^4}{256},
\]

\[
P_{ZZ-D}(x)=\frac{1264+289x+17x^2}{8},
\]

\[
P_{XY}(x)=\frac{144+63x+7x^2}{8},
\]

\[
P_{XZ-B}(x)=\frac{224+79x+7x^2}{8},
\]

\[
P_{XZ-D}(x)=\frac{32+9x+x^2}{8},
\]

\[
P_{YZ-C}(x)=\frac{4608+3888x+1241x^2+174x^3+9x^4}{256},
\]

\[
P_{YZ-D}(x)=\frac{672+209x+17x^2}{8}.
\tag{6.2}
\]

Every coefficient in (6.2) is strictly positive. Therefore those nine Rayleigh numerators are positive for every physical `x>=0`. Equation (6.1) is positive for every physical `x=n>=1`. These ten orbits exhaust all distinct edge pairs, proving (2.3).

This is a complete proof for every `n>=1`, not a finite-order graph check.

## 7. Exact checker and falsification checks

Production checker:

`artifacts/prob10_2026-09-20/PROB10-07/20260920T0340Z_tripartite-k12n-transfer_checker.py`

creation commit `8590623ba2da4e8ead3efef74d68ca11f3cf1050`; read back at that exact commit, blob `d87a841a8eb7ccc7abcbf83ed5f4310fef90ea2d`.

The checker independently:

1. reconstructs the five-state transfer matrix from the acyclicity rule;
2. verifies `N^3=0`;
3. reconstructs every marked initial vector by direct enumeration;
4. derives all ten exact `Fraction` Rayleigh polynomials;
5. requires the exact coefficients displayed in §6;
6. brute-force enumerates the **original all-forests model** for `n=1,2,3`, checking every actual edge pair against the symbolic orbit formula.

The brute-force regressions recover

\[
Z(G_1)=24,\qquad Z(G_2)=134,\qquad Z(G_3)=712
\]

and match all `10`, `28`, and `55` edge pairs respectively.

Archived executed output:

`artifacts/prob10_2026-09-20/PROB10-07/20260920T0340Z_tripartite-k12n-transfer_checker.out`

creation/readback commit `793ea6ec96da400b291352ac376ffc65937acd80`, blob `beeb8e38e8f052e347a54f07b42a9672fdf90548`.

It ends

`PROB10_07_K12N_TRIPARTITE_EXACT_PASS`.

This is a self-check, not an independent audit.

## 8. Current-source and prior-art reconciliation

The source remains Grimmett–Winkler, arXiv `math/0302185` / *Random Structures & Algorithms* 24 (2004): uniform over all forests, arbitrary component count. Erickson, arXiv `1008.3660`, proves the stronger weighted Rayleigh property for series-parallel graphs. Tang–Zhang, arXiv `2603.10738`, concern specified complete-graph ensembles including fixed-component forests and do not imply this theorem. Bado's 2026 wheel result is another infinite 3-connected non-series-parallel family, but not this complete-tripartite family.

A bounded current search for combinations of `K_{1,2,n}`, `complete tripartite`, `uniform forest`, `negative edge correlation`, and `Rayleigh` did not locate this exact theorem or these formulas. The repository search likewise found no pre-existing `K_{1,2,n}` forest claim. This is negative evidence only: **novelty remains UNVERIFIED**.

The owner's random-cluster parameter-nonmonotonicity paper is a different statement and is not used as source closure here.

## 9. What moved and what did not

### Source-level movement

A new all-parameter graph class is proved:

\[
\boxed{K_{1,2,n}\text{ for every }n\ge1.}
\]

For `n>=2` this is outside the known series-parallel class by the explicit `K_4` minor above.

### Auxiliary/mechanism movement

The terminal-partition transfer is shown to tolerate a nonempty fixed core, not only the empty-side core used for complete bipartite graphs. This suggests a larger fixed-core-plus-twins program, e.g. other complete multipartite families, but no such general closure is claimed.

### No movement

The universal arbitrary-graph conjecture remains OPEN/PARTIAL. The complete-all-graphs order metric remains 9. There is no counterexample. No independent audit has yet been recorded for the new theorem.

## 10. Remaining full-scope gap and next mathematically distinct directions

The full source still requires either a proof for every finite graph or an exact source-valid counterexample. Three promising next directions, distinct from merely increasing the biclique width, are:

1. determine whether the fixed-core transfer can prove an all-`n` theorem for `K_{1,3,n}` or `K_{2,2,n}`, where the state space is still finite but the core is richer;
2. isolate a genuine false-twin extension theorem with the full terminal-connectivity response as the invariant rather than a scalar Rayleigh gap;
3. return to deletion-contraction and seek a closure identity for a bounded-rank terminal response class that contains both the bicliques and `K_{1,2,n}`.

A next run should not simply tune or rerun the same ten polynomials.

## 11. Ledger delta

```yaml
ledger_delta:
  track: PROB10-07
  source: "Grimmett-Winkler uniform all-forests pairwise edge negative correlation"
  source_status_before: OPEN
  source_status_after: OPEN
  all_graph_order_metric_before: 9
  all_graph_order_metric_after: 9
  structural_family_before: "all K_{a,b} with min(a,b)<=30"
  structural_family_after: "preceding biclique family plus all complete tripartite K_{1,2,n}, n>=1"
  new_theorem: "strict pairwise negative edge correlation on K_{1,2,n} for every n>=1"
  non_series_parallel_range: "n>=2"
  exact_self_check: PASS
  independent_audits: 0
  novelty: UNVERIFIED
  status: PARTIAL
```

No scheduler, cadence, enabled state, email, Drive, public-posting, workflow, peer-claim, or permission state was changed.
