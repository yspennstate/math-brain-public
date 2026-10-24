Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — this is not GPT-6 at maximum, and I do not claim otherwise. Frozen metric MOVED: `L <= Delta_2(Q): 250/2989 -> 2500/29711`. Methods tried: B10 / B14 / B16.**

# HARD7-03 — four-step pair-overlap Chernoff bound

Status: **PARTIAL / Seppäläinen Problem 4 remains open as a whole.** This run resumes the exclusive `D0025` claim and the latest three-step checkpoint. The substantive gain is a new four-step homogeneous lazy-LPP bound obtained without enumerating the full four-layer max-plus chamber arrangement. The resulting certified binary-disorder plateau half-width improves from `250/2989` to `2500/29711`.

## 1. Continuity, ownership, and required repository state

The active canonical claim remains

`operations/claims/D0025.md`

owned by `HARD7-03`, canonical intake key `disordered_asep_open_1999::problem_4`. I re-read the controlling HARD7 policy, `operations/NEW_METHODS_2026-09-16.md`, `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md`, campaign `INDEX.md` and `RANKING.md`, root `POSTED.md`, `RESULTS.md`, `QUEUE.md`, the claim file, the indexed D0025 intake/source material, the own checkpoint chain through

`runs/hard7_2026-09-18/HARD7-03/20260919T0522Z__d0025-three-step-order-cone-chernoff.md`,

and the newest neighboring HARD7-02 / HARD7-04 state available during this run. HARD7-02 has since entered its own STUCK1 report at commit `03c1a571e9dd69de6aac79956da5a6212fe130e3`; HARD7-04 remains on the distinct P0157 random-graph target, latest substantive checkpoint `ce1a10066959f2f13a5933a1c27dc5c0870d8df7`. No ownership collision, release, posted equivalent, or active alias of D0025 surfaced.

The shared root ledgers are not edited by this worker. A structured `ledger_delta` appears below for the designated reconciler.

A repository search of the preceding D0025 method labels showed B10, B14, and B16 had not been used as the three numbered methods on this target. This run therefore does not reuse the previous B4/B11/B30 triple.

## 2. Source and current-status refresh

Primary source: Timo Seppäläinen, *Recent Results and Open Problems on the Hydrodynamics of Disordered Asymmetric Exclusion and Zero-Range Processes*, Resenhas IME-USP 4(1) (1999), 1–15, Problem 4, Section 4; DOI `10.11606/resimeusp.v4i1.74889`; arXiv `math/9906194`.

Official source page checked 2026-09-19:

`https://revistas.usp.br/resenhasimeusp/pt_BR/article/view/74889`

ArXiv source:

`https://arxiv.org/abs/math/9906194`

The source's particle-system question asks for the phase-transition / flat-flux phenomenon for disordered asymmetric `K`-exclusion. The frozen residual here is **not** the known ordinary `K=1` result. It remains the `K>=2` iid site-disorder scope, with first fixed test case

\[
K=2,\qquad Q=\tfrac12\delta_{1/2}+\tfrac12\delta_1.
\]

A fresh bounded 2026-09-19 search used `disordered K-exclusion plateau site disorder K>=2 flux`, the exact source title, and adjacent `partial exclusion` terminology. It recovered the source and Gonçalves–Hayashi–Sasada, arXiv:2405.15142, on asymmetric partial exclusion under a different product-rate/gradient setup. No located 2024–2026 source closed Seppäläinen's exact iid site-rate `K>=2` plateau residual. This is bounded negative evidence only, not a worldwide openness or novelty certificate.

## 3. Frozen metric and before/after value

For the frozen binary law define

\[
\Delta_2(Q)=\sup\{\delta\ge0:
 f_{2,Q}\text{ is constant on }[1-\delta,1+\delta]\}.
\]

The stable metric is a rigorous certificate `L <= Delta_2(Q)` inside the current self-checked theorem chain.

Before:

\[
L_{\rm old}=\frac{250}{2989}=0.083640013382402\ldots.
\]

After:

\[
\boxed{L_{\rm new}=\frac{2500}{29711}=0.084143919760358\ldots.}
\]

The exact gain is

\[
L_{\rm new}-L_{\rm old}
=\frac{44750}{88806179}>0.
\]

As in the preceding checkpoints, the inherited site-disorder plateau argument gives for this frozen case

\[
\Delta_2(Q)\ge \frac{1}{4G_1(0)},
\tag{3.1}
\]

where `G_1(0)` is the rate-one homogeneous `K=2` lazy-LPP central shape constant. Thus the research task is to lower a rigorous upper bound on `G_1(0)` without changing the source model.

The preceding run proved

\[
G_1(0)\le\frac{2989}{1000}=2.989.
\tag{3.2}
\]

## 4. B10 — derandomize the fourth layer into a deterministic overlap inequality

The full exact four-step chamber integral is much larger than the three-step calculation. Instead of enumerating its chambers, this run first removes the difficult part of the fourth-layer maximum by a deterministic inequality.

For nonnegative `x,y,z`,

\[
\max(x,y,z)
\le x+y+z-\min(x,y)-\min(y,z).
\tag{4.1}
\]

For two variables there is equality:

\[
\max(x,y)=x+y-\min(x,y).
\tag{4.2}
\]

Equation (4.1) is checked directly by the three possible locations of the maximum. More precisely, there is the exact identity

\[
x+y+z-\min(x,y)-\min(y,z)-\max(x,y,z)
=(\min(x,z)-y)_+.
\tag{4.3}
\]

This last form will identify the remaining four-step obstruction below.

Apply (4.1)–(4.2) not to the passage times but to

\[
x_e=e^{\theta T_3(e)},
\]

where `T_3(e)` is the exact three-step homogeneous lazy-LPP passage value from the block start to displacement `e`. Since exponentiation preserves maxima,

\[
e^{\theta\max_eT_3(e)}=\max_e e^{\theta T_3(e)}.
\]

Thus an upper bound on the fourth-layer MGF can be obtained from the known one-endpoint three-step MGFs minus **positive pair-overlap corrections**. This is the category change that avoids a full four-step max-plus chamber decomposition while retaining nontrivial endpoint correlations.

**B10 outcome: successful.** The random fourth-layer endpoint competition is reduced to a deterministic positive-lattice inequality plus pair-minimum expectations.

## 5. Exact pair-overlap lower bound from a shared two-step predecessor

Let

\[
M_3(e;\theta)=\mathbb E e^{\theta T_3(e)},
\qquad
A_3(\theta)=\sum_{e=-3}^3M_3(e;\theta).
\]

The preceding exact order-cone calculation gives

\[
A_3(\theta)=
\frac{2(2268-4408\theta+3748\theta^2-1918\theta^3
+652\theta^4-143\theta^5+18\theta^6-\theta^7)}
{(3-\theta)^4(2-\theta)^3(1-\theta)^3}.
\tag{5.1}
\]

Now consider neighboring three-step endpoints `e,e+1`. Choose a two-step displacement `z` that can reach both endpoints in one step. If the independent third-layer endpoint weights are `C_e,C_{e+1}~Exp(1)`, then pointwise

\[
T_3(e)\ge T_2(z)+C_e,
\qquad
T_3(e+1)\ge T_2(z)+C_{e+1}.
\]

Hence

\[
\min(T_3(e),T_3(e+1))
\ge T_2(z)+\min(C_e,C_{e+1}).
\tag{5.2}
\]

Because `min(C_e,C_{e+1})~Exp(2)` and is independent of `T_2(z)`, for `0<theta<1`,

\[
\mathbb E e^{\theta\min(T_3(e),T_3(e+1))}
\ge M_2(z;\theta)\frac{2}{2-\theta}.
\tag{5.3}
\]

The exact two-step endpoint MGFs are elementary:

\[
M_2(\pm2;\theta)=\frac1{(1-\theta)^2},
\tag{5.4}
\]

\[
M_2(\pm1;\theta)=\frac2{(1-\theta)^2(2-\theta)},
\tag{5.5}
\]

\[
M_2(0;\theta)=
\frac6{(1-\theta)^2(2-\theta)(3-\theta)}.
\tag{5.6}
\]

Indeed, at time two the endpoint contributes one independent `Exp(1)` variable, while its predecessor set contains respectively one, two, or three iid `Exp(1)` weights; the MGF of the maximum of `r` iid unit exponentials is `r!/prod_{j=1}^r(j-theta)`.

## 6. B14 — reflection symmetry collapses all fourth-step pair corrections to three types

There are nine fourth-step displacements `d=-4,...,4`. Each `T_3(e)` is a predecessor of exactly three fourth-step endpoints, so the raw sum of predecessor MGFs over all fourth endpoints is exactly

\[
3A_3(\theta).
\tag{6.1}
\]

For a fourth endpoint with three predecessors, use the two chain-adjacent corrections from (4.1); for an endpoint with two predecessors, use the exact correction (4.2). Across all `d`, every adjacent pair `(e,e+1)` appears exactly twice.

The six adjacent pairs and a best common two-step predecessor are

\[
\begin{array}{c|c}
(e,e+1)&z\\ \hline
(-3,-2)&-2\\
(-2,-1)&-1\\
(-1,0)&0\\
(0,1)&0\\
(1,2)&1\\
(2,3)&2.
\end{array}
\tag{6.2}
\]

Reflection turns these into only three absolute predecessor types `|z|=0,1,2`. Since every adjacent pair is used twice, each absolute type appears four times in the total correction. Therefore the total pair correction has the rigorous lower bound

\[
C(\theta)
=\frac{8}{2-\theta}
\left(M_2(0;\theta)+M_2(1;\theta)+M_2(2;\theta)\right).
\tag{6.3}
\]

Let `D_d~Exp(1)` be the independent fourth-layer endpoint weight. Its MGF is `(1-theta)^{-1}`. Summing the fourth-step endpoint MGFs and applying (4.1)–(6.3) yields

\[
A_4^{\rm actual}(\theta)
:=\sum_{d=-4}^4\mathbb E e^{\theta T_4(d)}
\le
U_4(\theta)
:=\frac{3A_3(\theta)-C(\theta)}{1-\theta}.
\tag{6.4}
\]

**B14 outcome: successful.** The reflection group and path geometry reduce twelve pair-minimum terms to exactly three two-step MGF types, so a useful four-step bound needs no four-layer chamber enumeration.

## 7. B16 — exact four-step small-case certificate and a new shape bound

Concatenate independent four-step blocks. For a fixed coarse boundary sequence, distinct blocks use disjoint new time layers. The same Chernoff/union argument as in the preceding runs gives

\[
\Pr\{T_1(4m,0)\ge4ma\}
\le
\left[A_4^{\rm actual}(\theta)e^{-4\theta a}\right]^m
\le
\left[U_4(\theta)e^{-4\theta a}\right]^m.
\tag{7.1}
\]

Take the exact rational values

\[
\theta=\frac{147}{250},
\qquad
a=\frac{29711}{10000}.
\tag{7.2}
\]

The executed exact-arithmetic checker obtains

\[
U_4(147/250)
=
\frac{78796723997025150835937500000}
{72727683387654143845317033}
=1083.448837178295889\ldots,
\tag{7.3}
\]

and

\[
4\theta a=\frac{4367517}{625000}=6.9880272.
\tag{7.4}
\]

Let

\[
S_{20}(x)=\sum_{k=0}^{20}\frac{x^k}{k!}.
\]

For positive `x`, `S_20(x)<e^x`. Exact rational arithmetic gives

\[
S_{20}\!\left(\frac{4367517}{625000}\right)
-U_4(147/250)>0,
\tag{7.5}
\]

with exact positive fraction archived in the checker output; its decimal value is

\[
0.117515900350937\ldots.
\]

Therefore

\[
U_4(147/250)e^{-4\theta a}<1.
\]

The probabilities in (7.1) are summable in `m`. Borel–Cantelli, together with the homogeneous shape limit already used in the prior checkpoint chain, gives the new rigorous bound

\[
\boxed{G_1(0)\le\frac{29711}{10000}=2.9711.}
\tag{7.6}
\]

This strictly improves (3.2) by

\[
\frac{2989}{1000}-\frac{29711}{10000}
=\frac{179}{10000}.
\]

Combining (7.6) with the inherited plateau relation (3.1),

\[
\Delta_2(Q)
\ge\frac{1}{4G_1(0)}
\ge\frac1{4(29711/10000)}
=\boxed{\frac{2500}{29711}}.
\tag{7.7}
\]

**B16 outcome: successful.** The exact small block is not being confused with a finite simulation: it is an analytic block-MGF certificate used in an asymptotic Chernoff/Borel–Cantelli proof.

## 8. What the new method still loses

The four-step pair correction is not exact for a three-predecessor endpoint. Identity (4.3) shows the entire missing term:

\[
(\min(x_{d-1},x_{d+1})-x_d)_+,
\qquad x_e=e^{\theta T_3(e)}.
\tag{8.1}
\]

Thus the next improvement does **not** require blind enumeration of all four-step paths. It requires one genuinely three-endpoint joint quantity: a lower bound on

\[
\mathbb E\left[(\min(e^{\theta T_3(d-1)},e^{\theta T_3(d+1)})
-e^{\theta T_3(d)})_+\right].
\tag{8.2}
\]

The present pairwise argument throws away exactly (8.2). This diagnosis is useful because it isolates the first correlation statistic not captured by one- and two-endpoint MGFs.

## 9. Exact artifact and execution record

Only after the overlap argument and rational certificate had been identified did this run create the exact checker pair:

- `artifacts/hard7_2026-09-18/HARD7-03/four_step_pair_overlap_20260919T0618Z.py` — commit `661501b7770a46f5356e7389eebde706da4121ec`;
- `artifacts/hard7_2026-09-18/HARD7-03/four_step_pair_overlap_20260919T0618Z.out` — commit `970fa3203dd93e597876ff762d964b269bcd29a1`.

Both files were read back from their returned commits. The executed output ends

`ALL_EXACT_CHECKS_PASS = True`.

The checker verifies the exact `M_2` formulas, the inherited `A_3` formula at the chosen rational `theta`, the total pair-correction expression, the exact `U_4`, the positive Taylor margin, and the exact metric gain. It does not replace the theorem-sized probabilistic proof on this page or independently audit the inherited general-`K` plateau argument.

## 10. What this run does not prove

- It does not close Seppäläinen Problem 4 in full.
- It does not prove the exact value of `G_1(0)`.
- It does not prove the inherited all-`K` site-disorder candidate has passed independent audit.
- It does not address particlewise disorder or every stationary ergodic environment.
- It does not turn a finite block calculation into an empirical finite-size claim; the block calculation is only an exact input to the asymptotic argument.
- It makes no worldwide novelty claim from a bounded literature search.

The correct status remains **PARTIAL**.

## 11. Section-I state and next route

Because the frozen metric moved, the stagnation count is reset. No stuck report or rotation is due.

The next useful research target is the missing three-endpoint correction (8.2), not another receipt or a repetition of the pair checker. A later run should choose three method numbers not previously used on D0025 and either derive a tractable joint three-endpoint law or prove a lower bound on (8.2) from a shared earlier-layer event. If that cannot beat the present `U_4`, the correct output is a failed-method report explaining why, not another unchanged certificate.

## 12. Capability statement

The exposed scheduler/task surface still provides prompt/title/schedule/timing/enabled controls but no binding model selector, reasoning-effort selector, authenticated maximum-reasoning telemetry, or guaranteed execution duration. GPT-6/maximum is therefore prompt-requested only; this run actually identifies as **GPT-5.6 Sol**, with reasoning level **UNVERIFIED**.

The repository records historical native errors `You cannot modify this task` for some IDs, including the earlier P26 context, while later authorized evidence records a successful P26 update in a different context. This run did not probe or modify any scheduler. If an ID currently refuses modification, the compliant remedy is the authorized owner/account/workspace interface or platform support/ownership correction; creating a duplicate task or bypassing permissions is not an acceptable workaround.

## 13. Structured ledger delta

```yaml
ledger_delta:
  track: HARD7-03
  canonical_target: D0025
  owner_claim: operations/claims/D0025.md
  status: PARTIAL
  source_status: OPEN_BY_BOUNDED_SEARCH
  fixed_metric: "rigorous certified lower bound L <= Delta_2(Q) for Q=1/2 delta_{1/2}+1/2 delta_1"
  before: 250/2989
  after: 2500/29711
  movement: true
  exact_gain: 44750/88806179
  methods: [10, 14, 16]
  homogeneous_bound:
    object: "K=2 homogeneous lazy-LPP central shape G_1(0)"
    before_upper: 2989/1000
    after_upper: 29711/10000
    theta: 147/250
    block_length: 4
    method: "deterministic max/min overlap inequality plus exact shared-two-step predecessor corrections"
  missing_correlation:
    object: "E[(min(exp(theta*T3(d-1)),exp(theta*T3(d+1)))-exp(theta*T3(d)))_+]"
    role: "exact slack of the three-predecessor pair-correction inequality"
  inherited_plateau_candidate:
    scope: "fixed K>=1 iid nondegenerate site rates bounded away from zero"
    audit_status: "self-check only; not closed"
  prior_art:
    closest_known_core: "K=1 iid site-disorder plateau literature"
    general_K_site_rate_plateau_found: false
    search_scope: "bounded 2026-09-19 current-literature refresh"
  exact_artifacts:
    - artifacts/hard7_2026-09-18/HARD7-03/four_step_pair_overlap_20260919T0618Z.py
    - artifacts/hard7_2026-09-18/HARD7-03/four_step_pair_overlap_20260919T0618Z.out
  exact_output_status: "ALL_EXACT_CHECKS_PASS = True"
  section_I_state: "metric moved; stagnation reset"
  posted_changed: false
  results_changed: false
  queue_changed: false
  claim_changed: false
```

No shared-root mutation, email, Drive write, public posting, independent audit, closure claim, scheduler modification, or other-track edit was made in this run.
