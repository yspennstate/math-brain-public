Model actually run: GPT-5.6 Sol. Reasoning level: UNVERIFIED — GPT-6 maximum was requested in prompt text, but the exposed scheduler still has no model or reasoning selector, so GPT-6/maximum is not claimed. **NO MOVEMENT:** `W_exp = UNMEASURED -> UNMEASURED`; methods actually tried this run: **#2 attack the negation first, #18 say it in another language, #24 find the extremal object**.
Problem/source: **R16 / I0112 — Justin Salez (2025), arXiv:2508.21055v1, Problem 2.3: prove cutoff for all bounded-degree vertex-transitive expanders.** Status: **PARTIAL / first I0112 research run after mandatory I0013 handoff**.

# R16 — rotate from exhausted I0013 to Salez Problem 2.3; fixed products cannot be the counterexample

Run ID: `2026-09-16T18-48-00Z_i0112-product-varentropy`.
Repository: `yspennstate/math-open-problems`, branch `master`.

## 1. Continuity, mandatory handoff, and source admission

The preceding complete R16 report was read before research:

`runs/R16/2026-09-16T17-42-40Z_i0013-stuck-recovery-2.md`.

It records `STUCK_RECOVERY_2` on I0013, with frozen metric

\[
r_{\rm bad}=
\sup\{\gamma/\alpha<2:\text{source-valid Matsui/Bradley counterexample certified}\}
\]

still `UNMEASURED`, unchanged count 4. Its exact remaining blocker was recovery of the corrected Bradley (1987) parameter system and one explicit source-authentic coefficient `d_B>0`. The route had exhausted the two hard-target recoveries allowed by `operations/NEW_METHODS_2026-09-16.md`.

**I0013 handoff:** R16 therefore stops attacking I0013. Durable state for reassignment is: the base-two normalization compiler is preserved in earlier R16 reports; a literal Bradley coefficient transfers with the recorded `ln 2` correction; the unresolved source task is to recover corrected Bradley Theorem 1/Proposition 0, `A_j,B_tau`, all admissibility inequalities, and one exact positive `d_B`. No further I0013 claim is made here.

The mandatory campaign/root state was refreshed before rotation: `probability_campaign_2026_09/INDEX.md`, `RANKING.md`, root `POSTED.md`, root `RESULTS.md`, root `QUEUE.md`, `operations/NEW_METHODS_2026-09-16.md`, the newest own R16 report, the current R12 report, neighboring Salez rows I0110/I0113, and the intake record. Corpus-scale connector responses can truncate, so I do not claim a semantic line-by-line reread of every one of the roughly 780 intake rows.

The originating Beck--Fiala source is not reopened. A fresh 16 September 2026 primary search again found Guo--Fang--Lu, arXiv:2609.11189v1 (submitted 10 September 2026), explicitly proving the stronger Komlós theorem and the all-`t` Beck--Fiala consequence

\[
\operatorname{disc}(A)<3\sqrt{2\pi t}.
\]

Bansal--Jiang arXiv:2508.03961 remains the earlier baseline (`t\ge\log^2 n` for square-root order, polylogarithmic loss below), and Altschuler--Tikhomirov arXiv:2607.14238 reaches essentially logarithmic sparsity. No v2/withdrawal/proof-specific correction to Guo--Fang--Lu was found in the bounded search. This literature resolution is why the active R16 research target must rotate rather than duplicate R13.

### Queue/ownership screening

The high-ranked reserve was checked in order rather than claimed blindly. I0011 is already owned by P16; I0035 by C31; I0054 by R11; I0055 is no longer open in the queue's current source scope; I0070 is owned by R10; I0068 by P19. The queue's I0111 is the much broader request to characterize cutoff on vertex-transitive graphs. I0112 is the sharper source yes/no conjecture and had no canonical claim or mathematical attempt in repository-wide search immediately before creation.

A create-only claim was therefore made and read back:

`operations/claims/I0112.md` @ commit `6edb4a257e314f1f972b0ba510a151bdad98beb3`.

The exact source statement, from Salez Problem 2.3, is:

> For every sequence of finite undirected vertex-transitive graphs with sizes tending to infinity, uniformly bounded degrees and spectral gaps bounded away from zero, prove that simple random walk exhibits total-variation cutoff.

A fresh current-status search found no general resolution. In particular, Dylan Altschuler's arXiv:2609.14945 (14 September 2026) proves cutoff with Gaussian profile for fixed-degree **long-range expanders**, and explicitly describes this as intermediate progress between Ramanujan cutoff and the long-standing conjecture for transitive spectral expanders. Thus I0112 remains source-open in the bounded search.

The frozen progress quantity for R16/I0112 is

\[
W_{\exp}:=
\inf\left\{w\in[0,1]:
\begin{array}{l}
\text{R16 proves a new source-admissible vertex-transitive expander family}\
\text{has cutoff window }O((\log|V|)^w)
\end{array}
\right\},
\]

with value `UNMEASURED` until a class outside already-published cutoff classes is actually proved. Ramanujan/near-Ramanujan, long-range-expander and already-covered product-chain theorems are baselines and do not move this metric.

## 2. Method #2 — attack the negation first: try to manufacture a transitive expander without cutoff

The first counterexample attempt was to combine two transitive expanders with different mixing mechanisms so that the product has two macroscopic relaxation scales and hence a broad transition. The cleanest version is the Cartesian graph product. It fails completely: a fixed Cartesian product of cutoff transitive expanders is again cutoff.

### R16-I0112-C01 — fixed Cartesian products preserve cutoff

**Status: PROVED as a theorem; mechanism is standard/product-chain folklore and is not claimed novel.**

Let `k` be fixed. For each `j=1,...,k`, let `G_{j,n}` be a finite connected `d_j`-regular graph, where the degrees `d_j` are fixed in `n`. Let `P_{j,n}` be simple random walk and let

\[
H_{j,n}(t)=\exp\{t(P_{j,n}-I)\}
\]

be Salez's continuous-time convention. Assume the `j`th family has total-variation cutoff at time `t_{j,n}` with window `w_{j,n}=o(t_{j,n})` in the standard window sense.

Let

\[
G_n=G_{1,n}\square\cdots\square G_{k,n},
\qquad D=\sum_{j=1}^k d_j,
\qquad a_j=d_j/D.
\]

Then simple random walk on `G_n` has cutoff at

\[
T_n=\max_j\frac{t_{j,n}}{a_j}
\]

with window

\[
W_n=\max_j\frac{w_{j,n}}{a_j}=o(T_n).
\tag{C01.1}
\]

If every factor family is vertex-transitive, so is the product. If in addition every factor has spectral gap bounded below, then so does the product.

#### Proof

The transition operator on the Cartesian product is

\[
P_n=\sum_{j=1}^k a_j
\bigl(I\otimes\cdots\otimes P_{j,n}\otimes\cdots\otimes I\bigr).
\]

Hence

\[
P_n-I=\sum_{j=1}^k a_j
\bigl(I\otimes\cdots\otimes(P_{j,n}-I)\otimes\cdots\otimes I\bigr).
\]

The summands commute, so the continuous-time semigroup factorizes exactly:

\[
H_n(t)=\bigotimes_{j=1}^k H_{j,n}(a_jt).
\tag{C01.2}
\]

For probability measures `mu_j,pi_j`, total variation satisfies

\[
\max_j\|\mu_j-\pi_j\|_{\rm TV}
\le
\left\|\bigotimes_j\mu_j-\bigotimes_j\pi_j\right\|_{\rm TV}
\le
\sum_j\|\mu_j-\pi_j\|_{\rm TV}.
\tag{C01.3}
\]

The lower bound is projection; the upper bound follows by telescoping the product and using that tensoring with a probability measure preserves total variation.

Choose an index `j_*` realizing `T_n=t_{j_*,n}/a_{j_*}`. At time `T_n-cW_n`,

\[
a_{j_*}(T_n-cW_n)
=t_{j_*,n}-c a_{j_*}W_n
\le t_{j_*,n}-c w_{j_*,n}.
\]

By the factor's cutoff and the lower inequality in (C01.3), the product distance tends to one as first `n\to\infty` and then `c\to\infty`.

For every `j`, at time `T_n+cW_n`,

\[
a_j(T_n+cW_n)
\ge t_{j,n}+c a_jW_n
\ge t_{j,n}+cw_{j,n}.
\]

Each factor distance therefore tends to zero, and the upper inequality in (C01.3) gives product distance tending to zero. Because `k` and the `a_j` are fixed,

\[
\frac{W_n}{T_n}
\le \max_j\frac{w_{j,n}}{t_{j,n}}\to0.
\]

This proves cutoff and (C01.1).

For the gap statement, the eigenvalues of the product generator are sums of the scaled factor-generator eigenvalues, so

\[
\operatorname{gap}(G_n)=\min_j a_j\operatorname{gap}(G_{j,n}).
\]

Vertex transitivity is preserved coordinatewise.  QED.

### Consequence for the negation route

No counterexample to Salez Problem 2.3 can be obtained by taking a **fixed** Cartesian product of already-cutoff transitive expander families, even if the factors have distinct cutoff locations. This is exactly the kind of tempting two-scale construction one would try first.

This mechanism is not presented as new. Chen--Kumagai and related product-chain literature studies coordinate-update product chains and cutoff criteria. C01 is retained as an exact source-convention obstruction, not as metric movement or a novelty claim.

## 3. Method #24 — extremal object: products are far outside long-range expansion but still cutoff

Altschuler's 2026 theorem shows cutoff for every fixed-degree long-range expander. A natural suspicion is that the tree-like long-range growth hypothesis might be close to necessary. C01 gives a clean adversarial family showing it is not.

Take a fixed-degree family `G_n` and its Cartesian square

\[
H_n=G_n\square G_n.
\]

If `G_n` is `d`-regular, then `H_n` is `2d`-regular. For every radius `ell`, the universal tree bound gives a constant `C_d` such that

\[
|S_{G_n}(v,r)|\le C_d(d-1)^r.
\]

Since Cartesian distance is additive,

\[
|B_{H_n}((v,v),\ell)|
\le C_d^2\sum_{r+s\le\ell}(d-1)^{r+s}
\le C'_d(\ell+1)^2(d-1)^\ell.
\tag{C01.4}
\]

Long-range expansion at degree `2d` would require, for a singleton and all relevant `ell`, growth at least a fixed positive multiple of

\[
(2d-1)^\ell
\]

until macroscopic saturation. Choosing

\[
\ell_n=\left\lfloor\frac12\log_{2d-1}|V(H_n)|\right\rfloor
\]

keeps the required lower bound below the saturation cutoff while

\[
\frac{|B_{H_n}((v,v),\ell_n)|}{(2d-1)^{\ell_n}}
\le
C'_d(\ell_n+1)^2
\left(\frac{d-1}{2d-1}\right)^{\ell_n}
\to0.
\]

Thus every fixed Cartesian square fails the long-range expansion condition at large enough size, even though C01 preserves cutoff. If the factors are transitive spectral expanders, the squares are transitive spectral expanders as well.

**Interpretation:** tree-like long-range growth is a powerful sufficient mechanism but cannot be necessary for cutoff on transitive spectral expanders. A counterexample hunt must target a more irreducible source of information spreading than a bounded number of independent/product coordinates.

### Attempt to escape known product-chain theory: direct/tensor graph products

To avoid the exact coordinate-update factorization, I also examined the direct graph square `G_n\times G_n`, whose adjacency matrix is `A\otimes A` and degree is `d^2`. This is a genuinely different continuous-time walk: the Poisson clock moves both coordinates simultaneously, so the semigroup is **not** a tensor product of the two continuous-time factor semigroups. It therefore remains a candidate for a new source-admissible special class rather than an immediate corollary of C01.

Two exact structural facts were proved.

1. Its local growth is also far below the degree-`d^2` long-range scale. The universal bound has base `(d-1)^2`, whereas the long-range benchmark has base `d^2-1`; exactly

\[
\frac{(d-1)^2}{d^2-1}=rac{d-1}{d+1}<1.
\tag{C01.5}
\]

2. It eventually leaves the Ramanujan class even if the factor is Ramanujan. If `G` is simple `d`-regular on `n` vertices with adjacency eigenvalues `d=\lambda_1,\lambda_2,\ldots,\lambda_n`, then `\operatorname{tr}A^2=nd`, so

\[
\max_{i\ge2}|\lambda_i|^2
\ge \frac{d(n-d)}{n-1}.
\tag{C01.6}
\]

The tensor-square adjacency has a nontrivial eigenvalue `d\lambda_i`. Hence it is certified non-Ramanujan whenever

\[
d^3\frac{n-d}{n-1}>4(d^2-1).
\tag{C01.7}
\]

For `d=6`, the exact threshold from (C01.7) is `n\ge16`.

The exact self-check verifies (C01.5), the `d=6` threshold, and the elementary tensor-TV inequalities on 50,625 rational quadruples. It is archived at

- `artifacts/R16/R16_2026-09-16_1848Z_i0112_tensor_obstruction_checker.py` @ `a5aa6fba7ba68e99c41049e50e98ed1363efa8ec`;
- output @ `08e770e2929b8be18775306c728bc18a2c6937c7`, ending `ALL_EXACT_CHECKS_PASS`.

This tensor-square route is **not yet a theorem moving `W_exp`**. What remains is to prove cutoff in Salez's continuous-time convention for a concrete transitive expander factor family and to clear the resulting class against Bordenave--Lacoin/other covered-expander and product-chain theorems. A discrete-time identity `(P\otimes P)^k=P^k\otimes P^k` is not by itself enough because the source problem is continuous time.

## 4. Method #18 — say it in another language: the conjecture is an information-concentration problem

Salez's varentropy program gives a much sharper formulation of what a counterexample must do.

For a sparse fast-mixing chain, the relevant information-content random variable is the log-density of the time-`t` law relative to stationarity, and its variance is the **varentropy**. Salez's cutoff criterion gives, in the notation of the lecture notes, a sufficient condition of the form

\[
\gamma\,t_{\rm mix}(\varepsilon)
\gg
1+\sqrt{V_\varepsilon},
\tag{C01.8}
\]

where `gamma` is the spectral gap and `V_epsilon` is the worst-case varentropy at the relevant mixing scale. Salez's separate paper *The varentropy criterion is sharp on expanders* proves that, for sparse fast-mixing chains, this information-concentration criterion is in fact equivalent to cutoff.

For the source class I0112, bounded degree plus a spectral gap bounded below gives

\[
t_{\rm mix}(\varepsilon)=\Theta(\log |V|),
\qquad \gamma\ge\gamma_0>0.
\]

Therefore the clean target becomes

\[
\boxed{
V_\varepsilon=o((\log |V|)^2)
\quad\text{for every bounded-degree vertex-transitive expander sequence.}
}
\tag{C01.9}

Conversely, any counterexample must force information fluctuations on the maximal `log^2 |V|` scale at some relevant mixing time. This translation is useful because it says exactly what the next construction or proof has to control; spectral expansion alone fixes the mean mixing scale but not the concentration of information.

It also explains why fixed Cartesian products fail as counterexamples: in the exact product semigroup (C01.2), information content is a sum of finitely many independent coordinate information contents, so varentropy adds. A bounded number of factors cannot turn `o(log^2 n)` factor varentropy into a new `Theta(log^2 n)` obstruction merely by product composition.

This section is a reduction/interpretation using Salez's published criterion, not an original solution.

## 5. Prior-art and current-status audit

Dated 16 September 2026 searches covered:

- Salez arXiv:2508.21055 and its vertex-transitive/expander open problems;
- Dylan Altschuler arXiv:2609.14945, *Long-range expanders: construction and cutoff*;
- Salez, *The varentropy criterion is sharp on expanders*, arXiv:2307.10066;
- Chen--Kumagai product-chain cutoff literature;
- Bordenave--Lacoin, cutoff at entropic time for covered expander graphs;
- direct/tensor/Kronecker graph-product random-walk cutoff searches;
- the current Beck--Fiala comparison sources Guo--Fang--Lu arXiv:2609.11189 and Bansal--Jiang arXiv:2508.03961.

The fresh Altschuler abstract explicitly still calls cutoff for transitive spectral expanders a long-standing conjecture. No later general solution was found. A bounded negative search is not proof of worldwide novelty.

The Cartesian-product mechanism is treated as known/folklore because product-chain cutoff has a substantial literature. The direct/tensor-square candidate has **unresolved prior-art status**: the bounded searches did not produce an exact source-convention theorem for this class, but that negative search is not enough to claim novelty. In particular, Bordenave--Lacoin's covered-expander theorem must be checked against any concrete tensor family before metric credit.

## 6. Why the frozen metric does not move

`W_exp` stays `UNMEASURED`.

C01 is a genuine theorem-sized obstruction and the long-range failure calculation is rigorous, but the Cartesian-product cutoff mechanism belongs to known product-chain theory. The direct/tensor-square candidate escapes the immediate factorization and the Ramanujan/long-range classes, but its continuous-time cutoff and prior-art exclusion are not yet proved. Counting either as a new covered family would violate the frozen metric.

This is therefore substantive route narrowing, not artificial progress relabeling.

## 7. R12 directed-audit dependency

R12's current assignment was refreshed from the repository. Its newest located report is

`runs/R12/2026-09-16T17-30-35Z_stuck1_91c4e7.md`,

on the Paley degree-four SOS / I0102 target. It is explicitly `STUCK RECOVERY 1`, not a complete source-level package. Therefore

`R16_AUDIT_R12 = PENDING_NOT_READY`.

No spot check is counted as an independent audit.

## 8. Model/runtime escalation

The limitation remains exactly as stated in the controlling repository policy. The exposed scheduler update interface has fields for title, prompt, schedule, timing mode and enabled state, but **no model selector and no reasoning-effort selector**. The requested `GPT-6 / maximum` line is therefore prompt text only. This invocation actually identifies as `GPT-5.6 Sol`; reasoning effort is `UNVERIFIED`.

Changing this requires the authorized product scheduler/API/UI itself to expose model and reasoning fields, or an account/workspace administrator/platform-support action moving the task to an interface that does. GitHub edits cannot alter native runtime metadata.

The current policy also records historical modification probes for P26/P01/P03 returning `You cannot modify this task`. The compliant workaround is correction of task/account/workspace ownership through the authorized product interface or platform support. Duplicate schedules and permission bypass are prohibited. No scheduler modification was attempted here.

## 9. Next attack

The next run should not repeat `#2,#18,#24`. The most promising concrete route is the **direct/tensor square** of an explicit non-bipartite transitive Ramanujan family (for example an LPS family):

1. prove continuous-time cutoff despite the shared Poisson clock, preferably by combining the known discrete-time Gaussian cutoff profile with sharp Poisson concentration;
2. determine whether the resulting tensor family is already covered by Bordenave--Lacoin or another entropic/cover theorem;
3. if it is genuinely outside published classes, record the Gaussian `O(sqrt(log |V|))` window and move `W_exp` to `1/2`; otherwise treat it as another obstruction and move immediately to a non-product group construction.

Proposed new-method triple for that run: **#10 derandomize/Poissonize explicitly, #11 dualize to spectrum/information, #15 break product symmetry deliberately**.

## 10. Structured ledger delta

```yaml
ledger_delta:
  track: R16
  handoff:
    previous_claim: I0013
    status: "HANDOFF AFTER STUCK_RECOVERY_2; no further R16 attack"
    metric: "r_bad"
    last_value: UNMEASURED
    blocker: "corrected Bradley 1987 formulas and one explicit source-authentic d_B>0"
  current_claim: I0112
  canonical_claim: "operations/claims/I0112.md @ 6edb4a257e314f1f972b0ba510a151bdad98beb3"
  source: "Justin Salez (2025), arXiv:2508.21055v1, Problem 2.3"
  target: "cutoff for every bounded-degree vertex-transitive spectral expander sequence"
  metric: "W_exp = smallest new rigorously certified cutoff-window exponent outside already-published classes"
  before: UNMEASURED
  after: UNMEASURED
  movement: "NO MOVEMENT"
  status: "PARTIAL"
  unchanged_count_on_I0112: 1
  methods: [2, 18, 24]
  exact_evidence:
    - "R16-I0112-C01 fixed Cartesian products preserve continuous-time cutoff"
    - "Cartesian products can fail long-range expansion exponentially"
    - "tensor-square growth ratio (d-1)/(d+1)<1 and exact non-Ramanujan trace certificate"
    - "artifacts/R16/R16_2026-09-16_1848Z_i0112_tensor_obstruction_checker.out ends ALL_EXACT_CHECKS_PASS"
  audit_ids:
    p26: "PENDING / not counted"
    r12: "PENDING_NOT_READY / not counted"
  next_obligation: "prove and prior-art classify continuous-time cutoff for an explicit direct/tensor-square transitive expander family"
```

**NO CLOSURE CLAIM.** I0112 remains open.
