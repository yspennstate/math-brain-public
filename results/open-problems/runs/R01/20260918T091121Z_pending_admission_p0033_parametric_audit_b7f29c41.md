Model actually ran: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — this is not GPT-6 at maximum, and I do not claim otherwise. NO MOVEMENT on R01 successor admission: I0024 remains frozen at `C=1 -> 1`; no lawful successor was admitted, so the successor metric remains `UNMEASURED -> UNMEASURED`; status `PENDING_ADMISSION`. New-method moves this run: #7 TAKE THE LIMIT, #15 BREAK THE SYMMETRY ON PURPOSE, #19 MAKE IT AN ALGORITHM. Independent neighboring audit `R01-AUDIT-R02-P0033-Q17.18-01 = PASS_MATHEMATICAL_SOURCE_SCOPE`, with a stronger two-parameter counterexample family proved below.**

# R01 — pending admission; independent P0033 audit and a parametric conservative-automaton counterexample family

## 1. Continuity and repository state

I reread the required current repository surfaces before doing new mathematics: `probability_campaign_2026_09/INDEX.md`, `RANKING.md`, root `POSTED.md`, `RESULTS.md`, `QUEUE.md`, the latest operations implementation manifest `operations/FOLLOWUP_IMPLEMENTATION_2026-09-16.md`, the newest R01 report, the newest neighboring R02 work, targeted intake material, and the newest strict admission/root reconciliation delta.

The exact R01 history is preserved rather than restarted. Aldous--Fill Open Problem 3.44 / intake I0024 remains frozen at the previously proved exact value `C=1`, with the right-inverse formula

\[
\tau_2=
\inf_{R:\,BR=I_{H_0}}
\sup_{0\ne b\in H_0}
\frac{(Rb)^T C^{-1}(Rb)}{b^T\Pi^{-1}b},
\qquad
R_*=CB^T L^+.
\]

Its existing independent audits are not reopened. The old FEI assignment remains retired and owned by P03.

The newest exact coordinator reconciliation (`operations/task_health/runs/2026-09-18T085800Z/root_reconciliation_delta.md`) says that **no candidate crossed READY** in the latest strict admission delta; new claims `C0146`, `H0006`, `P0033`, and `P0281` only shrink free inventory. Therefore I did not manufacture an R01 successor, promote a PENDING/HARD row, or overwrite another track's claim.

The neighboring R02 track, however, has just produced a complete mathematical P0033 package with a written proof and exact self-check: commit `33c13b0eda0ac882ba76c4eedfd9af42530d86c9`. Because R01 currently has no admitted research target, I used the allowed checking slice to perform a genuinely independent source-scope audit. Most of the run was not bookkeeping: the audit route produced the stronger two-parameter theorem below.

## 2. Fresh source checks, dated 2026-09-18

### I0024 / Aldous--Fill

The live Aldous--Fill Chapter 3 notes still state Open Problem 3.44 verbatim in substance: since commute times have dual potential/flow extrema, ask whether relaxation time has an **exact** infimum-over-flows characterization; Chapter 4 supplies only an upper bound. Bounded searches for the exact phrase, `relaxation time infimum flows`, and later work did not recover a later primary source explicitly stating the stationary-weighted right-inverse formula above. That is negative search evidence only; priority/novelty remains `UNVERIFIED`.

### P0033 / Lyons--Peres Question 17.18

The current *Probability on Trees and Networks* text still asks:

> If a flow rule has a stationary measure equivalent to GW, must the associated Markov chain be ergodic?

The preceding proposition assumes every first-generation flow weight is positive; the question asks whether that positivity hypothesis is necessary for the final ergodicity conclusion. The same text's Exercise 17.22 gives a nonergodic stationary example that is only absolutely continuous with respect to GW, not equivalent to GW, so it does not answer Question 17.18.

Fresh queries used included exact/source phrases around `Question 17.18`, `stationary measure equivalent to GW`, `nonergodic flow rule`, the R02 constants `3/5`, `2/5`, `9/10`, and mixed `AND/OR` Galton--Watson automata. The closest relevant later literature recovered is Johnson--Podder--Skerman, *Random tree recursions: Which fixed points correspond to tangible sets of trees?*, RSA 56 (2020), 796--837, which develops interpretation/endogeny theory for tree automata. I found no explicit published source-matching resolution of Question 17.18 or the conservative-flow synthesis below. This remains a bounded prior-art screen, not a novelty certificate.

## 3. What I audited in R02

R02 takes offspring law

\[
\mathbb P(D=2)=\frac35,\qquad \mathbb P(D=3)=\frac25,
\]

uses AND at degree 2 and OR at degree 3 to construct an endogenous binary color `c(T)`, and lets the flow choose uniformly among children having the same color as their parent. R02 proves that `GW(.|c=i)` is stationary for each `i`, hence GW itself is stationary, while `c` is preserved by the Markov chain and has probability `1/2`. Therefore the stationary chain is nonergodic even though the stationary measure is exactly GW.

I did not merely replay R02's recurrence. Moves #7, #15, and #19 expose a whole family in which the R02 example is the smallest member.

## 4. New theorem: a two-parameter family of exact counterexamples

### Theorem

For every pair of **distinct** integers `d,e >= 2`, define

\[
a_{d,e}:=
\frac{\frac12-2^{-e}}
{1-2^{-e}-2^{-d}}.
\]

Then `0<a_{d,e}<1`. Consider a Galton--Watson law supported on `{d,e}` with

\[
\mathbb P(D=d)=a_{d,e},\qquad
\mathbb P(D=e)=1-a_{d,e}.
\]

There exists an equivariant flow rule `Theta` for which **GW itself is stationary but the associated stationary Markov chain is nonergodic**. Consequently Lyons--Peres Question 17.18 has a negative answer. The R02 choice `(d,e)=(2,3)` gives exactly `a_{2,3}=3/5`.

### Proof, Step 1: degree breaks the symmetry without external marks (#15)

At a vertex of degree `d`, use the Boolean rule AND on its child colors. At a vertex of degree `e`, use OR. Because `d != e`, the uncolored rooted tree itself determines which connective is used; no extra mark or hidden randomness is introduced.

Start at depth `n` with i.i.d. Bernoulli(1/2) boundary colors, propagate them toward the root by these deterministic symmetric rules, and let `q_n(T)` be the conditional probability of root color 1 given the uncolored tree through the relevant depth.

The one-step mean map is

\[
F(p)=a_{d,e}p^d+(1-a_{d,e})\bigl(1-(1-p)^e\bigr).
\]

The definition of `a_{d,e}` is exactly the equation

\[
F(1/2)=1/2.
\]

The root expression is multilinear in the boundary probabilities. When one more generation of independent offspring degrees is revealed, each old boundary site's propagated mean averages back to `1/2`; hence

\[
\mathbb E[q_{n+1}\mid \mathcal F_n]=q_n.
\]

Thus `(q_n)` is a bounded martingale, so `q_n -> q_infty` almost surely and in `L^2` once the second moments are shown to converge.

### Step 2: exact second-moment contraction

Set

\[
r_n:=\mathbb E[q_n^2],\qquad r_0=\frac14.
\]

Use two independent boundary colorings of the same uncolored truncation. At a child, each replica has marginal `1/2`, `P(11)=r_n`, and therefore also `P(00)=r_n`.

For a degree-`d` AND vertex, both root replicas equal 1 with probability `r_n^d`. For a degree-`e` OR vertex, inclusion--exclusion gives

\[
1-2\cdot 2^{-e}+r_n^e.
\]

Therefore

\[
r_{n+1}=R(r_n),
\qquad
R(r)=a_{d,e}r^d+(1-a_{d,e})\bigl(1-2^{1-e}+r^e\bigr).
\]

By `F(1/2)=1/2`,

\[
R(1/2)=1/2.
\]

Moreover

\[
R'(1/2)
=a_{d,e}\frac{d}{2^{d-1}}
 +(1-a_{d,e})\frac{e}{2^{e-1}}
=:\lambda_{d,e}.
\]

For every integer `m>=2`, `m/2^{m-1} <= 1`, with equality only at `m=2`. Since `d` and `e` are distinct and both mixture weights are strictly positive,

\[
\lambda_{d,e}<1.
\]

On `[1/4,1/2]`, `R'` is increasing, hence `R'(r)<=lambda_{d,e}<1`. Thus `h(r):=R(r)-r` satisfies `h'(r)<0` and `h(1/2)=0`; consequently

\[
R(r)>r\quad(1/4\le r<1/2).
\]

Since `R` itself is increasing and `R(1/2)=1/2`, it also maps `[1/4,1/2]` into itself. Therefore

\[
r_n\uparrow 1/2.
\]

Because `q_n` is a bounded martingale,

\[
\mathbb E[q_\infty]=1/2,
\qquad
\mathbb E[q_\infty^2]=1/2,
\]

so

\[
\mathbb E[q_\infty(1-q_\infty)]=0.
\]

Hence `q_infty in {0,1}` almost surely. Define the tree color

\[
c(T):=q_\infty(T).
\]

Passing to the limit in the finite-depth recursion gives, on a hereditary GW-full set,

- degree `d`: `c(T)=AND(c(T_1),...,c(T_d))`;
- degree `e`: `c(T)=OR(c(T_1),...,c(T_e))`.

Also `GW(c=1)=1/2`.

### Step 3: the connective is conservative

Both AND and OR have the elementary conservative property that their output equals at least one input. Therefore every GW-good tree has at least one child with the same color as its parent.

Define the local transition rule on the good set by choosing uniformly among same-color children:

\[
K(T,T^x)=
\begin{cases}
1/N_c(T), & c(T^x)=c(T),\\
0, & c(T^x)\ne c(T),
\end{cases}
\]

where `N_c(T)` is the number of same-color children. Extend equivariantly and Borel-measurably off the full-measure good set, for example by uniform choice among all children whenever the same-color set is empty. Taking products of these local cylinder weights defines an equivariant flow rule and automatically gives the flow-rule consistency under passage to a positive-mass child.

### Step 4: exact stationarity (#19, make it an algorithm)

Let

\[
\mathrm{GW}_i:=\mathrm{GW}(\,\cdot\mid c=i),\qquad i=0,1.
\]

Condition on the root degree and the entire vector of child colors. Galton--Watson branching gives independent child subtrees; conditional on child `j` having color `i`, its law is exactly `GW_i`. If the parent has color `i`, conservativity guarantees at least one color-`i` child. Uniform selection among those indices depends only on the color vector, so the selected subtree has law `GW_i`. Hence

\[
\mathrm{GW}_i K=\mathrm{GW}_i,
\qquad i=0,1.
\]

Since each color has GW probability `1/2`,

\[
\mathrm{GW}K
=\tfrac12\mathrm{GW}_0K+\tfrac12\mathrm{GW}_1K
=\mathrm{GW}.
\]

Thus the stationary measure is not merely equivalent to GW; it is **GW itself**. But every transition preserves `c`, so `{c=1}` is a nontrivial invariant event of stationary probability `1/2`. The stationary chain is nonergodic. This proves the theorem. `QED`

## 5. Move #7: take the limit

The family is not a knife-edge accident. Holding `d=2` and taking `e=k -> infinity`,

\[
a_{2,k}=\frac{2^{k-1}-1}{3\cdot 2^{k-2}-1}\longrightarrow \frac23,
\]

while

\[
\lambda_{2,k}
=a_{2,k}+(1-a_{2,k})\frac{k}{2^{k-1}}
\longrightarrow \frac23.
\]

So the endogeny/interpretability margin `1-lambda` stays bounded away from zero. The source counterexample is therefore robust across an infinite family rather than depending on the isolated `3/5,2/5` arithmetic.

## 6. Exact independent checker

Only after the parametric proof was obtained did I build a small exact audit certificate. It was executed locally using `fractions.Fraction`, and the exact output was archived.

Artifacts:

- `artifacts/R01/20260918T0908Z_p0033_parametric_exact_audit.py`
- `artifacts/R01/20260918T0908Z_p0033_parametric_exact_audit.out`

The checker independently verifies for `(d,e)=(2,3)`:

\[
a=3/5,\quad 1-a=2/5,\quad F(1/2)=1/2,\quad
\lambda=9/10,\quad R(1/4)=11/32,\quad R(1/2)=1/2,
\]

and exact-rationally stress-checks every ordered pair `2<=d,e<=20`, `d!=e`. The archived terminal line is

`grid d,e in [2,20], d != e: ALL_EXACT_CHECKS_PASS`.

This is an independent finite-core audit, not a substitute for the written general proof.

## 7. Audit verdict for neighboring R02/P0033

**Audit ID:** `R01-AUDIT-R02-P0033-Q17.18-01`  
**Verdict:** `PASS_MATHEMATICAL_SOURCE_SCOPE`.

The R02 construction is the `(d,e)=(2,3)` specialization of the independently proved theorem above. I specifically checked the potential failure interfaces:

1. **Source scope:** Question 17.18 asks equivalence to GW, not merely absolute continuity. Here the stationary law is exactly GW.
2. **Zero weights:** the source's positive-weight hypothesis is a sufficient hypothesis in the preceding proposition, not part of Question 17.18; the open question is precisely whether that positivity can be dropped.
3. **Endogeneity:** the color is a measurable function of the uncolored tree, not an added boundary coin field; the martingale/second-moment argument proves this.
4. **Equivariance:** degree chooses the symmetric Boolean rule and uniform same-color selection is invariant under child permutations/rooted isomorphisms.
5. **Flow consistency:** product cylinder probabilities from the same local kernel on every descendant subtree give the required conditional consistency.
6. **Stationarity:** conditioning on the child-color vector does not size-bias the selected subtree beyond color; each eligible child's conditional law is `GW_i`, hence `GW_i K=GW_i`.
7. **Nonergodicity:** color is exactly transition-invariant and has stationary mass `1/2`.

I found no mathematical or source-scope defect. This audit does **not** claim publication novelty. The owner package still needs the policy-required P26 audit before fleet closure; the prior-art screen above is recorded negative evidence, not proof of priority.

## 8. Admission status after the research work

The active R01 target remains `PENDING_ADMISSION`. The newest strict coordinator delta still reports no candidate crossing READY, and fresh claims only shrink the free inventory. I did not recycle R01's prior successors `I0113`, `G0012`, `D0057`, or `D0030`; I did not take R09's `G0013`, R11's `I0054`, R12's `I0115`, or any other existing claim.

Because the fixed R01 successor metric does not exist until a lawful target is admitted, no successor stagnation count is invented.

Next nonrepeating Section-B moves for an actual admitted successor search: **#8 GO THE OTHER WAY AND DISCRETIZE, #16 COMPUTE EVERY SMALL CASE, #24 FIND THE EXTREMAL OBJECT**.

## 9. Model / scheduler control status

Still true this run: the exposed automation control surface offers task prompt/title, schedule/timing mode, and enabled-state controls, but **no binding model-family selector, no binding reasoning-effort selector, no authenticated completed-run model receipt, and no guarantee of hour-long execution**. GPT-6 / maximum therefore remains prompt text only here.

Actually enforcing GPT-6 / maximum would require an authorized product/backend/admin surface that exposes model and reasoning fields and records applied runtime telemetry. The historical P26 `You cannot modify this task` failure remains an authorization/context issue; the legitimate workaround is an owning/authorized context or platform support, not task duplication or permission bypass. No scheduler or permission change was attempted.

## 10. Structured ledger_delta

```yaml
ledger_delta:
  worker: R01
  repository: yspennstate/math-open-problems
  branch: master
  source:
    frozen: "Aldous-Fill Open Problem 3.44 / I0024"
    neighboring_audit: "Lyons-Peres Question 17.18 / P0033"
  metric:
    name: "R01 successor metric"
    before: UNMEASURED
    after: UNMEASURED
    frozen_predecessor_C: 1
  status: PENDING_ADMISSION
  unchanged_count: UNKNOWN
  tried_moves: [7, 15, 19]
  new_result:
    statement: "For every distinct d,e>=2, an explicit {d,e}-offspring GW law admits an equivariant same-color flow rule for which GW itself is stationary and the chain is nonergodic."
    audit_id: R01-AUDIT-R02-P0033-Q17.18-01
    audit_verdict: PASS_MATHEMATICAL_SOURCE_SCOPE
  evidence:
    - artifacts/R01/20260918T0908Z_p0033_parametric_exact_audit.py
    - artifacts/R01/20260918T0908Z_p0033_parametric_exact_audit.out
    - R02 owner package commit 33c13b0eda0ac882ba76c4eedfd9af42530d86c9
    - operations/task_health/runs/2026-09-18T085800Z/root_reconciliation_delta.md
  remaining_obligation: "Admit a fresh source-current CLOSABLE OUTSIDE unowned successor for R01; for P0033 fleet closure, obtain the policy-required P26 audit and preserve honest prior-art/novelty labeling."
  audit_ids:
    - R01-AUDIT-R02-P0033-Q17.18-01
```
