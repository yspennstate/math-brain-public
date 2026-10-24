Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. NO METRIC MOVEMENT: 59 -> 59; Section-B moves actually used: #8 GO THE OTHER WAY AND DISCRETIZE, #24 FIND THE EXTREMAL OBJECT, #28 REPLACE “FOR ALL” WITH “FOR TYPICAL”.**

Problem/source: Krzysztof Burdzy and Michael Scheutzow, *Forward Brownian Motion* (PTRF 160 (2014), 95–126; arXiv:1302.6958), Problem 7.8 / intake I0077: generalize Theorem 4.3 from parabolic regions to other space-time shapes.

Status: **PARTIAL**. The fixed metric remains 59 because the result below strengthens the already-counted log-periodic parabolic-scale family rather than creating a genuinely new shape family. Mathematically, however, this run removes the main analytic obstruction isolated in the previous report: it proves the subcritical periodic moving-boundary analogue of the Perkins slow-point existence input used in Theorem 4.3(ii)–(iii). The remaining obstruction has moved from “prove periodic slow points” to “sew phase-dependent slow pieces into a decomposable FBM without destroying the independence of the Brownian pieces.”

# R07 CLOSABLE OUTSIDE — periodic Perkins input from a sharp two-terminal second moment

## 1. Continuity / admission / ownership readback

Before research I re-read the required repository state on `master`:

- `probability_campaign_2026_09/INDEX.md` and `RANKING.md`;
- root `POSTED.md`, `RESULTS.md`, and `QUEUE.md`;
- `operations/NEW_METHODS_2026-09-16.md`;
- `operations/claims/I0077.md`;
- newest own report `runs/R07/20260919T0521Z_i0077_critical_periodic_floquet_boundary_59_cf59n2.md`;
- the current `runs/R15/` directory, including the immutable I0076 / Problem 7.2 handoff chain;
- targeted repository searches for `I0077`, `Problem 7.8`, and `1302.6958` in lieu of pretending that the very large intake JSONL mirrors can be rendered end-to-end through the connector.

The canonical claim still says `Owner: R07` and `Status: PENDING_ADMISSION, not READY`. The current owner prompt nevertheless assigns this exact target to R07. No duplicate I0077 owner appeared. R15 owns/owned the distinct Problem 7.2 track and its handoff remains separate. `INDEX.md`/`RANKING.md` settle Problem 7.5, not 7.8, and `POSTED.md` contains no Problem 7.8 closure. The old R07 KPZ route remains preserved by immutable handoff and was not reopened.

The frozen metric remains the number of genuinely distinct nonparabolic shape families with a complete source-appropriate theorem, modulo the existing equivalence convention. The log-periodically modulated square-root tube family was already counted earlier, so the present strengthening cannot honestly create point 60.

## 2. Primary source recovered again

I rechecked arXiv:1302.6958v4 / the Washington-hosted PDF this run.

Definition 2.1: an FBM has witness times `S_n -> -infinity` such that, for every fixed witness, the forward process from that witness is standard Brownian motion.

Remark 4.1: for `c1<c2`, `lambda_0(c1,c2)` is the positive Dirichlet killing exponent associated with

\[
\mathcal A=\frac12\left(\frac{d^2}{dx^2}-x\frac d{dx}\right)
\]

on `(c1,c2)`, with continuity and strict domain monotonicity.

Theorem 4.3 has three clauses:

1. `lambda_0>=1`: every FBM must touch/escape one normalized parabolic boundary asymptotically;
2. `lambda_0<=1`: there exists a decomposable FBM satisfying the reverse asymptotic inequalities;
3. if `c1<=0<=c2` and `lambda_0<1`: there exists a decomposable FBM pointwise inside the parabolic strip for all negative times.

The source proof of clauses (ii)–(iii) starts from Perkins [1983, Thm. 2(a)], in the form

\[
\mathbb P\{\exists t\ge0,\Delta>0:\ B(t+h)-B(t)\in[c_1\sqrt h,c_2\sqrt h]
\ \forall h\in[0,\Delta]\}=1
\]

when `lambda_0(c1,c2)<1`; it then uses time reversal, support, Brownian scaling, and independent stopped Brownian pieces. Problem 7.8 is the separate one-sentence request to generalize Theorem 4.3 from parabolas to other space-time shapes. The trailing forward-Levy sentence is Problem 7.9, not part of I0077.

This run targets exactly the missing periodic counterpart of the quoted Perkins input.

## 3. Current literature / prior-art check, dated 2026-09-19

Fresh bounded searches included:

- `"Brownian slow points" periodic boundary`;
- `"slow points" "moving boundary" Brownian Hausdorff`;
- `"slow points" Ornstein-Uhlenbeck periodic`;
- exact `"Forward Brownian Motion" "Problem 7.8"` and later-author/citing-paper searches;
- recent slow-point work after Perkins/Bass–Burdzy.

Relevant sources recovered/rechecked:

- E. Perkins, *On the Hausdorff dimension of the Brownian slow points*, Z. Wahrscheinlichkeitstheorie verw. Gebiete 64 (1983), 369–399, DOI 10.1007/BF00532968.
- R. F. Bass and K. Burdzy, *A critical case for Brownian slow points*, Probab. Theory Relat. Fields 105 (1996), 85–108, DOI 10.1007/BF01192072.
- C. Esser and L. Loosveldt, *Slow, ordinary and rapid points for Gaussian Wavelets Series and application to Fractional Brownian Motions*, ALEA 19 (2022), arXiv:2203.05472; and their later multifractional slow-point work.
- D. Khoshnevisan and C. Y. Lee, *On the slow points of fractional Brownian motion*, arXiv:2603.07483 (submitted 8 March 2026), which introduces a different localization method for fBm slow points and emphasizes potentially reusable localization ideas.
- Periodic principal-eigenvalue/Floquet machinery from the literature already recorded in prior R07 reports (e.g. Nadin 2009) is treated as established background, not a new contribution here.

The bounded searches did **not** surface an accessible theorem giving the exact periodic moving-normalized-boundary slow-point result proved below, nor an accessible later source explicitly resolving Problem 7.8. This is bounded negative evidence only. Publication novelty remains **UNVERIFIED**.

## 4. Periodic moving normalized intervals and the Floquet estimate

Let `a,b:R->R` be `P`-periodic Lipschitz functions satisfying

\[
g_*:=\inf_{r\in\mathbb R}(b(r)-a(r))>0.
\]

Write

\[
I_r=[a(r),b(r)].
\]

Let `Lambda=Lambda(a,b)` be the principal Floquet killing exponent of stationary Ornstein–Uhlenbeck motion in the moving periodic interval `I_r`, with the same convention as in the previous R07 Floquet reports. In the constant case,

\[
\Lambda(c_1,c_2)=\lambda_0(c_1,c_2).
\]

For a phase `theta` (modulo `P`), terminal time `t`, and `0<epsilon<H`, define

\[
E_\theta(t;\epsilon,H)
:=\left\{
B_t-B_{t-h}\in\sqrt h\,I_{\theta+\log h}
\quad\forall h\in[\epsilon,H]
\right\}.
\tag{4.1}
\]

The phase convention is immaterial up to reversing the periodic schedule. The reversed schedule has the same principal Floquet exponent because the killed OU evolution is generated by self-adjoint instantaneous Dirichlet OU operators in Gaussian measure, and the one-period reversed evolution is the adjoint of the forward monodromy.

### Lemma 4.1 — uniform one-terminal Floquet survival

There exist constants `0<c0<C0<infinity`, depending only on `(a,b)`, such that uniformly in phase `theta` and `0<epsilon<H<=1`,

\[
c_0\left(\frac\epsilon H\right)^\Lambda
\le
\mathbb P(E_\theta(t;\epsilon,H))
\le
C_0\left(\frac\epsilon H\right)^\Lambda,
\tag{4.2}
\]

with the constants enlarged, if necessary, to cover bounded logarithmic durations.

**Proof.** For fixed `t`, the reversed increment process

\[
W_h:=B_t-B_{t-h},\qquad 0\le h\le t,
\]

has standard Brownian law in the lag variable `h`. Under the Lamperti transform

\[
Y_s=e^{-s/2}W_{e^s},
\]

`Y` is stationary Ornstein–Uhlenbeck motion with generator `A=(1/2)(d^2/dx^2-x d/dx)`. Event (4.1) is survival of this OU process in a periodic moving interval over logarithmic time `log(H/epsilon)`. The one-period killed evolution is compact and strongly positive. Krein–Rutman gives a simple positive principal multiplier `e^{-P Lambda}` and positive left/right Floquet eigenfunctions. Decompose an arbitrary duration into an integer number of periods plus a remainder in `[0,P]`. Positivity of the stationary Gaussian initial density, positivity of the principal eigenfunctions, compactness of the phase circle, and boundedness of the remainder evolution yield matching upper and lower constants uniform in the starting phase. This gives (4.2). QED.

The lower bound in (4.2), not just the exponent, is essential for the second moment below.

## 5. Refutation-first attack: the naive second moment appears to stop at Lambda<1/2

Before attempting a proof I tried to break the proposed `Lambda<1` slow-point threshold by looking at two candidate terminal times separated by `r`.

If one simply throws away every shared coarse-scale constraint and keeps only two disjoint fine neighborhoods, one gets the crude estimate

\[
\mathbb P(E_\theta(s;\epsilon,1)\cap E_\theta(t;\epsilon,1))
\lesssim
\left(\frac\epsilon r\right)^{2\Lambda}.
\tag{5.1}
\]

After normalization by the squared one-point probability `asymp epsilon^{2 Lambda}`, this behaves like `r^{-2 Lambda}`, which is integrable only when `Lambda<1/2`.

That looked like a genuine obstruction to the desired threshold. It is not. The estimate loses exactly one survival factor: the two terminal events share a coarse history, and that shared history itself costs `r^Lambda`. Restoring that factor changes the singularity from `r^{-2 Lambda}` to the sharp `r^{-Lambda}`, which is integrable for every `Lambda<1`.

This failed-negation search is the mechanism behind the theorem below.

## 6. Move #24 — extremal two-terminal overlap geometry

Put

\[
M:=\sup_r\max\{|a(r)|,|b(r)|\}<\infty.
\]

For brevity write

\[
E_t=E_\theta(t;\epsilon,1).
\]

### Lemma 6.1 — sharp two-terminal bound

Assume `Lambda<1`. There is `C<infinity`, uniform in `theta`, such that for `s,t in [1,2]`, `r=|t-s|`, and sufficiently small `epsilon`,

\[
\mathbb P(E_s\cap E_t)
\le
\begin{cases}
C\epsilon^\Lambda,&0<r<8\epsilon,\\[1ex]
C\epsilon^{2\Lambda}r^{-\Lambda},&8\epsilon\le r\le1/4,\\[1ex]
C\epsilon^{2\Lambda},&1/4<r\le1.
\end{cases}
\tag{6.1}
\]

**Proof.** The near-diagonal estimate is immediate from `P(E_s cap E_t)<=P(E_t)` and Lemma 4.1.

Now suppose `8 epsilon <= r <= 1/4` and, without loss of generality, `t=s+r`. Define the shared coarse event

\[
C_t:=E_\theta(t;2r,1),
\]

and the two fine events

\[
F_t:=E_\theta(t;\epsilon,r/8),
\qquad
F_s:=E_\theta(s;\epsilon,r/8).
\]

Then

\[
E_s\cap E_t\subset C_t\cap F_t\cap F_s.
\tag{6.2}
\]

By Lemma 4.1,

\[
\mathbb P(C_t)\le C r^\Lambda,
\qquad
\mathbb P(F_t),\mathbb P(F_s)\le C\left(\frac\epsilon r\right)^\Lambda.
\tag{6.3}
\]

The only issue is that `C_t` is not independent of the two fine events. The dependence can be controlled exactly by a Brownian-bridge density.

Let

\[
U:=B_t-B_{t-2r}.
\]

The event `C_t` is measurable with respect to `U` and the Brownian path up to time `t-2r`; on `C_t`,

\[
|U|\le M\sqrt{2r}.
\tag{6.4}
\]

Conditional on `U=u`, the Brownian path on `[t-2r,t]` is a Brownian bridge of duration `2r` and endpoint `u`, independent of the pre-`t-2r` path. The two fine events use disjoint subintervals

\[
A=[t-r/8,t],
\qquad
D=[s-r/8,s]=[t-9r/8,t-r].
\]

Let `Delta_A` and `Delta_D` denote the forward net increments on these two subintervals. Before conditioning on `U`, the paths on `A` and `D` are independent Brownian pieces and the complement of `A union D` inside `[t-2r,t]` has total duration

\[
2r-r/8-r/8=7r/4.
\]

Consequently the conditional law of the pair of fine paths, relative to the product of their unconditioned Brownian laws, has density

\[
R_u=
\frac{p_{7r/4}(u-\Delta_A-\Delta_D)}{p_{2r}(u)},
\tag{6.5}
\]

where `p_v(x)=(2 pi v)^(-1/2) exp(-x^2/(2v))`.

On `F_t cap F_s`,

\[
|\Delta_A|,|\Delta_D|\le M\sqrt{r/8},
\]

while (6.4) bounds `u/sqrt r`. Inserting these bounds in (6.5) shows

\[
R_u\le C_M
\tag{6.6}
\]

uniformly in `r`, `theta`, and all values of `u` that can occur on `C_t`. Therefore, conditional on `U` and the coarse past,

\[
\mathbb P(F_t\cap F_s\mid U,\mathcal F_{t-2r})
\le
C\left(\frac\epsilon r\right)^{2\Lambda}
\quad\text{on }C_t.
\tag{6.7}
\]

Combining (6.2), (6.3), and (6.7),

\[
\mathbb P(E_s\cap E_t)
\le
C r^\Lambda\left(\frac\epsilon r\right)^{2\Lambda}
=
C\epsilon^{2\Lambda}r^{-\Lambda}.
\tag{6.8}
\]

This is the key gain over the naive estimate (5.1).

Finally suppose `r>1/4`. Keep only the restrictions with lags in `[epsilon,1/16]`. They live on two disjoint Brownian time intervals, hence are independent. Lemma 4.1 gives

\[
\mathbb P(E_s\cap E_t)
\le C\epsilon^{2\Lambda}.
\]

This proves (6.1). QED.

The exponent `r^{-Lambda}` is exactly the overlap singularity predicted by the heuristic “one shared coarse survivor and two independent fine survivors.”

## 7. Moves #8 and #28 — finite-cutoff terminal sets, then all phases

For fixed phase `theta` and `epsilon>0`, define the finite-cutoff terminal set

\[
A_\epsilon^\theta
:=\{t\in[1,2]:E_\theta(t;\epsilon,1)\text{ holds}\}
\tag{7.1}
\]

and its Lebesgue mass

\[
Z_\epsilon^\theta:=|A_\epsilon^\theta|
=\int_1^2\mathbf 1_{E_\theta(t;\epsilon,1)}\,dt.
\tag{7.2}
\]

This is the useful discretization: first solve the finite logarithmic-depth problem exactly enough for a second moment, then let the cutoff go to zero. No checker or numerical certificate is involved; the finite-cutoff object is still analytic.

By Lemma 4.1,

\[
c\epsilon^\Lambda
\le
\mathbb E Z_\epsilon^\theta
\le
C\epsilon^\Lambda
\tag{7.3}
\]

uniformly in `theta`.

Using Lemma 6.1 and integrating in the separation `r=|t-s|`,

\[
\begin{aligned}
\mathbb E[(Z_\epsilon^\theta)^2]
&\le
C\epsilon^\Lambda\int_0^{8\epsilon}dr
+
C\epsilon^{2\Lambda}\int_{8\epsilon}^{1/4}r^{-\Lambda}\,dr
+
C\epsilon^{2\Lambda}\\
&\le C'\epsilon^{2\Lambda},
\end{aligned}
\tag{7.4}
\]

because `Lambda<1`; the near-diagonal term satisfies `epsilon^{1+Lambda}<=epsilon^{2Lambda}` for `epsilon<=1` and `Lambda<=1`.

Paley–Zygmund now gives a phase-uniform constant `c_*>0` such that

\[
\mathbb P(A_\epsilon^\theta\ne\varnothing)
\ge
\mathbb P(Z_\epsilon^\theta>0)
\ge c_*
\tag{7.5}
\]

for all sufficiently small `epsilon`.

Take the nested sequence

\[
\epsilon_n=e^{-nP}
\]

(starting at any large enough `n`). For a fixed Brownian sample path, the sets `A_{epsilon_n}^theta` are nested compact subsets of `[1,2]`: the defining inequalities are closed and involve a continuous Brownian path and a continuous moving boundary on `[epsilon_n,1]`. Hence the events `{A_{epsilon_n}^theta != empty}` decrease with `n`. By (7.5),

\[
\mathbb P\left(\bigcap_n\{A_{\epsilon_n}^\theta\ne\varnothing\}\right)
\ge c_*>0.
\tag{7.6}
\]

On the event in (7.6), Cantor’s intersection theorem gives a terminal point `t in [1,2]` belonging to every `A_{epsilon_n}^theta`, and therefore

\[
B_t-B_{t-h}\in\sqrt h\,I_{\theta+\log h}
\qquad\forall h\in(0,1].
\tag{7.7}
\]

At `h=0` both boundary endpoints and the Brownian increment converge to zero, so the condition extends continuously to `h=0`.

Translation to disjoint Brownian blocks, for example blocks `[3m,3m+2]`, gives independent trials with the same lower bound `c_*`. Borel–Cantelli therefore upgrades positive probability to almost-sure infinitely many terminal slow points for every **fixed** deterministic phase.

### Theorem T88 — subcritical periodic moving-boundary slow points

If

\[
\boxed{\Lambda(a,b)<1,}
\tag{T88a}
\]

then for every fixed deterministic phase `theta`, standard Brownian motion almost surely has infinitely many terminal times `t` such that

\[
\boxed{
B_t-B_{t-h}
\in
\sqrt h\,[a(\theta+\log h),b(\theta+\log h)]
\quad\forall h\in[0,1].
}
\tag{T88b}
\]

By time reversal the equivalent forward-increment formulation holds as well.

For constant `a=c1`, `b=c2`, T88 recovers the subcritical existence implication from the Perkins theorem quoted as (4.9) in Burdzy–Scheutzow.

This is stronger than the `Lambda<1/2` result suggested by the naive independent-fine-branches estimate; the bridge calculation in Lemma 6.1 is exactly what reaches the source threshold `1`.

## 8. Simultaneous phase upgrade

A random phase cannot automatically be substituted into a theorem proved only “for every fixed phase.” The run therefore used move #28 explicitly: prove the fixed-phase statement first, then upgrade it to a single Brownian probability-one event that covers **all phases**.

Assume `Lambda(a,b)<1`. By continuity of the periodic principal eigenvalue under a small uniform inward perturbation, choose `eta>0` such that

\[
I_r^{[-\eta]}:=[a(r)+\eta,b(r)-\eta]
\]

still has Floquet exponent strictly below `1`.

Let `L` be a common Lipschitz constant for `a` and `b`. If `L=0` there is no phase dependence and there is nothing to prove. Otherwise choose a finite phase net `theta_1,...,theta_N` on the circle `R/PZ` with mesh at most `eta/(2L)`.

Apply T88 to the **eroded** profile and each of the finitely many net phases. On one probability-one event, every net phase has infinitely many eroded slow points. Given an arbitrary phase `theta`, choose `theta_j` with circular distance at most `eta/(2L)`. For every `u`,

\[
a(\theta_j+u)+\eta\ge a(\theta+u),
\qquad
b(\theta_j+u)-\eta\le b(\theta+u),
\tag{8.1}
\]

so the eroded interval for `theta_j` is contained in the original interval for `theta`. Every eroded slow point for `theta_j` is therefore a slow point for phase `theta`.

### Corollary T89 — all phases on one Brownian event

If `Lambda(a,b)<1`, then there exists one Brownian probability-one event on which **for every** phase `theta in R/PZ` there are infinitely many `t` satisfying (T88b).

This resolves the random-phase loophole at the level of the Brownian slow-point input itself.

## 9. What this does and does not solve in Problem 7.8

The previous run identified the missing subcritical periodic analogue of Perkins’s local slow-point theorem as the main analytic obstacle. T88/T89 provide that input at the sharp `Lambda<1` threshold.

This does **not** yet complete the source’s clauses (ii) and (iii) for log-periodic tubes, because Burdzy–Scheutzow require the resulting process to be **decomposable**. In Definition 2.2 the stopped Brownian pieces

\[
(T_k,\{B^k_t:0\le t\le T_k\})
\]

must be independent across `k`.

For a log-periodic global tube, the phase seen at a seam depends on the cumulative random length of all later pieces. T89 says that an independent Brownian piece contains slow points for every externally supplied phase, but if one chooses `T_k` using that random seam phase, then `T_k` depends on the later pieces. That generally destroys the independence of the stopped-piece pairs required for decomposability.

This is now the exact source-facing obstruction:

\[
\boxed{
\text{periodic slow points exist at the sharp threshold, but adaptive phase selection couples the pieces.}
}
\tag{9.1}
\]

A conditional-on-phase construction is not enough; the stopping laws have to be fixed piece-by-piece without reading random future seam phases, or one must find a deterministic scale-separation scheme whose seam-phase error is summably negligible while keeping the pairs independent.

This is a materially different remaining obligation from the one in the preceding report.

## 10. Why the argument is not being counted as a new shape family

T88/T89 are new theorems for the already-counted log-periodic square-root tube family. Varying the periodic profile, its phase, or the Floquet exponent inside this same structural family cannot create another metric point under the frozen equivalence convention.

Therefore

\[
\boxed{59\longrightarrow59.}
\]

This is the **third consecutive unchanged metric run** since point 59 was reached. The unchanged count is therefore

\[
\boxed{2\longrightarrow3.}
\]

Under the owner’s Section-I policy, the **next** R07 invocation is a mandatory thinking/stuck run unless an intervening independently verified metric movement is recovered from repository history. It must not manufacture another lemma before writing the five-part stuck analysis.

## 11. Method accounting

### #8 GO THE OTHER WAY AND DISCRETIZE — succeeded

I replaced the infinite slow-point condition by the finite-cutoff sets `A_epsilon^theta`, proved quantitative first/second moment bounds there, and only then sent `epsilon` down a nested geometric sequence. This made the compactness step exact and isolated the only singular overlap scale.

### #24 FIND THE EXTREMAL OBJECT — succeeded

The extremal obstruction is a pair of candidate terminals separated by `r`. The correct geometry has one shared coarse survivor, costing `r^Lambda`, and two fine survivors, each costing `(epsilon/r)^Lambda`. The resulting kernel `epsilon^(2Lambda) r^(-Lambda)` is exactly integrable up to the source threshold `Lambda<1`.

### #28 REPLACE “FOR ALL” WITH “FOR TYPICAL” — succeeded, then upgraded

I first proved the theorem for one deterministic phase. Erosion plus a finite phase net then upgraded the result to all phases simultaneously on one Brownian probability-one event. The upgrade is essential because phase can be random in later concatenation attempts.

### Mandatory refutation-first outcome

The naive overlap estimate `r^(-2Lambda)` appeared to refute the sharp threshold beyond `Lambda=1/2`. Tracking the coarse shared survivor showed exactly why that apparent obstruction was false and produced the sharp `r^(-Lambda)` kernel.

## 12. Finite-core/checker decision

There is no nontrivial finite arithmetic or combinatorial core in T88/T89. The proof consists of Floquet spectral bounds, an explicit Gaussian bridge Radon–Nikodym ratio, a second-moment integral, compactness, and a finite phase-net argument. Under the 90/10 rule I did **not** manufacture a checker on an unchanged metric run.

T88/T89 currently have **0/2 independent OTHER-track audits**. They are research claims written with full proofs here, not closure certificates.

## 13. Honest status / next obligation

Source status remains **PARTIAL**. Problem 7.8 is not called solved, refuted, or closed. Publication novelty is **UNVERIFIED**.

The next run is required by the stagnation rule to be a thinking/stuck report. Its exact blocker should now be stated as follows:

\[
\boxed{
\begin{gathered}
\text{Given the all-phase slow-point theorem T89, construct independent stopped Brownian pieces}\
(T_k,B^k_{[0,T_k]})_{k\in\mathbb Z}\text{ whose concatenation tracks one deterministic log-periodic tube,}\
\text{without letting }T_k\text{ depend on the random cumulative seam phase generated by the other pieces.}
\end{gathered}}
\tag{13.1}
\]

The simplest promising recovery is a deterministic, superexponentially separated **primary-window scheme**: for each negative `k`, prescribe in advance a narrow family of scale windows and a phase-specific stopping rule depending only on `B^k`; make primary-window failure probabilities summable; and arrange that, on primary success, `T_k` dominates the total later duration strongly enough that the actual seam phase differs from the preassigned phase by a summable error. The proof obligation is to do this while controlling the seam neighborhoods themselves, not only the bulk of each Brownian piece.

No audit is requested before that obstruction is either resolved or reduced to a clean independent-piece lemma.

## 14. Model / scheduler control reality

The exposed automation control surface still has no binding model-family selector, no reasoning-effort selector, no guaranteed-duration field, and no authenticated completed-run model receipt. GPT-6/maximum is therefore prompt text only. This report truthfully identifies the runtime as GPT-5.6 Sol with reasoning level UNVERIFIED.

The repository records context-specific scheduler permission history: some P/C updates, including a later P26 update, succeeded from an authorized context, while R-series edits were denied in another context. No scheduler, permission, workflow, email, Drive, or public-posting action was attempted in this run.

## ledger_delta

```yaml
ledger_delta:
  track: R07
  allocation: CLOSABLE_OUTSIDE
  source: "Burdzy--Scheutzow, Forward Brownian Motion, Problem 7.8"
  intake: I0077
  claim_status: "PENDING_ADMISSION, not READY"
  fixed_metric: "number of genuinely distinct nonparabolic shape families with a complete source-appropriate theorem"
  before: 59
  after: 59
  movement: "NO MOVEMENT"
  unchanged_count_before: 2
  unchanged_count_after: 3
  methods: [8, 24, 28]
  new_claims:
    - "I0077-R07-T88: for any periodic Lipschitz moving normalized interval with Floquet killing exponent Lambda<1, every fixed phase has a.s. infinitely many Brownian terminal slow points"
    - "I0077-R07-T89: after a small erosion and finite phase-net upgrade, one Brownian probability-one event contains infinitely many slow points for every phase simultaneously"
    - "sharp two-terminal overlap estimate P(E_s cap E_t) <= C epsilon^(2 Lambda) |t-s|^(-Lambda) in the intermediate separation regime"
  source_status: PARTIAL
  novelty_status: UNVERIFIED
  audits_other_tracks: "0/2"
  finite_core: "none; analytic proof, no checker manufactured"
  remaining_obligation: "independent-piece/decomposable sewing across random periodic seam phases"
  next_run_protocol: "MANDATORY_STUCK_THINKING_RUN if no intervening metric movement is recovered"
```
