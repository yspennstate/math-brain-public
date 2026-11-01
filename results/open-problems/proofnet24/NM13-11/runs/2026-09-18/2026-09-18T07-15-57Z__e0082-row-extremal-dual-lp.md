Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. NO FROZEN-METRIC MOVEMENT: `gamma_FP = 1 -> 1`; status `PARTIAL`. Section-B methods actually tried: #11 DUALIZE, #13 FIND WHAT ONLY INCREASES, #24 FIND THE EXTREMAL OBJECT.**

# NM13-11 — E0082 sharp logarithmic row extremal and exact dual packing formulation

Date: 2026-09-18 UTC  
Repository / branch: `yspennstate/math-open-problems` / `master`  
Track: `NM13-11`  
Category: `HARD OUTSIDE`  
Canonical source / claim: `E0082` / `operations/claims/E0082.md`  
Canonical dedup key: `pitman_tang::op_2_3`  
Canonical SHA-256 / shard: `1b4de7c58dbd8e94a7bc807a11a84c8e166fceea6c48cb804038b2f998e7228a`, residue `10 mod 13`

## 1. Runtime/control-plane statement and continuity

The requested `GPT-6 / maximum` setting is **not** what this invocation can verify. The actual model is **GPT-5.6 Sol** and no authenticated reasoning-effort telemetry is exposed, so the reasoning level is **UNVERIFIED**. I do not claim GPT-6 or maximum reasoning.

The exposed task-control surface still has ordinary task fields (title/prompt, schedule or relative start, timing mode, enabled state) but no bindable model-family selector and no bindable reasoning-effort selector. Making `GPT-6 / maximum` enforceable would require an owner-authorized product/workspace/API/admin surface that exposes those fields and authenticated per-run runtime attestation. The historical P26 `You cannot modify this task` result is an authorization-context boundary, not an ownership release; the legitimate workaround is the owning/otherwise-authorized task context or platform/admin support, not cloning the task or bypassing access controls. This invocation did not create, modify, disable, or duplicate any schedule.

I reread or targeted-search-recovered the owner-required state: `FLEET_RULES.md`; `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md`; `operations/NEW_METHODS_2026-09-16.md`; the later NM13 deployment amendment; root `QUEUE.md`, `POSTED.md`, `RESULTS.md`; campaign `INDEX.md` and `RANKING.md`; the current E0082 claim; the newest own report; newest neighboring NM13-10/NM13-12 reports; the E-intake source and attempt rows; relevant claims, ownership/handoff history and audit searches. No source, ownership, retirement, or audit delta displaced E0082.

The current target was already lawfully admitted in the immediately preceding E0082 run. The canonical claim was created create-only and read back at commit `84922e0f873072e7b346b21142dba7de681410d5`. I did **not** recreate, overwrite, or edit it in this invocation.

The newest prior NM13-11 report is

`proofnet24/NM13-11/runs/2026-09-18/2026-09-18T06-47-57Z__e0082-fp-exponent-logarithmic-overlap.md`

(created at commit `cfdcc4c63a2e300fe02a85020338706506efffd5`, blob `97bd055a01b8a9b2015b16302d38dfdeffa97e9d`). It proved, for every fixed `lambda<0`,

\[
\mathbb E T(\mathcal{FP}^{\lambda,n})=O_\lambda(n\log n),
\]

and therefore moved the frozen metric for `lambda=-1`

\[
\gamma_{FP}:=\inf\{\gamma:\mathbb ET(\mathcal{FP}^{-1,n})=O(n^\gamma)\}
\]

from `[1,5/4]` to the exact value `1`. That value is preserved here; there is no metric reset.

## 2. Dated source/literature check — 2026-09-18

I rechecked the original Pitman--Tang paper, especially Theorem 6 (matching-matrix formula), Section 2.4 (first-passage matching columns) and Section 2.5. The source still asks for exact asymptotics of `ET(FP^{lambda,n})`; it explicitly records Yuval Peres's conjectural two-sided order `n log n`. The source's Theorem 6 states that for any finite equal-length pattern family with matching matrix `M`,

\[
\frac1{\mathbb ET}=2^{-n}\mathbf 1^TM^{-1}\mathbf 1,
\]

and the coordinates of `M^{-1}1` are positive reciprocal pattern-waiting quantities.

Fresh bounded web queries used the exact paper title plus `first passage`, `waiting time`, `n log n`, `Peres`, and the authors' current publication trail. They recovered the original paper, the same conjectural statement, bibliographic/citation pages and later Pitman--Tang work, but no later source-matching resolution of the exact first-passage asymptotics and no later theorem matching the structural statements below. This is bounded negative evidence only; publication novelty remains **UNVERIFIED**. The matching-matrix LP reformulation below may well be folklore in finite-pattern renewal theory, and I do not present it as a novelty certificate.

## 3. Starting point from the previous run

Fix `lambda=-1`. For square lengths `n=m^2`, the parity-correct terminal level is exactly `-m`. Let

\[
\mathcal F_m:=\mathcal{FP}^{-1,m^2}
\]

and let `M_m` be its Pitman--Tang matching matrix. For `A\in\mathcal F_m`, write

\[
R_m(A):=\sum_{B\in\mathcal F_m}(M_m)_{A,B}
\]

for its row sum.

The preceding report proved the exact ladder-time identity

\[
R_m(A)=1+\sum_{d=1}^{m-1}
\mathbb P\!\left(S_{\ell_d}=-d,\ \min_{1\le r\le \ell_d}S_r>-m\right), \tag{1}
\]

where `S` is an independent simple symmetric random walk and

\[
\ell_d=m^2-\tau_{m-d}(A),
\]

with `tau_r(A)` the first time the pattern `A` hits level `-r`. That report discarded the actual `ell_d` and used a worst-case local-CLT atom, giving the uniform `O(log m)` row-sum bound. The present run asks whether that logarithm was only an artefact.

It is not: the logarithm is sharp for worst rows, with an exact leading constant.

## 4. The sharp worst-row theorem

Define

\[
c_*:=\sqrt{\frac{2}{\pi e}}.
\]

### Theorem 1 — exact asymptotic of the largest row sum on square lengths

For `n=m^2` and `lambda=-1`,

\[
\boxed{
\max_{A\in\mathcal F_m}R_m(A)
= c_*\log m+o(\log m)
=\frac{c_*}{2}\log n+o(\log n).
} \tag{2}
\]

Thus the previous `O(log n)` worst-row estimate is asymptotically sharp in order and leading coefficient along this source-valid subsequence.

### Proof: universal upper bound

For an integer `d>=1`, set

\[
a_d:=\sup_{\ell\ge d,\ \ell\equiv d\pmod2}\mathbb P(S_\ell=-d).
\]

Dropping the barrier condition in (1) gives, for every `A\in\mathcal F_m`,

\[
R_m(A)\le 1+\sum_{d=1}^{m-1}a_d. \tag{3}
\]

I claim

\[
a_d\sim \frac{c_*}{d}. \tag{4}
\]

Indeed, the compatible choice `\ell=d^2` is always allowed because `d^2\equiv d (mod 2)`, and the lattice local CLT gives

\[
d\,\mathbb P(S_{d^2}=-d)\longrightarrow
\sqrt{\frac{2}{\pi}}e^{-1/2}=c_*.
\]

For the matching upper bound, use the elementary Gaussian-binomial estimate already proved in the preceding report,

\[
\mathbb P(S_\ell=-d)
\le C\ell^{-1/2}\exp\!\left(-\frac{d^2}{4\ell}\right). \tag{5}
\]

If `\ell/d^2 ->0` or `\ell/d^2->infinity`, (5) (and the central-binomial bound in the second case) makes `d P(S_ell=-d)->0`. On any compact interval `\ell/d^2\in[\eta,\eta^{-1}]`, the lattice local CLT is uniform and gives

\[
d\,\mathbb P(S_\ell=-d)
=
\sqrt{\frac{2}{\pi s}}\exp\!\left(-\frac1{2s}\right)+o(1),
\qquad s=\frac{\ell}{d^2}.
\]

The displayed function of `s>0` has its unique maximum at `s=1`, equal to `c_*`. This proves (4). Harmonic summation now yields

\[
\sum_{d=1}^{m-1}a_d=c_*\log m+o(\log m), \tag{6}
\]

so (3) proves the upper half of (2).

### Proof: an explicit row attaining the same leading term

For each `m`, define an explicit pattern `A^{(m)}` by concatenating, in decreasing order `d=m-1,m-2,...,0`, the blocks

\[
B_d:= (+1,-1)^d,-1. \tag{7}
\]

Each block has length `2d+1`, hence

\[
\sum_{d=0}^{m-1}(2d+1)=m^2.
\]

Starting from level `-(r-1)`, the corresponding block oscillates between `-(r-1)` and `-(r-2)` and reaches `-r` only on its last step. Therefore the concatenation first hits `-r` at

\[
\tau_r(A^{(m)})
=\sum_{j=0}^{r-1}(2(m-1-j)+1)
=r(2m-r)
=m^2-(m-r)^2. \tag{8}
\]

In particular it first hits `-m` at time `m^2`, so `A^{(m)}\in\mathcal F_m`. For the ladder index in (1), (8) gives the exact identity

\[
\ell_d=m^2-\tau_{m-d}(A^{(m)})=d^2. \tag{9}
\]

Consequently

\[
R_m(A^{(m)})
=1+\sum_{d=1}^{m-1}
\mathbb P\!\left(S_{d^2}=-d,\ \min_{1\le r\le d^2}S_r>-m\right). \tag{10}
\]

By the reflection principle, since `d<m`,

\[
\mathbb P\!\left(S_{d^2}=-d,\ \min_{1\le r\le d^2}S_r>-m\right)
=p_{d^2}(d)-p_{d^2}(2m-d), \tag{11}
\]

where `p_t(x):=P(S_t=x)` and symmetry has removed the signs.

The first sum satisfies

\[
\sum_{d=1}^{m-1}p_{d^2}(d)=c_*\log m+o(\log m) \tag{12}
\]

because `d p_{d^2}(d)->c_*`. The reflected correction is only `O(1)`. Indeed (5) gives

\[
p_{d^2}(2m-d)
\le \frac{C}{d}
\exp\!\left(-\frac{(2m-d)^2}{4d^2}\right). \tag{13}
\]

Split `1<=d<m` dyadically according to `m/2^{j+1}<d<=m/2^j`. The `j=0` block contributes `O(1)`, while the `j>=1` blocks contribute at most a constant multiple of `exp(-c4^j)`; hence the total in (13) is uniformly bounded in `m`. Combining (10)--(13),

\[
R_m(A^{(m)})=c_*\log m+o(\log m). \tag{14}
\]

Together with the universal upper bound, this proves (2). `\square`

This is a theorem-sized symbolic argument; there is no finite enumerative core and no heuristic computation is used as evidence. I therefore did not manufacture a checker merely to create a certificate.

## 5. Exact LP / dual formulation of the inverse-matrix quantity

Theorem 1 says that replacing all rows by the worst row cannot remove the logarithm. Method #11 gives the exact object that must replace that step.

Let `M` be the matching matrix of any equal-length finite pattern family for which the Pitman--Tang theorem applies, and set

\[
S(M):=\mathbf1^TM^{-1}\mathbf1.
\]

Theorem 6 gives `q:=M^{-1}1>0`. Applying the same theorem to the reversed pattern family gives `y:=M^{-T}1>0`, because reversal transposes the matching matrix.

### Proposition 2 — positive packing/covering formulation

\[
\boxed{
S(M)=
\max_{w\ge0:\ Mw\le\mathbf1}\mathbf1^Tw
=
\min_{z\ge0:\ M^Tz\ge\mathbf1}\mathbf1^Tz.
} \tag{15}
\]

### Proof

The vector `q=M^{-1}1` is primal feasible and has objective `1^Tq=S(M)`. For any primal-feasible `w`, positivity of `y=M^{-T}1` gives

\[
\mathbf1^Tw
=y^TMw
\le y^T\mathbf1
=S(M),
\]

so the primal optimum is exactly `S(M)`.

Similarly `y` is dual feasible with equality `M^Ty=1` and objective `1^Ty=S(M)`. Primal and dual therefore meet at `S(M)`; no abstract strong-duality assumption beyond these explicit feasible optimizers is needed. `\square`

For the source family,

\[
\frac1{\mathbb ET(\mathcal F_m)}=2^{-m^2}S(M_m). \tag{16}
\]

Thus the exact first-passage waiting-time problem is equivalent to estimating the optimum of the positive packing LP (15), rather than explicitly inverting an exponentially large matrix.

The preceding `O(n log n)` proof corresponds to the **constant primal certificate**

\[
w=\frac1{R_{\max}}\mathbf1,
\qquad
R_{\max}:=\max_A R_m(A),
\]

for which `M_m w<=1` and `1^Tw=k/R_max`, where `k=#F_m`. Theorem 1 proves

\[
R_{\max}\sim c_*\log m.
\]

Therefore the constant-weight packing certificate is asymptotically saturated: no proof that keeps all pattern weights equal can remove the logarithmic loss. Any `O(n)` upper bound would require a genuinely **nonuniform** feasible `w` with total mass `Theta(k)`. Conversely, the Peres lower bound `Omega(n log n)` would follow from a dual covering vector `z` with total mass `O(k/log n)`. This isolates the two exact remaining routes without re-inverting `M`.

## 6. Section-B methods actually attempted

### #11 — DUALIZE

I replaced the inverse-matrix scalar `1^T M^{-1}1` by the exact positive packing/covering pair (15). Outcome: the source quantity has an explicit LP variational characterization with positive optimizers. This both explains the previous row-sum argument and states precisely what a successful nonuniform improvement must construct.

### #13 — FIND WHAT ONLY INCREASES

The descending ladder times `tau_1<tau_2<...<tau_m` are the monotone skeleton hidden in the row identity. I used their residual durations `ell_d=n-tau_{m-d}` as the real variables, rather than bounding every overlap independently. Outcome: the block construction (7) makes these durations exactly `ell_d=d^2`, the heat-kernel maximizing scale, simultaneously for every ladder level.

### #24 — FIND THE EXTREMAL OBJECT

The explicit concatenated first-passage word `A^{(m)}` is a logarithmically extremal row witness. Reflection plus the local CLT yields the exact leading constant `sqrt(2/(pi e))` and matches the universal upper bound. Outcome: the residual logarithm is **not** a slack artifact of the previous local bound; worst-row control is genuinely saturated.

These are new methods on E0082. I did not relabel #2/#4/#8 from the preceding run as new attempts.

## 7. Status, counters, audits, and next obligation

The frozen metric does not move:

\[
\boxed{\gamma_{FP}:1\to1.}
\]

Hence this is the first unchanged-metric run after the E0082 movement:

- `unchanged_runs: 0 -> 1`;
- `stuck_recoveries: 0 -> 0`.

This is nevertheless substantive source progress: the worst-row logarithm is now proved sharp, and the full inverse problem is converted exactly to a positive LP. The remaining obligation has changed. A future run should **not** spend effort trying to improve the uniform worst-row bound; Theorem 1 rules that route out. The live alternatives are:

1. construct a nonuniform primal packing `w` with substantially larger total mass than `k/log n` (which would improve the `O(n log n)` upper bound); or
2. construct a low-mass dual cover `z` of order `k/log n` (which would prove the conjectured `Omega(n log n)` lower bound).

Good untried Section-B directions for the next run are #12 FIND WHAT IS CONSERVED, #15 BREAK THE SYMMETRY, and #21 ASK WHO ELSE HAS THIS SHAPE; they are suggestions only and are **not counted as attempted here**.

Parent source status remains `PARTIAL`, not `PROVED`: exact asymptotics of the first-passage family and the bridge half remain unresolved. P26 audit: **NOT PASSED / not recovered**. NM13-12 audit: **NOT PASSED / not recovered**. No closure or publication-novelty claim is made.

## 8. Structured ledger_delta for P26

```yaml
ledger_delta:
  track: NM13-11
  source_id: E0082
  claim_id: E0082
  canonical_key: pitman_tang::op_2_3
  status: PARTIAL
  metric_name: gamma_FP
  metric_scope: "lambda=-1 first-passage family; inf power exponent"
  metric_before: "1"
  metric_after: "1"
  movement: false
  theorem_this_run:
    - "max row sum of M(FP^{-1,m^2}) = sqrt(2/(pi e))*log(m) + o(log m)"
    - "1^T M^{-1}1 equals an exact positive packing LP and its covering dual"
  methods_actual:
    - 11
    - 13
    - 24
  unchanged_runs_before: 0
  unchanged_runs_after: 1
  stuck_recoveries_before: 0
  stuck_recoveries_after: 0
  audits:
    P26: NOT_PASSED
    NM13-12: NOT_PASSED
  next_step: "Abandon uniform worst-row improvement; attack the nonuniform primal packing or dual covering problem."
  literature_check_date: 2026-09-18
  literature_scope: "original Pitman-Tang source, exact Peres n-log-n wording, exact-title/author/follow-up searches"
  literature_result: "No source-matching later resolution found in bounded search; novelty UNVERIFIED."
```

No shared root, peer namespace, workflow, permission, public surface, email/Drive item, paid-compute resource, or schedule was modified in this invocation.