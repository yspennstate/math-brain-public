Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED** — this is **not GPT-6 at maximum**, and I do not claim otherwise. **Frozen metric MOVED: `L <= Delta_2(Q): 5000/61903 -> 250/2989`. Methods tried: B4 / B11 / B30.**

# HARD7-03 — exact three-step order-cone block bound and transfer-operator obstruction

Status: **PARTIAL / Seppäläinen Problem 4 remains open as a whole.** This run resumes the exclusive `D0025` claim and the last checkpoint rather than reopening admission. The main mathematical gain is a new exact three-step block calculation for the homogeneous `K=2` lazy last-passage comparator. It improves the certified central homogeneous shape bound from `61903/20000` to `2989/1000`, hence moves the frozen binary-disorder plateau-width certificate from `5000/61903` to `250/2989`.

## 1. Continuity, repository state, and ownership

I resumed:

`operations/claims/D0025.md`

owned by `HARD7-03`, with canonical intake key `disordered_asep_open_1999::problem_4`.

Before new mathematics I re-read/recovered:

- `operations/hard7_2026-09-18/CONTROL.md`;
- `operations/NEW_METHODS_2026-09-16.md`;
- `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md`;
- `probability_campaign_2026_09/INDEX.md` and `RANKING.md`;
- root `POSTED.md`, `RESULTS.md`, and `QUEUE.md`;
- the exact D0025 claim and repository-wide exact-key/alias search over the intake material;
- the complete HARD7-03 checkpoint chain through the newest own report `runs/hard7_2026-09-18/HARD7-03/20260919T0421Z__d0025-two-step-block-chernoff-metric-move.md`;
- newest neighboring HARD7-02 report `2026-09-19T04-12-00Z__critical-endpoint-and-axis-boundary-layer.md`;
- newest neighboring HARD7-04 report `2026-09-19T04-40Z__p0157_four_hub_exclusion.md`.

No canonical claim collision, release, posted equivalent, or competing D0025 owner surfaced. The root ledgers are shared concurrent files, so this worker does not mutate them; the structured `ledger_delta` below is the handoff to the designated reconciler. Concurrent fleet writes were active while the artifacts were committed.

## 2. Source/current-status refresh

The source remains Timo Seppäläinen, *Recent Results and Open Problems on the Hydrodynamics of Disordered Asymmetric Exclusion and Zero-Range Processes*, Resenhas IME-USP 4(1) (1999), 1--15, Problem 4; DOI `10.11606/resimeusp.v4i1.74889`, arXiv `math/9906194`.

The frozen residual is **not** the known ordinary `K=1` result. It is the general-capacity `K>=2` iid site-disorder question, with the first fixed test case

\[
K=2,\qquad Q=\tfrac12\delta_{1/2}+\tfrac12\delta_1.
\]

The source asks for the phase-transition/flat-flux phenomenon for the disordered asymmetric `K`-exclusion process; the active metric is tied only to its flat-segment clause.

A fresh bounded literature search dated 2026-09-19 used combinations of `site disorder K-exclusion flux plateau K>=2`, `disordered K-exclusion flat segment`, and `partial exclusion site disorder flux plateau`. It re-located:

1. the official 1999 source page, which describes the paper as a collection of results and open problems and records publication date 1999-07-01;
2. Allan Sly, arXiv:1609.06589, whose abstract explicitly proves a plateau for iid-disordered ordinary TASEP (`K=1`);
3. Balázs--Bowen's asymmetric `K>=2` discussion, which notes that constant-parameter product measures are not stationary and that the translation-invariant stationary structure is unknown;
4. Ayyer--Misra (2024), an exactly solvable **deformed-rate** asymmetric `K`-exclusion model, not Seppäläinen's rate-one process.

I did not locate a 2024--2026 theorem closing the exact iid site-rate `K>=2` plateau question. This is bounded negative evidence, not a worldwide proof of openness. No novelty claim is made for the all-`K` candidate proof chain before independent proof audit and broader citation-graph review.

## 3. Frozen metric: genuine movement

For the binary frozen law define

\[
\Delta_2(Q)=\sup\{\delta\ge0:
 f_{2,Q}\text{ is constant on }[1-\delta,1+\delta]\}.
\]

The stable tracked quantity is a rigorous certificate `L <= Delta_2(Q)` inside the current self-checked theorem chain.

Before this run:

\[
L_{\rm old}=\frac{5000}{61903}=0.08077152\ldots.
\]

After this run:

\[
\boxed{L_{\rm new}=\frac{250}{2989}=0.08364001338\ldots.}
\]

The exact gain is

\[
L_{\rm new}-L_{\rm old}
=\frac{530750}{185028067}>0.
\]

The inherited general-`K` plateau argument from the preceding checkpoints gives, in this frozen binary case,

\[
\Delta_2(Q)\ge \frac{1}{4G_1(0)},
\tag{3.1}
\]

where `G_1(0)` is the rate-one homogeneous `K=2` central lazy-LPP shape constant. Thus it suffices to improve a rigorous upper bound on `G_1(0)`.

## 4. B4 — prove a smaller theorem completely: exact three-step block integration

The previous run used two-step blocks and obtained

\[
G_1(0)\le \frac{61903}{20000}=3.09515.
\]

The suggested four-step route immediately encounters a much larger max-plus chamber decomposition. Instead of inserting a lossy inequality merely to reach length four, this run solves the **smallest unexplored block exactly**, length three. The key new device is order-cone integration: condition on the first layer, integrate the second-layer maximum exactly, then integrate the first layer separately over its six possible strict orderings.

### Theorem 4.1 — three-step homogeneous bound

For the same unrestricted rate-one `K=2` lazy-LPP comparator used in the prior checkpoints,

\[
\boxed{G_1(0)\le\frac{2989}{1000}=2.989.}
\tag{4.1}
\]

### Proof

A three-step block starts at height `0`. Let the first new time layer have independent `Exp(1)` weights

\[
A_{-1},A_0,A_1.
\]

At the second new layer, for `x=-2,-1,0,1,2`, let `B_x` be iid `Exp(1)`. Maximizing only over the first step gives the deterministic-in-`A` shifts

\[
\begin{aligned}
m_{-2}&=A_{-1},\\
m_{-1}&=\max(A_{-1},A_0),\\
m_0&=\max(A_{-1},A_0,A_1),\\
m_1&=\max(A_0,A_1),\\
m_2&=A_1.
\end{aligned}
\tag{4.2}
\]

Fix the block endpoint `d in {-3,-2,...,3}` at the third new layer, and let its independent endpoint weight be `C_d~Exp(1)`. Then the exact block maximum is

\[
X_3(d)=C_d+
\max_{\substack{-2\le x\le2\\ |d-x|\le1}}
\{B_x+m_x\}.
\tag{4.3}
\]

We now integrate the inner shifted exponential maximum exactly. For fixed shifts `c_1,...,c_s`, put

\[
Y=\max_i(c_i+B_i),\qquad c_*=\max_i c_i.
\]

For `0<\theta<1` and `y>=c_*`,

\[
\Pr(Y\le y\mid c)=
\prod_i(1-e^{c_i-y}).
\]

Tail integration and inclusion-exclusion therefore give

\[
\mathbb E(e^{\theta Y}\mid c)
=e^{\theta c_*}
+\theta\sum_{\varnothing\ne S\subseteq[s]}
\frac{(-1)^{|S|+1}}{|S|-\theta}
\exp\!\left(
\sum_{i\in S}c_i-(|S|-\theta)c_*
\right).
\tag{4.4}
\]

Every exponent in (4.4) is linear in `A_{-1},A_0,A_1` once their ordering is fixed. On an order cone

\[
0\le A_{\pi_1}\le A_{\pi_2}\le A_{\pi_3},
\]

write the additional exponent as

\[
\beta_1A_{\pi_1}+\beta_2A_{\pi_2}+\beta_3A_{\pi_3}.
\]

Including the iid exponential density and changing to the three nonnegative gaps gives the exact cone integral

\[
\int_{A_{\pi_1}\le A_{\pi_2}\le A_{\pi_3}}
 e^{-\sum A_i+\sum\beta_iA_{\pi_i}}\,dA
=
\frac{1}
{(3-\beta_1-\beta_2-\beta_3)
 (2-\beta_2-\beta_3)
 (1-\beta_3)}.
\tag{4.5}
\]

Ties have measure zero. Summing (4.4)--(4.5) over all six orderings and multiplying by the endpoint factor `(1-theta)^{-1}` yields the following **exact** fixed-displacement moment generating functions; by reflection, `M_3(-d;theta)=M_3(d;theta)`:

\[
M_3(0;\theta)
=\frac{4(18-11\theta)}
{(3-\theta)^2(2-\theta)^3(1-\theta)^3},
\tag{4.6}
\]

\[
M_3(1;\theta)
=\frac{648-889\theta+394\theta^2-57\theta^3}
{(3-\theta)^4(2-\theta)^3(1-\theta)^3},
\tag{4.7}
\]

\[
M_3(2;\theta)
=\frac{8-5\theta}
{(2-\theta)^3(1-\theta)^3},
\qquad
M_3(3;\theta)=\frac1{(1-\theta)^3}.
\tag{4.8}
\]

As a zeroth-order check, every `M_3(d;0)=1`, as required.

Let

\[
A_3(\theta)=\sum_{d=-3}^3M_3(d;\theta).
\]

The exact simplification is

\[
A_3(\theta)=
\frac{2(2268-4408\theta+3748\theta^2-1918\theta^3
+652\theta^4-143\theta^5+18\theta^6-\theta^7)}
{(3-\theta)^4(2-\theta)^3(1-\theta)^3}.
\tag{4.9}
\]

Now concatenate `m` three-step blocks. Fix coarse boundary heights

\[
y_0=0,y_1,\ldots,y_m=0,
\qquad |y_j-y_{j-1}|\le3.
\]

If starting-layer weights are not double-counted, distinct blocks use disjoint new time layers. Hence, for a fixed coarse sequence, the block maxima are independent and Chernoff gives

\[
\Pr\left\{
\sum_{j=1}^mX_{3,j}(y_j-y_{j-1})\ge3ma
\right\}
\le e^{-3m\theta a}
\prod_{j=1}^mM_3(y_j-y_{j-1};\theta).
\tag{4.10}
\]

Union over all endpoint-zero coarse sequences. Dropping the final endpoint constraint can only increase the positive sum, so

\[
\Pr\{T_1(3m,0)\ge3ma\}
\le
\left[A_3(\theta)e^{-3\theta a}\right]^m.
\tag{4.11}
\]

Take the exact rational choices

\[
\theta=\frac{301}{500},
\qquad
a=\frac{2989}{1000}.
\tag{4.12}
\]

The exact checker obtains

\[
A_3(301/500)
=\frac{1229263344958889641724750000000}
{5562467529854156401619442501},
\tag{4.13}
\]

and

\[
3\theta a=\frac{2699067}{500000}.
\tag{4.14}
\]

Let `S_18(x)=sum_{k=0}^{18}x^k/k!`. Since `x>0`,

\[
S_{18}(x)<e^x.
\]

Exact rational arithmetic gives

\[
S_{18}\!\left(\frac{2699067}{500000}\right)
-A_3(301/500)>0,
\tag{4.15}
\]

with exact positive rational archived in the output; its decimal value is `0.000288667874744...`. Therefore the bracket in (4.11) is strictly smaller than one. The tail probabilities are summable in `m`; Borel--Cantelli and the already-established homogeneous shape limit yield

\[
G_1(0)\le a=\frac{2989}{1000}.
\]

This proves (4.1). `QED`

Combining with (3.1),

\[
\Delta_2(Q)
\ge\frac{1}{4G_1(0)}
\ge\frac1{4(2989/1000)}
=\boxed{\frac{250}{2989}}.
\tag{4.16}
\]

**B4 outcome: successful.** Rather than force a four-step calculation through an uncontrolled approximation, the run completely solves the next exact block and moves the source-relevant metric.

## 5. B11 — transfer-operator dualization, and a precise obstruction

The block Chernoff union can be written as a positive convolution transfer operator. Define

\[
K_\theta(d)=M_3(d;\theta),\qquad -3\le d\le3,
\]

and

\[
(\mathcal T_\theta f)(x)
=\sum_{d=-3}^3K_\theta(d)f(x+d).
\tag{5.1}
\]

Then the weighted sum over `m` coarse block sequences from `0` back to `0` is exactly

\[
(\mathcal T_\theta^m\delta_0)(0).
\tag{5.2}
\]

This reformulation answers an important tactical question: can the endpoint-zero condition itself improve the exponential constant below `A_3(theta)` without retaining more state?

No. The Fourier symbol is

\[
\widehat K_\theta(\phi)
=\sum_{d=-3}^3K_\theta(d)e^{id\phi}.
\]

All coefficients are positive and symmetric, so

\[
|\widehat K_\theta(\phi)|
\le\sum_dK_\theta(d)
=A_3(\theta),
\]

with equality at `phi=0`. Thus the convolution operator's spectral radius is exactly `A_3(theta)`. Any argument that remembers **only** the one-block displacement kernel cannot lower the exponential base by exploiting the final zero displacement; the lost information is correlation between competing boundary endpoints inside a larger block.

This is a useful negative result rather than a failed proof: it identifies precisely why the next improvement must enlarge the block or retain a richer boundary state.

**B11 outcome: successful structural diagnosis.** The dual/transfer language exposes the exact bottleneck and prevents wasting later runs on a Perron--Frobenius optimization that cannot improve the exponent in this state space.

## 6. B30 — one scale at a time

The homogeneous comparator now has three successive explicit certified bounds from genuinely different levels of overlap retention:

| scale | certified upper bound on `G_1(0)` | induced binary plateau half-width |
|---|---:|---:|
| one-step / path-union predecessor | `6578563/2000000 = 3.2892815` | `500000/6578563 = 0.07600444...` |
| exact two-step block | `61903/20000 = 3.09515` | `5000/61903 = 0.08077152...` |
| exact three-step order-cone block | `2989/1000 = 2.989` | `250/2989 = 0.08364001...` |

These three displayed certificates decrease strictly. I do **not** claim that the optimal block-`ell` certificates form a monotone sequence for every `ell`; only these three rigorously exhibited values are being compared.

The exact two-to-three-step shape improvement is

\[
\frac{61903}{20000}-\frac{2989}{1000}
=\frac{2123}{20000}.
\]

**B30 outcome: successful.** Localizing by the next block scale moved the frozen source metric without changing definitions or replacing an asymptotic theorem by simulation.

## 7. Exact artifact and execution record

This run created one substantive checker pair only after the order-cone idea was complete:

- `artifacts/hard7_2026-09-18/HARD7-03/three_step_order_cone_20260919T0522Z.py` — commit `a3068d4f03ac33599d914b06c715af652d68e70d`;
- `artifacts/hard7_2026-09-18/HARD7-03/three_step_order_cone_20260919T0522Z.out` — commit `51ee60b1d8a3823c51b7f6ec4c0739eea02b3aa5`.

Both were read back from their returned commits. The executed output ends

`ALL_EXACT_CHECKS_PASS = True`.

The checker independently constructs all six first-layer order cones, integrates the conditional inclusion-exclusion formula symbolically, verifies (4.6)--(4.9), evaluates the rational choice `(theta,a)`, certifies the degree-18 Taylor inequality exactly, and checks both the homogeneous-bound and frozen-metric improvements. It does not replace the probabilistic block concatenation, Borel--Cantelli argument, or inherited plateau theorem; those remain written mathematical arguments and the inherited all-`K` part remains self-checked pending independent audit.

## 8. What this run does not prove

- It does not close Seppäläinen's full Problem 4.
- It does not independently audit the inherited general-`K` plateau/cusp argument.
- It does not identify the exact value of `G_1(0)`.
- It does not solve particlewise disorder or arbitrary stationary ergodic site disorder.
- It does not claim that a three-step numerical-looking bound is an exact shape formula.
- It does not claim novelty of the all-`K` candidate theorem from a negative search.

The correct label remains **PARTIAL**.

## 9. Next mathematical route

Because the frozen metric moved again, the Section-I stagnation counter is reset; no stuck report or rotation is due. The next run must use a different triple. The most informative continuation is:

- **B1 — change category:** view the four-step max recursion as a tropical hyperplane/chamber arrangement rather than enumerating paths;
- **B19 — make it an algorithm:** enumerate only distinct max-plus linear forms/chambers needed for the four-step endpoint MGFs, merging equivalent states before exact integration;
- **B20 — find why the algorithm fails:** if chamber growth still prevents an exact four-step integral, isolate the smallest nonintegrable boundary-state obstruction instead of inserting a crude checker-only bound.

This directly targets what B11 proved is missing: richer within-block endpoint correlation.

## 10. Capability statement

The exposed task/automation surface still provides prompt/title/schedule/timing/enabled controls but no binding model selector, reasoning-effort selector, authenticated maximum-reasoning telemetry, or guaranteed execution duration. GPT-6/maximum is therefore prompt-requested only. The model actually exposed to this run is **GPT-5.6 Sol** and the reasoning level is **UNVERIFIED**.

The repository records historical scheduler failures of the form `You cannot modify this task`, including the earlier P26 case, and separately records that P26 later became editable from a different authorized context. This run did not probe or modify P26 or any other schedule. If a task still rejects modification, the compliant remedy is the authorized owner/account/workspace interface or platform support/ownership correction. Creating a duplicate or bypassing permissions is not a workaround.

## 11. Structured ledger delta

```yaml
ledger_delta:
  track: HARD7-03
  canonical_target: D0025
  owner_claim: operations/claims/D0025.md
  status: PARTIAL
  source_status: OPEN_BY_BOUNDED_SEARCH
  fixed_metric: "rigorous certified lower bound L <= Delta_2(Q) for Q=1/2 delta_{1/2}+1/2 delta_1"
  before: 5000/61903
  after: 250/2989
  movement: true
  exact_gain: 530750/185028067
  methods: [4, 11, 30]
  new_homogeneous_bound:
    object: "K=2 homogeneous lazy-LPP central shape G_1(0)"
    before_upper: 61903/20000
    after_upper: 2989/1000
    theta: 301/500
    block_length: 3
    method: "exact conditional shifted-exponential MGF + six order-cone integrals"
    proof_status: "self-contained theorem on page + exact symbolic/rational checker"
  transfer_obstruction:
    statement: "one-block positive convolution state has spectral radius A3(theta), attained at Fourier mode 0; endpoint-zero alone cannot improve its exponential base"
  inherited_plateau_candidate:
    scope: "fixed K>=1, iid nondegenerate site rates Q subset [r,1], r>0"
    audit_status: "self-check only; not closed"
  prior_art:
    closest_exact: "Sly 2016, K=1 iid site-disorder plateau"
    general_K_site_rate_plateau_found: false
    search_scope: "bounded 2026-09-19 source/current-literature refresh"
  exact_artifacts:
    - artifacts/hard7_2026-09-18/HARD7-03/three_step_order_cone_20260919T0522Z.py
    - artifacts/hard7_2026-09-18/HARD7-03/three_step_order_cone_20260919T0522Z.out
  exact_output_status: "ALL_EXACT_CHECKS_PASS = True"
  section_I_state: "metric moved; stagnation reset to 0"
  next_methods: [1, 19, 20]
  posted_changed: false
  results_changed: false
  queue_changed: false
  claim_changed: false
```

No shared-root mutation, public posting, email, Drive write, independent audit, closure claim, or scheduler change was made in this run.