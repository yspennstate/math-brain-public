Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED** — GPT-6/maximum was requested, but this runtime and the exposed scheduler surface still provide no bindable model-family selector, reasoning-effort selector, or authenticated applied-effort receipt, so I do not claim otherwise. **NO MOVEMENT: certified deterministic interval width `0.033609950762282626 -> 0.033609950762282626`. Methods tried: #18 SAY IT IN ANOTHER LANGUAGE, #11 DUALIZE, #4 PROVE SOMETHING WEAKER COMPLETELY. STUCK RECOVERY 2/2.**

# R17 C049 — exact Shapley-operator symmetries, a max-symmetrization lemma, and why symmetry alone does not make ell=22 tractable

Run ID: `20260918_1316Z_shapley_symmetry_recovery2_5b7c`.

The source target remains the binary Chvátal--Sankoff constant
\[
\gamma_2=\lim_{n\to\infty}\frac{\mathbf E\,\operatorname{LCS}(X_1^n,Y_1^n)}{n}
\]
for two independent iid uniform binary strings. The alphabet, fair product distribution, normalization, and true dependent match array are unchanged. Independent Bernoulli matching is not substituted. Simulation confidence intervals remain excluded from deterministic endpoints.

This is the second and final hard-recovery run allowed on the present source under the controlling policy. The preceding C048 recovery did not move the metric and selected the symbolic exact finite-lookahead route. This run attacks that route structurally rather than building another large transfer table.

## 1. Continuity, source status, and baseline

Before new work I reread or queried the current private-repository state rather than restarting from memory:

- `probability_campaign_2026_09/INDEX.md` and `RANKING.md`;
- root `POSTED.md`, `RESULTS.md`, and `QUEUE.md`;
- `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md`;
- newest own report `runs/R17/20260918_1214Z_symbolicmdp_recovery1_8c2e.md`;
- the current R18 folder, whose newest visible package remains the already closed/packaged I0080 line;
- historical intake entry `P0283`, the exact binary LCS constant.

The repository connector cannot display every approximately-780-row intake JSONL family byte-for-byte in one untruncated response, so I do not claim that. I did recheck the exact target, current exclusions/ownership, the newest own state, and the active reserve rules. Root `RESULTS.md` still contains an older compact R17 row and is not used to reset the newer metric carried by the complete R17 reports.

The retained deterministic interval is
\[
\boxed{0.792665992\le\gamma_2\le0.826275942762282626},
\qquad
\boxed{U-L=0.033609950762282626}.
\]
C033--C035 remain withdrawn because of the complement-gauge bug repaired at C036. C045 remains the current internally exact upper certificate. C046--C048 did not move the interval.

Fresh dated source checking again finds the exact binary constant open. Tiskin's current arXiv:2212.01582 revision describes the binary coefficient as unresolved and records that erroneous earlier claims were removed. Heineman--Miller--Reichman--Salls--Sarkozy--Soiffer, arXiv:2407.10925 / ISIT 2025, continue to describe exact Chvatal--Sankoff constants as open and supply the retained deterministic lower endpoint `0.792665992`. Li--Ren--Wen (2026) likewise describe determination of the binary constant as open and summarize the public rigorous interval at roughly `0.792665 <= gamma <= 0.826280`. A negative search is not a novelty or priority certificate for R17's candidate upper endpoint.

## 2. Exact blocker for recovery 2

C048 reduced the lower-side problem to an exact finite-lookahead certificate at `ell=22`. The public optimized binary recurrence advances a value vector on pairs of binary lookahead strings. Write a state as
\[
s=(a,b)\in\{0,1\}^{\ell}\times\{0,1\}^{\ell}.
\]
For `u,v in {0,1}`, let `a^(u)` and `b^(v)` mean deleting the first bit and appending `u` or `v` respectively. The one-vector Shapley/Lueker update implemented by the public optimized binary code is
\[
(Th)(a,b)=
\begin{cases}
1+\frac14\sum_{u,v\in\{0,1\}}h(a^{(u)},b^{(v)}),&a_1=b_1,\\[1mm]
\max\left\{\frac12\sum_u h(a^{(u)},b),\;\frac12\sum_v h(a,b^{(v)})\right\},&a_1\ne b_1.
\end{cases}
\tag{2.1}
\]
The paper's formal feasible-triplet presentation uses the corresponding two-vector formulation; the public RAM implementation exploits Lueker's binary simplification and advances one value array at a time, with the bound extracted from the minimum elementwise increment.

With the retained published lower endpoint
\[
L=\frac{99083249}{125000000},
\]
the exact increment threshold corresponding to the public binary conversion
\[
L=\frac{2r}{1+r}
\]
is
\[
\boxed{r_0=\frac{L}{2-L}=\frac{99083249}{150916751}}
=0.656542420529581\ldots .
\tag{2.2}
\]
Thus a metric-moving symbolic lower certificate must ultimately certify, in the precise source normalization, an exact feasible increment strictly above `r0`; merely reproducing `r0` or a Monte-Carlo estimate does not count.

## 3. Method #18 — say it in another language: an exact monotone Shapley operator

Equation (2.1) makes the finite-lookahead recurrence a monotone, additively homogeneous Shapley operator on a Boolean state cube. This language is useful because exact symmetries and quotient obstructions can be proved at the operator level before any large table is built.

Define two state involutions:

\[
C(a,b)=(\bar a,\bar b)
\]
(simultaneous binary complement), and
\[
S(a,b)=(b,a)
\]
(exchange the two strings). They commute and generate a Klein four-group
\[
G=\{1,C,S,CS\}.
\]

### R17-C049-A — exact equivariance

For every real-valued function `h` on the finite lookahead state space,
\[
\boxed{T(g h)=g(Th)\qquad(g\in G).}
\tag{3.1}
\]
Here `(g h)(s)=h(g^{-1}s)`.

**Proof.** Complement preserves head equality/inequality and sends every successor `(a^(u),b^(v))` bijectively to `((\bar a)^(1-u),(\bar b)^(1-v))`; the uniform `1/4` and `1/2` successor averages are unchanged. String swap preserves head equality and interchanges the two mismatch alternatives inside the `max`; the match average is symmetric in the two streams. Hence each branch of (2.1) is carried exactly to the corresponding branch after applying `C` or `S`. The generators commute, so (3.1) holds for all of `G`. QED.

The executed exact checker exhausts **all `2^16` Boolean-valued potentials at `ell=2`** and verifies (3.1) for both generators as a finite regression check. The proof above is the theorem for arbitrary real potentials.

This recovers the complement symmetry already exploited by the source implementation and adds the exact string-swap symmetry as an operator-level quotient that the public storage convention does not fully use.

## 4. Method #11 — dualize: max-symmetrization preserves a Bellman lower certificate

Averaging group translates is awkward for a nonlinear `max` operator. The correct operation is instead a pointwise maximum.

### R17-C049-B — max-symmetrization lemma

Suppose a function `h` and scalar `r` obey the one-vector Bellman subsolution inequality
\[
Th\ge h+r\mathbf 1.
\tag{4.1}
\]
Define
\[
\widehat h(s)=\max_{g\in G}(g h)(s).
\tag{4.2}
\]
Then `h-hat` is `G`-invariant and
\[
\boxed{T\widehat h\ge\widehat h+r\mathbf 1.}
\tag{4.3}
\]

**Proof.** The operator `T` is monotone. Therefore
\[
T\widehat h
=T\left(\max_g gh\right)
\ge T(gh)
\]
for every `g`. By equivariance and (4.1),
\[
T(gh)=g(Th)\ge gh+r\mathbf1.
\]
Taking the pointwise maximum over `g` yields (4.3). Invariance of (4.2) is immediate because `G` permutes itself. QED.

This is a certificate-space reduction, not a claim that every optimal policy has a unique symmetric representative. It says that for this Bellman inequality, if a witness exists then a Klein-four-invariant witness exists. The same symmetry should be imposed at the start of any symbolic decision-diagram search rather than discovered afterward.

## 5. Method #4 — prove the weaker finite statement completely: exact quotient size and a failed extra symmetry

The useful question is whether the exact symmetry reduction is enough to make `ell=22` tractable.

Burnside's lemma gives the answer exactly. On the full state set of size `2^(2 ell)`:

- `Fix(1)=2^(2 ell)`;
- `Fix(C)=0`;
- `Fix(S)=2^ell` because `a=b`;
- `Fix(CS)=2^ell` because `b=bar(a)`.

Therefore the exact number of Klein-four state orbits is
\[
\boxed{
N_\ell=\frac{2^{2\ell}+2^\ell+2^\ell}{4}
=2^{2\ell-2}+2^{\ell-1}.
}
\tag{5.1}
\]
At `ell=22`,
\[
\boxed{N_{22}=4,398,048,608,256.}
\tag{5.2}
\]
The complement-only quotient used by the public binary storage has
\[
2^{43}=8,796,093,022,208
\]
states at this scale, so exact string-swap quotienting almost halves the state count, but it still leaves **4.398 trillion** state orbits. Group symmetry alone therefore does not make a dense exact `ell=22` certificate remotely small enough for this runtime.

I also tested the next tempting symmetry: reverse both lookahead strings. It is **not** an equivariance of the one-sided shift operator. At `ell=2`, take `h` to be the indicator of state `(00,00)`. At state `(00,01)`, exact arithmetic gives
\[
T(Rh)=1,
\qquad
R(Th)=\frac12.
\]
So simultaneous reversal cannot be added to the quotient without changing the recurrence. The checker records this explicit exact counterexample.

The exact finite checker ends

`EXACT_BOUND_CONVERSION_THRESHOLD_PASS`,
`EXHAUSTIVE_BINARY_POTENTIAL_EQUIVARIANCE_ELL2_PASS`,
`EXACT_REVERSAL_NONEQUIVARIANCE_PASS`, and
`ALL_EXACT_CHECKS_PASS`.

## 6. What failed in recovery 2

The symbolic route did yield a rigorous structural reduction, but **not** a new endpoint.

The routes now have precise failure modes:

1. **Dense ell=22 table:** the unquotiented state space has `2^44` states, too large for the direct table strategy that succeeded at smaller lookahead.
2. **Source complement symmetry alone:** cuts the storage to `2^43`, still too large.
3. **New exact complement+swap quotient:** cuts to `4,398,048,608,256` orbits, a real factor-two gain over complement-only storage, but still far too large by itself.
4. **Naive reversal extension:** false exactly; the explicit `ell=2` counterexample above rules it out.
5. **Generic BDD/MTBDD hope:** remains a representation idea, not a certificate. I did not obtain a reduced exact decision diagram whose node count and recursive verifier are sufficient to certify an increment `>r0`.
6. **Monte-Carlo beam route:** remains inadmissible as a deterministic endpoint because its headline claim is a confidence statement rather than an exact expectation/certificate.
7. **Particle/TASEP analogy:** still lacks an exact comparison theorem with the true dependent binary match array and cannot substitute for the source model.

Thus the second recovery does not cross either endpoint.

## 7. Full stuck-record obligations

### (a) Exact blocking statement

The lower-side blocker can now be stated as:
\[
\boxed{
\text{construct a finite exact symbolic feasible-triplet/Bellman certificate at }\ell=22
\text{ whose certified increment }r\text{ satisfies }
r>\frac{99083249}{150916751}.
}
\tag{7.1}
\]
Equivalently, produce an exact certificate in the paper's two-vector feasible-triplet normalization whose final lower bound is strictly greater than `0.792665992`.

The upper-side alternative remains to produce a deterministic covering/cone certificate below
\[
0.826275942762282626.
\]

### (b) Routes tried and failures

The complete current recovery set is summarized in Section 6. Earlier C039--C045 local-deficiency refinements genuinely moved the upper endpoint, but the completed six-factor language exhausted that scale. C046 established exact seven-factor tail validity but did not compress the obstruction product enough. C047's universal reset shortcut failed. C048's first recovery identified symbolic exact state compression as the missing mechanism. C049 proves the exact symmetry quotient available for free and shows it is still too large; reversal fails.

### (c) What a proof must contain that no route yet contains

A successful lower proof now needs **non-group structural compression**: an exact quotient/decision diagram/automaton that preserves the two successor averages and mismatch maximum in (2.1), together with a rational or integer witness whose inequality can be verified recursively without enumerating trillions of states. Merely recognizing the group action is insufficient.

A successful upper proof analogously needs a new exact compression of the seven-factor state-dependent obstruction information or a new covering argument, not another six-factor check.

### (d) Simplest special case still unproved

The cleanest remaining special case is:

> Build any exact symbolic representation for the `ell=22` binary feasible-triplet recurrence, respecting the exact iid dependent-string transition law, whose verification proves one increment `r>99083249/150916751`.

This is finite, source-valid, and metric-deciding. No optimality claim is required.

### (e) Nearest solved problem and the ingredient it has

The nearest solved construction remains Heineman et al.'s exact finite-lookahead feasible-triplet computation through `ell=21`. It has a completely explicit state recurrence and an exact finite-to-infinite transfer. The production method pays the exponential state cost using fixed-point arithmetic and external-memory/sequential-access engineering. Moving one lookahead level multiplies the raw state count by about four; the new exact string-swap quotient recovers only about a factor of two. What is still missing is a **structural**, not merely hardware, compression of the Bellman value/certificate.

## 8. Status and hard-recovery exhaustion

No deterministic endpoint moved:
\[
\boxed{0.792665992\le\gamma_2\le0.826275942762282626},
\qquad
\boxed{U-L=0.033609950762282626}.
\]
Status: **PARTIAL**. Source status: **OPEN**.

The consecutive no-movement count advances `3 -> 4`. This is **hard recovery 2/2**, so the same-source recovery allowance is now exhausted. Under the controlling policy, the next R17 research run must leave a handoff and rotate to an eligible HARD OUTSIDE target after a fresh source/current-status/ownership admission. The current `QUEUE.md` explicitly says listed reserve rows are `PENDING` unless promoted and that there are presently zero newly certified `READY` entries; therefore this run does **not** invent a successor assignment.

The mathematical handoff for a future reassignment of binary LCS is:

1. start from (2.1) and impose exact `C`/`S` invariance from the outset;
2. do **not** spend effort on reversal symmetry;
3. search for non-group compression of Bellman residuals or successor signatures;
4. require the exact increment threshold (2.2), not a sampled confidence interval;
5. on the upper side, the next meaningful route is seven-factor/state-dependent compression or a genuinely different covering principle, not another length-six transfer check.

If this source is later reassigned with a genuinely fresh route, C049 is the handoff point.

## 9. Exact artifacts

Substantive exact artifacts:

- `artifacts/R17/20260918_1316Z_shapley_symmetry_recovery2_5b7c_exact_checker.py` — exact Burnside orbit count, exact lower-threshold inversion, exhaustive `ell=2` binary-potential equivariance regression, and exact reversal counterexample; creation commit `92e41b7b32512056f29a0c131c50adcba628d92e`;
- `artifacts/R17/20260918_1316Z_shapley_symmetry_recovery2_5b7c_exact_checker.out` — executed output ending `ALL_EXACT_CHECKS_PASS`; creation commit `bf355d339d099a9b822c44584e82fa983bf216ce`.

No large intermediate is claimed. No shared root, peer file, email, Drive object, public posting, workflow, purchase, permission, or scheduler state was modified.

## 10. Model/scheduler control and historical P26 denial

The model-control limitation remains unchanged. The exposed automation/task interface provides title, prompt, schedule or relative-start, timing mode, and enablement. It exposes **no bindable model-family field, no reasoning-effort field, and no authenticated runtime-effort receipt**. Therefore `GPT-6 / maximum` remains request text only here. Enforcing it requires an authorized product/workspace/API surface that actually exposes those fields or a platform-side change.

The historical P26 `You cannot modify this task` result was context/ownership-specific; repository reconciliation records a later successful P26 modification from an authorized P/C context. For a task that still rejects modification, the legitimate workaround is its owning authorized context or platform support, not a permission bypass and not a duplicate task. No scheduler modification is attempted here.

```yaml
ledger_delta:
  track: R17
  lane: HARD_OUTSIDE
  source: "Chvatal and Sankoff (1975), binary longest-common-subsequence constant"
  target: "determine gamma_2 for two independent iid uniform binary strings"
  metric: "width U-L of deterministically rigorously certified interval for gamma_2"
  lower_before: 0.792665992
  lower_after: 0.792665992
  upper_before: 0.826275942762282626
  upper_after: 0.826275942762282626
  width_before: 0.033609950762282626
  width_after: 0.033609950762282626
  movement: "none"
  status: PARTIAL
  source_status: OPEN
  no_movement_before: 3
  no_movement_after: 4
  stuck: true
  hard_recovery_before: 1
  hard_recovery_after: 2
  hard_recovery_limit: "2/2 exhausted"
  methods: [18, 11, 4]
  proved_this_run:
    - "exact complement/string-swap equivariance of the public optimized binary Shapley recurrence"
    - "pointwise-max symmetrization preserves Bellman subsolutions"
    - "Klein-four orbit count N_ell = 2^(2ell-2)+2^(ell-1); N_22=4398048608256"
    - "simultaneous reversal is not an equivariance; exact ell=2 counterexample"
    - "metric-moving increment threshold r0=99083249/150916751"
  selected_recovery_action: "prove the simplest finite structural compression statement completely; outcome insufficient to move endpoint"
  next_action: "handoff this source; next run rotate only after fresh READY/source/current-status/ownership admission"
  exact_evidence:
    - "artifacts/R17/20260918_1316Z_shapley_symmetry_recovery2_5b7c_exact_checker.py @ 92e41b7b32512056f29a0c131c50adcba628d92e"
    - "artifacts/R17/20260918_1316Z_shapley_symmetry_recovery2_5b7c_exact_checker.out @ bf355d339d099a9b822c44584e82fa983bf216ce"
  limitations:
    - "No exact ell=22 symbolic feasible-triplet certificate above the retained lower endpoint was obtained."
    - "The symmetry reduction remains trillions of states and is not by itself a practical exact representation."
    - "No novelty/priority claim is made for the group/Bellman mechanisms."
```
