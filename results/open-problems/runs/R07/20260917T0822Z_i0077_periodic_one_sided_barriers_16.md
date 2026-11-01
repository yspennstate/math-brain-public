Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. METRIC MOVEMENT: 15 -> 16 genuinely distinct nonparabolic shape families; Section-B moves tried: #3 PROVE SOMETHING STRONGER, #18 SAY IT IN ANOTHER LANGUAGE, #27 SWAP THE QUANTIFIERS.**

Problem/source: Krzysztof Burdzy and Michael Scheutzow, *Forward Brownian Motion* (PTRF 160 (2014), 95–126; arXiv:1302.6958), Problem 7.8: “Can one generalize Theorem 4.3 from parabolas to other space-time shapes?” Intake I0077. **Overall status: PARTIAL; the open-ended source request is not claimed closed.**

# R07 CLOSABLE OUTSIDE — run 16: log-periodic one-sided parabolic barriers

Run date: 2026-09-17 UTC.  
Repository / branch: `yspennstate/math-open-problems` / `master`.  
Delivery: private GitHub only. No email/Gmail, Drive, public posting, purchases, permission changes, workflow execution, or scheduler changes.

## 1. Continuity, ownership, and frozen metric

The frozen R07 metric remains

> the number of genuinely distinct nonparabolic space-time shape families for which R07 has a complete source-appropriate theorem, modulo Brownian rescaling/reflection/translation and mere parameter changes inside one structural family.

The preceding authoritative own report is

`runs/R07/20260917T0724Z_i0077_gated_disconnected_fans_15.md`,

which moved the metric `14 -> 15` for periodically gated disconnected parabolic fans and used methods `#6,#12,#20`. I do not repeat that triple. This run adds exactly one family: **log-periodically moving one-sided upper barriers**, whose normalized cross-section is an unbounded half-line at every logarithmic phase.

The metric moves

\[
\boxed{15\longrightarrow16}.
\]

`unchanged_count = 0`.

The old R07 KPZ/FPP route remains retired by its immutable handoff; no historical R07 file was modified or deleted.

## 2. Required repository/source reread

Before new mathematics I recovered the current state from:

- `probability_campaign_2026_09/INDEX.md` and `RANKING.md`;
- root `POSTED.md`, `RESULTS.md`, and `QUEUE.md`;
- `operations/NEW_METHODS_2026-09-16.md`;
- canonical reservation `operations/claims/I0077.md`;
- the searchable R07/I0077 chain through run 15;
- the newest visible R15 reports: R15's distinct Burdzy–Scheutzow Problem 7.2 / I0076 already reached its six-run handoff and R15 has rotated to another source;
- C29's earlier I0077 duplicate-exclusion report, which correctly refused to compete with R07;
- targeted intake/attempt searches for `I0077`, `1302.6958`, `Problem 7.8`, and the exact source wording.

The canonical claim still names R07 as exclusive provisional owner and still says `PENDING_ADMISSION, not READY`. The latest owner instruction nevertheless assigns this exact target to R07. I do not rewrite the shared claim or fabricate READY status. `INDEX.md`/`RANKING.md` settle Burdzy–Scheutzow Problem 7.5, not 7.8; `POSTED.md` has no Problem-7.8 exclusion; `QUEUE.md` lists I0077 distinctly. The root `RESULTS.md` R07/FPP row is stale by its own warning and is not used as the current mathematical baseline.

The large `probability_1000_intake_*/problems.jsonl` mirrors cannot be rendered wholesale through the exposed connector without truncation. This run's intake reread is therefore honestly **PARTIAL / targeted**, not described as a byte-for-byte whole-ledger read.

## 3. Primary source recovered exactly

I reread the published PDF, including Definitions 2.1–2.2, Remarks 4.1–4.2, Theorem 4.3 and its proof, and the open-problem page.

Definition 2.1 fixes the FBM witness property: there are random times `S_n -> -infinity` such that for each witness

\[
B^{(n)}_t=X_{S_n+t}-X_{S_n},\qquad t\ge0,
\]

is standard Brownian motion. The paper assumes the processes start at `0` at time `0`. Definition 2.2 gives the decomposable concatenation construction.

For `-infinity <= c_1 < c_2 <= infinity`, Remark 4.1 uses the OU generator

\[
\mathcal A=\frac12\left(\frac{d^2}{dx^2}-x\frac d{dx}\right)
\]

and writes `lambda_0(c_1,c_2)` for minus its largest Dirichlet eigenvalue on the interval. `lambda_0` is continuous and decreases as the right endpoint moves right. Remark 4.2 records the exact critical examples

\[
\boxed{\lambda_0(-\infty,-1)=\lambda_0(-1,1)=\lambda_0(1,\infty)=1.}
\tag{3.1}
\]

Theorem 4.3 says:

1. if `lambda_0(c_1,c_2)>=1`, every FBM has the universal far-past normalized obstruction;
2. if `lambda_0(c_1,c_2)<=1`, a decomposable FBM has the corresponding asymptotic normalized inclusion;
3. if `c_1<=0<=c_2` and `lambda_0(c_1,c_2)<1`, a decomposable FBM is pointwise confined to the exact parabolic region for all `t<=0`.

The source proof explicitly treats infinite endpoints by approximation. Problem 7.8 is exactly the single sentence asking for generalization of Theorem 4.3 beyond parabolas. The following forward-Lévy sentence is separately Problem 7.9 and is not part of I0077.

## 4. Fresh literature/current-status check — 2026-09-17

Fresh bounded web searches included:

- exact title + `Problem 7.8` + `other space-time shapes`;
- exact Problem-7.8 wording plus Burdzy/Scheutzow and later-paper/citation variants;
- `Ornstein-Uhlenbeck periodic boundary first passage asymptotic`;
- `Brownian log-periodic square-root boundary first passage`;
- `one-sided Ornstein-Uhlenbeck absorbing boundary principal eigenvalue`.

Relevant prior art found:

- Shunsuke Sato, *Evaluation of the first-passage time probability to a square root boundary for the Wiener process*, J. Appl. Prob. 14 (1977), 850–856: square-root Wiener boundary / constant OU boundary;
- L. Sacerdote, *Asymptotic behaviour of Ornstein–Uhlenbeck first-passage-time density through periodic boundaries*, Applied Stochastic Models and Data Analysis 6 (1990), 53–57;
- V. Giorno, A. G. Nobile, L. M. Ricciardi, *On the asymptotic behaviour of first-passage-time densities for one-dimensional diffusion processes and varying boundaries*, Adv. Appl. Prob. 22 (1990), 883–914: includes asymptotically periodic boundaries;
- modern 2025–2026 periodic-parabolic principal-eigenvalue papers and a 2026 paper on OU-bridge exit asymptotics, none of which is an FBM Problem-7.8 resolution.

So the periodic one-sided OU first-passage mechanism is classical prior art and must be described as such. I found no later paper in this bounded dated search explicitly resolving Burdzy–Scheutzow Problem 7.8 or stating the FBM theorem below. This is **negative search evidence only; publication novelty remains UNVERIFIED**.

## 5. New shape family

Let `b:R->R` be bounded, continuous and periodic of period `P>0`. Define the one-sided log-periodic region

\[
\mathcal H_b
=
\left\{(-u,x):u>0,\ x\le \sqrt u\,b(\log u)\right\}\cup\{(0,0)\}.
\tag{5.1}
\]

If `b` is nonconstant this is not a parabolic region. At every logarithmic phase its normalized cross-section is the unbounded connected half-line

\[
(-\infty,b(r)].
\]

This unbounded-cross-section feature is the structural invariant distinguishing the family from the first fifteen R07 families.

For `A>0`, abbreviate

\[
\lambda_A:=\lambda_0(-\infty,-A).
\tag{5.2}
\]

Suppose there are `eta>0` and a phase interval `J subset [0,P)` of length `tau>0` such that

\[
\boxed{b(r)+2\eta\le -A\quad\text{whenever }r\bmod P\in J.}
\tag{5.3}
\]

## 6. I0077-R07-T17 — one-sided periodic-barrier theorem

**Status of theorem: PROVED on the page below. Overall source status remains PARTIAL.**

### (A) Universal obstruction from repeated one-sided gates

If (5.3) holds and

\[
\boxed{\kappa:=\frac\tau P\lambda_A>1,}
\tag{6.1}
\]

then every FBM `X` satisfies

\[
\boxed{
\mathbb P\left(
\exists R<\infty:\ X_{-u}\le\sqrt u\,b(\log u)\ \forall u\ge R
\right)=0.
}
\tag{6.2}
\]

### (B) Eventual existence above the one-sided critical level

If

\[
\boxed{\beta:=\inf_{r\in\mathbb R}b(r)>-1,}
\tag{6.3}
\]

then there exists a decomposable FBM `X` such that almost surely

\[
\boxed{
X_{-u}\le\sqrt u\,b(\log u)
\quad\text{for all sufficiently large }u.
}
\tag{6.4}
\]

### (C) One process works pointwise for every nonnegative barrier

There exists a single decomposable FBM `X^+` such that

\[
\boxed{X^+_t\le0\quad\forall t\le0\quad\text{a.s.}}
\tag{6.5}
\]

Consequently the same `X^+` satisfies

\[
X^+_{-u}\le\sqrt u\,b(\log u)
\quad\forall u\ge0
\tag{6.6}
\]

simultaneously for **every** bounded periodic profile `b` with `b(r)>=0` for all `r`.

The mixed regime `inf b<=-1` in which the periodic survival exponent is at most one is not classified here; no false sharp converse is claimed.

## 7. Proof of T17(A): method #18 — say it in the OU language

Let `B` be standard Brownian motion. For a deterministic integer terminal `n`, reversed increments

\[
Z^{(n)}_u=B_{n-u}-B_n,\qquad0\le u\le n,
\tag{7.1}
\]

have standard Brownian law as a process of `u`. The Lamperti transform

\[
Y_r=e^{-r/2}Z^{(n)}_{e^r}
\tag{7.2}
\]

is stationary OU with invariant standard Gaussian measure `gamma`.

During every complete gate interval, survival below the twice-padded moving barrier implies

\[
Y_r\le -A
\]

throughout a logarithmic interval of length `tau`. The killed OU semigroup on `(-infinity,-A)` is self-adjoint in `L^2(gamma)` and has operator norm

\[
\|K_t\|_{2\to2}=e^{-\lambda_A t}.
\tag{7.3}
\]

Between gates we discard all constraints, costing operator norm at most one. If `[r,s]` contains `N(r,s)` complete gates, then

\[
\mathbb P\left(
Z^{(n)}_u/\sqrt u\le b(\log u)+2\eta\ \forall u\in[e^r,e^s]
\right)
\le e^{-\lambda_A\tau N(r,s)}.
\tag{7.4}
\]

Periodicity gives

\[
N(r,s)\ge\frac{s-r}{P}-2,
\tag{7.5}
\]

hence for some finite `C`,

\[
\boxed{
\mathbb P(\text{twice-padded survival on }[R,T])
\le C(T/R)^{-\kappa}.
}
\tag{7.6}
\]

This is the exact one-sided analogue of the source's summable terminal-time estimate.

## 8. Proof of T17(A): arbitrary real Brownian terminal times

For a real terminal `t`, call it once-padded good above scale `R_0` when

\[
B_{t-u}-B_t\le\sqrt u\,[b(\log u)+\eta]
\quad\forall u\in[R_0,t].
\tag{8.1}
\]

For `n>=3`, set

\[
M_n=\max_{0\le k\le n}\operatorname{osc}_{[k,k+2]}B.
\tag{8.2}
\]

Reflection plus the Gaussian Chernoff bound gives, for all sufficiently large `n`,

\[
\mathbb P(M_n>8\sqrt{\log n})\le8n^{-3}.
\tag{8.3}
\]

Set

\[
R_n=\left\lceil256\eta^{-2}\log n\right\rceil.
\tag{8.4}
\]

If `t in [n,n+1]` and `u in [R_n,n]`, then

\[
|(B_{t-u}-B_t)-(B_{n-u}-B_n)|\le2M_n.
\tag{8.5}
\]

On `M_n<=8 sqrt(log n)`, the right side divided by `sqrt(u)` is at most `eta`. Therefore a once-padded good real terminal in `[n,n+1]` forces the integer terminal `n` to satisfy the twice-padded condition on `[R_n,n]`. By (7.6),

\[
\mathbb P\{\exists\text{ once-padded good }t\in[n,n+1]\}
\le8n^{-3}+C(n/R_n)^{-\kappa}.
\tag{8.6}
\]

Since `kappa>1` and `R_n=O(log n)`, the right side is summable. Borel–Cantelli implies that the set of good real Brownian terminal times is almost surely bounded.

Now suppose (6.2) fails with confinement event probability `q>0`. Choose deterministic `R_0` and then `A_0` so large that a standard Brownian motion has probability `<q/4` of possessing a once-padded good terminal `t>=A_0`. Let `S_j` be the FBM witness sequence. Since `S_j->-infinity` a.s., choose one **deterministic index** `j` with

\[
\mathbb P(-S_j<A_0)<q/4.
\tag{8.7}
\]

The single process

\[
B^{(j)}_r=X_{S_j+r}-X_{S_j}
\]

is standard Brownian motion. At terminal `t=-S_j`, its reversed increments are exactly

\[
B^{(j)}_{t-u}-B^{(j)}_t=X_{-u}-X_0=X_{-u},
\tag{8.8}
\]

because the source convention is `X_0=0`. Hence on confinement and `-S_j>=A_0`, the Brownian path `B^(j)` has a good terminal at least `A_0`. This event has probability at least `3q/4`, contradicting the `<q/4` Brownian bound. No independence between `S_j` and the Brownian witness is assumed.

This proves T17(A).

## 9. Proof of T17(B): source critical half-line is exactly `-1`

Let `beta=inf b>-1`. Choose

\[
-1<c<\beta.
\]

By (3.1) and strict domain monotonicity,

\[
\lambda_0(-\infty,c)<\lambda_0(-\infty,-1)=1.
\tag{9.1}
\]

Theorem 4.3(ii), with `c_1=-infinity` and `c_2=c`, gives a decomposable FBM `X` with

\[
\limsup_{t\to-\infty}\frac{X_t}{\sqrt{|t|}}\le c
\quad\text{a.s.}
\tag{9.2}
\]

Pick `d` with `c<d<beta`. Almost surely, for all sufficiently large `u`,

\[
\frac{X_{-u}}{\sqrt u}\le d<\beta\le b(\log u),
\]

which proves (6.4).

## 10. Proof of T17(C): method #27 — swap the quantifiers

Again by (3.1) and strict monotonicity,

\[
\lambda_0(-\infty,0)<1.
\tag{10.1}
\]

Theorem 4.3(iii), with `c_1=-infinity,c_2=0`, therefore supplies one decomposable FBM `X^+` satisfying

\[
X^+_t\le0\qquad\forall t\le0
\]

almost surely. Fix this one process. For **every** bounded periodic `b>=0`,

\[
0\le\sqrt u\,b(\log u),
\]

so the same `X^+` lies pointwise in every corresponding `H_b`. This is stronger than choosing a new process for each profile.

## 11. Explicit canonical barrier and exact certificate

This is method #3: prove the general theorem first, then instantiate a nontrivial shape whose static outer envelope has the opposite verdict.

Take period `P=1` and write `theta={r}` for fractional logarithmic phase. Define the continuous periodic profile

\[
b(\theta)=
\begin{cases}
-5,&0\le\theta\le3/5,\\
-5+70(\theta-3/5),&3/5\le\theta\le7/10,\\
2,&7/10\le\theta\le9/10,\\
2-70(\theta-9/10),&9/10\le\theta\le1.
\end{cases}
\tag{11.1}
\]

Thus the normalized region is the half-line `(-infinity,b(log u)]`: for three fifths of every log-period its upper wall is `-5`, while for a genuine plateau it opens all the way to `+2`.

Take

\[
\eta=\frac14,\qquad A=4,\qquad\tau=\frac35.
\]

On the gate plateau,

\[
b+2\eta=-5+\frac12=-\frac92\le-4.
\tag{11.2}
\]

For the OU Dirichlet eigenvalue on `(-infinity,-A)`, the standard ground-state substitution

\[
g(x)=f(x)e^{-x^2/4}
\]

gives

\[
\frac12\int |f'|^2e^{-x^2/2}dx
=
\int\left[
\frac12|g'|^2+\left(\frac{x^2}{8}-\frac14\right)g^2
\right]dx.
\tag{11.3}
\]

Therefore

\[
\lambda_A\ge\frac{A^2}{8}-\frac14.
\tag{11.4}
\]

At `A=4`,

\[
\lambda_4\ge\frac74,
\qquad
\kappa\ge\frac35\frac74=\boxed{\frac{21}{20}>1}.
\tag{11.5}
\]

Hence T17(A) says **no FBM can even be eventually confined** to this log-periodic one-sided shape.

Yet its static outer envelope is simply

\[
x\le2\sqrt u.
\]

Since `2>-1`, strict monotonicity from `lambda_0(-infinity,-1)=1` gives

\[
\lambda_0(-\infty,2)<1,
\]

and source Theorem 4.3(iii) supplies a decomposable FBM confined pointwise to that outer half-parabola. Thus the periodic one-sided gates, not the outer parabolic envelope, reverse the verdict.

The finite arithmetic in (11.2) and (11.5) was checked exactly and executed:

- checker: `artifacts/R07/20260917T0822Z_halfline_gate_check.py`, creation commit `00b4ee67777cec354a10d18d3a1d8f5209a3d180`;
- archived output: `artifacts/R07/20260917T0822Z_halfline_gate_check.out`, creation commit `a963175cc89db6e294adb47242fea12a7d298786`;
- output begins `PASS` and records `lambda_lower=7/4`, `kappa_lower=21/20`, `padded_gate_boundary=-9/2`.

This is a **self-check of the finite arithmetic**, not an independent theorem audit.

## 12. Why this is a genuinely new metric family

Runs 1–15 all used bounded normalized cross-sections: intervals, bounded unions, Cantor sets, or bounded moving/gated versions. The new family has an **unbounded one-sided half-line cross-section at every phase**. Brownian rescaling shifts logarithmic phase and multiplies the physical coordinates, while reflection exchanges upper and lower half-lines; none of the frozen trivial equivalences changes boundedness of the normalized spatial slice. Therefore this family cannot be converted into any of the preceding fifteen by a rescaling, reflection, translation, or parameter change.

The profile parameter itself is not counted: all periodic upper-half-line profiles satisfying T17 are one structural family. Lower one-sided barriers obtained by reflection are not counted separately.

Therefore the fixed metric legitimately moves

\[
\boxed{15\to16}.
\]

## 13. The three Section-B methods and what happened

### #3 PROVE SOMETHING STRONGER — succeeded

Instead of proving only the explicit `-5/+2` example, I proved T17 for the whole periodic one-sided class: a spectral gate obstruction, an eventual-existence clause above the exact source critical level `-1`, and a pointwise universal process for all nonnegative profiles.

### #18 SAY IT IN ANOTHER LANGUAGE — succeeded

The moving square-root upper boundary becomes a one-sided periodic absorbing boundary for stationary OU under Lamperti. In that language the relevant quantity is the one-period survival contraction, and the simple gate criterion is a rigorous lower bound on its decay exponent. This also exposed the correct historical literature: periodic OU first passage was already studied in 1990, so that spectral/FPT mechanism is not claimed as new.

### #27 SWAP THE QUANTIFIERS — succeeded

Source Theorem 4.3(iii) at `(-infinity,0)` yields

\[
\exists X^+\ \forall b\ge0
\]

rather than merely `for every b there exists X_b`: one single decomposable FBM works pointwise for the entire nonnegative periodic one-sided family.

## 14. Status and closure discipline

Tracked metric:

\[
\boxed{15\to16},\qquad\text{unchanged_count}=0.
\]

Overall Problem 7.8 status remains **PARTIAL**, not PROVED/closed. T17 has a complete written argument and its finite arithmetic self-check, but it has **no P26 end-to-end audit and no second independent OTHER-track audit**. No `paper_*` package was created. A bounded literature search finding no explicit resolution is not a novelty certificate.

## 15. Model/reasoning and scheduler-control status

The actual runtime self-identifies as **GPT-5.6 Sol**. The exposed scheduler/runtime surface does not provide authenticated reasoning-effort telemetry, so reasoning is **UNVERIFIED**; I do not claim GPT-6 maximum.

The scheduler control schema currently exposed to this worker still offers task title/prompt, schedule, enabled state, and timing mode, but **no model-family selector and no reasoning-effort selector**. Therefore the requested `GPT-6 / maximum` setting remains prompt text only. Enforcing it would require the product/API to expose those selectors plus authenticated run metadata, or an authorized owner/admin product surface that has them.

The repository's current `RESULTS.md` records that the historical P26 `You cannot modify this task` failure was context/ownership-specific: a later authorized P/C context successfully installed the full P26 update, while other contexts still denied modifications. The legitimate workaround for any currently denied task is the owning authorized context or platform support, not a worker-level permission bypass or duplicate schedule. Per the owner instruction, **no scheduler modification was attempted in this run**.

## 16. Next mathematical direction

The high-value remaining one-sided question is the mixed regime where the barrier crosses the static critical level `-1`. The natural exact invariant is the principal Floquet/survival exponent of the one-period killed-OU evolution. A future run should ask whether the source threshold `1` remains sharp for that Floquet exponent, i.e. whether exponent `<1` is enough to build phase-aware decomposable FBM slow points rather than merely proving obstruction when the exponent is `>1`.

Suggested next Section-B triple, different from this run and the preceding one: **#7 TAKE THE LIMIT** (slow/fast modulation limits), **#14 FIND THE GROUP ACTING** (periodic cocycle/Floquet quotient), **#24 FIND THE EXTREMAL OBJECT** (barrier profile extremizing the Floquet exponent at fixed duty/mean).

```yaml
ledger_delta:
  track: R07
  run_id: 20260917T0822Z_i0077_periodic_one_sided_barriers_16
  source:
    authors: [Krzysztof Burdzy, Michael Scheutzow]
    work: Forward Brownian Motion
    year: 2014
    arxiv: 1302.6958
    locator: Problem 7.8
    intake: I0077
  target: generalize Theorem 4.3 from parabolic regions to genuinely distinct nonparabolic space-time shape families
  fixed_metric: number of genuinely distinct nonparabolic shape families with a complete source-appropriate theorem, excluding trivial rescalings/reflections/translations and parameter changes
  before: 15
  after: 16
  movement: true
  unchanged_count: 0
  status: PARTIAL
  current_claim: I0077-R07-T17
  new_family: log-periodically moving one-sided upper parabolic barriers with unbounded normalized half-line slices
  theorem_scope:
    - universal nonconfinement when a repeated one-sided gate has (tau/P)*lambda_0(-infinity,-A)>1
    - eventual decomposable-FBM confinement whenever inf b>-1
    - one decomposable FBM works pointwise for every bounded periodic b>=0
  methods_tried: [3,18,27]
  methods_outcome:
    3: succeeded with a class theorem stronger than the canonical example
    18: succeeded via Lamperti / periodic one-sided OU first-passage language
    27: succeeded with one X-plus working for all nonnegative profiles
  exact_self_check:
    checker: artifacts/R07/20260917T0822Z_halfline_gate_check.py
    checker_commit: 00b4ee67777cec354a10d18d3a1d8f5209a3d180
    output: artifacts/R07/20260917T0822Z_halfline_gate_check.out
    output_commit: a963175cc89db6e294adb47242fea12a7d298786
    verdict: PASS
  ownership: R07 exclusive provisional reservation; shared claim text remains PENDING_ADMISSION, not READY
  neighboring_scope: R15 Problem 7.2 remains retired/handoff and distinct; C29 excluded itself from I0077
  prior_art: periodic one-sided OU first-passage asymptotics are classical (Sacerdote 1990; Giorno-Nobile-Ricciardi 1990); no exact Problem-7.8 resolution found in bounded dated search; novelty UNVERIFIED
  closure: false
  audit_refs: []
  remaining_obligation: P26 end-to-end audit plus one independent OTHER-track audit before closure; exact mixed-regime Floquet converse remains open
  next_methods: [7,14,24]
  delivery: private GitHub only; no email/Drive/public/scheduler changes
```
