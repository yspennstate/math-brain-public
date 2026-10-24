Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum.**

# NM13-04 / T07 — exact sign theorem for the complete split graphs `K_3 ∨ \overline{K_n}`

Status: **PARTIAL on the parent problem / CANDIDATE_FULL for the restricted all-parameter class proved below.** The Grimmett–Winkler conjecture for arbitrary finite graphs remains OPEN. No counterexample was found.

Repository/branch: private `yspennstate/math-open-problems` / `master`  
Assigned root: `proofnet24/NM13-04/progress-forest/`  
Companion: NM13-08, `proofnet24/NM13-08/progress-forest-structure/`

## 0. Short transition handoff

The immediately preceding NM13-04 durable state was

`proofnet24/NM13-04/runs/2026-09-19/2026-09-19T23-23-30Z__admission-delta-progress-first-not-assigned-vdh-bhs-released-hard-no-residue3-closable.md`.

That report belonged to the old residue-3 CLOSABLE admission loop, with no admitted mathematical target and successor metric `UNMEASURED`. The later owner policy `operations/PROGRESS20_2026-09-20.md` explicitly supersedes that intake-only loop and maps NM13-04 to T07, uniform-forest sign/deletion–contraction research. I preserve the old screening history but do not count it as T07 progress.

`POSTED.md` was checked. The source conjecture is not listed as a posted/settled result.

## 1. Exact parent problem and current recovered scope

For a finite simple graph `G=(V,E)`, let

\[
I_G(\mathbf y)=\sum_{F\subseteq E:\,F\text{ acyclic}}\prod_{e\in F}y_e.
\]

For distinct edges `e,f`, write

\[
\Delta_G(e,f)=I_e I_f-I_G I_{ef}.
\]

At unit weights, `Delta_G(e,f)>=0` is exactly

\[
\Pr(e,f\in F)\le \Pr(e\in F)\Pr(f\in F)
\]

for a uniformly sampled acyclic spanning edge subset `F` (isolated vertices and all component counts are allowed).

The exact-source/literature check in this run recovered the following scopes.

* Grimmett–Winkler, arXiv `math/0302185` / RSA 24 (2004), verify the conjecture for every graph on at most eight vertices and every nine-vertex graph with at most eighteen edges. They explicitly distinguish this from the already-known uniform-spanning-tree statement.
* Erickson, arXiv `1008.3660`, proves the stronger weighted/I-Rayleigh property for series-parallel graphs via a sum-of-squares identity and records the relevant deletion/contraction and 2-sum closure machinery.
* Historical P14/HARD10 repository work completes the complementary dense nine-vertex sector, so every simple graph on at most nine vertices is certified at unit weights. The preserved source-level complete-order metric is therefore `9`; a source counterexample, if one exists, has at least ten vertices.
* Bado, DOI `10.1016/j.spl.2026.110960`, online in 2026, proves strict pairwise negative edge correlation for all wheel graphs using a `2 x 2` transfer matrix. This is an infinite 3-connected non-series-parallel family, but not the class below.
* Tang–Zhang, arXiv `2603.10738`, proves p-NC for specified uniform spanning-subgraph families of `K_n`, including forests with exactly `k` components for fixed `k` and sufficiently large `n`. That is not the arbitrary-graph, all-component-count measure here.
* Huang, arXiv `2311.00965`, treats negative correlation for arboreal gas on specific graph/parameter regimes and states the general problem remains open.

A bounded 20 September 2026 search for combinations of `uniform forest`, `negative correlation`, `complete split graph`, `K_3 join independent set`, and `K_{3,n}` did not surface the theorem below. That is only bounded negative evidence. **Novelty/priority is UNVERIFIED.**

## 2. P14 continuity: what already worked and what failed

I recovered the full P14 mandatory handoff and the final degree-three blocker before choosing a route.

Preserved successful mechanisms:

1. complete exact source-unit coverage through nine vertices;
2. block/direct-sum factorization, reducing a vertex-minimal counterexample to 2-connected;
3. two-separator transfer, upgrading the minimal-counterexample reduction to 3-connected once the fixed-graph weighted dependency is supplied;
4. exact one-edge-field quadratics, useful as an auxiliary invariant.

Preserved failed or insufficient routes:

1. raw partial ten-vertex enumeration does not move the source metric;
2. generic degree-three star/mesh elimination leaves a mixed three-terminal polarization term for old-edge pairs;
3. that mixed term is not universally nonnegative;
4. the proposed reverse-Cauchy bound on the mixed term is exactly false already in a six-vertex physical graph, although the source Rayleigh gap there remains positive;
5. Lorentzian/complete-log-concavity does not by itself give the needed entrywise Hessian sign;
6. the naive real-stability perturbation and the unverified Garding shortcut do not close the gap.

So I did **not** retry a universal simplicial-apex induction. Instead I restricted the environment enough that the entire three-terminal response can be propagated exactly.

## 3. Three routes compared in this run

### Route A — another 2-sum/deletion–contraction closure

The 2-sum Rayleigh factorization is already known and was already exploited by P14/Cocks/Erickson. Re-proving it would not attack the 3-connected core. **Rejected as non-new.**

### Route B — arbitrary simplicial degree-three vertex

Adding one degree-three vertex whose neighbors span a triangle still produces the same two-environment mixed term isolated by P14. Without extra structure on the rest of the graph, endpoint Rayleigh signs do not control the covariance debt. **Failed for the same precise reason as the historical apex route.**

### Route C — process every degree-three vertex through the full five-state terminal partition chain

For a complete split graph with fixed clique of size three, every non-clique vertex sees the same three terminals. Future cycle legality depends only on the induced partition of those terminals, giving a closed five-state exact transfer. This route succeeds and yields explicit positive Rayleigh numerators for every pair orbit and every `n`.

## 4. New all-parameter theorem

For `n>=1`, define the complete split graph

\[
S_n:=K_3\vee \overline{K_n}.
\]

Thus three clique vertices are pairwise adjacent, the other `n` vertices are independent, and every clique vertex is adjacent to every independent-side vertex.

### Theorem `T07-SPLIT3-SIGN-01`

For every `n>=1`, under the uniform measure on **all forests** of `S_n`, every pair of distinct edges is strictly negatively correlated:

\[
\boxed{\Delta_{S_n}(e,f)>0\qquad(e\ne f).}
\]

The family is genuinely outside the recovered classical scopes: every `S_n` contains `K_4`, so it is not series-parallel; it is 3-connected; for `n>=3` it contains `K_{3,3}` and is nonplanar; and it is neither a wheel nor a complete graph.

## 5. Five-state transfer proof

Let the clique terminals be `1,2,3`, and process the independent-side vertices one at a time. Because the partial edge set is always a forest, when a new independent vertex is joined to a subset `A` of the three terminals, a cycle is created iff two terminals of `A` were already in the same connected component. Hence the only state information needed is the partition of `{1,2,3}`.

Use the state order

\[
D=1|2|3,\quad P_{12}=12|3,\quad P_{13}=13|2,\quad P_{23}=23|1,\quad T=123.
\]

The unmarked one-vertex transfer is

\[
M=
\begin{pmatrix}
4&1&1&1&1\\
0&4&0&0&2\\
0&0&4&0&2\\
0&0&0&4&2\\
0&0&0&0&4
\end{pmatrix}.
\tag{5.1}
\]

The initial triangle `K_3` contributes the state vector

\[
u=(1,1,1,1,3),
\tag{5.2}
\]

because the empty triangle forest gives `D`, each single triangle edge gives one of the three `P` states, and the three two-edge trees give `T`.

Write `N=M-4I`. Direct multiplication gives `N^3=0`, so

\[
M^n=4^n I+n4^{n-1}N+\binom n2 4^{n-2}N^2.
\tag{5.3}
\]

For marked spokes, let `E_i` be the same transfer restricted to legal subsets that contain the spoke from the new vertex to terminal `i`. The matrices needed below are

\[
E_1=
\begin{pmatrix}
1&1&1&0&1\\
0&1&0&0&1\\
0&0&1&0&1\\
0&0&0&1&2\\
0&0&0&0&1
\end{pmatrix},
\]

\[
E_2=
\begin{pmatrix}
1&1&0&1&1\\
0&1&0&0&1\\
0&0&1&0&2\\
0&0&0&1&1\\
0&0&0&0&1
\end{pmatrix},
\]

\[
E_3=
\begin{pmatrix}
1&0&1&1&1\\
0&1&0&0&2\\
0&0&1&0&1\\
0&0&0&1&1\\
0&0&0&0&1
\end{pmatrix},
\]

and if two spokes to terminals `1,2` at the same new vertex are both required,

\[
E_{12}=
\begin{pmatrix}
0&1&0&0&1\\
0&0&0&0&0\\
0&0&0&0&1\\
0&0&0&0&1\\
0&0&0&0&0
\end{pmatrix}.
\tag{5.4}
\]

For a fixed triangle edge, say `12`, the initial marked vector is

\[
w_t=(0,1,0,0,2),
\tag{5.5}
\]

and for two fixed triangle edges `12,13`,

\[
w_{tt}=(0,0,0,0,1).
\tag{5.6}
\]

Let `1` denote the all-ones column vector. Symmetry leaves six edge-pair orbits. Put `Z` for the total number of forests, `Z_t` for a fixed triangle-edge count, `Z_s` for a fixed spoke count, and use the evident pair subscripts. Exact transfer gives

\[
\begin{aligned}
Z&=uM^n\mathbf1,\\
Z_t&=w_tM^n\mathbf1,\\
Z_{tt}&=w_{tt}M^n\mathbf1,\\
Z_s&=uE_1M^{n-1}\mathbf1,\\
Z_{ts}^{\rm inc}&=w_tE_1M^{n-1}\mathbf1,\\
Z_{ts}^{\rm non}&=w_tE_3M^{n-1}\mathbf1,\\
Z_{ss}^{R}&=uE_{12}M^{n-1}\mathbf1,\\
Z_{ss}^{L}&=uE_1E_1M^{n-2}\mathbf1,\\
Z_{ss}^{D}&=uE_1E_2M^{n-2}\mathbf1.
\end{aligned}
\tag{5.7}
\]

Here `R` means same independent-side vertex, `L` means same clique endpoint and two distinct independent-side vertices, and `D` means disjoint endpoints. The last two orbits exist only for `n>=2`.

Substituting (5.3) into (5.7) and multiplying the fixed matrices gives the closed forms

\[
\begin{array}{c|c}
\text{count}&\text{exact value}\\ \hline
Z&4^n(3n^2+37n+112)/16\\
Z_t&4^n(n+6)/2\\
Z_{tt}&4^n\\
Z_s&4^n(3n^2+47n+174)/64\\
Z_{ts}^{\rm inc}&4^n(n+7)/8\\
Z_{ts}^{\rm non}&4^n(n+9)/8\\
Z_{ss}^{R}&4^n(n+7)/8\\
Z_{ss}^{L}&4^n(3n^2+57n+242)/256\\
Z_{ss}^{D}&4^n\,3(n^2+19n+86)/256.
\end{array}
\tag{5.8}
\]

Every pairwise Rayleigh numerator is `Z_e Z_f-ZZ_{ef}`. Using (5.8), the six orbit values are

\[
\Delta_{tt}=\frac{16^n}{16}(n^2+11n+32),
\tag{5.9}
\]

\[
\Delta_{ts}^{\rm inc}=\frac{16^n}{128}(7n^2+85n+260),
\tag{5.10}
\]

\[
\Delta_{ts}^{\rm non}=\frac{16^n}{128}(n^2+11n+36),
\tag{5.11}
\]

\[
\Delta_{ss}^{R}=\frac{16^n}{4096}
(9n^4+186n^3+1397n^2+4484n+5188),
\tag{5.12}
\]

\[
\Delta_{ss}^{L}=\frac{16^n}{2048}(41n^2+509n+1586),
\tag{5.13}
\]

\[
\Delta_{ss}^{D}=\frac{16^n}{2048}(17n^2+213n+690).
\tag{5.14}
\]

All coefficients in every displayed polynomial are positive. Therefore every available orbit has strictly positive Rayleigh numerator for every `n>=1`, proving the theorem. QED.

## 6. Why this is a real new mechanism gain rather than finite enumeration

The theorem holds for arbitrary `n`; the proof is the nilpotent five-state transfer, not a finite census. It also resolves a structured degree-three regime that the P14 generic apex argument could not handle: the crucial difference is that the entire outside environment is itself summarized by the same five terminal partitions, so the mixed response never escapes the finite state space.

This extends the immediately neighboring repository result for `K_{3,n}`. The `K_{3,n}` theorem starts from the pure-disconnected initial vector `(1,0,0,0,0)`. Here the triangle changes the initial response to `(1,1,1,1,3)` and creates three new edge-pair orbits involving clique edges. The formulas (5.9)–(5.14) certify all of them for every parameter value.

## 7. Coordination with NM13-08: transparent-port expansion from unbounded split cores

NM13-08's current T07 report proves the transparent two-terminal substitution identity and exhibits the octahedral gadget

`A = O_6 - g`

with exact terminal counts `D_A=C_A=361`; the completed gadget `O_6=A+g` is I-Rayleigh by Erickson's SOS inheritance. I independently checked the algebraic part used here: when such a unit-transparent gadget replaces an edge `g` of a unit-p-NC core `H`, core-core Rayleigh differences are multiplied by `D_A^2`, gadget-gadget pairs reduce to the weighted completed gadget, and cross pairs factor as two port Rayleigh differences. Hence the sign is preserved.

Combining that sign-preserving substitution with `T07-SPLIT3-SIGN-01` gives a joint new all-parameter class.

### Corollary `T07-SPLIT3-OCTA-EXPANSION-02`

Start from any `S_n=K_3\vee\overline{K_n}`, `n>=1`. Repeatedly choose any current edge and replace it by a fresh copy of `O_6-g`, with arbitrary choices at each step. After any finite number `k>=0` of replacements, the resulting simple graph has pairwise negative edge correlation for the uniform measure on all forests.

Its size is

\[
|V|=n+3+4k,\qquad |E|=3n+3+10k.
\]

This is a strict extension of NM13-08's explicit seed class based on cores with at most nine vertices: for `n>6`, the split core itself already has more than nine vertices, and `k` remains arbitrary. Thus the two companion workers now cover complementary pieces: NM13-08 supplies the sign-preserving decomposition mechanism; this run supplies an unbounded 3-connected seed family to which that mechanism applies.

## 8. Exact checker and executed output

The theorem argument above is symbolic and complete; the checker is a sanity certificate, not the proof for arbitrary `n`.

Checker:

`proofnet24/NM13-04/progress-forest/runs/2026-09-20/2026-09-20T00-20-38Z__split3_checker.py`

created at commit `a28ab4acd4a5e5901698c653dcd047446c15567d`.

Executed output:

`proofnet24/NM13-04/progress-forest/runs/2026-09-20/2026-09-20T00-20-38Z__split3_checker.out`

created at commit `6223a28e165f3896a96b6ef7bb9eaf1cb77065be`.

The checker uses only exact integers. It independently:

1. evaluates the five-state transfer for `1<=n<=12` and matches every closed-form count and Rayleigh polynomial;
2. brute-force enumerates all edge subsets for `n=1,2,3` and checks the transfer counts against direct acyclicity testing;
3. confirms strict positivity of every available pair orbit.

The output ends

`ALL_EXACT_CHECKS_PASS`.

## 9. Parent-problem progress vs mechanism progress

**Parent source problem:** `OPEN -> OPEN`. No arbitrary-graph proof and no counterexample is claimed. The universal complete-order baseline remains `counterexample order >=10`; finite enumeration coverage is unchanged.

**New proved restricted scope:** `none in NM13-04 T07 -> all complete split graphs K_3 ∨ \overline{K_n}, n>=1`, with strict pairwise negative correlation for every distinct edge pair.

**Joint decomposition scope with NM13-08:** cores restricted in its explicit application to order at most nine -> now includes arbitrary `K_3 ∨ \overline{K_n}` cores for all `n`, followed by arbitrary iterated octahedral transparent-port substitutions.

These are theorem-scope gains, not a relabeling of the parent conjecture.

## 10. Residual obstruction and next attack

The surviving universal obstruction is still P14's: a general 3-connected graph has a three-terminal response that need not stay in this nilpotent five-state orbit family, and the mixed polarization can have either sign.

The most direct next nonduplicative attack is to enlarge the solvable terminal core from a triangle to a four-clique. The family `K_4\vee\overline{K_n}` has a 15-state Bell-partition transfer. A successful orbit reduction would test whether the positive sign mechanism persists one treewidth level higher; a failure could produce an exact source-valid counterexample candidate. This is materially different from repeating the generic apex inequality.

## 11. Runtime and access honesty

The scheduler prompt requests GPT-6/maximum, but no authenticated per-run model/effort telemetry is exposed. The actual model family available to this run is GPT-5.6 Sol; reasoning effort is therefore reported as UNVERIFIED. No schedule, workflow, permission, email/Gmail, Drive, public posting, or paid-compute action was taken.

```yaml
ledger_delta:
  worker: NM13-04
  parent: T07_UNIFORM_FOREST_CORRELATION
  source_status_before: OPEN
  source_status_after: OPEN
  source_metric: universal_complete_order_lower_bound_for_counterexample
  source_metric_before: 10
  source_metric_after: 10
  source_metric_note: "P14 proves every graph on <=9 vertices; this run does not extend universal order coverage"
  restricted_theorem_id: T07-SPLIT3-SIGN-01
  restricted_scope_before: NONE_IN_NM13_04_T07
  restricted_scope_after: "all S_n = K_3 join independent_n, n>=1, every distinct edge pair strict p-NC"
  joint_theorem_id: T07-SPLIT3-OCTA-EXPANSION-02
  joint_scope: "all n>=1, all k>=0, arbitrary iterated NM13-08 octahedral transparent-port substitutions from S_n"
  theorem_status: CANDIDATE_FULL_PENDING_LATER_INDEPENDENT_REVIEW
  mathematical_movement: true
  exact_checker: proofnet24/NM13-04/progress-forest/runs/2026-09-20/2026-09-20T00-20-38Z__split3_checker.py
  checker_output: proofnet24/NM13-04/progress-forest/runs/2026-09-20/2026-09-20T00-20-38Z__split3_checker.out
  checker_terminal: ALL_EXACT_CHECKS_PASS
  preserved_P14_failures:
    - generic_degree3_mixed_polarization_uncontrolled
    - universal_mixed_term_nonnegativity_false
    - reverse_Cauchy_route_exactly_refuted
    - Lorentzian_stability_Garding_shortcuts_missing_required_hypothesis
  next_attack: "15-state partition transfer for K_4 join independent_n, with exact sign-or-counterexample search"
  unchanged_substantive_runs: 0
  failed_recovery_routes: 0
  novelty: UNVERIFIED
```
