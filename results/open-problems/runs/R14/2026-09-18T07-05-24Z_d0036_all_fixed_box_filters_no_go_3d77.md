Model actually ran: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. NO FIXED-METRIC MOVEMENT on D0036: `C_power: 1 -> 1`; authoritative stagnation count remains UNKNOWN. Methods actually used: #4 PROVE SOMETHING WEAKER COMPLETELY, #7 TAKE THE LIMIT, #19 MAKE IT AN ALGORITHM.**

# R14 — Bradley Question 8: every fixed-order box-filter witness is asymptotically phase-blind after an allowed integer zero

Date: 2026-09-18 UTC.  
Repository / branch: `yspennstate/math-open-problems` / `master`.

## 0. Continuity and current source

Repository continuity controls over the stale native task title. I do **not** reopen the negative-margin spherical perceptron, I0089, BIS32, or H0017. The perceptron handoff still preserves the last supported bracket

\[
6.30297437506\le \alpha_c(-1)\le12.78437096216,
\qquad
\alpha_U-\alpha_L=6.48139658710.
\]

H0017 already consumed both hard-task recoveries and was terminally handed off. R14's current exclusive HARD OUTSIDE claim remains `operations/claims/D0036.md`, Richard C. Bradley's 2005 Question 8 on the spectral characterization of `r*(n)->0` for a CCWS sequence.

At the start of this run I reread/recovered the required current state rather than restarting: campaign `INDEX.md` and `RANKING.md`; root `POSTED.md`, `RESULTS.md`, and `QUEUE.md`; the controlling new-methods owner directive; the D0036 claim; the newest R14 report `runs/R14/2026-09-18T05-52-52Z_d0036_bandlimit_alias_no_go_d7a3.md`; the neighboring R08 D0037 polynomial-zero report; the P13 D0036 residual screen; and the current Bradley/intake search hits. The shared ledger still has stale native R14 configuration and explicitly requires recovery of the current complete report before replacing it, so the live D0036 claim controls.

Fresh bounded literature searches dated 2026-09-18 again recovered Bradley's source, where Question 8 explicitly asks for a necessary-and-sufficient spectral-density condition for `r*(n)->0`, and later Bradley work on interlaced mixing, but no source-matching full spectral characterization. This is bounded negative evidence only, not a worldwide openness or priority certificate. No novelty claim is made below.

No shared root, peer file, scheduler, email, Drive, public surface, purchase, permission, or workflow was modified.

## 1. Frozen metric and the exact residual tested this run

The frozen D0036 metric remains

`C_power in {0,1}`,

which moved `0 -> 1` when the finite algebraic-zero family was classified. It is already saturated as a restricted metric and is not replaced to manufacture movement. Hence this run is honestly

**before: `C_power=1`; after: `C_power=1` — NO MOVEMENT.**

The current boundary family is

\[
h_\beta(t)=
\begin{cases}
\displaystyle\left[\log\!\left(\frac{2e}{|1-e^{it}|}\right)\right]^{-\beta},&t\ne0,\\[1ex]
0,&t=0,
\end{cases}
\qquad
f_{m,\beta}(t)=|1-e^{it}|^{2m}h_\beta(t),
\tag{1.1}
\]

with `m>=1`, `beta>0`. The preceding run proved that one broad **fixed-ratio** family of repeated-box filters cannot witness nondecay of `r*` for these spectra when the filter order `q>=m+1`. It left two obvious escape hatches:

1. let the decimation sit only barely beyond the filter support, so the physical separation tends to infinity but `N/M -> q`;
2. use a lower-order box filter `q<=m`, where the integrable tangent-profile argument from the preceding report does not apply.

This run closes **both** escape hatches for every fixed `q`. The result is a route obstruction, not a proof that `f_{m,beta}` is `r*`-mixing.

## 2. Setup: repeated box filtering with arbitrary growing legal gap

Let

\[
D_M(t)=\sum_{s=0}^{M-1}e^{ist}
=\frac{1-e^{iMt}}{1-e^{it}}
\tag{2.1}
\]

(up to the removable values at multiples of `2pi`). Fix an integer `q>=1`; write

\[
D_M(t)^q=\sum_{s=0}^{q(M-1)}c_{M,s}e^{ist}.
\]

Choose any integer sequence `d_M -> infinity` and put

\[
N_M=qM+d_M.
\tag{2.2}
\]

For a CCWS process `X` with spectral density `f_{m,beta}`, define

\[
Z_j^{(M)}=\sum_{s=0}^{q(M-1)}c_{M,s}X_{N_Mj+s}.
\tag{2.3}
\]

The `X`-coordinates entering an even `Z` block and an adjacent odd `Z` block are separated by exactly

\[
N_M-q(M-1)=d_M+q\longrightarrow\infty.
\tag{2.4}
\]

Thus the maximal linear correlation between the even and odd `Z` subspaces is a legitimate candidate lower bound for `r_X^*(d_M+q)`.

Let `g_M` be the spectral density of `Z^(M)`. Filtering and decimation give

\[
g_M(\theta)
=\frac1{N_M}\sum_{r=0}^{N_M-1}
 f_{m,\beta}\!\left(\frac{\theta+2\pi r}{N_M}\right)
 \left|D_M\!\left(\frac{\theta+2\pi r}{N_M}\right)\right|^{2q}.
\tag{2.5}
\]

For any scalar stationary sequence with density `g`, the standard two-fiber calculation gives

\[
\rho_{eo}(g)
=\operatorname*{ess\,sup}_{\theta}
\frac{|g(\theta)-g(\theta+\pi)|}
{g(\theta)+g(\theta+\pi)}.
\tag{2.6}
\]

The goal is therefore to decide whether `(2.5)` retains order-one phase contrast as `M -> infinity`.

## 3. #4 PROVE SOMETHING WEAKER COMPLETELY — the entire fixed-q box family is sterile

### Theorem 3.1 — complete fixed-order repeated-box no-go

Fix `m>=1`, `beta>0`, and an integer `q>=1`. For **every** sequence `d_M -> infinity`, let `N_M=qM+d_M` and let `g_M` be `(2.5)`. Then

\[
\boxed{\rho_{eo}(g_M)\longrightarrow0.}
\tag{3.1}
\]

Consequently no fixed-order repeated-box filter `D_M^q`, with any legal inter-block gap tending to infinity however slowly, can prove that `r^*(n)` fails to tend to zero for `f_{m,beta}`.

The proof has two regimes. Together they exhaust every integer `q`.

## 4. Regime I: `1 <= q <= m` — exact telescoping turns the problem into finite Fourier aliasing

The key identity is exact:

\[
|1-e^{it}|^{2q}|D_M(t)|^{2q}
=|1-e^{iMt}|^{2q}.
\tag{4.1}
\]

Therefore when `q<=m`,

\[
f_{m,\beta}(t)|D_M(t)|^{2q}
=a_{m,q,\beta}(t)\,P_q(Mt),
\tag{4.2}
\]

where

\[
a_{m,q,\beta}(t)
:=|1-e^{it}|^{2(m-q)}h_\beta(t),
\qquad
P_q(x):=|1-e^{ix}|^{2q}.
\tag{4.3}
\]

The function `a_{m,q,beta}` is continuous on the circle, including at `0`. The function `P_q` is a trigonometric polynomial of degree exactly `q`.

Fix `epsilon>0`. By uniform trigonometric approximation, choose a trigonometric polynomial `A_R` of degree `R` such that

\[
\|a_{m,q,\beta}-A_R\|_\infty<\epsilon.
\tag{4.4}
\]

Then `A_R(t)P_q(Mt)` has degree at most `qM+R`. Since `d_M->infinity`, eventually

\[
qM+R<N_M=qM+d_M.
\tag{4.5}
\]

Averaging a trigonometric polynomial of degree strictly less than `N_M` over the `N_M` equally spaced aliases in `(2.5)` kills every nonconstant Fourier mode. Hence

\[
\frac1{N_M}\sum_{r=0}^{N_M-1}
 A_R(t_r)P_q(Mt_r)
\]

is independent of `theta`, where `t_r=(\theta+2\pi r)/N_M`.

The approximation error is uniformly bounded by

\[
\epsilon\,\|P_q\|_\infty\le 4^q\epsilon.
\tag{4.6}
\]

Since `epsilon` is arbitrary,

\[
\operatorname{osc}_\theta g_M(\theta)\longrightarrow0.
\tag{4.7}
\]

It remains only to rule out a vanishing denominator in `(2.6)`. The mean of `g_M` is the variance of `Z_0^(M)` and equals the constant Fourier coefficient of `a(t)P_q(Mt)`. Since `a` is continuous, Riemann--Lebesgue gives

\[
\frac1{2\pi}\int_{-\pi}^{\pi}a(t)P_q(Mt)\,dt
\longrightarrow
\binom{2q}{q}\,rac1{2\pi}\int_{-\pi}^{\pi}a(t)\,dt
=:c_{m,q,\beta}>0.
\tag{4.8}
\]

Thus `g_M` converges uniformly to the positive constant `c_{m,q,beta}`, and `(3.1)` follows in this regime.

This argument is especially transparent at the first unresolved case `m=q=1`:

\[
|1-e^{it}|^2|D_M(t)|^2=|1-e^{iMt}|^2.
\]

The attempted long block inverse does not recover the old `m=0` obstruction; it turns it into a bounded oscillatory multiplier whose aliases flatten once the physical gap `d_M` tends to infinity.

## 5. #7 TAKE THE LIMIT — `q >= m+1`, including the near-Nyquist limit `d_M/M -> 0`

Now assume `q>=m+1`. Put

\[
\ell_M=(\log M)^{-\beta},
\qquad
b_M=M^{2q-2m-1}\ell_M,
\tag{5.1}
\]

and define the integrable tangent profile

\[
\Phi_{m,q}(x)
=|x|^{2m}
\left|\frac{2\sin(x/2)}x\right|^{2q}.
\tag{5.2}
\]

Since `q-m>=1`,

\[
\Phi_{m,q}(x)=O(|x|^{-2(q-m)})
\]

and hence `Phi_{m,q} in L^1(R)`.

For a general decimation `N>=qM+1`, set `lambda=N/M>q` and reindex the aliases by

\[
x_{k,\theta}=\frac{\theta+2\pi k}{\lambda}.
\tag{5.3}
\]

Define

\[
\Psi_M(x)
:=
\frac{f_{m,\beta}(x/M)|D_M(x/M)|^{2q}}
{M^{2q-2m}\ell_M}.
\tag{5.4}
\]

For every fixed compact set,

\[
\Psi_M(x)\longrightarrow\Phi_{m,q}(x)
\tag{5.5}
\]

uniformly, including at `x=0`: away from zero this is ordinary slow variation, while near zero the factor `|x|^{2m}` uniformly suppresses the logarithmic singularity.

The convergence can be summed **uniformly in every `lambda>q`**, not only for a fixed ratio. Indeed, for `|x|<=M^{1/2}` one has a uniform bound

\[
\Psi_M(x)\le C(1+|x|)^{-2(q-m)},
\tag{5.6}
\]

while for `|x|>M^{1/2}` the weaker bound `h_beta/ell_M <= (\log M)^beta` gives

\[
\Psi_M(x)
\le C(\log M)^\beta |x|^{-2(q-m)}.
\tag{5.7}
\]

On a grid of spacing `2pi/lambda`, multiplication by `1/lambda` turns these sums into uniformly bounded Riemann sums. The far-tail contribution in the worst case `q-m=1` is

\[
O((\log M)^\beta M^{-1/2})=o(1),
\tag{5.8}
\]

and the missing part of the infinite tangent periodization beyond the finite alias range is also `o(1)`. Consequently

\[
\boxed{
\sup_{N\ge qM+1}\sup_\theta
\left|
\frac{g_{M,N}(\theta)}{b_M}
-
G_{N/M}(\theta)
\right|\longrightarrow0,
}
\tag{5.9}
\]

where

\[
G_\lambda(\theta)
:=\frac1\lambda\sum_{k\in\mathbb Z}
\Phi_{m,q}\!\left(\frac{\theta+2\pi k}{\lambda}\right).
\tag{5.10}
\]

The preceding report used this periodization only at fixed `lambda>q`. The important new point is the **uniformity in `lambda`**, which includes `lambda_M=q+d_M/M -> q` for an arbitrarily slowly growing physical gap.

Now Fourier duality finishes the argument. The function

\[
s(x)=\frac{2\sin(x/2)}x
\]

has Fourier transform supported in `[-1/2,1/2]`; hence `s(x)^{2q}` has transform supported in `[-q,q]`. Multiplication by `x^{2m}` differentiates the transform but does not enlarge support, so

\[
\operatorname{supp}\widehat{\Phi_{m,q}}\subseteq[-q,q].
\tag{5.11}
\]

The `j`th Fourier coefficient of `(5.10)` is

\[
\frac1{2\pi}\widehat{\Phi_{m,q}}(j\lambda).
\tag{5.12}
\]

For every `lambda>q`, all nonzero coefficients vanish exactly. Therefore

\[
G_\lambda(\theta)
\equiv
C_{m,q}:=\frac1{2\pi}\int_{\mathbb R}\Phi_{m,q}(x)\,dx>0
\quad\text{for every }\lambda>q.
\tag{5.13}
\]

Combining `(5.9)` and `(5.13)` yields

\[
\sup_{N\ge qM+1}\sup_\theta
\left|
\frac{g_{M,N}(\theta)}{b_M}-C_{m,q}
\right|\to0.
\tag{5.14}
\]

In particular it applies to `N_M=qM+d_M` for **every** `d_M->infinity`, even `d_M=o(M)`. Equation `(2.6)` then gives `(3.1)`.

This closes the second regime and proves Theorem 3.1.

## 6. #19 MAKE IT AN ALGORITHM — an exact decision rule for every fixed box order

The proof can be turned into a two-line analytic decision procedure for this witness class.

Input: the polynomial-zero order `m>=1` and a **fixed** repeated-box order `q>=1`.

1. If `q<=m`, use the exact factorization
   \[
   |1-z|^{2m}|D_M(z)|^{2q}
   =|1-z|^{2(m-q)}|1-z^M|^{2q}.
   \]
   The residual factor is continuous. Any legal gap `d_M->infinity` eventually exceeds the degree of an arbitrary fixed trigonometric approximation, so alias averaging kills all phase information.

2. If `q>=m+1`, form the integrable tangent profile `Phi_{m,q}`. Its Fourier bandwidth is at most `q`, while legal separation forces the decimation ratio to satisfy `lambda>q`. Every nonconstant periodization harmonic is therefore sampled outside the bandwidth and vanishes.

Output in both cases: **STERILE as an `r*` nondecay witness.**

There is no third fixed-integer regime. Thus the simple repeated-box program is now completely classified.

No code or exact-arithmetic checker was created: this is an analytic theorem with the full proof on the page, not a finite claim. Building a checker would violate the owner's research-first instruction without adding certification value.

## 7. What this changes, and what it does not

For the first concrete unresolved family

\[
f_{1,1}(t)
=|1-e^{it}|^2
\left[\log\!\left(\frac{2e}{|1-e^{it}|}\right)\right]^{-1},
\tag{7.1}
\]

**every fixed-order box filter `D_M^q`, for every fixed `q>=1`, fails as an interlaced obstruction no matter how the decimation gap `d_M->infinity` is tuned.** This includes the telescoping `q=1` route, the triangular `q=2` route, every higher fixed `q`, proportional gaps, near-critical gaps `d_M=o(M)`, and very large gaps.

This does **not** prove `(7.1)` is `r*`-mixing. It proves that a large and natural constructive counterexample strategy is exhausted. Any future lower-bound witness must leave at least one of the assumptions above. Plausible escape routes are:

- let the box order itself grow, `q=q_M->infinity`, so fixed-order asymptotics no longer apply;
- abandon repeated boxes and use a filter whose tangent mass is not tight at one scale;
- use nonperiodic/asymmetric separated sets rather than an even/odd decimation witness;
- switch direction and prove an upper bound on the angle between arbitrary separated Toeplitz coordinate subspaces.

The fourth option is the only route currently visible that could prove `r*`-mixing rather than merely fail to disprove it.

## 8. Prior-art and source status

Bradley's 2005 source still states Question 8 explicitly. Fresh bounded searches on 2026-09-18 for the exact question, `r*(n)`, interlaced linear dependence, spectral density zeros, and later Bradley work recovered the source and later interlaced-mixing papers but no full source-matching characterization. The 2014 Bradley note on reversible Markov chains shows again that ordinary and interlaced rho-mixing can differ, but it does not answer this spectral question.

I found no exact published statement of Theorem 3.1 in this bounded search. The mechanisms are classical Fourier aliasing, trigonometric approximation, and compact Fourier support, so priority is **UNVERIFIED / folklore-adjacent**. A negative search is not a novelty certificate.

Status remains **PARTIAL / source OPEN-looking under bounded search**. There are `0/2` external audits of the new theorem.

## 9. Stuck-rule consequence

The authoritative stagnation field in the shared ledger remains **UNKNOWN** and is preserved as such. I do not replace it with an invented integer.

However, the three consecutive own immutable D0036 reports after the `0->1` metric movement now each state no fixed-metric movement:

- `2026-09-18T04-50-43Z_d0036_subpower_block_obstruction_a91c.md`;
- `2026-09-18T05-52-52Z_d0036_bandlimit_alias_no_go_d7a3.md`;
- this report.

Therefore, under the owner's Section-I rule, **the next R14 invocation on D0036 must be the first thinking-only stuck recovery**, not another ordinary lemma run, unless an independently supported metric movement appears first. That recovery should write the exact source blocker, route-failure table, simplest unproved special case, nearest solved theorem, and then choose exactly one authorized recovery action.

A sensible next-method triple for that recovery, deliberately different from this run, is **#1 CHANGE THE CATEGORY, #20 FIND WHY THE ALGORITHM FAILS, #28 REPLACE FOR ALL WITH FOR TYPICAL**. The strongest candidate action is to prove the simplest unproved special case `(7.1)` by changing category from block aliases to Toeplitz-subspace angle operators; if that fails, the report should identify the missing uniform operator estimate rather than producing another box-filter lemma.

## 10. Structured ledger_delta

```yaml
ledger_delta:
  worker: R14
  deployment: NEW-METHODS-2026-09-16
  stale_native_title_target:
    source: negative_margin_spherical_perceptron_kappa_minus_1
    reopened: false
    last_supported_bracket: [6.30297437506, 12.78437096216]
    last_supported_width: 6.48139658710
  predecessor_hard_target:
    id: H0017
    status: TERMINAL_HANDOFF
    reopened: false
  active_target:
    id: D0036
    source: Bradley_2005_Question_8
    allocation: HARD_OUTSIDE
    claim: operations/claims/D0036.md
    status: PARTIAL_OPEN_LOOKING_BOUNDED_SEARCH
  fixed_metric:
    name: C_power
    before: 1
    after: 1
    movement: none
    authoritative_stagnation_count: UNKNOWN
  methods_actually_used: [4, 7, 19]
  theorem_this_run:
    name: complete_fixed_order_repeated_box_no_go
    statement: "For every m>=1, beta>0, fixed q>=1 and d_M->infinity, the even/odd maximal correlation of the D_M^q-filtered process decimated by N_M=qM+d_M tends to zero."
    scope: analytic_witness_class_obstruction
    finite_checker_required: false
    audits: 0/2
  route_effect:
    q_le_m: exact_telescoping_plus_trigonometric_alias_flattening
    q_ge_m_plus_1: uniform_tangent_periodization_plus_bandlimit
    excluded_escape: fixed_q_with_arbitrarily_slow_growing_gap
    remaining_routes:
      - q_M_growing
      - non_box_multiscale_filter
      - nonperiodic_asymmetric_separated_sets
      - Toeplitz_subspace_angle_upper_bound
  next_run_protocol: SECTION_I_STUCK_RECOVERY_1_OF_2
  next_methods: [1, 20, 28]
  shared_roots_modified: false
  peer_files_modified: false
```

## 11. Model / scheduler-control truth

The runtime available to this report identifies as **GPT-5.6 Sol**. Reasoning effort is not exposed as authenticated runtime metadata, so it is **UNVERIFIED**. The scheduler/task surface available here still exposes no binding model-family selector, reasoning-effort selector, guaranteed-duration field, or authenticated completed-run telemetry. GPT-6/maximum therefore remains prompt text only and I do not claim it actually ran.

The historical P26 `You cannot modify this task` failure was authorization-context dependent; later P26 modification succeeded from an authorized P/C context. For any ID that still rejects edits, the legitimate workaround is the authorized owning/admin context or platform support, not a permission bypass or duplicate task.
