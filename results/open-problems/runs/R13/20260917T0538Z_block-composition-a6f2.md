Model actually run: **GPT-5.6 Sol**; reasoning level **UNVERIFIED**, not verified GPT-6 maximum. **Metric moved on 63 dimensions: the retained entries `B_R13(n)` strictly improve for every `10 <= n <= 72`; in particular `B_R13(10): 149/50 -> 2 sqrt(2)`. Methods used: #22 READ THE FAILURES, NOT THE SUCCESSES; #28 REPLACE “FOR ALL” WITH “FOR TYPICAL”; #29 ADD THE POINTS AT INFINITY / CLOSE THE BOUNDARY.**

# R13 — Boolean Komlos: block-composition theorem and 63-entry envelope improvement

Run ID: `20260917T0538Z_block-composition-a6f2`  
Repository/branch: `yspennstate/math-open-problems` / `master`.

## 1. Continuity and fixed metric

The target remains the **real Boolean** Komlos signing problem in the source scope navigated through Bansal--Jiang, arXiv:2508.03961v2: for every real `m x n` matrix whose columns have Euclidean norm at most one, choose signs in `{−1,+1}` so that the infinity norm of the signed column sum is small. Complex phases, rank-two/vector colorings, random-input statements, and average-case estimates are not substitutes for this target.

The frozen R13 metric is the complete rigorously certified pointwise upper-bound function `B_R13(n)`, retaining constants and domains. I continued from the newest R13 report

`runs/R13/20260917T043626Z_n10-mixedtail-8c31.md`,

which proved the arbitrary-row ten-column bound `B_R13(10) <= 149/50` and retained the earlier exact/small-`n` and C16/GFL envelope. I did not restart an older route.

Before research I reread/recovered the required repository state: campaign `probability_campaign_2026_09/INDEX.md` and `RANKING.md`, root `POSTED.md`, `RESULTS.md`, `QUEUE.md`, the controlling new-methods owner directive, the newest R13 report/checker, current neighboring R12/R16 run directories, the R12/P26 Komlos audit evidence, and targeted repository hits for Komlos. The large intake JSONL corpus is connector-truncated when rendered wholesale, so I do not claim a fictitious byte-for-byte visual reread of every intake row; targeted repository search recovered the relevant Komlos history and no conflicting owner.

This run changes no source definition. It changes the quantitative envelope only.

## 2. Dated source/current-status refresh — 17 September 2026

Current primary sources checked:

1. Nikhil Bansal and Haotian Jiang, *Decoupling via Affine Spectral-Independence: Beck-Fiala and Komlos Bounds Beyond Banaszczyk*, arXiv:2508.03961. It gives the earlier full Boolean `\widetilde O((\log n)^{1/4})` Komlos bound.
2. Shengtao Guo, Ethan X. Fang and Junwei Lu, *Vector Balancing via Directional Total Variation*, arXiv:2609.11189v1, submitted 10 September 2026. Its main theorem states the unrestricted deterministic real Boolean bound `< 3 sqrt(2 pi)`, independent of dimension and family size.
3. Nestor Guillen and Vladimir A. Kobzar, *The Komlos conjecture for complex discrepancy*, arXiv:2609.15071v1, submitted 14 September 2026. It allows arbitrary unit-modulus complex phases; for real inputs that is rank-two vector discrepancy, not Boolean signing.

A fresh bounded search also checked combinations of `Komlos`, `block`, `grouping`, `two-stage signing`, `composition`, `sqrt ceil(n/k)`, and `vector balancing`. I did not locate the exact finite-column recurrence proved below. This is not a novelty certificate: the proof is elementary enough that the mechanism should be treated as **potential folklore unless a more exhaustive citation search says otherwise**. Novelty is therefore **UNVERIFIED**.

The source-level Guo--Fang--Lu universal theorem already has two distinct internal fleet audits, `R12-AUDIT-R13-KOMLOS-01=PASS` and `P26-AUDIT-R13-GFL-KOMLOS-ENDTOEND-11=PASS`. Those audits explicitly do not cover R13's later finite-`n` sharpenings, including the theorem below.

## 3. New methods used this run

The preceding run used `#2,#11,#21`; the old initial triple `#1,#10,#20` was already exhausted. The only three section-B moves not previously used by R13 were `#22,#28,#29`, so this run used all three.

### #22 — READ THE FAILURES, NOT THE SUCCESSES

The recent R13 sequence had already identified the failure mode of the one-row route. At `n=8,9` the row-incidence compiler is sharp at its threshold on principal subcubes, and at `n=10` the direct shifted-family extension already has an exact asymmetric obstruction to the naive uniform-facet certificate (`26784/49 > 384`). Rather than manufacture another one-row anticode lemma, I changed scale and asked whether the already certified small-`n` bounds compose.

### #28 — REPLACE “FOR ALL” WITH “FOR TYPICAL”

Inside one block of columns, I stopped trying to construct an optimal internal signing. A uniformly random internal signing has an **exact mean squared Euclidean norm** equal to the block's total column energy. Therefore at least one internal signing is no worse than that mean. This one probabilistic-method line is the engine of the composition theorem.

### #29 — CLOSE THE BOUNDARY

The block theorem is stated for every `n <= k q`, not only divisible cases. I close the decomposition under empty blocks and the zero aggregate vector. This removes every residue class/boundary case: incomplete final blocks and empty padded blocks require no separate argument. I also checked the extremal boundary of the internal step: `q` orthonormal unit vectors force Euclidean norm exactly `sqrt(q)` for every internal signing, so the internal `sqrt(q)` factor itself cannot be improved in a theorem using only a per-block Euclidean norm bound.

## 4. R13-C22 — block-composition theorem

Let `B(k)` be any certified constant with the following arbitrary-row meaning: every finite family of exactly `k` vectors `w_1,...,w_k` in an arbitrary real Euclidean space, each satisfying `||w_i||_2 <= 1`, has Boolean signs `sigma_i` with

\[
\left\|\sum_{i=1}^k \sigma_i w_i\right\|_\infty\le B(k).
\]

(As usual, families with fewer than `k` vectors are padded by zeros.)

### Theorem C22

For every positive integers `n,k,q` with `n <= k q`,

\[
\boxed{B(n)\le \sqrt q\,B(k).}
\tag{4.1}
\]

Equivalently, for every `1 <= k <= n`,

\[
\boxed{B(n)\le B(k)\sqrt{\left\lceil\frac nk\right\rceil}.}
\tag{4.2}
\]

### Proof

Let `v_1,...,v_n` be arbitrary real vectors with `||v_j||_2 <= 1`. Partition the indices into `k` blocks

\[
G_1,\ldots,G_k,
\qquad |G_i|\le q,
\]

allowing empty blocks.

For one block `G_i`, choose independent uniform signs `delta_j in {−1,+1}`. Expanding the square and averaging,

\[
\begin{aligned}
\mathbb E_\delta\left\|\sum_{j\in G_i}\delta_jv_j\right\|_2^2
&=\sum_{j\in G_i}\|v_j\|_2^2
 +\sum_{j\ne \ell}\mathbb E(\delta_j\delta_\ell)\langle v_j,v_\ell\rangle\\
&=\sum_{j\in G_i}\|v_j\|_2^2\\
&\le |G_i|\\
&\le q.
\end{aligned}
\tag{4.3}
\]

Hence there exists a deterministic internal signing for which

\[
u_i:=\sum_{j\in G_i}\delta_jv_j,
\qquad \|u_i\|_2\le\sqrt q.
\tag{4.4}
\]

Set `w_i=u_i/sqrt(q)` (and `w_i=0` for an empty block). Then `||w_i||_2<=1`. Apply the certified `k`-column bound to obtain outer signs `sigma_i` such that

\[
\left\|\sum_{i=1}^k\sigma_iw_i\right\|_\infty\le B(k).
\]

Multiplying by `sqrt(q)` and defining the original signs by

\[
\varepsilon_j=\sigma_i\delta_j\qquad(j\in G_i)
\]

gives

\[
\left\|\sum_{j=1}^n\varepsilon_jv_j\right\|_\infty
=\left\|\sum_{i=1}^k\sigma_i u_i\right\|_\infty
\le\sqrt q\,B(k).
\]

This proves (4.1), and (4.2) follows with `q=ceil(n/k)`. `QED`

The theorem is fully deterministic as an existence statement. Random signs occur only in the averaging argument proving that one internal signing exists.

## 5. R13-X07 — exact limitation of the internal block step

The factor `sqrt(q)` in (4.1) cannot be lowered if the only information retained from a block is that it contains at most `q` Euclidean-unit vectors.

Take `q` orthonormal unit vectors `e_1,...,e_q`. For every Boolean signing,

\[
\left\|\sum_{j=1}^q\delta_je_j\right\|_2^2=q.
\]

Thus every internal signing has norm exactly `sqrt(q)`. This does **not** prove that the final Komlos recurrence (4.1) is globally sharp: a stronger method may couple the blocks and outer signs simultaneously. It does prove that simply replacing (4.4) by a universally smaller per-block Euclidean bound is impossible.

## 6. R13-C23 — new complete certified envelope

Apply C22 to the already certified small-column bounds

\[
B(4)=\sqrt3,
\quad B(5)\le2,
\quad B(6)\le\frac3{\sqrt2},
\quad B(7)\le\frac{\sqrt{21}}2,
\quad B(8)\le\sqrt6,
\quad B(9)\le\frac{3\sqrt3}{2}.
\]

For `n >= 10`, define the exact block envelope by its square

\[
\boxed{
F(n)^2=
\min\left\{
3\left\lceil\frac n4\right\rceil,
4\left\lceil\frac n5\right\rceil,
\frac92\left\lceil\frac n6\right\rceil,
\frac{21}{4}\left\lceil\frac n7\right\rceil,
6\left\lceil\frac n8\right\rceil,
\frac{27}{4}\left\lceil\frac n9\right\rceil
\right\}.
}
\tag{6.1}
\]

Then C22 gives `B(n) <= F(n)`.

The exact checker compares (6.1) against **every retained pre-run rational entry for `10 <= n <= 61`** and verifies strict improvement in all 52 cases. It also compares against the Guo--Fang--Lu universal constant on `62 <= n <= 72` and verifies another 11 strict improvements. Thus **63 distinct values move in this run**.

Some anchor values are

\[
\begin{array}{c|c}
n & F(n)\\ \hline
10 & 2\sqrt2\\
11,12 & 3\\
13,14 & \sqrt{21/2}\\
15,16 & \sqrt{12}\\
17,18 & \sqrt{27/2}\\
19,20 & \sqrt{15}\\
61,62,63 & \sqrt{189/4}\\
64 & \sqrt{48}\\
71,72 & \sqrt{54}.
\end{array}
\]

At `n=72`,

\[
F(72)^2=54<18\pi=(3\sqrt{2\pi})^2
\]

because `pi>3`. At `n=73`,

\[
F(73)^2=57>18\pi
\]

because `pi<22/7` implies `18 pi < 396/7 <57`. Each of the six functions in the minimum (6.1) is nondecreasing in `n`, hence their pointwise minimum is nondecreasing. Therefore **for this certified block envelope** the crossover to the current universal Guo--Fang--Lu bound occurs at 73 and remains there thereafter.

The complete retained pointwise certificate is consequently

\[
\boxed{
B_{R13}(n)=
\begin{cases}
1,&n=1,\\
\sqrt2,&n=2,\\
(\sqrt{11}+\sqrt2)/3,&n=3,\\
\sqrt3,&n=4,\\
2,&n=5,\\
3/\sqrt2,&n=6,\\
\sqrt{21}/2,&n=7,\\
\sqrt6,&n=8,\\
3\sqrt3/2,&n=9,\\
F(n),&10\le n\le72,\\
3\sqrt{2\pi},&n\ge73.
\end{cases}}
\tag{6.2}
\]

The entries `n=1,2,3,4` retain their earlier exact-value status. The entries `n>=5` in (6.2) are upper certificates unless an earlier report separately established exactness. Equation (6.2) is a complete pointwise upper-bound function, not an assertion that each displayed upper bound is optimal.

The block recurrence also closes under iteration: if a later `B(k)` used in a second block step was itself obtained from one of the primitive bases in (6.1), composing the two ceiling factors cannot beat applying that primitive base directly, because

\[
\left\lceil\frac nk\right\rceil
\left\lceil\frac kr\right\rceil
\ge
\left\lceil\frac nr\right\rceil.
\tag{6.3}
\]

So repeated use of C22 does not secretly produce a stronger value than (6.1) from these same primitive inputs.

## 7. Exact checker

Checker:

`artifacts/R13/20260917T0538Z_block-composition-a6f2_checker.py`

Archived output:

`artifacts/R13/20260917T0538Z_block-composition-a6f2_output.txt`

The checker was executed before upload and ends `ALL_EXACT_CHECKS_PASS`. Its acceptance tests use exact integers/Fractions. It verifies:

- all 52 strict comparisons against the previous rational table on `10..61`;
- the exact new values `F(10)^2=8`, `F(61)^2=F(62)^2=F(63)^2=189/4`, `F(72)^2=54`, and `F(73)^2=57`;
- monotonicity numerically on a wide sanity range, while the all-`n` proof is on the page;
- an exact rational Machin bracket `3 < pi < 22/7`;
- all 11 strict comparisons `F(n)<3 sqrt(2 pi)` for `62..72`;
- `3 sqrt(2 pi)<F(73)`;
- the total movement count `52+11=63`.

Local pre-upload SHA-256 values:

- checker: `cb74590c4749101297dec867048353e789102039c34cdb8cc3324a761a995edf`;
- raw executed output: `82f091c908025aae17ec51b0c658c2cb867472f63b3953b555cd17c09a437fab`.

GitHub creation commits:

- checker: `7503446cae17d229a60b85c136864d7600f724eb`;
- output: `ffb9494fd1b4a29ef5ba81d473b871e2961b0e36`.

This checker is a **self-check**, not an independent audit.

## 8. What the movement means and what it does not mean

The gain is not a new universal constant theorem. Guo--Fang--Lu already provide the current universal Boolean constant `3 sqrt(2 pi)`. The new point is quantitative finite-column interpolation: strong small-`n` arbitrary-row certificates can be composed, and this replaces the previous mixed-tail table on every `n=10,...,61` and extends finite-column improvements eleven dimensions beyond it.

The composition theorem also explains why the old table looked irregular: once several base dimensions have squared discrepancy-per-column near `3/4`, the correct first comparison is no longer against `sqrt(n)` or a separately optimized one-dimensional tail at every `n`; it is against the lower envelope of the six staircase functions in (6.1).

The next genuinely different route is **not** another refinement of (4.3). X07 makes the `sqrt(q)` internal factor sharp for isolated blocks. Further progress must correlate the internal and outer sign choices, use overlap among blocks, or produce a better primitive base value (for example lower `B(5),...,B(10)`) and then re-run the composition envelope.

## 9. Audit and closure status

- Universal Guo--Fang--Lu package: `R12-AUDIT-R13-KOMLOS-01=PASS` and `P26-AUDIT-R13-GFL-KOMLOS-ENDTOEND-11=PASS` — **2/2 distinct audits for that external universal theorem only**.
- New C22/C23 block-composition result: full proof on this page + exact envelope self-check, but **no independent OTHER-track audit yet**.
- Prior-art search: bounded and recorded; no exact recurrence source located, but the mechanism is elementary and **novelty remains UNVERIFIED / potentially folklore**.

Therefore this run is **PARTIAL / metric moved / finite-n composition audit pending**, not fleet-closed.

## 10. Model and scheduler-control status

The situation is still the same at the native runtime-control level. The exposed task-update interface offers task prompt/title/schedule/enabled/timing controls, but no model selector and no reasoning-effort selector. Thus the text `GPT-6 / maximum` is only a request embedded in the prompt; it is not authenticated runtime configuration. This run actually identifies as GPT-5.6 Sol, with reasoning metadata UNVERIFIED.

The repository also records that a native `You cannot modify this task` error is context/ownership-dependent: P26 was later successfully modified from an authorized P/C context while R-series edits were denied from another exposed context. The legitimate workaround is an authorized task/workspace-owner context or platform support that exposes the native task/model fields. Duplicating the task or bypassing permissions is not an acceptable workaround. No scheduler change was attempted in this run.

## Status and structured ledger delta

```yaml
ledger_delta:
  track: "R13 HARD OUTSIDE"
  source: "Boolean Komlos real +/-1 vector balancing; Bansal-Jiang arXiv:2508.03961; current universal preprint Guo-Fang-Lu arXiv:2609.11189v1; complex/rank-two Guillen-Kobzar arXiv:2609.15071v1 excluded from Boolean scope"
  metric: "complete rigorously certified pointwise arbitrary-row bound B_R13(n)"
  before: "n<=9 as retained; B(10)=149/50; prior C16 rational table for 11<=n<=61; 3 sqrt(2 pi) for n>=62"
  after: "n<=9 retained; for 10<=n<=72, F(n)^2=min{3 ceil(n/4),4 ceil(n/5),(9/2)ceil(n/6),(21/4)ceil(n/7),6ceil(n/8),(27/4)ceil(n/9)}; for n>=73, 3 sqrt(2 pi)"
  movement: "strict improvement at every n=10,...,72 (63 entries); B(10):149/50 -> 2sqrt(2)"
  status: "PARTIAL / metric moved / C22-C23 independent audits pending; source-level GFL universal theorem has 2/2 audits"
  stagnation_count: 0
  methods: [22, 28, 29]
  checker: "artifacts/R13/20260917T0538Z_block-composition-a6f2_checker.py @ 7503446cae17d229a60b85c136864d7600f724eb"
  output: "artifacts/R13/20260917T0538Z_block-composition-a6f2_output.txt @ ffb9494fd1b4a29ef5ba81d473b871e2961b0e36"
  remaining_obligation: "independent audits of C22/C23 and deeper prior-art check; any further movement must correlate block/internal and outer choices or improve primitive small-n bases, since isolated-block sqrt(q) is sharp"
```

No shared root ledger, peer file, email, Drive object, public post, permission, workflow, purchase, or scheduler setting was changed.
