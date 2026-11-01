Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 at maximum. NO SOURCE-METRIC MOVEMENT: `W_sigma = 0.083457166870867772411698563411662... -> 0.083457166870867772411698563411662...`; C0021 unchanged-run streak `0 -> 1`. Methods actually tried: B1, B12, B27.**

# P13 / C0021 — Bellman-regret martingale and concave-envelope lower-bound route

Date: 2026-09-18 UTC. Track: P13 Outside Counterexample Research. Native slot: `6aa7b253b37c8191b693d8dc79298d37`. Own root: `proofnet24/P13-outside-successor/`.

Source target: Christophe Garban and Jeffrey E. Steif, *Noise Sensitivity of Boolean Functions and Percolation*, Exercise VIII.5 / book Open Problem XIII.1: determine the revealment exponent `sigma` for depth-`h` iterated 3-majority on `n=3^h` unbiased leaves.

Status after this run: **CLAIMED / CURRENT-OPEN-LOOKING / PARTIAL / NO SOURCE-METRIC MOVEMENT.** No closure, novelty certificate, or independent audit is claimed.

## 1. Continuity, ownership, exclusions, and recovered metric

I continued the create-only canonical claim `operations/claims/C0021.md`, which names this native slot and `proofnet24/P13-outside-successor/`. I did not reopen retired I0051, handed-off P0082, or six-run-handed-off D0093.

The mandatory I0054 screen was performed first. I0054 remains occupied by R11. The newest recovered R11 report is

`runs/R11/2026-09-18T17-40-00Z_i0054-uniform-first-factor-u028-c049-51af.md`,

which continues I0054 and moves its own frozen metric `48 -> 49`. P13 therefore did not touch that claim.

Before research I reread the owner directive at anchor `749da260517828ed311f6f1b1af74915c054bdf3`, `operations/NEW_METHODS_2026-09-16.md`, campaign `INDEX.md` and `RANKING.md`, root `POSTED.md`, `RESULTS.md`, `QUEUE.md`, the current C0021 claim, the newest P13 report, the neighboring R11 report, and the probability-1000 intake and attempt ledgers. The intake record for C0021 is the Garban--Steif Exercise VIII.5 target; its original attempt C0021-A001 gives only the much older natural recursive algorithm / influence bounds. Root `RESULTS.md` still contains stale retired-I0051 configuration history and was not allowed to override the newer canonical C0021 claim.

The inherited exact reduction remains

\[
\delta_{f_h}=\frac{D_h}{3^h},\qquad
c=\lim_{h\to\infty}D_h^{1/h}=\inf_h D_h^{1/h},\qquad
\sigma=1-\log_3 c,
\]

where `D_h` is the minimum expected number of leaf queries of a deterministic zero-error decision tree under iid unbiased leaves.

The frozen source metric is the width of the rigorous interval for this one exponent. The previous report certified

\[
0.178402340272047101787355665273859\ldots
\le \sigma \le
0.261859507142914874199054228685522\ldots
\]

and therefore

\[
W_\sigma=
0.083457166870867772411698563411662\ldots.
\]

Nothing in this run changes either asymptotic endpoint, so the source metric is unchanged and the unchanged-run streak becomes `1`.

## 2. Idea before code and the three required methods

The previous run exposed an exact positive square remainder in the O'Donnell--Servedio queried-sign lower bound. The goal here was to make that remainder recursive rather than to add another shallow Bellman patch.

- **B1 — change the category.** I moved the lower-bound problem from Fourier/Cauchy bookkeeping into stochastic control. The relevant object is the optimal completion value `V_h(s)` of a partially queried child, and the natural defect is the Bellman regret of the action actually taken.
- **B12 — find what is conserved.** This produced an exact childwise martingale: query count plus optimal remaining value minus accumulated Bellman regret has constant expectation. Combining the three children gives an exact parent accounting identity. The already-proved top-level pair-product martingale fixes the first moment of the residual child posterior.
- **B27 — swap the quantifiers.** The obvious pointwise induction `V-A <= D(1-m^2)` is false. I therefore replaced “every state obeys one scalar bound” by “there is one concave majorant controlling the average over whatever residual state an arbitrary exact outer algorithm leaves.” This works exactly at each fixed height and produces a new finite lower bound for `D_4`; what remains missing is a height-uniform strict envelope.

Only after these statements were derived was the exact finite state calculation written.

## 3. B12: Bellman-regret conservation

Fix a child height `h`. For a partial child state `s`, let

\[
V_h(s)
\]

be the optimal expected number of additional leaf queries required to determine `f_h` from `s`. Write

\[
D_h=V_h(o_h)
\]

for the full unqueried state `o_h`. If a legal query action `a` at `s` has two equiprobable successor states `s^+,s^-`, define its **local Bellman regret**

\[
r_h(s,a)
=
1+\frac{V_h(s^+)+V_h(s^-)}2-V_h(s)\ge0.
\tag{3.1}
\]

For a path through child states, let `R` be the sum of these regrets.

### Theorem 3.1 — exact three-child regret accounting

Consider any deterministic zero-error algorithm that evaluates

\[
\operatorname{Maj}_3(f_h^{(1)},f_h^{(2)},f_h^{(3)})
\]

under three independent unbiased depth-`h` inputs, with arbitrary interleaving between the children. Let `N_i` be the number of queries made in child `i`, `S_i` its state when the global algorithm stops, and `R_i` the accumulated local Bellman regret (3.1) of the actions actually used in that child. Then

\[
\boxed{
\mathbb E\!\left[N_i+V_h(S_i)-R_i\right]=D_h
}
\tag{3.2}
\]

for each child. If `J` denotes the child left over after choosing two children certified equal to the final root value, then

\[
\boxed{
\mathbb E T
=
3D_h-\mathbb E V_h(S_J)
+\mathbb E(R_1+R_2+R_3).
}
\tag{3.3}
\]

#### Proof

Project the global interleaved transcript onto one fixed child. When the next global query is outside that child, `N_i`, `V_h(S_i)`, and `R_i` do not change. When the next query is an action `a` at child state `s`, the query count increases by one and, by definition of `r_h`,

\[
\mathbb E[V_h(S_i^{\rm next})\mid s,a]
=
V_h(s)-1+r_h(s,a).
\]

The regret accumulator increases by exactly `r_h(s,a)`. Hence the conditional expected increment of

\[
N_i+V_h(S_i)-R_i
\]

is zero. It starts at `D_h`, proving (3.2) by finite optional stopping.

At global termination, exact determination of the majority forces at least two child functions to be individually fixed to the final root value: otherwise two not-fixed-to-that-value children could be completed independently to the opposite value and flip the root, contradicting zero error. Choose such a certified agreeing pair and call the remaining child `J`. The two certified children have completion value zero, so

\[
V_h(S_1)+V_h(S_2)+V_h(S_3)=V_h(S_J).
\]

Summing (3.2) over the three children and using `T=N_1+N_2+N_3` gives (3.3). ∎

Now define

\[
A_h(s)
=
\min\{\text{accumulated Bellman regret over a legal path }o_h\to s\}.
\tag{3.4}
\]

The actual projected path to `S_J` is one such legal path, so

\[
R_J\ge A_h(S_J),
\]

and all other regrets are nonnegative. Thus (3.3) immediately gives

\[
\boxed{
D_{h+1}
\ge
3D_h-
\mathbb E\!\left[V_h(S_J)-A_h(S_J)\right].
}
\tag{3.5}
\]

This is the first new structural reduction of the run.

## 4. The conserved top-level first moment

Let

\[
m_i(t)=\mathbb E[f_h^{(i)}\mid\mathcal F_t]
\]

be the three child-output posterior martingales under a global exact algorithm. The previous P13 run already proved that

\[
Z_t=m_1m_2+m_1m_3+m_2m_3
\]

is a martingale. At stopping, after choosing two certified children equal to the root value `R`, the remaining child `J` has posterior `m_J`, and

\[
Z_\tau=1+2R\,m_J.
\]

Since `Z_0=0`,

\[
\boxed{\mathbb E[R\,m_J]=-\frac12.}
\tag{4.1}
\]

I use (4.1) here as inherited proved input rather than claiming it again.

## 5. B27: replace a false pointwise bound by a concave envelope

For every canonical child state set

\[
m_h(s)=\mathbb E[f_h\mid s]\in[-1,1]
\]

and define the normalized regret-corrected residual profile

\[
g_h(x)
=
\max_{\{s:m_h(s)=x\}}
\frac{V_h(s)-A_h(s)}{D_h}.
\tag{5.1}
\]

Global sign flip preserves `V_h` and `A_h` and negates `m_h`, so `g_h` is even. Let `F_h` be the least concave majorant of the finite profile `g_h`, and put

\[
\rho_h=F_h(-1/2).
\tag{5.2}
\]

### Theorem 5.1 — concave-envelope one-step lower bound

For every `h`,

\[
\boxed{
D_{h+1}\ge(3-\rho_h)D_h.
}
\tag{5.3}
\]

#### Proof

For the residual child in any exact outer algorithm, write

\[
X=R\,m_h(S_J).
\]

Because `R` is a sign, evenness gives

\[
F_h(m_h(S_J))=F_h(X).
\]

By definition of `F_h`,

\[
V_h(S_J)-A_h(S_J)
\le
D_hF_h(X).
\]

Taking expectations, applying concavity and then the conserved first moment (4.1),

\[
\mathbb E[V_h(S_J)-A_h(S_J)]
\le
D_h\mathbb E F_h(X)
\le
D_hF_h(\mathbb EX)
=
D_hF_h(-1/2)
=
\rho_hD_h.
\]

Substitute this in (3.5). Since the argument applies to every exact deterministic outer algorithm, it applies in particular to the optimum `D_{h+1}`. ∎

This theorem is the B27 quantifier swap: no pointwise uncertainty inequality is required. Only one concave envelope and one conserved average are used.

## 6. Exact finite calculation through child height three

The exact-arithmetic self-check enumerates the complete recursive child-permutation quotient of partial states through height three, computes `V_h` by exact Bellman recursion, computes every local regret, computes `A_h` by the acyclic shortest-regret recursion, constructs the exact upper concave hull, and evaluates it at `-1/2`.

The complete exact output is:

| child height `h` | canonical states | `D_h` | regret-corrected `rho_h` | raw envelope at `-1/2` | resulting lower bound on `D_{h+1}` | failures of the pointwise uncertainty candidate |
|---:|---:|---:|---:|---:|---:|---:|
| 0 | 3 | `1` | `1/2` | `1/2` | `5/2` | 0 |
| 1 | 6 | `5/2` | `3/5` | `3/5` | `6` | 0 |
| 2 | 46 | `393/64` | `585/917` | `91/131` | `3249/224` | 2 |
| 3 | 17,206 | `15796051/1048576` | `165736792/236940765` | `48395511900/64905973559` | `545085503/15728640` | 146 |

For height three,

\[
\boxed{
\rho_3=
\frac{165736792}{236940765}
=
0.6994861859249927\ldots
}
\]

and therefore

\[
\boxed{
D_4\ge
\frac{545085503}{15728640}
=
34.65560296376546\ldots.
}
\tag{6.1}
\]

The two exact hull vertices bracketing `-1/2` are

\[
\left(-\frac{293}{512},
\frac{10088708}{15796051}\right),
\qquad
\left(-\frac{31}{64},
\frac{11256776}{15796051}\right),
\]

and exact interpolation between them gives the displayed `rho_3`.

Combining (6.1) with the current explicit 52-override upper policy gives the finite-depth bracket

\[
\boxed{
\frac{545085503}{15728640}
\le D_4\le
\frac{1332467382289843607}{36028797018963968}.
}
\tag{6.2}
\]

No claim is made here that either endpoint equals `D_4`.

### Exact obstruction to the tempting pointwise induction

The natural stronger candidate

\[
V_h(s)-A_h(s)
\stackrel{?}{\le}
D_h\bigl(1-m_h(s)^2\bigr)
\tag{6.3}
\]

already fails at height two. For the exact canonical state

\[
s=
\bigl(+,(+,u,u),(+,u,u)\bigr),
\]

the checker gives

\[
m_2(s)=\frac78,\qquad
V_2(s)=\frac{15}{8},\qquad
A_2(s)=\frac38.
\]

Thus

\[
V_2(s)-A_2(s)=\frac32,
\]

whereas

\[
D_2(1-m_2(s)^2)
=
\frac{5895}{4096},
\]

with exact excess

\[
\boxed{\frac{249}{4096}>0.}
\]

There are exactly two sign-conjugate failures at height two and 146 failures in the 17,206 canonical height-three states. This is why the quantifier swap to a concave average envelope is necessary.

The raw envelope, without Bellman-regret credit, is already

\[
0.7456249285900954\ldots
\]

at height three, very close to the critical `3/4`. The regret-corrected envelope lowers it to about `0.69949`, so the conservation law is doing real work.

## 7. Why the frozen source metric does not move

Equation (6.1) is a genuine new finite lower bound, but the source exponent depends on

\[
c=\inf_hD_h^{1/h}.
\]

A lower bound on one finite value `D_4` does **not** imply

\[
c\ge D_4^{1/4}.
\]

Therefore it cannot be used to lower the source upper endpoint for `sigma`.

The exact route would become source-moving if one proved a height-uniform strict envelope

\[
\boxed{
\rho_h\le\rho<\frac34
\quad\text{for all sufficiently large }h.
}
\tag{7.1}
\]

Then Theorem 5.1 would give

\[
D_{h+1}\ge(3-\rho)D_h,
\qquad
c\ge3-\rho>\frac94,
\]

which would strictly decrease the current rigorous upper endpoint

\[
\sigma\le\log_3(4/3).
\]

The finite exact sequence

\[
\rho_0=\frac12,\quad
\rho_1=\frac35,\quad
\rho_2=\frac{585}{917}\approx0.63795,\quad
\rho_3\approx0.69949
\]

does not establish (7.1). It is evidence for the shape of the correct invariant, not an asymptotic theorem. This is the precise residual obstruction after B1/B12/B27.

## 8. Exact artifact and self-check status

Executed exact-arithmetic checker:

`proofnet24/P13-outside-successor/artifacts/2026-09-18/c0021_bellman_envelope_2026-09-18T19-21-21Z_check.py`

Creation commit: `3b5765922c43dbf5983917997772eaff5614142a`  
Read-back Git blob: `949b409f737ff33f9686d5f628cc1b041add0dc5`  
SHA-256: `25d2ed7bc845b723ef1d90c872d54e2b27cfc5db387c5f4b6384681ac7fc74ee`

Archived output:

`proofnet24/P13-outside-successor/artifacts/2026-09-18/c0021_bellman_envelope_2026-09-18T19-21-21Z_check.out`

Creation commit: `53d044d68fe957968ca6277be0b45c9d464c1bfe`  
Read-back Git blob: `366ab94067128daf471c54aab37523deb7db0c6f`  
SHA-256: `05cec7247b5fea54d41868c7583a257e4883d841917f375745bd73a205f2395e`

The output ends

`ALL_EXACT_BELLMAN_ENVELOPE_CHECKS_PASS`.

This is a **P13 self-check**, not an independent audit.

## 9. Source and literature refresh, 2026-09-18

The original Clay proceedings text was rechecked. Exercise VIII.5 says that iterated 3-majority revealment decays like `1/n^sigma` for some `sigma` and explicitly says that determining `sigma` is open. The later Cambridge book's Open Problem XIII.1 likewise asks for the randomized algorithm of smallest revealment and says even the exponent is not known in that source.

A fresh bounded search used, among others, the dated queries:

- `"iterated 3-majority" revealment exponent sigma Garban Steif`
- `"revealment exponent" iterated majority`
- `"recursive majority" uniform expected decision tree complexity`
- `"expected deterministic complexity" recursive ternary majority`
- `"majority-of-three" decision tree uniform distribution complexity 2024 2025 2026`

The closest checked literature remains:

1. Michael Simkin, *Random-Turn and Richman Games* (MSc thesis, 2014): the same uniform expected deterministic complexity, the classical `(9/4)^h` lower bound, and the level-two value `393/64`; it does not determine the asymptotic exponent.
2. Julia Jansson and Patrik Jansson, *Level-p-complexity of Boolean functions using thinning, memoization, and polynomials* (JFP, 2023): exact finite-level machinery applied to two-level iterated majority, not the asymptotic exponent.
3. Magniez--Nayak--Santha--Sherman--Tardos--Xiao, *Improved bounds for the randomized decision tree complexity of recursive majority* (2016): worst-case randomized query complexity under the problem's worst-case/minimax formulation, not the iid-uniform expected cost defining `D_h`.
4. The 2025 ITCS recursive-majority lifting application likewise concerns worst-case randomized/parity decision-tree complexity, not this source metric.
5. The June 2026 paper titled *Majority-of-Three is Optimal* is about realizable PAC learning and is unrelated to this revealment problem.

I found no checked source-matching determination of `sigma` in this bounded search. This is bounded negative evidence only, not a global openness or novelty certificate.

PDF analysis requirement/access note: the Clay PDF text layer exposed the Exercise VIII.5 statement on PDF page 127, but the required screenshot attempt returned an internal cache-miss/fetch error. The failure is recorded here rather than treated as a successful visual verification.

## 10. What the three approaches accomplished

- **B1 succeeded structurally:** the lower-bound problem now has a Bellman-regret / stochastic-control formulation with a theorem-sized exact accounting identity.
- **B12 succeeded structurally but killed its simplest induction:** the conserved childwise quantity gives exact regret credit, while the natural pointwise uncertainty domination is exactly false from height two onward.
- **B27 succeeded at fixed height:** the concave-envelope theorem turns only the conserved average `E[Rm_J]=-1/2` into an arbitrary-algorithm lower bound and gives `D_4 >= 545085503/15728640`. It does not yet supply the uniform strict `rho<3/4` needed for asymptotic source movement.

This is substantive mathematical movement but **not source-metric movement**.

## 11. Next nonrepeating route

Next methods are recorded as **B4, B16, B21**.

- **B4:** prove a weaker statement completely: seek an inductively closed subclass of residual states on which a height-uniform envelope can be proved, and quantify whether every exact outer algorithm must leave that subclass with positive mass.
- **B16:** compute the next small case without attempting the impossible full height-four state space; exploit the posterior/orientation quotient and exact branch-and-bound to test whether `rho_h` crosses or stays below `3/4`.
- **B21:** look for the same Bellman-regret / concave-envelope shape in sequential testing, controlled martingales, and three-diffusion majority scheduling, where a ready-made supermartingale may provide the missing uniform envelope.

No stuck-rule recovery is triggered: this is the first unchanged source-metric run after the preceding movement.

## 12. Structured ledger delta for P26

```yaml
ledger_delta:
  track: P13
  canonical_id: C0021
  native_slot: 6aa7b253b37c8191b693d8dc79298d37
  root: proofnet24/P13-outside-successor
  source: "Garban--Steif, iterated 3-majority revealment exponent"
  status_before: CLAIMED_CURRENT_OPEN_LOOKING_PARTIAL
  status_after: CLAIMED_CURRENT_OPEN_LOOKING_PARTIAL
  frozen_metric: rigorous_sigma_interval_width
  metric_before: "0.083457166870867772411698563411662..."
  metric_after: "0.083457166870867772411698563411662..."
  source_metric_movement: false
  unchanged_run_streak_before: 0
  unchanged_run_streak_after: 1
  methods_tried: [B1, B12, B27]
  theorem_delta:
    bellman_regret_accounting: PROVED_AUTHOR_SIDE
    concave_envelope_one_step_lower_bound: PROVED_AUTHOR_SIDE
    source_asymptotic_closure: NOT_PROVED
  finite_delta:
    canonical_states_h3: 17206
    rho_3: "165736792/236940765"
    D4_lower: "545085503/15728640"
    D4_upper_inherited: "1332467382289843607/36028797018963968"
    pointwise_candidate_h2_status: REFUTED_BY_EXACT_STATE
  checker:
    path: proofnet24/P13-outside-successor/artifacts/2026-09-18/c0021_bellman_envelope_2026-09-18T19-21-21Z_check.py
    creation_commit: 3b5765922c43dbf5983917997772eaff5614142a
    output_path: proofnet24/P13-outside-successor/artifacts/2026-09-18/c0021_bellman_envelope_2026-09-18T19-21-21Z_check.out
    output_commit: 53d044d68fe957968ca6277be0b45c9d464c1bfe
    self_check: true
    pass_marker: ALL_EXACT_BELLMAN_ENVELOPE_CHECKS_PASS
  literature_status: bounded_search_no_source_matching_resolution_found
  source_pdf_screenshot: FAILED_INTERNAL_CACHE_MISS
  closure_claimed: false
  audits_claimed: []
  next_methods: [B4, B16, B21]
```

No shared root ledger, historical report, peer file, claim owned by another track, workflow, public surface, email/Gmail item, Drive item, credential, permission, paid-compute resource, or schedule was modified.
