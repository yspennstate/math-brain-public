Model: GPT-5.6 Sol. Reasoning: UNVERIFIED by runtime metadata; not verified as GPT-6 maximum. **Metric no movement: 15 -> 15.** Section-B methods used: **#1 CHANGE THE CATEGORY, #7 TAKE THE LIMIT, #19 MAKE IT AN ALGORITHM**.

Problem/source: David Aldous and James Fill, *Reversible Markov Chains and Random Walks on Graphs* (unfinished 1994--2002 manuscript / 2014 web compilation), Open Problem 7.30, Section 7.3.3; intake I0030.

# R05 immutable run report — I0030 / spectral-projector criterion and an 8-vertex sharpness witness

Run ID: `20260916T221717Z_i0030_spectral_projector_sharpness`  
Repository/branch: `yspennstate/math-open-problems`, `master`.

Overall source status: **candidate positive answer mathematically PROVED / audit-gated / publication novelty UNVERIFIED**. The frozen finite metric did not move this run because the research effort was deliberately spent on a new structural route rather than another census extension. The previous run moved the metric `14 -> 15`, so the unchanged-run count is now `1`.

## 1. Continuity, repository state, and exact source statement

I continued from the latest authoritative R05 report

`runs/R05/20260916T211813Z_i0030_n15_sharpness.md`

rather than restarting. Before new mathematics I reread/recovered the required campaign controls: `probability_campaign_2026_09/INDEX.md`, `RANKING.md`, root `POSTED.md`, `RESULTS.md`, `QUEUE.md`, `operations/FLEET_2026-09-16.md`, `operations/RFLEET_2026-09-16.md`, and the operative `operations/FOLLOWUP_IMPLEMENTATION_2026-09-16.md`; the newest R04 report `runs/R04/20260916T2127Z_i0027_er_cluster_closure.md`; the newest R06 report `runs/R06/20260916T2121Z_i0079_phase_cancellation_01.md`; and the exact I0030 intake row in `probability_1000_intake_I_20260914/problems.jsonl`.

The original source was rechecked on 2026-09-17 Asia/Jerusalem:

- https://www.stat.berkeley.edu/~aldous/RWG/Book_Ralph/Ch7.S1.html
- https://www.stat.berkeley.edu/~aldous/RWG/Book_Ralph/Ch7.S3.html

Aldous--Fill's terminology in Section 7.1 is important: a *symmetric reversible chain* is a reversible chain whose symmetry group acts transitively on the state space. For unweighted graph random walk this is the vertex-transitive case. Corollary 7.3 says
\[
P_i(X_{2t}=j)\le P_i(X_{2t}=i)
\]
for every `i,j` and discrete `t>=1`, and the source explicitly says the continuous-time analogue holds for all times.

Proposition 7.29 then proves for continuous-time random walk on a **distance-regular** graph, writing
\[
P_v(X_t=w)=q(t,d(v,w)),
\]
that
1. `d -> q(t,d)` is non-increasing for fixed `t`; and
2. for fixed distance `d`,
\[
t\longmapsto q(t,d)/q(t,0)
\]
is non-decreasing.

Immediately afterward Open Problem 7.30 asks verbatim:

> Does random walk on an arc-transitive graph have some monotonicity property stronger than that of Corollary 7.3?

The I0030 intake row records the same statement and locator. Aldous--Fill 7.27 remains a distinct excluded problem and is not used as the target here.

### Frozen R05 statement — unchanged

For every finite simple connected arc-transitive graph `G`, with degree `d`,
\[
P=A/d,\qquad H_t=e^{t(P-I)},
\]
and every arc `x~y`,
\[
\boxed{
r_{xy}(t):=\frac{H_t(x,y)}{H_t(x,x)}
\text{ is strictly increasing for }t\ge0,
\quad r_{xy}(0)=0,\quad r_{xy}(t)\to1.
}
\tag{R05-I0030-C1}
\]

C1 remains mathematically proved in the earlier reports and independently audited by R04 as

`R04-AUDIT-R05-I0030-C1-20260916T130900Z: PASS_MATH / NOVELTY_UNVERIFIED`.

A fresh repository search still found no P26 I0030 audit, so source closure remains **PENDING P26** and no paper folder is created.

Frozen metric:
\[
N_{\rm certified}
=\max\{N:\text{ every source-admissible graph on at most }N
\text{ vertices has the retained complete certificate}\}.
\]
Before `15`; after `15`; unchanged count `1`.

## 2. Idea before code: change category from graph symmetry to local spectral projectors (#1)

The preceding run isolated the exact obstruction away from the source class: regularity makes the **average** neighboring ratio monotone but does not prevent a single neighboring channel from borrowing derivative mass from another. The natural object is therefore not another graph census but the local spectral decomposition at one ordered edge.

Let `G` be any finite connected `d`-regular simple graph. Put
\[
L=I-P=I-A/d.
\]
Let
\[
0=\lambda_0<\lambda_1<\cdots<\lambda_m
\]
be the distinct eigenvalues of `L`, with orthogonal spectral projectors `E_j`. Fix an adjacent ordered pair `x~y` and define
\[
\alpha_j=(E_j)_{xx},\qquad
\beta_j=(E_j)_{xy}.
\]
Since `E_j` is positive semidefinite, `alpha_j>=0`; if `alpha_j=0`, the entire `x` row/column of `E_j` is zero, so `beta_j=0`. On the local support
\[
J_x:=\{j:\alpha_j>0\}
\]
define
\[
\phi_j:=\beta_j/\alpha_j.
\]

Then
\[
H_t(x,x)=a(t)=\sum_{j\in J_x}\alpha_j e^{-\lambda_jt},
\qquad
H_t(x,y)=b(t)=\sum_{j\in J_x}\alpha_j\phi_j e^{-\lambda_jt}.
\]

This turns the graph problem into a signed ordering problem for the scalar list `(lambda_j, phi_j)`.

## 3. R05-I0030-C10 — exact pairwise spectral derivative identity

**STATUS: PROVED.**  
**Quantifiers:** every finite connected `d`-regular simple graph, every ordered adjacent pair `x~y`, every `t>=0`, with the notation in Section 2.

Differentiating `r=b/a` gives
\[
a(t)^2r'_{xy}(t)=b'(t)a(t)-b(t)a'(t).
\]
Expanding both finite exponential sums and pairing `(i,j)` with `(j,i)` yields the exact identity
\[
\boxed{
 r'_{xy}(t)=
 \frac{
 \displaystyle
 \sum_{\substack{i<j\\i,j\in J_x}}
 \alpha_i\alpha_j(\lambda_j-\lambda_i)
 (\phi_i-\phi_j)e^{-(\lambda_i+\lambda_j)t}
 }{
 \left(\displaystyle\sum_{j\in J_x}\alpha_j e^{-\lambda_jt}\right)^2
 }.
}
\tag{C10}
\]

Indeed, the coefficient of `exp(-(lambda_i+lambda_j)t)` from the two ordered terms is
\[
\alpha_i\alpha_j
\{\phi_i(\lambda_j-\lambda_i)+\phi_j(\lambda_i-\lambda_j)\}
=
\alpha_i\alpha_j(\lambda_j-\lambda_i)(\phi_i-\phi_j).
\]
No graph symmetry has been used.

### Immediate sufficient criterion

If
\[
\lambda_i<\lambda_j\quad\Longrightarrow\quad \phi_i\ge\phi_j
\qquad(i,j\in J_x),
\tag{C10.1}
\]
then every summand in C10 is nonnegative, so
\[
r'_{xy}(t)\ge0\quad\text{for all }t\ge0.
\]
If at least one supported pair has strict inequality in (C10.1), then `r'_{xy}(t)>0` for every finite `t`.

Thus one exact way to weaken global arc-transitivity is to ask only for a monotone local spectral-projector ratio along the chosen edge.

## 4. R05-I0030-C11 — local eigenspace edge homogeneity is enough

**STATUS: PROVED.**  
**Quantifiers:** every finite connected `d`-regular simple graph; fixed vertex `x` and neighbor `y`; assume that for every spectral projector `E_j` of `L`, the value `(E_j)_{xz}` is independent of the choice of `z~x`.

Because
\[
P E_j=(1-\lambda_j)E_j,
\]
the `(x,x)` entry gives
\[
\frac1d\sum_{z\sim x}(E_j)_{zx}
=(1-\lambda_j)(E_j)_{xx}.
\]
Under the stated local edge-homogeneity assumption every term in the sum is `beta_j`, hence
\[
\boxed{\beta_j=(1-\lambda_j)\alpha_j,\qquad
\phi_j=1-\lambda_j.}
\tag{C11.1}
\]
Therefore `phi_j` is strictly decreasing in `lambda_j`, and C10 gives
\[
\boxed{r'_{xy}(t)>0\quad\text{for every finite }t.}
\tag{C11.2}
\]

Arc-transitivity implies the hypothesis: the stabilizer of `x` is transitive on its neighbors and every spectral projector commutes with graph automorphisms. Standard 1-walk-regularity also implies the relevant projector entries are homogeneous on edges. Thus C11 recovers the frozen source theorem while identifying a strictly local spectral mechanism.

This is also the eigenspace form of the earlier variance identity. Substituting `phi_j=1-lambda_j` into C10 gives
\[
r'_{xy}(t)=\operatorname{Var}_{\nu_t}(\lambda)>0
\]
for the exponentially tilted local spectral measure.

## 5. Method #7 — take the long-time limit and obtain an exact failure certificate

For a connected regular graph,
\[
E_0=\frac1n\mathbf 1\mathbf 1^T,
\qquad
\alpha_0=\beta_0=1/n,
\qquad
\phi_0=1.
\]
Define
\[
\lambda_*
:=
\min\{\lambda_j>0:\alpha_j>0,\ \phi_j\ne1\}.
\]
Such an eigenvalue exists for `x!=y`, since at `t=0` the ratio is zero rather than one.

### R05-I0030-C12 — eventual sign criterion

**STATUS: PROVED.** Under the hypotheses above,
\[
\boxed{
r_{xy}(t)
=
1+n\alpha_*(\phi_*-1)e^{-\lambda_*t}
+o(e^{-\lambda_*t}),
}
\tag{C12.1}
\]
and hence
\[
\boxed{
r'_{xy}(t)
=
-n\lambda_*\alpha_*(\phi_*-1)e^{-\lambda_*t}
+o(e^{-\lambda_*t}).
}
\tag{C12.2}
\]

Proof: split both `a(t)` and `b(t)` into the stationary term `1/n`, the first local nonstationary term at `lambda_*`, and faster exponentials, then use `(1+u)/(1+v)=1+(u-v)+o(u-v)` at that scale. Differentiating the finite exponential expansion gives (C12.2).

Consequences:
- if `phi_*>1`, the individual adjacent ratio is **strictly decreasing for all sufficiently large t**;
- if `phi_*<1`, it is strictly increasing for all sufficiently large `t`.

This gives a very cheap exact adversarial test: one does not need to locate a finite time at which the derivative changes sign. The first local spectral mode already decides the eventual direction.

## 6. Method #19 — turn the criterion into a one-sided exact algorithm

For a finite graph with algebraic adjacency spectrum, the following is an exact certificate procedure for a chosen edge:

1. compute the distinct eigenvalues of `L` and their algebraic spectral projectors;
2. compute `alpha_j=(E_j)xx`, `beta_j=(E_j)xy`, and `phi_j=beta_j/alpha_j` on the local support;
3. if `phi_j` is non-increasing in `lambda_j`, C10 certifies monotonicity for every time;
4. if the first nonstationary local `phi_*` exceeds `1`, C12 certifies eventual failure.

This is deliberately described as a **one-sided certificate algorithm**, not a complete decision procedure: if the `phi_j` are not ordered and `phi_*<1`, mixed exponential terms can still require additional work.

A rational/algebraic small-graph search using this certificate led to the following exact witness. Only the final witness, not the exploratory scan, is promoted to a proved finite claim.

## 7. R05-I0030-C13 — exact 8-vertex unweighted regular sharpness witness

**STATUS: PROVED exact finite statement.**  
**Scope:** this is explicitly **outside the source arc-transitive class** and therefore does **not** refute Aldous--Fill 7.30.

Let `G_8` be the connected cubic graph on vertices `0,...,7` with graph6 code

`G}GOW[`

and edge set
\[
\{01,02,03,12,13,24,35,46,47,56,57,67\}.
\tag{C13.1}
\]
Take the adjacent ordered pair `(x,y)=(2,0)`.

The exact adjacency characteristic polynomial is
\[
\boxed{
\chi_A(z)=(z-3)(z-1)(z+1)^4(z^2-5).
}
\tag{C13.2}
\]
For the five distinct adjacency eigenvalues
\[
3,\ \sqrt5,\ 1,\ -1,\ -\sqrt5,
\]
the exact local projector data `(alpha,beta,phi)` at `(2,0)` are
\[
\begin{array}{c|c|c|c}
r&\alpha_r&\beta_r&\phi_r\\ \hline
3&1/8&1/8&1\\
\sqrt5&1/8-\sqrt5/40&\sqrt5/20&(1+\sqrt5)/2\\
1&1/4&0&0\\
-1&3/8&-1/8&-1/3\\
-\sqrt5&1/8+\sqrt5/40&-\sqrt5/20&(1-\sqrt5)/2.
\end{array}
\tag{C13.3}
\]

For rate-one SRW, `L=I-A/3`, so the first nonstationary local Laplacian eigenvalue is
\[
\lambda_*=1-\frac{\sqrt5}{3}>0
\]
and its projector ratio is
\[
\phi_*=\frac{1+\sqrt5}{2}>1.
\]
C12 therefore gives the exact asymptotics
\[
\boxed{
r_{20}(t)
=
1+\left(-1+\frac{3\sqrt5}{5}\right)
 e^{-(1-\sqrt5/3)t}
+o(e^{-(1-\sqrt5/3)t}),
}
\tag{C13.4}
\]
with positive leading ratio coefficient, and
\[
\boxed{
r'_{20}(t)
=
\left(2-\frac{14\sqrt5}{15}\right)
 e^{-(1-\sqrt5/3)t}
+o(e^{-(1-\sqrt5/3)t})<0
}
\tag{C13.5}
\]
for every sufficiently large `t`, because `2-14 sqrt(5)/15<0`.

The graph is not edge-transitive, hence not arc-transitive: the common-neighbor count of an edge is an automorphism invariant, but edge `01` has two common neighbors whereas edge `24` has zero; over all edges the values are exactly `{0,1,2}`.

Thus the previous 9-vertex regular counterexample C7 is sharpened to eight vertices. **No minimality claim is made**: the exploratory search was not archived as a complete exact exhaustion of every smaller regular graph for every possible finite-time failure mode.

### Exact finite certificate

Executed checker:
`artifacts/R05/20260916T221717Z_i0030_spectral_projector_sharpness_exact.py`

- create/readback commit: `2c9a93da412d4ef4afe16f379ccdf55b70a2796f`
- readback blob: `b027d0affbd26dcb5d651f3cf12dda927544ba08`
- local pre-upload SHA-256: `3069b2866d7b9b4a1a8846cfd725a03efe99906ae91df1b4bd465c43f6d815ad`

Executed stdout archive:
`artifacts/R05/20260916T221717Z_i0030_spectral_projector_sharpness_exact.out`

- create/readback commit: `f92d40a882f8714e867e5e0f3551415fd5a2307c`
- readback blob: `b7190b3d47c2f435103220d0e474438bfb8e01e2`
- local SHA-256: `1f892d8f3c602bd8e4a2dc82c2554b14cec27ba5ef76d82f87555fd7a25e4bd4`
- process exit code: `0`
- final line: `RESULT PASS`.

The execution environment emitted an unrelated spreadsheet-runtime warmup warning on stderr after the checker had completed; it did not alter the checker stdout or zero exit code.

## 8. Why this matters for the source rather than replacing it

C13 is not a source counterexample. Its role is to identify what the source hypothesis is buying.

The hierarchy now looks like
\[
\text{regular}
\quad\not\Rightarrow\quad
\text{pointwise adjacent monotonicity},
\]
while
\[
\text{local spectral edge homogeneity at }x
\quad\Rightarrow\quad
\phi_j=1-\lambda_j
\quad\Rightarrow\quad
r'_{xy}(t)>0,
\]
and arc-transitivity implies that local homogeneity.

This explains the source answer without invoking distance partitions, distance-regularity, or all-pairs MNHD. It also gives an exact spectral obstruction to weakening the graph symmetry too far.

## 9. Current-status / prior-art search — 2026-09-17 Asia/Jerusalem

The original source page still prints Open Problem 7.30. The bounded current search used combinations of:

- `Aldous Fill Open Problem 7.30 arc-transitive monotonicity`;
- `normalized heat diffusion arc-transitive`;
- `normalized heat diffusion 1-walk-regular`;
- `spectral projector normalized heat diffusion graph`;
- `H_t(x,y) H_t(x,x) graph monotone`;
- `1-walk-regular spectral idempotents edges`;
- `walk-regular spectral idempotent adjacent`.

Relevant primary/current literature recovered:

1. Regev--Shinkar, arXiv:1506.08631 / ECP 2016: a Cayley-graph counterexample to the stronger **all-pairs** MNHD property.
2. Price, arXiv:1612.07306 / ECP 2017: all-pairs MNHD for finite weighted Abelian Cayley graphs.
3. Nica (2020): all-pairs MNHD for graphs with three distinct Laplacian eigenvalues.
4. Kubo--Namba, arXiv:2103.08149 / Graphs and Combinatorics 2022: regular bipartite graphs with four eigenvalues.
5. Liu--Zhang, arXiv:2505.04314 / Graphs and Combinatorics 41 (2025), article 106: distance-regular graphs with classical parameters of diameter three.
6. Godsil--Sun--Zhang, arXiv:2302.03854, current 2025 version: standard 1-walk-regular definition by constancy of diagonal and edge entries of powers of `A`; this is prior art for the structural class, not for the R05 heat-ratio conclusion.

The bounded search did **not** locate a paper explicitly stating C10--C12 or the adjacent-edge arc-transitive theorem C1. That is not a novelty certificate. C10 is an elementary finite-exponential identity, and the earlier log-convexity/decreasing-hazard mechanism is classical. **Publication novelty remains UNVERIFIED.**

## 10. Independent R06 audit — new I0079 phase-cancellation package

Newest R06 package audited:
`runs/R06/20260916T2121Z_i0079_phase_cancellation_01.md`.

R06 has rotated from I0056 and now studies Question 2 in Jardón-Sánchez--Mellick--Poulin--Wróbel, *Exactness and the topology of the space of invariant random equivalence relations*, arXiv:2502.11622 / PLMS 2026: uniqueness of ideal Bernoulli Voronoi tessellations. Its new T1 concerns the frozen marked refinement on equal regular-tree products.

I independently checked the algebraic core of T1. For a fixed finite boundary signature, R06 uses a PPP on `(m,u) in Z x [0,1]` with intensity
\[
\frac cM q^m\,du,\qquad q>1.
\]
The cumulative intensity before `(m,u)` in lexicographic order is indeed
\[
\frac cM\left(\sum_{j<m}q^j+q^m u\right)
=
\frac{c}{M(q-1)}q^m(1+(q-1)u).
\]
Writing `A_c=c/[M(q-1)]`, the cumulative-intensity coordinate
\[
E=A_cq^m(1+(q-1)u)
\]
maps the disjoint strips `m in Z` exactly onto the intervals
\[
[A_cq^m,A_cq^{m+1}),
\]
whose union is `(0,infinity)`, and pushes the PPP to a rate-one PPP. Hence the first `E` is exactly `Exp(1)`. For distinct finite signatures the variables are independent.

Moreover, for integer `r` and `u in[0,1)`, the map
\[
(r,u)\longmapsto q^r(1+(q-1)u)
\]
is strictly order-preserving for lexicographic order because its image for fixed `r` is precisely `[q^r,q^{r+1})`. Therefore R06's winner comparison becomes
\[
\arg\min_\sigma q^{h_\sigma(v)}E_\sigma,
\]
and the common phase factor `c` disappears exactly. I find no mathematical defect in this phase-cancellation core.

Audit verdict:

`R05-AUDIT-R06-I0079-PHASE-CANCELLATION-01-20260916T221717Z: PASS_CORE_MATH / SOURCE-HANDOFF_SCOPED / NOVELTY_UNVERIFIED`.

Scope qualification: I did **not** re-prove the later paper's Theorems 20 and 25 that R06 uses to identify all subsequential boundary intensities/partition limits, so this is not an end-to-end source audit. Current literature also raises a real overlap question: D'Achille--Khezeli, arXiv:2606.30517 (June 2026), advertises graph versions of unique IPVT convergence and independence of a natural parameter `xi` under mild assumptions. A publication claim for R06 therefore needs an exact theorem-to-theorem scope comparison, not merely a negative search.

## 11. Model/scheduler capability and the historical P26 permission issue

The limitation is unchanged in the interface exposed to this worker. Available task controls do not contain a per-task model-family selector or reasoning-effort selector. Therefore the line `GPT-6 / maximum` in task text is a request, not authenticated runtime telemetry.

Actually changing this requires the platform/API or an authorized owner-facing task UI to expose explicit model and reasoning-effort fields, ideally with authenticated run metadata.

Repository history distinguishes two facts about P26:
- `operations/FOLLOWUP_IMPLEMENTATION_2026-09-16.md` records that task ID `6aa7b43682948191b697d72fec69d539` returned `You cannot modify this task` from one R-series context;
- current `RESULTS.md` records that a separate authorized P/C deployment later updated P26 successfully.

Thus the denial is context/permission-specific, not evidence that the task is globally immutable. The legitimate workaround is an authorized owner/admin context with modification rights; no bypass, replacement task, permission change, or scheduler mutation was attempted here.

## 12. Status ledger and next attack

```yaml
ledger_delta:
  worker: R05
  source: "David Aldous and James Fill, Reversible Markov Chains and Random Walks on Graphs (2002/2014), Open Problem 7.30, Section 7.3.3; intake I0030"
  frozen_target: "For every finite simple connected arc-transitive G, P=A/d and H_t=e^{t(P-I)}, H_t(x,y)/H_t(x,x) is strictly increasing for every arc x~y"
  metric: "largest N for which every source-admissible graph on <=N vertices has a retained complete certificate"
  before: 15
  after: 15
  movement: "no movement"
  unchanged_count: 1
  mathematical_status: "PROVED candidate positive source answer; closure audit-gated"
  publication_novelty: "UNVERIFIED"
  tried_methods:
    - "#1 CHANGE THE CATEGORY -> exact spectral-projector derivative identity C10 and local-homogeneity theorem C11"
    - "#7 TAKE THE LIMIT -> exact eventual-sign criterion C12"
    - "#19 MAKE IT AN ALGORITHM -> one-sided spectral certificate; exact 8-vertex regular sharpness witness C13"
  new_claims:
    - "R05-I0030-C10 PROVED: pairwise spectral derivative identity for every finite connected regular graph and adjacent edge"
    - "R05-I0030-C11 PROVED: local eigenspace edge homogeneity implies strict adjacent ratio monotonicity"
    - "R05-I0030-C12 PROVED: first nonstationary local spectral ratio decides eventual derivative sign"
    - "R05-I0030-C13 PROVED: exact 8-vertex cubic graph outside source class has eventually decreasing adjacent ratio"
  exact_evidence:
    - "artifacts/R05/20260916T221717Z_i0030_spectral_projector_sharpness_exact.py @ 2c9a93da412d4ef4afe16f379ccdf55b70a2796f"
    - "artifacts/R05/20260916T221717Z_i0030_spectral_projector_sharpness_exact.out @ f92d40a882f8714e867e5e0f3551415fd5a2307c; RESULT PASS"
  audit_ids:
    R04_to_R05: "R04-AUDIT-R05-I0030-C1-20260916T130900Z: PASS_MATH / NOVELTY_UNVERIFIED"
    P26_to_R05: "PENDING"
    R05_to_R06: "R05-AUDIT-R06-I0079-PHASE-CANCELLATION-01-20260916T221717Z: PASS_CORE_MATH / SOURCE-HANDOFF_SCOPED / NOVELTY_UNVERIFIED"
  remaining_obligation: "P26 end-to-end I0030 audit plus deeper prior-art clearance before source closure/paper packaging"
```

The next R05 run should **not** repeat #1/#7/#19 and should not default to an order-16 census. The most useful next structural question is whether C10's projector-ratio ordering can be characterized by a finite local walk condition weaker than full 1-walk-regularity. Suggested next methods: **#4 PROVE SOMETHING WEAKER COMPLETELY, #13 FIND WHAT ONLY INCREASES, #26 HUNT THE SPORADIC CASE**. In particular, try to determine the least number of local moments
\[
(A^k)_{xy},\quad (A^k)_{xx}
\]
whose edge-homogeneity forces the full projector ordering, or construct an exact source-near counterexample showing that no fixed finite moment order can suffice.
