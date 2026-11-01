Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 at maximum. SOURCE-METRIC MOVEMENT: `W_sigma = 0.083458870871305542695912279857624... -> 0.083458052478335484902095404052916...`; C0021 unchanged-run streak `0 -> 0`. Methods actually tried: B10, B22, B28.**

# P13 / C0021 — clock-14 typical-state patches and a buy-out-rule obstruction

Date: 2026-09-18 UTC. Track: P13 Outside Counterexample Research. Native slot: `6aa7b253b37c8191b693d8dc79298d37`. Own root: `proofnet24/P13-outside-successor/`.

Source target: Christophe Garban and Jeffrey E. Steif, *Noise Sensitivity of Boolean Functions and Percolation*, Chapter VIII, Exercise VIII.5: for depth-`k` iterated 3-majority on `n=3^k` unbiased leaves, determine the exponent `sigma` governing the asymptotic decay of revealment. The author-hosted book text says the decay is polynomial and that determining `sigma` is open. The P13 frozen metric remains the width of the rigorous interval for this single source exponent.

Status after this run: **CLAIMED / CURRENT-OPEN-LOOKING / PARTIAL / SOURCE-METRIC MOVEMENT.** No closure, novelty certificate, or independent audit is claimed.

## 1. Continuity, ownership, and required state recovery

I continued the active create-only ownership marker `operations/claims/C0021.md`, which names this P13 slot and this own root. I did not reopen retired I0051, handed-off P0082, or six-run-handed-off D0093. I0054 was rechecked first as required: the newer R11 report `runs/R11/2026-09-18T16-40-00Z_i0054-ordinary-polynomial-occurrence-u027-c048-6d2e.md` still owns that source and moves its own frozen metric `47 -> 48`, so P13 did not touch it.

Before research I reread the controlling owner directive at anchor `749da260517828ed311f6f1b1af74915c054bdf3`, `operations/NEW_METHODS_2026-09-16.md`, campaign `INDEX.md` and `RANKING.md`, root `POSTED.md`, `RESULTS.md`, and `QUEUE.md`, the newest P13 report `2026-09-18T16-13-57Z__c0021-performance-difference-movement.md`, the canonical C0021 claim, the C0021 intake/attempt history, and the newer neighboring R11 report. Stale root summaries were not allowed to reset the newer C0021 history.

The inherited exact reduction is

\[
\delta_{f_k}=\frac{D_k}{3^k},\qquad
c=\lim_{k\to\infty}D_k^{1/k}=\inf_k D_k^{1/k},\qquad
\sigma=1-\log_3 c,
\]

where `D_k` is the minimum expected number of leaf queries of an exact deterministic decision tree under iid unbiased leaves. Before this run the best certified explicit depth-4 policy had

\[
U_{40}=\frac{1332477360033879887}{36028797018963968}
=36.9836761225339451797\ldots,
\]

hence

\[
\sigma\ge 0.178400636271609331503141948827898\ldots
\]

and, using the unchanged source-side upper endpoint

\[
\sigma\le \log_3(4/3)=0.261859507142914874199054228685522\ldots,
\]

the frozen width was

\[
W_{\rm old}=0.083458870871305542695912279857624\ldots .
\]

## 2. Idea before code

The previous run proved a performance-difference identity showing that a local Bellman defect contributes to root cost with its **total occupation/hit probability**, not merely its probability at one query clock. The present idea was therefore not to demand a pointwise invariant over the whole state space. Instead I searched among states actually reached by the current policy and asked whether a small number of positive-defect types carried enough occupancy to produce a certified global improvement.

The three required methods were used as follows.

- **B10 — derandomize / make explicit.** I tried to replace the finite patch table by the obvious deterministic scale-free `R` rule: at each state choose the legal next query minimizing the exact one-step “buy each child outright” surrogate. This route fails on an explicit reached state; the surrogate ranks the two relevant actions in the wrong order. The failure is proved exactly below.
- **B22 — read failures, not successes.** I compared the current obstruction to the recursive-majority literature. The strongest classical lower-bound lines are worst-case or hard-distribution arguments, while the source quantity here is the minimum expected cost under the fixed uniform product law. Their hard-distribution minority-path recurrences therefore cannot simply be imported. The interleaving upper-bound literature, however, predicts exactly the kind of nonlocal option value seen in the new defect.
- **B28 — replace “for all” by “typical.”** Instead of trying to prove the globally false pointwise completion-cost/uncertainty inequality, I patched six **actually reached** clock-14 canonical states (three global-sign orbits) with positive exact Bellman defect. Total occupancy then converts those local gains into a rigorous source-domain improvement.

## 3. B10: exact obstruction to the buy-out surrogate

Let `pi_40` denote the 40-override depth-4 policy from the preceding report, and let `E_40(s)` be its exact continuation cost from canonical state `s`.

The baseline heuristic uses a child buy-out surrogate `R(s)`: each unfinished child is assigned its exact optimal local completion cost `V` and its exact posterior probability `q`, and the outer majority is solved as a three-item stochastic lottery. This is the strongest simple scalar rule used in the existing baseline construction.

Consider the reached clock-14 state `s_*` represented by the large-defect global-sign orbit in the explicit `EXTRA6` certificate table. Its three top-child `(q,V)` signatures are

\[
\left(\frac{59}{64},\frac{1417}{512}\right),\quad
\left(\frac{11}{16},\frac{3028131}{262144}\right),\quad
\left(\frac38,\frac{6697443}{524288}\right).
\]

Let `a_0` be the action selected by the buy-out rule and `a_1` the new interleaving action stored in the certificate. Exact arithmetic gives

\[
Q_R(s_*,a_0)=\frac{9896172505}{536870912},
\]

\[
Q_R(s_*,a_1)=\frac{9896679645}{536870912},
\]

so the surrogate rejects `a_1` by

\[
Q_R(s_*,a_1)-Q_R(s_*,a_0)
=\frac{126785}{134217728}>0.
\]

But under the true continuation value of `pi_40`,

\[
Q_{40}(s_*,a_0)=\frac{9896172505}{536870912},
\]

whereas

\[
Q_{40}(s_*,a_1)=\frac{9890627465}{536870912},
\]

and therefore

\[
Q_{40}(s_*,a_0)-Q_{40}(s_*,a_1)
=\boxed{\frac{346565}{33554432}}>0.
\]

### Proposition 3.1 — the exact buy-out rule is not locally correct

The deterministic rule “choose the query minimizing the one-step exact buy-out surrogate `R`” is not Bellman-optimal even on the support of the current depth-4 policy.

**Proof.** The state `s_*` is reached under `pi_40`; the checker verifies both actions are legal one-leaf queries. The displayed exact inequalities show that `R` strictly prefers `a_0`, while the actual continuation cost under `pi_40` strictly prefers `a_1`. Hence the rule disagrees with the Bellman ordering at `s_*`. ∎

This does **not** rule out every scale-free symbolic rule. It rules out the most direct derandomization of the current child-buy-out surrogate and identifies what it misses: future interleaving option value in the successors.

## 4. B28: a typical-state performance theorem and six certified patches

I use the preceding report's performance-difference identity, but reproduce the needed statement and proof here.

### Lemma 4.1 — finite policy replacement identity

Let `pi` and `pi'` be exact policies on a finite acyclic Boolean decision state graph. Write `E_pi(s)` for the expected remaining queries under `pi`. At any state where `pi'` chooses action with successors `s^+,s^-`, define its defect relative to `pi` by

\[
d(s)=E_\pi(s)-\left(1+\frac{E_\pi(s^+)+E_\pi(s^-)}2\right).
\]

Then from any root `r`,

\[
E_\pi(r)-E_{\pi'}(r)
=\mathbb E_{\pi'}\!\left[\sum_{t<\tau} d(S_t)\right]
=\sum_s H_{\pi'}(r,s)d(s),
\]

where `H_{pi'}(r,s)` is the expected number of visits to `s` (here at most one for a fixed unresolved-rank state, but canonical state types may occur at different raw clocks).

**Proof.** Put `G(s)=E_pi(s)-E_pi'(s)`. At a nonterminal state where `pi'` takes successors `s^+,s^-`, Bellman recursion gives

\[
G(s)=d(s)+\frac{G(s^+)+G(s^-)}2.
\]

Iterating this identity down the strictly rank-decreasing decision DAG telescopes at terminal states, where `G=0`. Taking expectation over the `pi'` trajectory gives the first equality; grouping visits by canonical state gives the second. ∎

### The three reached sign orbits

The exact checker starts from the certified 40-patch policy, forms its clock-14 reachable support (1021 canonical states), and verifies six selected reached states, grouped into three global-sign orbits, each with a legal strictly improving action. I make **no exhaustiveness claim** that these six are the only improvable clock-14 states.

Sequentially installing the three sign orbits gives:

\[
\begin{array}{c|c|c|c}
\text{orbit} & d & H & H d\\ \hline
1 & 346565/33554432 & 57/8192 & 19754205/274877906944\\
2 & 25155/4194304 & 1197/131072 & 30110535/549755813888\\
3 & 16875/33554432 & 3321/262144 & 56041875/8796093022208
\end{array}
\]

Here `H` is the exact total hit probability of that sign orbit under the policy applicable at that sequential stage. The fact that `H` can exceed the orbit's single clock-14 layer probability is precisely why the occupancy formulation matters: the same canonical type can be reached at more than one raw query clock.

By Lemma 4.1 every row lowers the root expected cost by exactly `H d`. After all six new overrides, the explicit 46-patch policy has

\[
\boxed{
U_{46}
=\frac{1332472567939180367}{36028797018963968}
=36.98354311518715539786\ldots
}
\]

and the exact improvement over `U_40` is

\[
\boxed{
U_{40}-U_{46}
=\frac{1169944995}{8796093022208}
=0.00013300734678978188\ldots .
}
\]

This is not an invented side metric; it improves the same depth-4 block cost used to certify the source exponent.

## 5. Source-domain consequence

### Theorem 5.1 — improved rigorous lower endpoint for `sigma`

For the source exponent of iterated 3-majority,

\[
\boxed{\sigma\ge
0.178401454664579389296958824632605\ldots}.
\]

Consequently

\[
\boxed{
W_\sigma\le
0.083458052478335484902095404052916\ldots}.
\]

**Proof.** Compose the explicit exact depth-4 policy as a stationary four-level block algorithm. At depth `4m`, the top depth-4 decision tree sees virtual leaf values given by independent depth-`4(m-1)` recursive-majority subtrees. Those virtual values are iid unbiased bits. The top policy queries an expected `U_46` virtual leaves; each queried virtual leaf is evaluated by an independent copy of the depth-`4(m-1)` composed algorithm. Induction therefore gives

\[
D_{4m}\le U_{46}^m.
\]

Hence the submultiplicative growth constant satisfies

\[
c=\lim_k D_k^{1/k}\le U_{46}^{1/4}
=2.46605142530463998011111465329656\ldots .
\]

Since `sigma = 1-log_3 c`,

\[
\sigma\ge 1-\frac14\log_3 U_{46}
=0.178401454664579389296958824632605\ldots .
\]

The rigorous upper endpoint remains `log_3(4/3)=0.261859507142914874199054228685522...`. Subtraction yields the displayed width. ∎

The width contraction this run is

\[
\boxed{
8.18392970057793816875804707322436\times 10^{-7}
}.
\]

Therefore the unchanged-run streak resets/remains at zero.

## 6. B22: what the failure literature actually says for this target

Fresh bounded searches on 2026-09-18 used the queries `iterated 3-majority revealment sigma Garban Steif recursive majority`, `recursive majority uniform expected queries decision tree complexity Jansson 2023`, `recursive majority information complexity decision tree Jayram Kumar Sivakumar`, `recursive majority randomized query complexity Magniez Nayak Santha Sherman Tardos Xiao`, and `stochastic boolean function evaluation optimal decision tree 2026`.

The useful negative lessons are specific.

1. **Hard-distribution lower bounds do not directly lower-bound the fixed uniform law.** Jayram--Kumar--Sivakumar and the Magniez et al. refinements use a specially designed hard distribution with an absolute minority path. In contrast, under the unbiased product law relevant to `D_h`, conditioned on a parent majority value `R`, the three child values are uniformly distributed over the four compatible patterns: one is `(R,R,R)` and three have exactly one `-R`. Thus a minority child exists with probability `3/4`, not probability one. More fundamentally, a lower bound for `max_D min_A C(A,D)` does not by itself lower-bound `min_A C(A,D_uniform)`. The hard-distribution recurrence cannot be imported without a new uniform-law argument.

2. **Interleaving is known to beat simple recursive structure in the worst-case literature.** Magniez--Nayak--Santha--Sherman--Tardos--Xiao explicitly improve their zero-error upper bound using a depth-two interleaving algorithm and say deeper recursive analyses become unwieldy. That is structurally consistent with the B10 obstruction above: paying a slightly worse local/buy-out score can buy a better future interleaving position.

3. **Bottom-up constants are fragile.** The ECCC revision of Leonardos records that an error in Corollary 6 forced the claimed base from `2.6` down to `2.55`. That is a direct warning against promoting a shallow numerical recurrence before its induction invariant is exact.

4. **Exact stochastic-Boolean evaluation remains finite-instance oriented.** Jansson--Jansson compute the level-`p` complexity of two-level iterated majority exactly; the paper emphasizes exponential growth in decision trees/call states. The June 2026 Zong--Lehtonen--Rintanen work gives a general branch-and-bound exact optimizer for stochastic Boolean evaluation, but not a scale-stable analytic determination of this recursive exponent.

So B22 did not yield a transferable lower bound this run. It sharpened the missing ingredient: a **uniform-product-law, interleaving-stable dual potential**, not a hard-distribution minority-path recurrence and not a forced locally optimal child completion rule.

## 7. Current literature/source check and access notes

The author-hosted Garban--Steif PDF was accessible on 2026-09-18 and its Chapter VIII exercise sheet states that the iterated 3-majority revealment has polynomial decay and that the exponent remains an open question in that source. A PDF screenshot request for the relevant page failed with an internal fetch error; the text layer and source locator were available and were used. Cambridge's current book metadata also remains available.

The bounded current-literature search recovered Jansson--Jansson (JFP 2023), Magniez et al. (Random Structures & Algorithms 2016 / arXiv:1309.7565), Leonardos's corrected ECCC report, Jayram--Kumar--Sivakumar (STOC 2003), and Zong--Lehtonen--Rintanen (arXiv:2606.24672, June 2026). I did not find a checked primary source determining the exact Garban--Steif exponent. This is **bounded negative evidence only**, not a global openness or publication-novelty certificate.

## 8. Exact checker and immutable artifacts

Executed exact-arithmetic checker:

`proofnet24/P13-outside-successor/artifacts/2026-09-18/c0021_clock14_typical_patch_check.py`

Creation commit: `6e2e9a15a3d9a29168a3834d730173a85688f5ad`. Read-back Git blob: `0a7d0899db240dfe873f813078d5054a6d9b0910`.

Executed output:

`proofnet24/P13-outside-successor/artifacts/2026-09-18/c0021_clock14_typical_patch_check.out`

Creation commit: `1227d331af094198a2448422def8c25993022c11`. Read-back Git blob: `0173e046fd0909c91e9bc755e893e8f5504b4500`.

The output ends

`ALL_EXACT_CLOCK14_TYPICAL_PATCH_CHECKS_PASS`.

The checker verifies: the inherited 40-state policy table, the six new legal sign-equivariant overrides, reachability of all six at query clock 14, each exact defect, the B10 surrogate reversal, all three sequential root gains and total-hit coefficients, the final exact depth-4 cost, and the source interval movement. This is a **P13 self-check**, not an independent audit.

## 9. What remains and next methods

C0021 is not closed. The exact exponent still requires matching upper and lower growth constants for `D_k`. The present upper-policy line is improving only the lower endpoint of `sigma`; the source-side upper endpoint still comes from the `c >= 9/4` lower bound on uniform expected query growth.

The main residual obstruction is now clearer: finite interleaving defects exist on actually occupied states, but the current lower-bound technology has no scale-stable uniform-law potential that charges those same interleavings. The next distinct research triple is **B11, B17, B26**:

- B11: dualize the uniform expected-cost Bellman problem and seek a self-similar feasible dual potential proving `c > 9/4`;
- B17: compare the resulting coefficients with martingale/optimal-stopping and stochastic-Boolean-evaluation constants elsewhere, without importing mismatched worst-case distributions;
- B26: isolate the sporadic canonical states where the buy-out surrogate reverses the true Bellman ordering and determine the smallest symbolic correction term that handles all of them.

No closure audit was requested because closure is not claimed. The previously completed P14-directed audit duty is not repeated.

## 10. Structured `ledger_delta` for P26

```json
{
  "track": "P13",
  "native_slot": "6aa7b253b37c8191b693d8dc79298d37",
  "target": "C0021",
  "source_scope": "Garban-Steif Exercise VIII.5, iterated 3-majority revealment exponent",
  "claim_path": "operations/claims/C0021.md",
  "status_before": "CLAIMED/CURRENT-OPEN-LOOKING/PARTIAL",
  "status_after": "CLAIMED/CURRENT-OPEN-LOOKING/PARTIAL",
  "metric": "rigorous sigma-interval width W_sigma",
  "metric_before": "0.083458870871305542695912279857623595744052789910165026420297166470678340599575491822859184",
  "metric_after": "0.083458052478335484902095404052916273307627595753522462739367968207135851225971433022261585",
  "movement": true,
  "unchanged_run_streak_before": 0,
  "unchanged_run_streak_after": 0,
  "methods": [10, 22, 28],
  "depth4_policy_cost_before": "1332477360033879887/36028797018963968",
  "depth4_policy_cost_after": "1332472567939180367/36028797018963968",
  "new_patch_states": 6,
  "new_patch_sign_orbits": 3,
  "checker_path": "proofnet24/P13-outside-successor/artifacts/2026-09-18/c0021_clock14_typical_patch_check.py",
  "checker_commit": "6e2e9a15a3d9a29168a3834d730173a85688f5ad",
  "output_path": "proofnet24/P13-outside-successor/artifacts/2026-09-18/c0021_clock14_typical_patch_check.out",
  "output_commit": "1227d331af094198a2448422def8c25993022c11",
  "self_check": "PASS",
  "p26_end_to_end_audit": "NOT_REQUESTED_NO_CLOSURE",
  "second_other_track_end_to_end_audit": "NOT_REQUESTED_NO_CLOSURE",
  "closure_claimed": false,
  "shared_root_ledgers_modified": false
}
```
