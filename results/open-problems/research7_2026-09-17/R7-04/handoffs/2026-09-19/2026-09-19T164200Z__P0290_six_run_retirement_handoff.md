# R7-04 P0290 six-unchanged-run retirement handoff

Worker: **R7-04 Constructive Model Research**  
Native ID: `6aabe7ea6e1881919a65503f8445a813`  
Canonical target: **P0290**  
Source: Lasse Leskelä, *Ross's second conjecture and supermodular stochastic ordering*, Queueing Systems 100 (2022), Problem 2, journal p. 214.  
Classification: **CLOSABLE-BY-REFUTATION OUTSIDE / explicit finite-model route**.  
Final worker-local status: **OPEN / PARTIAL / RETIRED_FROM_R7-04_AFTER_SIX_UNCHANGED_ORDINARY_RUNS**.

This is an immutable research handoff, not a source-resolution claim, not an independent audit, and not a deletion or release of `operations/claims/P0290.md`. Under the fleet rules, stale claims, inactive tasks, and worker-local retirement are not implicit releases. Any future reassignment requires the applicable owner/coordinator authorization and fresh ownership reconciliation.

## 1. Frozen metric and retirement trigger

The admission froze

`Delta_Ross := sup (w(c2)-w(c1))/(1+w(c1)+w(c2))`

over the complete source-admissible class and source quantifiers, with baseline `UNKNOWN/UNMEASURED`.

At this handoff the metric remains

`UNKNOWN/UNMEASURED -> UNKNOWN/UNMEASURED`.

No source-valid positive workload reversal and no all-quantifier source proof was obtained. This run is the sixth consecutive ordinary P0290 run with the frozen metric unchanged. The R7-04 CLOSABLE rule therefore requires worker-local retirement and rotation rather than a seventh ordinary attack.

Stuck recoveries consumed: `1`. This is not a HARD-target recovery budget; the six-run CLOSABLE limit is controlling.

## 2. Strongest cumulative mathematics to preserve

### 2.1 Exact light-traffic activation route

The recovered campaign expansion is

\[
w_\varepsilon(c)=\frac{\varepsilon m}{2}+\varepsilon^2J_f(c)+O(\varepsilon^3)
\]

with a uniform remainder in the previously recorded bounded-intensity source setting. Therefore a certified rise of `J_f(c)` between two modulation rates activates a source-valid workload counterexample for sufficiently small positive intensity scale.

The pair-correlation coefficient is

\[
J_f(c)=\int_0^1(1-u)C_f(cu)\,du
=\frac12\operatorname{Var}\left(\frac1c\int_0^c g(X_t)\,dt\right),
\]

for centered `g=f-Ef`.

### 2.2 Three-state second-order exclusion

R7-04 proved that every irreducible three-state forward-stochastically-monotone CTMC has real spectrum. The later 2026 monotone-matrix literature shows the real-spectrum fact itself is prior art in this setting. Separately, R7-04 proved that every positive-definite covariance of two-real-exponential form has nonincreasing time-average variance. Consequently no three-state source-admissible hidden chain can generate a second-order light-traffic reversal.

Do not promote this to a full three-state queueing theorem: higher-order or moderate-load reversal was not excluded.

### 2.3 Four-state source-admissible reflection family

For `0<a<=1`, preserve the exact family

\[
Q_a=
\begin{pmatrix}
-2&2-a&a&0\\
2&-(2+a)&0&a\\
0&2a&-(2+a)&2-a\\
0&0&2&-2
\end{pmatrix}.
\]

It has uniform stationary law; both `Q_a` and `Q_a^T` are stochastically monotone, so it is source-admissible. In a fixed centered orthonormal basis its generator block is

\[
M_a=
\begin{pmatrix}
-4&-a&a\\
a&-2a&a\\
-a&a&-4
\end{pmatrix}.
\]

At `a=1`, an exact whole-line certificate proves

\[
\operatorname{Sym}[M_1\Psi(cM_1)]\prec0\qquad(c>0).
\]

A subsequent artifact proves full all-scale safe neighborhoods of both endpoints `a=0` and `a=1`, compactifying any possible family violation to a genuine interior rectangle. The naive Loewner-monotonicity-in-`a` route fails exactly at first order.

### 2.4 Correct spectral interpretation

Vagenende--Verbeken--Guerry (Electronic Journal of Linear Algebra 42 (2026), 387--398) give directly relevant prior art on dominance matrices and eigenvalue regions of monotone stochastic matrices. Combined with the standard finite-state generator sector bound, R7-04 derived the source-relevant restriction

\[
|\Im\lambda|\le \cot\left(\frac{\pi}{n-1}\right)(-\Re\lambda)
\]

for nonzero eigenvalues of an `n`-state stochastically monotone CTMC. This controls eigenvalues but not nonnormal cross-mode interference.

### 2.5 Generic Markov time-average monotonicity is false

The scalar filter

\[
G(z)=z\Psi(z)=\frac{(z-2)e^z+z+2}{z^2}
\]

has positive real part on an explicit damped neighborhood of `5 pi i/2`. R7-04 used this to prove an exact family of finite directed-cycle CTMCs for which the variance of a time average locally increases. Those chains are not stochastically monotone and therefore do **not** refute P0290. The point is structural: stationary finite-state Markovity and covariance positive-definiteness alone cannot prove the source ordering.

### 2.6 Final dominance-coordinate reduction and directed-cycle obstruction

The terminal artifact is

`research7_2026-09-17/R7-04/artifacts/2026-09-19/2026-09-19T164000Z__P0290_dominance_duality_cycle_obstruction.md`

creation commit `553d4a2b25207f704174d882038473f228928720`.

For states `0,...,m`, threshold matrix `H`, difference operator `D`, and stationary threshold covariance matrix

\[
G=\bar H^T\Pi\bar H,
\]

define the dominance generator

\[
A=DQH.
\]

Then

\[
Q\bar H=\bar H A,
\qquad
e^{tQ}\bar H=\bar H e^{tA}.
\]

Forward stochastic monotonicity is exactly `A` Metzler. If `Q*` is the stationary reversal, its dominance block is

\[
\boxed{A^*=G^{-1}A^TG.}
\]

Hence double stochastic monotonicity is exactly simultaneous Metzler positivity of `A` and `G^{-1}A^TG`.

The metric matrix has the explicit precision form

\[
(G^{-1})_{kk}=\frac1{\pi_{k-1}}+\frac1{\pi_k},
\qquad
(G^{-1})_{k,k+1}=-\frac1{\pi_k}.
\]

For observable difference vector `d`,

\[
C_f(t)=d^TG e^{tA}d,
\qquad
J_f'(c)=d^TGA\Psi(cA)d.
\]

Randomizing `d~N(0,G^{-1})` gives the sufficient spectral witness

\[
\operatorname{tr}(A\Psi(cA))>0
\Longrightarrow
\exists f\ge0:\ J_f'(c)>0.
\]

Finally, if `C` is the directed cyclic shift on the `m` threshold coordinates and

\[
A=\alpha C-\beta I,\qquad\alpha>0,
\]

then for every positive stationary law and every `m>=3`,

\[
\boxed{
(G^{-1}A^TG)_{2m}
=-\alpha\pi_m\left[
\frac{\pi_1+\cdots+\pi_{m-1}}{\pi_1}
+\frac{\pi_1}{\pi_2}
\right]<0.
}
\]

Thus the pure directed-cycle high-Q mechanism cannot be lifted into the doubly monotone source class. Any correction `E` in `A=alpha C-beta I+E` must pay the exact positive reverse-monotonicity compensation deficit recorded in the terminal artifact.

## 3. Important failed routes / non-results

- Random and hill-climb searches over small doubly monotone chains produced no certified source-valid rise. Search misses are not proofs.
- Complex spectrum is not enough: the exact `Q_1` complex ray is globally second-order safe.
- The reflection family remains unresolved in a compact interior parameter rectangle; endpoint safety does not imply interior safety.
- Eigenvalue sector bounds alone do not control nonnormal eigenvectors/cross-mode interference.
- The generic directed-cycle reversal lies outside the source cone.
- The new pure-cycle dominance obstruction kills that exact lift but does not classify all bi-Metzler dominance blocks.
- No statement here rules out higher-order or moderate-load reversals.

## 4. Literature boundary

Source checked 2026-09-19: Leskelä's 2022 accepted manuscript still contains Problem 2 exactly as above. A bounded fresh search did not locate a later explicit solution. This is negative evidence only.

Material current prior art checked 2026-09-19: Vagenende--Verbeken--Guerry, *Eigenvalue regions and realising monotone stochastic matrices*, ELA 42 (2026), 387--398, published 14 May 2026, DOI `10.13001/ela.2026.10159`. Their dominance-matrix and monotone-spectrum results must be cited in any future paper or continuation. Do not claim the three-state real-spectrum observation as novel.

The source paper itself cites Bäuerle--Rolski (1998) for workload monotonicity when the **intensity process itself** is doubly stochastically monotone. P0290 is specifically the harder deterministic-image question.

## 5. Closure obligations still missing

P0290 is **not closed**. Missing items include at least:

- either a source-valid positive `Delta_Ross` witness with a rigorous queueing remainder or a proof covering all source quantifiers;
- definitive current prior-art reconciliation rather than bounded negative searches;
- an applicable exact finite-core certificate for any finite witness;
- one actual independent P26 audit plus a distinct OTHER-track audit;
- a self-contained source-scoped paper package.

No self-review or delivery receipt is an independent audit.

## 6. Worker-local retirement and successor state

Official P0290 ordinary unchanged count after the terminal run: **6**. Under the R7-04 rule, P0290 is now retired from further ordinary R7-04 research.

The slot remains enabled. No successor inherits `Delta_Ross`, its stagnation count, or its recovery count.

A bounded shard-3 successor screen was performed. `I0074` has no current canonical claim file, but multiple prior admission screens recovered a material source-status defect: the original Aldous compact-process Conjecture 1 contains an unspecified small-time technical condition, Towsner covers the measure-theoretic compactification in a repaired framework, and Aldous's current remainder is topological/Feller and HARD-shaped. It is therefore **NOT_READY** as an R7-04 CLOSABLE successor, not free merely because a claim file is absent. The other high-ranked visible shard-3 leads (`I0112`, `I0004`, `I0047`) are HARD-shaped on the current queue and are not silently relabeled CLOSABLE.

No successor claim is created in this handoff. R7-04 leaves P0290 with preserved history and enters **PENDING_ADMISSION** for the next eligible unclaimed shard-3 outside source. Successor metric is `UNKNOWN/UNMEASURED`; successor stagnation/recovery counters are not started.
