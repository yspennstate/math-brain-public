Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum.** GPT-6 / maximum was requested, but no authenticated model/effort selector or applied-effort receipt is exposed here, so I do not claim otherwise. **NO MOVEMENT IN THIS R17 ITERATION on the current source interval; status OPEN/PARTIAL.** The current repository-internal source metric had moved between R17 runs because the P02 companion track proved a stricter exact C045 spectral rate; this report recovers that stricter baseline before measuring its own run.

# PROB10-02 / R17 — disagreement flux, formal reset, and an exact coalescence Bellman dual

Repository / branch: private `yspennstate/math-open-problems` / `master`.

Controlling owner directive: `operations/PROB10_2026-09-20.md`.  The later `operations/PROGRESS20_2026-09-20.md` division of work is respected: P02 owns the covering/cone variational refinement, P13 owns the direct boundary-recursion/reset line, while this R17 run attacks the missing **history-coupled controller / temporal dependence** question left by the preceding R17 report.

Target:
\[
\gamma_2=\lim_{n\to\infty}{\mathbf E\,LCS(X_1^n,Y_1^n)\over n}
\]
for two independent iid uniform binary strings.  The same raw source letters generate all matches in each row/column.  No independent Bernoulli matching surrogate is used.

## 0. Continuity, ownership, and the actual current baseline

The owner-required H0021 handoff was already completed at the beginning of the PROB10 refocus.  Its R16/R17 claims and artifacts remain preserved and H0021 remains released/unassigned; this run does not touch it.  The R17 LCS failure/recovery history is also preserved rather than reset.

The newest previous own report is

`runs/prob10_2026-09-20/PROB10-02/20260920T0212Z_r17_suffix_control_obstruction_4a6c.md`.

It proved that independently reselecting a forgotten-prefix carry cannot strengthen the finite-width lower hierarchy: the optimum is attained by zero incoming carry.  It also showed that the pair of Boolean hidden-prefix carry maps is not itself Markov.  Thus the mandated within-problem method change is to keep **temporal coupling information**, rather than relax it away.

Two same-source companion tracks have advanced since that R17 report and were recovered before new work:

- P02, latest complete report recovered here: `proofnet24/P02-progress-lcs/runs/2026-09-20/2026-09-20T03-05-17Z__two-step-rational-collatz-report.md`.  It strengthens the inherited C045 covering rate by the exact two-step rational-Collatz gap
  \[
  \lambda_2=\lambda-\varepsilon_2,
  \qquad
  \varepsilon_2={t^2\over 2Sab},
  \]
  with
  \[
  t={256717\over800000},\quad
  S=142418378752000000000000000000000000000000,
  \]
  \[
  a=1995237757733917147310102692686664915858011319606812684127301,
  \quad b=4220452010631561279.
  \]
  Hence its current exact repository-internal upper candidate is
  \[
  U_2={\log(4t^2)\over\log\lambda_2},
  \]
  strictly below the unstrictified C045 endpoint.  The decrease is about `9.67e-122`, so ordinary displayed decimal digits are unchanged.
- P13, latest complete report recovered here: `proofnet24/P13-progress-lcs/runs/2026-09-20/2026-09-20T02-06-47Z__overlapping-reset-error-and-p02-strict-update.md`.  It proves the exact overlapping-reset mean `2(4^m-1)/3`, `m=2w`, and the corresponding finite-horizon-to-stationary strip error.  This R17 run does not rederive that waiting-time formula; it uses it only as a valid starting upper bound for a different synchronous-coupling dual.

The retained rigorous lower endpoint is
\[
L={99083249\over125000000}=0.792665992.
\]
Thus the **before and after source metric for this run** is exactly
\[
\boxed{
W_{\rm before}=W_{\rm after}=U_2-L
={\log(4t^2)\over\log\lambda_2}-{99083249\over125000000}.
}
\]
Numerically this begins
\[
W_{\rm current}
=0.03360995076228262501510658153729663282346199619\ldots,
\]
with the P02 improvement occurring only around the 121st decimal place relative to C045.  This run does not claim another source-endpoint improvement.

Fresh source checking on 2026-09-20 still finds the exact binary coefficient unresolved.  Tiskin `https://arxiv.org/abs/2212.01582v2` explicitly says the problem is unresolved and that erroneous v1 claims were removed.  Heineman--Miller--Reichman--Salls--Sárközy--Soiffer `https://arxiv.org/abs/2407.10925` give the retained deterministic lower endpoint.  Li--Ren--Wen `https://arxiv.org/abs/2504.10425` still describe exact Chvátal--Sankoff constants as open.  Chia--Bundschuh (Phys. Rev. E 70, 021906, 2004) is prior art for dependence-preserving finite-width sequence comparison.  I make no novelty claim for finite-width LCS or for generic monotone coupling.  A bounded current search found no later deterministic determination of `gamma_2`; that negative search is not a priority certificate.

## 1. New idea before code and the three attacks

The idea was archived before the checker at

`artifacts/prob10_2026-09-20/PROB10-02/20260920T0320Z_r17_disagreement_flux_dual_d7c9_idea.md`.

The three distinct attacks were:

1. **Conserve/transport disagreement:** synchronously drive two exact correlated strip states with the same future source letters and derive an exact flux identity for comparable gradient fronts.
2. **Try to turn the monovariant into immediate contraction:** test plain Hamming disagreement and a natural geometric positional weighting; if false, isolate exact counterexamples rather than tune numerically.
3. **Dualize the coupling time:** after the raw windows synchronize, bracket arbitrary gradients by formal extremal fronts and build an exact absorbing finite-state Bellman supersolution for the coalescence time.  In parallel, exhaust shortest synchronizing input words at the first three strip widths to determine whether any gain is merely a larger reset-word family.

Roughly all substantive work in this run went into these derivations and their failure/success mechanisms; the checker only verifies the finite statements after the route was fixed.

## 2. Exact strip update retained from the prior R17 route

Put `m=2w`.  A strip state is
\[
S=(x_1,\ldots,x_m;g_1,\ldots,g_m),
\]
where `x_i` are the actual raw letters and `g_i` are frontier increments.  For a fresh iid source pair `(u,v)`, define the carry
\[
d_0=0,\qquad
 d_i=(1-g_i)\bigl(d_{i-1}\vee {\bf1}_{\{x_i=v\}}\bigr),
\qquad 1\le i\le m.
\tag{2.1}
\]
The exact next gradient is
\[
g_i'=g_{i+1}+d_{i+1}-d_i\quad(1\le i<m),
\tag{2.2}
\]
\[
g_m'=(1-d_m){\bf1}_{\{u=v\}},
\tag{2.3}
\]
and `x'=(x_2,...,x_m,u)`.  This is the genuine correlated binary-string update: one common `v` is tested against the entire old raw window.

## 3. Attack 1: an exact disagreement-flux identity

Take two states with the **same raw window** `x` and comparable gradient fronts
\[
g\le h
\]
coordinatewise.  Let `d^g,d^h` be their carries under the same incoming `v`, and put
\[
\delta g_i=h_i-g_i,\qquad
\delta d_i=d_i^g-d_i^h,
\qquad
D=\sum_{i=1}^m\delta g_i.
\]
Because (2.1) is decreasing in the current gradient bit and increasing in the incoming carry, induction gives
\[
\delta d_i\ge0\quad\text{for every }i.
\tag{3.1}
\]
The update preserves the order `g'<=h'`.

### Theorem 3.1 — exact disagreement flux

For every formal same-`x` comparable pair and every source input `(u,v)`,
\[
\boxed{
D'=D-\delta g_1{\bf1}_{\{x_1\ne v\}}
       -\delta d_m{\bf1}_{\{u\ne v\}}.
}
\tag{3.2}
\]
In particular,
\[
\boxed{D'\le D\quad\text{pathwise}.}
\tag{3.3}
\]
Averaging over the genuine iid fresh bits gives
\[
\boxed{
\mathbf E[D-D'\mid x,g,h]
={1\over2}\delta g_1
+{1\over2}\mathbf E_v\delta d_m.
}
\tag{3.4}
\]

### Proof

For `i<m`, subtracting the two copies of (2.2) yields
\[
\delta g_i'=\delta g_{i+1}-\delta d_{i+1}+\delta d_i,
\]
while (2.3) gives
\[
\delta g_m'=\delta d_m{\bf1}_{\{u=v\}}.
\]
Summing telescopes:
\[
D'=D-\delta g_1+\delta d_1-\delta d_m
+\delta d_m{\bf1}_{\{u=v\}}.
\]
At the first site, `d_0=0`.  If `delta g_1=0`, the carries agree; if `delta g_1=1`, then `g_1=0,h_1=1`, so
\[
\delta d_1={\bf1}_{\{x_1=v\}}.
\]
Thus `-delta g_1+delta d_1=-delta g_1 1_{x_1 != v}`, and the terminal terms give `-delta d_m 1_{u != v}`.  This proves (3.2).  Nonnegativity in (3.1) gives (3.3), and independence/fairness of `u,v` gives (3.4).  QED.

Interpretation: disagreement mass can disappear only through two exactly identified boundary fluxes.  It cannot branch.  This is the temporal information that the preceding arbitrary-carry relaxation discarded.

The exact checker exhaustively verifies (3.2), order preservation and (3.3) on every reachable same-window comparable pair through `m=4`.

## 4. Attack 2: why a one-step contraction is still false

The flux identity does **not** imply a uniform one-step contraction.  At `m=3`, the exact reachable pair
\[
x=(1,0,1),\quad g=(0,0,1),\quad h=(0,1,1)
\]
has `D=1`, and the checker verifies
\[
D'=1
\]
for all four choices of `(u,v)`.  Hence
\[
\sup {\mathbf E D'\over D}=1
\]
already at `m=3`.

I next tried the simplest directional correction,
\[
F_\alpha(g,h)=\sum_{i=1}^m\alpha^{i-1}(h_i-g_i),
\qquad \alpha={6\over5}.
\]
This also fails, now by expansion rather than equality.  At `m=4`,
\[
x=(0,1,0,1),\quad g=(0,0,0,0),\quad h=(0,1,0,0),
\]
the exact four next-step values are
\[
{6\over5},{36\over25},{6\over5},{36\over25},
\]
so
\[
F_\alpha={6\over5},\qquad
\mathbf E F_\alpha'={33\over25},
\qquad
{\mathbf E F_\alpha'\over F_\alpha}={11\over10}>1.
\tag{4.1}
\]
Thus the next quantitative route cannot be another one-parameter positional Lyapunov function.  It must retain some environment/history state or use a multi-step Bellman potential.

## 5. A stronger formal reset theorem

The reset mechanism can be stated without a reachability hypothesis.

### Theorem 5.1 — length-`m` formal mismatch reset

For **every** formal binary strip state `(x,g)` of length `m` and either `a in {0,1}`, applying
\[
(u_t,v_t)=(a,1-a),\qquad t=1,\ldots,m,
\]
sends the state to
\[
\boxed{(a^m,0^m).}
\tag{5.1}
\]

### Proof

After `t` steps, the rightmost `t` raw letters are `a`.  Induct simultaneously that the rightmost `t` gradient bits are zero.  The new last bit is zero because `u != v`, so (2.3) vanishes.  For every other newly included suffix position `i`, the old site `i+1` already has `g_{i+1}=0` and `x_{i+1}=a != v`; hence (2.1) gives `d_{i+1}=d_i`, and (2.2) gives `g_i'=0`.  At `t=m` all raw letters are `a` and all gradients are zero.  QED.

The checker exhausts **all formal states** for `m=1,...,6` and both mismatch signs.  This theorem justifies using the reset waiting time as an upper start for the joint Bellman dual below; it is not itself a new `gamma_2` endpoint.

A related exact census asks whether there are many other shortest universal resets.  Since an input word shorter than `m` cannot overwrite the whole raw window, no universal full-state synchronizer can have length `<m`.  Exhaustion of all `4^m` source-pair words at the first three strip widths finds exactly two length-`m` universal synchronizers:
\[
(0,1)^m\quad\text{and}\quad(1,0)^m
\]
for `m=2,4,6`.  Thus, at least through `w=3`, the better coupling bounds below do **not** come from discovering additional shortest reset words.

## 6. Attack 3: exact coalescence Bellman dual and a rigorous temporal error

The pathwise monovariant suggests solving a different finite problem from the original strip chain.

For fixed `m`, let `J_m` be the nonabsorbed states reachable from
\[
(x,0^m,1^m),\qquad x\in\{0,1\}^m,
\]
when the two fronts are driven by the same future `(u,v)` sequence.  Equality of the two gradients is absorbing.  Theorem 3.1 guarantees order preservation.  Let `Q_m` be the resulting substochastic transition matrix on `J_m`.

The formal reset theorem implies absorption almost surely.  Moreover the first occurrence of either constant mismatch run of length `m` resets every formal state.  The exact P13 overlap calculation therefore gives the valid coarse starting bound
\[
H_0(s)={2(4^m-1)\over3}
\tag{6.1}
\]
for every nonabsorbed joint state.

Define the exact Bellman iterates
\[
H_{r+1}=1+Q_mH_r.
\tag{6.2}
\]
Every `H_r` remains a rigorous upper bound on the expected coalescence time because `H_0` is one and the Bellman map is monotone.  More strongly, for the finite iterations selected below the checker verifies the **statewise dual inequality**
\[
\boxed{H_r\ge1+Q_mH_r}
\tag{6.3}
\]
using integer arithmetic after clearing the common denominator `3*4^r`.  Therefore optional stopping gives an independently checkable exact coalescence certificate.

Let
\[
K_m=\max_x\mathbf E_{(x,0^m,1^m)}\tau.
\]
The exact certificates prove
\[
\boxed{K_2<{1561\over500}=3.122,}
\tag{6.4}
\]
\[
\boxed{K_4<{7787\over1000}=7.787,}
\tag{6.5}
\]
\[
\boxed{K_6<{13139\over1000}=13.139.}
\tag{6.6}
\]
The corresponding exact maxima of the archived rational potentials are
\[
{26181361\over8388608},
\]
\[
{273975518243713\over35184372088832},
\]
and
\[
{2516810114759473628214826418194899531470875284660494553
 \over
 191561942608236107294793378393788647952342390272950272},
\]
respectively.  The joint state counts are only
\[
14,\quad634,\quad18770
\]
for `m=2,4,6`.

### Corollary 6.1 — certified finite-horizon-to-stationary strip error

Let `R_N` be the first `N` rewards of the width-`w` strip chain from any initial strip state and let `gamma_w` be its stationary average reward, with `m=2w`.  Then
\[
\boxed{
|\mathbf E_sR_N-N\gamma_w|\le m+K_m.
}
\tag{6.7}
\]

**Proof.** Couple the chain from `s` to an independent stationary initial state using the same future source pairs.  After exactly `m` updates their raw windows are identical because both consist solely of the common appended `u` bits.  Each resulting gradient lies between the formal fronts `0^m` and `1^m`.  The strip transition is monotone in the gradient for fixed raw window and source input, so both chains are thereafter sandwiched between the extremal synchronous pair.  Once the extremal pair coalesces, the two genuine chains have coalesced as well.  Thus their expected coupling time is at most `m+K_m`.  Since each one-step reward lies in `[0,1]`, the absolute difference of their cumulative rewards is at most the pre-coalescence time.  The stationary chain has expected total reward `N gamma_w`, proving (6.7).  QED.

Numerically, but with exact rational certificates behind the decimals, this gives
\[
|\mathbf E_sR_N-N\gamma_1|<5.122,
\]
\[
|\mathbf E_sR_N-N\gamma_2^{\rm strip}|<11.787,
\]
\[
|\mathbf E_sR_N-N\gamma_3^{\rm strip}|<19.139.
\]
For comparison, the reset-only constants `2(4^m-1)/3` are `10,170,2730` at `m=2,4,6`.  Thus at `w=3` the exact joint Bellman dual reduces the temporal additive error from `2730` to less than `19.139` without changing the model or using simulation.

This is **auxiliary mechanism progress**, not source-metric movement: the known exact strip values through these widths lie below the retained source lower endpoint, and (6.7) controls finite time versus `gamma_w`, not the width error `gamma_2-gamma_w`.

## 7. Exact checks actually executed

Artifacts:

- `artifacts/prob10_2026-09-20/PROB10-02/20260920T0320Z_r17_disagreement_flux_dual_d7c9_exact.py`
- `artifacts/prob10_2026-09-20/PROB10-02/20260920T0320Z_r17_disagreement_flux_dual_d7c9_exact.out`

Local SHA-256 values of the executed source/output before upload:

- source: `9955bc9f322cb8e2c3acf07b49b63780b34360b15a727ac0814e699c2e0b2057`
- output: `49e8f8b6097bce1d7420caf57c187fa8cad2e016f08256759b415c5d791b7b6b`

The output ends

`EXACT_DISAGREEMENT_FLUX_IDENTITY_PASS`,
`EXACT_PATHWISE_HAMMING_MONOVARIANT_PASS`,
`EXACT_GEOMETRIC_WEIGHT_CONTRACTION_COUNTEREXAMPLE_PASS`,
`EXACT_FORMAL_MISMATCH_RESET_M1_TO_M6_PASS`,
`EXACT_SHORTEST_SYNCHRONIZER_CENSUS_W1_W2_W3_PASS`,
`EXACT_JOINT_COALESCENCE_BELLMAN_DUAL_PASS`, and
`ALL_EXACT_CHECKS_PASS`.

The finite enumeration is a self-check of the finite claims; the general flux identity, formal reset theorem and coupling/error implication are proved on the page above.

## 8. Full-scope gap and next nonduplicating route

Nothing here determines `gamma_2`.  The exact source interval is unchanged during this R17 run:
\[
\boxed{L\le\gamma_2\le U_2},
\qquad
\boxed{W=U_2-L}.
\]
Status remains **OPEN / PARTIAL**.

The result changes the next question.  Plain boundary-carry relaxation is too loose (previous R17), and plain one-step disagreement contraction is false (this run).  But the exact joint chain is dramatically smaller than a naïve pair-of-strip-states construction at small widths, and its Bellman potential gives a rigorous temporal error far below the rare-reset estimate.

The next R17 route should therefore stay inside PROB10-02 and ask for **structural compression of the joint disagreement chain / its Bellman potential as `m` grows**, not another independent-carry model and not P02's covering/cone work.  Two concrete quantitative targets are:

1. prove a width-uniform analytic bound such as `K_m=poly(m)` from the flux identity, or find the exact obstruction to such a bound; and
2. combine such a temporal bound with a compressed exact finite-horizon strip computation at a width whose stationary value can actually exceed `0.792665992`.

Even a polynomial `K_m` alone would not move the source interval without the second ingredient, because it controls time truncation, not strip-width truncation.  This distinction is kept explicit.

Since P02 moved the source metric between the previous R17 report and this run, the source-level stagnation counter is not inherited as four unchanged runs.  Relative to the newly recovered `U_2` baseline, this is the first subsequent unchanged R17 iteration.  No unrelated rotation is made.

## 9. Delivery / boundaries

One immutable R17 report is written for this run.  No root ledger, peer report, H0021 claim/artifact, schedule, cadence, enabled state, workflow, permission, email, Drive item, purchase, or public posting is modified.

```yaml
ledger_delta:
  track: R17
  target: PROB10-02
  source: "Chvatal--Sankoff binary LCS constant"
  model_actual: "GPT-5.6 Sol"
  reasoning_actual: "UNVERIFIED"
  status: PARTIAL
  source_status: OPEN
  lower_before: "99083249/125000000"
  lower_after: "99083249/125000000"
  upper_before: "log(4 t^2)/log(lambda_2)"
  upper_after: "log(4 t^2)/log(lambda_2)"
  width_before: "log(4 t^2)/log(lambda_2)-99083249/125000000"
  width_after: "log(4 t^2)/log(lambda_2)-99083249/125000000"
  movement_this_run: false
  companion_movement_recovered: "P02 two-step rational-Collatz lambda_2 strictification"
  auxiliary_progress:
    - "exact comparable-front disagreement flux identity and Hamming monovariant"
    - "exact counterexamples to uniform one-step Hamming/geometric-weight contraction"
    - "formal length-m mismatch reset theorem"
    - "exact shortest universal synchronizer census through w=3"
    - "exact coalescence Bellman dual: K_2<3.122, K_4<7.787, K_6<13.139"
    - "finite-horizon-to-stationary strip error at w=3 improved from reset-only 2730 to <19.139"
  unresolved_full_scope: "need scalable structural compression plus a width large enough to cross a source endpoint; temporal coupling error alone does not bound gamma_2-gamma_w"
  source_level_stagnation_after_recovered_companion_movement: 1
```
