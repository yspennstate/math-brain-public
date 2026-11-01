Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. Fixed I0084 metric `2/2 -> 2/2` (NO MOVEMENT in the frozen alpha=1/2 source-case count); genuine theorem progress: exact-`(2+alpha)`-moment mode-location asymptotics for every interior classical/free-stable ordinary-`*` branch, plus an all-orders expansion for the classical-Brownian half of Hasebe--Ueda Problem 4.6 under its full exponential-square source hypothesis. Section-B moves: #5 ADD A PARAMETER AND DIFFERENTIATE IN IT, #12 FIND WHAT IS CONSERVED, #29 ADD THE POINTS AT INFINITY. These are second-cycle reuses because all 30 moves were already exhausted historically; the immediately preceding C022 triple was #2/#24/#30, so the preceding triple is not repeated.**

Problem/source: Takahiro Hasebe and Yuki Ueda, *Large time unimodality for classical and free Brownian motions with initial distributions*, arXiv:1710.08240v2, Conjecture 5.5 / intake I0084.

Status: **SOURCE REFUTED MATHEMATICALLY already at alpha=1/2 because the source permits extremal skewness; repository status remains PARTIAL / AUDIT_PENDING. New this run: R19-I0084-C023A/B/C are CANDIDATE THEOREMS / PROVED INTERNALLY / AUDIT PENDING. No source-level closure promotion is claimed.**

# 1. Continuity, source convention, and what is genuinely new

I resumed from the actual latest R19 report

`runs/R19/2026-09-20_04-45-51_UTC__i0084-critical-moment-sharpness_c022_m2e24s30.md`

at creation commit `f75b511b645eb578b81154edb625204332c4902f`. An exact repository comparison to the current pre-write head found 161 intervening commits and no later R19 report. I re-read the campaign INDEX/RANKING, root POSTED/RESULTS/QUEUE, the latest R19 theorem package, neighboring activity, the intake history, and the later progress-first owner directive. That later directive keeps the 90/10 mathematics-first rule and explicitly permits a genuine structural theorem even when the frozen headline metric is already saturated.

The primary source was checked again directly in arXiv v2. Conjecture 5.5 says that `S_t` may be the law of a **classical or free alpha-stable process**, assumes exactly

\[
\int_{\mathbb R}|x|^{2+\alpha}\,d\mu(x)<\infty,
\]

and concludes eventual unimodality of

\[
\boxed{\mu*S_t}.
\]

Thus `*` below is **ordinary classical convolution even when `S_t` is the law of a free stable process**. I do not replace it by `\boxplus`.

The preceding C022 run proved internally that the source exponent `2+alpha` is sharp in power-moment order throughout the two-sided/interior region. The new question in this run is different: once eventual unimodality is known, can the same exact source moment condition determine the large-time **location of the unique mode** rather than merely its existence?

The answer below is yes. The expansion is also directly relevant to Hasebe--Ueda Problem 4.6. Existing campaign work had only compact-support asymptotics for that mode-location question; the source itself assumes an exponential-square moment. C023C extends the **classical Brownian half** from compact support to the full source exponential-square class and produces all algebraic orders. I do **not** label all of Problem 4.6 solved, because its free-Brownian half remains separate and the source asks programmatically to “estimate” the mode rather than specifying a single closure norm/order.

# 2. Three new-method moves

## Move #5 — ADD A PARAMETER AND DIFFERENTIATE IN IT

Introduce the inverse dilation `q=1/s` and write the rescaled smoothed density as

\[
F_q(u)=\mathbb E\,k(u-qY).
\]

At `q=0`, the distribution collapses to the explicit kernel `k`; the mode equation becomes a perturbative implicit equation around the kernel mode. This creates a genuine deformation parameter in which the critical-point equation can be solved coefficient by coefficient.

## Move #12 — FIND WHAT IS CONSERVED

After separating the mean `a=E[Y]`, the first corrections are controlled only by the centered moments

\[
\sigma^2=E[(Y-a)^2],\qquad \kappa_3=E[(Y-a)^3],\ldots
\]

and local derivatives of the kernel at its mode. In particular, the mean appears as an exact `O(1)` translation, the variance controls the first `1/s` correction, and the third centered moment controls the next `1/s^2` correction. This moment hierarchy is the invariant bookkeeping hidden inside the large-time smoothing problem.

## Move #29 — ADD THE POINT AT INFINITY

Large time `s=infinity` becomes the finite boundary point `q=0`. Uniform convergence

\[
F_q\to k\quad\text{in }L^\infty
\]

forces every global mode of `F_q` into the unique kernel-mode neighborhood, after which local Taylor expansion is legitimate. This converts the global question “where can a remote mode hide?” into a local implicit-function problem at the compactified boundary `q=0`.

# 3. R19-I0084-C023A — mode expansion for an arbitrary wide kernel

**STATUS: PROVED INTERNALLY / AUDIT PENDING.**

Let `k` be a probability density on `R` such that:

1. `k in C_0(R)` and `k'` is bounded;
2. `k` has a unique global maximizer `m`;
3. `k` is sufficiently smooth near `m`, with
   \[
   A:=k''(m)<0.
   \]

For `s>0` set

\[
k_s(x)=s^{-1}k(x/s).
\]

Let `Y` have law `mu`, let

\[
a=E[Y],\qquad Z=Y-a,
\]

and let `M_s` be any global maximizer of

\[
f_s=\mu*k_s.
\]

The first claim is that, under the finite first moment assumption,

\[
\boxed{M_s=sm+a+o(1).}\tag{C023.1}
\]

With additional moments one obtains a full algebraic expansion. In particular, if `E|Y|^3<infinity` and `k` has four derivatives near `m`, then

\[
\boxed{
M_s
=sm+a-
\frac{k'''(m)}{2k''(m)}\frac{\sigma^2}{s}
+rac{k''''(m)}{6k''(m)}\frac{\kappa_3}{s^2}
+o(s^{-2})
}\tag{C023.2}
\]

provided the displayed orders are supported by the available moment; more generally the coefficient recursion below gives every integer order allowed by the corresponding absolute moment.

The exact source-moment fractional refinement needed later is:

- if `2<p<3` and `E|Y|^p<infinity`, then
  \[
  M_s=sm+a-
  \frac{k'''(m)}{2k''(m)}\frac{\sigma^2}{s}
  +o(s^{-(p-1)});\tag{C023.3}
  \]
- if `3<=p<4` and `E|Y|^p<infinity`, then
  \[
  M_s=sm+a-
  \frac{k'''(m)}{2k''(m)}\frac{\sigma^2}{s}
  +\frac{k''''(m)}{6k''(m)}\frac{\kappa_3}{s^2}
  +o(s^{-(p-1)}).\tag{C023.4}
  \]

Here `sigma^2=E[Z^2]` and `kappa_3=E[Z^3]`.

## Step 1: every global mode is forced to the kernel mode

Define

\[
F_s(u):=s f_s(su)=\mathbb E\,k(u-Y/s).
\]

Because `k in C_0(R)`, it is uniformly continuous. Hence

\[
\|F_s-k\|_\infty
\le \mathbb E\,\|\tau_{Y/s}k-k\|_\infty\longrightarrow0
\]

by dominated convergence. Since `m` is the unique global maximizer of `k`, any global maximizer `u_s=M_s/s` of `F_s` satisfies

\[
u_s\to m.\tag{C023.5}
\]

Write

\[
M_s=sm+r_s,
\]

so `r_s=o(s)`.

## Step 2: the `O(1)` translation is exactly the mean

The mode is an interior critical point for all sufficiently large `s`, so

\[
0=\mathbb E\,k'\!\left(m+\frac{r_s-Y}{s}\right).\tag{C023.6}
\]

Near `m`, write

\[
k'(m+h)=Ah+\eta(h),\qquad \eta(h)=o(h).
\]

Fix a small `delta>0` and split the expectation into

\[
|Y|\le \delta s/2
\quad\text{and}\quad
|Y|>\delta s/2.
\]

Since `r_s=o(s)`, on the central event the Taylor form is valid for large `s`, and for every `epsilon>0`,

\[
s\,\mathbb E|\eta((r_s-Y)/s)|
\le \epsilon\bigl(|r_s|+E|Y|\bigr).
\]

On the tail, boundedness of `k'` and `E|Y|<infinity` give

\[
s\,P(|Y|>\delta s/2)\to0,
\qquad
E[|Y|;|Y|>\delta s/2]\to0.
\]

Multiplying (C023.6) by `s` therefore yields

\[
A(r_s-a)=o(1)+o(|r_s|).
\]

Choosing the local Taylor tolerance strictly below `|A|/2` first shows `r_s` is bounded, and then the error tends to zero. Thus

\[
r_s\to a,
\]

which proves (C023.1).

# 4. Coefficient recursion and the first two corrections

Put

\[
\delta_s:=r_s-a,\qquad q=s^{-1}.
\]

Then (C023.6) becomes

\[
0=E\,k'(m+q(\delta_s-Z)).\tag{C023.7}
\]

Suppose first that enough moments exist for an integer expansion. Write formally

\[
\Delta(q)=\sum_{n\ge1}c_nq^n.
\]

Taylor expansion gives the coefficient equation

\[
0=A\Delta(q)
+\sum_{j\ge2}
\frac{k^{(j+1)}(m)}{j!}
q^j E[(\Delta(q)-Z)^j].\tag{C023.8}
\]

After division by `q`, equivalently

\[
0=A\frac{\Delta(q)}q
+\sum_{j\ge2}
\frac{k^{(j+1)}(m)}{j!}
q^{j-1}E[(\Delta(q)-Z)^j].\tag{C023.9}
\]

At each order only `A c_n` contains the new coefficient `c_n`, so the recursion is triangular and unique.

At order `q`,

\[
Ac_1+\frac{k'''(m)}2\sigma^2=0,
\]

hence

\[
\boxed{c_1=-\frac{k'''(m)}{2k''(m)}\sigma^2.}\tag{C023.10}
\]

At order `q^2`, the quadratic term contributes no new centered odd moment because `E[Z]=0`, while the cubic term contributes `-k''''(m)\kappa_3/6`. Thus

\[
Ac_2-\frac{k''''(m)}6\kappa_3=0,
\]

so

\[
\boxed{c_2=\frac{k''''(m)}{6k''(m)}\kappa_3.}\tag{C023.11}
\]

This proves the displayed coefficients in (C023.2).

## Remainder control with only a fractional moment

The point relevant to I0084 is that no stronger moment than the source exponent is required.

Let `p>2`. A local Taylor remainder `R(h)` satisfying

\[
R(h)=o(|h|^p)
\]

can be averaged at `h=(\delta_s-Z)/s` under the sole condition `E|Z|^p<infinity`. Indeed, split at `|\delta_s-Z|<=epsilon s`. On the central region the `o(|h|^p)` bound gives an arbitrarily small multiple of `s^{-p}E|\delta_s-Z|^p`. On the complement, boundedness of `k'` plus uniform integrability of `|Z|^p` gives

\[
s^pP(|Z|>cs)\to0,
\]

and for every `j<=p` in the needed polynomial terms,

\[
s^{p-j}E[|Z|^j;|Z|>cs]\to0.\tag{C023.12}
\]

For `2<p<3`, expand `k'` through the quadratic term; smoothness gives an `O(h^3)=o(|h|^p)` remainder. Equation (C023.7), multiplied by `s`, becomes

\[
0=A\delta_s
+\frac{k'''(m)}{2s}(\sigma^2+\delta_s^2)
+o(s^{-(p-1)}).
\]

First this yields `delta_s=O(s^{-1})`; substituting back proves (C023.3).

For `3<=p<4`, expand through the cubic term. At `p=3` use the ordinary `o(h^3)` Taylor remainder; for `p>3`, the `O(h^4)` remainder is `o(|h|^p)`. Then

\[
\begin{aligned}
0={}&A\delta_s
+\frac{k'''(m)}{2s}(\sigma^2+\delta_s^2)\\
&+\frac{k''''(m)}{6s^2}
(\delta_s^3+3\delta_s\sigma^2-\kappa_3)
+o(s^{-(p-1)}).
\end{aligned}\tag{C023.13}
\]

Using `delta_s=O(s^{-1})`, the nonlinear terms not displayed in (C023.4) are `O(s^{-3})`, which is `o(s^{-(p-1)})` because `p<4`. Solving the remaining triangular equations gives (C023.4).

This completes C023A.

# 5. R19-I0084-C023B — exact-source-moment mode asymptotics for stable kernels

**STATUS: PROVED INTERNALLY from C023A plus the retained C018--C021 stable-kernel geometry; AUDIT PENDING.**

Fix `0<alpha<2` and an **interior/two-sided** stable skewness in either frozen source branch:

1. a classical alpha-stable process, or
2. a free alpha-stable process whose time law is used as a kernel under ordinary classical convolution `*`.

The retained C018--C021 package proves internally that the time-one density has a unique nondegenerate mode `m`, is smooth, and has enough tail/derivative control for the C008 eventual-unimodality theorem. Write the time law in the convention-preserving affine form

\[
S_t\stackrel d=b_t+s_tX,
\qquad s_t=t^{1/\alpha},\tag{C023.14}
\]

where `b_t` contains the ordinary drift/location correction and, at `alpha=1`, the usual logarithmic centering term. This formula is deliberately left in affine form so no skewness convention is silently changed.

Let `M_t` denote the eventual unique mode of `mu*S_t`, and suppose exactly the source hypothesis

\[
E|Y|^{2+\alpha}<\infty.\tag{C023.15}
\]

Set `a=E[Y]`, `sigma^2=Var(Y)` and, when `alpha>=1`, `kappa_3=E[(Y-a)^3]`. Applying C023A with

\[
p=2+\alpha
\]

gives:

### `0<alpha<1`

Since `2<p<3`,

\[
\boxed{
M_t=b_t+s_tm+a
-\frac{k'''(m)}{2k''(m)}\frac{\sigma^2}{s_t}
+o(s_t^{-1-\alpha}).
}\tag{C023.16}
\]

### `1<=alpha<2`

Since `3<=p<4`,

\[
\boxed{
M_t=b_t+s_tm+a
-\frac{k'''(m)}{2k''(m)}\frac{\sigma^2}{s_t}
+\frac{k''''(m)}{6k''(m)}\frac{\kappa_3}{s_t^2}
+o(s_t^{-1-\alpha}).
}\tag{C023.17}
\]

No compact-support hypothesis and no moment above the source's exact `2+alpha` exponent is used.

For the frozen `alpha=1/2` target, `s_t=t^2`, so every interior branch satisfying the exact source `5/2` moment has

\[
\boxed{
M_t=b_t+t^2m+a
-\frac{k'''(m)}{2k''(m)}\sigma^2 t^{-2}
+o(t^{-3}).
}\tag{C023.18}
\]

This is new structural information inside the already saturated `2/2` frozen source-case metric; it earns no extra source-case count.

# 6. R19-I0084-C023C — classical Brownian mode expansion under the full Problem 4.6 source class

**STATUS: PROVED INTERNALLY / PARTIAL relative to the two-branch Problem 4.6 / AUDIT PENDING.**

Hasebe--Ueda Problem 4.6 assumes that for some `epsilon>0`,

\[
\int e^{\epsilon x^2}\,d\mu(x)<\infty,\tag{C023.19}
\]

and asks to estimate the mode position for classical Brownian motion, followed by the analogous free-Brownian question. Existing campaign work obtained compact-support `O(1/t)` asymptotics. Condition (C023.19) supplies every absolute moment, so C023A removes the compact-support restriction for the **classical** half and gives an all-orders algebraic expansion.

For the standard Gaussian kernel

\[
\phi(x)=(2\pi)^{-1/2}e^{-x^2/2},
\]

the kernel mode is `m=0`, and

\[
\phi''(0)=-\phi(0),\qquad
\phi'''(0)=0,\qquad
\phi''''(0)=3\phi(0).
\]

The critical equation can be written exactly as

\[
E\Big[(\delta-Z)e^{-(\delta-Z)^2/(2t)}\Big]=0,
\qquad
\delta=M_t-a.\tag{C023.20}
\]

Because the Gaussian depends on `1/t`, only integer powers of `1/t` occur. Write

\[
\delta=d_2t^{-1}+d_4t^{-2}+O(t^{-3}).
\]

Expanding (C023.20) gives at order `t^{-1}`

\[
d_2+\frac{\kappa_3}{2}=0,
\]

and at order `t^{-2}`

\[
d_4-\frac32d_2\sigma^2-\frac{\kappa_5}{8}=0.
\]

Therefore

\[
\boxed{
M_t
=a-\frac{\kappa_3}{2t}
+\left(
\frac{\kappa_5}{8}-\frac{3\sigma^2\kappa_3}{4}
\right)t^{-2}
+O(t^{-3})
}\tag{C023.21}
\]

under the exponential-square source condition. Continuing the same triangular expansion gives every algebraic order, with coefficients polynomial in the centered moments of `mu`.

This is a genuine strengthening of the repository's previous compact-support mode asymptotics, but it is **not** promoted to a full solution of Problem 4.6 because:

- the source also asks for the free-Brownian mode;
- the source uses the programmatic word “estimate” rather than fixing one target order or norm;
- no independent audit of this extension exists yet.

# 7. Stress tests and failure modes considered

The proof above was built to survive three common gaps.

1. **Local critical point versus global mode.** The uniform convergence `F_s -> k` is what first traps every global maximizer near the unique kernel mode. The Taylor argument is not started until that global step is complete.

2. **Unbounded input support.** The source moment is used through uniform integrability rather than compact support. Tail terms are controlled after splitting at distance proportional to `s`; no bounded-support substitution is made.

3. **Fractional source exponent.** For `p=2+alpha` one cannot simply demand the next integer moment. The remainder argument is explicitly formulated in `L^p`, so for `alpha<1` only the variance correction is asserted and for `alpha>=1` the third centered moment correction is asserted, exactly at the moment strength supplied by the source.

# 8. Prior-art check and novelty qualification

Fresh bounded 2026-09-20 searches were run for:

- exact arXiv `1710.08240`, Conjecture 5.5 and later Hasebe/Ueda work;
- eventual stable-convolution unimodality under the `(2+alpha)` moment;
- mode asymptotics of stable convolutions at large time;
- kernel-smoothed density mode bias and asymptotic mode estimation.

I did not locate a later primary theorem resolving the exact frozen arXiv-v2 ordinary-`*` Conjecture 5.5 or stating the stable-process corollary C023B. That is bounded negative evidence only, **not** a novelty certificate.

The abstract perturbative mechanism in C023A is clearly adjacent to classical kernel-density mode-bias theory; the literature search surfaced Romano (1988), *On weak convergence and optimality of kernel density estimates of the mode*, and later kernel-mode estimation work. Accordingly, I do **not** claim that the generic expansion principle itself is new. The campaign-level new content claimed here is narrower: its exact-moment application to the retained stable-kernel package, and the extension of the classical Problem 4.6 mode expansion from the repository's compact-support result to the full exponential-square source class.

# 9. Audit and closure state

The fixed source metric remains

\[
\boxed{2/2\to2/2.}
\]

The frozen source is still mathematically refuted internally because extremal skewness is allowed and the retained C011/C017 endpoint construction supplies all-polynomial-moment, all-time counterexamples. But repository closure remains **PARTIAL / AUDIT_PENDING**.

Relevant retained independent evidence includes:

- `R18-AUDIT-R19-I0084-C008-ABSTRACT-003 = PASS_FULL_MATHEMATICAL_PROOF` for the abstract eventual-unimodality engine;
- the historical R18 classical half-stable finite/symbolic audit;
- P26/R18 audits of narrower C010/C002 components, with C002's end-to-end pass belonging to the different ALEA free-`boxplus` formulation rather than the frozen arXiv ordinary-`*` package.

The required version-matched end-to-end frozen-package P26 pass plus a distinct second outside-track pass are still not located. C021, C022 and C023 also have not yet received independent theorem-level audits. No finite arithmetic claim was introduced in C023, so no checker was manufactured merely for bookkeeping; the validation object is the full analytic proof above.

# 10. Model/control status

The available scheduler/task-control surface still exposes task identity/title, prompt, schedule/timing mode, enabled state and ordinary update fields, but no binding model-family selector, no binding reasoning-effort selector, no authenticated applied-model/effort receipt and no guaranteed one-hour execution field. Therefore GPT-6/maximum remains a prompt request rather than an authenticated runtime setting in this context.

Making that requirement enforceable would require a scheduler/product/API surface that persists explicit model-family and reasoning-effort fields and returns a per-run attestation of what was actually applied. The historical P26 `You cannot modify this task` event was authorization-context-specific; the repository later records a context in which the full P26 update succeeded. The supported workaround is therefore the owning/authorized context, ordinary permission/ownership repair or platform support, not a bypass. This R19 run made no scheduler changes, as required.

# ledger_delta

```yaml
ledger_delta:
  track: R19
  source: "Takahiro Hasebe and Yuki Ueda, arXiv:1710.08240v2, Conjecture 5.5 / I0084"
  source_version_scope: "frozen arXiv v2: ordinary classical convolution mu*S_t for both classical-stable and free-stable kernel laws; exact (2+alpha)-moment; original skewness conventions"
  fixed_metric:
    name: "number of complete classical-stable/free-stable alpha=1/2 source cases proved"
    before: "2/2"
    after: "2/2"
    movement: "NO MOVEMENT"
    unchanged_count: "UNKNOWN/UNMEASURED preserved; not reset merely by a structural theorem"
  status_before: "PARTIAL / AUDIT_PENDING; mathematical source refutation internal"
  status_after: "PARTIAL / AUDIT_PENDING; mathematical source refutation internal"
  tried_moves: [5, 12, 29]
  previous_move_triple: [2, 24, 30]
  new_claims:
    - id: "R19-I0084-C023A"
      status: "PROVED_INTERNALLY_AUDIT_PENDING"
      statement: "global mode expansion for wide kernels, with fractional-moment remainder control"
    - id: "R19-I0084-C023B"
      status: "PROVED_INTERNALLY_AUDIT_PENDING"
      statement: "exact-(2+alpha)-moment mode-location expansion for every interior classical/free-stable ordinary-* branch"
    - id: "R19-I0084-C023C"
      status: "PROVED_INTERNALLY_PARTIAL_FOR_PROBLEM_4_6_AUDIT_PENDING"
      statement: "classical Brownian mode has an all-orders 1/t expansion under the full exponential-square Problem 4.6 source hypothesis"
  retained_source_verdict: "Conjecture 5.5 frozen arXiv scope is mathematically refuted internally because extremal skewness is allowed"
  remaining_obligation:
    - "independent mathematical audit of C021-C023"
    - "version-matched P26 end-to-end audit of the full frozen ordinary-* package"
    - "distinct second end-to-end outside-track audit of the same full package"
    - "no claim that the free-Brownian half of Problem 4.6 is solved"
  evidence:
    - "predecessor report runs/R19/2026-09-20_04-45-51_UTC__i0084-critical-moment-sharpness_c022_m2e24s30.md @ f75b511b645eb578b81154edb625204332c4902f"
    - "primary arXiv v2 Conjecture 5.5 rechecked: ordinary mu*S_t in both branches"
    - "progress-first owner directive operations/progress_first_2026-09-20/OWNER_DIRECTIVE.md"
    - "P0177 repository history: compact-support mode asymptotics only; full exponential-square class previously untouched"
  audit_ids:
    - "R18-AUDIT-R19-I0084-C008-ABSTRACT-003=PASS_FULL_MATHEMATICAL_PROOF"
    - "R18-I0084-C001=PASS [narrow classical alpha=1/2 finite/symbolic core]"
    - "R18-AUDIT-R19-I0084-C010-ABSTRACT-004=PASS_FULL_MATHEMATICAL_PROOF [C010 only]"
    - "historical C002 end-to-end audits are ALEA free-boxplus scope, not frozen ordinary-* scope"
  finite_claim_checker: "NOT_APPLICABLE; C023 is analytic/infinite-dimensional and is proved on the page"
  shared_roots_edited: false
  email_drive_public_posting_scheduler_changes: false
```
