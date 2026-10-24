Model actually ran: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — GPT-6 / maximum was requested, but this runtime exposes no authenticated GPT-6 selector, reasoning-effort selector, or applied-run attestation, so I do not claim GPT-6 maximum. NO MOVEMENT on the frozen full-range metric: `r(11) <= 522.9989062413841009635431653560194...` remains, `r(10)=222.6104736743168493957921796888577...` remains exact, and every retained `n>=12` branch is unchanged. Historical F0001 stuck/handoff count `6` is preserved; in the current explicit reassignment sequence this is the second consecutive no-movement run after runs55-56 moved the metric. Methods: #22 READ THE FAILURES, #3 PROVE SOMETHING STRONGER, #21 ASK WHO ELSE HAS THIS SHAPE.**

# R03 HARD OUTSIDE — F0001: a self-contained sparse-circuit cutoff and the exact R2 literature gap

Date checked: 2026-09-18 UTC.  
Repository / branch: private `yspennstate/math-open-problems` / `master`.

Status: **PARTIAL / SOURCE OPEN UNDER THIS AUDIT STANDARD.** The sharp asymptotic is not certified closed here. This run gives a source-scale theorem that removes every minimal row/column circuit whose support misses more than `(2+epsilon)n/log_2 n` coordinates, without using Blinovsky's R1 classification. It also identifies a separate missing reduction in the citation used for Blinovsky v7 equation (18).

## 1. Continuity, exclusions and repository state

Before new mathematics I recovered/read:

- `probability_campaign_2026_09/INDEX.md` and `RANKING.md`;
- root `POSTED.md`, `RESULTS.md`, and `QUEUE.md`;
- `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md`;
- newest own report `runs/R03/20260918T1106Z_57_fold_projection_repair.md`;
- the neighboring random-matrix report `research7_2026-09-17/R7-07/runs/2026-09-18/2026-09-18T092900Z__report.md` (F0003);
- targeted F0001 intake/history hits. The intake corpus is too large to render byte-for-byte through the connector, so I do not claim a literal reread of every roughly 780 intake rows.

`POSTED.md` does not exclude the F0001 source target. The root ledger still names R03 as the sharp sign-matrix singularity track. The owner's repeated current R03 instruction is treated, as in runs55-57, as the explicit reassignment permitting work on F0001 after the earlier terminal handoff; the old stuck history is preserved rather than erased.

No shared root, peer-track file, scheduler state, email, Drive item, permission, workflow, purchase, or public posting is modified in this run.

## 2. Source normalization and current literature

The exact source statement remains the iid nonsymmetric uniform Rademacher problem. Vu's Conjecture 2.2 in `arXiv:2005.02797` states

\[
p_n=(2+o(1))n^2 2^{-n}.
\]

The exact elementary mechanism is the union `T_n` of equal/opposite row-pair and column-pair events. Its first-order probability is

\[
(4+o(1)){n\choose2}2^{-n}
=(1+o(1))n(n-1)2^{1-n},
\]

so the owner's retained target

\[
\boxed{\Pr(\det B_n=0)=(1+o(1))n(n-1)2^{1-n}}
\]

matches the source normalization.

The source-navigation paper Jain--Sah--Sawhney, `arXiv:2010.06554` / GAFA 2021, still proves the full elementary-mechanism asymptotic for finite-support laws **not uniform on their support**. For laws uniform on their support, which includes the Rademacher endpoint, its abstract states exponential-scale precision and a sharp analysis of the compressible contribution, not this polynomial prefactor.

Tikhomirov gives the established logarithmic/exponential rate

\[
\Pr(\det B_n=0)=(1/2+o(1))^n,
\]

not the prefactor.

There is now a current direct claim of the full result: Vladimir Blinovsky, `arXiv:1511.05283v7`, last revised 26 October 2025, states

\[
P_n\sim4{n\choose2}2^{-n}
\]

and the second-term claim

\[
P_n-4{n\choose2}2^{-n}
\sim16{n\choose4}(3/8)^n.
\]

Run56 found a false pointwise folded-concentration inequality in its equation (22); run57 replaced the *dense R3 use* of that inequality by an exact projection argument. That repair does not audit the rest of the paper.

A bounded current 2026 search found later growing-corank and related Bernoulli-matrix work but no independent peer-reviewed source that supplies the missing Rademacher polynomial prefactor. This is negative evidence only, not a novelty proof.

## 3. Frozen metric before and after

Let

\[
T_n=\{\text{at least one equal/opposite row pair or column pair}\}
\]

be the **exact union**, and retain

\[
\boxed{r(n):=2^n\Pr(\det B_n=0,\,T_n^c).}
\]

Source closure is equivalent to

\[
\boxed{r(n)=o(n^2).}
\]

Inherited full-range envelope:

\[
r(10)=222.6104736743168493957921796888577\ldots
\]

exactly, and

\[
\boxed{
r(11)\le
\frac{32584505999078998526809081107735}
     {62303201039659529147657486336}
=522.9989062413841009635431653560194103841\ldots .
}
\]

All replay-certified `n>=12` branches are retained unchanged. This run does not lower the finite full-domain envelope, so the frozen metric has **NO MOVEMENT**.

## 4. Method #22 — read the failure literally

Run57 left two unaudited displayed inputs in Blinovsky v7: the sparse R1 estimate (17) and the intermediate R2 estimate (18). I read both against the cited earlier literature rather than accepting their labels.

Equation (17) contains the sum

\[
2\sum_{k=5}^{n-6\lfloor n/\log_2 n\rfloor}
{n-1\choose k-2}{n\choose k}p_k^{n-k+1},
\qquad
p_k=2^{-k}{k\choose\lfloor k/2\rfloor}.
\]

The prose immediately following it describes the correct circuit mechanism: choose a rank-`k-1` `k x (k-1)` minor, then require all remaining columns to lie in the same hyperplane. This is exactly the part that can be rederived without the R1 classification.

Equation (18), however, requires more care. Blinovsky defines `R2` as a family of arbitrary real subspaces `V` satisfying

\[
(0.51)^{n/2}<\Pr(X\in V^\perp)\le100/\sqrt n
\]

and then writes

\[
\Pr\left(\bigcup_{V\in R2}\{A_{n,n}\subset V^\perp\}\right)\le(o(1))^n,
\tag{B18}
\]

citing Bourgain--Vu--Wood Proposition 5.4.

I checked the cited proposition itself. BVW Proposition 5.4 is a **medium combinatorial dimension estimate for nontrivial hyperplanes over `Z/QZ`**, and its event `A_H` is defined to mean that the random rows **span `H` exactly**. The proposition bounds

\[
\sum_{H\in\mathrm{Gr}(d_\pm)}\Pr(A_H)\le o(1)^n.
\]

That is not literally the same event as (B18), which ranges over arbitrary real relation subspaces and asks only that all rows are contained in `V^\perp`. A reduction may exist through rank/corank stratification and extension to a spanning hyperplane, but it is not supplied by the cited proposition as stated. Therefore this run records a **citation/reduction gap, not a counterexample**: Proposition 5.4 by itself does not justify the displayed equation (18).

This is the second independent place where the current v7 proof needs an explicit repair after equation (22).

## 5. Method #3 — prove a stronger sparse-circuit statement directly

I now remove the sparse sector at the source scale without using membership in R1.

### Definition: minimal row/column circuits

A set of `k` rows is a **minimal circuit** if those `k` rows are linearly dependent but every proper subset is independent. Equivalently, the selected `k x n` submatrix has rank `k-1` and the unique dependence vector

\[
a=(a_1,\ldots,a_k)
\]

has every coordinate nonzero. Define the same notion for columns.

Let `S_k` be the event that there exists a minimal row circuit or minimal column circuit of size `k`.

### Lemma C342 — exact circuit union bound

For every `2<=k<=n`,

\[
\boxed{
\Pr(S_k)
\le
2{n\choose k}{n-1\choose k-2}p_k^{n-k+1},
\qquad
p_k=2^{-k}{k\choose\lfloor k/2\rfloor}.
}
\tag{C342}
\]

#### Proof

Fix a specific set of `k` rows and suppose it is a minimal circuit. Regard the resulting `k x n` matrix by columns. Its column span is the `(k-1)`-dimensional hyperplane

\[
H=a^\perp\subset\mathbb R^k,
\]

where every coordinate of `a` is nonzero.

The first column is a nonzero sign vector, hence it can be extended to a basis of `H` using `k-2` of the remaining `n-1` columns. There are at most

\[
{n-1\choose k-2}
\]

ways to choose those additional basis columns.

Condition on one such basis realization. Every one of the remaining `n-k+1` columns is still an independent uniform vector of `{+-1}^k` and must lie in `H`. By the Erdos--Littlewood--Offord inequality, because all `k` coefficients `a_i` are nonzero,

\[
\Pr(X\in H)=\Pr\left(\sum_{i=1}^k a_i\varepsilon_i=0\right)
\le p_k.
\]

Thus a fixed row set contributes at most

\[
{n-1\choose k-2}p_k^{n-k+1}.
\]

Union over the `{n\choose k}` row sets and repeat for columns. This proves C342. `square`

For `k=2`, C342 recovers the correct pair-collision scale. For the nontrivial remainder we use it only for `k>=3`, where

\[
p_k\le3/8.
\]

### Theorem C343 — any fixed cutoff constant `C>2` is source-negligible

Fix any constant `C>2` and put

\[
K_C(n)=n-\left\lceil\frac{Cn}{\log_2 n}\right\rceil.
\]

Then

\[
\boxed{
\Pr\left(\bigcup_{k=3}^{K_C(n)}S_k\right)
\le
2^{-[\gamma_C-o(1)]n},
\qquad
\gamma_C:=\min\{\log_2(8/3),\ C/2\}>1.
}
\tag{C343}
\]

Consequently

\[
\boxed{
\Pr\left(\bigcup_{k=3}^{K_C(n)}S_k\right)
=o(n^2 2^{-n}).
}
\tag{C344}
\]

#### Proof

By C342 it is enough to bound

\[
2\sum_{k=3}^{K_C(n)}
{n\choose k}{n-1\choose k-2}p_k^{n-k+1}.
\tag{5.1}
\]

Split the range into three parts.

**I. `3<=k<=n/log n`.**  Uniformly in this range,

\[
\log_2\left[{n\choose k}{n-1\choose k-2}\right]
=O\bigl(k\log(n/k)\bigr)=o(n).
\]

Also `p_k<=3/8` and `n-k+1=n-o(n)`. Hence every summand is at most

\[
2^{-[\log_2(8/3)-o(1)]n}.
\]

The extra factor `n` from summing the range is `2^{o(n)}`.

**II. `n/log n<k<=n-n/sqrt(log n)`.**  The standard central-binomial estimate gives

\[
p_k\le C_0 k^{-1/2}
\]

for an absolute constant `C_0`. The two binomial factors are at most `2^{2n}`, while

\[
n-k+1\ge n/\sqrt{\log n}
\]

and `log k=(1+o(1))log n`. Therefore

\[
p_k^{n-k+1}
\le2^{-\Omega(n\sqrt{\log n})},
\]

so the entire middle range is `2^{-\Omega(n\sqrt{\log n})}`.

**III. `n-n/sqrt(log n)<k<=K_C(n)`.**  Write `j=n-k`. Then

\[
\frac{Cn}{\log_2 n}+O(1)\le j\le\frac{n}{\sqrt{\log n}}.
\]

The combinatorial factor becomes

\[
{n\choose j}{n-1\choose j+1}=2^{o(n)}
\]

uniformly in this interval. Since `k=n-o(n)`, the central-binomial estimate gives

\[
\log_2(1/p_k)=\frac12\log_2 n+O(1).
\]

Thus

\[
p_k^{j+1}
\le
2^{-(C/2-o(1))n}.
\]

Combining I--III proves C343. Since `C>2`, both numbers entering `gamma_C` exceed `1`:

\[
\log_2(8/3)=1.4150374992788437\ldots,
\qquad C/2>1.
\]

Therefore C344 follows. `square`

### Corollary C344a — the whole remaining obstruction is near-full support

Every singular square matrix has a minimal dependent subset of rows. On `T_n^c`, such a circuit has size at least `3`. Hence, for every fixed `epsilon>0`,

\[
\boxed{
\Pr\left(
\det B_n=0,\ T_n^c,\
\text{some minimal row circuit has size}\le
n-\frac{(2+\epsilon)n}{\log_2 n}
\right)
=o(n^2 2^{-n}).
}
\tag{C345}
\]

So, at the source scale, the only remaining nontrivial singular matrices have every minimal row dependence supported on

\[
\boxed{
k>n-\frac{(2+\epsilon)n}{\log_2 n}.}
\]

This is stronger, for the purpose of first-order asymptotics, than the `6n/log_2 n` cutoff used in Blinovsky (17), and it does not depend on the R1/R2/R3 taxonomy.

### Novelty qualification

I do **not** claim C342--C345 as novel mathematics. The circuit-plus-Littlewood--Offord mechanism is classical and sits inside the Kahn--Komlos--Szemeredi / Bourgain--Vu--Wood / Jain--Sah--Sawhney sparse/compressible lineage. Its value here is auditability: it gives a self-contained, source-scale replacement for the sparse R1 input and improves the cutoff constant in the exact bookkeeping needed by this track.

## 6. Method #21 — who else has exactly this shape?

The closest established framework is Bourgain--Vu--Wood's decomposition by the cube mass of a **spanning hyperplane**. Their setup makes two distinctions that matter for repairing Blinovsky v7:

1. `A_H` means the random rows **span** a nontrivial hyperplane `H`, not merely lie inside it.
2. Proposition 5.4 sums over finite-field hyperplanes in one combinatorial-dimension class.

This suggests that the right next move for R2 is not to manipulate arbitrary relation spaces. It is to stratify by actual row rank first.

- **Corank one:** the row span itself is a hyperplane, so the BVW event has the right shape. One must still match Blinovsky's real cube-mass threshold to BVW's finite-field combinatorial dimension carefully.
- **Corank at least two:** a direct appeal to Proposition 5.4 is not enough, because the rows span a lower-dimensional space. This sector needs a separate extension-to-hyperplane count or a growing-corank theorem at the correct `2^{-n}` prefactor scale.

This is a cleaner remaining obligation than the displayed equation (18): first prove the corank-one transfer exactly, then show higher corank is source-negligible.

## 7. What moved mathematically, and what did not

**New proved/rederived source-relevant statement:** C342--C345 remove all nontrivial minimal row/column circuits up to

\[
n-(2+\epsilon)n/\log_2 n
\]

at `o(n^2 2^{-n})` cost, with a complete proof on the page.

**New literature/audit finding:** the cited BVW Proposition 5.4 does not literally imply Blinovsky's equation (18); a rank/codimension reduction is missing from the displayed argument.

**Not proved:** the sharp asymptotic, the R2 transfer, or the near-full-support corank-one remainder. The frozen numerical full-range envelope is unchanged, so this run is **NO MOVEMENT** under the task's fixed metric despite genuine structural progress.

No exact checker was produced: the new claim is theorem-sized and its proof is written above; there is no finite enumeration whose certificate would add value.

## 8. Stuck accounting

Historical F0001 terminal handoff/stuck count `6` is preserved. Runs55 and 56 moved the frozen metric. Run57 was the first no-movement run after that movement; this run is the second consecutive no-movement run in the current explicit reassignment sequence. I do not relabel or reset the historical count.

If the next run also fails to move the frozen metric / leaves the same source obligation, the Section-I trigger is reached for this current sequence; the next action must follow the stuck protocol rather than adding another cosmetic sparse lemma.

## 9. Next route — nonrepeating methods

Do not return to another fold and do not extend the finite support-shell catalogue merely for activity.

Next methods:

- **#1 CHANGE THE CATEGORY:** replace arbitrary relation subspaces by the actual random **row-span** and stratify by corank.
- **#11 DUALIZE:** translate the R2 cube-mass condition on a relation space `V` into combinatorial dimension of the row-span hyperplane `V^perp` in the exact corank-one case.
- **#19 MAKE IT AN ALGORITHM:** write an explicit map from every R2 singular matrix to either (a) one BVW hyperplane-spanning certificate or (b) a higher-corank certificate, with bounded multiplicity. The multiplicity bound must be on the page; otherwise Proposition 5.4 cannot be imported.

Concrete next target:

\[
\boxed{
\Pr(\det B_n=0,\ T_n^c,\ \operatorname{corank}B_n=1,\ \text{R2 mass})
=o(n^2 2^{-n})
}
\]

by a source-faithful BVW transfer, followed separately by the `corank>=2` sector.

## 10. `ledger_delta`

```yaml
ledger_delta:
  track: R03
  target: F0001
  source_status: OPEN_UNDER_R03_AUDIT
  status: PARTIAL
  metric_name: "r(n)=2^n P(det B_n=0, T_n^c), full-range retained envelope"
  before:
    r10: "222.6104736743168493957921796888577... exact"
    r11_upper: "522.9989062413841009635431653560194..."
    n_ge_12: "retained unchanged"
  after:
    r10: "222.6104736743168493957921796888577... exact"
    r11_upper: "522.9989062413841009635431653560194..."
    n_ge_12: "retained unchanged"
  movement: "NO MOVEMENT"
  historical_stuck_count: 6
  current_reassignment_no_movement_streak: 2
  methods_tried: [22, 3, 21]
  new_claims:
    - "C342 exact minimal-circuit union bound"
    - "C343 any fixed C>2 cutoff gives exponent gamma_C=min(log2(8/3),C/2)>1"
    - "C345 source-scale remainder localizes to minimal row circuits of size > n-(2+epsilon)n/log2 n"
    - "Blinovsky eq18 citation requires an unstated rank/codimension reduction; BVW Prop5.4 is a hyperplane spanning event"
  novelty: "UNCLAIMED; sparse circuit/LO mechanism is classical"
  checker: "none; theorem-sized written proof, no new finite enumeration"
  next_methods: [1, 11, 19]
  remaining_obligation: "prove r(n)=o(n^2), beginning with an exact corank-one R2 transfer and a separate corank>=2 bound"
```

## 11. Model / scheduler-control note

The actual report model remains GPT-5.6 Sol with reasoning telemetry UNVERIFIED. The exposed task-control surface available to this worker still has no binding model-family or reasoning-effort selector and no authenticated completed-run model/effort attestation. Therefore `GPT-6 / maximum` remains prompt text rather than a setting I can truthfully certify from this context.

The repository's prior deployment record says a historical P26 `You cannot modify this task` denial was authorization-context dependent and that an authorized context later succeeded on P26; R-series edits were denied in another context. The lawful workaround is the owning/authorized task-management context or platform support, not duplication, permission bypass, or pretending the setting applied.
