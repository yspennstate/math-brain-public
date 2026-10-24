Model actually ran: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. NO FIXED-METRIC MOVEMENT on D0036: `C_power: 1 -> 1`; status PARTIAL, source still OPEN-looking under bounded current search. Methods actually used: #3 PROVE SOMETHING STRONGER, #12 FIND WHAT IS CONSERVED, #30 ONE SCALE AT A TIME.**

# R14 — Bradley Question 8: a subpower zero can be ordinary-r mixing but fail interlaced r-star mixing

Date: 2026-09-18 UTC.  
Repository / branch: `yspennstate/math-open-problems` / `master`.

## 0. Continuity, exclusions, and repository read

Repository continuity controls over the stale native task title. I do **not** reopen the negative-margin spherical perceptron, I0089, BIS32, or H0017. The perceptron handoff still preserves the last supported bracket

\[
6.30297437506\le \alpha_c(-1)\le12.78437096216,
\qquad
\alpha_U-\alpha_L=6.48139658710.
\]

H0017 already consumed both permitted hard-task recoveries and was terminally handed off. R14's current exclusive HARD OUTSIDE claim is `operations/claims/D0036.md`.

At the start of this run I reread/recovered the required current state rather than restarting:

- `probability_campaign_2026_09/INDEX.md` and `RANKING.md`;
- root `POSTED.md`, `RESULTS.md`, and `QUEUE.md`;
- `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md`;
- the current D0036 claim and the newest R14 report `runs/R14/2026-09-18T04-06-08Z_d0036_power_zero_quantization_4e9f.md`;
- the newest available neighboring R15 report and the newest available R08 report, together with their earlier D0036/D0037 spectral screens;
- the D-intake Bradley rows and current ownership search hits.

No shared root ledger, peer file, scheduler, email, Drive, public surface, purchase, permission, or workflow was modified.

## 1. Source/current-status check and frozen metric

Outside source: Richard C. Bradley, *Basic Properties of Strong Mixing Conditions. A Survey and Some Open Questions*, *Probability Surveys* **2** (2005), Section 6.5, Question 8.

For a centered complex weakly stationary sequence `X=(X_k)`, Bradley defines `r*(n)` as the supremum of normalized covariances of finite linear combinations on arbitrary nonempty finite disjoint index sets `Q,S subset Z` with `dist(Q,S)>=n`; the sets may be interlaced. The source records

\[
r(n)\le r^*(n),
\]

and hence `r*(n)->0` implies ordinary `r(n)->0`. Bradley's Theorem 6.2 (Helson--Sarason) says that ordinary `r(n)->0` is equivalent to

\[
f=|p|^2\exp(u+\widetilde v),
\tag{HS}
\]

with `p` a polynomial and `u,v` continuous real functions. Theorems 6.4--6.5 give the clean bounded-away-from-zero / positive-continuous cases. Bradley then explicitly asks for a necessary-and-sufficient condition for `r*(n)->0`.

Fresh bounded searches dated 2026-09-18 for the exact Question 8 wording, `r*(n)` / interlaced linear dependence, spectral-density zeros, logarithmic/slowly-varying zeros, and later Bradley material again found no source-matching full characterization and no exact match for the construction below. This is bounded negative evidence only. The ingredients are classical harmonic analysis and elementary spectral decimation, so **priority remains UNVERIFIED / folklore-adjacent; no novelty claim is made**.

The frozen R14 metric remains

`C_power in {0,1}`,

the exact classification of the finite algebraic-zero family from the preceding run. It already moved `0 -> 1`. This run does not game the metric by replacing it. Therefore

**before: `C_power=1`; after: `C_power=1` — NO MOVEMENT.**

The new result is instead a certified source-relevant obstruction beyond the algebraic family.

## 2. #3 PROVE SOMETHING STRONGER — dyadic local zero order is quantized without a power-law ansatz

The previous report assumed a pointwise algebraic asymptotic `f(t_0+x)=c|x|^alpha(1+o(1))` and proved that `alpha` must be an even integer if `r*(n)->0`. Ordinary `r(n)->0` already gives a stronger local invariant that requires no regular-variation hypothesis.

For a locally integrable function `g` on the positive side of `0`, put

\[
A_h(g):=\frac1h\int_h^{2h}g(x)\,dx.
\]

### Proposition 2.1 — dyadic log-order quantization

Assume `r(n)->0` and let `f` be the spectral density. Fix `t_0` and write `zeta=e^{it_0}`. Let `m>=0` be the multiplicity at `zeta` of the polynomial `p` in one Helson--Sarason representation `(HS)` (with `m=0` if `p(zeta) != 0`). Then

\[
\boxed{
\lim_{h\downarrow0}
\frac{A_{2h}(\log f(t_0+\cdot))-A_h(\log f(t_0+\cdot))}{\log 2}
=2m\in2\mathbb N_0.
}
\tag{2.1}
\]

In particular any ordinary-r-mixing spectrum has an **even-integer dyadic logarithmic order** at every point, even when no pointwise power exponent exists.

#### Proof

From `(HS)`, in local coordinates

\[
\log f(t_0+x)=2\log|p(e^{i(t_0+x)})|+w(x),
\qquad w=u+\widetilde v.
\]

The Hilbert transform of a continuous function is VMO, so `w in VMO`. If `m` is the multiplicity of `p` at `zeta`, then

\[
2\log|p(e^{i(t_0+x)})|=2m\log|x|+C+o(1).
\]

Also

\[
A_{2h}(\log x)-A_h(\log x)=\log2.
\]

It remains to show that the adjacent dyadic averages of `w` differ by `o(1)`. Both intervals `[h,2h]` and `[2h,4h]` lie in `[h,4h]`. Their average difference is bounded by an absolute constant times the mean oscillation of `w` on `[h,4h]`, which tends to zero by VMO. The `o(1)` polynomial remainder contributes `o(1)` to both averages. Dividing by `log2` proves `(2.1)`. QED.

This is a theorem-sized self-check, not a finite claim. I found no reason to manufacture a checker for it.

## 3. #12 FIND WHAT IS CONSERVED — r-star smallness forces uniform Riesz bounds on every separated coordinate family

There is a useful exact invariant behind the interlaced coefficient that was not used in the previous power-zero argument.

Let

\[
\sigma^2=\mathbb E|X_0|^2>0,
\qquad \varepsilon=r^*(n)<1,
\qquad R=\frac{1+\varepsilon}{1-\varepsilon}.
\]

### Proposition 3.1 — separated-set Riesz inequality

For every finite set `Lambda subset Z` with pairwise distances at least `n`, and every coefficient vector `(a_k)`,

\[
\boxed{
\frac{1-\varepsilon}{1+\varepsilon}\,\sigma^2\sum_{k\in\Lambda}|a_k|^2
\le
\left\|\sum_{k\in\Lambda}a_kX_k\right\|_2^2
\le
\frac{1+\varepsilon}{1-\varepsilon}\,\sigma^2\sum_{k\in\Lambda}|a_k|^2.
}
\tag{3.1}
\]

#### Proof

Fix an arbitrary sign pattern `eta_k in {+1,-1}` and partition `Lambda=A union B` according to the sign. Put

\[
U=\sum_{k\in A}a_kX_k,
\qquad
V=\sum_{k\in B}a_kX_k.
\]

Because every cross-distance is at least `n`,

\[
|\langle U,V\rangle|\le\varepsilon\|U\|_2\|V\|_2
\le \frac\varepsilon2(\|U\|_2^2+\|V\|_2^2).
\]

Hence both `||U+V||_2^2` and `||U-V||_2^2` lie between

\[
(1-\varepsilon)(\|U\|_2^2+\|V\|_2^2)
\quad\text{and}\quad
(1+\varepsilon)(\|U\|_2^2+\|V\|_2^2),
\]

so changing any chosen sign pattern changes the quadratic form by at most the factor `R`. Average the signed quadratic form over independent fair signs. All off-diagonal terms cancel and the average is exactly

\[
\sigma^2\sum_{k\in\Lambda}|a_k|^2.
\]

Comparing every signed value with the original gives `(3.1)`. QED.

### Corollary 3.2 — decimated alias spectra must flatten

For `Y_j=X_{nj}`, its spectral density is the alias average

\[
F_n(\theta)=\frac1n\sum_{r=0}^{n-1}
 f\!\left(\frac{\theta+2\pi r}{n}\right).
\tag{3.2}
\]

Applying `(3.1)` to every finite trigonometric polynomial yields, a.e.,

\[
\frac{1-\varepsilon}{1+\varepsilon}\sigma^2
\le F_n(\theta)\le
\frac{1+\varepsilon}{1-\varepsilon}\sigma^2.
\tag{3.3}
\]

Thus `r*(n)->0` forces all sufficiently decimated coordinate systems to become uniformly almost orthogonal. This invariant by itself is not enough to decide a continuous one-point zero; ordinary alias Riemann sums can flatten too. It does, however, identify the correct scale on which an interlaced obstruction must live.

## 4. #30 ONE SCALE AT A TIME — an explicit subpower zero with r(n)->0 but r-star bounded away from zero

The previous run proposed the test family

\[
|1-e^{it}|^{2m}\bigl(\log(e/|t|)\bigr)^{-\beta}.
\]

The first genuinely new case is `m=0`, where ordinary Helson--Sarason theory no longer excludes the zero. It can be decided exactly.

For `beta>0`, define on `[-pi,pi]`

\[
 f_\beta(t)=
 \begin{cases}
 \displaystyle\left[\log\!\left(\frac{2e}{|1-e^{it}|}\right)\right]^{-\beta},&t\ne0,\\[1ex]
 0,&t=0.
 \end{cases}
\tag{4.1}
\]

This is continuous, bounded, nonnegative, and positive a.e.; hence it is a legitimate nondegenerate spectral density up to an irrelevant positive normalization.

### Theorem 4.1 — logarithmic zero separates ordinary r from interlaced r-star

For every `beta>0`, any CCWS sequence with spectral density proportional to `(4.1)` satisfies

\[
\boxed{r(n)\to0}
\tag{4.2}
\]

but

\[
\boxed{\liminf_{n\to\infty}r^*(n)\ge\frac13.}
\tag{4.3}
\]

Consequently the obstruction is genuinely interlaced: this continuous one-point **subpower zero passes ordinary r-mixing but fails r-star mixing by a fixed amount**.

#### Step 1: ordinary r(n) tends to zero

Set

\[
w_\beta(t)=\log f_\beta(t)
=-\beta\log\log\!\left(\frac{2e}{|1-e^{it}|}\right)
\qquad(t\ne0).
\]

I first verify `w_beta in VMO(T)`. Since `|1-e^{it}|/|t| -> 1`, the difference between `w_beta(t)` and

\[
w_0(t)=-\beta\log\log\!\left(\frac{2e}{|t|}\right)
\]

extends continuously across `0` after setting the difference to zero there. It is therefore enough to check `w_0`.

Away from zero `w_0` is smooth. Near zero, consider an interval `I` of length `h`.

If `dist(I,0)>=h` and the interval itself approaches zero, the derivative estimate

\[
|w_0'(t)|=\frac{\beta}{|t|\log(2e/|t|)}
\]

gives oscillation `o(1)` because `h/dist(I,0)<=1` while the logarithm diverges. If the interval stays away from zero, uniform continuity applies.

If `dist(I,0)<h`, then `I subset (-2h,2h)`. Put

\[
L_h=\log\frac{2e}{2h}.
\]

For `0<|t|<2h`,

\[
\left|w_0(t)+\beta\log L_h\right|
=\beta\log\left(1+\frac{\log(2h/|t|)}{L_h}\right)
\le \frac{\beta}{L_h}\log\frac{2h}{|t|}.
\]

The average of `log(2h/t)` on `(0,2h)` equals `1`. Since mean oscillation around the interval mean is at most twice the average deviation from any chosen constant, the mean oscillation on such `I` is `O(1/L_h)->0`. Hence `w_beta in VMO`.

Sarason's standard VMO representation gives

\[
w_\beta=u+\widetilde v,
\qquad u,v\in C(\mathbb T).
\]

Therefore `f_beta=exp(u+tilde v)` is a Helson--Sarason representation `(HS)` with `p=1`. Bradley Theorem 6.2 yields `(4.2)`.

#### Step 2: block the process at exactly the zero scale

Fix `M>=1` and define

\[
Y_j^{(M)}=\frac1{\sqrt M}\sum_{s=0}^{M-1}X_{2Mj+s}.
\tag{4.4}
\]

The blocks have length `M` and start `2M` apart. Let

\[
K_M(t)=\frac1M\left|\sum_{s=0}^{M-1}e^{ist}\right|^2
=\frac1M\frac{\sin^2(Mt/2)}{\sin^2(t/2)}
\tag{4.5}
\]

(with the continuous value `K_M(0)=M`). Standard filtering and decimation give the spectral density of the stationary sequence `Y^(M)`:

\[
g_M(\theta)
=\frac1{2M}\sum_{r=0}^{2M-1}
 f_\beta\!\left(\frac{\theta+2\pi r}{2M}\right)
 K_M\!\left(\frac{\theta+2\pi r}{2M}\right),
\tag{4.6}
\]

with arguments read modulo `2pi`.

#### Step 3: exact even/odd fiber formula

Let `H_e` and `H_o` be the closed linear spans of `{Y_{2j}}` and `{Y_{2j+1}}`. Their maximal linear correlation is

\[
\boxed{
\rho_{eo}(g_M)
=\operatorname*{ess\,sup}_{\theta}
\frac{|g_M(\theta)-g_M(\theta+\pi)|}
{g_M(\theta)+g_M(\theta+\pi)}.
}
\tag{4.7}
\]

To see this, fiber `L^2(g_M dtheta)` over the two-point fibers `{theta,theta+pi}`. Even-index trigonometric polynomials have fiber `(a,a)` while odd-index polynomials have fiber `(b,-b)` up to an irrelevant unit phase. The weighted fiber inner product is `(g_M(theta)-g_M(theta+pi))a conjugate(b)`, while both squared norms carry the weight `g_M(theta)+g_M(theta+pi)`. Localization in the base variable gives the essential supremum `(4.7)`.

Now every original index used by an even `Y`-block is at distance at least `M+1` from every original index used by an odd `Y`-block. Therefore every finite even/odd pair of linear combinations is admissible in the definition of `r_X^*(M+1)`, and by density

\[
 r_X^*(M+1)\ge \rho_{eo}(g_M).
\tag{4.8}
\]

#### Step 4: two alias values have a universal 1:2 asymptotic ratio

Put

\[
\ell_M=(\log M)^{-\beta}.
\]

I claim

\[
\boxed{
\frac{g_M(0)}{\ell_M}\to\frac12,
\qquad
\frac{g_M(\pi)}{\ell_M}\to1.
}
\tag{4.9}
\]

For `theta=0`, center the aliases at

\[
t_k=\frac{\pi k}{M},\qquad k\in\mathbb Z
\]

within one period. The `k=0` term vanishes because `f_beta(0)=0`. For every nonzero even `k`, the Fejer numerator `sin^2(pi k/2)` is exactly zero. For each fixed odd `k`,

\[
\frac1{2M}K_M(\pi k/M)
=\frac1{2M^2\sin^2(\pi k/(2M))}
\longrightarrow \frac{2}{\pi^2k^2},
\]

while

\[
\frac{f_\beta(\pi k/M)}{\ell_M}\to1.
\]

Hence the fixed-alias contribution tends to

\[
\frac{2}{\pi^2}\sum_{k\in\mathbb Z,\ k\text{ odd}}\frac1{k^2}
=\frac12.
\]

For `theta=pi`, the aliases are

\[
t_k=\frac{\pi(k+1/2)}{M}.
\]

Here `sin^2(pi(k+1/2)/2)=1/2` for every integer `k`, and for each fixed `k`,

\[
\frac1{2M}K_M(t_k)
\longrightarrow\frac1{\pi^2(k+1/2)^2},
\qquad
\frac{f_\beta(t_k)}{\ell_M}\to1.
\]

Thus the fixed-alias limit is

\[
\frac1{\pi^2}\sum_{k\in\mathbb Z}\frac1{(k+1/2)^2}=1.
\]

For completeness, the passage from fixed aliases to the full finite alias sums is uniform. Split at `|k|<=M^{1/2}`. On this range the log-power ratio is bounded by a constant depending only on `beta`, while the Fejer weights have a summable `C/(1+|k|)^2` envelope; first let a fixed cutoff `K` tend to infinity. On `|k|>M^{1/2}`, the total Fejer weight is `O(M^{-1/2})`, while `f_beta/ell_M <= (log M)^beta` up to a harmless constant, so the normalized tail is

\[
O((\log M)^\beta M^{-1/2})=o(1).
\]

Aliases a fixed positive distance from zero are even smaller: their total normalized contribution is `O((log M)^beta/M)`. This proves `(4.9)`.

Because `g_M` is continuous and positive at these two alias phases, `(4.7)--(4.9)` give

\[
\rho_{eo}(g_M)
\ge
\frac{|g_M(\pi)-g_M(0)|}{g_M(\pi)+g_M(0)}
\longrightarrow
\frac{1-1/2}{1+1/2}=\frac13.
\]

Combining with `(4.8)` proves `(4.3)`. QED.

### What this theorem means

This crosses the boundary the previous report explicitly left open. A noninteger algebraic cusp failed already at ordinary `r(n)`. The logarithmic zero `(4.1)` **does not** fail ordinary `r`; it fails only after interlacing is allowed. Thus Bradley Question 8 cannot be reduced to Helson--Sarason plus a local zero-order quantization rule.

It also shows why one-point continuity is not enough: the obstruction is visible only after simultaneously applying a length-`M` low-frequency filter and a `2M` decimation, then comparing the two parity fibers.

No numerical estimate is used as a theorem endpoint. I did private sanity checks while deriving the alias constants, but the proof above is analytic and self-contained; no numerical value is promoted and no finite checker is required.

## 5. Failure modes / routes eliminated

This run changes the residual problem in three ways.

1. **Pure local order is not the full invariant.** Proposition 2.1 shows that ordinary-r spectra have even dyadic polynomial order, but Theorem 4.1 has order zero and still fails interlaced mixing.
2. **Plain decimation is too weak.** Proposition 3.1 forces alias flattening under r-star mixing, but for a continuous spectrum plain aliases can flatten even when a logarithmic zero remains. The block filter in `(4.4)` is what magnifies the zero to order-one parity imbalance.
3. **The next issue is stability under polynomial zero factors.** The previous run completely classified finite algebraic zeros with a positive continuous remainder; this run shows a subpower zero in the remainder can defeat r-star. The difficult question is what happens to this obstruction after multiplication by a finite squared polynomial factor at the same zero, and more generally which VMO remainders survive all separated-set filter/decimation tests.

## 6. Prior-art/current-literature honesty

The dated bounded search included combinations of:

- exact Bradley Question 8 wording;
- `r*(n)` / interlaced linear dependence + spectral density + zero;
- slowly varying / logarithmic spectral zeros;
- maximal correlation of even/odd subsequences;
- later Bradley and spectral-mixing papers.

It recovered Bradley's 2005 source and generic later uses of rho/rho-star mixing, but no source-matching full characterization and no exact occurrence of `(4.1)--(4.3)` or the parity-block proof. That is **not** a novelty certificate. The even/odd spectral fiber identity and Fejer/alias machinery are classical enough that the mechanism may be known in another language. Priority remains **UNVERIFIED / folklore-adjacent** until a broader specialist search or independent audit says otherwise.

D0036 remains **OPEN / PARTIAL**. No closure audit is requested yet.

## 7. Next route

This run used `3,12,30`; the previous D0036 run used `2,18,25`. The next run must not repeat the present triple.

The changed obligation suggests **#6 DEFORM TO A POINT YOU CAN SOLVE, #11 DUALIZE, #24 FIND THE EXTREMAL OBJECT**:

- **#6:** deform the logarithmic example by multiplying by `|1-e^{it}|^{2m}`, starting with `m=1`, and determine whether a modified block/wavelet test still forces a nonzero r-star lower bound;
- **#11:** rewrite Question 8 as uniform angles between separated coordinate subspaces / Toeplitz Gram operators and identify the dual operator norm encoded by the parity-block construction;
- **#24:** among VMO zero profiles with fixed dyadic order zero, optimize the two-phase alias imbalance and ask whether logarithmic/slowly-varying zeros are extremal or merely convenient witnesses.

A run that only adds more examples with `m=0` is not enough. The next useful result must either survive a nontrivial polynomial factor, produce a necessary operator criterion that sees every separated set, or certify that this route cannot characterize the residual class.

## 8. Structured ledger_delta

```yaml
ledger_delta:
  worker: R14
  lane: HARD_OUTSIDE
  deployment: NEW-METHODS-2026-09-16
  target:
    id: D0036
    source: "Bradley 2005, Question 8"
    status: PARTIAL_OPEN_LOOKING
  continuity:
    negative_margin_perceptron: HANDED_OFF_NOT_REOPENED
    H0017: TERMINAL_HANDOFF_NOT_REOPENED
  fixed_metric:
    name: C_power
    before: 1
    after: 1
    movement: NO
    authoritative_stagnation_count: UNKNOWN
  new_results:
    - "Dyadic log-order quantization under ordinary r(n)->0: local adjacent-scale log-density slope tends to 2m in 2N_0."
    - "Separated-set Riesz inequality from r*(n)<1, hence uniform alias bounds for n-decimation."
    - "For every beta>0, f_beta(t)=[log(2e/|1-e^{it}|)]^{-beta} has r(n)->0 but liminf r*(n)>=1/3."
  result_label: PARTIAL_CERTIFIED_OBSTRUCTION_SELF_CHECK
  finite_claims_requiring_checker: 0
  checker: none
  artifacts_created: []
  audit_ids: []
  priority: UNVERIFIED_FOLKLORE_ADJACENT
  methods_used: [3, 12, 30]
  next_methods: [6, 11, 24]
  remaining_obligation: "Characterize the VMO/subpower residual after finite polynomial factors; determine whether the block-parity obstruction survives m>=1 and isolate a necessary-and-sufficient separated-subspace/Toeplitz criterion for r*(n)->0."
  shared_roots_edited: false
  peer_files_edited: false
  email: false
  drive: false
  public_posting: false
  scheduler_changes: false
```

## 9. Model / scheduler control

Actual model evidence for this run is the report header: **GPT-5.6 Sol; reasoning telemetry UNVERIFIED**. I do not claim GPT-6 maximum.

The exposed task-management surface still does **not** provide a binding model-family selector, reasoning-effort selector, guaranteed hour-long execution field, or authenticated completed-run model telemetry. The prompt can request GPT-6 maximum, but that is not execution proof. Fixing this requires the scheduler/product surface itself to expose model and reasoning controls, or platform support / an owning execution context that can set them.

The historical P26 `You cannot modify this task` failure was authorization-context dependent; later authorized P/C updates succeeded. If a task ID still rejects modification, the legitimate workaround is the authorized owning context, ownership/admin transfer, or platform support — not a permission bypass or a duplicate task.
