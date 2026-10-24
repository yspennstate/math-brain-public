Model actually ran: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. NO FIXED-METRIC MOVEMENT on D0036: `C_power: 1 -> 1`; authoritative stagnation count remains UNKNOWN. Methods actually used: #6 DEFORM TO A POINT YOU CAN SOLVE, #11 DUALIZE, #24 FIND THE EXTREMAL OBJECT.**

# R14 — Bradley Question 8: one-scale block witnesses are phase-blind after an integer spectral zero

Date: 2026-09-18 UTC.  
Repository / branch: `yspennstate/math-open-problems` / `master`.

## 0. Continuity, exclusions, and repository read

Repository continuity controls over the stale native task title. I do **not** reopen the negative-margin spherical perceptron, I0089, BIS32, or H0017. The perceptron handoff still preserves the last supported bracket

\[
6.30297437506\le \alpha_c(-1)\le12.78437096216,
\qquad
\alpha_U-\alpha_L=6.48139658710.
\]

H0017 already consumed both permitted hard-task recoveries and was terminally handed off. R14's current exclusive HARD OUTSIDE claim remains `operations/claims/D0036.md`, Bradley Question 8.

At the start of this run I reread/recovered the current campaign state rather than restarting:

- `probability_campaign_2026_09/INDEX.md` and `RANKING.md`;
- root `POSTED.md`, `RESULTS.md`, and `QUEUE.md`;
- `operations/NEW_METHODS_2026-09-16.md` and the controlling owner directive;
- the D0036 claim and newest R14 report `runs/R14/2026-09-18T04-50-43Z_d0036_subpower_block_obstruction_a91c.md`;
- the relevant neighboring Bradley screen in R08 (D0037, polynomial-zero `rho*` closure), the recent R15 successor screens, and the D-intake / attempt material around D0036--D0037.

The shared ledgers still treat the old R14 scheduler title as stale historical configuration and explicitly require recovery of the current complete report before replacing it. I therefore preserve the live D0036 claim and its metric rather than reverting to the perceptron.

No shared root ledger, peer file, scheduler, email, Drive, public surface, purchase, permission, or workflow was modified.

## 1. Source/current-status check and frozen metric

Outside source: Richard C. Bradley, *Basic Properties of Strong Mixing Conditions. A Survey and Some Open Questions*, *Probability Surveys* **2** (2005), 107--144, Section 6.5, **Question 8** (arXiv:math/0511078).

For a centered complex weakly stationary sequence, Bradley's `r*(n)` is the supremum of normalized covariances of finite linear combinations over arbitrary nonempty finite disjoint index sets whose mutual distance is at least `n`; the sets may be interlaced. Question 8 asks for a necessary-and-sufficient condition on the spectral density for `r*(n)->0`.

Fresh bounded searches dated 2026-09-18 again recovered Bradley's source and later work on ordinary/interlaced mixing but no source-matching necessary-and-sufficient answer. In particular, Cohen--Lin, *Results in Mathematics* **81** (2026), article 131, studies Doeblin and ordinary `rho`-mixing for convolution Markov operators on the circle; it does not give the CCWS interlaced-`r*` spectral characterization asked in Question 8. This is bounded negative evidence only, not a worldwide openness or priority certificate.

The frozen R14 metric remains

`C_power in {0,1}`,

which already moved `0 -> 1` when the finite algebraic-zero family was classified. It is saturated as a restricted metric but cannot be replaced merely to manufacture movement. Therefore this run is honestly

**before: `C_power=1`; after: `C_power=1` — NO MOVEMENT.**

The new result is instead a source-relevant analytic obstruction to the most natural next route.

## 2. The boundary family left by the preceding run

The preceding run produced the explicit `m=0` family

\[
h_\beta(t)=
\begin{cases}
\displaystyle\left[\log\!\left(\frac{2e}{|1-e^{it}|}\right)\right]^{-\beta},&t\ne0,\\[1ex]
0,&t=0,
\end{cases}
\qquad \beta>0,
\tag{2.1}
\]

for which ordinary `r(n)->0` but a block-alias construction gives

\[
\liminf_{n\to\infty}r^*(n)\ge\frac13.
\tag{2.2}
\]

The proposed deformation was to insert an allowed integer polynomial zero,

\[
f_{m,\beta}(t)=|1-e^{it}|^{2m}h_\beta(t),
\qquad m\in\mathbb N.
\tag{2.3}
\]

These densities still satisfy ordinary `r(n)->0`: the factor `|1-e^{it}|^{2m}` is exactly an allowed Helson--Sarason polynomial factor, while `\log h_\beta` is VMO as proved in the preceding report. The question is whether the **interlaced** obstruction in (2.2) survives.

This run shows that the entire obvious one-scale block strategy loses its signal as soon as `m>=1`.

## 3. #6 DEFORM TO A SOLVED POINT — the `m=0` point defect disappears at `m=1`

For `M>=1` define

\[
D_M(t)=\sum_{s=0}^{M-1}e^{ist}
=e^{i(M-1)t/2}\frac{\sin(Mt/2)}{\sin(t/2)}.
\]

Fix integers

\[
q\ge m+1,\qquad \lambda>q,
\tag{3.1}
\]

and filter with `D_M^q`, then decimate by `N=\lambda M`. If `c_{M,s}` are the coefficients of `D_M^q`, put

\[
Y_j^{(M)}=\sum_s c_{M,s}X_{\lambda M j+s}.
\tag{3.2}
\]

The coefficient support has diameter `q(M-1)`, so the underlying `X`-coordinates used by an even `Y` block and an odd `Y` block are at mutual distance at least

\[
n_M=\lambda M-q(M-1)=(\lambda-q)M+q\longrightarrow\infty.
\tag{3.3}
\]

Thus the maximal linear correlation between the even and odd `Y` subspaces is a legitimate lower-bound candidate for `r_X^*(n_M)`.

Let `g_M` be the spectral density of `Y^(M)`. Standard filtering and decimation give

\[
g_M(\theta)
=\frac1{\lambda M}\sum_{r=0}^{\lambda M-1}
 f_{m,\beta}\!\left(\frac{\theta+2\pi r}{\lambda M}\right)
 \left|D_M\!\left(\frac{\theta+2\pi r}{\lambda M}\right)\right|^{2q},
\tag{3.4}
\]

with arguments on the circle.

Put

\[
\ell_M=(\log M)^{-\beta},
\qquad
b_M=M^{2q-2m-1}\ell_M,
\tag{3.5}
\]

and define the tangent profile

\[
\Phi_{m,q}(x)
:=|x|^{2m}
\left|\frac{2\sin(x/2)}{x}\right|^{2q},
\tag{3.6}
\]

with the continuous value at zero. For `m>=1`, `\Phi_{m,q}(0)=0`.

### Proposition 3.1 — uniform one-scale alias limit

For every `m>=1`, `beta>0`, `q>=m+1`, and integer `lambda>q`,

\[
\boxed{
\frac{g_M(\theta)}{b_M}
\longrightarrow
G_{m,q,\lambda}(\theta)
:=\frac1\lambda\sum_{k\in\mathbb Z}
\Phi_{m,q}\!\left(\frac{\theta+2\pi k}{\lambda}\right)
}
\tag{3.7}
\]

uniformly in `theta`.

#### Proof

Reindex the aliases in (3.4) by their representative near zero and put

\[
x_{k,\theta}=\frac{\theta+2\pi k}{\lambda},
\qquad
 t_{k,\theta}=\frac{x_{k,\theta}}{M}.
\]

For fixed `x`,

\[
M^{2m}|1-e^{ix/M}|^{2m}\to |x|^{2m},
\tag{3.8}
\]

\[
M^{-2q}|D_M(x/M)|^{2q}
\to
\left|\frac{2\sin(x/2)}x\right|^{2q},
\tag{3.9}
\]

and, for `x\ne0`,

\[
\frac{h_\beta(x/M)}{\ell_M}\to1.
\tag{3.10}
\]

At `x=0`, both the exact term and the proposed limit are zero because `m>=1`. Moreover, multiplication by `|x|^{2m}` makes (3.8)--(3.10) jointly uniform on every compact `x`-interval: first exclude `|x|<delta`, where both sides are `O(delta^{2m})`, then use ordinary uniform slow variation on `delta<=|x|<=K`.

For the tails, on `|t|<=pi`,

\[
|1-e^{it}|\le |t|,
\qquad
|D_M(t)|\le C M\min\{1,|Mt|^{-1}\}.
\tag{3.11}
\]

When `|x|<=M^{1/2}`, the ratio `h_beta(x/M)/ell_M` is bounded uniformly, and the normalized summand is at most

\[
C(1+|x|)^{-2(q-m)}.
\tag{3.12}
\]

This is summable because `q-m>=1`. For `|x|>M^{1/2}`, use only `h_beta<=1`; after division by `ell_M`, the total tail is bounded by

\[
C(\log M)^\beta
\sum_{|k|\gtrsim M^{1/2}} |k|^{-2(q-m)}
=o(1),
\tag{3.13}
\]

with the worst case `q=m+1` giving `O((log M)^beta M^{-1/2})`. The estimates are uniform in `theta`. Compact convergence plus the uniform tails proves (3.7). QED.

The key point is already visible: for `m=0`, the slowly varying factor has a **point defect** at the exact zero (`h_beta(0)=0` while `h_beta(x/M)/ell_M->1` for every fixed `x!=0`). For `m>=1`, the additional factor `|x|^{2m}` makes the tangent profile itself vanish continuously at `x=0`; the point defect disappears.

## 4. #11 DUALIZE — Poisson summation makes the tangent alias spectrum exactly flat

The right side of (3.7) looks phase-dependent. It is not.

Use the Fourier-transform convention

\[
\widehat\varphi(\xi)=\int_{\mathbb R}\varphi(x)e^{-i\xi x}\,dx.
\]

The function

\[
s(x)=\frac{2\sin(x/2)}x
\]

has Fourier transform supported in `[-1/2,1/2]`. Hence `s(x)^{2q}` has Fourier transform supported in `[-q,q]`. Multiplication by `x^{2m}` differentiates the Fourier transform and does not enlarge its support. Therefore

\[
\boxed{
\operatorname{supp}\widehat{\Phi_{m,q}}\subseteq[-q,q].
}
\tag{4.1}
\]

Because `q>=m+1`, `Phi_{m,q}(x)=O(|x|^{-2})` or better, so the periodized sum in (3.7) converges absolutely and uniformly.

### Proposition 4.1 — exact phase blindness

If `lambda>q`, then

\[
\boxed{
G_{m,q,\lambda}(\theta)
\equiv C_{m,q}
:=\frac1{2\pi}\int_{\mathbb R}\Phi_{m,q}(x)\,dx>0.
}
\tag{4.2}
\]

#### Proof

The `j`th Fourier coefficient of `G` is

\[
\begin{aligned}
\frac1{2\pi}\int_0^{2\pi}G(\theta)e^{-ij\theta}\,d\theta
&=\frac1{2\pi\lambda}
\sum_{k\in\mathbb Z}
\int_0^{2\pi}
\Phi_{m,q}\!\left(\frac{\theta+2\pi k}{\lambda}\right)e^{-ij\theta}\,d\theta\\
&=\frac1{2\pi}\int_{\mathbb R}\Phi_{m,q}(x)e^{-ij\lambda x}\,dx\\
&=\frac1{2\pi}\widehat{\Phi_{m,q}}(j\lambda).
\end{aligned}
\tag{4.3}
\]

For every nonzero integer `j`, `|j lambda|>q`, so (4.1) makes (4.3) zero. Only the constant Fourier coefficient survives, giving (4.2). QED.

This is the exact dual obstruction: **the spatial separation condition `lambda>q` is simultaneously the Nyquist inequality that kills every nonconstant Fourier mode of the tangent alias profile.**

## 5. Consequence for the actual interlaced witness

Let `E_M` and `O_M` be the closed linear spans of `{Y_{2j}^{(M)}}` and `{Y_{2j+1}^{(M)}}`. For a scalar stationary sequence with spectral density `g`, the linear maximal correlation between its even and odd subsequences is the standard two-fiber coherence

\[
\rho_{eo}(g)
=\operatorname*{ess\,sup}_{\theta}
\frac{|g(\theta)-g(\theta+\pi)|}
{g(\theta)+g(\theta+\pi)}.
\tag{5.1}
\]

By (3.7) and (4.2), `g_M/b_M -> C_{m,q}` uniformly, with `C_{m,q}>0`. Hence

\[
\boxed{
\rho(E_M,O_M)=\rho_{eo}(g_M)\longrightarrow0.
}
\tag{5.2}
\]

Since (3.3) makes this a valid family of increasingly separated interlaced tests,

\[
r_X^*(n_M)\ge \rho(E_M,O_M),
\]

but the lower bound tends to zero. Thus this entire one-scale route cannot prove non-decay of `r*` for `f_{m,beta}` once `m>=1`.

This is a no-go statement about the witness family, **not** an upper bound on `r_X^*` and not a proof that `f_{m,beta}` is `r*`-mixing.

## 6. Why the preceding `m=0` theorem escapes the no-go

The calculation also explains, rather than merely contrasts with, the preceding `1/3` obstruction.

Take `m=0`, `q=1`, and any integer `lambda>1`. The formal tangent profile is

\[
\Phi_{0,1}(x)=\left|\frac{2\sin(x/2)}x\right|^2,
\]

whose periodization is again constant by the same Fourier-support argument. In fact

\[
\frac1{2\pi}\int_{\mathbb R}\Phi_{0,1}(x)\,dx=1.
\]

However, at `theta=0` the `k=0` alias is **exactly** `t=0`, where `h_beta(0)=0`; the formal tangent profile would have assigned that term the value `Phi_{0,1}(0)=1`. Therefore

\[
\frac{g_M(0)}{\ell_M}\to1-\frac1\lambda,
\qquad
\frac{g_M(\pi)}{\ell_M}\to1.
\tag{6.1}
\]

For each finite `M`, `g_M` is continuous, so these point values still give an essential-supremum lower bound through nearby frequencies. Consequently

\[
\liminf_M \rho_{eo}(g_M)
\ge
\frac{1/\lambda}{2-1/\lambda}
=\frac1{2\lambda-1}.
\tag{6.2}
\]

At `lambda=2`, (6.2) is exactly the preceding run's `1/3` lower bound.

So the `m=0 -> m=1` deformation fails for one very precise reason:

\[
\boxed{
\text{the logarithmic zero creates a single missing alias atom at tangent scale;}
\quad
|1-e^{it}|^{2m},\ m\ge1,\text{ turns that atom into a continuous zero.}
}
\tag{6.3}
\]

## 7. #24 FIND THE EXTREMAL OBJECT — the best admissible leading contrast in this entire family is zero

For fixed `m>=1`, let the one-scale family range over every

\[
q\ge m+1,\qquad \lambda\in\mathbb N,\quad\lambda>q.
\]

The condition `lambda>q` is not cosmetic: it is exactly what makes the two colors' underlying `X` supports separate by a distance tending to infinity. Propositions 3.1 and 4.1 show that for **every** admissible pair `(q,lambda)`, the limiting even/odd phase contrast is zero. Hence

\[
\boxed{
\sup_{q\ge m+1,\ \lambda>q}
\limsup_{M\to\infty}\rho(E_M,O_M)=0.
}
\tag{7.1}
\]

Thus there is no better choice of smoothing order or fixed decimation ratio inside this route.

The same dual mechanism extends beyond Dirichlet powers. If a fixed-shape block filter has rescaled transfer `A(x)` and physical support of asymptotic length `qM`, then its tangent energy after the integer zero is

\[
|x|^{2m}|A(x)|^2.
\]

For a sufficiently regular compactly supported coefficient shape, the Fourier transform of `|A|^2` is its autocorrelation and is supported in `[-q,q]`; multiplying by `x^{2m}` differentiates without enlarging that support. Any decimation ratio `lambda>q` therefore periodizes the tangent energy to a constant exactly as above. So the obstruction is a one-scale **uncertainty/Nyquist phenomenon**, not a peculiarity of the rectangular block.

I record this extension as a route diagnosis rather than promote every regularity variant to a separate theorem. The proved Dirichlet-power statement already rules out the natural compensating filters `D_M^{m+1}`.

## 8. What the three methods actually accomplished

- **#6 DEFORM TO A POINT YOU CAN SOLVE — SUCCESS AS A NO-GO.** The `m=0` logarithmic zero had a fixed `1/3` interlaced obstruction. Deforming to the first allowed polynomial zero `m=1` does not preserve that witness; the exact failure is the removal of the missing-alias point defect.
- **#11 DUALIZE — SUCCESS.** Fourier support / Poisson summation converts the alias computation into the support inclusion `supp hat(Phi) subset [-q,q]`; the same inequality needed for spatial separation forces every nonzero phase mode to vanish.
- **#24 FIND THE EXTREMAL OBJECT — SUCCESS AS A CERTIFIED ROUTE OBSTRUCTION.** Optimizing over all admissible `q>=m+1` and integer `lambda>q` inside the Dirichlet-power one-scale family still gives asymptotic contrast exactly zero.

No exact-arithmetic checker was created because the claims are analytic theorem-sized statements with proofs on the page, not finite computations. This run therefore follows the 90/10 rule instead of manufacturing a certificate for an unchanged metric.

## 9. Remaining obligation and next route

The simplest source-relevant special case still genuinely unresolved by R14 is now very sharp:

\[
\boxed{
 f_{1,\beta}(t)
 =|1-e^{it}|^2
 \left[\log\!\left(\frac{2e}{|1-e^{it}|}\right)\right]^{-\beta},
 \qquad \beta>0:
 \quad r^*(n)\stackrel{?}{\longrightarrow}0.
}
\tag{9.1}
\]

It is ordinary-`r` mixing, the naive logarithmic-zero block obstruction is gone, and the one-scale compensating-filter family above is rigorously sterile. A successful attack must therefore leave the fixed-shape one-scale category. The plausible remaining options are:

1. a genuinely **multiscale / noncompact filter** whose rescaled transfer does not have a single compact Fourier-support window;
2. an **upper bound** proving that every separated coefficient pair for (9.1) has vanishing weighted Toeplitz angle;
3. a counterexample witness using many alternating scales rather than translates of one block shape.

The next deliberately different Section-B triple is **#4 PROVE SOMETHING WEAKER, COMPLETELY; #7 TAKE THE LIMIT; #19 MAKE IT AN ALGORITHM**:

- #4: decide the fixed `m=1, beta=1` case of (9.1), without pretending that this solves Question 8;
- #7: derive the continuum scaling problem for multiscale separated coefficient arrays in the weighted Sobolev form `|x|^2/log(1/|x|)`;
- #19: formulate the finite generalized-eigenvalue problem for two- or three-scale separated supports to discover a candidate analytic extremizer. Any resulting numerics remain numerics until converted to a proof.

If the fixed metric remains unchanged for the owner-defined stuck threshold, the next invocation must follow Section I rather than accumulate more lemmas.

## 10. Prior-art / priority status

The dated search included:

- exact Bradley Question 8 / `r*(n)` / interlaced linear dependence / spectral density;
- spectral zeros and finite polynomial filters;
- slowly varying / logarithmic spectral zeros;
- recent 2026 work on `rho`-mixing and spectra of Markov/convolution operators.

No exact published match for the one-scale bandlimit cancellation statement above was located in that bounded search. The mechanism itself is elementary Poisson summation / compact Fourier support and may well be folklore. Therefore **priority is UNVERIFIED / folklore-adjacent** and no novelty claim is made.

D0036 remains **OPEN / PARTIAL**. Nothing here is labeled PROVED at the source level, and there are `0/2` external closure audits because no source closure is claimed.

## 11. Structured ledger_delta

```yaml
ledger_delta:
  worker: R14
  deployment: NEW-METHODS-2026-09-16
  stale_native_source:
    target: negative-margin spherical perceptron kappa=-1
    reopened: false
    last_supported_bracket_width: 6.48139658710
  prior_hard_target:
    id: H0017
    status: TERMINAL_HANDOFF
    reopened: false
  active_target:
    id: D0036
    source: "Bradley 2005, Question 8"
    lane: HARD_OUTSIDE
    ownership: EXCLUSIVE_R14
    status: PARTIAL
    worldwide_open_status: OPEN_CURRENT_BOUNDED
    priority: UNVERIFIED_FOLKLORE_ADJACENT
    metric:
      name: C_power
      before: 1
      after: 1
      movement: false
    authoritative_stagnation_count: UNKNOWN
    result_this_run: "For m>=1, every admissible one-scale D_M^q / lambda M parity-block witness with q>=m+1 and lambda>q has asymptotically flat alias spectrum; its even/odd correlation tends to 0. The m=0 logarithmic obstruction escapes only through the exact missing t=0 alias atom."
    source_closed: false
    external_audits: "0/2"
  methods_used: [6, 11, 24]
  next_methods: [4, 7, 19]
  finite_checker_required: false
  shared_roots_modified: false
  peer_files_modified: false
```

## 12. Model / scheduler-control truth

The model request in the prompt is not an execution control in this environment. The actual model exposed to this run is **GPT-5.6 Sol**; reasoning telemetry is **UNVERIFIED**, so I do not claim GPT-6 or maximum reasoning.

The currently exposed task-management schema still offers title, prompt, schedule / relative start, timing mode, and enablement. It exposes **no binding model-family field, no reasoning-effort field, no guaranteed-duration field, and no authenticated completed-run model telemetry**. Making GPT-6/maximum enforceable therefore requires a scheduler/product execution surface that actually exposes those fields, or an authorized platform-side change to the execution configuration; prompt text alone cannot do it.

The repository's current reconciliation also clarifies the historical P26 `You cannot modify this task` event: P26 later **did** update successfully from an authorized P/C context, while other contexts still denied edits to inaccessible IDs (including the R-series). The legitimate workaround for a task that still rejects modification is the authorized owning account/workspace/context, an ownership/admin transfer through the supported interface, or platform support. A GitHub edit, duplicate task, or permission bypass is not a scheduler repair.
