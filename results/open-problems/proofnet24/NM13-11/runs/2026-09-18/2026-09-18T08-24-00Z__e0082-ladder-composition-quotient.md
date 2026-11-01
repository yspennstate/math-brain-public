Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. NO FROZEN-METRIC MOVEMENT: `gamma_FP = 1 -> 1`; status `PARTIAL`. Section-B methods actually tried: #14 FIND THE GROUP ACTING, #16 COMPUTE EVERY SMALL CASE, #18 SAY IT IN ANOTHER LANGUAGE.**

# NM13-11 — E0082 exact ladder-composition quotient of the first-passage matching matrix

Date: 2026-09-18 UTC  
Repository / branch: `yspennstate/math-open-problems` / `master`  
Track: `NM13-11`  
Category: `HARD OUTSIDE`  
Canonical source / claim: `E0082` / `operations/claims/E0082.md`  
Canonical dedup key: `pitman_tang::op_2_3`  
Canonical SHA-256 / shard: `1b4de7c58dbd8e94a7bc807a11a84c8e166fceea6c48cb804038b2f998e7228a`, residue `10 mod 13`

## 1. Runtime, control surface, and continuity

The prompt requests `GPT-6 / maximum`. That is **not** the model this invocation can honestly report. The actual model is **GPT-5.6 Sol**; authenticated reasoning-effort telemetry is not exposed, so the reasoning level is **UNVERIFIED**. I do not claim GPT-6 or maximum reasoning.

The task-control surface available to this worker still exposes task title/prompt, schedule or relative start, timing mode, enabled state, and ordinary task update fields. It still exposes **no bindable model-family selector and no bindable reasoning-effort selector**. Making `GPT-6 / maximum` binding would require an owner-authorized product/workspace/API/admin surface that exposes those settings plus authenticated per-run model/reasoning attestation. The historical P26 `You cannot modify this task` response was context-specific: current `RESULTS.md` records that a later P26 full update succeeded from a different authorized context. The lawful workaround for a denied task is therefore the owning/otherwise-authorized context or platform/admin support, not cloning the schedule or bypassing access control. This invocation did not create, modify, disable, or duplicate any schedule and does not claim a support escalation.

Before mathematics I reread or targeted-search-recovered the required current state:

- `FLEET_RULES.md`;
- `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md`;
- `operations/NEW_METHODS_2026-09-16.md`;
- later owner-authorized amendment `operations/NM13_DEPLOYMENT_2026-09-17T203709Z.md`;
- root `QUEUE.md`, `POSTED.md`, `RESULTS.md`;
- `probability_campaign_2026_09/INDEX.md` and `RANKING.md`;
- canonical claim `operations/claims/E0082.md`;
- newest own report `proofnet24/NM13-11/runs/2026-09-18/2026-09-18T07-15-57Z__e0082-row-extremal-dual-lp.md`;
- newest neighboring NM13-12 report `proofnet24/NM13-12/runs/2026-09-18/2026-09-18T07-51-25Z__e0086-potential-kernel-hazard-upper-bound.md` and the current neighboring-track inventory;
- the E-intake source row, canonical alias material, and substantive prior attempt `E0082-A001`;
- current/historical claim and audit searches.

Pre-write `master` was observed at `db414f222de698e12993db82759e1ed71da96305`. No release, duplicate ownership, retirement, POSTED closure, or source-status correction displaced E0082. P26 audit: **NOT PASSED / not recovered**. NM13-12 audit: **NOT PASSED / not recovered**. The prior attempt `E0082-A001` identified the full matching/correlation system and nonuniform first-hit weights as the obstruction; it did not contain the quotient theorem below.

The preceding E0082 run had frozen

\[
\gamma_{FP}:=\inf\{\gamma:\mathbb ET(\mathcal{FP}^{-1,n})=O(n^\gamma)\}=1
\]

and then showed that the worst matching-matrix row really is logarithmic, so a uniform row certificate cannot remove the residual log. Its methods were #11/#13/#24. The admission run used #2/#4/#8. I do not repeat either triple here.

## 2. Source and literature check — 2026-09-18

The exact source remains Jim Pitman and Wenpin Tang, *Patterns in Random Walks and Brownian Motion* (arXiv:1411.0041; Springer LNM 2137). Section 2.5 of the accessible PDF still identifies the exponent gap for first-passage patterns, says that the exact computation is the sum of all entries of the inverse matching matrix, and records Yuval Peres's conjecture that for fixed `lambda<0`,

\[
c_\lambda n\log n\le \mathbb ET(\mathcal{FP}^{\lambda,n})\le C_\lambda n\log n.
\]

The PDF version labels the Section 2.5 source question as `Open Problem 1`; the repository's canonical intake locator uses `Open problem 2.3 / Section 2.5`. This is a locator/version convention, not a different source problem.

Dated bounded queries included the exact title together with `first passage`, `matching matrix`, `Dyck`, `Catalan`, `weak composition`, `n log n`, and `Peres`, plus the authors' names. They recovered the original paper and a Berkeley eScholarship thesis treatment that repeats the same inverse-matrix difficulty and Peres conjecture. I did **not** locate a later source-matching resolution or a published ladder-composition quotient matching the theorem below. Search-engine coverage, citation indexing, and full-text access are incomplete, so this is bounded negative evidence only. **Publication novelty remains UNVERIFIED**; the equitable-partition mechanism could be folklore in pattern-matching or Catalan combinatorics.

Primary/source URLs checked:

- `https://www.columbia.edu/~wt2319/Patterns.pdf`
- `https://arxiv.org/abs/1411.0041`
- `https://escholarship.org/content/qt51j6244c/qt51j6244c.pdf`

## 3. New idea before code: quotient by descending-ladder block lengths

The preceding run said the correct object is the positive packing/covering LP for the full matching matrix `M`, but that matrix has exponentially many rows. The new question was whether the first-passage constraint itself supplies an exact symmetry quotient before any asymptotics.

It does.

Fix integers `m>=1`, `n>=m` of the same parity and let

\[
\mathcal F_{m,n}:=\{A\in\{\pm1\}^n:S_j(A)>-m\ (j<n),\ S_n(A)=-m\}.
\]

This is the exact first-passage pattern family to level `-m`; for the source subsequence `lambda=-1`, `n=m^2`, it is precisely `\mathcal{FP}^{-1,m^2}`.

For `A in F_{m,n}`, let

\[
\tau_j(A):=\min\{t:S_t(A)=-j\},\qquad \tau_0=0.
\]

Between `tau_{j-1}` and `tau_j`, after translating the current minimum to zero, the path stays nonnegative and first reaches `-1` on its final step. Therefore the segment has a unique form

\[
D_j\,-,
\]

where `D_j` is a Dyck word of even length `2r_j`. Consequently every first-passage word has a unique factorization

\[
\boxed{A=D_1-\,D_2-\cdots D_m-} \tag{3.1}
\]

with

\[
r(A)=(r_1,\ldots,r_m),\qquad r_j\ge0,\qquad
\sum_{j=1}^m r_j=N:=\frac{n-m}{2}. \tag{3.2}
\]

Thus the exponentially large family splits into classes `C_r` indexed by weak compositions `r` of `N` into `m` parts. Their sizes are exactly

\[
\boxed{c_r:=|\mathcal C_r|=\prod_{j=1}^m C_{r_j}},\qquad
C_a=\frac1{a+1}{2a\choose a}. \tag{3.3}
\]

The number of classes is only

\[
\boxed{Q_{m,n}={N+m-1\choose m-1}}. \tag{3.4}
\]

For `n=m^2`, this is

\[
Q_{m,m^2}={\frac{(m-1)(m+2)}2\choose m-1}
=\exp(O(m\log m))
=\exp(O(\sqrt n\log n)), \tag{3.5}
\]

subexponential in `n`, whereas `|F_{m,n}|` is exponential.

## 4. Exact equitable-partition theorem for the matching matrix

Use the source's matching convention

\[
M_{A,B}
=\sum_{\ell=0}^{n-1}2^{-\ell}
\mathbf 1\{A_1\cdots A_{n-\ell}=B_{\ell+1}\cdots B_n\}. \tag{4.1}
\]

For weak compositions `r,s` of `N`, define provisionally

\[
K_{r,s}(A):=\sum_{B\in\mathcal C_s}M_{A,B},\qquad A\in\mathcal C_r. \tag{4.2}
\]

### Theorem 1 — exact ladder-composition lumping

`K_{r,s}(A)` is independent of the internal Dyck shapes of `A`; it depends only on `r` and `s`. Hence we may write it simply as `K_{r,s}`. Equivalently, the subspace of vectors constant on every ladder-composition class is exactly invariant under `M`.

More explicitly, put

\[
R_j:=r_1+\cdots+r_j,\qquad \tau_j(r)=2R_j+j, \tag{4.3}
\]

and define the ballot/meander number

\[
B(t,e):=
\begin{cases}
{t\choose (t+e)/2}-{t\choose (t+e)/2+1},
& t\ge e\ge0,\ t\equiv e\pmod2,\\
0,&\text{otherwise.}
\end{cases} \tag{4.4}
\]

For `1<=d<=m-1`, `0<=e<=d-1`, set

\[
k=m-d+e,\qquad
t_{d,e}=2(s_{k+1}-R_{e+1})-e. \tag{4.5}
\]

Then

\[
\boxed{
\begin{aligned}
K_{r,s}
={}&\mathbf1_{\{r=s\}}\\
&+\sum_{d=1}^{m-1}2^{-(n-\tau_d(r))}
\sum_{e=0}^{d-1}
\mathbf1_{\{(s_{k+2},\ldots,s_m)=(r_{e+2},\ldots,r_d)\}}
\left(\prod_{j=1}^{k}C_{s_j}\right)
B(t_{d,e},e),
\end{aligned}} \tag{4.6}
\]

where `k=m-d+e` inside the inner sum and empty tails/products have their usual meanings.

### Proof

The `ell=0` overlap in (4.1) contributes exactly `1_{r=s}` after summing over `B in C_s`, because it requires `A=B`.

Now fix a nontrivial overlap `ell>0` and let `L=n-ell`. Write

\[
W=A_1\cdots A_L=B_{\ell+1}\cdots B_n. \tag{4.7}
\]

Since `B` first reaches `-m` at time `n`, `S_B(ell)>-m`. Thus the suffix `W` has total sum `-d` for some `1<=d<=m-1`. Moreover `W` must first hit `-d` at its own last step: if an earlier prefix of `W` hit `-d`, then `B` would hit `-m` before time `n`. But `W` is also a prefix of `A`, so

\[
L=\tau_d(A)=2R_d+d. \tag{4.8}
\]

Therefore nontrivial overlaps are possible only at source descending-ladder times, and their matching weight is exactly

\[
2^{-\ell}=2^{-(n-\tau_d(r))}. \tag{4.9}
\]

At the cut time `ell`, the target path `B` is at level `-(m-d)`. Suppose it has already completed `k` descending ladder blocks, so its running minimum is `-k`. Necessarily

\[
k=m-d+e,\qquad 0\le e\le d-1, \tag{4.10}
\]

and the partial target block after that minimum is a nonnegative meander `Q` ending at height `e`.

Starting from height `e`, the first `e` source ladder blocks in `W` descend back to the current target minimum without crossing it. The `(e+1)`st source ladder block creates the next new target minimum. Thereafter the remaining source blocks are exactly the remaining target ladder blocks. Consequently a target of composition `s` exists for this `(d,e)` only if

\[
(s_{k+2},\ldots,s_m)=(r_{e+2},\ldots,r_d). \tag{4.11}
\]

The first `k` target Dyck blocks are arbitrary, giving

\[
\prod_{j=1}^k C_{s_j} \tag{4.12}
\]

choices. The unfinished target Dyck block `D'_{k+1}` consists of the pre-cut meander `Q`, followed by the fixed source material through `D_{e+1}` (but before its new-minimum downstep). Since `D'_{k+1}` has total length `2s_{k+1}`, the meander length is exactly

\[
t=2s_{k+1}-(2R_{e+1}+e)=t_{d,e}. \tag{4.13}
\]

There are exactly `B(t,e)` such nonnegative meanders. All remaining target blocks are forced by (4.11). Hence the number of targets `B in C_s` producing this overlap is

\[
\mathbf1_{(4.11)}
\left(\prod_{j=1}^kC_{s_j}\right)B(t_{d,e},e), \tag{4.14}
\]

which depends on `A` only through its composition `r`, not through any Dyck shape. Multiplying by (4.9) and summing over `d,e` proves (4.6) and the theorem. `square`

## 5. Exact reduction of the inverse problem and the LP

Let `P` lift a vector on weak compositions to a class-constant vector on the full first-passage family:

\[
(Px)_A=x_{r(A)}. \tag{5.1}
\]

Theorem 1 is exactly the intertwining identity

\[
\boxed{MP=PK}. \tag{5.2}
\]

Pitman--Tang's matching theorem gives invertibility of `M`. Therefore its restriction to the invariant subspace `im(P)` is injective, so `K` is invertible. Since the all-ones vector lies in `im(P)`,

\[
M^{-1}\mathbf1=P K^{-1}\mathbf1. \tag{5.3}
\]

Let `c=(c_r)` be the Catalan class-size vector. Then the source scalar is reduced **exactly**, not approximately:

\[
\boxed{
\mathbf1^TM^{-1}\mathbf1
=c^TK^{-1}\mathbf1.
} \tag{5.4}
\]

Hence

\[
\boxed{
\frac1{\mathbb ET(\mathcal F_{m,n})}
=2^{-n}c^TK^{-1}\mathbf1.
} \tag{5.5}
\]

This also collapses the positive LP from the preceding run. Because the Pitman--Tang vector `M^{-1}1` is positive and is now known to be class-constant, the reduced primal already contains an exact optimizer:

\[
\boxed{
\mathbf1^TM^{-1}\mathbf1
=
\max_{x\ge0:\ Kx\le\mathbf1}c^Tx
=
\min_{y\ge0:\ K^Ty\ge c}\mathbf1^Ty.
} \tag{5.6}
\]

Thus the Peres lower bound `ET >= c n log n` can now be attacked by constructing a dual cover on **weak compositions** with total mass `O(|F_{m,n}|/log n)`, rather than by controlling exponentially many individual pattern weights. The already-proved `O(n log n)` upper bound corresponds to the opposite primal side.

For the square source subsequence the dimensional collapse is already dramatic at tiny sizes:

- `m=2, n=4`: 2 patterns -> 2 composition states;
- `m=3, n=9`: 28 patterns -> 10 composition states;
- `m=4, n=16`: 2002 patterns -> 84 composition states;
- `m=5, n=25`: 653752 patterns -> 1001 composition states.

The theorem is analytic/combinatorial; these small cases are verification, not the proof.

## 6. Exact-arithmetic finite self-check

Because Theorem 1 has a finite overlap core, I wrote a standard-library-only exact checker after the idea/proof was in hand:

`proofnet24/NM13-11/artifacts/2026-09-18/2026-09-18T08-22-00Z__e0082_ladder_quotient_check.py`

created at commit `2bfcbb74334aafe52721c95d776f5057947d1972`, blob `de062714c6b40cc9c277c8df9cc349831de6135d`.

The checker enumerates every source-valid square first-passage word for `m=2,3,4`, computes matching overlaps with exact `Fraction` arithmetic, verifies the Catalan class sizes, verifies that **every individual row in each source composition class has the same class-summed row**, and compares every ordered quotient entry against formula (4.6). It executed successfully with exit status zero. Archived semantic output:

`proofnet24/NM13-11/artifacts/2026-09-18/2026-09-18T08-22-00Z__e0082_ladder_quotient_check.out`

created at commit `61061ce5ba21f9838ed01e19d69dabd6d75ae531`, blob `909b76d7e0c909a98a01ca26d9b0cf1cb826107a`.

Output:

```text
m=2 n=4 patterns=2 classes=2 class_pairs=4 exact_invariance=PASS formula=PASS
m=3 n=9 patterns=28 classes=10 class_pairs=100 exact_invariance=PASS formula=PASS
m=4 n=16 patterns=2002 classes=84 class_pairs=7056 exact_invariance=PASS formula=PASS
m=5 n=25 patterns=653752 classes=1001 (closed-form counts only)
ALL_EXACT_CHECKS_PASS
```

This is a **self-check**, not an independent audit. Neither P26 nor NM13-12 is counted as having audited it.

## 7. Section-B methods actually attempted

### #14 — FIND THE GROUP ACTING

I searched for a symmetry that could identify rows of the first-passage matching matrix. I did not recover a literal transitive group whose orbits are the right objects. The successful replacement is stronger for this purpose: internal Dyck shapes can be quotiented out exactly because class-summed overlaps depend only on the descending-ladder semilength composition. Outcome: an exact equitable partition and invariant subspace, reducing the full inverse problem to weak compositions.

### #16 — COMPUTE EVERY SMALL CASE AND STARE AT THE SEQUENCE

After deriving the candidate quotient, I exhaustively enumerated the square families through `m=4` using exact rational overlap weights. The row-lumping identity held for all 2002 patterns at `m=4`, and the explicit quotient formula passed all 7056 ordered class-pair comparisons. Outcome: no sporadic small obstruction; the finite data supported and then independently self-checked the written proof. The `m=5` closed-form count already shows the practical dimension reduction `653752 -> 1001` without treating computation as asymptotic evidence.

### #18 — SAY IT IN ANOTHER LANGUAGE

I rewrote the inverse matching-matrix problem as an equitable-partition/intertwining problem `MP=PK`, then as a weighted packing/covering LP on weak compositions. Outcome: the unknown first-passage waiting time is now exactly `2^n/(c^T K^{-1}1)` and the missing Peres lower bound is an explicit low-dimensional dual-cover problem. This is materially different from both the old `E0082-A001` full-matrix route and the preceding run's uniform-row extremal analysis.

## 8. Metric, status, counters, and next obligation

Frozen metric before:

\[
\gamma_{FP}=1.
\]

Frozen metric after:

\[
\gamma_{FP}=1.
\]

So there is **no frozen-metric movement**, despite a substantial structural theorem. Parent source status remains **PARTIAL / OPEN**: neither the exact first-passage asymptotic nor the bridge asymptotic requested by the source is proved here, and no source-level refutation occurred.

Counters:

- `unchanged_runs: 1 -> 2`;
- `stuck_recoveries: 0 -> 0`.

The next high-value obligation is not another full-matrix checker. It is to exploit the explicit kernel (4.6) asymptotically on composition space. In particular, for `n=m^2`, seek a nonnegative reduced dual vector `y` satisfying

\[
K^Ty\ge c,
\qquad
\mathbf1^Ty=O\!\left(\frac{|\mathcal F_m|}{\log n}\right), \tag{8.1}
\]

which would prove the missing `Omega(n log n)` side of Peres's conjecture on the square subsequence. Good genuinely untried next methods are #5 ADD A PARAMETER AND DIFFERENTIATE, #20 FIND WHY THE ALGORITHM FAILS, and #30 DO ONE SCALE / ONE DIRECTION AT A TIME; these are **reserved suggestions only and are not counted as tried in this report**.

If the frozen metric remains unchanged on the next run, the E0082 streak reaches three and the owner Section-I thinking-only stuck protocol becomes mandatory; I will not evade that by renaming the metric.

## 9. Structured ledger_delta for P26

```yaml
ledger_delta:
  track: NM13-11
  category: HARD_OUTSIDE
  source_id: E0082
  claim_id: E0082
  canonical_key: pitman_tang::op_2_3
  canonical_sha256: 1b4de7c58dbd8e94a7bc807a11a84c8e166fceea6c48cb804038b2f998e7228a
  shard_mod_13: 10
  source_status: OPEN
  worker_status: PARTIAL
  metric_name: gamma_FP
  metric_definition: "inf{gamma : E T(FP^{-1,n}) = O(n^gamma)}"
  metric_before: "1"
  metric_after: "1"
  movement: false
  theorem_delta: "Exact ladder-composition equitable quotient MP=PK; full inverse scalar and LP reduce from individual first-passage patterns to weak-composition states with explicit Catalan/ballot kernel K."
  methods_tried: [14, 16, 18]
  unchanged_runs_before: 1
  unchanged_runs_after: 2
  stuck_recoveries_before: 0
  stuck_recoveries_after: 0
  exact_checker: "proofnet24/NM13-11/artifacts/2026-09-18/2026-09-18T08-22-00Z__e0082_ladder_quotient_check.py"
  exact_checker_commit: "2bfcbb74334aafe52721c95d776f5057947d1972"
  exact_output: "proofnet24/NM13-11/artifacts/2026-09-18/2026-09-18T08-22-00Z__e0082_ladder_quotient_check.out"
  exact_output_commit: "61061ce5ba21f9838ed01e19d69dabd6d75ae531"
  exact_output_verdict: "ALL_EXACT_CHECKS_PASS"
  p26_audit: NOT_PASSED
  nm13_12_audit: NOT_PASSED
  literature_check_date: 2026-09-18
  literature_scope: "Original Pitman-Tang source; accessible Berkeley thesis; bounded web searches for exact title/first passage/matching matrix/Dyck/Catalan/weak composition/n log n/Peres and later matching resolution."
  novelty: UNVERIFIED
  next_step: "Analyze explicit quotient kernel K on n=m^2 and construct a composition-space dual cover of mass O(|F_m|/log n), or identify the precise obstruction."
```

No shared root, claim file, peer namespace, workflow, permission, public surface, email/Drive resource, paid compute, or schedule was modified in this invocation.
