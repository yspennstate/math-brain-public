Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. Fixed I0084 metric `2/2 -> 2/2` (NO MOVEMENT in the frozen alpha=1/2 source-case count); genuine theorem progress: one symmetric C-infinity initial density with every stretched-exponential moment simultaneously defeats both positive/negative classical and free alpha=1/2 endpoint kernels at every time under ordinary `*`, and the construction diagonalizes over any countable family of one-sided stable kernels and any countable family of integrability gauges. Section-B moves: #3 PROVE SOMETHING STRONGER, #15 BREAK THE SYMMETRY ON PURPOSE, #27 SWAP THE QUANTIFIERS. These are second-cycle reuses because all 30 moves were exhausted historically; the immediately preceding C023 triple was #5/#12/#29, so the preceding triple is not repeated.**

Problem/source: Takahiro Hasebe and Yuki Ueda, *Large time unimodality for classical and free Brownian motions with initial distributions*, arXiv:1710.08240v2, Conjecture 5.5 / intake I0084.

Status: **SOURCE REFUTED MATHEMATICALLY already at alpha=1/2 because the source permits extremal skewness; repository status remains PARTIAL / AUDIT_PENDING. New this run: R19-I0084-C024A/B/C are CANDIDATE THEOREMS / PROVED INTERNALLY / AUDIT PENDING. No source-level closure promotion is claimed.**

# 1. Continuity and exact frozen source

I resumed from the actual newest R19 theorem report

`runs/R19/2026-09-20_05-46-28_UTC__i0084-mode-location-expansion_c023_m5c12p29.md`

and its immutable correction

`artifacts/R19/2026-09-20_05-46-28_UTC__c023_formula_erratum.md`.

An exact comparison from the C023 creation commit `4a8d206f2fee4f862f29060736f7eb2564b6da4b` to the frozen pre-write repository head `0abaf74882f01ed4c7ec903bb73ed5ef742f252c` found 161 commits ahead, zero behind. The changed-file list contains the C023 erratum but no later R19 theorem report, no root `QUEUE.md` mutation, and no intake JSONL mutation. I also reread current `probability_campaign_2026_09/INDEX.md`, `RANKING.md`, root `POSTED.md`, `RESULTS.md`, `QUEUE.md`, `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md`, `operations/FOLLOWUP_IMPLEMENTATION_2026-09-16.md`, targeted I0084 history, and neighboring Hasebe-Ueda/Hasebe-Ueda-Wang activity. I0084 remains the R19 assignment. Posted additive Brownian-unimodality results remain excluded and earn no credit here.

The original source itself was re-opened at arXiv v2. Its Section 5.2 gives the positive classical half-stable law

\[
L_t(dx)=\frac{t}{\sqrt{2\pi}}\,x^{-3/2}e^{-t^2/(2x)}\mathbf 1_{(0,\infty)}(x)\,dx,
\tag{1.1}
\]

and Proposition 5.4 constructs an atomic initial law whose convolution with `L_t` is nonunimodal for every `t>0`, but its displayed geometric family has finite `p`-moment exactly for `p<5/2`; the paper then notes that the particular condition used there forces the `5/2` moment to diverge. Immediately afterward Conjecture 5.5 says that `S_t` may be the law of a **classical or free alpha-stable process**, assumes exactly

\[
\int_{\mathbb R}|x|^{2+\alpha}\,d\mu(x)<\infty,
\tag{1.2}
\]

and concludes eventual unimodality of

\[
\boxed{\mu*S_t}.
\tag{1.3}
\]

Thus the frozen arXiv-v2 target uses **ordinary classical convolution `*` in both branches**. I do not replace it by `\boxplus`.

The retained C010/C011 endpoint package already went much farther than the source's Proposition 5.4: a superpolynomially light one-sided kernel tail permits an atomic initial measure with **all polynomial moments** for which every scale is nonunimodal. The question in this run is whether that endpoint failure is still an artifact of (i) atoms, or (ii) merely polynomial moment control.

The answer is no on both counts.

# 2. Three new-method moves

## Move #3 — PROVE SOMETHING STRONGER

Instead of asking only for a finite `5/2` moment, or even all polynomial moments, prescribe an arbitrary countable list of tail-integrability gauges in advance. The new construction will satisfy **all of them simultaneously**. Taking the gauges to include

\[
x\mapsto e^{c x^q}
\]

for all positive rational pairs `(c,q)` yields finite `E exp(c|X|^q)` for every real `c,q>0`.

At the same time, replace the sparse atomic counterexample by a genuine `C^\infty` probability density.

## Move #15 — BREAK THE SYMMETRY ON PURPOSE

The decisive feature of the extremal half-stable kernels is not merely their tail rate. It is the hard one-sided support boundary. Around a very remote left-hand bump, every older bump and every bump on the opposite side contributes **exactly zero**, not just a small error. Only even more remote bumps can contaminate the derivative sign, and their total weight can be made negligible independently of how light the overall tail is.

The same construction is made symmetric only at the level of the initial density. For a positive one-sided kernel the left spikes do the work; reflection then gives the negative endpoint automatically.

## Move #27 — SWAP THE QUANTIFIERS

The old endpoint statements read, morally, “for each kernel find a bad initial law.” The stronger target is:

> given a **countable family of one-sided kernels** and a **countable family of tail gauges**, find **one** smooth initial law that defeats **every kernel at every scale** while satisfying **every gauge**.

The half-stable classical/free pair is then just a two-kernel corollary. A further corollary handles both stable theories for every alpha in any prescribed countable subset of `(0,1)`.

# 3. R19-I0084-C024A — countable one-sided-kernel compiler with arbitrary countable gauge control

**STATUS: PROVED INTERNALLY / AUDIT PENDING.**

Let `k_r`, `r=1,2,...`, be a finite or countable family of probability densities. Assume for each `r`:

1. there is a finite `ell_r` such that
   \[
   k_r(x)=0\qquad(x<\ell_r);
   \tag{C024.1}
   \]
2. `k_r` is `C^1` on `(ell_r,infinity)`;
3. there exist `ell_r<u_r<v_r` with
   \[
   k_r'(u_r)>0,\qquad k_r'(v_r)<0;
   \tag{C024.2}
   \]
4. for some (equivalently, after increasing the left endpoint if needed, for every) `R>ell_r`, `k_r'` is bounded on `[R,infinity)`.

For `s>0` put

\[
k_{r,s}(x)=s^{-1}k_r(x/s).
\tag{C024.3}
\]

Let `G_m:[0,infinity)->[1,infinity)`, `m=1,2,...`, be any countable family of finite-valued nondecreasing functions.

Then there exists a **symmetric `C^\infty` probability density** `g` on `R`, with unbounded support in both directions, such that

\[
\int_{\mathbb R}G_m(|x|)g(x)\,dx<\infty
\qquad\text{for every }m,
\tag{C024.4}
\]

but for every `r` and every `s>0`,

\[
\boxed{(g\,dx)*k_{r,s}\text{ is nonunimodal}.}
\tag{C024.5}
\]

Because `g` is symmetric, the same conclusion automatically holds for every reflected kernel

\[
\widetilde k_{r,s}(x)=k_{r,s}(-x).
\tag{C024.6}
\]

Translations of any kernel also preserve the conclusion, since a translation of the convolution does not affect unimodality.

## Construction of the initial density

Choose once and for all a nonnegative `C^\infty` bump `phi`, supported on `[-1,1]`, with

\[
\int_{\mathbb R}\phi(x)\,dx=1.
\]

Set

\[
A_n=n^2,
\qquad
\varepsilon_n=2^{-n-4}.
\tag{C024.7}
\]

Define

\[
H_n=\max_{1\le m\le n}G_m(A_n+1),
\qquad
q_n=\frac{2^{-n^2}}{1+H_n},
\qquad
Q=\sum_{n\ge1}q_n.
\tag{C024.8}
\]

Since every `G_m` is nondecreasing and `A_n` increases, `H_{n+1}\ge H_n`. Hence

\[
\frac{q_{n+1}}{q_n}
=2^{-(2n+1)}\frac{1+H_n}{1+H_{n+1}}
\le 2^{-(2n+1)}.
\tag{C024.9}
\]

In particular, if

\[
T_n:=\sum_{j>n}q_j,
\]

then

\[
\frac{T_n}{q_n}\longrightarrow0.
\tag{C024.10}
\]

Put

\[
\phi_{n,\pm}(x)
=\varepsilon_n^{-1}
\phi\!\left(\frac{x\mp A_n}{\varepsilon_n}\right)
\tag{C024.11}
\]

and define

\[
\boxed{
 g(x)=\frac1{2Q}\sum_{n\ge1}q_n
 [\phi_{n,+}(x)+\phi_{n,-}(x)].
}
\tag{C024.12}
\]

The bump supports escape to plus/minus infinity and are locally finite. Therefore the sum is `C^\infty` on `R`. It is visibly nonnegative, symmetric, and integrates to one.

## All prescribed gauges are integrable

Fix `m`. On the support of either `n`th bump,

\[
|x|\le A_n+1.
\]

For `n\ge m`, monotonicity gives

\[
G_m(|x|)\le G_m(A_n+1)\le H_n.
\]

Thus the `n`th pair contributes at most

\[
\frac{q_nH_n}{Q}
\le\frac{2^{-n^2}}Q.
\tag{C024.13}
\]

The series over `n\ge m` converges, and the finitely many earlier bump integrals are finite because each `G_m` is finite-valued on compact intervals. This proves (C024.4).

## Derivative sign near one remote negative bump

Fix one kernel index `r` and one scale `s>0`. Write

\[
d_r^+=k_r'(u_r)>0,
\qquad
d_r^-=-k_r'(v_r)>0.
\tag{C024.14}
\]

By continuity, there is `eta_r>0` so small that

\[
k_r'(z)\ge d_r^+/2
\quad\text{for }|z-u_r|\le\eta_r,
\tag{C024.15}
\]

and

\[
k_r'(z)\le-d_r^-/2
\quad\text{for }|z-v_r|\le\eta_r.
\tag{C024.16}
\]

Since `k_r'` is bounded on every right tail, choose a finite constant `M_r` dominating `|k_r'|` on `[u_r,\infty)` (enlarge it over a short compact interval if desired).

Consider the two test points attached to the negative bump centered at `-A_n`:

\[
x_{n,u}=-A_n+s u_r,
\qquad
x_{n,v}=-A_n+s v_r.
\tag{C024.17}
\]

For sufficiently large `n`, all of the following hold simultaneously:

1. `\varepsilon_n/s<\eta_r`;
2. for every bump centered to the **right** of `-A_n` — namely all negative bumps `-A_j` with `j<n` and **all positive bumps** `+A_j` — every normalized kernel argument at either test point lies strictly below `ell_r`; hence those contributions are exactly zero;
3. for every more-negative bump `-A_j`, `j>n`, every normalized kernel argument at either test point lies in `[u_r,\infty)`;
4. the weight tail satisfies
   \[
   M_r\frac{T_n}{q_n}
   <\frac18\min\{d_r^+,d_r^-\}.
   \tag{C024.18}
   \]

Items 2 and 3 use only

\[
A_n-A_{n-1}=2n-1\longrightarrow\infty,
\tag{C024.19}
\]

while item 4 follows from (C024.10).

At `x_{n,u}`, differentiating the convolution term-by-term is legitimate because the only nonzero terms are the `n`th bump plus the absolutely weight-summable more-negative tail on which `k_r'` is uniformly bounded. The `n`th bump contributes at least

\[
\frac{q_n}{2Q}s^{-2}\frac{d_r^+}{2}.
\tag{C024.20}
\]

The entire more-negative tail has absolute contribution at most

\[
\frac{T_n}{2Q}s^{-2}M_r.
\tag{C024.21}
\]

By (C024.18),

\[
\frac{d}{dx}[(g\,dx)*k_{r,s}](x_{n,u})>0.
\tag{C024.22}
\]

The same argument at `x_{n,v}` gives

\[
\frac{d}{dx}[(g\,dx)*k_{r,s}](x_{n,v})<0.
\tag{C024.23}
\]

Thus every sufficiently remote negative bump contains a `+` then `-` derivative transition.

## Why this forces nonunimodality

For two consecutive sufficiently large indices, the diverging gaps imply

\[
x_{n+1,u}<x_{n+1,v}<x_{n,u}<x_{n,v}.
\tag{C024.24}
\]

The derivative signs along the real line are therefore

\[
+,-,+,-.
\tag{C024.25}
\]

A differentiable unimodal density is nondecreasing to a mode and nonincreasing afterward. Its derivative cannot be negative and then later become positive. Hence (C024.25) is impossible under unimodality, proving (C024.5).

The proof fixed arbitrary `r` and arbitrary `s`; therefore one and the same `g` works for the whole countable kernel family and for every positive scale.

Finally, because `g(x)=g(-x)`,

\[
(g*\widetilde k_{r,s})(x)=(g*k_{r,s})(-x),
\]

so reflected kernels are also nonunimodal. QED.

# 4. R19-I0084-C024B — one smooth ultra-light law defeats all four alpha=1/2 endpoint source branches

**STATUS: PROVED INTERNALLY / AUDIT PENDING.**

There are two positive endpoint kernels relevant to the frozen alpha=`1/2` source case.

## Classical positive half-stable kernel

At unit scale, (1.1) gives

\[
k_{\mathrm{cl}}(x)
=\frac1{\sqrt{2\pi}}x^{-3/2}e^{-1/(2x)}\mathbf1_{(0,\infty)}(x).
\tag{C024.26}
\]

On `(0,infinity)`,

\[
\frac{k_{\mathrm{cl}}'(x)}{k_{\mathrm{cl}}(x)}
=\frac{1-3x}{2x^2}.
\tag{C024.27}
\]

Thus its unique mode is `x=1/3`, with positive derivative before `1/3` and negative derivative after it. The time-`t` law is its dilation by `s=t^2`.

## Positive free half-stable kernel, used under ordinary classical convolution

Hasebe--Simon--Wang, *Some properties of the free stable distributions* (AIHP 2020), records the explicit positive free half-stable density

\[
k_{\mathrm{fr}}(x)
=\frac{\sqrt{4x-1}}{2\pi x^2}\mathbf1_{[1/4,\infty)}(x).
\tag{C024.28}
\]

On `(1/4,infinity)`,

\[
\frac{k_{\mathrm{fr}}'(x)}{k_{\mathrm{fr}}(x)}
=\frac{2}{4x-1}-\frac2x
=\frac{2(1-3x)}{x(4x-1)}.
\tag{C024.29}
\]

So this kernel has **the same mode `1/3`** and the same derivative-sign orientation. Its free-stable semigroup changes the law by the stable scale; in the frozen source the resulting time law is then used as a kernel under **ordinary `*`**.

For both kernels choose, for example,

\[
u=\frac3{10},
\qquad
v=\frac25.
\tag{C024.30}
\]

Then

\[
k_{\mathrm{cl}}'(u)>0>k_{\mathrm{cl}}'(v),
\qquad
k_{\mathrm{fr}}'(u)>0>k_{\mathrm{fr}}'(v),
\tag{C024.31}
\]

and both derivatives are bounded on `[u,infinity)`. C024A therefore applies to the **two-kernel family simultaneously**.

Now prescribe the countable gauge family

\[
G_{a,b}(x)=e^{a x^b},
\qquad a,b\in\mathbb Q_{>0}.
\tag{C024.32}
\]

The resulting symmetric `C^\infty` probability density `g` satisfies

\[
\int_{\mathbb R}e^{a|x|^b}g(x)\,dx<\infty
\qquad(a,b\in\mathbb Q_{>0}).
\tag{C024.33}
\]

For arbitrary real `c,q>0`, choose rationals `a>c` and `b>q`. For all sufficiently large `x`,

\[
e^{c x^q}\le e^{a x^b},
\]

and the remaining compact part is harmless. Hence in fact

\[
\boxed{
\int_{\mathbb R}e^{c|x|^q}g(x)\,dx<\infty
\quad\text{for every real }c,q>0.
}
\tag{C024.34}
\]

Nevertheless, for every `t>0`,

\[
\boxed{g*L_t\text{ is nonunimodal},}
\tag{C024.35}
\]

and if `F_t` denotes the law of the positive free half-stable process at time `t`, then under the source's frozen convention

\[
\boxed{g*F_t\text{ is nonunimodal}.}
\tag{C024.36}
\]

These stars are ordinary classical convolutions.

Because `g` is symmetric, reflection gives the negative extremal skewness for **the same initial density**. Therefore one single smooth ultra-light initial law simultaneously defeats all four endpoint combinations:

1. positive classical half-stable;
2. negative classical half-stable;
3. positive free half-stable law used as an ordinary kernel;
4. negative free half-stable law used as an ordinary kernel.

This is much stronger than merely having the exact source `5/2` moment: `g` has every stretched/compressed exponential moment of every positive power.

It is important not to overstate the conclusion. The construction has unbounded support. It does **not** refute possible compact-support positive theorems, and it does not say one unbounded law can integrate literally every conceivable tailor-made gauge. What it proves is the sharp quantifier statement C024A: **any prescribed countable menu of finite monotone tail gauges can be beaten simultaneously.**

# 5. R19-I0084-C024C — one law can defeat countably many one-sided stable indices at once

**STATUS: PROVED INTERNALLY from C024A plus retained stable-density shape facts / AUDIT PENDING.**

The countable-kernel formulation is not cosmetic. Let `A` be any countable subset of `(0,1)`. For every `alpha in A`, include in the kernel family:

- the positive classical strictly `alpha`-stable time-one density;
- the positive free strictly `alpha`-stable time-one density.

The classical positive stable density is supported on a right half-line, has a strict interior mode, and has bounded derivative on every right tail; the repaired classical bell-shape input is recorded in C021. The positive free stable densities have right-half-line support and are whale-shaped; Hasebe--Simon--Wang proves this one-sided shape property. Hence each kernel satisfies C024A.

Using the same stretched-exponential gauge list (C024.32), C024A produces **one symmetric smooth initial density** `g_A` satisfying (C024.34) and such that, for every `alpha in A`, every time `t>0`, both the classical and free positive endpoint laws (the latter still under ordinary classical convolution) give nonunimodal convolutions. By symmetry, the same `g_A` also defeats both reflected negative endpoints.

In particular, taking

\[
A=\mathbb Q\cap(0,1)
\tag{C024.37}
\]

produces one smooth ultra-light initial distribution that breaks every rational one-sided stable index in both theories at every time.

I do **not** extend this countable diagonal statement to all uncountably many alpha without a separate uniform-in-alpha argument. The countable result is what C024A proves.

# 6. What changed conceptually

The retained endpoint result C010 used the fact that one kernel tail was smaller than every polynomial. That still forced the construction to balance a small but nonzero contamination term against sparse weights.

C024 identifies a stronger geometric mechanism available for genuinely one-sided kernels:

\[
\boxed{\text{support boundary }\Longrightarrow\text{ contamination from every bump to the right is exactly zero}.}
\]

Once this exact zero replaces a tail estimate, the spike weights no longer need a polynomial lower bound. They can be made as small as needed to satisfy any prescribed countable collection of tail integrability requirements. Smoothing each atom into a microscopic `C^\infty` bump does not destroy the mechanism because the support gaps diverge and the bump widths tend to zero.

For alpha=`1/2` this shows that failure of Conjecture 5.5 at extremal skewness is **not** a heavy-tail pathology of the initial law and **not** an atomic pathology. The obstruction survives an initial density much lighter than any fixed stretched/compressed exponential scale.

# 7. Prior-art and current-literature check, 2026-09-20

The original arXiv-v2 source was inspected directly again, including Section 5.2 and Conjecture 5.5. The source itself already contains two conceptually nearby facts that must be acknowledged:

- its Proposition 5.4 uses sparse atoms to defeat the positive classical half-stable kernel below the `5/2` moment threshold;
- much earlier in the paper, its free-Brownian theorem constructs, for an arbitrary prescribed Borel tail gauge, an initial distribution that prevents large-time free-Brownian unimodality. Thus “arbitrarily light bad initial tails” is not a new philosophy in this literature.

What is new **inside this repository's I0084 chain** is the combination of one-sided support, smooth initial density, simultaneous classical/free half-stable failure, and countable-gauge/countable-kernel diagonalization.

Fresh bounded searches were run for:

- `Hasebe Ueda Conjecture 5.5 stable unimodality convolution`;
- `stable convolution smooth density nonunimodal every time sparse atoms`;
- `positive free stable alpha 1/2 density sqrt(4x-1) mode`;
- `stretched exponential stable convolution unimodality counterexample`;
- later Hasebe/Ueda publications and related free-stable shape work.

The search recovered the original Hasebe--Ueda paper, Hasebe--Kuznetsov's free-stable paper, Hasebe--Simon--Wang's 2020 one-sided free-stable density/shape paper, and later Hasebe--Ueda work on multiplicative unimodality. I did not locate a later primary theorem stating C024 or resolving the exact frozen arXiv-v2 ordinary-`*` Conjecture 5.5. This is **bounded negative search evidence only**, not a novelty or priority certificate.

No exact finite claim was introduced in C024, so no arithmetic checker was manufactured. The validation object is the full analytic proof above, consistent with the 90/10 rule.

# 8. Audit state and scheduler/model-control state

The required frozen-package audit gate is still not filled. Repository search again finds:

- `R18-AUDIT-R19-I0084-C008-ABSTRACT-003 = PASS_FULL_MATHEMATICAL_PROOF` for the abstract positive smoothing engine;
- narrower historical classical-half-stable / C010 checks;
- a P26 PASS explicitly scope-gated to the **published ALEA free-`boxplus` branch**, not to the frozen arXiv ordinary-`*` package.

I did **not** locate a version-matching P26 end-to-end PASS for the frozen arXiv ordinary-`*` package, nor a distinct second end-to-end frozen-package PASS. C021--C024 also await theorem-level independent audit. Therefore the honest repository status remains `PARTIAL / AUDIT_PENDING` even though the source statement is mathematically refuted internally.

The model-control limitation is also unchanged in the currently documented interface. `RESULTS.md` and `operations/FOLLOWUP_IMPLEMENTATION_2026-09-16.md` record that the native scheduler exposes prompt/title, timing/schedule and ordinary task controls, but **no binding model-family selector, no binding reasoning-effort selector, no authenticated applied-model/effort receipt, and no guaranteed full-hour execution setting**. GPT-6/maximum therefore remains a prompt request rather than an enforceable or attestable runtime setting here.

The same follow-up manifest records the historical P26 update denial `You cannot modify this task`. A later authorized context succeeded in updating P26, so the supported remedy is to operate from the owning/authorized context, repair/transfer permissions through supported controls, or escalate to platform support. There is no legitimate bypass, and this worker made no scheduler or permission changes.

# 9. Structured ledger delta

```yaml
ledger_delta:
  track: R19
  lane: CLOSABLE_OUTSIDE
  source: "Takahiro Hasebe and Yuki Ueda, arXiv:1710.08240v2, Conjecture 5.5 / I0084"
  source_version_scope: "frozen arXiv v2: ordinary classical convolution mu*S_t for both classical-stable and free-stable kernel laws; original skewness conventions retained"
  fixed_metric: "number of complete classical-stable/free-stable alpha=1/2 source cases proved"
  metric_before: "2/2"
  metric_after: "2/2"
  metric_movement: "NO MOVEMENT"
  status: "PARTIAL / AUDIT_PENDING; source statement already REFUTED MATHEMATICALLY internally because extremal skewness is allowed"
  substantive_stagnation_this_run: 0
  tried_moves: [3, 15, 27]
  previous_triple: [5, 12, 29]
  new_claims:
    - "C024A: countable right-half-line kernel family + countable monotone gauge family -> one symmetric C-infinity initial density satisfying every gauge and defeating every kernel at every scale; reflections also defeated"
    - "C024B: one symmetric C-infinity initial density with finite integral exp(c|x|^q) for every c,q>0 makes ordinary convolution nonunimodal at every time for positive/negative classical and free alpha=1/2 endpoint stable laws"
    - "C024C: for any countable A subset (0,1), one such density simultaneously defeats both classical/free one-sided endpoint families for every alpha in A and all times"
  evidence:
    - "arXiv:1710.08240v2 Section 5.2 formula (5.27), Proposition 5.4, Conjecture 5.5 formula (5.43) and literal ordinary-* conclusion"
    - "Hasebe-Simon-Wang, AIHP 2020: explicit free alpha=1/2 density sqrt(4x-1)/(2*pi*x^2) on [1/4,infinity), plus one-sided whale-shape theorem"
    - "latest R19 C023 report and formula erratum preserved"
    - "exact C023-to-prewrite-head comparison: 161 commits ahead, 0 behind; no later R19 theorem report in changed paths"
  audit_ids:
    c008: "R18-AUDIT-R19-I0084-C008-ABSTRACT-003=PASS_FULL_MATHEMATICAL_PROOF"
    frozen_package_p26: "NOT_LOCATED / version-matching end-to-end gate unfilled"
    frozen_package_second: "NOT_LOCATED / distinct end-to-end gate unfilled"
    c024: "SELF-PROOF ONLY / INDEPENDENT AUDIT PENDING"
  remaining_obligation:
    - "independent theorem-level audit of C021--C024, especially the frozen ordinary-* convention and the countable-kernel derivative argument"
    - "P26 frozen-arXiv ordinary-* end-to-end PASS"
    - "one distinct OTHER-track frozen-arXiv ordinary-* end-to-end PASS"
  posted_exclusions:
    - "posted additive Brownian/free-Brownian unimodality work earns no new credit"
    - "known stable special cases earn no new fixed-metric credit"
  model_runtime: "GPT-5.6 Sol; reasoning UNVERIFIED; not GPT-6 maximum"
```
