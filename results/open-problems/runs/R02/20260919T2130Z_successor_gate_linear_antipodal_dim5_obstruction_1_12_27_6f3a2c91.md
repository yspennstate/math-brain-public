Model actually ran: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — this was not GPT-6 at maximum, and I do not claim otherwise. NO SOURCE-METRIC MOVEMENT: `7/sqrt(17) -> 7/sqrt(17)`; successor availability `E_ready: 0 -> 0`; methods #1 CHANGE THE CATEGORY, #12 FIND WHAT IS CONSERVED, #27 SWAP THE QUANTIFIERS.**

# R02 — successor gate plus a complete obstruction to all low-dimensional linear antipodal constructions

Run ID: `20260919T2130Z_successor_gate_linear_antipodal_dim5_obstruction_1_12_27_6f3a2c91`  
Repository / branch: private `yspennstate/math-open-problems` / `master`  
Worker: R02  
Lane: **CLOSABLE OUTSIDE**

## 1. Continuity and current state

I continued from the newest complete R02 report

`runs/R02/20260919T2011Z_successor_gate_srg69_owned_a17_two_border_obstruction_10_18_23_f3a91c6d.md`

rather than restarting the retired I0095 search. The old KLS route remains retired from this slot and its history is preserved.

The source is Afonso S. Bandeira, Anastasia Kireeva, Antoine Maillard and Almut Rödder, *Randomstrasse101: Open Problems of 2024*, arXiv:2504.20539v1, Open Problem 11. The source asks for

\[
C^*=\sup_{n\ge1}\sup_{A\in\{\pm1\}^{n\times n}}
\frac{\operatorname{disc}(A)}{\sqrt n},
\qquad
\operatorname{disc}(A)=\min_{x\in\{\pm1\}^n}\|Ax\|_\infty.
\]

The fixed R02 metric remains the greatest certified explicit-matrix lower bound. The durable certificate is

\[
\operatorname{disc}(A_{17})=7,
\qquad
\boxed{C^*\ge \frac7{\sqrt{17}}=1.697749375\ldots}.
\]

The independent R01 audit exhaustively checked all `2^16=65536` projective signings of the explicit matrix and returned discrepancy `7 / PASS`. The exact ratio squared remains `49/17`.

Canonical `operations/claims/I0095.md` still says `PENDING_ADMISSION, not READY`. Operationally the active I0095 CLOSABLE route already hit its six-unchanged retirement boundary and remains **RETIRED / HANDOFF**. This run therefore does not reopen blind sign-matrix enumeration and does not call Open Problem 11 closed.

Required continuity reads before new work included:

- `probability_campaign_2026_09/INDEX.md` and `RANKING.md`;
- root `POSTED.md`, `RESULTS.md`, `QUEUE.md`;
- `operations/NEW_METHODS_2026-09-16.md`;
- `operations/claims/I0095.md`;
- the newest complete R02 report and exact A17 border artifacts;
- the newest neighboring R13 discrepancy report;
- current coordinator/task-health state and current CLOSABLE successor screens;
- intake/attempt history recovered through the canonical I0095 and queue material.

No shared root, peer file, email, Drive, public post, workflow, permission, purchase, scheduler or task prompt was modified.

## 2. Exact repository delta and successor gate

The preceding immutable R02 report was created at

`30738a3805e42db694a523a1f2096da1a9034f87`.

After writing the mathematical idea before the archive checker and archiving the exact finite output, the pre-report head used for the exact delta was

`190fa567f42060bd0a48425be964c5bb161741ab`.

The exact comparison

`30738a3805e42db694a523a1f2096da1a9034f87 .. 190fa567f42060bd0a48425be964c5bb161741ab`

returns:

- status `ahead`;
- **166 commits ahead**;
- **0 behind**;
- `too_large = null`.

The only new canonical `operations/claims/*.md` file in this interval is

`operations/claims/E0011-REASSIGNED-2026-09-19.md`.

That is a real CLOSABLE OUTSIDE lifecycle event, but it is already consumed by another native slot. Its controlling record says `CLAIMED / RE-ADMITTED_ACTIVE / CLOSABLE OUTSIDE` and assigns a fresh Durrett Problem 5 regeneration route. It is therefore not R02 inventory.

The coordinator status at `operations/task_health/runs/2026-09-19T210100Z/status.md` records four assigned CLOSABLE targets (`I0130`, `E0017`, `SHPECTOROV-ZHAO-2026-SRG69`, `E0011`) and explicitly records **no additional free READY CLOSABLE candidate** after consuming E0011 and SRG69. The newer independent R06 CLOSABLE successor screen reaches the same conclusion.

Therefore

\[
\boxed{E_{\rm ready}:0\longrightarrow0.}
\]

R02 remains **CLOSABLE OUTSIDE / SUCCESSOR_ADMISSION_HOLD / NO ACTIVE MATHEMATICAL TARGET**.

## 3. Current source / literature sentinel

Checked on 2026-09-19 UTC (2026-09-20 local Jerusalem time):

1. The official arXiv record for `2504.20539` still shows only **v1, submitted 29 April 2025**. No later arXiv version is listed.
2. Emrullah Akbas and Suvrit Sra, *Boolean Small-Ball Inequalities for Discrepancy Theory*, arXiv:2609.20785, submitted 17 September 2026, gives new Boolean small-ball machinery and recovers Komlós and Matrix Spencer, but its advertised results do not determine the exact real flat sign-matrix constant in Open Problem 11.
3. A bounded search for the exact low-dimensional linear-covering obstruction proved below recovered standard covering-code and hereditary-discrepancy references, including the standard definition of linear covering radius and Sylvester-Hadamard discrepancy literature, but no primary source matching this exact finite `F_2^4` parity-support statement. This is **bounded negative evidence only**, not a novelty or priority certificate.

No source-matching resolution of Open Problem 11 was found in this bounded current check.

## 4. Neighboring discrepancy update does not transfer

The newest complete R13 report keeps its fixed upper metric

\[
B_{R13}(86)=7.28139
\]

unchanged, while improving its explicit general Boolean-Komlós finite obstruction

\[
2.264655\longrightarrow 2.2647288.
\]

That is genuine neighboring progress, but general unit-column matrices form a larger class than normalized flat sign matrices. A lower obstruction in the larger Komlós class does not furnish an explicit flat sign-matrix lower witness. R02's fixed metric therefore does not move.

## 5. Methods #1 / #12 / #27 — stop searching linear codes; prove they cannot work

The immediately preceding R02 triple was `#10/#18/#23`; this run uses a different mechanism.

### #1 CHANGE THE CATEGORY

Instead of searching sign matrices directly, move through the exact antipodal covering-code dictionary. For the `n` row vectors `r_i`, let

\[
C=\{r_i,-r_i:1\le i\le n\}\subset\{\pm1\}^n.
\]

Then

\[
\operatorname{disc}(A)=n-2R(C),
\]

where `R(C)` is the Hamming covering radius. A very natural construction route is therefore a complement-closed **binary linear code** with at most `2n` codewords.

At `n=22`, for example, an improving discrepancy `8` would correspond to covering radius `7`. The question becomes: can a complement-closed binary linear code of length 22 and size at most 44 have covering radius at most 7?

### #12 FIND WHAT IS CONSERVED

For `17<=n<=31`, any binary linear code with `|C|<=2n<64` has dimension at most five. If it is complement-closed, it contains the all-one vector.

Choose a basis whose first generator is the all-one vector. The remaining at most four generator rows identify each coordinate `j` with a point

\[
x_j\in\mathbf F_2^4.
\]

Let `m_x` be the multiplicity of type `x`. The key conserved datum after adversarial balancing inside equal-type coordinate groups is only the **parity support**

\[
O=\{x\in\mathbf F_2^4:m_x\text{ is odd}\}.
\]

Since \(\sum_xm_x=n\), `|O|` has the same parity as `n`.

### #27 SWAP THE QUANTIFIERS

Rather than trying to find one good linear code, prove that **for every** such linear code there is **one adversarial target word** far from it.

For each coordinate type `x`:

- if `m_x` is even, choose target signs with equal numbers `+1` and `-1`, giving group sum `q_x=0`;
- if `m_x` is odd, choose target signs whose group sum is `q_x in {+1,-1}`.

The correlation with an affine codeword indexed by `a in F_2^4` is then exactly the Walsh coefficient

\[
W_a(q)=\sum_{x\in O}q_x(-1)^{a\cdot x}.
\]

So a finite signing lemma on the order-16 Sylvester Walsh matrix controls **every** dimension-at-most-five complement-closed linear code, regardless of its coordinate multiplicities.

## 6. New finite lemma — exact exhaustive certificate

### R02-I0095-LIN16-01

**STATUS: PROVED FINITELY / SELF-CHECKED / NOVELTY UNVERIFIED.**

For every subset `O subset F_2^4`:

- if `|O|` is even, there is a signing `q:O->{+-1}` such that
  \[
  \max_{a\in\mathbf F_2^4}\left|\sum_{x\in O}q_x(-1)^{a\cdot x}\right|\le6;
  \]
- if `|O|` is odd, there is such a signing with the stronger bound
  \[
  \max_{a\in\mathbf F_2^4}\left|\sum_{x\in O}q_x(-1)^{a\cdot x}\right|\le5.
  \]

### Exact finite certificate

The new-method idea was archived before the checker at

`artifacts/R02/20260919T2122Z_linear_antipodal_dim5_idea.md`.

The exact checker is

`artifacts/R02/20260919T2122Z_linear_antipodal_dim5_checker.cpp`

with executed output

`artifacts/R02/20260919T2122Z_linear_antipodal_dim5_checker.out`.

It checks **all `2^16=65536` supports**, split as 32768 even and 32768 odd supports. For each nonempty support it fixes one sign by global negation, Gray-enumerates signings, and stops only when the required threshold certificate is found. The executed output records

```text
even_supports_checked=32768
even_threshold=6
even_signings_examined_until_certificate=85462
even_largest_returned_certificate=6
odd_supports_checked=32768
odd_threshold=5
odd_signings_examined_until_certificate=170421
odd_largest_returned_certificate=5
total_supports_checked=65536
total_signings_examined_until_certificate=255883
PASS
```

This is a **self-check**, not an independent audit. The checker establishes existence at the stated thresholds; because it stops once a threshold witness is found, the `largest_returned_certificate` fields are not claimed to be exact hereditary-discrepancy optima.

## 7. New theorem — all linear antipodal constructions are blocked through order 31

### R02-I0095-LIN31-02

**STATUS: PROVED modulo the exact finite lemma above / PARTIAL FOR THE SOURCE / NOVELTY UNVERIFIED.**

Let `C <= F_2^n` be a binary linear code of dimension at most five containing the all-one word. Then

\[
R(C)\ge
\begin{cases}
(n-6)/2,&n\text{ even},\\
(n-5)/2,&n\text{ odd}.
\end{cases}
\tag{7.1}
\]

### Proof

Choose the basis and coordinate types `x_j in F_2^4` described above, padding the nonconstant basis by zero rows if the dimension is below five. Every codeword, in sign notation, is

\[
\pm\big((-1)^{a\cdot x_j}\big)_{j=1}^n
\qquad(a\in\mathbf F_2^4).
\]

For each type `x`, balance an adversarial target word inside the `m_x` coordinates of that type so the signed group sum is zero when `m_x` is even and is the finite-lemma sign `q_x in {+-1}` when `m_x` is odd. This is always possible.

For every affine codeword, the absolute correlation with this target is therefore

\[
\left|\sum_{x\in O}q_x(-1)^{a\cdot x}\right|.
\]

If `n` is even, `|O|` is even and the finite lemma makes every such correlation at most 6. Hence the target's distance to every codeword is at least

\[
\frac{n-6}{2}.
\]

If `n` is odd, the odd-support half of the lemma makes every absolute correlation at most 5, giving distance at least `(n-5)/2`. This proves (7.1). `square`

### Corollary for the R02 construction search

For every `17<=n<=31`, any complement-closed binary **linear** code with `|C|<=2n` has dimension at most five. Therefore any sign-matrix construction whose row/complement covering code is linear satisfies

\[
\operatorname{disc}(A)=n-2R(C)\le
\begin{cases}
6,&n\text{ even},\\
5,&n\text{ odd}.
\end{cases}
\tag{7.2}
\]

In particular:

- at `n=22`, **no linear complement-closed code of size at most 44 can have covering radius 7**; hence the tempting `[22,<=5]` linear-code route cannot produce the metric-improving discrepancy `8`;
- throughout orders `17..31`, a linear antipodal construction cannot even match the existing discrepancy-7 A17 witness at odd order, and cannot improve its normalized value at any order in the interval;
- the existing A17 certificate is therefore genuinely on the **nonlinear** side of the covering-code dictionary.

This is substantially more useful than another failed random code search: it removes the entire low-dimensional linear-code architecture, not merely one generator family.

## 8. What remains viable

The theorem does **not** rule out the source and does **not** rule out the promising `n=22, R=7` target in the nonlinear class. The earlier direct nonlinear quotient search at `n=22` reached only 2399 uncovered projective points after exact best-response coordinate descent; nonzero residual was explicitly labeled diagnostic, not impossibility.

If I0095 is ever lawfully reactivated with a fresh route, the next useful construction search should therefore be one of:

1. a genuinely nonlinear complement-closed `(22,<=44,7)` covering code;
2. a nonlinear group-orbit / coset-union code not closed under vector addition;
3. an order `n>=32` linear construction, where `2n` first permits dimension six and the present `F_2^4` obstruction no longer exhausts the linear class;
4. a direct flat sign-matrix orbit unrelated to the A17 one-/two-border architecture.

Do **not** spend another run searching `[22,5]` linear codes: theorem (7.1) proves that route cannot work.

## 9. Source metric and labels

The source metric does not move in this run:

\[
\boxed{
C^*\ge\frac7{\sqrt{17}}=1.697749375\ldots
}
\]

before and after. The new result is a **route-elimination theorem**, not a stronger lower bound and not source closure.

Honest labels:

- Open Problem 11: **OPEN / PARTIAL** in R02 evidence;
- explicit A17 finite claim: **PROVED / independently audited**;
- low-dimensional linear antipodal obstruction: **PROVED with exact finite self-check / independent audit pending / novelty unverified**;
- active R02 source route: **RETIRED / HANDOFF**;
- current R02 operational state: **SUCCESSOR_ADMISSION_HOLD**.

## 10. Model / scheduler control truth

The current policy file and current coordinator status agree with the actually exposed scheduler surface: it provides task identity/title, prompt, schedule/timing mode, enabled state and ordinary task-update controls, but **no binding model-family selector, no reasoning-effort selector, no guaranteed-duration field and no authenticated applied-run model/effort receipt**.

Therefore GPT-6/maximum remains a prompt request only on this surface. Enforcing it would require an eligible owner/admin/product/API scheduling surface that persists model and reasoning choices into routing and returns authenticated applied-runtime metadata.

The historical `You cannot modify this task` failures, including P26-class cases, are authorization/context boundaries. The compliant workaround is to modify the same task from its owning/authorized workspace/API/admin context or use platform support to repair access. Do not duplicate the job, bypass permissions or infer that a repository prompt edit changes native scheduler configuration.

No scheduler or permission change was attempted in this run.

## 11. Structured ledger_delta

```yaml
ledger_delta:
  worker: R02
  lane: CLOSABLE_OUTSIDE
  lifecycle: SUCCESSOR_ADMISSION_HOLD
  active_mathematical_target: null
  retired_handoff_source: I0095
  source:
    work: "Bandeira-Kireeva-Maillard-Rodder, Randomstrasse101: Open Problems of 2024"
    locator: "Open Problem 11"
    arxiv: "2504.20539v1"
  source_metric:
    name: greatest_certified_explicit_sign_matrix_lower_bound
    before: "7/sqrt(17)"
    after: "7/sqrt(17)"
    order: 17
    discrepancy: 7
    exact_ratio_squared: "49/17"
    movement: false
  successor_metric:
    name: E_ready_free_closable
    before: 0
    after: 0
    movement: false
  exact_repo_delta:
    base: "30738a3805e42db694a523a1f2096da1a9034f87"
    pre_report_head: "190fa567f42060bd0a48425be964c5bb161741ab"
    commits_ahead: 166
    commits_behind: 0
    too_large: null
    material_claim_event:
      id: E0011
      state: "CLAIMED / RE-ADMITTED_ACTIVE / CLOSABLE OUTSIDE"
      available_to_R02: false
  new_mathematical_handoff:
    finite_lemma:
      id: R02-I0095-LIN16-01
      supports_checked: 65536
      even_support_threshold: 6
      odd_support_threshold: 5
      self_check: PASS
      independent_audit: false
    theorem:
      id: R02-I0095-LIN31-02
      statement: "If C <= F2^n is linear, dim C <= 5, and 1^n in C, then R(C)>=(n-6)/2 for even n and >=(n-5)/2 for odd n."
      consequence: "For 17<=n<=31, any complement-closed linear code with |C|<=2n yields discrepancy <=6 (even n) or <=5 (odd n)."
      source_closure: false
      novelty: UNVERIFIED
  artifacts:
    idea: "artifacts/R02/20260919T2122Z_linear_antipodal_dim5_idea.md"
    checker: "artifacts/R02/20260919T2122Z_linear_antipodal_dim5_checker.cpp"
    output: "artifacts/R02/20260919T2122Z_linear_antipodal_dim5_checker.out"
  methods: [1, 12, 27]
  next_if_reactivated:
    - "nonlinear complement-closed (22,<=44,7) covering code"
    - "nonlinear group/coset-union construction"
    - "dimension-six linear regime n>=32"
    - "direct flat sign-matrix orbit not containing A17 as a local border core"
  prohibited_actions_used: false
```
