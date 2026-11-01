Model actually ran: **GPT-5.6 Sol. Reasoning level: UNVERIFIED; GPT-6 / maximum was requested, but the exposed runtime/task interface has no model-family selector, no reasoning-effort selector, and no authenticated runtime telemetry, so GPT-6 maximum is not claimed. NO MOVEMENT on the fixed rigorously replay-certified remainder metric: the best retained bounds remain `r(10)<=275.751921258717971...` and `r(11)<=525.118207165694344...`. Section-B methods actually used: #17 LOOK FOR YOUR NUMBERS SOMEWHERE ELSE, #20 FIND WHY THE ALGORITHM FAILS, #29 ADD THE POINTS AT INFINITY.**

Problem/source: **iid Rademacher square-matrix singularity — Komlós (1967) lineage; Jain--Sah--Sawhney arXiv:2010.06554, Conjecture 1.1 specialized to uniform Rademacher; Sahasrabudhe arXiv:2512.15077, Section 4 / Eq. (4.1). Overall source status: OPEN. R03 status: PARTIAL.**

# R03 run22 — exact collision sequence and CRT/profinite null witnesses

Run ID: `20260916T2337Z_22_collision_exact_crt`  
Repository/branch: `yspennstate/math-open-problems`, `master`.

## 1. Continuity, source, and frozen metric

Before new mathematics I recovered/reread the campaign controls `probability_campaign_2026_09/INDEX.md`, `RANKING.md`, root `POSTED.md`, `RESULTS.md`, `QUEUE.md`, `operations/NEW_METHODS_2026-09-16.md`; newest own report `runs/R03/20260916T2208Z_21_overlap_partition_mobius.md`; newest R04 report `runs/R04/20260916T2312Z_i0027_quantitative_rate.md`; and targeted intake/source material. The large intake JSONL surfaces remain connector-truncated, so I do not claim a byte-for-byte visual reread of all roughly 780 intake rows.

Fresh source/status searches are archived at `artifacts/R03/20260916T2337Z_22_status_search.md`. Jain--Sah--Sawhney still distinguish the sharp non-uniform finite-support theorem from the uniform-support case, where full singularity is only determined at exponential scale. Sahasrabudhe's December 2025 survey remains consistent with the precise iid-sign prefactor being open. Symmetric Bernoulli matrices are a distinct dependent-entry ensemble and are not imported.

The exact target normalization remains
\[
\Pr(\det B_n=0)
=(1+o(1))\,n(n-1)2^{1-n}
=(1+o(1))\,2n(n-1)2^{-n}.
\]
Let `T_n` be the exact union of signed equal/opposite row-pair and column-pair events. Retained C225 proves the matching lower asymptotic with explicit overlaps. The fixed R03 upper metric is
\[
\boxed{r(n):=2^n\Pr(\det B_n=0,\ T_n^c).}
\tag{M}
\]
Source closure is equivalent to
\[
\boxed{r(n)=o(n^2).}
\]

Retained C240/C246 put `m=n-1` and identify `T_n^c` with
\[
\mathcal G_m=
\{A\in\{0,1\}^{m\times m}:\text{rows and columns are nonzero and pairwise distinct}\}.
\]
Run21's best replay-certified values were
\[
r(10)\le275.751921258717971\ldots,
\qquad
r(11)\le525.118207165694344\ldots.
\]
Those do **not** move this run. Since the immediately preceding run moved, the unchanged count is now `1`, not a stuck episode.

The retained killed routes remain killed and their history is not reset: X27 fixed-epsilon JSS diagonalization, X28 conditional row/column independence, X29 fixed-best-prime, naive left/right-normal multiplication, and exponential-rate-only bounds.

## 2. Method #17 — LOOK FOR YOUR NUMBERS SOMEWHERE ELSE: the residual is OEIS A116527

Let
\[
S_m:=\#\{A\in\{0,1\}^{m\times m}:\det A=0\},
\]
and
\[
G_m:=|\mathcal G_m|.
\]
Every binary matrix with a zero row/column or two equal rows/columns is singular. Therefore the collision-free singular count is exactly
\[
R_m:=\#\{A\in\mathcal G_m:\det A=0\}
=S_m-(2^{m^2}-G_m).
\tag{2.1}
\]

Run21 C260, specialized to `V=0` and grouped only by the number of partition blocks, gives the completely explicit all-`m` formula
\[
\boxed{
G_m
=\sum_{b=0}^m s(m+1,b+1)(2^b-1)_m,
}
\tag{2.2}
\]
where `s` is the signed Stirling number of the first kind and `(x)_m` is the falling factorial.

### R03-C263 — exact residual-sequence identity

**STATUS: PROVED / auxiliary exact reformulation, not source closure.**

Current OEIS A116527 is defined as the number of singular rational binary `m x m` matrices with no zero rows or columns and all rows and columns distinct, modulo row permutation. Hence, definitionally,
\[
\boxed{
R_m=m!\,A116527(m),
\qquad
r(m+1)=2^{m+1-m^2}m!\,A116527(m).
}
\tag{C263.1}
\]

OEIS A000410 counts singular binary matrices with distinct nonzero rows, modulo row permutation. OEIS A000409 counts exactly the subfamily among those matrices with a zero column or two equal columns. Therefore
\[
\boxed{
A116527(m)=A000410(m)-A000409(m).
}
\tag{C263.2}
\]
This is a direct set difference; no asymptotic estimate is involved.

The current A116527 page contains a conjectural cross-reference with a shifted `A000409(n-1)`. As written that line is false already at `n=4`: `A000410(4)-A000409(3)=425-6=419`, while `A116527(4)=75`. The same-index identity (C263.2) is the exact definitional relation. This is recorded only as an auxiliary database correction; no public OEIS edit was made.

The exact checker brute-forces every binary matrix through `m=4`, verifies (2.2), verifies that every excluded collision matrix is singular, and reproduces all retained R03 exact residuals through sign order `n=9` from the classified total singular counts through binary order `m=8`:
\[
0,0,0,\frac{225}{256},\frac{335475}{65536},
\frac{149664375}{8388608},
\frac{1658391558075}{34359738368},
\frac{15544095862461075}{140737488355328}.
\]

This route is useful because the R03 remainder is not a new ad hoc finite statistic: it is exactly a classical binary-matrix sequence after a deterministic normalization.

## 3. Method #20 — FIND WHY THE ALGORITHM FAILS: the order-nine database term is not a campaign certificate

Equation (2.2) gives, with no external enumeration input,
\[
\boxed{
G_9=2040859528996474439366400,
}
\]
and therefore the exact number of order-nine binary matrices having at least one zero/equal row or column is
\[
\boxed{
2^{81}-G_9=376992110232783910045952.
}
\tag{3.1}
\]

Current OEIS A046747 lists
\[
S_9=902616230040448613437952,
\]
credited to Dominik Beck on 2 July 2026. Combining that database value with (3.1) would give
\[
R_9=525624119807664703392000
\]
and hence the source-backed candidate
\[
\boxed{
r(10)
=\frac{2053219217998690247625}{9223372036854775808}
=222.61047367431684\ldots .}
\tag{3.2}
\]
This is smaller than the current replay-certified R03 bound by
\[
53.14144758440115\ldots .
\]

I deliberately do **not** promote (3.2) to the fixed metric. The current TheoremDB audit of the new order-nine A046747 term explicitly records it as sourced database evidence and says it located no primary paper or replayable orbit/enumeration certificate for that extension. Fresh exact-string / author / certificate searches in this run likewise did not locate a replayable certificate. A000410's new order-nine term is explicitly derived from A046747, so it is not an independent certification route. The checker therefore labels the input

`EXTERNAL_SOURCE_INPUT_NOT_REPLAY_CERTIFIED`

and uses it only to calculate the candidate consequence.

This is the precise failure of the small-case algorithm: **the arithmetic reduction is complete; the missing object is an independently reproducible order-nine total-singular enumeration certificate.** Under the campaign's finite-claim rule, an approved database term without such a replay is not enough to change the rigorously certified metric.

## 4. Method #29 — ADD THE POINTS AT INFINITY: exact CRT/profinite singularity

The single-prime modular routes of runs17--21 deliberately overcount real singularity, because a real-nonsingular integer matrix can be singular modulo one prime. Rather than trying another prime, compactify all relevant residues at once.

Let `P` be a finite set of distinct primes and
\[
Q=\prod_{p\in P}p.
\]
Hadamard gives, for every binary `m x m` matrix,
\[
|\det A|\le m^{m/2}.
\tag{4.1}
\]

### R03-C264 — finite CRT/Hadamard exactness

**STATUS: PROVED.** If
\[
Q>m^{m/2},
\]
then for every binary `m x m` matrix,
\[
\boxed{
\det A=0\text{ over }\mathbb Z
\iff
\det A\equiv0\pmod p\quad\text{for every }p\in P.
}
\tag{C264}
\]

**Proof.** The forward implication is immediate. Conversely, simultaneous modular singularity implies every `p in P` divides the integer determinant, hence `Q | det A`. If `det A` were nonzero, `|det A|>=Q`, contradicting (4.1). QED.

For `m=9`, take
\[
P=\{2,3,5,7,11,13\},
\qquad Q=30030.
\]
The exact checker verifies
\[
Q^2=901800900>9^9=387420489,
\]
so real singularity of a `9 x 9` binary matrix is **exactly** simultaneous singularity at those six primes.

There is a stronger null-vector version which identifies the object that should be counted next.

### R03-C265 — primitive CRT null-witness reformulation

**STATUS: PROVED REDUCTION.** Assume `Q>m^(m/2)` is squarefree. Define a CRT vector
\[
a\in(\mathbb Z/Q\mathbb Z)^m
\]
to be *primitive* if its reduction modulo every prime divisor `p|Q` is not the zero vector. Then
\[
\boxed{
\det A=0
\iff
\exists\text{ primitive }a\in(\mathbb Z/Q\mathbb Z)^m
\text{ with }A^Ta=0\pmod Q.
}
\tag{C265}
\]

**Proof.** If `A` is singular over the integers, choose a nonzero integer null vector and divide its coordinates by their gcd. Its reduction is nonzero modulo every prime, hence gives a primitive CRT witness. Conversely, a primitive CRT witness makes `A` singular modulo every `p|Q`; C264 then forces real singularity. QED.

For a fixed CRT witness `a`, put
\[
H_Q(a)=\{y\in\{0,1\}^m:a\cdot y=0\pmod Q\}.
\]
The partition-Möbius proof of C260 did not use field division: it only counted allowed Boolean columns under a linear congruence. Therefore the same partition formula counts collision-free matrices carrying a fixed primitive CRT witness. This turns the remaining real-singularity problem into a **single squarefree-ring concentration/incidence problem**, rather than a collection of unrelated marginal finite-field problems.

### Why the obvious CRT gluing still fails

The new exact reformulation does not by itself improve the metric. Let `Z_p(A)` be a projective modular-null witness count. Real singularity is bounded by each marginal `Z_p`, but summing `min_p Z_p` is no larger than the best marginal only if one can evaluate the joint distribution. Hölder/product tricks go the wrong direction because higher modular corank increases witness multiplicity. In particular, multiplying the six marginal probabilities is unjustified; the elementary row/column mechanisms create strong cross-prime dependence.

So the next route is now concrete: count **primitive CRT-projective null witnesses** directly, using the allowed-column concentration
\[
h_Q(a)=|H_Q(a)|,
\]
partition Möbius collision removal, and a sparse/dense split on `a`. If one can show that, after the signed pair mechanisms are removed, the total primitive CRT incidence is `o(n^2 2^{-n})`, the accidental one-prime determinant-divisibility sector disappears automatically by C264/C265.

This is materially different from choosing a better single prime.

## 5. Exact evidence

Checker:
`artifacts/R03/20260916T2337Z_22_collision_exact_crt_exact.py`

Archived output:
`artifacts/R03/20260916T2337Z_22_collision_exact_crt_exact.out`

Source SHA-256:
`f155dc328e982f83a4762398e75d5125c5704ed2308e32147cc59821577372c9`

Output SHA-256:
`fca6ee52df4a0a21f9b95792b88b555902fa11dd6e94363acd748ff7da2cc553`

The output ends `SELF-CHECK PASS`.

## 6. Independent R04 audit

Newest ready R04 package read:
`runs/R04/20260916T2312Z_i0027_quantitative_rate.md`.

I record
\[
\boxed{\texttt{R03-AUDIT-R04-I0027-C11-09 = PASS}}
\]
**claim-scoped to the new quantitative upgrade C11, conditional on the already-audited retained C8 dependency chain.**

The fresh primary-source check confirms Alev--Anari--Lau--Oveis Gharan's effective-resistance clustering theorem has exactly the scaling R04 uses: cross weight `O(m/delta)` and induced-cluster resistance diameter `O(delta^3 n/m)`.

For a maximizing dense graph, R04 takes `delta=n^(1/4)`, hence
\[
q=O(n^{7/4}),\qquad \epsilon=O(n^{-1/4}).
\]
The retained surgery errors become
\[
O(qn)=O(n^{11/4}),
\qquad
O(q^2n/m)=O(n^{5/2}),
\]
and the intra-cluster resistance term is
\[
O(mn\epsilon)=O(n^{11/4}).
\]
Its new uniform bridge estimate is
\[
K_{\rm br}\le n^3/54+O(n^{5/2}).
\]
Thus the dominant error is `O(n^(11/4))`, giving
\[
M_n=n^3/54+O(n^{11/4}).
\]
I also rechecked the moving-cutoff balance in C11a: with `eta=n^(-1/2)`, both the small-block mass loss and large-block-count/capacity loss are `O(n^(-1/2))`, and the retained Hölder step
\[
(\sum \tilde p_i^2)(\sum\sqrt{\tilde p_i})^2\ge1
\]
indeed yields `(1-Q_2)/S^2<=Q_2(1-Q_2)<=1/4`. I found no new algebraic gap in C11. This audit does not certify publication novelty and does not replace the still-missing P26 end-to-end audit.

## 7. Model/runtime and permissions

The limitation remains exactly as recorded in the controlling policy. The exposed native task mutation schema offers prompt/title/schedule/timing/enabled controls but **no model-family or reasoning-effort selector**. Therefore GPT-6/maximum can only be requested in prompt text; actual runtime remains UNVERIFIED.

The repository records that one context returned `You cannot modify this task` for P26/P01/P03, while a different authorized context later succeeded in updating P26. That is consistent with a task/workspace ownership boundary, not a field this R03 worker can repair. The legitimate workaround is the owning/admin-authorized native-task context, or platform support if that owning context still lacks model controls. I did not duplicate the task, bypass permissions, or change scheduler state.

## 8. Current ledger and next attack

| Item | Status |
|---|---|
| Source asymptotic `n(n-1)2^(1-n)(1+o(1))` | **OPEN** |
| C225 collision lower bound with overlaps | **PROVED / retained** |
| Exact `r(n)`, `1<=n<=9` | **PROVED / retained** |
| C260/C261/C262 partition-Möbius modular machinery | **PROVED / retained** |
| **C263 exact residual-sequence identity** | **PROVED NEW auxiliary reformulation** |
| OEIS A116527 shifted-index cross-reference | **FALSE AS WRITTEN; auxiliary database correction only** |
| Source-backed candidate `r(10)=222.6104736743...` from A046747 order-9 term | **NOT REPLAY-CERTIFIED; NOT METRIC** |
| **C264 CRT/Hadamard exactness** | **PROVED NEW** |
| **C265 primitive CRT null-witness reformulation** | **PROVED NEW REDUCTION** |
| Best replay-certified `r(10)` | **unchanged <=275.751921258717971...** |
| Best replay-certified `r(11)` | **unchanged <=525.118207165694344...** |
| Full `r(n)=o(n^2)` | **OPEN** |
| P26 full-package R03 audit | **ABSENT in targeted search** |
| second distinct full-package R03 audit | **ABSENT** |
| R03 audit of R04-C11 | **PASS, claim-scoped / conditional on retained audited dependency chain** |

Because the fixed metric did not move, this is `UNCHANGED 1`; it is **not** yet a section-I stuck episode. The next run should not enumerate another bounded support plane as its main route. It should attack the primitive CRT witness count from C265: formulate inverse Littlewood--Offord over the squarefree ring `Z/QZ`, isolate witnesses whose Boolean zero-set has near-maximal density, and use C260-style partition Möbius inversion to remove row/column collisions exactly. The target-scale question is whether the dense primitive CRT sector is `o(n^2 2^{-n})` once elementary signed-pair witnesses are excluded.

### ledger_delta

```yaml
ledger_delta:
  track: R03
  source: "Komlos 1967 lineage; Jain-Sah-Sawhney arXiv:2010.06554 Conjecture 1.1 specialized to uniform Rademacher; Sahasrabudhe arXiv:2512.15077 Sec.4/Eq.(4.1)"
  target: "P(det B_n=0)=(1+o(1))*n(n-1)*2^(1-n)"
  metric: "r(n)=2^n P(det B_n=0 and no signed equal/opposite row/column pair), with smallest rigorously replay-certified complete-domain upper envelope"
  before:
    r10_upper: "275.751921258717971..."
    r11_upper: "525.118207165694344..."
    full_asymptotic: "OPEN"
  after:
    r10_upper: "275.751921258717971..."
    r11_upper: "525.118207165694344..."
    full_asymptotic: "OPEN"
  movement: "NO MOVEMENT; new exact sequence and CRT reductions do not yet lower the replay-certified envelope"
  unchanged_count: 1
  status: "PARTIAL / SOURCE OPEN"
  tried_moves: [17, 20, 29]
  new_claims:
    - "R03-C263 exact collision-free residual sequence identity and all-m Stirling formula"
    - "R03-C264 finite CRT/Hadamard exactness"
    - "R03-C265 primitive CRT null-witness reformulation"
  source_backed_not_promoted:
    - "OEIS A046747 S9 implies candidate r10=222.61047367431684..., but no replayable order-9 enumeration certificate was located"
  exact_evidence:
    checker: "artifacts/R03/20260916T2337Z_22_collision_exact_crt_exact.py"
    output: "artifacts/R03/20260916T2337Z_22_collision_exact_crt_exact.out"
    source_sha256: "f155dc328e982f83a4762398e75d5125c5704ed2308e32147cc59821577372c9"
    output_sha256: "fca6ee52df4a0a21f9b95792b88b555902fa11dd6e94363acd748ff7da2cc553"
  audit_ids:
    - "R02-AUDIT-R03-C253-04=PASS (retained claim-scoped audit)"
    - "R03-AUDIT-R04-I0027-C11-09=PASS (new claim-scoped audit)"
    - "P26 full-package R03 audit: NONE LOCATED"
```

No shared ledger, peer file, email, Drive, public posting, purchase, permission, workflow, or scheduler state was changed.
