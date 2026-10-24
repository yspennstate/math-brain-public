Model actually ran: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — GPT-6 / maximum was requested, but this runtime exposes no authenticated GPT-6 selector, reasoning-effort selector, or applied-run attestation, so I do not claim GPT-6 maximum. NO MOVEMENT on the frozen full-range metric: `r(11) <= 522.9989062413841009635431653560194...` remains, `r(10)=222.6104736743168493957921796888577...` remains exact, and every retained `n>=12` branch is unchanged. Historical F0001 stuck/handoff count `6` is preserved; since runs55-56 both moved the metric, this is the first no-movement episode of the current explicit reassignment sequence and does not erase or reset that history. Methods: #25 COUNT THE SAME THING TWICE, #27 SWAP THE QUANTIFIERS, #28 REPLACE FOR ALL WITH TYPICAL.**

# R03 HARD OUTSIDE — F0001: exact fold averaging and a projection repair of the dense R3 step

Date checked: 2026-09-18 UTC.  
Repository / branch: private `yspennstate/math-open-problems` / `master`.

Status: **PARTIAL.** The source-level sharp asymptotic is not certified closed here. This run does not move the finite full-range envelope, but it repairs the concrete pointwise-fold obstruction isolated in run56 at the level actually needed for the dense completion estimate.

## 1. Continuity and repository state

Before new mathematics I recovered/read:

- `probability_campaign_2026_09/INDEX.md` and `RANKING.md`;
- root `POSTED.md`, `RESULTS.md`, and `QUEUE.md`;
- `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md`;
- newest own report `runs/R03/20260918T1010Z_56_f0001_supportsum10_8f31.md`;
- newest neighboring random-matrix report located for F0003, `research7_2026-09-17/R7-07/runs/2026-09-18/2026-09-18T092900Z__report.md`;
- targeted F0001 intake/history hits. The large intake JSONL files remain connector-truncated, so I do not claim a byte-for-byte read of all roughly 780 rows.

The owner's repeated current R03 instruction is treated as the explicit reassignment that authorized runs55-57 to return to F0001; the old terminal handoff and stuck history are preserved rather than rewritten.

No shared root, peer-track file, scheduler state, email, Drive item, permission, workflow, purchase, or public posting is modified in this run.

## 2. Exact source normalization and current primary literature

The outside source statement remains Van H. Vu, *Recent progress in combinatorial random matrix theory*, arXiv:2005.02797 / *Probability Surveys* 18 (2021), Section 2, Conjecture 2.2. For an `n x n` iid uniform sign matrix,

\[
 p_n=(2+o(1))n^2 2^{-n}.
\]

The elementary equal/opposite row-or-column lower mechanism has leading probability

\[
 (4+o(1)){n\choose2}2^{-n}
 =(1+o(1))n(n-1)2^{1-n},
\]

so the owner's retained target

\[
\boxed{\Pr(\det B_n=0)=(1+o(1))n(n-1)2^{1-n}}
\]

matches the source normalization.

Let `T_n` be the **exact union** of all equal/opposite signed row-pair and column-pair events. The frozen R03 remainder metric remains

\[
\boxed{r(n):=2^n\Pr(\det B_n=0,\,T_n^c).}
\]

Source closure is equivalent to

\[
\boxed{r(n)=o(n^2).}
\]

Primary-literature check, 2026-09-18:

1. Jain--Sah--Sawhney, arXiv:2010.06554 / GAFA, proves the sharp elementary-mechanism asymptotic for finite-support laws **not uniform** on their support. For a distribution uniform on its support, including the Rademacher endpoint, it states only exponential-scale precision, while providing a sharp compressible-vector analysis.
2. Tikhomirov supplies the sharp logarithmic/exponential rate `(1/2+o(1))^n`, not the polynomial prefactor.
3. Vladimir Blinovsky, arXiv:1511.05283v7, dated 26 Oct 2025, currently **claims** the full asymptotic and a second term. Run56 found that the first pointwise inequality displayed in its equation (22) is false: `v=(1,1,2)` has concentration `1/4`, whereas one fold gives `(1,-1)` with concentration `1/2`. This does not disprove the theorem.
4. This run shows that the **particular dense-completion use** of (22), and analogously (24), can be replaced by an exact projection argument. This is not an end-to-end audit of the v7 paper. In particular, the sparse estimate (17), the imported R2 estimate (18), and all global bookkeeping still require independent verification before the preprint can count as closure here.

Accordingly I record the external situation as: **a current preprint claims the theorem, but R03 does not yet certify it as KNOWN/closed.**

## 3. Frozen metric before and after

Inherited from run56:

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

All replay-certified `n>=12` branches are retained unchanged.

This run proves no smaller numerical full-range envelope, so the metric is unchanged.

## 4. Idea before code — methods #25, #27, #28

Run56 established that the pointwise assertion in Blinovsky (22)

\[
\rho_r(F_b(v))\le \rho_n(v)\quad\hbox{for every }b
\]

is false. The error is conceptual: fixing the tail pattern is conditioning, and one conditional fiber can be denser than the unconditional zero set.

The new route is to stop asking for a pointwise inequality.

### #25 COUNT THE SAME THING TWICE

Let

\[
Z_d(u):=\{\varepsilon\in\{\pm1\}^d:\varepsilon\cdot u=0\},
\qquad
\rho_d(u):=2^{-d}|Z_d(u)|.
\]

Split `n=r+m`. Choose a pivot `q<=r` with `v_q != 0`. For each
`b=(b_{r+1},...,b_n) in {+-1}^m`, define the folded prefix vector
`F_b(v) in R^r` by keeping every first-`r` coefficient except

\[
(F_b(v))_q=v_q+\sum_{j=r+1}^n b_jv_j.
\]

Then there is the **exact identity**

\[
\boxed{
|Z_n(v)|=\sum_{b\in\{\pm1\}^m}|Z_r(F_b(v))|,
}
\tag{C334}
\]

or equivalently

\[
\boxed{
2^{-m}\sum_b\rho_r(F_b(v))=\rho_n(v).
}
\tag{C335}
\]

**Proof.** For `eps in {+-1}^n`, set `a=eps_[1:r]` and

\[
b_j=\varepsilon_j\varepsilon_q,
\qquad j>r.
\]

Conversely, from `(a,b)` reconstruct `eps_j=a_qb_j` for `j>r`. This is a bijection, and

\[
\varepsilon\cdot v=a\cdot F_b(v).
\]

Counting zeros on both sides gives C334.

This explains the run56 counterexample exactly: one folded fiber may increase, but the **average over all folds is fixed**.

### #27 SWAP THE QUANTIFIERS

The union of the folded zero sets is not mysterious either:

\[
\boxed{
\bigcup_b Z_r(F_b(v))=\pi_r Z_n(v),
}
\tag{C336}
\]

where `pi_r` is projection onto the first `r` signs. Therefore

\[
2^{-r}|\pi_rZ_n(v)|
\le 2^m\rho_n(v).
\tag{C337}
\]

More generally, and this is the form that removes the need to choose an individual relation at all:

> **Projection-density lemma.** For every `E subset {+-1}^n` and `n=r+m`,
> \[
> \boxed{
> 2^{-r}|\pi_rE|\le 2^m\,2^{-n}|E|.
> }
> \tag{C338}
> \]

The proof is the one-line injection bound `|pi_r E| <= |E|` after normalizing the two cubes.

For a whole relation subspace `V`, take

\[
E_V=V^\perp\cap\{\pm1\}^n.
\]

This is strictly better suited to the corank-two step than handling two folded relations independently: the common constraint is treated in one object.

### #28 REPLACE FOR ALL WITH TYPICAL

Blinovsky's `R3` class is defined by

\[
\mu_n(E_V):=2^{-n}|E_V|\le (0.51)^{n/2}.
\]

For `m=floor(alpha n)` and `r=n-m`, C338 gives

\[
\mu_r(\pi_rE_V)
\le
2^m(0.51)^{n/2}
=
2^{-(L-\alpha)n+O(1)},
\qquad
L:=\frac12\log_2(1/0.51).
\tag{C339}
\]

Numerically

\[
L=0.485715423901614553\ldots .
\]

Thus any fixed `alpha<L` makes a projected admissible prefix exponentially rare. Once the seed submatrix has determined `V`, the remaining independent column prefixes need only be treated as **typical independent draws** from the `r`-cube; no statement is required for every individual fold.

## 5. Repair of the displayed dense R3 completion step

The paper takes

\[
\alpha=0.3,\qquad m=[0.3n],\qquad r=[0.7n].
\]

Hence C339 becomes

\[
\boxed{
\mu_r(\pi_rE_V)
\le
2^{-(c_0+o(1))n},
\qquad
c_0=L-0.3
=0.185715423901614553\ldots .
}
\tag{C340}
\]

In the completion count used in the paper's equation (23), after a seed `r x (r-1)` submatrix fixes the relevant relation space, there are order `m=0.3n` independent remaining column prefixes that must lie in the admissible projected set. Replacing the false pointwise-max fold bound by C340 gives

\[
\Pr(\text{that completion}\mid\text{seed})
\le
2^{-(c_0+o(1))nm}.
\]

Thus

\[
\boxed{
\Pr(\text{dense R3 corank-one sector})
\le
2^{-(0.3c_0+o(1))n^2+O(n)}
=2^{-(0.055714627170484366+o(1))n^2}.
}
\tag{C341}
\]

The combinatorial seed choices displayed in (23) contribute only `2^{O(n)}` (the paper crudely bounds them by `2^{3n}`), so they do not affect the quadratic exponent.

This is weaker than the numerical factor the paper obtains from its false pointwise inequality, but it is vastly stronger than needed: the sector remains superexponentially below the target `2^{-n}` scale.

The same repair applies more cleanly to the paper's equation (24). For a two-relation space `V`, work directly with the common zero set

\[
E_V=V^\perp\cap\{\pm1\}^n,
\]

rather than two separately folded vectors. Since `V in R3` already gives the same cube-mass threshold, C338 again bounds every admissible prefix by C339. The remaining independent prefixes therefore give the same kind of `2^{-Omega(n^2)}` suppression. No simultaneous pointwise folded-concentration inequality is needed.

### Parameter note

C339 in fact permits any fixed `0<alpha<L`. The crude quadratic exponent is

\[
\alpha(L-\alpha),
\]

maximized at `alpha=L/2=0.242857711950807...`, where it equals

\[
0.05897986825398128\ldots .
\]

I do **not** need this optimization for the repair; the paper's original `alpha=0.3` already leaves a positive quadratic exponent.

## 6. What this does and does not prove

**Proved in this run:**

1. C334--C336: exact fold-average and fold-union identities.
2. C338: the exact projection-density lemma for arbitrary subsets of the sign cube.
3. C340--C341: under the paper's own `R3` cube-mass definition and seed/completion setup, the dense corank-one completion step remains `2^{-Omega(n^2)}` after replacing the false pointwise inequality in (22).
4. The analogous common-subspace projection removes the same pointwise issue from the displayed corank-two fold step (24).

**Not proved:** an end-to-end proof of Blinovsky v7 or of Vu's conjecture. In particular I have not independently rederived the sparse `R1` estimate (17), the exact four-row second-term bookkeeping, or the imported `R2` proposition. A local repair is not closure.

The source-level remaining obligation is still

\[
\boxed{r(n)=o(n^2).}
\]

## 7. Exact finite self-check

Only after obtaining C334--C341 did I build a finite exact sanity check.

Checker:

`artifacts/R03/20260918T1106Z_57_fold_projection_exact.py`

creation commit:

`5bac96182da38bbc354cecf1f74b9a30f4398f61`

Exact-SHA readback completed.

It exhausts every coefficient vector

\[
v\in\{-2,-1,0,1,2\}^n,\qquad 2\le n\le6,
\]

every split `n=r+m`, and every nonzero prefix pivot. It verifies C334 and C336 exactly and rechecks the run56 pointwise counterexample.

Executed/archived output:

`artifacts/R03/20260918T1106Z_57_fold_projection_exact.out`

creation commit:

`fd8b7d871d085f6b7e699c6cb4b8af23de9f85f4`

Exact-SHA readback completed. It records

`EXHAUSTIVE_CASES=215820`

and ends

`SELF-CHECK PASS`.

The checker is a finite self-check, not the proof of the theorem-sized projection lemma; the proof is above.

## 8. Outcome of the three methods

- **#25 COUNT THE SAME THING TWICE — SUCCESS.** The fold construction has an exact average identity C334/C335. The pointwise inequality was the wrong quantity.
- **#27 SWAP THE QUANTIFIERS — SUCCESS.** Asking which prefixes admit *some* tail completion converts the whole issue to a projection of the original zero set, yielding C338 and simultaneously handling multiple relations.
- **#28 REPLACE FOR ALL WITH TYPICAL — SUCCESS for the dense completion sector.** Independent remaining prefixes only need the projected density, producing the superexponential bound C341. This does not settle the sparse/intermediate sectors.

No full-range metric movement follows yet because the retained finite envelope is already much more specific than a sector-level asymptotic repair and the other source sectors remain unaudited.

## 9. Next new route

Do **not** return to another fold or another finite support-shell checker next run unless it moves the fixed envelope.

Next methods: **#22 READ THE FAILURES, #3 PROVE SOMETHING STRONGER, #21 ASK WHO ELSE HAS THIS SHAPE.**

Concrete next obligation: audit/replace the sparse equation (17) and its uniformity up to `k=n-O(n/log^2 n)` against the established compressible machinery of Jain--Sah--Sawhney / Bourgain--Vu--Wood. The useful target is stronger than merely reproducing `(1/2+o(1))^n`: isolate the exact pair and four-row mechanisms and prove every remaining sparse-support contribution is `o(n^2 2^{-n})`. If that succeeds, combine it with C341 and then inspect the R2 imported proposition under the exact same normalization.

If this direction leaves the fixed full-range metric unchanged for three consecutive runs, invoke Section I rather than manufacturing more projection lemmas.

## 10. Model/scheduler control

The exposed task-control interface still has prompt/title, schedule/timing, enablement and relative-start controls, but no binding model-family field, no reasoning-effort field, and no authenticated completed-run telemetry. GPT-6/maximum therefore remains prompt-only from this surface.

The repository also records that an earlier P26 `You cannot modify this task` result was authorization-context dependent: P26 was later updated successfully from an authorized context, whereas R-series edits were denied in another context. The lawful workaround is the owning/authorized task-management context or platform support, not task duplication or permission bypass. No scheduler modification was attempted in this run.

```yaml
ledger_delta:
  track: R03
  source: "F0001 / Vu Conjecture 2.2 / iid uniform Rademacher singularity"
  source_status: "OPEN for this campaign; Blinovsky arXiv:1511.05283v7 claims a proof but is not yet independently certified"
  run_status: PARTIAL
  fixed_metric: "r(n)=2^n P(det B_n=0, T_n^c), with exact trivial collision union T_n removed"
  before: "r(11)<=32584505999078998526809081107735/62303201039659529147657486336 = 522.9989062413841009635431653560194...; r(10)=222.6104736743168493957921796888577... exact; n>=12 retained"
  after: "same"
  movement: "NO MOVEMENT"
  historical_stuck_handoff_count: 6
  history_policy: "preserved, not reset; runs55-56 moved the metric, run57 is the first subsequent no-movement episode"
  methods: [25, 27, 28]
  new_result: "exact fold-average/projection identities; projection-density repair makes displayed dense R3 corank-one/two completion sectors 2^{-Omega(n^2)} despite the false pointwise fold inequality"
  checker_cases: 215820
  remaining_obligation: "r(n)=o(n^2); independently validate/replace sparse R1 and intermediate R2 sectors and full bookkeeping"
  next_methods: [22, 3, 21]
```
