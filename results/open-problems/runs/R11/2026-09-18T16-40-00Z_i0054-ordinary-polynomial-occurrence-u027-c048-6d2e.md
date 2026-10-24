Model: GPT-5.6 Sol. Reasoning: UNVERIFIED runtime level; GPT-6 / maximum was requested in prompt text, but the exposed scheduler/runtime still has no binding model-family selector, no reasoning-effort selector, no guaranteed-duration control, and no authenticated completed-run routing telemetry, so GPT-6 / maximum is not verified or claimed. Metric movement: `47 -> 48` distinct nontrivial discrete model classes with complete author-side proofs of the frozen CTCS(infinity) limit. Actual section-B moves: **#3, #21, #26**.

# R11 / I0054 — U027 multiplicity-profile compiler and C048 ordinary-polynomial occurrence pointing

Date: 2026-09-18 UTC.  
Repository / branch: private `yspennstate/math-open-problems` / `master`.  
Track: R11, CLOSABLE OUTSIDE.  
Source: David J. Aldous and Svante Janson, *The Critical Beta-splitting Random Tree II: Overview and Open Problems*, arXiv:2303.02529v3, Open Problem 18.  
Source-level campaign status after this run: **PARTIAL, not CLOSED**.  
New author-side claims: `R11-I0054-U027 = PROVED_AUTHOR_SIDE`; `R11-I0054-C048 = PROVED_AUTHOR_SIDE under frozen equivalence`.

## 1. Continuity, source, ownership, and current-status checks

I continued from

`runs/R11/2026-09-18T15-40-00Z_i0054-pointed-squarefree-u026-c047-9c4f.md`

rather than restarting. That report proved U026/C047, moved the frozen metric `46 -> 47`, and prescribed the nonrepeating moves `#3/#21/#26`; those are the moves actually used here.

Before new research I reread or recovered the required control state:

- `probability_campaign_2026_09/INDEX.md` and `RANKING.md`;
- root `POSTED.md`, `RESULTS.md`, and `QUEUE.md`;
- `operations/claims/I0054.md`;
- `operations/NEW_METHODS_2026-09-16.md` and the controlling new-methods directive;
- the newest complete R11 report and the recent arithmetic/logarithmic-assembly reports needed to avoid duplicating C046/C047;
- exact intake/source hits under `probability_1000_intake_I_20260914/problems.jsonl` through the repository search surface;
- the newest neighboring P13 report, which is currently on the distinct C0021 iterated-majority problem and does not own I0054;
- current repository searches for `I0054`, the exact finite-law witness below, and `P26-AUDIT-R11-I0054`.

The canonical claim still names R11 and still says `PENDING_ADMISSION, not READY`. `POSTED.md` does not list Aldous--Janson Open Problem 18 as posted or settled. The previous planar self-avoiding-walk route remains retired and untouched. A repository search still does not recover a present-package P26 end-to-end PASS plus a second complete independent OTHER-track end-to-end PASS, so the source is not called closed here.

I rechecked the current primary source and current literature on 2026-09-18. The arXiv source is still v3, revised 18 April 2025. Its abstract says that CTCS(infinity) is formalized through exchangeable partitions. Printed page 58 states Open Problem 18 as the question whether superficially different discrete models can have the same CTCS(infinity) limit, and immediately asks whether the source's subordinator-approximation mechanism can arise in another discrete tree model. I therefore keep the strong frozen target used throughout this chain: convergence of the **complete partition-valued cadlag path** on each fixed restriction in Skorokhod `J_1`, followed by convergence in the summable projective finite-restriction path topology. A root split, tagged fragment, or fixed-time marginal does not count.

Fresh bounded searches on 2026-09-18 again found Chorbadzhiyska--Minchev--Savov, arXiv:2608.18320, which studies beta-splitting through homogeneous fragmentations and resolves a height problem, but no announced solution of exact Open Problem 18. For the finite-field input I searched `random polynomial finite field irreducible factor multiplicity`, `size-biased irreducible factor`, `pointed factor`, `Omega random polynomial`, and combinations with `CTCS` / `critical beta-splitting`. Arratia--Barbour--Tavare and later random-polynomial work make the polynomial/permutation analogy, geometric multiplicities, and factor-count asymptotics clear prior art. Those ingredients are not claimed as new. I did not locate the recursive occurrence-pointed CTCS hierarchy or U027 below. This is bounded negative evidence only, not a publication-novelty certificate.

## 2. Idea before code; the three methods

C047 removed fixed-factor-count conditioning but still imposed **squarefreeness**. The next target was to remove squarefreeness itself without losing the beta kernel.

The possible obstruction is repeated factors. For an ordinary polynomial

\[
 f=\prod_g g^{v_g(f)},
\]

small-degree factors can appear with multiplicity, and in characteristic two repeated linear factors are not rare enough to dismiss at finite `N`. The key question is whether these repetitions change the macroscopic factor-degree intensity that produced the beta kernel.

The actual section-B moves were:

- **#3 -- prove something stronger.** Instead of proving only the binary-field `a_r=1` construction, I prove a fixed-field **bounded multiplicity-profile compiler**: any bounded nonnegative profile `(a_r)` with `a_1=1` has the same CTCS beta tangent. Ordinary occurrence pointing is the special case `a_r=1`.
- **#21 -- ask who else has this shape.** Ordinary finite-field polynomial factorization is a logarithmic multiset structure. Classical work says individual irreducible multiplicities are approximately geometric and large factors resemble permutation cycles. This suggests that repetitions alter an analytic/end-point correction but should not change the first harmonic `1/m` term.
- **#26 -- hunt the sporadic case.** I attacked the repeated-factor boundary directly, especially repeated degree-one factors. They make the finite `N=4` law dramatically different from C047, but exact bounds show their contribution to every fixed visible beta rate is an endpoint term which vanishes as `N -> infinity`.

No checker was written until the counting identity and limit proof below were on the page.

## 3. Exact occurrence counting for ordinary monic polynomials

Fix a prime power `q`. Let `I_q(m)` be the number of monic irreducible degree-`m` polynomials over `F_q`. The classical exact formula is

\[
 I_q(m)=\frac1m\sum_{d\mid m}\mu(d)q^{m/d}.
\tag{3.1}
\]

Let `P_N` be the set of all `q^N` monic degree-`N` polynomials. For `f in P_N`, write `v_g(f)` for the multiplicity of irreducible `g`.

An **indexed occurrence** is a triple

\[
 (f,g,r),\qquad 1\le r\le v_g(f).
\]

For an irreducible `g` of degree `m`, an indexed `r`-th occurrence exists exactly when `g^r | f`. There are exactly `q^{N-rm}` monic degree-`N` multiples of `g^r`. Therefore the exact number of indexed degree-`m` occurrences is

\[
 \boxed{
 A_{N,m}^{(q)}
 =I_q(m)\sum_{r=1}^{\lfloor N/m\rfloor}q^{N-rm}.
 }
\tag{3.2}
\]

After division by `q^N`, define

\[
 \boxed{
 W_{N,m}^{(q)}
 =I_q(m)\sum_{r=1}^{\lfloor N/m\rfloor}q^{-rm}.
 }
\tag{3.3}
\]

The same quantity has the direct probabilistic interpretation

\[
 \sum_{m=1}^N W_{N,m}^{(q)}
 =\mathbb E\,\Omega(F_N),
\tag{3.4}
\]

where `F_N` is uniform on `P_N` and `Omega` counts irreducible factors with multiplicity.

From (3.1), `I_q(m) <= q^m/m`; hence

\[
 \boxed{
 W_{N,m}^{(q)}
 \le \frac{1}{m(1-q^{-m})}
 \le \frac{q}{(q-1)m}.
 }
\tag{3.5}
\]

Moreover

\[
 I_q(m)q^{-m}=\frac1m+O_q(q^{-m/2}),
\tag{3.6}
\]

so, uniformly for every fixed `epsilon>0` and
`epsilon N <= m <= (1-epsilon)N`, the repetitions `r>=2` are exponentially negligible and

\[
 \boxed{
 W_{N,m}^{(q)}=\frac1m(1+o(1)).
 }
\tag{3.7}
\]

The same calculation gives the useful total-intensity estimate

\[
 \boxed{
 \kappa_N^{(q)}:=\sum_{m=1}^N W_{N,m}^{(q)}
 =H_N+O_q(1)=O_q(\log N).
 }
\tag{3.8}
\]

Indeed, the `r=1` correction to `1/m` is absolutely summable by (3.6), and the total `r>=2` contribution is dominated by a convergent exponential series.

## 4. U027 -- bounded multiplicity profiles have the same beta tangent

The preceding argument is stable under much more than the literal occurrence count. Let `(a_r)_{r>=1}` be any bounded nonnegative sequence with

\[
 a_1=1,
 \qquad
 \sup_r a_r=M<\infty.
\]

Define the weighted degree intensity

\[
 W_{N,m}^{(q,a)}
 =I_q(m)\sum_{r\le N/m}a_rq^{-rm}.
\tag{4.1}
\]

Then

\[
 W_{N,m}^{(q,a)}\le \frac{Mq}{(q-1)m},
\tag{4.2}
\]

and on every macroscopic bulk window

\[
 W_{N,m}^{(q,a)}=\frac1m(1+o(1)),
\tag{4.3}
\]

because `a_1=1` fixes the first geometric term while every `r>=2` term is exponentially small there.

For a specified visible unordered binary partition with block sizes `i,j>=1`, `b=i+j`, conditional on a selected occurrence of degree `m`, allocate the `N` labels uniformly to `m` selected slots versus `N-m` complementary slots. The exact probability of the specified support is

\[
 s_{N,m}(i,j)
 =\frac{
 (m)_{\underline i}(N-m)_{\underline j}
 +(m)_{\underline j}(N-m)_{\underline i}
 }{(N)_{\underline{i+j}}}.
\tag{4.4}
\]

Define

\[
 q_N^{(q,a)}(i,j)
 =\sum_{m=1}^N W_{N,m}^{(q,a)}s_{N,m}(i,j).
\tag{4.5}
\]

### Bulk

If `x=m/N in [epsilon,1-epsilon]`, then for fixed `i,j`, uniformly,

\[
 W_{N,m}^{(q,a)}s_{N,m}(i,j)
 =\frac1N\left[
 x^{i-1}(1-x)^j+x^{j-1}(1-x)^i
 \right]+o(N^{-1}).
\tag{4.6}
\]

Thus the bulk is a Riemann sum.

### Small selected occurrences

For `m <= epsilon N`, (4.2) and the falling-factorial bound give

\[
 W_{N,m}^{(q,a)}s_{N,m}(i,j)
 \le \frac{C_{i,j,q,M}}{m}
 \left[(m/N)^i+(m/N)^j\right],
\]

and therefore

\[
 \sum_{m\le\epsilon N}
 W_{N,m}^{(q,a)}s_{N,m}(i,j)
 =O_{i,j,q,M}(\epsilon^i+\epsilon^j).
\tag{4.7}
\]

### Small complement

If `n=N-m <= epsilon N`, then `m >= N/2`, so `W_{N,m}^{(q,a)}=O(1/N)`. Hence

\[
 \sum_{N-m\le\epsilon N}
 W_{N,m}^{(q,a)}s_{N,m}(i,j)
 =O_{i,j,q,M}(\epsilon^{i+1}+\epsilon^{j+1}).
\tag{4.8}
\]

Letting `N -> infinity` and then `epsilon ->0`, (4.6)--(4.8) yield

\[
\begin{aligned}
 q_N^{(q,a)}(i,j)
 &\longrightarrow
 \int_0^1\left[
 x^{i-1}(1-x)^j+x^{j-1}(1-x)^i
 \right]dx\\
 &=B(i,j+1)+B(j,i+1)\\
 &=\boxed{B(i,j)
 =\frac{(i-1)!(j-1)!}{(i+j-1)!}}.
\end{aligned}
\tag{4.9}
\]

This proves the stronger structural statement

\[
 \boxed{\texttt{R11-I0054-U027 = PROVED\_AUTHOR\_SIDE}.}
\]

C048 below is the literal combinatorial case `q=2` and `a_r=1` for every `r`.

## 5. C048 -- ordinary binary-polynomial occurrence-pointed hierarchy

For every `N>=2`, let

\[
 \mathcal J_N
 =\{(f,g,r):
 f\in\mathbb F_2[x]\text{ monic},\ \deg f=N,
 \ g\text{ monic irreducible},\ 1\le r\le v_g(f)\}.
\tag{5.1}
\]

Thus

\[
 |\mathcal J_N|
 =2^N\kappa_N,
 \qquad
 \kappa_N=\sum_{m=1}^N W_{N,m}^{(2)}.
\tag{5.2}
\]

A **C048 proposal** samples an indexed occurrence `(f,g,r)` uniformly from `J_N`. If `m=deg g`, it then chooses a uniform `m`-subset `A` of `[N]`; the proposal is the binary partition `{A,A^c}`.

Set

\[
 \delta_N=\min\{N^{-2},(2\kappa_N)^{-1}\},
 \qquad
 a_N=\delta_N\kappa_N\le\frac12.
\tag{5.3}
\]

Start from the one-block partition of `[N]`. In each raw step, independently for every current nonsingleton block `B`:

1. attempt with probability `a_N`;
2. on an attempt, draw a fresh uniform incidence from `J_N` and its fresh uniform subset `A`;
3. replace `B` by the nonempty intersections `B cap A` and `B cap A^c`;
4. an empty-side proposal is invisible;
5. children are first eligible on the next raw step.

One raw step has physical duration `delta_N`.

This is a finite discrete model built from **all** monic degree-`N` binary polynomials. There is no squarefree condition and no fixed factor-count condition.

## 6. Exact hidden-label lumping and complete path convergence

Fix a visible restriction `[k]`. Every future proposal is fresh and sampled from the same global-`N` law, independently of the current carrier's hidden size and history. Therefore an invisible split involving only hidden labels cannot alter the future law seen by a visible carrier. Hidden labels lump out exactly, and the restriction to `[k]` is itself Markov.

An attempted block is sampled at physical intensity `a_N/delta_N=kappa_N`. Conditional on an attempt, a degree-`m` occurrence is chosen with probability

\[
 \frac{A_{N,m}}{|\mathcal J_N|}
 =\frac{W_{N,m}}{\kappa_N}.
\]

Therefore the exact first-order rate of a specified visible `i|j` transition is precisely

\[
 \sum_m W_{N,m}s_{N,m}(i,j)=q_N(i,j).
\tag{6.1}
\]

By U027,

\[
 Q_N^{(k)}\longrightarrow Q_{\rm CTCS}^{(k)}
\tag{6.2}
\]

entrywise on every fixed finite partition state space. Every one-block effective transition is binary at every finite `N`.

The only raw-step discrepancy from the continuous generator comes from two or more visible blocks attempting in one step. For fixed `k`,

\[
 P_N^{(k)}
 =I+\delta_NQ_N^{(k)}+R_N^{(k)},
 \qquad
 \|R_N^{(k)}\|_{\rm row,1}
 =O_k(\delta_N^2\kappa_N^2).
\tag{6.3}
\]

Since `kappa_N=O(log N)`, eventually `delta_N=N^{-2}` and

\[
 \boxed{
 \delta_N\kappa_N^2
 =O\!\left(\frac{(\log N)^2}{N^2}\right)\to0.
 }
\tag{6.4}
\]

Finite-state Euler/uniformization coupling now yields, for every fixed `k`,

\[
 \boxed{
 \Pi_{N,048}^{[k]}
 \Longrightarrow
 \Pi_{\rm CTCS}^{[k]}
 \quad\text{in Skorokhod }J_1.
 }
\tag{6.5}
\]

The finite model reaches singletons almost surely. If two labels are still in one carrier, their separation probability per raw step is `delta_N q_N(1,1)>0`; fresh proposals repeat independently until they separate. Monotonicity of the finite partition lattice then gives absorption.

Using the frozen summable projective metric

\[
 d_{\rm proj}(\omega,\eta)
 =\sum_{k\ge2}2^{-k}
 \bigl(1\wedge d_{J_1,k}(\omega^{[k]},\eta^{[k]})\bigr),
\tag{6.6}
\]

fixed-restriction convergence plus the deterministic tail of the sum gives

\[
 \boxed{
 \Pi_{N,048}
 \Longrightarrow
 \Pi_{\operatorname{CTCS}(\infty)}.
 }
\tag{6.7}
\]

This is the complete partition-valued genealogy limit required by the frozen R11 target, not a marginal statement.

## 7. #26: repeated factors are a real finite perturbation, not a relabeling

Repeated factors have not merely produced the same finite model with a new description. Exact enumeration at `N=4` gives

\[
 \boxed{
 \kappa_4=\frac{21}{8},\qquad
 q_4(1,1)=\frac{61}{48},\qquad
 q_4(2,2)=\frac5{48},\qquad
 q_4(1,3)=\frac{17}{32}.
 }
\tag{7.1}
\]

Hence the time-rescaling-invariant root-rate pair is

\[
 \boxed{
 \left(
 \frac{q_4(2,2)}{q_4(1,1)},
 \frac{q_4(1,3)}{q_4(1,1)}
 \right)
 =\left(\frac5{61},\frac{51}{122}\right).
 }
\tag{7.2}
\]

The immediate squarefree predecessor C047 has instead

\[
 q_4^{\rm sf}(1,1)=\frac{17}{24},
 \qquad
 q_4^{\rm sf}(2,2)=\frac1{24},
 \qquad
 \frac{q_4^{\rm sf}(2,2)}{q_4^{\rm sf}(1,1)}=\frac1{17}.
\tag{7.3}
\]

Thus removing squarefreeness changes the finite root law in a way no deterministic leaf relabeling or positive global time/branch rescaling can repair. A targeted repository search for the exact ordinary witness `(61/48,5/48,17/32)` found no earlier retained R11 class with that witness. Under the frozen equivalence convention, C048 is therefore counted as a distinct class. As throughout this campaign, this is an author-side classification subject to independent audit rather than a claim of publication novelty.

## 8. Exact-arithmetic checker, executed after the proof route closed

Only after the counting and convergence proof was established did I write and execute

`artifacts/R11/2026-09-18T16-40-00Z_c048_ordinary_polynomial_occurrence_checker.py`

created at commit `1bc9ddd5029a7081e8994aaac7a3ac6fe80b67d2`.

Its archived stdout is

`artifacts/R11/2026-09-18T16-40-00Z_c048_ordinary_polynomial_occurrence_checker.out`

created at commit `45da137e8068262005d3f6549e2930151ce84b90`.

The checker executes **6,653 exact assertions** and ends

`ALL_EXACT_CHECKS_PASS`.

It independently:

- brute-factors every monic binary polynomial through degree 9 and verifies the exact indexed-occurrence formula (3.2);
- independently enumerates subsets and verifies the hypergeometric support law (4.4);
- verifies `W_{N,m} <= 2/m` and `kappa_N <= 2H_N` throughout the tested range;
- verifies the exact ordinary `N=4` witness (7.1)--(7.2);
- independently brute-recovers C047's squarefree `N=4` comparator;
- checks exact dyadic finite-`N` beta-rate diagnostics through `N=128`.

This is a self-check, not an independent audit.

## 9. Prior art and what is / is not claimed

The random-polynomial mechanism itself is classical. Arratia--Barbour--Tavare studied uniform monic polynomials over finite fields, including approximately geometric irreducible multiplicities and the similarity of large irreducible factors to permutation cycles. More recent work studies factor counts with multiplicity and universality of low-degree factors. I therefore make **no novelty claim** for:

- formula (3.1);
- geometric/repeated irreducible multiplicities;
- the logarithmic `Omega(F_N) ~ log N` scale;
- the broad polynomial/permutation analogy.

The author-side claim here is narrower and specific: the indexed-occurrence intensity (3.2), coupled to the uniform label-box split, gives the beta kernel (4.9) and therefore the complete recursive CTCS(infinity) path limit (6.7); U027 also isolates the bounded multiplicity-profile universality mechanism. The bounded search did not locate that CTCS compiler/application, but external novelty remains **UNVERIFIED**.

## 10. Status, metric, and next route

The stable author-side state after this run is

\[
 \boxed{\texttt{R11-I0054-U027 = PROVED\_AUTHOR\_SIDE}},
 \qquad
 \boxed{\texttt{R11-I0054-C048 = PROVED\_AUTHOR\_SIDE under frozen equivalence}},
 \qquad
 \boxed{47\to48}.
\]

I am **not** calling Aldous--Janson Open Problem 18 closed. The canonical ownership file remains `PENDING_ADMISSION, not READY`; the required present-package P26 end-to-end PASS plus a second independent OTHER-track end-to-end PASS are still absent from the repository search; and external novelty has not been certified. Source-level campaign status therefore remains **PARTIAL**.

The model-control limitation is unchanged. The exposed scheduler interface provides prompt/title, schedule, enabled state, and timing mode, but no model-family selector, reasoning-effort selector, guaranteed-duration control, or authenticated per-run routing telemetry. Making GPT-6/maximum binding requires those controls and runtime attestation to be exposed by the authorized product/workspace/platform. A task returning `You cannot modify this task` must be handled from its authorized owning context or by platform support; cloning/bypassing it is not the workaround. No scheduler modification was attempted.

The next nonrepeating methods recorded are **#11, #22, #28**. The strongest next target is a more natural de-biasing problem: sample the ordinary monic polynomial **uniformly first**, then choose one of its `Omega(f)` irreducible occurrences uniformly, instead of sampling the polynomial through the occurrence-Palm bias used in C048. The selected degree law becomes

\[
 \mathbb E\left[
 \frac1{\Omega(F_N)}
 \sum_{g,r\le v_g(F_N)}
 \mathbf 1\{\deg g=m\}
 \right],
\]

which is no longer given by the one-line divisibility count. The next run should dualize this Palm transform (#11), read the nearest random-factor failures/size-biased results (#22), and use typical concentration of `Omega(F_N)` (#28) either to prove the same beta kernel or exhibit the exact bias obstruction.

```yaml
ledger_delta:
  track: R11
  lane: CLOSABLE_OUTSIDE
  intake: I0054
  source: "Aldous--Janson arXiv:2303.02529v3, Open Problem 18"
  source_status: PARTIAL
  canonical_claim_status: PENDING_ADMISSION
  metric_name: "number of distinct nontrivial discrete model classes with complete author-side required-limit proofs under frozen equivalence"
  value_before: 47
  value_after: 48
  movement: 1
  new_theorem: R11-I0054-U027
  new_model: R11-I0054-C048
  model_description: "ordinary monic binary-polynomial indexed-occurrence pointing, uniform factor-slot label subset, recursive raw-step fragmentation"
  topology: "Skorokhod J1 on every fixed restriction, then summable projective finite-restriction path topology"
  methods_used: [3, 21, 26]
  next_methods: [11, 22, 28]
  finite_checker: artifacts/R11/2026-09-18T16-40-00Z_c048_ordinary_polynomial_occurrence_checker.py
  finite_checker_output: artifacts/R11/2026-09-18T16-40-00Z_c048_ordinary_polynomial_occurrence_checker.out
  checker_assertions: 6653
  checker_result: ALL_EXACT_CHECKS_PASS
  audit_state: "self-check only; required current-package P26 + second OTHER-track end-to-end audits absent"
  stagnation_before: 0
  stagnation_after: 0
```
